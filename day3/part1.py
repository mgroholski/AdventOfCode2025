"""
For each bank,
(1) Choose tenths place by finding the max digit such that the digit does not reside at the last index.
(2) Choose the ones place as the max digit after the index of the tenths digit's index.

"""


def getBankValue(bank):
    l_1, l_2 = "0", "0"

    for idx, c in enumerate(bank):
        if c > l_1 and idx != len(bank) - 1:
            l_1 = c
            l_2 = "0"
        elif c > l_2:
            l_2 = c
    return int(l_1 + l_2)


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
