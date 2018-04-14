def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    values = [1, 1]
    for _ in range(2, n):
        values.append(values[-1] + values[-2])
    return values
    
