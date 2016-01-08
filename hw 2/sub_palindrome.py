# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def is_small_pal(s):
    return s[0] == s[-1]

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    n = len(text)
    if n < 2: return (0,n)
    text = text.lower()
    pals_indices = []
    n = len(text)
    pals_indices = [grow(text, start, end) for start in range(n-1) 
                    for end in (start + 2, start + 3) 
                    if end <= n and is_small_pal(text[start:end])]
    return max(pals_indices, key=lambda x: x[1]-x[0])

def grow(text, start, end):
    n = len(text)
    while start > 0 and end < n and text[start-1] == text[end]:
        start -= 1
        end += 1
    return (start, end)
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'
