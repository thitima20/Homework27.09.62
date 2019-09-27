"""
ไม้ท่อนหนึ่งยาว 10.50 เมตร ส่วนที่อยู่ในโครน 2.25 เมตร
และส่วนที่อยู่ในน้ำยาว 2.50 เมตร ส่วนที่พ้นน้ำจะยาวกี่เมตร
"""
J = float(input("long : "))
O = float(input("in krone : "))
N = float(input("in the water   : "))
print("the long past ",(J-(O+N)),"m")