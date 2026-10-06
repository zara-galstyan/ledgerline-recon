import anthropic
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

def get_invoices(customer):
    invoices = pd.read_csv("data/invoices.csv")
    customers = pd.read_csv("data/customers.csv")
    customer = customers[customers["name"] == customer]
    return invoices[invoices["customer_id"] == customer["customer_id"].iloc[0]]

print(get_invoices("Lusin Bakery"))


def find_payments(customer, from_date, to_date):
        bank_payments = pd.read_csv("data/bank_payments.csv", parse_dates=["date"])
        filtered = bank_payments[
            (bank_payments["payer_name"].str.casefold() == customer.casefold())
            & (bank_payments["date"] >= pd.to_datetime(from_date))
            & (bank_payments["date"] <= pd.to_datetime(to_date))
        ]
        return filtered

print(find_payments("Lusin Bakery", "2026-05-05", "2026-07-27"))

tools = [
    {
        "name": "get_invoices",
        "description": "Get all invoices for a customer",
        "input_schema": {
            "type": "object",
            "properties": {
                "customer": {"type": "string", "description": "Customer name, e.g. Lusin Bakery"}
            },
            "required": ["customer"]
        }
    },
    {
        "name": "find_payments",
        "description": "Find bank payments for a customer in a date range",
        "input_schema": {
            "type": "object",
            "properties": {
                "customer":  {"type": "string", "description": "Customer name"},
                "from_date": {"type": "string", "description": "Start date, YYYY-MM-DD"},
                "to_date":   {"type": "string", "description": "End date, YYYY-MM-DD"}
            },
            "required": ["customer", "from_date", "to_date"]
        }
    }
]

messages = [{"role": "user", "content": "Which invoices does Lusin Bakery have?"}]

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    tools=tools,
    messages=messages,
)

tool_use = next(b for b in response.content if b.type == "tool_use")
print(tool_use.name, tool_use.input)          # your log line

result = get_invoices(**tool_use.input)       # your function runs

messages += [
    {"role": "assistant", "content": response.content},
    {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": tool_use.id, "content": str(result)}
    ]},
]

followup = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    tools=tools,
    messages=messages,
)

print(next(b for b in followup.content if b.type == "text").text)


# Output
# invoice_id customer_id  issue_date    due_date  amount_amd erp_status
# 3    INV-1004         C02  2026-06-04  2026-06-18      120000       open
# 17   INV-1018         C02  2026-06-28  2026-07-12      210000       open
# 45   INV-1046         C02  2026-08-04  2026-08-18       85000       open
# 50   INV-1051         C02  2026-08-09  2026-08-23      480000       open
# 52   INV-1053         C02  2026-08-11  2026-08-25      210000       open
# transaction_id       date  amount_amd    payer_name reference
# 0      TXN-50004 2026-06-16      120000  LUSIN BAKERY  INV-1004
# 6      TXN-50014 2026-07-05      210000  LUSIN BAKERY  INV-1018
# get_invoices {'customer': 'Lusin Bakery'}
# Lusin Bakery has the following invoices:
#
# | Invoice ID | Issue Date | Due Date | Amount (AMD) | Status |
# |------------|------------|----------|--------------|--------|
# | INV-1004 | 2026-06-04 | 2026-06-18 | 120,000 | Open |
# | INV-1018 | 2026-06-28 | 2026-07-12 | 210,000 | Open |
# | INV-1046 | 2026-08-04 | 2026-08-18 | 85,000 | Open |
# | INV-1051 | 2026-08-09 | 2026-08-23 | 480,000 | Open |
# | INV-1053 | 2026-08-11 | 2026-08-25 | 210,000 | Open |
#
# All 5 invoices are currently open with a total amount of **1,105,000 AMD**.

