"""
We need to figure out which spaces are used for padding versus splits.


"""


def main(inp, columnLengths):
    m, n = len(inp), len(inp[0])

    res = 0
    for col_idx in range(n):
        operation = inp[-1][col_idx][0]
        result = 0 if operation == "+" else 1

        numbers = ["" for _ in range(columnLengths[col_idx])]
        for row_idx in range(m - 1):
            for idx, i in enumerate(inp[row_idx][col_idx]):
                if i != " ":
                    numbers[idx] += i

        for num_str in numbers:
            num_int = int(num_str, 10)
            if operation == "+":
                result += num_int
            else:
                result *= num_int
        print(f"Result for col_idx {col_idx}: {result}.")
        res += result
    print(res)


if __name__ == "__main__":
    inp = []

    with open("inp.txt", "r") as file:
        for line in file:
            inp.append(line.rstrip("\n\r"))

    columnCnt = len(inp[-1]) - (inp[-1].count(" "))
    columnLengths = []

    # TODO: Figure out how to parse spaces.
    #  We can parse the last row and for each symbol seen we compute the length at that point
    cnt = 0
    for idx, i in enumerate(inp[-1]):
        if i != " " and idx != 0:
            columnLengths.append(cnt - 1)
            cnt = 0
        cnt += 1
    columnLengths.append(cnt)

    n_inp = []
    for line in inp:
        s = ""
        inp_line = []
        col_idx = 0
        for i in line:
            if len(s) == columnLengths[col_idx]:
                inp_line.append(s)
                col_idx += 1
                s = ""
            else:
                s += i
        inp_line.append(s)
        n_inp.append(inp_line)

    main(n_inp, columnLengths)
