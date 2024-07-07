nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums: list[int]) -> int:
    ptr1 = 0
    k = 1
    if len(nums) > 1:
        ptr2 = 1
    else: 
        return 1
    while ptr2 < len(nums):
        if nums[ptr1] == nums[ptr2]:
            nums.remove(nums[ptr2])
        else:
            ptr1 += 1
            ptr2 += 1
            k += 1
    for i in range(k):
        nums.append("_")
    return k

print(removeDuplicates(nums))
print(nums)

