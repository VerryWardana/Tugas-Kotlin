'''
nama = input("masukkan nama anda:")
Tinggi = float(input("masukkan tinggi badan anda dalam (cm): "))/100
Berat = float(input("masukkan berat badan anda (kg): "))
bmi = Berat/Tinggi**2

if bmi < 18.5: 
    print("BMI anda Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("BMI anda Normal weight")
elif bmi >= 25.0 and bmi <= 29.9:
     print("BMI anda Overweight")
elif bmi >= 30.0 and bmi <= 34.9:
    print("BMI anda Obesity class 1")
elif bmi >= 35.0 and bmi <= 39.9:
    print("BMI anda Obesity class 2")
elif bmi >= 40:
    print("BMI anda Obesity class 3")
else:
    print("Masukkan tinggi/berat anda dengan benar")
'''

nama = input("masukkan nama anda:")
Tinggi = float(input("masukkan tinggi badan anda dalam (cm): "))/100
Berat = float(input("masukkan berat badan anda (kg): "))
bmi = Berat/Tinggi**2

if bmi < 18.5: 
    print("BMI anda Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("BMI anda Normal weight")
elif bmi >= 25.0 and bmi <= 29.9:
     print("BMI anda Overweight")
elif bmi >= 30.0 and bmi <= 34.9:
    print("BMI anda Obesity class 1")
elif bmi >= 35.0 and bmi <= 39.9:
    print("BMI anda Obesity class 2")
elif bmi >= 40:
    print("BMI anda Obesity class 3")
else:
    print("Masukkan tinggi/berat anda dengan benar")




    