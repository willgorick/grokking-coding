
def evaluate(expression):
  result = []
  if '+' not in expression and '-' not in expression and '*' not in expression:
    result.append(int(expression))
  else:
    for i in range(len(expression)):
      char = expression[i]
      if not char.isdigit(): #the operators
        left = evaluate(expression[0:i]) #1
        right = evaluate(expression[i+1:]) #2 * 3 -> 6 recursively
        for part1 in left:
          for part2 in right:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)
  return result

def evaluate_memoize_start(expression):
  return evaluate_memoize({}, expression)

def evaluate_memoize(map, expression):
  if expression in map:
    return map[input]
  result = []
  if '+' not in expression and '-' not in expression and '*' not in expression:
    result.append(int(expression))
  else:
    for i in range(len(expression)):
      char = expression[i]
      if not char.isdigit(): #the operators
        left = evaluate(expression[0:i])
        right = evaluate(expression[i+1:])
        for part1 in left:
          for part2 in right:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)
  map[expression] = result
  return result

def main():
  print("Expression evaluations: " +
        str(evaluate("1+2*3")))

  print("Expression evaluations: " +
        str(evaluate("2*3-4-5")))

  print("Expression evaluations: " +
        str(evaluate_memoize_start("1+2*3")))

  print("Expression evaluations: " +
        str(evaluate_memoize_start("2*3-4-5")))


main()