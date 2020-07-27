from numpy import *

m= array([['mon',18,20,22,17],['tue',11,18,21,18],
          ['wed',15,21,20,19],['thu',11,20,22,21],
          ['fri',18,17,23,22],['sat',12,22,20,18],
         ['sun',13,15,19,16]])
# m=reshape(a,(7,5))
# print(m)
# print(m[2])
# print(m[6][4])

# m_r=append(m,[['aug',12,15,13,11]],0)
# print(m_r)

# m_c=insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)
# print(m_c)

# m_d=delete(m,[2],0)
# print(m_d)

# m_d=delete(m,s_[3],1)
# print(m)
# print(m_d)

m[3]=['thu',0,0,0,0]
print(m)
