# This template is provided to give you a starting point for structuring your code,
# but it is intentionally left empty. You are encouraged to write the entire implementation
# from scratch to help you practice the problem-solving process and reinforce the
# programming concepts we've discussed in class.
#
# Writing code from scratch helps you:
# - Develop a deeper understanding of Python syntax and logic.
# - Improve your problem-solving skills by working through challenges.
# - Gain confidence in implementing object-oriented principles and other key topics.
#
# Please sketch your implementations and logic on paper before writing code.
#
# Important: **Do not change the name of this file**.
# If you submit this file to Gradescope using a different file name, you will receive a penalty of **-10 points**.
#
# Please write your code below.

def flip_bit(num,bit_position):
    new_number=1<<bit_position
    num^=new_number
    return num

print(flip_bit(10,1))