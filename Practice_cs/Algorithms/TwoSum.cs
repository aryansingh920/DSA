namespace Practice.Algorithms;

public class TwoSum
{
    public int[] Solve(int[] nums, int target)
    {
        var map = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int need = target - nums[i];

            if (map.ContainsKey(need))
                return new[] { map[need], i };

            map[nums[i]] = i;
        }

        return Array.Empty<int>();
    }
}
