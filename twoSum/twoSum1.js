/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let i, j;

  for (i = 0; i < nums.length; i++) {
    j = i + 1;
    while (nums[i] + nums[j] === target) {
      return [i, j];
    }
  }
};

// approach - nested loops
// TIME COMPLEXITY 0(n^2)
