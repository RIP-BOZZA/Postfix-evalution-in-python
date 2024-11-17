"""


Infix representation :
    The general mathematical way of representing algebraic expressions is to write the operator between operands: 
        Example: a + b. Such representation is called the Infix representation.
Postfix represntation:
     If we write the operator after the operands Example:
       a b +, it is called the Postfix representation. It is also called the "Reverse Polish notation"


Applications of stack

    - processing of function calls
        in every function calls the control jumps to that function ,it can be tracked

        when a function(e.g. main) is called an execution frame is called in the stack ,
        stack stores the function,variables and locations
        now after another function calls antoher frame is created in the top
        this go on like every funtion call is made

        when every function returns the stack is cleared

        recursice funtion also uses stack
            in recursion conditon there need to be base condition or termination conditon to stop the recursion
        
    - posix expression evalutaion
    - conversion of infix to prefix /post fix expression evaluation

        post fix expression evaluation

"""


# postfix expression evaluation in python

def postfix_evaluation(expression):# Postfix notation, also known as Reverse Polish Notation (RPN)
    expressions_array =expression.split(" ")
    stack =[]
    for obj in expressions_array:
        if obj.isdigit():
            stack.append(int(obj))
        elif obj=='+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1+num2)
        elif obj=='-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2-num1)
        elif obj=='*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 * num1)
        elif obj=='/':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2/num1)
    return stack


print(postfix_evaluation("2 3 + 9 -"))