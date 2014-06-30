def fibonacci(upper_bound):
    numbers = [1, 2]
    while numbers[-1] <= upper_bound:
        numbers.append(numbers[-1]+numbers[-2])
    return numbers

numbers = fibonacci(4000000)
even_numbers = [x for x in numbers if x % 2 == 0]
total = sum(even_numbers)
print total
