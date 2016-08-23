file = open("newfile.txt", "w")

file.write("hello world in the new file")

file.write("and another line")
file = open('newfile.txt', 'r')

print file.read()


file.close()

