import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_FILE = os.path.join(os.path.dirname(__file__), 'example.txt')

def solve(input) -> int:
    l1, l2 = [], []
    for line in input.splitlines():
        n1, n2 = line.split()
        l1.append(int(n1))
        l2.append(int(n2))

    l1.sort()
    l2.sort()

    return sum([abs(val1 - val2) for val1, val2 in zip(l1, l2)])

def main() -> int:
    with open(EXAMPLE_FILE) as f:
        print(solve(f.read()))

    with open(INPUT_FILE) as f:
        print(solve(f.read()))

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
