def check_prime(num):
    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
        return num, False
    else:
        print(num, "is a prime number")
        return num, True


def prime_no_btw(payload):
    num1 = payload["num1"]
    num2 = payload["num2"]
    prime_lst = []
    for num in range(payload["num1"], payload["num2"] + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
                prime_lst.append(num)
    return prime_lst



def num_add_mul_large(payload):
    num1 = payload["num1"]
    num2 = payload["num2"]
    num3 = payload["num3"]
    num4 = payload["num4"]
    addition = num1 + num2 + num3 + num4
    multiple = num1 * num2 * num3 * num4
    if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
        largest = num2
    elif (num3 >= num1) and (num3 >= num2) and (num3 >= num4):
        largest = num3
    else:
        largest = num4
    return addition, multiple, largest


def fib_series(payload):
    p = 0
    q = 1
    i = 2
    lst = [p, q]
    while i < payload["num"]:
        fibo = p + q
        lst.append(fibo)
        p = q
        q = fibo
        i += 1
    return lst

