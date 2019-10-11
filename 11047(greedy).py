import sys
N,K=map(int,sys.stdin.readline().split())
coin=[]
count=[]
Sum=0
for n in range(N):
    coin.append(int(sys.stdin.readline()))
    count.append(0)
j=N
while(Sum!=K):
    for i in reversed(range(j)):
        if coin[i]<=K-Sum:
            count[i]=(K-Sum)//coin[i]
            Sum+=coin[i]*count[i]
            j=i
            break
print(sum(count))
