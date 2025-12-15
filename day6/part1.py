def main(inp):
    m, n = len(inp), len(inp[0])

    res = 0
    for col_idx in range(n):
        operation = inp[-1][col_idx]

        result = 0 if operation == "+" else 1
        for row_idx in range(m - 1):
            if operation == "*":
                result *= int(inp[row_idx][col_idx])
            else:
                result += int(inp[row_idx][col_idx])

        res += result
    print(res)


if __name__ == "__main__":
    inp = []
    with open("inp.txt") as file:
        for line in file:
            line = [i for i in line.strip().split(" ") if len(i) > 0]
            inp.append(line)

    main(inp)
