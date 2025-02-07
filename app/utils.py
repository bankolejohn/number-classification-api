import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def classify_number(n: int):
    properties = ["even" if n % 2 == 0 else "odd"]
    if is_armstrong(n):
        properties.append("armstrong")

    return {
        "number": n,
        "is_prime": is_prime(n),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(n)),
        "fun_fact": f"{n} is an Armstrong number" if is_armstrong(n) else f"{n} is not an Armstrong number"
    }
