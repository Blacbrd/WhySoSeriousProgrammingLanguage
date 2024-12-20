from runtime.values import ValueType, NullValue, NumberValue
from frontend.abstractSyntaxTree import NodeType, NumericLiteral
import sys

# Evaluate numeric binary expressions
def evaluateNumericBinaryExpression(lhs, rhs, operator):

    # If it is not a number/int/float
    if not isinstance(lhs, NumberValue) or not isinstance(rhs, NumberValue):
        print(f"Cannot perform numeric operation on non-numeric values: {lhs}, {rhs}")
        sys.exit(3)

    if operator == "+":
        return NumberValue(lhs.value + rhs.value)
    elif operator == "-":
        return NumberValue(lhs.value - rhs.value)
    elif operator == "*":
        return NumberValue(lhs.value * rhs.value)
    elif operator == "/":

        # Makes it so that you cant divide by zero
        if rhs.value == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return NumberValue(lhs.value / rhs.value)

    else:
        raise ValueError(f"Unsupported operator: {operator}")

# Evaluate any binary expression
def evaluateBinaryExpression(binaryOperation, env):
    leftHandSide = evaluate(binaryOperation.left, env)
    rightHandSide = evaluate(binaryOperation.right, env)

    if isinstance(leftHandSide, NumberValue) and isinstance(rightHandSide, NumberValue):
        # Perform numeric operations
        return evaluateNumericBinaryExpression(leftHandSide, rightHandSide, binaryOperation.operator)
    
    # Handle other cases if needed (e.g., string concatenation or logical operators)
    print(f"Unsupported operand types for {binaryOperation.operator}: {type(leftHandSide)}, {type(rightHandSide)}")
    sys.exit(3)

# Evaluate a program
def evaluateProgram(program, env):
    lastEvaluated = NullValue()

    for statement in program.body:
        lastEvaluated = evaluate(statement, env)

    return lastEvaluated

def evaluateIdentifier(identifier, env):

    # Symbol is the name of the variable
    value = env.lookUpVariable(identifier.symbol)
    return value

# Evaluate an AST node
# Environment tells us which variables we have access to
def evaluate(astNode, env):
    match astNode.kind:
        case NodeType.NUMERICLITERAL.value:
            return NumberValue(astNode.value)
        
        case NodeType.IDENTIFIER.value:
            return evaluateIdentifier(astNode, env)

        case NodeType.BINARYEXPRESSION:
            return evaluateBinaryExpression(astNode, env)

        case NodeType.PROGRAM:
            return evaluateProgram(astNode, env)

        case _:
            print(f"This AST node has not yet been implemented: {astNode.kind}")
            sys.exit(3)