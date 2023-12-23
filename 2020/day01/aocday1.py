from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./day1input.txt")
f = open(file_path, 'r')


content = f.read()
lines = content.split("\n")

result = 0

# part 1
for i in lines:
	for j in lines:
		if int(i) + int(j) == 2020:
 		result =  int(i) * int(j)
 		print(result)
 		exit()
            
#part 2
for i in lines:
	for j in lines:
		for k in lines:
        	if int(i) + int(j) + int(k) == 2020:
				result =  int(i) * int(j) * int(k)
				print(result)
				exit()

