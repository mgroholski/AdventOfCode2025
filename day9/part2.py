"""
For any possible square, we'll check if there's a line intersecting it.

How to check if there's an intersecting line?

Given two points (a,b), (c,d), we can compute if a line intersects through the following two cases:

1. Horizontal Line
We only need to test against vertical lines within the prospective square. x=a and x=c while y in [min(b,d), max(b,d)]

2. Vertical Line
We only need to test against horizontal lines within the prospective square. y=b and y=d while x in [min(a,c), max(a,c)]
"""


def main(inp):
    horizontal = []
    vertical = []
    for i in range(len(inp)):
        j = (i + 1) % len(inp)

        a_i, b_i = inp[i]
        a_j, b_j = inp[j]

        if a_i == a_j:
            vertical.append((b_i, [min(a_i, a_j), max(a_i, a_j)]))
            vertical.append((b_j, [min(a_i, a_j), max(a_i, a_j)]))
        else:
            horizontal.append((a_i, [min(b_i, b_j), max(b_i, b_j)]))
            horizontal.append((a_j, [min(b_i, b_j), max(b_i, b_j)]))

    res = 0

    for i in range(len(inp)):
        x_i, y_i = inp[i]
        for j in range(i + 1, len(inp)):
            x_j, y_j = inp[j]

            valid = True
            # TODO: Check boundaries

            if valid:
                area = (abs(x_i - x_j) + 1) * (abs(y_i - y_j) + 1)
                res = max(res, area)

    print("Res: ", res)


if __name__ == "__main__":
    inp = []

    with open("inp.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")
            inp.append((int(line[0]), int(line[1])))
    main(inp)
