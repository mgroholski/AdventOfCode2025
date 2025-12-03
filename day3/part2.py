"""
We modify the last problem to finding 12 digits. Thus,
1. We want to find the maximum number before the 11th to last index (let this number be at index i)
2. Find the maximum number between the index i and 10th to last index.
etc.

"""


def getBankValue(bank):
    if not len(bank):
        return 0

    res = ""

    cmpIdx = 0
    for i in range(len(bank)):
        if i >= len(bank) - 11:
            cmpIdx += 1

        c = bank[i]
        if not len(res):
            res += c
        else:
            replaced = False
            for resIdx in range(cmpIdx, len(res)):
                if c > res[resIdx]:
                    res = res[:resIdx] + c
                    replaced = True
                    break

            if not replaced and len(res) < 12:
                res += c

    return int(res)


def main(banks):
    res = 0

    for bank in banks:
        res += getBankValue(bank)
    print(res)


if __name__ == "__main__":
    banks = []

    with open("inp.txt", "r") as file:
        for line in file:
            banks.append(line.strip())

    main(banks)
