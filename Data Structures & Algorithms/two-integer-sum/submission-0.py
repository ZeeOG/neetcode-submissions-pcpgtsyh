class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returned = {}

        for i, number in enumerate(nums):
            num = target  - number
            if num in returned:
                return [returned[num], i] 
            returned[number] = i