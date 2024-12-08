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
        return {
            "kind": self.kind.value,
            "body": self.body

        }

# Expect to return a value
# An expression is a statement
class Expression(Statement):
    pass

# 4 + 5
class BinaryExpression(Expression):

    kind: NodeType
    left: Expression
    right: Expression
    operator: str

    def __init__(self, left, right, operator):
        self.kind = NodeType.BINARYEXPRESSION.value
        self.left = left
        self.right = right
        self.operator = operator
    
    def getJSON(self):

        return {
            "kind": self.kind,
            "left": self.left.getJSON() if hasattr(self.left, "getJSON") else self.left,
            "right": self.right.getJSON() if hasattr(self.right, "getJSON") else self.right,
            "operator": self.operator
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

    kind: NodeType
    value: int

    def __init__(self, value):
        self.kind = NodeType.NUMERICLITERAL.value
        self.value = value
    
    def getJson(self):
        return {
            "kind": self.kind,
            "value": self.value
        }