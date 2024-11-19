#// BEGIN_TODO [Prime_numbers] Prime numbers 
def is_prime(num: int) -> bool:
    """
    Returns True if num is a prime number or False if it isnt.
    
    :param num1: int to be checked.
    :returns: Boolean value.
    """
    n = num - 1
    while n!= 1:
        if num % n == 0:
            return False
        n -= 1
    return True
def primes(max_num: int) -> list[int]:
    """
    Returns all the numbers that are prime that are smaller than max_num.
    
    :param num1: maximum integer number
    :returns: list of all prime numbers that are smaller than max_num.
    """
    assert max_num > 1
    prime_list = list()
    for num in range(2, max_num+1):
        if is_prime(num) == True:
            prime_list.append(num)
    return prime_list
    
#// END_TODO [Prime_numbers]
print(primes(23))




