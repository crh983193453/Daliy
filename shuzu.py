import numpy as np
a=np.arange(15)
print(a)
# =====================
b=np.eye(3)
print(b)
# ==============
c=np.ones((10,10))
for i in range(1,9):
    for j in range(1,9):
        c[i,j]=0
print(c)
# ====================
d=np.random.randint(0,100,size=(5,10))
for i in range(0,2):
    print(d[i])
# ======================
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[1,1,1],[1,1,1],[1,1,1]])
print(A+B)
print(np.matmul(A,B))