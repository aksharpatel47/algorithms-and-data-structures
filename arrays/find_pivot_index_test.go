package arrays

import (
	"fmt"
	"testing"
)

func TestFindPivot(t *testing.T) {
	cases := []struct {
		input          []int
		expectedResult int
	}{
		{[]int{1, 7, 3, 6, 5, 6}, 3},
		{[]int{1, 2, 3}, -1},
		{[]int{2, 1, -1}, 0},
	}

	for _, tc := range cases {
		t.Run(fmt.Sprintf("%v->%d", tc.input, tc.expectedResult), func(t *testing.T) {
			if pivotIndex(tc.input) != tc.expectedResult {
				t.Fatal("failure")
			}
		})
	}
}
