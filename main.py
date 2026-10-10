total = 0
expected_id = ""
coupon = ["SAVE10", "VIP20"]
n_coupon = "NONE"
c = []
saved_order = []

a = input("Enter order details: ")   #"OD0001|0901234567|2|100000|SAVE10"  #test
while True:
    if len(a.split("|")) != 5:
        print("WRONG FORMAT")
        a = input("Enter order details: ")
        continue
    else:
        break

if a == "QUIT":
    print("Total: ", total)
    exit()
if a == "REPORT":  
    print("Total: ", total)
    print("Saved Orders: ", saved_order)
    exit()

after = a.strip()

b = after.split("|")

b[0] = b[0].upper()
b[4] = b[4].upper()


if len(after) > 120:
    print("E_LENGTH")
elif after.count("|") != 4:
    print("E_FORMAT")
elif any(part.strip() == "" for part in after.split("|")):
    print("E_EMPTY")
elif not (len(b[0]) == 6 and b[0].startswith("OD")):
    print("E_ID")
elif not (len(b[1]) == 10 and b[1].isdigit() and b[1].startswith("0")):
    print("E_PHONE")
elif not (b[2].isdigit() and int(b[2]) > 0 and int(b[2]) < 100):
    print("E_QUANTITY")
elif not (b[3].isdigit() and len(b[3]) <= 8 and int(b[3]) > 0 and int(b[3]) < 10000000):
    print("E_PRICE")
elif b[4] not in coupon and b[4] != n_coupon:
    print("E_COUPON")
elif b[0] not in c:
    c.append(b[0])  
    if b[4] == "SAVE10":
        if min(int(b[3]), 200000) >= 200000:
            if (money * 10)/100 >= 50000:
                print("E_RULE")
            else:
                money = int(b[3]) - (int(b[3]) * 10) / 100
                total += money
    elif b[4] == "VIP20":
        if min(int(b[3]), 500000) >= 500000:
            if (money * 20)/100 >= 100000:
                print("E_RULE")
            else:
                money = int(b[3]) - (int(b[3]) * 20) / 100
                total += money
    elif b[4] == "NONE":
        money = int(b[3])
        total += money
elif b[0] in c:
    print("E_DUP")
else:
    print("ACCEPTED| ", b[0], "|", b[1], "|", b[2], "|", b[3], "|", b[4])  










