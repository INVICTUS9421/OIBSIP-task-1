print("----------BMI Calculator----------")
weight = int(input("Enter weight(in kg): "))
height = int(input("Enter height(in cm): "))
bmi = int((weight/(height^2))*100)
#print(bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi <= 29.9:
    print("Overweight")
elif 30 <= bmi <= 34.9:
    print("Obesity I")
elif 35 <= bmi <= 39.9:
    print("Obesity II")
elif bmi >= 40:
    print("Obesity III")
