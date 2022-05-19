def simple_find_interest(p1, r1, t1):
    s_interest = (p1 * r1 * t1) / 100
    total_amount = p1 + s_interest
    return s_interest, total_amount


def compound_find_interest(p2, r2, t2):
    c_interest = p2 * (pow((1 + r2 / 100), t2))
    total_amount = p2 + c_interest
    return c_interest, total_amount

def find_prime_number(payload):
    start = payload["start"]
    stop = payload["stop"]
    prime_lst = []
    for val in range(start, stop):
        if val > 1:
            for i in range(2, val):
                if (val % i) == 0:
                    break
            else:
                print(val, end=" ")
                prime_lst.append(val)
    return prime_lst
