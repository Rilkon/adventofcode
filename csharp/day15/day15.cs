

class SolveDay15
{
    private readonly string path = "";
    private readonly string[] input;
    private readonly long[] times;
    private readonly long[] records;

    public SolveDay15(String path)
    {
        this.path = path;
        this.input = File.ReadAllLines(path);


        this.times = this.input[0]
                .Substring("Time:".Length)
                .Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(long.Parse)
                .ToArray();

        this.records = this.input[1]
                .Substring("Distance:".Length)
                .Split(" ", StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries)
                .Select(long.Parse)
                .ToArray();
    }


    private int GetWaysToWin(long[] times, long[] records)
    {
        int total = 1;
        for (int race = 0; race < times.Length; race++)
        {
            total *= Enumerable.Range(0, (int)times[race])
                    .Count(time => time * (times[race] - time) > records[race]);
        }
        return total;
    }
    public int Part1()
    {
        return GetWaysToWin(this.times, this.records);
    }


    public int Part2()
    {
        long totalTime = long.Parse(string.Join("", this.times));
        long record = long.Parse(string.Join("", this.records));

        return GetWaysToWin([totalTime], [record]);

    }
}