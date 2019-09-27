"""
ในการเทคอนกรีตพื้นห้องกว้าง 4.25 เมตร ยาว 15.50 เมตร เสียค่าใช้จ่ายตารางเมตรละ 300 บาท
อยากทราบว่าจะต้องเสียเงินในการเทคอนกรีตทั้งหมดกี่บาท
"""
wide  = float(input("wide = "))
long  = float(input("long  = "))
po   = int(input("po = "))
mix   = wide * long
print("area",mix, "square mater")
pay = mix * po 
print("pay","bath")