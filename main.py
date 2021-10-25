"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""


# no imports needed

def foo(x):
    if x <= 1:
        return x
    else:
        return foo(x - 1) + foo(x - 2)


def longest_run(mylist, key):
    run = 0
    runlist = []
    for k, v in enumerate(mylist):
        if k == len(mylist) - 1:
            runlist.append(run + 1)
        elif key == mylist[k] and key == mylist[k + 1]:
            run += 1
        else:
            runlist.append(run + 1)
            run = 0
    return max(runlist)


class Result:
    """ done """

    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size  # run on left side of input
        self.right_size = right_size  # run on right side of input
        self.longest_size = longest_size  # longest run in input
        self.is_entire_range = is_entire_range  # True if the entire input matches the key

    def __repr__(self):
        return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
                (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def longest_run_recursive(mylist, key):
    # Base Case
    if len(mylist) == 1:
        if key == mylist[0]:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    # Divide
    left = mylist[:int(len(mylist) / 2)]
    right = mylist[int(len(mylist) / 2):]
    # Conquer
    left_result = longest_run_recursive(left, key)
    right_result = longest_run_recursive(right, key)
    # Combine
    left_and_right = left_result.right_size + right_result.left_size
    longest_run = max(left_and_right, left_result.longest_size, right_result.longest_size)
    # Combine if one side is all matching and the corresponding, non-matching side also contains a run
    if left_result.is_entire_range is False or right_result.is_entire_range is False:
        if left_result.is_entire_range is True:
            longest_run = max(left_and_right, left_result.longest_size + right_result.left_size)
        if right_result.is_entire_range is True:
            longest_run = max(left_and_right, right_result.longest_size + left_result.right_size)
        return Result(left_result.longest_size, right_result.longest_size,
                      longest_run, False)
    # Combine if both are all matching the key and simply add the left and right sizes to get the longest run
    else:
        longest_run = max(left_and_right,left_result.longest_size + right_result.longest_size)
        return Result(left_result.longest_size, right_result.longest_size,
                  longest_run, True)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2, 12, 12, 8, 12, 12, 3, 12, 12, 12], 12) == 3 


test_list = [12, 3, 12, 12, 4, 12, 12]
#test_list2 = [12, 12, 4, 5, 3, 12, 12, 12]
k = 12
print(longest_run_recursive(test_list, k))
