# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.


def check_ten(n1, n2):
    # Code Here
    # result = n1 + n2
    # if result == 10:
    #     return True
    # else:
    #     return False
    return (n1 + n2) == 10

# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1, n2):
    # Code Here
    result = n1 + n2
    if result == 10:
        return True
    else:
        return result


# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.


def first_upper(mystring):
    # Code Here

    # ## Task 4
    #
    # Create a function that takes in a string and returns the last two characters.
    # If there are less than two chracters, return the string:  "Error".
    # Use this link if you need help/hint.
    # (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)
    return str(mystring[0]).upper()

def last_two(mystring):
    # Code Here
    # last_2 = mystring[-2:]
    # return last_2
    if len(mystring) < 2:
        return "Error"
    else:
        return mystring[-2:]

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.


def seq_check(nums):

    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    print(range(len(nums)-2))
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        print(nums[i])
        print(nums[i+1])
        print(nums[i+2])
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**


def compare_len(s1, s2):
    # Code Here
    # len_s1 = len(s1)
    # len_s2 = len(s2)
    # if (len_s1 - len_s2) >= 0:
    #     return len_s1 - len_s2
    # else:
    #     return 0
    return abs(len(s1)-len(s2))




# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.


def sum_or_max(mylist):

    # Code Here
    # if len(mylist) / 2 == 0:
    #     for num in mylist:
    #         num = num + num
    #     return num
    # else:
    #     return max(mylist)
    length = len(mylist)

    if length % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)
