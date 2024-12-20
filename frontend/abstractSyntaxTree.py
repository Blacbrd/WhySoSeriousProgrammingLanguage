# Program is an array of all of our statements
# https://astexplorer.net/
# Website above is a good visualisation of what is going on behind the scenes
# The abstract syntax tree is the glue between front end and backend, a protocol
# Most ASTs operate on a JSON structure
# https://www.youtube.com/watch?v=wINY109MG10
# Essentially, we want to generate a JSON file that represents an AST


from enum import Enum
from abc import ABC, abstractmethod

class NodeType(Enum):

    PROGRAM = "Program"
    NUMERICLITERAL = "NumericLiteral"
    IDENTIFIER = "Identifier"
    BINARYEXPRESSION = "BinaryExpression"

# Abstract class
# Statements will not return a value, therefore they are not expressions
class Statement(ABC):

    kind: NodeType

class Program(Statement):
    
    kind: NodeType
    body: Statement

    def __init__(self, body):
        self.kind = NodeType.PROGRAM
        self.body = body
    
    def getJSON(self):

        # This gets the JSON for each statement in the body
        return {
            "kind": self.kind.value,
            "body": [statement.getJSON() for statement in self.body]
        }

# Expect to return a value
# An expression is a statement
class Expression(Statement):
    pass

# 4 + 5
class BinaryExpression:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator
        self.kind = NodeType.BINARYEXPRESSION

    def getJSON(self):
        return {
            "kind": self.kind.value if hasattr(self.kind, "value") else self.kind,
            "operator": self.operator,
            "left": self.left.getJSON() if hasattr(self.left, "getJSON") else self.left,
            "right": self.right.getJSON() if hasattr(self.right, "getJSON") else self.right,
        }

class Identifier(Expression):

    kind: NodeType

    # This is our variable or value
    symbol: str

    def __init__(self, symbol):
        self.kind = NodeType.IDENTIFIER.value
        self.symbol = symbol
    
    def getJSON(self):
        return {
            "kind": self.kind,
            "symbol": self.symbol
        }

class NumericLiteral(Expression):
    value: float

    def __init__(self, value):
        self.value = float(value)  # Ensure it's converted to a float
        self.kind = NodeType.NUMERICLITERAL.value

    def getJSON(self):
        return {
            "kind": self.kind.value if hasattr(self.kind, "value") else self.kind,
            "value": self.value
        }