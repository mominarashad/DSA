public class Solution {
  public List<List<int>> FourSum(int[] nums, int target) {
    Array.Sort(nums);

    int n = nums.Length;
    List<List<int>> res = new List<List<int>>();
    if (n < 4) {
      return res;
    }

    for (int i = 0; i < n - 3; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }
      for (int j = i+1; j < n - 2; j++) {
        if (j > i + 1 && nums[j] == nums[j - 1]) {
          continue;
        }
        int low = j + 1;
        int high = n - 1;

        while (low < high) {
          long sum = (long)nums[low] + nums[high] + nums[i] + nums[j];

          if (sum == target) {
            res.Add(new List<int> { nums[low], nums[high], nums[i], nums[j] });
            low += 1;
            high -= 1;

            while (low < high && nums[low] == nums[low - 1]) {
              low++;
            }
            while (low < high && nums[high] == nums[high + 1]) {
              high--;
            }
          } else if (sum < target) {
            low += 1;
          } else {
            high -= 1;
          }
        }
      }
    }

    return res;
  }
}
