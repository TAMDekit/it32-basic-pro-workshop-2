#งาน2
Name = input("กรุณากรอกชื่อของคุณ: ")
Age = int(input("กรุณากรอกอายุของคุณ: "))
Height = float(input("กรุณากรอกส่วนสูงของคุณ (เมตร): "))
Power = int(input("พละกำลัง: "))
StarterPackDollar = float(input("Starter Pack Dollar: "))
if Power >= 9:
    print("ผ่านคัดกรองครับ")
elif Power < 9:
    print("ไม่ผ่านคัดกรองครับ")
else:
    print("กรอกแค่ 1-10 เท่านั้นครับ")
