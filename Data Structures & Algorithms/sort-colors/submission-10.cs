public class Solution {
    public void SortColors(int[] nums) {
        
        int left=0;
        int mid=0;

        int high=nums.Length-1;

        while(mid<=high){

            if (nums[mid]==0){
                (nums[left],nums[mid])=(nums[mid],nums[left]);
                mid++;
                left++;
            }
            else if(nums[mid]==1){
                mid++;
            }
            else{
                (nums[high],nums[mid])=(nums[mid],nums[high]);
                high--;
            }
        }
    }
}