"""
ปลาบ่อหนึ่งมีจำนวน 60 ตัว ตาย 0.5 ของปลาทั้งหมด จงหาปลาที่ตาย
"""
count = int(input("total namber of fish : "))
dead = input("dead : ")
f = round(int(count) *float(dead))
print("dead",f,"fish")