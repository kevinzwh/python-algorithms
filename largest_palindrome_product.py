def largest_palindrome_product():
    values = { "first": 0, "second": 0, "product": 0 }
    for first in range(1000):
        for second in range(1000):
            product = first * second
            product_string = str(product)
            if product_string == product_string[::-1]:
                if first + second > values["first"] + values["second"]:
                    values = { "first": first, "second": second, "product": product }
    return values["product"]

print(largest_palindrome_product())
