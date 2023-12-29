using System;
using System.Collections.Generic;
using System.IO;

class SolveDay23
{
    static readonly int[][] DELTAS =
{
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
};

    static readonly Dictionary<char, int[]> SLOPEDELTAS = new Dictionary<char, int[]>
    {
        { '^', new int[] { 0, -1 } },
        { 'v', new int[] { 0, 1 } },
        { '<', new int[] { -1, 0 } },
        { '>', new int[] { 1, 0 } }
    };

    private readonly string[] input;
    private List<(string, long, string)> puzzledata = new List<(string, long, string)>();

    public SolveDay23(String path)
    {
        this.input = File.ReadAllLines(path);
    }
    static Tuple<Dictionary<Tuple<int, int>, char>, int, int> Parse(string[] parsedata, bool p2 = false)
    {
        var grid = new Dictionary<Tuple<int, int>, char>();
        int max_x = 0;
        int max_y = 0;

        for (int y = 0; y < parsedata.Length; y++)
        {
            string line = parsedata[y];
            for (int x = 0; x < line.Length; x++)
            {
                char trail = line[x];
                grid[Tuple.Create(x, y)] = trail;

                max_x = Math.Max(max_x, x);
                max_y = Math.Max(max_y, y);

                if (p2 && SLOPEDELTAS.ContainsKey(trail))
                {
                    grid[Tuple.Create(x, y)] = '.';
                }
            }
        }

        return Tuple.Create(grid, max_x, max_y);
    }

    private static int Dfs(Dictionary<Tuple<int, int>, char> g,
                           Tuple<int, int> curr,
                           Tuple<int, int> end,
                           HashSet<Tuple<int, int>>? visited = null)
    {
        visited ??= [];

        if (curr.Equals(end))
        {
            return visited.Count - 1;
        }

        visited.Add(curr);

        int x = curr.Item1;
        int y = curr.Item2;

        int? best = null;
        foreach (int[] delta in DELTAS)
        {
            int dx = delta[0];
            int dy = delta[1];
            Tuple<int, int> newpos = Tuple.Create(x + dx, y + dy);
            if (!g.ContainsKey(newpos) || g[newpos] == '#')
            {
                continue;
            }
            if (g[newpos] != '.' && (SLOPEDELTAS.ContainsKey(g[newpos]) && SLOPEDELTAS[g[newpos]][0] != dx || SLOPEDELTAS[g[newpos]][1] != dy))
            {
                continue;
            }
            if (visited.Contains(newpos))
            {
                continue;
            }

            visited.Add(newpos);
            int result = Dfs(g, newpos, end, visited);
            best = best.HasValue ? Math.Max(best.Value, result) : result;
            visited.Remove(newpos);

        }
        
                    var observer = Task.Run(() =>
            {
                while (true)
                {
                    Console.WriteLine($"Current best: {best}");
                    Thread.Sleep(3000);
                }
            });


        return best ?? 0;
    }

    public int SolveBothParts(Tuple<Dictionary<Tuple<int, int>, char>, int, int> data, bool p2 = false)
    {
        var grid = data.Item1;
        int max_x = data.Item2;
        int max_y = data.Item3;

        Tuple<int, int> start = Tuple.Create(1, 0);
        Tuple<int, int> end = Tuple.Create(max_x - 1, max_y);

        return Dfs(grid, Tuple.Create(1, 0), end);
    }

    public int PartOne()
    {
        var data = Parse(this.input);
        return SolveBothParts(data);
    }

    public int PartTwo()
    {



        int stackSize = 1024 * 1024 * 64;
        var data = Parse(this.input, true);
        int result = 0; // Used to store the return value

        var watch = System.Diagnostics.Stopwatch.StartNew();
        // the code that you want to measure comes here


        var thread = new Thread(() => { result = SolveBothParts(data); }, stackSize);
        thread.Start();
        thread.Join();

        watch.Stop();
        var elapsedMs = watch.ElapsedMilliseconds;
        Console.WriteLine($"Runtime in ms: {elapsedMs}");
        return result;

    }

}
