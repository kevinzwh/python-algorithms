def even_fibonacci_sum(first=1, second=2, values=[], upper_limit=4000000):
    if first % 2 == 0:
        values.append(first)
    new_second = first + second
    if new_second > upper_limit:
        values.append(second)
        return sum(values)
    return even_fibonacci_sum(second, new_second)

print(even_fibonacci_sum())
