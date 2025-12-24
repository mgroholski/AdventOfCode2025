if __name__ == "__main__":
    res = 0

    pieceArea = [5, 7, 6, 7, 7, 7]
    with open("inp.txt", "r") as file:
        for line in file:
            line = line.strip()
            dim, pieces = line.split(":")
            x, y = dim.split("x")
            dim = int(x) * int(y)

            coveredArea = 0
            for idx, p in enumerate(pieces.strip().split(" ")):
                coveredArea += pieceArea[idx] * int(p)

            if coveredArea < dim:
                res += 1

    print(res)
