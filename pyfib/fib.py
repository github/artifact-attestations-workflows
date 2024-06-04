import argparse

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def main():
    parser = argparse.ArgumentParser(description='Calculate the first N numbers of the Fibonacci sequence.')
    parser.add_argument('N', type=int, help='The number of Fibonacci numbers to calculate.')
    args = parser.parse_args()

    for i in range(1, args.N + 1):
        print(fibonacci(i))

if __name__ == "__main__":
    main()
