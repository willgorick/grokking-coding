from collections import deque

class AbbrevWord:
  def __init__(self, str, start, count):
    self.str = str
    self.start = start
    self.count = count

def unique_abbrevs(word):
  word_len = len(word);
  result = []
  queue = deque()
  queue.append(AbbrevWord(list(), 0, 0))
  while queue:
    abbrev_word = queue.popleft()
    if abbrev_word.start == word_len: #if word.start is past the last index in the word
      if abbrev_word.count != 0: #if we've added a count val, append it
        abbrev_word.str.append(str(abbrev_word.count))
      result.append(''.join(abbrev_word.str))
    else: 
      queue.append(AbbrevWord(list(abbrev_word.str), abbrev_word.start+1, abbrev_word.count +1)) #move the word start index by one, increase the count number by 1
      if abbrev_word.count != 0: #if we have a count val, append it
        abbrev_word.str.append(str(abbrev_word.count))
      
      new_word = list(abbrev_word.str)
      new_word.append(word[abbrev_word.start])
      queue.append(AbbrevWord(new_word, abbrev_word.start + 1, 0))
      
  return result

def generate_generalized_abbreviation(word):
  result = []
  generate_abbreviation_recursive(word, list(), 0, 0, result)
  return result


def generate_abbreviation_recursive(word, abWord, start, count, result):

  if start == len(word):
    if count != 0:
      abWord.append(str(count))
    result.append(''.join(abWord))
  else:
    # continue abbreviating by incrementing the current abbreviation count
    generate_abbreviation_recursive(
      word, list(abWord), start + 1, count + 1, result)

    # restart abbreviating, append the count and the current character to the string
    if count != 0:
      abWord.append(str(count))
    newWord = list(abWord)
    newWord.append(word[start])
    generate_abbreviation_recursive(word, newWord, start + 1, 0, result)


def main():
  print("Generalized abbreviation are: " +
        str(unique_abbrevs("BAT")))
  print("Generalized abbreviation are: " +
        str(unique_abbrevs("code")))

  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()