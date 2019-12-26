words = input("Input something: ").lower()
letter = input("Some element to find: ").lower()
# print(words)

letter_count = 0
for i in words:
    if i == letter:
        letter_count += 1

print(f'Number of elements "{letter}" in "{str(words)}" is: {letter_count}')



