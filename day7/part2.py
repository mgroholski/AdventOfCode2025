def main(inp):
    """
    We repeat computations at certain positions a lot. We'll want to perform a bottom up DP...

    we can create an array and consider from any point, if a beam was here how many unique paths are there?
    """
    m, n = len(inp), len(inp[0])
    last_row = [1 for _ in range(n)]

    for line_idx in range(m - 1, -1, -1):
        line = inp[line_idx]
        row_dp = []
        for c_idx, c in enumerate(line):
            val = 0
            if c == "^":
                if c_idx - 1 >= 0:
                    val += last_row[c_idx - 1]
                if c_idx + 1 < n:
                    val += last_row[c_idx + 1]
            else:
                val += last_row[c_idx]
            row_dp.append(val)
        last_row = row_dp

    for idx, c in enumerate(inp[0]):
        if c == "S":
            print(last_row[idx])
            return


if __name__ == "__main__":
    inp = []

    with open("test_inp.txt", "r") as file:
        for line in file:
            inp.append(line.strip())

    main(inp)
