def containsDuplicate(nums: list[int]) -> bool:
    """Returns true if any value appears at least twice in a given list"""
    return len(nums) != len(set(nums))