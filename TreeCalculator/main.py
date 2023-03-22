import operator
import re
from data_structures import stack, BinaryTree


def infixToPostfix(infix_expr):
    """ Converting the infix expression to the postfix """
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = stack()
    postfixList = []

    tokenList = re.split(r'([-*(+)^/])', infix_expr)

    for _ in range(len(tokenList)):
        token = tokenList[_]
        if token not in "/()+*-^":
            postfixList.append(token)
        # useless in case of not fully parenthesized expression
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


def evaluate(parseTree):
    """ Evaluate the parse tree """
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": "^"}
    leftC = parseTree.get_left()  # store left child in leftC
    rightC = parseTree.get_right()  # store right child in rightC

    if leftC and rightC:  # execute if node have 2 children
        fn = operators[parseTree.getRootVal()]  # ' A <<< operator >>> B ' assign the operator to fn
        if fn == "^":  # in case if the operator is a power, we treat it in a special way
            return round(pow(evaluate(leftC), evaluate(rightC)), 2)
        else:
            return round(fn(evaluate(leftC), evaluate(rightC)), 2)
    else:
        return float(parseTree.getRootVal())


def ParseTree(infix):
    """ Building the tree without fully parenthesized expression """
    post_exp = infixToPostfix(infix)
    token_list = post_exp.split()
    p_stak = stack()
    etree = BinaryTree("")
    p_stak.push(etree)
    current = etree
    for token in reversed(token_list):
        if token in "+-^/*":  # token is an operator
            current.setRootVal(token)  # put its value in the current node
            current.insertright("")  # insert a right node
            p_stak.push(current)  # push the current value to the stack
            current = current.get_right()  # move the current to the right node
        else:  # token is an operand
            current.setRootVal(token)  # put its value in the current node
            # move the the current back to the parent node using the previous value from the stack
            current = p_stak.pop()

            if not p_stak.isEmpty():  # check the stack if it is empty then, get out
                current.insertLeft("")
                current = current.get_left()

    return current


def summation(parseTree):
    leftC = parseTree.get_left()  # store left child in leftC
    rightC = parseTree.get_right()  # store right child in rightC

    if leftC and rightC:
        return summation(leftC) + summation(rightC)
    else:
        return float(parseTree.getRootVal())


def opersum(parseTree):
    leftC = parseTree.get_left()  # store left child in leftC
    rightC = parseTree.get_right()  # store right child in rightC
    if leftC and rightC:
        return 1 + opersum(leftC) + opersum(rightC)
    else:
        return 0


def print_tree(root, level=0):
    if root:
        print_tree(root.get_right(), level + 1)
        print(' ' * 4 * level + '->', root.getRootVal())
        print_tree(root.get_left(), level + 1)


infix_exp = input("Enter an expression infix : ")

tree = ParseTree(infix_exp)  # build the tree using parseTree.
print_tree(tree)

print("Postfix expression: ", infixToPostfix(infix_exp))  # convert infix to postfix.
print(
    "The Evaluation to the 3rd decimal = {:.3f}".format(
        evaluate(tree)))  # here we restricted the output to show only 2 decimal point.
print('Summation of all operands :{:.3f}'.format(summation(tree)))
print('Count of all operators : ', opersum(tree))
