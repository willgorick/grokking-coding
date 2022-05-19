def backspace_compare(str1, str2):
  pointer1 = len(str1)-1
  pointer2 = len(str2)-1
  while pointer1 >= 0 or pointer2 >= 0:
    pointer1 = get_next_valid_char_index(str1, pointer1)
    pointer2 = get_next_valid_char_index(str2, pointer2)
    print(pointer1, pointer2)
    if pointer1 < 0 and pointer2 < 0:
      return True
    if pointer1 < 0 or pointer2 < 0:
      return False
    if str1[pointer1] != str2[pointer2]:
      return False
    
    pointer1 -= 1
    pointer2 -= 1
  return True
  
def get_next_valid_char_index(str, index):
  backspace_count = 0
  while (index >= 0):
    if str[index] == '#':
      backspace_count += 1
    elif backspace_count > 0: #if not a backspace and we've already encountered backspaces
      backspace_count -= 1
    else: #if it's not a backspace and we don't have any backspace characters return that index
      return index
    index -= 1 #decrement the pointer for all cases except when we hit a char and don't have any backspaces yet
  return index

def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()