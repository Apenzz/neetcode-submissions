class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, op, cl):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            if (op < n):
                backtrack(curr + "(", op + 1, cl)
            if (cl != op):
                backtrack(curr + ")", op, cl + 1)
        backtrack("", 0, 0)
        return res