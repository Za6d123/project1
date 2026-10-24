
## 1. Problem Description
The Retail Order Validator is a simple terminal tool that cleans and double-checks sales orders before they go through. It easily catches things like typos, broken phone numbers, weird quantities, or invalid order IDs, and it automatically figures out coupon discounts on the fly without slowing down your system or wasting memory.
## 2. How to Run
Ensure you have Python 3 installed. Run the validator from a fresh terminal session using the following command:
```bash
python main.py
```

## 3. Input Format
Orders are read sequentially via standard input. Each transaction record must be a single line containing exactly 5 fields isolated by 4 pipe characters (`|`):
```text
Order_ID | Phone_Number | Quantity | Unit_Price | Coupon_Code
```
*Example input line:* `OD0001|0901234567|2|100000|SAVE10`

## 4. Operational Commands
* `REPORT`: Displays current real-time financial tracking figures (`N` total inputs evaluated, `A` accepted orders count, `R` rejected count, `T` cumulative subtotal gross, `G` total discount grants distributed, and `P` net balance payment expected). This does not modify the structural or computational session state.
* `QUIT`: Formats and displays the final session state line summary matrix and immediately exits the terminal interface routine loop safely.

## 5. System Error Codes & Prioritization Matrix
1. `E_LENGTH`: Total individual command input line strictly exceeds 120 character limits.
2. `E_FORMAT`: Character structure does not contain exactly 4 boundary pipe (`|`) splitters.
3. `E_EMPTY`: Any data field resolves to blank or void spaces after removing outer string padding.
4. `E_ID`: The order identity token is structural code invalid (must be 6 alphanumeric tokens starting with `OD`).
5. `E_PHONE`: Phone string fails ASCII numerical pattern or does not align with the 10-character `0` prefix pattern.
6. `E_QUANTITY`: Total order quantity does not map into the strict bounds requirement (\(0 < \text{Qty} < 100\)).
7. `E_PRICE`: Unit price fails numerical criteria or spans outside defined ranges (\(0 < \text{Price} < 10000000\)).
8. `E_COUPON`: The provided string token is unrecognized within active validation systems.
9. `E_RULE`: Coupon conditions are verified but transaction metrics fail to reach minimum value thresholds.
10. `E_DUP`: Order identification token matches a transaction sequence historically logged as `ACCEPT` in the active run.

## 6. Execution Examples
### Input Sequence
```text
OD0001|0901234567|2|100000|SAVE10
OD0001|0901234567|2|100000|SAVE10
REPORT
QUIT
```
### Output Sequence
```text
ACCEPT|OD0001|T=200000|G=200000|P=0
REJECT|E_DUP|Ma don hang da ton tai trong phien
REPORT|N=2|A=1|R=1|T=200000|G=200000|P=0
REPORT|N=2|A=1|R=1|T=200000|G=200000|P=0
```

## 7. Operational Limitations
* State arrays are memory-capped at a cumulative total threshold capacity of 100 system evaluations ($N \ge 100$).
* No backing state file persistence is supported; transaction histories clear entirely at session teardown.
* Text evaluation parameters are localized to Vietnamese translation feedback codes inside terminal layers.

## 8. Submitted Session Identifiers
* **Commit ID:** `e9c1d428bf937a09141f237efb04b9012a67f12c`
