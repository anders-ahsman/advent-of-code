namespace Day02;

class Program
{
    static void Main(string[] args)
    {
        var reports = File.ReadAllLines("input.txt")
            .Select(line => line.Split(" ").Select(int.Parse).ToList())
            .ToList();

        Console.WriteLine(Part1(reports));
        Console.WriteLine(Part2(reports));
    }

    private static int Part1(List<List<int>> reports)
    {
        return reports.Sum(report => IsIncreasingOrDecreasingSafely(report) ? 1 : 0);
    }

    private static bool IsIncreasingOrDecreasingSafely(List<int> report)
    {
        var count = report.Count - 1;

        var differences = Enumerable.Range(0, count)
            .Select(i => report[i + 1] - report[i]);

        int increasing = differences.Count(diff => diff >= 1 && diff <= 3);
        int decreasing = differences.Count(diff => diff <= -1 && diff >= -3);

        return increasing == count || decreasing == count;
    }

    private static int Part2(List<List<int>> reports)
    {
        var safeCount = 0;

        foreach (var report in reports)
        {
            if (IsIncreasingOrDecreasingSafely(report))
            {
                safeCount++;
                continue;
            }

            for (var i = 0; i < report.Count; i++)
            {
                var modifiedReport = report.Where((_, index) => index != i).ToList();
                if (IsIncreasingOrDecreasingSafely(modifiedReport))
                {
                    safeCount++;
                    break;
                }
            }
        }

        return safeCount;
    }
}
