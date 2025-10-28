
# def measure_time(func):
    
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return True
    return True

def prime_generator(n):
    count = 0
    num = 2
    while count<n:
        if is_prime(num):
            yield num
            count += 1
        num += 1