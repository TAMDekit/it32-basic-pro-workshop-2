# งาน1
quantity = int(input("รับมาขายกี่กระบอก: "))
cost_price = float(input("ต้นทุนของปืนที่รับมา: "))
sell_price = float(input("ราคาที่จะนำไปขายต่อ: "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน: "))

total_cost = quantity * cost_price # ต้นทุนทั้งหมด เอา รับมากกี่กระบอก * ต้นทุนปืน
total_income = quantity * sell_price # รายรับทั้งหมด มาจาก รับมากี่กระบอก * ราคาที่ขายต่อ
profit = total_income - total_cost # กำไรสุทธิ มาจาก รายรับทั้งหมด - ต้นทุนทั้งหมด
boss_share = profit * 0.20 # เงินที่หักให้บอส 20%

print("ต้นทุนทั้งหมด:", total_cost)
print("รายรับทั้งหมด:", total_income)
print("กำไรสุทธิ:", profit)
print("เงินที่หักให้บอส 20%:", boss_share)
print("จำนวนลูกน้องในทีม:", team_members)