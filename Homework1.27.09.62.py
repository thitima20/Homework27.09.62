"""
ร้านขายรองเท้าเพิ่มยอดขายโดยมีโปรโมชั่นพิเศษถ้าซื้อมากกว่า 2 คู่มีมูลค่ารวมเกิน 1000 บาท จะได้ส่วนลด 15% ลูกค้าคนแรกมาซื้อ 3 คู่ ราคา 1350 บาท คนที่สองซื้อ 1 คู่ ราคา 700 บาท แต่ละคนจะต้องจ่ายเงินกี่บาท
"""
count = int(input("How many pairs:"))
money = int(input("How much:"))
if count > 2 and money > 1000:
   x = money-money*0.15
else:
   x = money
print("You have to pay",int(x),"bath.")
