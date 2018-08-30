import { sort } from "./insertion_sort";

describe("Insertion Sort", () => {
  test("Should sort the list of numbers in ascending order", () => {
    expect(sort([5, 4, 3, 2, 1])).toEqual([1, 2, 3, 4, 5]);
    expect(sort([5, 2, 4, 6, 1, 3])).toEqual([1, 2, 3, 4, 5, 6]);
  });
});
