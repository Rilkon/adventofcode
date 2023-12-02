import pathlib
import sys
import regex as re

maxred = 12
maxgreen = 13
maxblue = 14


def solve_parts(parsedata):
    valid_game_idx = []
    power = 0
    for game in parsedata.splitlines():
        gameindex = int(re.match(r"Game (\d+)", game).group(1))
        sumred = max([int(x) for x in re.findall(r"(\d+) red", game)])
        sumgreen = max([int(x) for x in re.findall(r"(\d+) green", game)])
        sumblue = max([int(x) for x in re.findall(r"(\d+) blue", game)])
        power = power + (sumred * sumgreen * sumblue)
        if sumred <= maxred and sumblue <= maxblue and sumgreen <= maxgreen:
            valid_game_idx.append(gameindex)

    return sum(valid_game_idx), power


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(solve_parts(puzzle_input))
