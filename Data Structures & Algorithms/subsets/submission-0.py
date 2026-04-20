class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index: int, current: List[int]) -> None:
            # base case
            if index == len(nums):
                res.append(current.copy())
                return
            
            # choice 1: add nums[index] to current
            current.append(nums[index])
            backtrack(index + 1, current)
            # choice 2: exclude nums[index] from current
            current.pop()
            backtrack(index + 1, current)
        
        backtrack(0, [])
        return res