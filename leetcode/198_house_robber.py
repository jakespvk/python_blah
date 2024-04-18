#nums = [1,2,3,1]
nums = [2,7,9,3,1]

def rob_1(nums: list[int]) -> int:
    max_money: int = max(nums)
    max_index: int = nums.index(max_money)
    max_adj: int = 0
    if max_index + 2 > len(nums) - 1:
        max_adj = nums[max_index - 2]
    elif max_index - 2 < 0:
        max_adj = nums[max_index + 2]
    else:
        max_adj = max(nums[max_index + 2], nums[max_index - 2])
    return max_money + max_adj

# im stupid and u can rob more than 2 houses

# starting over

def rob_2(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for i in range(0, len(nums), 2):
        rob1 += nums[i]
    for i in range(1, len(nums), 2):
        rob2 += nums[i]
    return max(rob1, rob2)

# taking only adjacents does not work...
def rob(nums: list[nums]) -> int:
    return max(nums[0] + rob(nums[2:], nums[1] + rob(nums[3:])))
    


print(rob(nums))
