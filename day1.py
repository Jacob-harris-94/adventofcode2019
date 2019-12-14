from math import floor

def get_inputs(path):
  print("reading file: " + path)
  values = []
  with open(path, 'r') as infile:
    for line in infile:
      values.append(int(line))
  return values

"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
"""
def part_one(mass_list):
  return sum(floor(mass/3)-2 for mass in mass_list)

"""
Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative.
"""
def part_two(mass_list):
  def fuel_required(mass):
    fuel = max(0, floor(mass/3)-2)
    if fuel == 0:
      return mass
    else:
      return mass + fuel_required(fuel)

  return sum(fuel_required(m)-m for m in mass_list)

if __name__ == "__main__":
  print("main, day 1!")

  inputs = get_inputs("inputs/day1_input.txt")
#  print(inputs)

  print("part 1: " + str(part_one(inputs)))
  print("part 2: " + str(part_two(inputs)))