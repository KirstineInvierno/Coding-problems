def multiples_of_3_or_5(n: int) -> list[str]:
    number_list = []
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            number_list.append("FizzBuzz")
        elif number % 3 == 0:
            number_list.append("Fizz")
        elif number % 5 == 0:
            number_list.append("Buzz")
        else:
            number_list.append(str(number))
    return number_list


print(multiples_of_3_or_5(15))
