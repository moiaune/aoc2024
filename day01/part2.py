import os
import collections

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_FILE = os.path.join(os.path.dirname(__file__), 'example.txt')

def solve(input) -> int:
    l1, l2 = [], collections.Counter()
    for line in input.splitlines():
        n1, n2 = line.split()

        # list of left side numbers
        l1.append(int(n1))

        # count how many times a number appears in the right list
        l2[int(n2)] += 1

    # for each number in left list, multiply it by the number of times it appears in the right list
    return sum([(i * l2[i]) for i in l1])

def main() -> int:
    with open(EXAMPLE_FILE) as f:
        print(solve(f.read()))

    with open(INPUT_FILE) as f:
        print(solve(f.read()))

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
