package arrays

func pivotIndex(nums []int) int {
	leftSum := 0
	rightSum := 0

	for _, v := range nums[1:] {
		rightSum += v
	}

	for i := 0; i < len(nums); i++ {
		if leftSum == rightSum {
			return i
		}

		leftSum += nums[i]

		if i+1 < len(nums) {
			rightSum -= nums[i+1]
		}
	}

	return -1
}
