from itertools import groupby

def get_inputs(path):
  print("reading file: " + path)
  lines = []
  with open(path, 'r') as infile:
    for line in infile.readlines():
      lines.append(line.strip().split('-'))
  return lines

def test():
  # funcs = [
  #   lambda code: code > 0,
  #   lambda code: code > 5,
  #   lambda code: code < 10,
  # ]
  # return all([func(10) for func in funcs])

  # test_string = '111122' # true
  # test_string = '133344321' 
  # test_string = '222111' # false

  """ maybe look at pairs to make sure there's at least one pair which doesn't have an adjacent matching pair?"""

  # pairs = list(zip(test_string, test_string[1:]))
  # pair_pairs = zip(pairs, pairs[1:])
  # matching_pairs = [p1 != p2 and (p1[0]==p1[1] or p2[0]==p2[1])  for p1,p2 in pair_pairs]

  return list(len(list(v)) for k,v in groupby(test_string))
    

  # return matching_pairs


"""
rules:
* 6 digits
* Two adjacent digits are the same (like 22 in 122345).
* Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
"""
def part_one(start, stop):
  num_passes = 0
  rules = [
    lambda code: any([b == a for a,b in zip(code, code[1:])]),
    lambda code: all([b >= a for a,b in zip(code, code[1:])]),
  ]
  for code in range(int(start), int(stop)+1):
    if all([rule(str(code)) for rule in rules]):
      num_passes += 1
  return num_passes

"""
... previous rules also, plus:
* the two adjacent matching digits are not part of a larger group of matching digits.
"""
def part_two(start, stop):
  num_passes = 0
  rules = [
    #lambda code: any([b == a for a,b in zip(code, code[1:])]),
    lambda code: all([b >= a for a,b in zip(code, code[1:])]),
    lambda code: any([length == 2 for length in list(len(list(v)) for k,v in groupby(code)) ] ),
  ]
  for code in range(int(start), int(stop)+1):
    if all([rule(str(code)) for rule in rules]):
      num_passes += 1
  return num_passes

# solution inspired by: https://codereview.stackexchange.com/questions/233741/advent-of-code-2019-day-4
# I read that days before filling out this solution, and didn't look at it while solving this one. As it turns out (unsurprisingly) mine was very similar. I am impressed that we both used "groupby" for the additional rule in part 2.

if __name__ == "__main__":
  print("main, day 4!")

  range_ = get_inputs("inputs/day4_input.txt")[0]

  print(range_)

  # print(test())
  # exit(0)

  print("part 1: " + str(part_one(*range_)))
  print("part 2: " + str(part_two(*range_)))