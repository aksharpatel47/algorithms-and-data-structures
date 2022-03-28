import { pivotIndex } from "./find_pivot_index";

it.each([
  [[1, 7, 3, 6, 5, 6], 3],
  [[1, 2, 3], -1],
  [[2, 1, -1], 0],
])("Should find pivot index", (input, expected_output) => {
  expect(pivotIndex(input)).toEqual(expected_output);
});
