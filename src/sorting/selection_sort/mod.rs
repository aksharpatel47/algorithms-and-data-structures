pub fn sort(values: &mut Vec<i32>) {
  for i in 0..values.len() {
    let mut least_index = i;
    for j in i + 1..values.len() {
      if values[j] < values[least_index] {
        least_index = j;
      }
    }

    let temp = values[i];
    values[i] = values[least_index];
    values[least_index] = temp;
  }
}

#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn test_sort() {
    let mut v: Vec<i32> = vec![5, 4, 3, 2, 1];
    sort(&mut v);
    assert_eq!(v, [1, 2, 3, 4, 5]);

    v = vec![5, 2, 4, 6, 1, 3];
    sort(&mut v);
    assert_eq!(v, [1, 2, 3, 4, 5, 6]);
  }
}
