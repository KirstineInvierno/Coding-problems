def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return dict
        else:
            dict[i] = nums[i]
            dict[nums[i]] = i


list = [1, 2, 3, 4]
print(twoSum(list, 6))


def twoSum(nums: list[int], target: int) -> list[int]:
    for i in nums:
        for j in nums:
            if nums[i] + nums[j] == target and [i] != [j]:
                return [i, j]
