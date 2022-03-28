/**
 * @param {number[]} nums
 * @return {number}
 */
export function pivotIndex(nums) {
  let leftSum = 0;
  let rightSum = nums.reduce((a, b) => a + b) - nums[0];

  for (let i = 0; i < nums.length; i++) {
    if (leftSum === rightSum) {
      return i;
    }

    leftSum += nums[i];
    if (i + 1 < nums.length) {
      rightSum -= nums[i + 1];
    }
  }

  return -1;
}
