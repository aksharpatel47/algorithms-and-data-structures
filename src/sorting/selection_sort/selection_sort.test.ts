import { sort } from "./selection_sort";

describe("Selection Sort", () => {
  test("Should sort the array of numbers", () => {
    const arr = [5, 4, 3, 2, 1];
    sort(arr);
    expect(arr).toEqual([1, 2, 3, 4, 5]);
    const arr2 = [5, 2, 4, 6, 1, 3];
    sort(arr2);
    expect(arr2).toEqual([1, 2, 3, 4, 5, 6]);
  });
});
