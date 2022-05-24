def find_letter_case_string_permutations(str):
  perms = []
  perms.append(str)

  for i in range(len(str)):
    if str[i].isalpha(): #only handle letters, skip numbers
      n = len(perms)
      for j in range(n):
        chars = list(perms[j])
        chars[i] = chars[i].swapcase()
        perms.append("".join(chars))
  return perms

def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()