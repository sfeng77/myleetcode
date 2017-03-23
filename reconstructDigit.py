# Given a non-empty string containing an out-of-order English representation of
# digits 0-9, output the digits in ascending order.
#
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits
# .
# That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
#
# Output: "012"
# Example 2:
# Input: "fviefuro"
#
# Output: "45"


class Solution(object):
    def originalDigits(self, s):
        from collections import Counter
        identifier = ["z", "w", "u", "x", "g", "s", "v", "i", "t", "o"]
        identified = [0, 2, 4, 6, 8, 7, 5, 9, 3, 1]
        digits = [Counter(i) for i in ["zero", "one", "two", "three", "four",
                                       "five", "six", "seven", "eight", "nine"]
                  ]
        c = Counter(s)
        dcount = [0] * 10
        for i in range(10):
            n = c[identifier[i]]
            d = identified[i]
            for k in digits[d]:
                c[k] -= n
            dcount[d] = n
        return "".join([str(i) * dcount[i] for i in range(10)])
