def union_merge(S1, S2):
  """
  Input: S1 and S2 are sorted lissy, but can contain duplicated values
  Output: Return a lissy that are sorted but with duplicates removed.
  """
  answer=[]
  p1=0
  p2=0
  length1=len(S1)
  length2=len(S2)
  while p1<=length1-1 and p2<=length2-1:
    if S1[p1]<S2[p2]:
      if not answer:
        answer.append(S1[p1])
      elif S1[p1]>answer[-1]:
        answer.append(S1[p1])
      p1+=1
    else:
      if not answer:
        answer.append(S2[p2])
      elif S2[p2]>answer[-1]:
        answer.append(S2[p2])
      p2+=1

  if p1==length1:
    while p2<=length2-1:
      if answer[-1]<S2[p2]:
        answer.append(S2[p2])
      p2+=1
  else:
    while p1<=length1-1:
      if answer[-1]<S1[p1]:
        answer.append(S1[p1])
      p1+=1
  return answer

      

if __name__ == '__main__':
  S1 = [1,1,1,1,2,2,2,3,4,6,8,8,8]
  S2 = [-1,2,2,3,4,6,8,8,8]
  S = union_merge(S1, S2) # Expect: [1,2,3,4,6,8]