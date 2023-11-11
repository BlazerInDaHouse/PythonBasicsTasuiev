age_str = input("Скільки вам років?")
age = int(age_str)
if age >= 18:
    print("Ви повнолітні")
elif age <= 0:
    print("Ви ще не народились")
else:
    print("Ви неповнолітні")