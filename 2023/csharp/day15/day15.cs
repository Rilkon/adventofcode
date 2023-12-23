using System.Collections.Specialized;

class SolveDay15(String path)
{
    private readonly string[] input = File.ReadAllText(path).Trim().Split(',');

    private static int Hash(string line)
    {
        int curr = 0;
        foreach (char c in line)
        { curr = (curr + ((int)c)) * 17 % 256; }
        return curr;
    }


    public int Part1()
    {
        return this.input.Select(Hash).Sum();
    }

    public int Part2()
    {
    Dictionary<int, OrderedDictionary> hashmap = [];

        foreach (string label in this.input)
        {
            if (label.Contains('='))
            {
                string[] parts = label.Split("=");
                string _key = parts[0];
                int focal_length = int.Parse(parts[1]);
                int hash = Hash(_key);
                if (!hashmap.ContainsKey(hash))
                {
                    hashmap[hash] = [];
                }
                hashmap[hash][_key] = focal_length;
            }
            else if (label.Contains('-'))
            {
                string _key = label.Split("-")[0];
                int hash = Hash(_key);
                if (hashmap.ContainsKey(hash))
                {
                    hashmap[hash].Remove(_key);
                }
            }
        }

        int result = 0;
        foreach (int key in hashmap.Keys)
        {
            int i = 1;
            foreach (int focal_length in hashmap[key].Values)
            {
                result += (1 + key) * i * focal_length;
                i++;
            }
        }

        return result;
    }

}