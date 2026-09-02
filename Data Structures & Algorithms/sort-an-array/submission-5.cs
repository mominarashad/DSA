public class Solution {
  public int[] SortArray(int[] nums) {
    int n = nums.Length;

    int mid = n / 2;

    if(n<=1){
        return nums;
    }

    int[] first_half = SortArray(nums[..mid]);
    int[] second_half = SortArray(nums[mid..]);

    int i = 0;
    int j = 0;
    int k = 0;

    int[] res = new int[n];

    while (i < first_half.Length && j < second_half.Length) {
      if (first_half[i] <= second_half[j]) {
        res[k] = first_half[i];
        i++;

      } else {
        res[k] = second_half[j];

        j++;
      }
      k++;
    }

    while (i < first_half.Length) {
      res[k] = first_half[i];
      i++;
      k++;
    }
    while (j < second_half.Length) {
      res[k] = second_half[j];
       j++;
      k++;
     
    }

    return res;
  }
}