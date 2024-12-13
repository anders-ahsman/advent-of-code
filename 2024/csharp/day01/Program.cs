namespace day01;

class Program
{
    static void Main(string[] args)
    {
        var left = new List<int>();
        var right = new List<int>();
        string[] lines = File.ReadAllLines("input.txt");
        foreach (string line in lines)
        {
            string[] parts = line.Split("  ");
            left.Add(int.Parse(parts[0]));
            right.Add(int.Parse(parts[1]));
        }
        left.Sort();
        right.Sort();

        int totalDifference = left.Zip(right, (l, r) => Math.Abs(l - r)).Sum();

        var rightCounts = right.GroupBy(x => x).ToDictionary(x => x.Key, x => x.Count());
        var similarityScore = left.Sum(l => l * rightCounts.GetValueOrDefault(l, 0));

        Console.WriteLine("Part 1: " + totalDifference);
        Console.WriteLine("Part 2: " + similarityScore);
    }
}
