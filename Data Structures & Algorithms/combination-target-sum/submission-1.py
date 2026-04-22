class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums
        )
        def backtrack(curr, index):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            for i, n in enumerate(nums[index:]):
                if sum(curr) + n > target:
                    break
                curr.append(n)
                backtrack(curr, index + i)
                curr.pop()
        
        backtrack([], 0)
        return res
