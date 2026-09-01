public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {

        Dictionary<string, List<string>> groups =
            new Dictionary<string, List<string>>();

        foreach (string word in strs) {

            Dictionary<char, int> freq =
                new Dictionary<char, int>();

            foreach (char ch in word) {

                if (freq.ContainsKey(ch)) {
                    freq[ch]++;
                }
                else {
                    freq[ch] = 1;
                }
            }

            // Create a key from the frequency dictionary
            string key = "";

            foreach (var item in freq.OrderBy(x => x.Key)) {
                key += item.Key + item.Value.ToString();
            }

            if (groups.ContainsKey(key)) {
                groups[key].Add(word);
            }
            else {
                groups[key] = new List<string> { word };
            }
        }

        return new List<List<string>>(groups.Values);
    }
}