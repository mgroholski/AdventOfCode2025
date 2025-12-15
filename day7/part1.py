def main(inp):
    """
    Process input by line.
    If it's the first line, find where S is.
    If not the first line, keep an array of the beam locations.
    If a ^ exists at that location l, create a new beam at l + 1 and l - 1 (if they're in bounds).
    """
    res = 0
    pos = set()
    first_line, inp = inp[0], inp[1:]
    m = len(first_line)

    for idx, c in enumerate(first_line):
        if c == "S":
            pos.add(idx)

    for line in inp:
        new_pos = set()
        for idx in pos:
            # print(f"Adding {idx}:")
            if line[idx] == "^":
                # print(f"    Splitting {idx}")
                res += 1
                if idx - 1 not in new_pos and idx - 1 >= 0:
                    new_pos.add(idx - 1)
                if idx + 1 not in new_pos and idx + 1 < m:
                    new_pos.add(idx + 1)
            elif line[idx] == ".":
                # print(f"    Passing through {idx}")
                new_pos.add(idx)
        pos = new_pos
        # for idx in range(m):
        #     if idx in pos:
        #         print("|", end="")
        #     else:
        #         print(line[idx], end="")
        # print()
        # print(f"Res: {res}")

    print(res)


if __name__ == "__main__":
    inp = []

    with open("inp.txt", "r") as file:
        for line in file:
            inp.append(line.strip())
    main(inp)
