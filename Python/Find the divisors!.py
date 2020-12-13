def divisors(number):
    number = int(number)
    divisors_list = []
    [divisors_list.append(integer) for integer in range(2, number) if number % integer == 0]
    if not divisors_list:
        result = f'{number} is prime'
    else:
        result = divisors_list
    return result

