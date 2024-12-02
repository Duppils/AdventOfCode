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


def ok(i: int, j: int, asc: bool = True) -> bool:
    # print(i, j, asc)
    diff = abs(i - j)
    if diff < 1 or diff > 3:
        return False
    if asc and i > j:
        return False
    elif not asc and i < j:
        return False
    return True


# NOTE: can be made simpler at the cost of running
# the entire result minus fault candidates (i,j) again.
# I wanted to skip previous elements, but not worth it
# assuming that each result continues to only a few elements.
def safe2(report: list[int], faulty=False, asc=None) -> bool:
    if asc is None:
        asc = report[0] < report[1]

    for idx, j in enumerate(report[1:]):
        i = report[idx]
        if not ok(i, j, asc=asc):
            if faulty:
                # Faulty twice is unacceptable
                return False

            if idx + 2 == len(report):
                # Skip last element implies the result is safe
                return True

            report_skip_i = []
            if idx == 0 or idx == 1:
                # If first element or second removed, reset ascending/descending
                asc = None

            is_safe = False
            if idx + 2 < len(report):
                # Skip j and elements before i (already checked).
                report_skip_j = [i] + report[idx + 2 :]
                is_safe = safe2(report_skip_j, faulty=True, asc=asc)

            if is_safe:
                return True

            # Skip i and elements before i - 1 (already checked).
            report_skip_i = []
            if idx - 1 >= 0:
                # Add previous if current idx isn't the first element
                report_skip_i.append(report[idx - 1])

            report_skip_i.extend(report[idx + 1 :])
            return safe2(report_skip_i, faulty=True, asc=asc)

    return True


if __name__ == "__main__":
    reports = read_input("input.txt")
    n_safe = 0
    for report in reports:
        n_safe += int(safe(report))
    print(f"# safe reports: {n_safe}/{len(reports)}")
