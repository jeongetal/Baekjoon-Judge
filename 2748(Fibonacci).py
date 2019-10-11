import sys
n=int(sys.stdin.readline())
F=[]
for i in range(n+1):
    F.append(0)
F[0]=0
F[1]=1
for i in range(2,n+1):
    if F[i]==0:
        F[i]=F[i-2]+F[i-1]
print(F[n])