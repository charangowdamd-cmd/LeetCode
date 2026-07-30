class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        left=0
        window_sum=0
        max_sum=0

        for right in range(len(nums)):
            window_sum += nums[right]
            freq[nums[right]] =freq.get(nums[right],0) +1

            if right - left + 1 > k:
                window_sum-= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left +=1

            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum