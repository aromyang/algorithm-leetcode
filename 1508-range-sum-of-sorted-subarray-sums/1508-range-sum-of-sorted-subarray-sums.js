/**
 * @param {number[]} nums
 * @param {number} n
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeSum = function(nums, n, left, right) {
      const sums = [];
      let mod = Math.pow(10, 9) + 7;

      for (let i = 0; i < nums.length; i++) {
        let cur = nums[i];
        sums.push(cur);
        for (let j = i + 1; j < nums.length; j++) {
          cur += nums[j];
          sums.push(cur);
        }
      }

      sums.sort((a, b) => a - b);

      let result = 0;
      for (let i = left - 1; i < right; i++) {
        result += sums[i];
      }

      return result % mod;
};