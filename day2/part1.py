"""
Comma seperated IDs
We want to find numbers within the range that have repeat a sequence twice (e.g. 999 is not invalid but 1010 is).
We add the invalid numbers within the range to get the answer.

Do we search every number within the range?
    - For a range to be invalid, it must have an even amount of digits.
    - We split at the centerpoint to see if the first half of the number equals the second half.
    -


Suppose range 998 - 1112
    There's two invalid ids: 1010 and 1111
    1. We could start with 998 -> not an even length number.
    We need to add a digit that will be prepended to the number. So we split the number into odd - even group (floor(n/2) and ceil(n/2))
    2. We can check if the repeated sequence number is within the range. If so, continue the process.
"""


def main(ranges):
    res = 0

    for s, e in ranges:
        for i in range(s, e + 1):
            str_i = str(i)
            if str_i[: len(str_i) // 2] == str_i[len(str_i) // 2 :]:
                res += i
    print(res)


if __name__ == "__main__":
    ranges = []
    with open("inp.txt", "r") as text:
        inp = ""
        for line in text:
            inp += line

        ranges_str = inp.split(",")
        for r in ranges_str:
            a, b = r.split("-")
            ranges.append([int(a), int(b)])

    main(ranges)
