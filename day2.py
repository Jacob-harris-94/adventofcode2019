from math import floor
from itertools import product

def get_inputs(path):
  print("reading file: " + path)
  values = []
  with open(path, 'r') as infile:
    values = list(infile.readline().split(','))
  return [int(val) for val in values]

"""
"""
def part_one(state, in1, in2):
  state[1] = in1
  state[2] = in2
  
  ptr = 0

  while ptr < len(state):
    if state[ptr] == 1:
      state[state[ptr+3]] = state[state[ptr+1]] + state[state[ptr+2]]
    elif state[ptr] == 2:
      state[state[ptr+3]] = state[state[ptr+1]] * state[state[ptr+2]]
    elif state[ptr] == 99:
      break
    else:
      raise ValueError("invalid opcode ", state[ptr], " noun: ", in1, " verb: ", in2)

    ptr += 4  

  return state[0]

"""
"""
def part_two(state):
  desired_oudput = 19690720
  for noun, verb in product(range(100), range(100)):
    if part_one(state.copy(), noun, verb) == desired_oudput:
      return 100*noun + verb

if __name__ == "__main__":
  print("main, day 2!")

  state = get_inputs("inputs/day2_input.txt")
  # print(state)

  print("part 1: " + str(part_one(state.copy(), 12, 2)))
  print("part 2: " + str(part_two(state.copy())))