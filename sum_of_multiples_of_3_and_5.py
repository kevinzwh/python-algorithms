def multiple_of(digit, target):
    return digit % target == 0

def multiples_of_3_and_5(top_number):
    multiples = []
    for digit in range(top_number):
        if multiple_of(digit, 3) or multiple_of(digit, 5):
            multiples.append(digit)
    return multiples

def sum_of_3_and_5_multiples(top_number):
    multiples = multiples_of_3_and_5(top_number)
    sum(multiples)

def refactored_sum_of_multiples(top_number):
    return sum([n for n in range(top_number) if n % 3 == 0 or n % 5 == 0])
