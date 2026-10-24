## Bug Hypothesis Verification Tracking

### Bug ID 01: Core Loop Stream Count Leak
* **Hypothesis/Cause:** The primitive data system implementation evaluated stream allocations using a hardcoded `for attempt in range(100)` statement block. If an enterprise data interface processed 100 invalid rows consecutively, the routine exited immediately, failing to fulfill strict baseline specifications.
* **Fix & Verification Method:** Replaced the index loop configuration blocks with a standard unbound loop framework (`while True`), governed exclusively by structural balance comparisons against current total order updates ($N = A + R \ge 100$).
* **Related Test Reference:** Case `T25` and `T26` evaluations confirming structural operations persist across variable-length command rows.

### Bug ID 02: Floating Point Float Distortions in Balance Outputs
* **Hypothesis/Cause:** Applying raw fractional math structures (`discount = subtotal * rate / 100`) introduced float types to total currency records. This caused monetary indicators to display trailing components (e.g., `G=20000.0`), violating strict integer constraints.
* **Fix & Verification Method:** Updated math logic routines to utilize floor arithmetic division operators (`// 100`), ensuring processing matrices maintain pure integer tracking.
* **Related Test Reference:** Case `T19` verified against precise scalar boundary thresholds.

### Bug ID 03: State Corruption via Premature Metric Assignment
* **Hypothesis/Cause:** Financial summary values were added to total counters (`T += subtotal`) *before* checking downstream validation rules (like duplicate matching algorithms or exception limits). This meant that even if an order was rejected late in the validation process, its value had already permanently corrupted the global counts.
* **Fix & Verification Method:** Restructured the program flow to evaluate every validation rule first. State totals are now updated only at the very end of the execution block, right before printing the `ACCEPT` message.
* **Related Test Reference:** Case `T02` and `T28` duplicates are blocked correctly without inflating global financial fields.
