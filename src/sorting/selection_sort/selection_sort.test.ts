import { sort } from "./selection_sort";

describe("Selection Sort", () => {
  test("Should sort the array of numbers", () => {
    const actual = sort([5, 4, 3, 2, 1]);
    expect(actual).toEqual([1, 2, 3, 4, 5]);
    expect(sort([5, 2, 4, 6, 1, 3])).toEqual([1, 2, 3, 4, 5, 6]);
  });
});
