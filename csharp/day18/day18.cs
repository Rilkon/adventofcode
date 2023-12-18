using System.Text.RegularExpressions;


class SolveDay18
{
    private string[] input;
    private List<(string, long, string)> puzzledata = new List<(string, long, string)>();

    public SolveDay18(String path)
    {
        this.input = File.ReadAllLines(path);

        foreach (string line in input)
        {
            string[] parts = line.Split(' ');
            string direction = parts[0];
            int meters = int.Parse(parts[1]);
            string rgb = parts[2].Substring(2, parts[2].Length - 3);

            this.puzzledata.Add((direction, meters, rgb));
        }
    }

    private static readonly Dictionary<string, (long, long)> deltas = new(){
          {"U", (0, -1)},
          {"D", (0, 1)},
          {"L", (-1, 0)},
          {"R", (1, 0)},
          {"3", (0, -1)},
          {"1", (0, 1)},
          {"2", (-1, 0)},
          {"0", (1, 0)},
    };




    private static long DigPath(List<(string, long, string)> instructions, bool p2 = false)
    {
        Dictionary<(long, long), string> digpath = new Dictionary<(long, long), string>();
        (long x, long y) curr = (0, 0);

        long steps = 0;

        foreach (var instrs in instructions)
        {
            string direction = instrs.Item1;
            long meters = instrs.Item2;
            string rgb = instrs.Item3;
            (long x, long y) delta;

            if (p2)
            {
                meters = Convert.ToInt64(rgb[..5], 16);
                delta = deltas[rgb[rgb.Length - 1].ToString()];
            }
            else
            {
                delta = deltas[direction];
            }

            steps += meters;
            curr = TupleExtensions.GetNewCoords(curr, delta, meters);
            digpath.Add(curr, "#");
        }

        var coords = digpath.Keys.ToList();
        return (long)Shoelace(coords) + (long)steps / 2 + 1;

    }

    static double Shoelace(List<(long Row, long Col)> polygon)
    {
        var n = polygon.Count;
        var result = 0.0;
        for (var i = 0; i < n - 1; i++)
        {
            result += polygon[i].Row * polygon[i + 1].Col - polygon[i + 1].Row * polygon[i].Col;
        }

        result = Math.Abs(result + polygon[n - 1].Row * polygon[0].Col - polygon[0].Row * polygon[n - 1].Col) / 2.0;
        return result;
    }

    public long Part1()
    {
        return DigPath(puzzledata, false);
    }

    public long Part2()
    {
        return DigPath(puzzledata, true);
    }


}

public static class TupleExtensions
{
    public static (long x, long y) GetNewCoords(this (long x, long y) left, (long dx, long dy) right, long factor)
    {
        return (left.x + right.dx * factor, left.y + right.dy * factor);
    }
}