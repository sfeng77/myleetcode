#  Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        myStr = ""
        s = list(s)
        while(s):
            c = s.pop(0)
            if c.isalpha():
                myStr += c
            if c.isdigit():
                count = 0
                stack += [myStr]
                myStr = ""
                while(c != '['):
                    count *= 10
                    count += int(c)
                    c = s.pop(0)
                stack += [count]
            if c == ']':
                myStr = stack.pop() * myStr
                myStr = stack.pop() + myStr

        return myStr
