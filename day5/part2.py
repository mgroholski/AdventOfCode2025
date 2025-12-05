def main(fresh_ranges, product_ids):
    fresh_ranges.sort()

    ranges = []
    # Merge ranges
    for s, e in fresh_ranges:
        if not len(ranges):
            ranges.append([s, e])
        else:
            r_s, r_e = ranges[-1]
            if r_e >= s:
                ranges[-1] = [r_s, max(r_e, e)]
            else:
                ranges.append([s, e])

    res = 0
    for s, e in ranges:
        res += e - s + 1
    print(res)


if __name__ == "__main__":
    ranges = []
    product_ids = []

    with open("inp.txt", "r") as file:
        isId = False
        for row in file:
            row = row.strip()
            if not len(row):
                isId = True
                continue

            if not isId:
                range = row.split("-")
                ranges.append([int(range[0]), int(range[1])])
            else:
                product_ids.append(int(row))

    main(ranges, product_ids)
