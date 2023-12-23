from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./day2input.txt")
f = open(file_path, 'r')


content = f.read()
lines = content.split("\n")

test = [
"1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc"
]

rule_upper   = 0
rule_lower   = 0
rule_letter = "a"
password    = "bb"
count = 0

for text in lines:
    
    word = text.split(" ")
    #print(word)
    rule = word[0].split("-")
    #print(rule)
    rule_upper = rule[1]
    #print(rule_upper)
    rule_lower = rule[0]
    #print(rule_lower)
    rule_letter = word[1][0]
    #print(rule_letter)
    password = word[2]
    #print(password)
    
    if int(rule_upper) >= int(password.count(rule_letter)) & int(password.count(rule_letter)) >= int(rule_lower):
        count+= 1

print(count)



    
    