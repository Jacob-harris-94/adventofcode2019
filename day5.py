from itertools import product

def get_inputs(path):
  print("reading file: " + path)
  values = []
  with open(path, 'r') as infile:
    values = list(infile.readline().split(','))
  return [int(val) for val in values]

def _add(state, ptr, args):
  state[args[2]] = args[0] + args[1]
  print(f"ADD: {args}")
  return ptr + 4

def _multiply(state, ptr, args):
  state[args[2]] = args[0] * args[1]
  print(f"MULTIPLY: {args}")
  return ptr + 4

def _get_input(state, ptr, args):
  try:
    val = int(input("program requesting integer INPUT: "))
  except:
    print("can't convert to int.")
    raise
  state[args[0]] = val
  return ptr + 2

def _output(state, ptr, args):
  val = state[args[0]]
  print("OUTPUT: " + str())
  return ptr + 2

def _halt(state, ptr, args):
  print("HALT")
  return len(state)

operations = {
  1 : _add,
  2 : _multiply,
  3 : _get_input,
  4 : _output,
  99 : _halt,
}

def run(state):
  ptr = 0
  while ptr < len(state):
    print(f"state, ptr: {state}, {ptr}")
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
      # TODO: only works for non-immediate addressing
      # assert(all(m == 0 for m in modes))
      
      # 0 == position mode, 1 == immediate mode
      args = [state[state[ii]] if modes[ii-(ptr+1)] == 0 else state[ii] for ii in range(ptr+1, ptr+3)]

      # args = [state[ii] for ii in range(ptr+1, ptr+4)]

      # 0 == position mode, 1 == immediate mode
      # args = []
      # for ii in range(ptr+1, ptr+3):
      #   if modes[ii-(ptr+1)] == 0:
      #     # position mode is the value pointed to by the arg at that position
      #     args.append(state[state[ii]])
      #     print(f"position arg {args[-1]}")
      #   else:
      #     args.append(state[ii])
      #     print(f"immediate arg {args[-1]}")
      args.append(state[ptr+3])
      ptr = operations[opcode](state, ptr, args)
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


  state = get_inputs("inputs/day5_test_input.txt")
  run(state.copy())
  exit(-1)

  test_day_2 = True
  # test_day_2 = False
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
    print(state)

  print("Done!")