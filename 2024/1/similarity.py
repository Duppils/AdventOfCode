def parse_file(my_file_path: str) -> tuple[list[int], dict]:
    with open(my_file_path, "+r") as input:
        lines = input.readlines()

    numbers = []
    similarity_mult = {}
    for line in lines:
        tmp_a, tmp_b = line.split()
        numbers.append(int(tmp_a))
        tmp_b = int(tmp_b)
        similarity_mult[tmp_b] = similarity_mult.get(tmp_b, 0) + 1

    return numbers, similarity_mult


def calculate(numbers: list[int], similarity_mult: dict) -> int:
    similarity_score = 0
    for number in numbers:
        similarity_score += similarity_mult.get(number, 0) * number

    return similarity_score
