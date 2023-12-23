using System.Text.RegularExpressions;

partial class SolveDay1(String path)
{
    private readonly string[] input = File.ReadAllLines(path);

    private static readonly Dictionary<string, int> convert = new() {
        { "one"  , 1 },
        { "two"  , 2 },
        { "three", 3 },
        { "four" , 4 },
        { "five" , 5 },
        { "six"  , 6 },
        { "seven", 7 },
        { "eight", 8 },
        { "nine" , 9 },
        { "1"    , 1 },
        { "2"    , 2 },
        { "3"    , 3 },
        { "4"    , 4 },
        { "5"    , 5 },
        { "6"    , 6 },
        { "7"    , 7 },
        { "8"    , 8 },
        { "9"    , 9 },
    };


    [GeneratedRegex(@"[0-9]|one|two|three|four|five|six|seven|eight|nine", RegexOptions.Compiled)]
    private static partial Regex Ltr();

    [GeneratedRegex(@"[0-9]|one|two|three|four|five|six|seven|eight|nine", RegexOptions.Compiled | RegexOptions.RightToLeft)]
    private static partial Regex Rtl();



    private static int GetCalibrationValue(string s, bool p2)
    {
        var matchesLtr = Ltr().Matches(s);
        var matchesRtl = Rtl().Matches(s);
        var result = 0;
        if (matchesLtr.Count > 0)
        {
            var a = 0;
            var b = 0;
            if (!p2)
            {
                a = convert[matchesLtr.First(x => int.TryParse(x.Value, out var _)).Value];
                b = convert[matchesRtl.First(x => int.TryParse(x.Value, out var _)).Value];
            }
            else
            {

                a = convert[matchesLtr.First().Value];
                b = convert[matchesRtl.First().Value];
            }

            result = a * 10 + b;
        }
        return result;
    }
    public int Part1()
    {
        return input
            .Select(s => GetCalibrationValue(s, false))
            .Sum();
    }

    public int Part2()
    {
        return input
            .Select(s => GetCalibrationValue(s, true))
            .Sum();
    }


}