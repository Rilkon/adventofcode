from os.path import dirname, join
import re

current_dir = dirname(__file__)
file_path   = join(current_dir, "./day4input.txt")
f           = open(file_path, 'r')
content     = f.read()
lines       = content.split("\n")

# required keys
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

#passport dictionary + initial line
passports = []
passport = { "byr": "" , "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "", "cid": "" }

# build a dictionary of passports for easier use later (thought this was a good idea in part 1)
for line in lines:
    contents = line.split(" ")
    for contentline in contents:
        valuePair = contentline.split(":")

        if len(valuePair) < 2:
            # happens when there is a full linebreak which indicates one set of passport data 
            # -> append current passport and make a new one
            passports.append(passport)
            passport = { "byr": "" , "iyr": "", "eyr": "", "hgt": "", "hcl": "", "ecl": "", "pid": "", "cid": "" }
        else:
            #set the proper value at the key of the dictionary
            passport[valuePair[0]] = valuePair[1]

# Dont forget to append the last one (this can probably solved in a cleaner loop above but meh)
passports.append(passport)

#validation
validPass   = 0
invalidPass = 0
for checkPass in passports:
    try:
        # part 1 / get rid of the empty ones with regards to required fields
        for key in required:
            if checkPass[key] == "": 
                raise Exception("ZONK")

        # for the remaining (full set of fields) do detailed checks    
        # birth year
        if not (1920 <= int(checkPass["byr"]) <= 2002): raise Exception("ZONK") 
        # issue year
        if not (2010 <= int(checkPass["iyr"]) <= 2020): raise Exception("ZONK")
        # expiration year
        if not (2020 <= int(checkPass["eyr"]) <= 2030): raise Exception("ZONK")

        # height (this can probably be improved a lot)
        if checkPass["hgt"] != "":
            r = re.compile(r"(\d+)(cm|in)")
            m = r.match(checkPass["hgt"])
            if m is not None:
                height = m.groups()
                if height[1] == "cm":
                    if not( 150 <= int(height[0]) <= 193) :
                        raise Exception("ZONK")
                
                elif height[1] == "in":
                    if not( 59 <= int(height[0]) <= 76) :
                        raise Exception("ZONK")
                else:
                    raise Exception("ZONK")
            else:
                raise Exception("ZONK")
        else:
            raise Exception("ZONK")

        # hair color
        r = re.compile(r"(#)([a-f0-9]){6}")
        m = r.match(checkPass["hcl"])
        if m is None:
            raise Exception("ZONK")

        # Eye color
        if checkPass["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            raise Exception("ZONK")
        
        # Passport ID
        if not(checkPass["pid"].isdigit() and len(checkPass["pid"]) == 9):
            raise Exception("ZONK")

        #if we reach this without any failed validation we have a valid passport
        validPass+=1    
    except Exception as err:
        invalidPass+= 1

print("Total number of passports:", len(passports))
print("Number of valid passports:", validPass)
print("Number of invalid passports:", invalidPass)


    