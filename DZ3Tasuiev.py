 = int(input("Введіть вік кота в кошачих роках: "))
human_age = 15  # Перший рік кота
if n == 1:
    human_age = 15
elif n > 1:
    human_age = 15 + (n - 1) * 9
print("Вік кота в людських роках:", human_age)
