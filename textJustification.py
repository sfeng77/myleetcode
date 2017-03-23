#  Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
#
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res= []
        myline = ""
        n= len(words)
        ll = [len(w) for w in words]
        i = 0
        while(i < n):
            #print i
            #print res
            j = i + 1
            mylen = ll[i]
            while(j < n and mylen + 1 + ll[j] <= maxWidth):
                mylen += 1 + ll[j]
                j += 1
            spaces = maxWidth - mylen

            if j == i + 1:
                myline = words[i] + " " * spaces
                i += 1
                res += [myline]
                continue

            if j == n:
                myline = words[i]
                for j in range(i+1, n):
                    myline += " "
                    myline += words[j]

                myline += " " * spaces
                res += [myline]
                i = n
                break

            b = j - i - 1
            s = spaces / b
            spaces -= s * b
            myline = words[i]
            for j in range(b):
                myline += " " * (s + 1)
                if spaces:
                    spaces -= 1
                    myline += " "
                myline += words[i + 1 + j]
            res += [myline]
            i += b + 1
        return res
