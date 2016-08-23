str1,str2 =input(),input()
matrix = [[0]*(len(str2)+1) for i in range(len(str1)+1)]
for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]+1
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
print (matrix[len(str1)][len(str2)])
