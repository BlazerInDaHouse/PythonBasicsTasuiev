input_word = input("Введіть слово чи фразу: ")
output_word = input_word.replace(" ", "").lower()
if output_word == output_word[::-1]:
    result = True
else:
    result = False
print(result)
