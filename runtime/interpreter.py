from runtime.values import ValueType, NullValue, NumberValue
from frontend.abstractSyntaxTree import NodeType, NumericLiteral
import sys

# Evaluate numeric binary expressions
def evaluateNumericBinaryExpression(lhs, rhs, operator):

    # If it is not a number/int/float
    if not isinstance(lhs, NumberValue) or not isinstance(rhs, NumberValue):
        raise TypeError(f"Cannot perform numeric operation on non-numeric values: {lhs}, {rhs}")

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
    
    elif operator == "**":
        return NumberValue(lhs.value ** rhs.value)
    else:
        raise ValueError(f"Unsupported operator: {operator}")

# Evaluate any binary expression
def evaluateBinaryExpression(binaryOperation):
    leftHandSide = evaluate(binaryOperation.left)
    rightHandSide = evaluate(binaryOperation.right)

    if isinstance(leftHandSide, NumberValue) and isinstance(rightHandSide, NumberValue):
        # Perform numeric operations
        return evaluateNumericBinaryExpression(leftHandSide, rightHandSide, binaryOperation.operator)
    
    # Handle other cases if needed (e.g., string concatenation or logical operators)
    raise TypeError(f"Unsupported operand types for {binaryOperation.operator}: {type(leftHandSide)}, {type(rightHandSide)}")

# Evaluate a program
def evaluateProgram(program):
    lastEvaluated = NullValue()

    for statement in program.body:
        lastEvaluated = evaluate(statement)

    return lastEvaluated

# Evaluate an AST node
def evaluate(astNode):
    match astNode.kind:
        case NodeType.NUMERICLITERAL.value:
            return NumberValue(astNode.value)

        case NodeType.NULLLITERAL.value:
            return NullValue()

        case NodeType.BINARYEXPRESSION:
            return evaluateBinaryExpression(astNode)

        case NodeType.PROGRAM:
            return evaluateProgram(astNode)

        case _:
            print(f"This AST node has not yet been implemented: {astNode.kind}")
            sys.exit(3)