from itertools import product

def get_inputs(path):
  print("reading file: " + path)
  values = []
  with open(path, 'r') as infile:
    values = list(infile.readline().split(','))
  return [int(val) for val in values]

"""
the return args still don't handle a "write pointer" for the instruction output location
"""
def determine_args(state, ptr, modes, num_args):
  args = []
  if 2 <= num_args <= 3:
    args = [state[state[ii]] if modes[ii-(ptr+1)] == 0 else state[ii] for ii in range(ptr+1, ptr+3)]
    if num_args == 3:
      args.append(state[ptr+3])
  elif num_args == 1:
    args = [state[state[ii]] if modes[ii-(ptr+1)] == 0 else state[ii] for ii in range(ptr+1, ptr+2)]
  else:
    raise ValueError(f"Number of args ({num_args}) invalid.")
  return args

def _add(state, ptr, modes):
  args = determine_args(state, ptr, modes, 3)
  state[args[2]] = args[0] + args[1]
  # print(f"ADD: {args}")
  return ptr + 4

def _multiply(state, ptr, modes):
  args = determine_args(state, ptr, modes, 3)
  state[args[2]] = args[0] * args[1]
  # print(f"MULTIPLY: {args}")
  return ptr + 4

"""
spec: Parameters that an instruction writes to will never be in immediate mode.
Therefore, argument will always be in position mode
"""
def _get_input(state, ptr, modes):
  assert(all(m == 0 for m in modes))
  try:
    val = int(input("program requesting integer INPUT: "))
  except:
    print("can't convert to int.")
    raise
  # this doesn't match, because it doesn't handle the write location pointer
  # args = determine_args(state, ptr, modes, 1)
  # state[args[0]] = val
  state[state[ptr+1]] = val
  return ptr + 2

def _output(state, ptr, modes):
  args = determine_args(state, ptr, modes, 1)
  val = args[0]
  if val != 0:
    # print(f"ptr, state[ptr], state: {ptr, state[ptr], state}")
    # input("press any key to continue...")
    pass
  print("OUTPUT: " + str(val))
  return ptr + 2

"""
Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
"""
def _jit(state, ptr, modes):
  args = determine_args(state, ptr, modes, 2)
  # print("state at ptr, +1, and +2: ", state[ptr:ptr+3])
  # print("args: ", args)
  if args[0] != 0:
    return args[1]
  else:
    return ptr + 3

"""
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
"""
def _jif(state, ptr, modes):
  args = determine_args(state, ptr, modes, 2)
  # print("state at ptr, +1, and +2: ", state[ptr:ptr+3])
  # print("args: ", args)
  if args[0] == 0:
    return args[1]
  else:
    return ptr + 3

"""
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
"""
def _lst(state, ptr, modes):
  args = determine_args(state, ptr, modes, 3)
  # print("state at ptr, +1, and +2: ", state[ptr:ptr+3])
  # print("args: ", args)
  if args[0] < args[1]:
    state[args[2]] = 1 # is this the correct addressing dealeo?
  else:
    state[args[2]] = 0
  return ptr + 4

"""
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
"""
def _eql(state, ptr, modes):
  args = determine_args(state, ptr, modes, 3)
  # print("state at ptr, +1, and +2: ", state[ptr:ptr+3])
  # print("args: ", args)
  if args[0] == args[1]:
    state[args[2]] = 1 # is this the correct addressing dealeo?
  else:
    state[args[2]] = 0
  return ptr + 4

def _halt(state, ptr, modes):
  print("HALT")
  return len(state)

operations = {
  1 : _add,
  2 : _multiply,
  3 : _get_input,
  4 : _output,
  5 : _jit,
  6 : _jif,
  7 : _lst,
  8 : _eql,
  99 : _halt,
}

def run(state):
  ptr = 0
  while ptr < len(state):
    # print(f"state, ptr: {state}, {ptr}")
    instruction = state[ptr]
    # number places for 5 digits (through 10000)
    digits = [(instruction//10**ii)%(10) for ii in range(5)]
    modes = digits[2:]
    opcode = digits[0] + 10*digits[1]
    # print("opcode, type: " + str(opcode) + " " + str(type(opcode)))
    # print("modes, type: " + str(modes) + " " + str(type(modes)))
    if opcode not in operations.keys():
      raise ValueError("invalid opcode: " + str(state[ptr]) + " at position: " + str(ptr))
    else:
      if len(state) - ptr < 4:
        break # TODO: this ignores short instructions
      ptr = operations[opcode](state, ptr, modes)
  return state

"""
"""
def part_one(state, in1, in2):
  state[1] = in1
  state[2] = in2
  end_state = run(state)
  return end_state[0]

"""
"""
def part_two(state):
  desired_oudput = 19690720
  for noun, verb in product(range(100), range(100)):
    if part_one(state.copy(), noun, verb) == desired_oudput:
      return 100*noun + verb

if __name__ == "__main__":
  print("main, day 5!")

  # state = get_inputs("inputs/day5_test_input.txt")
  # run(state.copy())
  # exit(0)

  test_day_2 = True
  test_day_2 = False
  if test_day_2:
    state = get_inputs("inputs/day2_input.txt")
    assert part_one(state.copy(), 12, 2) == 2782414
    assert part_two(state.copy()) == 9820
    # print("part 1: " + str()
    # print("part 2: " + str())
    print("Tests passed!")
  else:
    state = get_inputs("inputs/day5_input.txt")
    run(state.copy())
    # print(state)

  print("Done!")