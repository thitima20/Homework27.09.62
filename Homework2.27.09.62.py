"""
แม่ค้าขายผลไม้ไป 20.50 กิโลกรัม ราคากิโลกรัมละ 10.25 บาท เอาเงินที่ขายได้ไปซื้อส้มโอ 
ราคาผลละ 12.50 บาท แม่ค้าจะซื้อส้มโอได้ประมาณกี่ผล *กำหนดให้ได้ส้มโอ 7 ผล*
"""
A = float(input("selling fruit to:"))
B = float(input("price per kilogram:"))
C = float(input("grapefruit price:"))
money = A*B
count = int(money // C)
print(" will get about grapefruit ",count, "grapefruit")
if count < 2:
    print("can not bay")
elif count > 20:
    print("over demand")
else:
    count == 7
    print("complete")