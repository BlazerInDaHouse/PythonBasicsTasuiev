def check_south_presence(phrase):
    if "Південь" in phrase or "південь" in phrase:
        return True
    else:
        return False
user_input = input("Введіть фразу: ")

result = check_south_presence(user_input)
print(result)
