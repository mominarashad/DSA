public class Solution {
    public int[] ProductExceptSelf(int[] nums) {

        int n=nums.Length;
        
        List<int> left_mul=new List<int>(); //it only initialize empty list


        for (int i=0; i<n; i++){
            left_mul.Add(1);
        }

        List<int> right_mul=new List<int>(); //it only initialize empty list
        

        for (int i=0; i<n; i++){
            right_mul.Add(1);
        }

        for (int i =1; i<n; i++){
            left_mul[i]=left_mul[i-1]*nums[i-1];
        }

        for (int i=n-2; i>=0; i--){
            right_mul[i]=right_mul[i+1]*nums[i+1];
        }

        List<int> res=new List<int>();

        for(int i=0; i<n; i++){
            res.Add(left_mul[i]*right_mul[i]);
        }
        return res.ToArray();


    }
}
