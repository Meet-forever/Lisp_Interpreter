from LISPParser import parser

expression_operations = ['aop', 'if']
boolean_operations = ['and', 'or', 'not', 'comparison']
list_operations = ['cdr', 'car', 'cons']


def eval(tree: list):
    if tree == None:
        return ['NONE', '']

    if tree[0] == 'number' or tree[0] in expression_operations:
        value = eval_expression(tree)
        return value

    elif tree[0] == 'boolean' or tree[0] in boolean_operations:
        value = eval_boolean(tree)
        return value

    elif tree[0] == 'list' or tree[0] in list_operations:
        value = eval_list(tree)
        return value

    else:
        return ['NONE', '']


def eval_expression(tree):
    if tree[0] == 'number':
        return ['OK', tree[1]]

    elif tree[0] == 'aop':
        x = eval(tree[2])
        if x[0] == 'ERROR':
            return x
        y = eval(tree[3])
        if y[0] == 'ERROR':
            return y

        if tree[1] == '+':
            return ['OK', x[1]+y[1]]
        elif tree[1] == '-':
            return ['OK', x[1]-y[1]]
        elif tree[1] == '*':
            return ['OK', x[1]*y[1]]
        elif y[1] != 0:
            return ['OK', x[1]/y[1]]
        else:
            return ['ERROR', 'ArithmeticError: Cannot divide by 0!']

    elif tree[0] == 'if':
        boolval = eval(tree[1])
        exp1 = eval(tree[2])
        exp2 = eval(tree[3])

        if boolval[1]:
            return ['OK', exp1[1]]
        else:
            return ['OK', exp2[1]]


def eval_boolean(tree):

    if tree[0] == 'boolean':
        return ['OK', tree[1]]

    elif tree[0] == 'and' or tree[0] == 'or':
        boolean1, boolean2 = None, None
        if isinstance(tree[1], bool):
            boolean1 = ['OK', tree[1]]
        else:
            boolean1 = eval_boolean(tree[1])

        if boolean1[0] == 'ERROR':
            return boolean1

        if isinstance(tree[2], bool):
            boolean2 = ['OK', tree[2]]
        else:
            boolean2 = eval_boolean(tree[2])

        if boolean2[0] == 'ERROR':
            return boolean2

        if tree[0] == 'and':
            return ['OK', boolean1[1] & boolean2[1]]
        else:
            return ['OK', boolean1[1] | boolean2[1]]

    elif tree[0] == 'not':
        boolean1 = None
        if isinstance(tree[1], bool):
            boolean1 = ['OK', tree[1]]
        else:
            boolean1 = eval_boolean(tree[1])

        if boolean1[0] == 'ERROR':
            return boolean1
        else:
            return ['OK', not boolean1[1]]

    elif tree[0] == 'comparison':
        number1, number2 = None, None
        if isinstance(tree[2], float):
            number1 = ['OK', tree[2]]
        else:
            number1 = eval(tree[2])
        if number1[0] == 'ERROR':
            return number1

        if isinstance(tree[3], float):
            number2 = ['OK', tree[3]]
        else:
            number2 = eval(tree[3])
        if number2[0] == 'ERROR':
            return number2

        if tree[1] == '>=':
            return ['OK', number1[1] >= number2[1]]
        elif tree[1] == '<=':
            return ['OK', number1[1] <= number2[1]]
        elif tree[1] == '>':
            return ['OK', number1[1] > number2[1]]
        elif tree[1] == '<':
            return ['OK', number1[1] < number2[1]]
        elif tree[1] == '=':
            return ['OK', number1[1] == number2[1]]
        elif tree[1] == '<>':
            return ['OK', number1[1] != number2[1]]


def eval_list(tree):
    if tree[0] == 'list':
        store = ""
        for item in tree[1]:
            store += str(eval(item)[1]) + " "

        return ['OK', '(' + store.strip() + ')']

    elif tree[0] == 'cdr':
        nums = eval(tree[1])
        if nums[0] == 'ERROR':
            return nums

        nums[1] = nums[1].strip('(').strip(')').split(' ')
        if len(nums[1][0]) == 0:
            return ['ERROR', 'Error: Cannot CDR on an empty list!']
        else:
            nums[1].pop(0)
            return ['OK', '(' + ' '.join(nums[1]) + ')']

    elif tree[0] == 'car':
        cur = eval(tree[1])
        if cur[0] == 'ERROR':
            return cur
        else:
            cur[1] = cur[1].strip('(').strip(')').split(' ')[0]
        if not cur[1]:
            return ['ERROR', 'Error: List is empty!']
        else:
            cur[1] = float(cur[1])
        return ['OK', cur[1]]

    elif tree[0] == 'cons':
        val = eval(tree[1])
        if val[0] == 'ERROR':
            return val
        nums = eval_list(tree[2])
        if nums[0] == 'ERROR':
            return nums
        else:
            nums[1] = '(' + \
                f'{str(val[1])} {nums[1].strip("(").strip(")")}'.strip() + ')'
            return ['OK', nums[1]]


def read_input():
    result = ''
    while True:
        data = input('LISP: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i+1]
            break
        else:
            result += data + ' '
    return result


def main():
    while True:
        data = read_input()
        if data == 'exit;':
            print("GoodBye!\n")
            break
        try:
            tree = parser.parse(data)
        except Exception as inst:
            print(inst.args[0])
            continue
        # print(tree if tree else '')
        try:
            answer = eval(tree)
            if answer[0] == 'ERROR':
                print(f'{answer[1]}\n')
            elif answer[0] == 'NONE':
                pass
            else:
                print(f'{answer[1]}\n')
        except Exception as inst:
            print(inst.args[0])


main()