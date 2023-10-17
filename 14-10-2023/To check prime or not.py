def prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, (number//2), 1):
            if number % i == 0:
                return False
        return True

n = int(input())
if prime(n):
    print("yes")
else:
    print("no")

