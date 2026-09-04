public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {

       Array.Sort(nums);

       int n=nums.Length;
       List<List<int>> res = new List<List<int>>();
       if (n<3){
          return res;
       }

       

       for (int i=0; i<n-2; i++){
        if (i>0 && nums[i]==nums[i-1]){
            continue;
        }
        int low=i+1;
        int high=n-1;

        while (low<high){
            int sum=nums[low]+nums[high]+nums[i];

            if (sum==0){
                res.Add(new List<int>{nums[low],nums[high],nums[i]});
                low+=1;
                high-=1;

                while (low<high && nums[low]==nums[low-1]){
                    low++;
                }
                while (low<high && nums[high]==nums[high+1]){
                    high--;
                }
            }
            else if(sum<0){
                low+=1;
            }
            else{
                high-=1;
            }
        }
       }
        return res;
        
    }
}
