lenght=int(input())
index=0
sequence=[0]*lenght
for i in range(lenght):
	sequence[i]=int(input())
#print sequence
temp=[0]*lenght
#print sequence[0]
temp[0]=sequence[0]
#print temp
for i in range(1,lenght):
	if sequence[i]>temp[index]:
		index+=1
		temp[index]=sequence[i]
	elif sequence[i]<temp[0]:
		temp[0]=sequence[i]
	else:
		maximum=index
		minimum=0
		while(maximum>=minimum):
			middle=(maximum+minimum)//2
			if(sequence[i]>temp[middle] and sequence[i]<temp[middle+1]):
				temp[middle+1]=sequence[i]
				break
			elif sequence[i]<temp[middle]:
				maximum=middle-1
			else:
				minimum=middle+1
print(index+1)
				
