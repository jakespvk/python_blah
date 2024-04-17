nums = [1,2,3,1]

def rob(nums: list[int]) -> int:
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

print(rob(nums))

# im stupid and u can rob more than 2 houses

# starting over
