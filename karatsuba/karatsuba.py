import math

def karastuba_multiplication(base_ten_int_one: int, base_ten_int_two: int) -> int:
    # reference: https://realpython.com/python-bitwise-operators/
    
    if not(isinstance(base_ten_int_one, int)):
        try:
            base_ten_int_one = int(base_ten_int_one)
        except:
            raise not_able_to_convert_into_an_integer_exception
    
    if not(isinstance(base_ten_int_two, int)):
        try:
            base_ten_int_two = int(base_ten_int_two)
        except:
            raise not_able_to_convert_into_an_integer_exception
    
    
    if abs(base_ten_int_one) < 10 or abs(base_ten_int_two) < 10:
        return base_ten_int_one * base_ten_int_two
    
    str_one: str = str(abs(base_ten_int_one))
    str_two: str = str(abs(base_ten_int_two))
    min_len = min(len(str_one), len(str_two))
    index_to_split_one_on = len(str_one) - int(min_len / 2)
    index_to_split_two_on = len(str_two) - int(min_len / 2)
    
    (a, b) = split_string_at_index_n(str_one, index_to_split_one_on)
    (c, d) = split_string_at_index_n(str_two, index_to_split_two_on)

    ac = karastuba_multiplication(a, c)
    bd = karastuba_multiplication(b, d)
    diff = karastuba_multiplication(a+b, c+d) - ac - bd

    multiplier = max(len(str_one) - index_to_split_one_on, len(str_two) - index_to_split_two_on)
    negative_multiplier = 1
    if (base_ten_int_one < 0 and base_ten_int_two > 0) or (base_ten_int_one > 0 and base_ten_int_two < 0):
        negative_multiplier = -1

    return (ac*(10**multiplier)**2 + diff*(10**multiplier) + bd) * negative_multiplier

def split_string_at_index_n(string_in: str, n: int) -> (int, int):
    return (int(string_in[:n]), int(string_in[n:]))

class not_able_to_convert_into_an_integer_exception(Exception):
    "One of the parameters cannot be converted into an integer"
    pass

