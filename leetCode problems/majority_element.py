def majorityElement(nums: list[int]) -> int:
    """Returns an element from the list that appears more than ⌊len(nums) / 2⌋ times."""
    n = len(nums) // 2

    num_counter = {}

    for num in nums:
        num_counter[num] = num_counter.get(num, 0) + 1
    
    for key, value in num_counter.items():
        if value > n:
            return key