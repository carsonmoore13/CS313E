"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my honor, <CARSON MOORE>, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: csm3682
"""


def length_of_longest_substring_n3(s):
    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    max_length = 0
    length_string = len(s)

    for i in range(length_string):
        for j in range(i,length_string):
            frequency = [0] * 256
            has_duplicate = False
            for k in range(i, j+1):
                character = ord(s[k])
                frequency[character] += 1
                if frequency[character] > 1:
                    has_duplicate = True
                    break
            if not has_duplicate:
                max_length = max(max_length, j-i+1)

    return max_length


def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    max_length = 0
    length_string = len(s)
    for i in range(length_string):
        frequency = [0] * 256
        for j in range(i,length_string):
            character = ord(s[j])
            frequency[character] += 1
            if frequency[character] > 1:
                break
            max_length = max(max_length, j-i+1)

    return max_length


def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list. However, this approach stops early, breaking out of the inner
    loop when a repeating character is found. You may also choose to challenge
    yourself by implementing a sliding window approach.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """


    seen_characters = set()
    max_length = 0
    left = 0

    for right in range(len(s)):
        while s[right] in seen_characters:
            seen_characters.remove(s[left])
            left +=1
        seen_characters.add(s[right])

        max_length = max(max_length, right - left +1)
    return max_length
