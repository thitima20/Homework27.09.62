"""
โปรโมชั่นทางร้าน ซื้ออาหารมากกว่า 2000 บาท ขึ้นไป ลดราคา 10 เปอร์เซ็น
คิดเงินค่าอาหารให้ลูกค้าโต๊ะที่ 1 รวมเงิน 470 บาท ต้องชำระเงินกี่บาท
คิดเงินค่าอาหารให้ลูกค้าโต๊ะที่ 2 รวมเงิน 2200 บาท ต้องชำระเงินกี่บาท
"""
while(True):
    Number = int(input("total = "))
    if(Number<2000):
        print("pay = ",Number,"bath")
    else:
        Number > 2000
        sale = round(Number * 0.10)
        pay  = Number - sale
        print("promotion pay = ",pay,"bath")
        break