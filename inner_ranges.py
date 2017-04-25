def innerRanges(nums, l, r):

''' inner_ranges
Given a sorted integer array in which the range of elements is in the inclusive range [l, r], return its missing inner ranges.

Example

For nums = [-5, 10, 12, 13, 50], l = -5 and r = 88, the output should be

innerRanges(nums, l, r) = ["-4->9", "11", "14->49", "51->88"].

'''

    nums.insert(0, l-1)
    nums.insert(len(nums), r+1)
    
    ans = []
    i = 0
    
    while i < len(nums)-1:
        if nums[i+1] - nums[i] == 2:
            ans.append(str(nums[i]+1))
        elif nums[i+1] - nums[i] > 2:
            ans.append("->".join([str(nums[i]+1), str(nums[i+1]-1)]))        
        i += 1
    
    return ans
    
