# The parser lets us break up the code for further processing

    
    # Orders of importance (what we do first):

    # PrimaryExpression
    # UnaryExpression
    # MultiplicativeExpression
    # AdditiveExpression
    # ComparisonExpression
    # LogicalExpression
    # FunctionCall
    # MemberExpression
    # AssignmentExpression

# Whatever has the most priority is passed in last as that gives it more presidence within the AST

from frontend.abstractSyntaxTree import Statement, Program, Expression, BinaryExpression, NumericLiteral, Identifier
from frontend.lexer import tokenise, Token, TokenType
import sys

class Parser:

    def __init__(self):
        
        # Token array
        self.tokens = []
    
    def notEof(self):

        # Return true if not end of line
        print(f"Current: {self.tokens[0].tokenType}")
        return self.tokens[0].tokenType != TokenType.EOF

    def parseStatement(self):
        # Function decleration
        # Variable decleration
        # While loops

        return self.parseExpression()
    
    def parseExpression(self):
        return self.parseAdditiveExpression()
    
    # 10 + 5 - 5
    # Left hand presidence, therefore we evaluate left first
    def parseAdditiveExpression(self):
        left = self.parsePrimaryExpression()

        # While there are still operators
        while self.currentToken().value == "+" or self.currentToken().value == "-":

            # Gets the operator we're dealing with
            operator = self.advance().value

            # Now we check the right hand side
            right = self.parsePrimaryExpression()

            # Since left can have multiple expressions, such as
            # (((10 + 4) - 2) + 2)
            # We need to account for this using recursion
            # So first value will be 10
            # Then it will become 10 + 4
            # Then it will become 10 + 4 - 2 etc.
            left = BinaryExpression(left, right, operator)
        
        return left.getJSON()
    
    # Returns current function
    def currentToken(self):
        return self.tokens[0]
    
    # Moves the list onwards, similar to how we did in the Lexer
    # This can also be known as "eat"
    def advance(self):
        previous = self.currentToken()
        del self.tokens[0]
        return previous
    
    def parsePrimaryExpression(self):

        # This is the current token
        token = self.currentToken().tokenType

        # Checks the type of the token, and then creates objects
        match token:

            case TokenType.IDENTIFIER:
                identifier = Identifier(self.advance().value)
                return identifier.getJSON()
            
            case TokenType.NUMBER:
                number = NumericLiteral(self.advance().value)
                return number.getJson()
            
            case _:

                print(f"Unexpected token found: {self.currentToken().tokenType}")

                # Tricks compiler
                sys.exit([1])
    
    # Adds tokens to the abstract syntax tree
    def produceAST(self, sourceCode):

        self.tokens = tokenise(sourceCode)
        
        # The body inside the program will be an array of statements
        program = Program([])

        # Parse until end of file
        while self.notEof():

            program.body.append(self.parseStatement())

        return program
