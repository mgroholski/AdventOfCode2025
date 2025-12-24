def main(inp):
    res = 0

    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            coord_i, coord_j = inp[i], inp[j]
            area = (abs(coord_i[0] - coord_j[0]) + 1) * (
                abs(coord_i[1] - coord_j[1]) + 1
            )
            res = max(res, area)

    print(res)


if __name__ == "__main__":
    inp = []

    with open("inp.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")
            inp.append((int(line[0]), int(line[1])))
    main(inp)
