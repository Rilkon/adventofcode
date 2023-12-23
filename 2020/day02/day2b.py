from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./day2input.txt")
f = open(file_path, 'r')

content = f.read()
lines = content.split("\n")

count = 0

for text in lines:
    
    word        = text.split(" ")
    rule        = word[0].split("-")
    rule_upper  = int(rule[1])
    rule_lower  = int(rule[0])
    rule_letter = word[1][0]
    password    = word[2]
    
    int_count = 0
    if (password[int(rule_lower) - 1 ] == rule_letter):
        int_count+= 1 
    if (password[int(rule_upper) - 1 ] == rule_letter):
        int_count+= 1
         
    if (int_count == 1):
        count+= 1

print(count)



    
    