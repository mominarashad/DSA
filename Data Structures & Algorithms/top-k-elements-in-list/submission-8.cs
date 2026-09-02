public class Solution
{
    public int[] TopKFrequent(int[] nums, int k)
    {
        Dictionary<int, int> freq = new Dictionary<int, int>();

        foreach (int ch in nums)
        {
            if (freq.ContainsKey(ch))
            {
                freq[ch] += 1;
            }
            else
            {
                freq[ch] = 1;
            }
        }

        List<List<int>> buckets = new List<List<int>>();

        for (int i = 0; i <= nums.Length; i++)
        {
            buckets.Add(new List<int>());
        }

        foreach (var item in freq)
        {
            buckets[item.Value].Add(item.Key);
        }

        List<int> res = new List<int>();

        for (int i = buckets.Count - 1; i >= 0; i--)
        {
            foreach (int num in buckets[i])
            {
                res.Add(num);

                if (res.Count == k)
                {
                    return res.ToArray();
                }
            }
        }

        return res.ToArray();
    }
}