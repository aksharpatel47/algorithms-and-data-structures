import { sum } from "./insertion-sort";

describe("Sum function", () => {
  test("Should return addition of two numbers", () => {
    const ans = sum(1, 2);
    expect(ans).toBe(3);
  });
});
