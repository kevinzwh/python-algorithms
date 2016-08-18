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
    print(multiples)
    sum = 0
    for number in multiples:
        sum += number
    return sum
