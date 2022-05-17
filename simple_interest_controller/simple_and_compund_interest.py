def simple_find_interest(p1, r1, t1):
    s_interest = (p1 * r1 * t1) / 100
    total_amount = p1 + s_interest
    return s_interest, total_amount


def compound_find_interest(p2, r2, t2):
    c_interest = p2 * (pow((1 + r2 / 100), t2))
    total_amount = p2 + c_interest
    return c_interest, total_amount
