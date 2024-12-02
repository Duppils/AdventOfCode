def parse_file(my_file_path: str) -> tuple[list[int], list[int]]:
    with open(my_file_path, "+r") as input:
        lines = input.readlines()

    a = []
    b = []
    for line in lines:
        tmp_a, tmp_b = line.split()
        a.append(int(tmp_a))
        b.append(int(tmp_b))

    return a, b


def calculate(a: list[int], b: list[int]) -> int:
    a.sort()
    b.sort()

    total_distance = 0
    for i in range(0, len(a)):
        distance = abs(a[i] - b[i])
        total_distance += distance

    return total_distance
