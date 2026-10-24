
| Case ID | Input Data Vector String | Initial Session State | Expected Validation Result / Output | Final Structural Review Conclusion |
| :--- | :--- | :--- | :--- | :--- |
| **T01** | `OD0001\|0901234567\|2\|100000\|SAVE10` | `A=0, R=0, T=0, G=0` | `ACCEPT\|OD0001\|T=200000\|G=20000\|P=180000` | Baseline standard run accepted successfully. |
| **T02** | `OD0001\|0901234567\|2\|100000\|SAVE10` | `A=1, R=0, T=200000` | `REJECT\|E_DUP\|Ma don hang da ton tai trong phien` | Validated duplicate blocker constraint logic. |
| **T03** | `OD0002\|0901234567\|1\|500000\|VIP20` | `A=1, R=1, T=200000` | `ACCEPT\|OD0002\|T=700000\|G=120000\|P=580000` | Verified VIP20 discount evaluation bounds. |
| **T04** | `OD0003\|0911223344\|1\|500010\|VIP20` | `A=2, R=1, T=700000` | `ACCEPT\|OD0003\|T=1200010\|G=220000\|P=980010` | Verified correct application of VIP20 cap. |
| **T05** | `OD0004\|0987654321\|1\|150000\|SAVE10` | `A=3, R=1, T=1200010` | `REJECT\|E_RULE\|Chua dat gia tri toi thieu...` | Blocked coupon entry under threshold bounds. |
| **T06** | `OD0005\|0912345678\|1\|250000\|NONE` | `A=3, R=2, T=1200010` | `ACCEPT\|OD0005\|T=1450010\|G=220000\|P=1230010` | Confirmed valid NONE token execution block. |
| **T07** | `OD0006\|0922334455\|0\|50000\|NONE` | `A=4, R=2, T=1450010` | `REJECT\|E_QUANTITY\|So luong khong hop le` | Verified quantity structural lower bound. |
| **T08** | `OD0007\|0933445566\|100\|50000\|NONE` | `A=4, R=3, T=1450010` | `REJECT\|E_QUANTITY\|So luong khong hop le` | Verified quantity structural upper bound. |
| **T09** | `OD0008\|0944556677\|1\|0\|NONE` | `A=4, R=4, T=1450010` | `REJECT\|E_PRICE\|Don gia khong hop le` | Verified price structural lower boundary. |
| **T10** | `OD0009\|0955667788\|1\|10000000\|NONE` | `A=4, R=5, T=1450010` | `REJECT\|E_PRICE\|Don gia khong hop le` | Verified price structural upper boundary. |
| **T11** | `OD0010\|0966778899\|1\|50000\|INVALID` | `A=4, R=6, T=1450010` | `REJECT\|E_COUPON\|Ma giam gia khong ton tai` | Handled unrecognized coupon token entries. |
| **T12** | `AB0011\|0977889900\|1\|50000\|NONE` | `A=4, R=7, T=1450010` | `REJECT\|E_ID\|Ma don hang khong hop le` | Caught incorrect order prefix constraints. |
| **T13** | `OD01234\|0988990011\|1\|50000\|NONE` | `A=4, R=8, T=1450010` | `REJECT\|E_ID\|Ma don hang khong hop le` | Rejected incorrect order ID length spacing. |
| **T14** | `OD0012\|1901234567\|1\|50000\|NONE` | `A=4, R=9, T=1450010` | `REJECT\|E_PHONE\|So dien thoai khong dung...` | Caught incorrect phone prefix start token. |
| **T15** | `OD0013\|090123456\|1\|50000\|NONE` | `A=4, R=10, T=1450010` | `REJECT\|E_PHONE\|So dien thoai khong dung...` | Blocked short phone string distributions. |
| **T16** | `OD0014\|09012345678\|1\|50000\|NONE` | `A=4, R=11, T=1450010` | `REJECT\|E_PHONE\|So dien thoai khong dung...` | Blocked over-length phone input variations. |
| **T17** | `OD0015\|09123456a7\|1\|50000\|NONE` | `A=4, R=12, T=1450010` | `REJECT\|E_PHONE\|So dien thoai khong dung...` | Filtered alphanumeric non-digit characters. |
| **T18** | `OD0016\|0901234567\|1\|500010\|SAVE10` | `A=4, R=13, T=1450010` | `ACCEPT\|OD0016\|T=1950020\|G=270000\|P=1680020` | Assigned max boundary cap to SAVE10 token. |
| **T19** | `OD0017\|0901234567\|1\|200009\|SAVE10` | `A=5, R=13, T=1950020` | `ACCEPT\|OD0017\|T=2150029\|G=290000\|P=1860029` | Verified standard percent math boundaries. |
| **T20** | `A*121` *(121 consecutive 'A' characters)* | `A=6, R=13, T=2150029` | `REJECT\|E_LENGTH\|Dong lenh vuot qua 120...` | Prevented inputs overflowing master size buffer. |
| **T21** | `OD0018\|0901234567\|1\|50000` | `A=6, R=14, T=2150029` | `REJECT\|E_FORMAT\|Dinh dang chuoi khong...` | Discovered missing delimiter column fields. |
| **T22** | `OD0019\|0901234567\|1\|50000\|NONE\|EXTRA` | `A=6, R=15, T=2150029` | `REJECT\|E_FORMAT\|Dinh dang chuoi khong...` | Identified over-delimited structural variants. |
| **T23** | `OD0020\| \|1\|50000\|NONE` | `A=6, R=16, T=2150029` | `REJECT\|E_EMPTY\|Co truong bi bo trong` | Caught whitespace field assignments correctly. |
| **T24** | `OD0021\|\t\|1\|50000\|NONE` | `A=6, R=17, T=2150029` | `REJECT\|E_EMPTY\|Co truong bi bo trong` | Caught tab values masking empty conditions. |
| **T25** | `REPORT` | `A=6, R=18, T=2150029` | `REPORT\|N=24\|A=6\|R=18\|T=2150029...` | Verified state reporting system alignment. |
| **T26** | `REPORT` | `A=6, R=18, T=2150029` | `REPORT\|N=24\|A=6\|R=18\|T=2150029...` | Proved consecutive report states match. |
| **T27** | `  od0022  \|0911111111\|5\|20000\|save10` | `A=6, R=18, T=2150029` | `ACCEPT\|OD0022\|T=2250029\|G=300000\|P=1950029` | Tested manual trimming and capitalization maps. |
| **T28** | `OD0022\|0911111111\|5\|20000\|SAVE10` | `A=7, R=18, T=2250029` | `REJECT\|E_DUP\|Ma don hang da ton tai...` | Verified historical duplicate matching trace. |
| **T29** | `OD0023\|0922222222\|1\|150000\|WEEKEND7` | `A=7, R=19, T=2250029` | `ACCEPT\|OD0023\|T=2400029\|G=310500\|P=2089529` | Verified alternate multi-tier rule paths. |
| **T30** | `QUIT` | `A=8, R=19, T=2400029` | `REPORT\|N=27\|A=8\|R=19\|T=2400029...` | Processed graceful exit shutdown signal cleanly. |
