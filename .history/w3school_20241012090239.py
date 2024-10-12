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

