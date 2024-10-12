# سوال 1: عدد اول
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    pass

number = int(input("Enter a number: "))
print(is_prime(number))

# سوال 2: معکوس کردن رشته
def reverse_string(s):
    return s[::-1]
    pass

string = input("Enter a string: ")
print(reverse_string(string))

# سوال 3: مجموع اعداد در یک لیست
def sum_of_list(lst):
    return sum(lst)
    pass

numbers = [10, 20, 30, 40, 50]
print(sum_of_list(numbers))

# سوال 4: یافتن بزرگترین عدد در یک لیست
def find_max(lst):
    return max(lst)
    pass

numbers = [3, 5, 1, 9, 2]
print(find_max(numbers))

# سوال 5: فیبوناچی
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    pass

terms = int(input("Enter the number of terms Fibonacci series: "))
print(fibonacci(terms))