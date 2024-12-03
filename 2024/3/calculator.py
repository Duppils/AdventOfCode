import re


OP_PATTERN = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\)|don't\(\))")
DIGITS_PATTERN = re.compile(r"(\d{1,3})")
MUL_PATTERN = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")


def load_input(file_path: str) -> str:
    with open(file_path, "+r") as input:
        corrupt_memory = input.read()

    return corrupt_memory


def parse_operations(memory: str) -> list[str]:
    groups = re.findall(OP_PATTERN, memory)
    operations = []
    for g1, g2 in groups:
        if g1:
            operations.append(g1)
        if g2:
            operations.append(g2)

    return operations


def calc_operations(operations: list[str]) -> int:
    should_mul = True
    total = 0
    for op in operations:
        if op == "don't()":
            should_mul = False
        elif op == "do()":
            should_mul = True
        elif should_mul:
            a, b = list(map(int, re.findall(DIGITS_PATTERN, op)))
            total += a * b

    return total


if __name__ == "__main__":
    corrupt_memory = load_input("secret_input.txt")
    operations = parse_operations(corrupt_memory)
    total = calc_operations(operations)
    print(f"Total sum: {total}")
