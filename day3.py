from collections import defaultdict

def get_inputs(path):
  print("reading file: " + path)
  lines = []
  with open(path, 'r') as infile:
    for line in infile.readlines():
      lines.append(line.strip().split(','))
  return lines

def path_to_pairs(path):
  ordered_pairs = []
  position = [0, 0]
  direction_change = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0]
  }
  steps = 0
  steps_table = defaultdict(list)
  for segment in path:
    direction, distance = segment[0], int(segment[1:])
    # print(direction, " ", distance)
    for _ in range(distance):
      steps += 1
      position[0] += direction_change[direction][0]
      position[1] += direction_change[direction][1]
      ordered_pairs.append(tuple(position))
      steps_table[tuple(position)].append(steps)
  return ordered_pairs, steps_table

"""
"""
def part_one(p1, p2):
  crosses = list(set(p1).intersection(set(p2)))
  crosses.sort(key=lambda pair: sum([abs(p) for p in pair]))
  manhattan_distances = [sum([abs(p) for p in pair]) for pair in crosses]
  return min(manhattan_distances)

"""
"""
def part_two(p1, st1, p2, st2):
  crosses = list(set(p1).intersection(set(p2)))
  lengths = {}
  min_length = int(1e9)
  for point in crosses:
    lengths[point] = min(st1[point]) + min(st2[point])
    if lengths[point] < min_length:
      min_length = lengths[point]
  return min_length


if __name__ == "__main__":
  print("main, day 3!")

  paths = get_inputs("inputs/day3_input.txt")

  p1, st1 = path_to_pairs(paths[0])
  p2, st2 = path_to_pairs(paths[1]) 

  print("part 1: " + str(part_one(p1, p2)))
  print("part 2: " + str(part_two(p1, st1, p2, st2))) 