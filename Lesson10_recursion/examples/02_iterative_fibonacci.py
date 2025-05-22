def fibonacci_iterative(n):
    # Обрабатываем базовые случаи: F(0) = 0, F(1) = 1
    if n <= 1:
        return n

    a = 0  # Соответствует F(0)
    b = 1  # Соответствует F(1)
    for _ in range(2, n + 1):
        next_fib = a + b
        a = b
        b = next_fib
    return b
