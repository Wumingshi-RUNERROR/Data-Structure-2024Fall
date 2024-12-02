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

class Person():
    def __init__(self,first_name,last_name,hobby):
        self.first_name=first_name
        self.last_name=last_name
        self.hobby=hobby

    def introduce(self):
        answer=('Hi, my name is {0} {1}. I like {2}.'.format(self.first_name,self.last_name,self.hobby))
        return answer
    
p1=Person("Xukun","Cai","singing, dancing, rapping and playing basketball")
p2=Person("Alin","Gu","skating")
p3=Person("Zhen","Ding","smoking")

print(p1.introduce(),p2.introduce(),p3.introduce(),sep='\n')