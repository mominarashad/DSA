class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums, k) {


        let prefix=0
        let count=0
        const seen=new Map()
        seen.set(0,1)

        for (const ch of nums ){
            prefix+=ch 
            count+=seen.get(prefix-k) || 0
            seen.set(prefix,(seen.get(prefix) || 0)+1)
        }

        return count
    }
}
