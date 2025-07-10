def twoSum(nums: list[int], target: int) -> list[int]:
    for i in nums:
        for j in nums:
            if nums[i] + nums[j] == target and [i] != [j]:
                return [i, j]
