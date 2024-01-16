/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let numIndices = {};
  for (let i = 0; i < nums.length; i++) {
    let complement = target - nums[i];

    if (numIndices.hasOwnProperty(complement)) {
      return [numIndices[complement], i];
    }

    numIndices[nums[i]] = i;
  }

  return [];
};

// approach - hash table method
// TIME COMPLEXITY 0(n)
