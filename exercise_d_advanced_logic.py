# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
prev = 0
for number in numbers:
    if number == prev and number == 2:
        print(True)
    prev = number

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# numbers = [11, 6, 4, 99, 7, 11]
total = 0
ignore = False
for number in numbers:
    if number == 6: ignore = True
    if not ignore:
        total += number
    if number == 7: ignore = False

print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

# numbers = [5, 13, 2]

index_13 = -2 # index of the last element with value 13, not used as an index
total = 0
for i in range(len(numbers)):
    if numbers[i] == 13:
        index_13 = i
    if numbers[i] != 13 and i != index_13 + 1:
        total += numbers[i]

print(total)




