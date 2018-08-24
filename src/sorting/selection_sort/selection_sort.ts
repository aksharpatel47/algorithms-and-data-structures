export function selectionSort(values: number[]): number[] {
  for (let i = 0; i < values.length; i++) {
    let leastValueIndex = i;
    for (let j = i + 1; j < values.length; j++) {
      if (values[j] < values[leastValueIndex]) {
        leastValueIndex = j;
      }
    }

    let temp = values[i];
    values[i] = values[leastValueIndex];
    values[leastValueIndex] = temp;
  }

  return values;
}
