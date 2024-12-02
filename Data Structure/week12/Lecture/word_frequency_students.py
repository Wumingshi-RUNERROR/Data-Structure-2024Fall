def max_word_count(filename):
  """
  # TODO: Use python dictionary to find the most frequent word in the input file
  # Please do not use the sorted(.) function for this exercise
  """
  max_word, max_count = '', 0
  dic={}
  # Phase 1: Count word occurrence
  with open(filename, "r") as F:
    for line in F:
      words = line.strip().lower().split()
      # TODO
      for i in words:
        try:
          dic[i]+=1
        except:
          dic[i]=1


  # Phase 2: Search a word with maximum occurrence
  # TODO: Use def items() in python dictionary to obtain a sequence of (key,value) pairs
  for i in dic:
    if dic[i]>max_count:
      max_count=dic[i]
      max_word=i

  return max_word, max_count

if __name__ == '__main__':
  filename = r"C:\Users\xym\Desktop\PeterXu\NYUSH\Fall 2024\Data Structure\week12\Lecture\inputtext2.txt"
  
  max_word, max_count = max_word_count(filename)
  
  print('The most frequent word is', max_word) # Expect: interest
  print('Its number of occurrences is', max_count) # Expect: 7
