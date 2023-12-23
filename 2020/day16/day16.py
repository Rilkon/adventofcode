from os.path import dirname, join
import re
import operator
import functools

content     = open(join(dirname(__file__), "./day16input.txt"), 'r').read()
lines       = content.split("\n")

def parse_rule(line):
    parsed_rule = dict()
    num_ranges   = []
    rule         = line.split(": ")
    
    for values in rule[1].split(" or "):
        pairs = [int(x) for x in values.split("-")]
        num_ranges.append(pairs)

    parsed_rule[rule[0]] = num_ranges
    return parsed_rule

def parse_set_of_rules(lines):
    parsed_rules = dict()
    for line in lines:
        parsed_rules.update(parse_rule(line))
    
    return parsed_rules

def is_rule_passed(value, rule):
    value = int(value)
    if (value >= rule[0][0] and value <= rule[0][1]) or (value >= rule[1][0] and value <= rule[1][1]):
        return True
    else:
        return False

def are_rules_passed_for_number(number, rules):
    for key in rules:
        if is_rule_passed(number, rules[key]) == True:
            return True
    return False

def are_rules_passed_for_numbers(numbers, rules):
    count = 0
    for number in numbers:
        if are_rules_passed_for_number(number, rules) == True:
            count+=1
    
    return count == len(numbers)

def get_total_rate_of_error(tickets, rules):
    failed_nums = []
    for ticket in tickets:
        for number in [int(x) for x in ticket.split(",")]:
            if are_rules_passed_for_number(number, rules) == False:
                failed_nums.append(number)

    return sum(failed_nums)

def get_error_rate_for_ticket(ticket, rules):
    failed_nums = []
    for number in [int(x) for x in ticket.split(",")]:
        if are_rules_passed_for_number(number, rules) == False:
            failed_nums.append(number)
    return sum(failed_nums)

def get_valid_tickets(tickets, rules):
    valid_tickets = []
    for ticket in other_tickets:
        if get_error_rate_for_ticket(ticket, ruleset) == 0:
            valid_tickets.append(ticket)
    return valid_tickets

def rule_matches_all_numbers(numbers, rule):
    count = 0
    for number in numbers:
        if is_rule_passed(number, rule) == True:
            count += 1
    return count == len(numbers)

def number_of_matches(numbers, rule):
    count = 0
    for number in numbers:
        if is_rule_passed(number, rule) == True:
            count += 1
    return count

def get_column(list_, n):
    return map(operator.itemgetter(n), list_)

ruleset = parse_set_of_rules(lines[0:20])
my_ticket = lines[22]
other_tickets = lines[25:]

print("Part1", get_total_rate_of_error(other_tickets, ruleset))
 
my_ticket_list = [int(x) for x in my_ticket.split(",")]
valid_tickets = [x.split(",") for x in get_valid_tickets(other_tickets, ruleset)]

indexes = {}
removed = set()

candidates = {rule: set() for rule in ruleset}

for column in range(len(valid_tickets[0])):
    values = [ticket[column] for ticket in valid_tickets]
    for key in enumerate(ruleset):
        if rule_matches_all_numbers(values, ruleset[key[1]]) == True:
            candidates[key[1]].add(column)

for column in range(len(valid_tickets[0])):
    for key in candidates:
        candidates_set = candidates[key] - removed

        if len(candidates_set) == 1:
            column = candidates_set.pop()
            indexes[key] = column
            removed.add(column)

product = 1
for column in indexes:
    if "departure" in column:
        product *= int(my_ticket_list[indexes[column]])

print("Part 2:", product)