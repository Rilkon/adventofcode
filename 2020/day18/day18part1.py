from os.path import dirname, join
import operator 
import re

content     = open(join(dirname(__file__), "./day18input.txt"), 'r').read()
input_data  = content.split("\n")


def makespace_for_brackets(line):
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")
    if line[len(line)-1] == " ":
        line = line[:-1]
    return line


class Calculator(object):

    def get_matching_parentheses(self, tokens, start):
        count = 1
        for i, token in enumerate(tokens[start + 1:]):
            if token == '(':
                count += 1
            elif token == ')':
                count -= 1

            if count == 0:
                return start + i + 1
        raise ValueError('No matching parenthesis')

    def get_token(self, tokens, index):
        token = tokens[index]
        if token == '(':
            end = self.get_matching_parentheses(tokens, index)
            val = self.eval_tokens(tokens[index + 1:end])
            end += 1
        else:
            end = index + 1
            val = float(tokens[index])
        return val, end

    def eval_tokens(self, tokens):
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return float(tokens[0])

        left_val, left_end = self.get_token(tokens, 0)
        op = tokens[left_end]
        right_val, right_end = self.get_token(tokens, left_end + 1)

# part 1 operations
        if op == "+":
            val = left_val + right_val
        elif op == "-":  # sub
            val = left_val - right_val
        elif op == "/":
            val = left_val / right_val
        else:  # mult
            val = left_val * right_val
        return self.eval_tokens([val] + tokens[right_end:])


    def evaluate_part1(self, string):
        num_sym = re.compile("([0-9.]+|[^ 0-9])")
        tokens = re.findall(num_sym, string)
        return self.eval_tokens(tokens)

    
input_data = [makespace_for_brackets(line) for line in input_data]
my_calc = Calculator()


print("Part1, ", sum([my_calc.evaluate_part1(line) for line in input_data]))


