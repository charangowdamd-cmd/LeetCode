class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = result = nums[0]

        for n in nums[1:]:
            if n < 0:
                max_so_far , min_so_far = min_so_far , max_so_far

            max_so_far = max(n, max_so_far * n)
            min_so_far = min(n, min_so_far * n)

            result = max(result, max_so_far)

        return result