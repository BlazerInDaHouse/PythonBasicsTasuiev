#Перший варіант вирішення задачі

input_phrase = input("Введіть фразу: ")

length_of_phrase = len(input_phrase)

print(f"Фраза '{input_phrase}' має довжину {length_of_phrase} символів.")

#Другий варіает вирішення задачі

input_phrase = input("Введіть фразу: ")

length_of_phrase = len(input_phrase)

result_string = "має" if length_of_phrase > 0 else "не має"

print("Фраза '{}' {} довжину {} символів.".format(input_phrase, result_string, length_of_phrase))
