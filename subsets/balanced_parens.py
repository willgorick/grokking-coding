from collections import deque

class ParenthesesString:
  def __init__(self, str, open_count, close_count):
    self.str = str
    self.open_count = open_count
    self.close_count = close_count

# the loop for 2 looks like: ( -> ((, () -> ((), ()( -> (()), ()()
def balanced_parens(num):
  perms = []
  queue = deque()
  queue.append(ParenthesesString("", 0, 0))
  while queue: #queue will only run empty once all parmutations are balanced with num opening and closing parens
    paren_string = queue.popleft()
    if paren_string.open_count == num and paren_string.close_count == num: #completed permutation
      perms.append(paren_string.str)
    else: #incomplete permutation
      if paren_string.open_count < num: #needs more opens
        queue.append(ParenthesesString(paren_string.str + "(", paren_string.open_count +1, paren_string.close_count))
      if paren_string.open_count > paren_string.close_count: #need more closes
        queue.append(ParenthesesString(paren_string.str + ")", paren_string.open_count, paren_string.close_count +1))
  return perms

def recursive_parens(num):
  result = []
  parentheses_string = [0 for _ in range(2*num)]
  generate_recursive_parens(num, 0, 0, parentheses_string, 0, result)
  return result

def generate_recursive_parens(num, open_count, close_count, parentheses_string, index, result):
  if open_count == num and close_count == num:
    result.append(''.join(parentheses_string))
  else:
    if open_count < num:
      parentheses_string[index] = '('
      generate_recursive_parens(num, open_count+1, close_count, parentheses_string, index+1, result)
    if open_count > close_count:
      parentheses_string[index] = ')'
      generate_recursive_parens(num, open_count, close_count+1, parentheses_string, index+1, result)
def main():
  print("All combinations of balanced parentheses are: " +
        str(balanced_parens(1)))
  print("All combinations of balanced parentheses are: " +
        str(balanced_parens(2)))
  print("All combinations of balanced parentheses are: " +
        str(balanced_parens(3)))

  print("All combinations of balanced parentheses are: " +
        str(recursive_parens(1)))
  print("All combinations of balanced parentheses are: " +
        str(recursive_parens(2)))
  print("All combinations of balanced parentheses are: " +
        str(recursive_parens(3)))

main()