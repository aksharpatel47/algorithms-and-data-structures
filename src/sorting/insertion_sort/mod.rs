pub fn sort(values: &mut Vec<i32>) {
  for i in 1..values.len() {
    let mut key = values[i];
    let mut last_key = i - 1;
    for j in (0..i).rev() {
      if values[j] > key {
        values[j + 1] = values[j];
        last_key = j;
      } else {
        last_key = j + 1;
        break;
      }
    }

    values[last_key] = key;
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
