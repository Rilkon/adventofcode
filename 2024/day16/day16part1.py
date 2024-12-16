import heapq
import pathlib
import sys
from collections import defaultdict
from copy import deepcopy

max_x, max_y = 0, 0

# N0, E1, S2, W3
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse(parsedata):
    global max_x, max_y

    goal = (0, 0)
    maze = defaultdict(str)
    walls = set()
    start = (0, 0)

    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            maze[(x, y)] = value
            if value == "#":
                walls.add((x, y))
            elif value == "S":
                start = (x, y)
            elif value == "E":
                goal = (x, y)

    max_x = x
    max_y = y

    return maze, walls, start, goal


def dijkstra(walls, start):
    state = (start[0], start[1], 1)
    q = []
    heapq.heappush(q, (0, state))

    # Initialize visited with float("inf") as default return value if no key exists
    visited = defaultdict(lambda: float('inf'))
    visited[state] = 0
    path = set()

    def update_state(upd_state, cost_incr):
        new_cost = cost + cost_incr
        if new_cost < visited[upd_state]:
            visited[upd_state] = new_cost
            heapq.heappush(q, (new_cost, upd_state))

    while q:
        cost, state = heapq.heappop(q)
        x, y, d = state

        # Skip if we already reached this point (in same direction) with lower cost
        if visited[state] < cost:
            continue

        # Calculate position to check
        dx, dy = DIRECTIONS[d]
        nx, ny = x + dx, y + dy

        # Forward
        if (nx, ny) not in walls:
            update_state((nx, ny, d), 1)

        # Left / Right
        for new_direction in [(d + 1) % 4, (d - 1) % 4]:
            update_state((x, y, new_direction), 1000)

    return visited, path

def part1(data):
    maze, walls, start, goal = data
    gx, gy = goal
    return min(dijkstra(walls, start)[0][gx, gy, d] for d in range(4))


def part2(data):
    maze, walls, start, goal = data
    gx, gy = goal

    print(len(dijkstra(walls, start)[1]))

    return ""



def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(deepcopy(data))
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
