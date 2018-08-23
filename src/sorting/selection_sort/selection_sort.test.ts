import { insertionSort } from "./selection_sort";

describe("Insertion Sort", () => {
  test("Should sort the array of numbers", () => {
    const actual = insertionSort([5, 4, 3, 2, 1]);
    expect(actual).toEqual([1, 2, 3, 4, 5]);
  });
});
