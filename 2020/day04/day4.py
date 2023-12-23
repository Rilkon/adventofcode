from os.path import dirname, join

current_dir = dirname(__file__)
file_path   = join(current_dir, "./day4input.txt")
f           = open(file_path, 'r')
content     = f.read()
lines       = content.split("\n")

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passports = []
passport = { "byr": "" , "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "", "cid": "" }

for line in lines:

    contents = line.split(" ")
    for contentline in contents:
        valuePair = contentline.split(":")

        if len(valuePair) < 2:
            passports.append(passport)
            passport = { "byr": "" , "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "", "cid": "" }
        else:
            passport[valuePair[0]] = valuePair[1]
passports.append(passport)

#validation 1
validPass = 0
for checkPass in passports:
    count = 0
    for key in required:
        if checkPass[key] == "": 
            count+= 1
    if count == 0:
        validPass+=1

#print(passports)

print(validPass)

    