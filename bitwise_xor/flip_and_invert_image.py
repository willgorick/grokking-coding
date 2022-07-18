
def flip_and_invert(image):
  for row in image:
    for i in range((len(row)+1)//2): #need the plus 1 so we xor the middle element
      row[i], row[len(row)-1-i] = row[len(row)-1-i]^1, row[i]^1
  return image

def main():
  flipped = flip_and_invert([
    [1,0,1],
    [1,1,1],
    [0,1,1]
  ])
  for row in flipped:
    print(row)

  flipped = flip_and_invert([
    [1,1,0,0],
    [1,0,0,1],
    [0,1,1,1], 
    [1,0,1,0]
  ])
  for row in flipped:
    print(row)

main()