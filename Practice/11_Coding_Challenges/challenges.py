"""
===========================================
CODING CHALLENGES - INTERVIEW PREP
===========================================

These problems are similar to what you'll see in:
- Job interviews
- LeetCode Easy/Medium
- HackerRank assessments

Tips:
- Try to solve WITHOUT looking at solutions first
- Time yourself (aim for 15-20 min per problem)
- Test your solutions with different inputs
- Think about edge cases
"""

# ============================================
# WARM-UP CHALLENGES (Easy)
# ============================================

# Challenge 1: Two Sum
# Given a list of numbers and a target, return indices of two numbers that add up to target
# Example: two_sum([2, 7, 11, 15], 9) → [0, 1] (because 2 + 7 = 9)
def two_sum(nums, target):
    """
    Input: nums (list of integers), target (integer)
    Output: list of two indices [i, j] where nums[i] + nums[j] = target
    """
    pass  # Your code here

# Test cases:
# print(two_sum([2, 7, 11, 15], 9))      # Should return [0, 1]
# print(two_sum([3, 2, 4], 6))           # Should return [1, 2]
# print(two_sum([3, 3], 6))              # Should return [0, 1]


# Challenge 2: Valid Palindrome
# Check if a string is a palindrome (reads same forwards and backwards)
# Ignore spaces, punctuation, and case
# Example: "A man, a plan, a canal: Panama" → True
def is_palindrome(s):
    """
    Input: s (string)
    Output: boolean (True if palindrome, False otherwise)
    """
    pass  # Your code here

# Test cases:
# print(is_palindrome("racecar"))                              # True
# print(is_palindrome("A man, a plan, a canal: Panama"))      # True
# print(is_palindrome("hello"))                                # False


# Challenge 3: Fizz Buzz
# Classic interview problem!
# Return a list of strings from 1 to n where:
# - "Fizz" if divisible by 3
# - "Buzz" if divisible by 5
# - "FizzBuzz" if divisible by both
# - The number as a string otherwise
def fizz_buzz(n):
    list1 = []
    for i in range (1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list1.append("FizzBuzz")
        elif i % 3 == 0:
            list1.append("Fizz")
        elif i % 5 == 0:
            list1.append("Buzz")
        else:
            list1.append(str(i))
    return list1

# Test cases:
print(fizz_buzz(15))
# Should return: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']


# Challenge 4: Reverse Integer
# Reverse the digits of an integer
# Example: 123 → 321, -123 → -321
def reverse_integer(x):
    """
    Input: x (integer)
    Output: integer with digits reversed
    """
    pass  # Your code here

# Test cases:
# print(reverse_integer(123))    # Should return 321
# print(reverse_integer(-123))   # Should return -321
# print(reverse_integer(120))    # Should return 21


# Challenge 5: Valid Anagram
# Check if two strings are anagrams (contain same letters in different order)
# Example: "listen" and "silent" are anagrams
def is_anagram(s, t):
    """
    Input: s (string), t (string)
    Output: boolean
    """
    pass  # Your code here

# Test cases:
# print(is_anagram("listen", "silent"))     # True
# print(is_anagram("anagram", "nagaram"))   # True
# print(is_anagram("rat", "car"))           # False


# ============================================
# INTERMEDIATE CHALLENGES
# ============================================

# Challenge 6: Longest Substring Without Repeating Characters
# Find the length of the longest substring without repeating characters
# Example: "abcabcbb" → 3 (substring "abc")
def length_of_longest_substring(s):
    """
    Input: s (string)
    Output: integer (length of longest substring)
    """
    pass  # Your code here

# Test cases:
# print(length_of_longest_substring("abcabcbb"))   # Should return 3
# print(length_of_longest_substring("bbbbb"))      # Should return 1
# print(length_of_longest_substring("pwwkew"))     # Should return 3


# Challenge 7: Group Anagrams
# Group strings that are anagrams of each other
# Example: ["eat","tea","tan","ate","nat","bat"] → [["eat","tea","ate"], ["tan","nat"], ["bat"]]
def group_anagrams(words):
    """
    Input: words (list of strings)
    Output: list of lists (grouped anagrams)
    """
    pass  # Your code here

# Test cases:
# print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))


# Challenge 8: Product of Array Except Self
# Given array nums, return array where output[i] equals product of all elements except nums[i]
# Example: [1,2,3,4] → [24,12,8,6] because 24=2*3*4, 12=1*3*4, etc.
# Challenge: Do it WITHOUT using division
def product_except_self(nums):
    """
    Input: nums (list of integers)
    Output: list of integers
    """
    pass  # Your code here

# Test cases:
# print(product_except_self([1, 2, 3, 4]))    # Should return [24, 12, 8, 6]
# print(product_except_self([2, 3, 4, 5]))    # Should return [60, 40, 30, 24]


# Challenge 9: Valid Parentheses
# Check if string of brackets is valid
# "()" = valid, "()[]{}" = valid, "(]" = invalid, "([)]" = invalid
def is_valid_parentheses(s):
    """
    Input: s (string containing only '(', ')', '{', '}', '[', ']')
    Output: boolean
    """
    pass  # Your code here

# Test cases:
# print(is_valid_parentheses("()"))        # True
# print(is_valid_parentheses("()[]{}"))    # True
# print(is_valid_parentheses("(]"))        # False
# print(is_valid_parentheses("([)]"))      # False


# Challenge 10: Merge Intervals
# Given list of intervals, merge overlapping ones
# Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
def merge_intervals(intervals):
    """
    Input: intervals (list of lists, each with [start, end])
    Output: list of merged intervals
    """
    pass  # Your code here

# Test cases:
# print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
# print(merge_intervals([[1,4],[4,5]]))                 # [[1,5]]


# ============================================
# REAL-WORLD CHALLENGES
# ============================================

# Challenge 11: Most Common Word
# Find the most common word in a string (ignore punctuation and case)
# Exclude words in a banned list
def most_common_word(paragraph, banned):
    """
    Input: paragraph (string), banned (list of strings to exclude)
    Output: string (most common non-banned word)
    """
    pass  # Your code here

# Test cases:
# print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
# Should return "ball"


# Challenge 12: Top K Frequent Elements
# Return the k most frequent elements from a list
# Example: nums = [1,1,1,2,2,3], k = 2 → [1,2]
def top_k_frequent(nums, k):
    """
    Input: nums (list of integers), k (integer)
    Output: list of k most frequent integers
    """
    pass  # Your code here

# Test cases:
# print(top_k_frequent([1,1,1,2,2,3], 2))      # [1, 2]
# print(top_k_frequent([1,2,2,3,3,3], 2))      # [3, 2]


# Challenge 13: String Compression
# Compress a string using counts of repeated characters
# Example: "aabcccccaaa" → "a2b1c5a3"
# If compressed string isn't shorter, return original
def compress_string(s):
    """
    Input: s (string)
    Output: string (compressed or original if compression doesn't help)
    """
    pass  # Your code here

# Test cases:
# print(compress_string("aabcccccaaa"))   # "a2b1c5a3"
# print(compress_string("abc"))           # "abc" (compressed would be longer)


# Challenge 14: Find Missing Number
# Given array of n-1 numbers in range 1 to n, find the missing number
# Example: [1, 2, 4, 5] → 3
def find_missing_number(nums):
    """
    Input: nums (list of integers)
    Output: integer (the missing number)
    """
    pass  # Your code here

# Test cases:
# print(find_missing_number([1, 2, 4, 5]))    # 3
# print(find_missing_number([1, 2, 3, 5]))    # 4


# Challenge 15: Rotate Array
# Rotate array to the right by k steps
# Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]
def rotate_array(nums, k):
    """
    Input: nums (list), k (integer - steps to rotate)
    Output: None (modify nums in-place)
    """
    pass  # Your code here

# Test cases:
# arr = [1,2,3,4,5]
# rotate_array(arr, 2)
# print(arr)  # Should be [4,5,1,2,3]


"""
===========================================
SOLUTIONS
===========================================
Don't look until you've tried!
"""

# Solution 1: Two Sum
def two_sum_solution(nums, target):
    seen = {}  # Store number: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Solution 2: Valid Palindrome
def is_palindrome_solution(s):
    # Remove non-alphanumeric and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


# Solution 3: Fizz Buzz
def fizz_buzz_solution(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# Solution 4: Reverse Integer
def reverse_integer_solution(x):
    sign = -1 if x < 0 else 1
    reversed_num = int(str(abs(x))[::-1])
    return sign * reversed_num


# Solution 5: Valid Anagram
def is_anagram_solution(s, t):
    return sorted(s) == sorted(t)


# Solution 6: Longest Substring Without Repeating
def length_of_longest_substring_solution(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Solution 7: Group Anagrams
def group_anagrams_solution(words):
    from collections import defaultdict
    groups = defaultdict(list)

    for word in words:
        # Sort the word to use as key
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# Solution 8: Product Except Self
def product_except_self_solution(nums):
    n = len(nums)
    result = [1] * n

    # Left pass
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Right pass
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result


# Solution 9: Valid Parentheses
def is_valid_parentheses_solution(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


# Solution 10: Merge Intervals
def merge_intervals_solution(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


# Solution 11: Most Common Word
def most_common_word_solution(paragraph, banned):
    import re
    from collections import Counter

    # Clean and split
    words = re.findall(r'\w+', paragraph.lower())
    # Filter banned words
    words = [w for w in words if w not in banned]
    # Count and return most common
    counter = Counter(words)
    return counter.most_common(1)[0][0]


# Solution 12: Top K Frequent
def top_k_frequent_solution(nums, k):
    from collections import Counter
    counter = Counter(nums)
    return [num for num, count in counter.most_common(k)]


# Solution 13: String Compression
def compress_string_solution(s):
    if not s:
        return s

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))
    result = ''.join(compressed)

    return result if len(result) < len(s) else s


# Solution 14: Find Missing Number
def find_missing_number_solution(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Solution 15: Rotate Array
def rotate_array_solution(nums, k):
    k = k % len(nums)  # Handle k > len(nums)
    nums[:] = nums[-k:] + nums[:-k]
