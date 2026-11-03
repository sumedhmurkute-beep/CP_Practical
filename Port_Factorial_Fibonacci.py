def factorial(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n must be a non-negative integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def combination(n: int, r: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError("n and r must be non-negative integers with r <= n.")
    if not isinstance(r, int) or isinstance(r, bool):
        raise ValueError("n and r must be non-negative integers with r <= n.")
    if n < 0 or r < 0 or r > n:
        raise ValueError("Invalid input: require n >= 0 and 0 <= r <= n.")
    return factorial(n) // (factorial(r) * factorial(n - r))


def fib_iter(n: int) -> list[int]:
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    sequence = []
    previous, current = 0, 1
    for _ in range(n):
        sequence.append(previous)
        previous, current = current, previous + current
    return sequence


def fib_rec(k: int) -> int:
    if not isinstance(k, int) or isinstance(k, bool) or k < 0:
        raise ValueError("k must be a non-negative integer.")
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fib_rec(k - 1) + fib_rec(k - 2)


print("Part A: Solvent combinations")
print(f"Possible mixtures for n=9, r=3: {combination(9, 3)}")

try:
    combination(6, 8)
except ValueError as error:
    print(f"n=6, r=8: {error}")

print("\nPart B: Crystallisation sampling schedule")
n = 10
fibonacci_tags = fib_iter(n)
recursive_tags = [fib_rec(sample_no) for sample_no in range(n)]

if fibonacci_tags != recursive_tags:
    raise AssertionError("Iterative and recursive Fibonacci results do not agree.")
print("Iterative and recursive Fibonacci results agree.")
print(f"{'Sample No.':>10} {'Fibonacci tag':>14} {'Sampling time (min)':>20}")
for sample_no, tag in enumerate(fibonacci_tags, start=1):
    print(f"{sample_no:10d} {tag:14d} {tag * 4:20d}")
