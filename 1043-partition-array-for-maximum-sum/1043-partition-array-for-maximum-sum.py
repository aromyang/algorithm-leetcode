class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        arr_length = len(arr)
        dp = [0] * (arr_length + 1)

        for position in range(1, arr_length + 1):
            max_val_in_subarray = 0
            for length in range(1, min(position, k) + 1):
                max_val_in_subarray = max(max_val_in_subarray, arr[position-length])
                current_sum = dp[position-length] + max_val_in_subarray * length
                dp[position] = max(dp[position], current_sum)

        return dp[arr_length]
