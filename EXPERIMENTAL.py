# Зчитування 10 слів з клавіатури
words = [input(f"Введіть слово {i + 1}: ") for i in range(10)]

# Сортування слів в алфавітному порядку
sorted_words = sorted(words)

# Зчитування 10 чисел з плаваючою зап'ятою з клавіатури
numbers = [float(input(f"Введіть число {i + 1}: ")) for i in range(10)]

# Сортування чисел з плаваючою зап'ятою за порядком зростання
sorted_numbers = sorted(numbers)

# Виведення результату
print("Слова в алфавітному порядку:", sorted_words)
print("Числа в порядку зростання:", sorted_numbers)
