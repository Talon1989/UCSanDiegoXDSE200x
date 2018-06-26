import math


def euler(times=100):
    num = 0
    for n in range(times):
        num += 1/math.factorial(n)
    return num


def euler2(times=100):
    return (1+1/times) ** times


# print(euler(times=2000))
print(euler2(times=9999999))


