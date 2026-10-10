expected_id = ""
coupon = ["SAVE10", "VIP20"]
n_coupon = "NONE"
c = []
saved_order = []
N = 0
A = 0
R = 0
T = 0
G = 0
P = 0

for attempt in range(100):
    N += 1
    a = input("Enter order details: ")
    raw = a.strip()
    upper = raw.upper()

    if upper == "QUIT":
        print("REPORT| ","N = ", N, "| A = ", A, "| R = ", R, "| T = ", T, "| G = ", G, "| P = ", P)
        break
    if upper == "REPORT":
        print("REPORT| ","N = ", N, "| A = ", A, "| R = ", R, "| T = ", T, "| G = ", G, "| P = ", P)
        print("Saved Orders: ", saved_order)
        break

    if N >= 100:
        print("REPORT| ","N = ", N, "| A = ", A, "| R = ", R, "| T = ", T, "| G = ", G, "| P = ", P)
        break

    parts = raw.split("|")
    parts[0] = parts[0].strip('"')
    parts[1] = parts[1].strip('"')
    parts[2] = parts[2].strip('"')
    parts[3] = parts[3].strip('"')
    parts[4] = parts[4].strip('"')

    if len(parts) != 5:
        print("E_FORMAT")
        R += 1
        continue

    parts[0] = parts[0].upper()
    parts[4] = parts[4].upper()

    if len(raw) > 120:
        print("E_LENGTH")
        R += 1
    elif raw.count("|") != 4:
        print("E_FORMAT")
        R += 1
    elif any(part.strip() == "" for part in raw.split("|")):
        print("E_EMPTY")
        R += 1
    elif not (len(parts[0]) == 6 and parts[0].startswith("OD")):
        print("E_ID")
        print(parts[0])
        R += 1
    elif not (len(parts[1]) == 10 and parts[1].isdigit() and parts[1].startswith("0")):
        print("E_PHONE")
        R += 1
    elif not (parts[2].isdigit() and int(parts[2]) > 0 and int(parts[2]) < 100):
        print("E_QUANTITY")
        R += 1
    elif not (parts[3].isdigit() and len(parts[3]) <= 8 and int(parts[3]) > 0 and int(parts[3]) < 10000000):
        print("E_PRICE")
        R += 1
    elif parts[4] not in coupon and parts[4] != n_coupon:
        print("E_COUPON")
        R += 1
    elif parts[0] in c:
        print("E_DUP")
        R += 1
    else:
        c.append(parts[0])
        price = int(parts[3])
        qty = int(parts[2])
        subtotal = price * qty
        discount = 0

        if parts[4] == "SAVE10":
            if subtotal >= 200000:
                discount = min(subtotal * 10 / 100, 200000)
                if discount >= 50000:
                    print("E_RULE")
                    R += 1
                    c.pop()
                    continue
        elif parts[4] == "VIP20":
            if subtotal >= 500000:
                discount = min(subtotal * 20 / 100, 500000)
                if discount >= 100000:
                    print("E_RULE")
                    R += 1
                    c.pop()
                    continue

        amount_paid = subtotal - discount
        T += subtotal
        G += discount
        P += amount_paid
        A += 1
        saved_order.append(parts[0])
        print("ACCEPTED| ", parts[0], "| ", parts[1], "| ", parts[2], "| ", parts[3], "| ", parts[4], "| ", amount_paid)
        print(c, saved_order, T, G, P)

