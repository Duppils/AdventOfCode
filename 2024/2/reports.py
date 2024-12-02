def safe(report: list[int]) -> bool:
    i = report[0]
    asc = report[0] < report[1]
    for j in report[1:]:
        diff = abs(i - j)
        if diff < 1 or diff > 3:
            return False
        if asc and i > j:
            return False
        elif not asc and i < j:
            return False

        i = j

    return True


def read_input(file_path: str) -> list[list[int]]:
    with open(file_path, "+r") as my_file:
        report_string = my_file.read()

    reports = [list(map(int, report.split())) for report in report_string.splitlines()]
    return reports


if __name__ == "__main__":
    reports = read_input("input.txt")
    n_safe = 0
    for report in reports:
        n_safe += int(safe(report))
    print(f"# safe reports: {n_safe}/{len(reports)}")
