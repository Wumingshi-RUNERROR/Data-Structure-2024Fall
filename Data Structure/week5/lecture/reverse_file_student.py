from array_stack_student import ArrayStack

def reverse_file(input_filename, output_filename):
  """Overwrite given file with its contents line-by-line reversed.
     Use with open(.) construct to read and write files as provided.
     Think about how to use ArrayStack to help you.
     You cannot use other data structures like Python List to complete this question.
  """
  # TODO
  S=ArrayStack()
  with open(input_filename, 'r') as F:
    for line in F:
      # TODO
      S.push(line)

  # now we overwrite with contents in LIFO order
  with open(output_filename, 'w') as F:
    # TODO
    for i in range(len(S)):
      F.write(S.pop())

if __name__ == '__main__':
  reverse_file('DSSyllabus.txt', 'DSSyllabus_reverse.txt')
