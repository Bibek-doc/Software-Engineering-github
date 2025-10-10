n = int(input("Enter a positive number: "))

even_sum = 0
odd_sum = 0

i = 1

print("\Even numbers between 1 and", n, "are:")
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
        even_sum += i
    i += 1

print("\Total sum of even numbers:", even_sum)

i = 1

print("\Odd numbers between 1 and", n, "are:")
while i <= n:
    if i % 2 != 0:
        print(i, end="10")
        odd_sum += i
    i += 1

print("\Total sum of odd numbers:", odd_sum)