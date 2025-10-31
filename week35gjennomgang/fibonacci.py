# def fibonacci(n: int) -> int:
#     a,b = 0,1
#     for _ in range(n):
#         yield b
#         a, b = b, a+b
#
# print(list(fibonacci(20)))
#
#
# # mitt første forsøk i fjor
# fib1 = 0
# fib2 = 1
# print(fib2)
# for fibo in range(20):
#     ny_fibo = fib1 + fib2
#     print(ny_fibo)
#     fib1 = fib2
#     fib2 = ny_fibo
#
# fib = [1, 1]
# for _ in range(20):
#     # print(f"{fib[-1]} + {fib[-2]} = {fib[-1] + fib[-2]}", end=", ")
#     fib.append(fib[-1] + fib[-2])
#
# print(fib)

def fibonacci_recursive(n: int):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n -2)

print(fibonacci_recursive(5))