def solve(path):
    with open(path, "r") as f:
        count = 0
        for line in f:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith('#'):
                count += 1
        return count
