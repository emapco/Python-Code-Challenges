from functools import lru_cache


# cache to speed up recursive function
@lru_cache(maxsize=None)
def prime_factorize(num: int):
    factors = []
    for i in range(2, num // 2):
        # identify first number the divides num evenly
        # then get the prime factors of the factor
        # and its complementary factor
        if num % i == 0:
            factors.extend(prime_factorize(i))
            factors.extend(prime_factorize(num // i))
            break

    # if for loop found no factors then number is a prime
    if len(factors) == 0:
        factors.append(num)

    return factors


def solution(num: int):
    factors = []
    divisor = 2
    while divisor <= num:
        if (num % divisor) == 0:
            factors.append(divisor)
            num = num/divisor
        else:
            divisor += 1


def main():
    # profile (best out of five): 27 ms (100%)
    # profile (worst out of five): 40 ms (100%)
    print(prime_factorize(18))
    print(prime_factorize(19))
    print(prime_factorize(630))
    print(prime_factorize(1001))
    print(prime_factorize(10003452345))

    """
    # profile (best out of five): 132 ms (100%)
    print(solution(18))
    print(solution(19))
    print(solution(630))
    print(solution(1001))
    print(solution(10003452345))
    """


if __name__ == '__main__':
    main()
