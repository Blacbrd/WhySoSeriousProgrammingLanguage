# The lexer grabs whatever syntax you've written, and outputs an array of tokens
# For example, if your script had :  WHY so = serious:)
# Lexer : [TypeToken, IdentifierToken, EqualsToken, NumberToken]

from enum import Enum

# Used to allow the return of arrays
from typing import List

class TokenType(Enum):
    NUMBER = "number"
    STRING = "string"
    IDENTIFIER = "identifier"
    EQUALS = "equals"
    OPENPARENTHASIS = "openParenthasis"
    CLOSEPARENTHASIS = "closeParenthasis"

    # This is + or - or / or *
    BINARYOPERATION = "binaryOperation"

    # For now I will use let, i will later change this to accept data types
    LET = "let"

    # Shows where the end of the file is
    ENDLINE = "endLine"

    EOF = "EndOfFile"


class Token:

    def __init__(self, value : str, tokenType : TokenType):

        self.value = value
        self.tokenType = tokenType

        print(f"value = {self.value}")
        print(f"token type = {self.tokenType}")

# I will change the
keyWordDict = {
    "let": TokenType.LET,
}

# Ignores all white space, including spaces, new lines and tabs
def isSkippable(string : str):
    return string == " " or string == "\n" or string == "\t"

def tokenise(sourceCode: str):

    # Using position approach better than constantly removing from an array
    tokens = []
    pos = 0
    length = len(sourceCode)

    while pos < length:
        char = sourceCode[pos]

        if char == "(":
            tokens.append(Token(char, TokenType.OPENPARENTHASIS))
            pos += 1

        elif char == ")":
            tokens.append(Token(char, TokenType.CLOSEPARENTHASIS))
            pos += 1

        elif char in "+-*/%":

            tokens.append(Token(char, TokenType.BINARYOPERATION))
            pos += 1

        elif char == "=":
            tokens.append(Token(char, TokenType.EQUALS))
            pos += 1

        elif char.isalpha():

            identifier = []

            # Builds the string, while the variable continues having characters, it gets added to the identifier
            while pos < length and sourceCode[pos].isalnum():
                identifier.append(sourceCode[pos])
                pos += 1

            # .get() returns either the token type if the identifier exists in the dictionary, or TokenType.IDENTIFIER as default
            # .join merges all of the array components together, so if we have ["l", "e", "t"], we get "let"
            tokenType = keyWordDict.get("".join(identifier), TokenType.IDENTIFIER)

            # Appends token object
            tokens.append(Token("".join(identifier), tokenType))

        elif char.isnumeric():

            number = []

            while pos < length and sourceCode[pos].isnumeric():

                number.append(sourceCode[pos])
                pos += 1

            tokens.append(Token("".join(number), TokenType.NUMBER))

        elif isSkippable(char):
            # Skip white space
            pos += 1

        else:
            print(f"Unrecognised character '{char}' at position {pos}")
            return False
    
    # Adds end of file token at the very end
    tokens.append(Token("EndOfFile", TokenType.EOF))
    return tokens