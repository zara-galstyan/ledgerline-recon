### 1. Nork Coworking overdue?
Expected: 210,000 overdue on INV-1035. INV-1056 (480k) isn't due until 13 Sep.
Evidence: TXN-50021, 8 Sep, 260,000, no ref, so INV-1025. TXN-50042, 17 Aug, 480,000, no ref, so INV-1055.

### 2. Payments with no invoice?
Expected: TXN-50047 and TXN-50049.
Evidence: 150k from ARMEN S., who isn't a customer. 145k from Gyumri marked "refund reversal".

### 3. TXN-50010 is for?
Expected: INV-1011, matched by elimination, since the amount alone is ambiguous.
Evidence: TXN-50010, 10 Jul, 260,000, Sevan Shore, no ref. Sevan has two 260k invoices, and INV-1002 is already paid by TXN-50002 (5 Aug).

### 4. Is Hotel Ardi's INV-1060 fully paid?
Expected: No. 1,200,000 outstanding of 3,800,000.
Evidence: TXN-50044, 19 Aug, 2,600,000.

### 5. Total overdue?
Expected: 4,902,500 across 15 invoices.
Evidence: the Q6 breakdown.

### 6. Overdue per customer?
Expected: Ardi 1,320,000 · Paper Cup 1,230,000 · Sevan 735,000 · Kond 737,500 · Gyumri 340,000 · Nork 210,000 · Lusin 210,000 · Dilijan 120,000 · Cascade 0 · Aurora 0.
Evidence: due before 10 Sep and not paid in full.

### 7. Invoices past due and unpaid?
Expected: 1005 (partly paid, 307,500 left), 1007, 1009 (partly paid, 170,000 left), 1015, 1016, 1017, 1027, 1029, 1033, 1035, 1041, 1049, 1052, 1053, 1060 (partly paid, 1,200,000 left).
Evidence: due before 10 Sep and not paid in full.

### 8. Partial payments?
Expected: TXN-50005, TXN-50008 and TXN-50044.
Evidence: 307,500 of 615,000 on INV-1005. 170,000 of 340,000 on INV-1009. 2,600,000 of 3,800,000 on INV-1060.

### 9. Payment larger than its invoice?
Expected: Yes, TXN-50048, over by 20,000.
Evidence: TXN-50048, 14 Jul, 105,000 on INV-1008 (85,000).

### 10. Duplicate bank lines?
Expected: Yes, TXN-50008 and TXN-50046.
Evidence: 3 Jul, 170,000, Kond Street, "payment for coffee". Count it once, or INV-1009 looks fully paid.