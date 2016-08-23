
import sys
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count=1
b=0
for i in range(0,n):
    for j in range(0,(n-count)):
        sum=a[j]+a[j+count]
    
        if sum%k==0:
            b=b+1
    count=count+1
        
print(b)
