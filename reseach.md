# Research Data & Structural Framework

## 1. Traceable Research Sources (02 Sources)
1. *Bách Hóa Xanh (Retail Grocery Chain — bachhoaxanh.com)* - We studied their store cashier checkout flow and sales invoices. From this business, we gathered standard retail rules like setting item quantity limits between 1 and 99 to prevent bulk-buying errors, and enforcing pricing structures using Vietnamese Dong (VND).
2. *Thế Giới Di Động (E-Commerce Platform — thegioididong.com)* - We researched their public online cart data ingestion page. From this company, we extracted data validation patterns such as requiring customer phone numbers to be exactly 10 digits starting with a `0`, and capping promotional coupon values to protect business profit margins.

## 2. The 08 Raw-Data Samples (08 Raw Samples)
*Examples of raw order streams found at real store cash registers before cleaning:*
1. `OD0001|0901234567|2|120000|SAVE10` -> Normal good order.
2. `  od0002  |0912345678|01|500000|VIP20` -> Order with bad spaces to test cleaning.
3. `OD0003|0987654321|1|150000|SAVE10` -> Order that did not spend enough money for the code.
4. `OD0004|0922334455|0|75000|NONE` -> Bad quantity (cannot be 0).
5. `OD0005|0933445566|1|12500000|NONE` -> Bad price (too expensive, over limit).
6. `OD0006| |1|50000|NONE` -> Bad line with an empty missing field.
7. `OD0007|1901234567|1|60000|NONE` -> Bad phone number (does not start with 0).
8. `OD0001|0901234567|2|120000|SAVE10` -> Order using a duplicate ID that was already taken.

## 3. Data Dictionary
*Mapping real-world retail fields directly to our system variables:*

| Real-World Field Name | Code Variable | Data Type | Value Constraints & Formats |
| :--- | :--- | :--- | :--- |
| Order ID (Mã đơn hàng) | `parts[0]` | String | Exactly 6 characters, uppercase, starts with "OD". |
| Phone Number (Số điện thoại) | `parts[1]` | String | Exactly 10 ASCII numbers, must start with "0". |
| Item Quantity (Số lượng) | `parts[2]` | Integer | Numerical digits only, range must be between 1 and 99. |
| Unit Price (Đơn giá) | `parts[3]` | Integer | Digits only, max 8 characters long, value < 10,000,000 VND. |
| Coupon Token (Mã giảm giá) | `parts[4]` | String | Uppercase token, must match the active rules array or be "NONE". |

## 4. 08 Business Logic Rules (08 Rules)
1. **Line Length Check:** Drops rows instantly if they contain over 120 total characters.
2. **Pipe Separator Check:** Makes sure there are exactly 4 pipe dividers (`|`) in the input stream line.
3. **Empty Field Check:** Blocks fields that are left empty or filled with blank padding spaces.
4. **Order ID Format Check:** Confirms the ID is exactly 6 letters long, starting with the characters `OD`.
5. **Phone Format Check:** Confirms the telephone string has exactly 10 digits and begins with a `0`.
6. **Quantity Bounds Check:** Confirms the item volume count is structured between 1 and 99.
7. **Price Bounds Check:** Confirms the item cost price is positive and sits underneath 10,000,000 VND.
8. **Minimum Spend Check:** Checks if the order subtotal is high enough to pass a coupon's activation threshold.

## 5. Decision Rules Matrix (Decision Table)

| Conditions to check | Rule 1 | Rule 2 | Rule 3 | Rule 4 | Rule 5 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Is text stream over 120 characters long? | **Yes** | No | No | No | No |
| Are there exactly 4 pipe characters? | — | **No** | Yes | Yes | Yes |
| Is any metadata field empty or blank? | — | — | **Yes** | No | No |
| Is the ID structure starting with `OD`? | — | — | — | **No** | Yes |
| **System Error Code Generated** | `E_LENGTH` | `E_FORMAT` | `E_EMPTY` | `E_ID` | `PROCEED` |

## 6. Real-World Mapping Analysis
In a live commercial business environment, sales data frequently captures unwanted trailing white spaces or human errors from automated inventory scanners. This program mirrors real enterprise databases by parsing and cleaning outer string padding fields *prior* to committing calculations, while proactively dropping corrupted transaction data rows that break validation accuracy.

## 7. Mathematical Process Tables (02 Trace Tables)

### Trace Table 1: Finding Pipes in text (`raw = "OD01|091|2|50|N"`)

| Step Pointer `i` | Letter Checked | Pipes Found | `p0` Index | `p1` Index | `p2` Index | `p3` Index |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 'O' | 0 | -1 | -1 | -1 | -1 |
| 4 | '|' | 1 | **4** | -1 | -1 | -1 |
| 8 | '|' | 2 | 4 | **8** | -1 | -1 |
| 10 | '|' | 3 | 4 | 8 | **10** | -1 |
| 13 | '|' | 4 | 4 | 8 | 10 | **13** |

### Trace Table 2: Scanning for Old Used IDs (`c = ["OD0001", "OD0002"]`, New Target: `"OD0002"`)

| Array Element Index | Value Checked | Did it match target? | System Operational Action |
| :---: | :---: | :---: | :--- |
| `c[0]` | `"OD0001"` | No match | Continues parsing through historical memory. |
| `c[1]` | `"OD0002"` | **Match!** | Stops loops immediately and raises `REJECT\|E_DUP`. |
