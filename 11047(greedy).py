input_data=input().split(' ')
N=int(input_data[0])
K=int(input_data[1])
coin=[]
count=[]
Sum=0
for n in range(N):
    coin.append(int(input()))
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
