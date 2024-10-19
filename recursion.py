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


def group_sum(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    #base case
    if start>=len(nums):
        #return true or false based on if we have some sum equal to target
        return target == 0
    # decision that we try and undo
    if group_sum(start + 1, nums, target-nums[start]):
        return True
    return group_sum(start + 1, nums, target)



def group_sum_6(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to the
    given target. Additionally, if there are 6's present in the array, they must all
    be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start>=len(nums):
        #return true or false based on if we have some sum equal to target
        return target == 0
    if nums[start] == 6:
        return group_sum_6(start +1, nums, target - nums[start])

    # decision that we try and undo
    if group_sum_6(start + 1, nums, target-nums[start]):
        return True
    return group_sum_6(start + 1, nums, target)


def group_no_adj(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a value is chosen, the value immediately after
    (the value adjacent) cannot be chosen.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    if group_no_adj(start + 2, nums, target - nums[start]):
        return True

    if group_no_adj(start + 1, nums, target):
        return True

    return False


def group_sum_5(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if a multiple of 5 is in the array, it must be included
    If the value immediately following a multiple of 5 if 1, it must not be chosen

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0

    if nums[start] % 5 == 0:
        if (start + 1 < len(nums)) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - nums[start])
        else:
            return group_sum_5(start + 1, nums, target - nums[start])

    include_current = group_sum_5(start + 1, nums, target - nums[start])
    exclude_current = group_sum_5(start + 1, nums, target)

    return include_current or exclude_current



def group_sum_clump(start, nums, target):
    """
    Given a list of ints, determine if there exists a group of some ints that sum to
    the given target. Additionally, if there is a group of identical numbers in succession,
    they must all be chosen, or none of them must be chosen.
    EX: [1, 2, 2, 2, 5, 2], all three of the middle 2's must be chosen, or none of them must be
    chosen to be included in the sum. One loop is allowed to check for identical numbers.

    pre: start >= 0, len(nums) >= 0, target >= 0, nums will only contain ints
    post: return True if nums has a group of ints that sum to target, False otherwise
    """
    if start >= len(nums):
        return target == 0
    clump_sum = nums[start]
    next_index = start + 1

    while next_index < len(nums) and nums[next_index] == nums[start]:
        clump_sum += nums[next_index]
        next_index += 1

    if group_sum_clump(next_index, nums, target - clump_sum):
        return True

    if group_sum_clump(next_index, nums, target):
        return True

    return False


def split_array(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """
    def helper(index, group1_sum, group2_sum):
        if index >= len(nums):
            return group1_sum == group2_sum

        include_in_group1 = helper(index + 1, group1_sum + nums[index], group2_sum)
        include_in_group2 = helper(index + 1, group1_sum, group2_sum + nums[index])

        return include_in_group1 or include_in_group2

    return helper(0, 0, 0)


def split_odd_10(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of one group must be odd, while the other group must be a multiple of 10
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    """

    def helper( index, sum_group1, sum_group2):
        if index >= len(nums):
            group1_valid = (sum_group1 % 10 == 0 and sum_group2 % 2 == 1)
            group2_valid = (sum_group2 % 10 == 0 and sum_group1 % 2 == 1)
            return group1_valid or group2_valid

        include_in_group1 = helper(index + 1, sum_group1 + nums[index], sum_group2)
        include_in_group2 = helper(index + 1, sum_group1, sum_group2 + nums[index])

        return include_in_group1 or include_in_group2

    return helper(0, 0, 0)

def split_53(nums):
    """
    Given a list of ints, determine if the numbers can be split evenly into two groups
    The sum of these two groups must be equal
    Additionally, all multiples of 5 must be in one group, and all multiples of 3 (and not 5)
    must be in the other group
    Write a recursive helper to call from this function

    pre: len(nums) >= 0, nums will only contain ints
    post: return True if nums can be split, False otherwise
    
    """

    if len(nums) == 0:
        return False

    def helper(index, sum_group1, sum_group2):
        if index >= len(nums):
            return sum_group1 == sum_group2
        if nums[index] % 5 == 0:
            return helper(index + 1, sum_group1 + nums[index], sum_group2)
        elif nums[index] % 3 == 0:
            return helper(index + 1, sum_group1, sum_group2 + nums[index])
        else:
            include_in_group1 = helper(index + 1, sum_group1 + nums[index], sum_group2)
            include_in_group2 = helper(index + 1, sum_group1, sum_group2 + nums[index])

            return include_in_group1 or include_in_group2

    return helper(0, 0, 0)
