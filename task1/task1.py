import math


def is_input_valid(end: str) -> bool:
    if not end.isdigit():
        return False
    return True


def is_prime_number(number: int) -> bool:
    for divider in range(2, math.floor(math.sqrt(number)) + 1):
        if number % divider == 0:
            return False
    return True


def find_prime_numbers(n: int) -> list[int] | None:
    prime_numbers = list()
    # 1 - не является натуральным, поэтому ее не проверяем
    for number in range(2, n + 1):
        if is_prime_number(number):
            prime_numbers.append(number)

    return prime_numbers


# while True:
#     n = input()
#
#     if not is_input_valid(n):
#         print("Введенное значение некорректно")
#     else:
#         print(find_prime_numbers(int(n)))
