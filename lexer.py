# The lexer grabs whatever syntax you've written, and outputs an array of tokens
# For example, if your script had :  WHY so = serious:)
# Lexer : [TypeToken, IdentifierToken, EqualsToken, NumberToken]

from enum import Enum

# Used to allow the return of arrays
from typing import List

class TokenType(Enum):
    NUMBER = "number"
    IDENTIFIER = "identifier"
    EQUALS = "equals"
    OPENPARENTHASIS = "openParenthasis"
    CLOSEPARENTHASIS = "closeParenthasis"

    # This is + or - or / or *
    BINARYOPERATION = "binaryOperation"

    # For now I will use let, i will later change this to accept data types
    LET = None

class Token:

    def __init__(self, value : str, tokenType : TokenType):

        self.value = value
        self.tokenType = tokenType

        print(f"value = {self.value}")
        print(f"token type = {self.tokenType}")

# I will change the
keyWordDict = {
    "let": TokenType.LET
}

def removeFirstChar(src):
    src.pop(0)

# Ignores all white space, including spaces, new lines and tabs
def isSkippable(string : str):
    return string == " " or string == "\n" or string == "\t"

def tokenise (sourceCode: str):

    tokens = []

    # Every character of the source code will be split up into an array
    src = list(sourceCode)

    # While the source code isn't empty:
    while src:

        print(len(src))
        print(src[0])
        
        # If parenthasis, then make open parenthasis token
        if src[0] == "(":
            tokens.append(Token(src[0], TokenType.OPENPARENTHASIS))
            removeFirstChar(src)
        
        elif src[0] == ")":
            tokens.append(Token(src[0], TokenType.CLOSEPARENTHASIS))
            removeFirstChar(src)
        
        elif src[0] == "+" or src[0] == "-" or src[0] == "*" or src[0] == "/":
            tokens.append(Token(src[0], TokenType.BINARYOPERATION))
            removeFirstChar(src)
        
        elif src[0] == "=":
            tokens.append(Token(src[0], TokenType.EQUALS))
            removeFirstChar(src)
        

        
        # Handle multicharacter tokens:
        else: 
            
            if src and src[0].isalpha():
                
                identifier = ""
                while src and src[0].isalnum():

                    # If it starts with a letter, append to identifier while more letters and or numbers are present
                    identifier += src[0]
                    removeFirstChar(src)
                
                # If not in dictionary, it is a user defined variable
                # If in dictionary, it fetches the token type and adds to array
                try:
                    value = keyWordDict[identifier]
                    tokens.append(Token(identifier, value))

                except KeyError:
                    tokens.append(Token(identifier, TokenType.IDENTIFIER))

            
            # If it starts with a number
            # I will change this later to allow for different base
            elif src and src[0].isnumeric():

                number = ""
                while src and src[0].isnumeric():

                    # While there are numbers in a row, it will append numbers to this variable
                    number += src[0]
                    removeFirstChar(src)
                
                tokens.append(Token(number, TokenType.NUMBER))
            
            elif isSkippable(src[0]):
                removeFirstChar(src)
            
            else:
                print("Unrecognised character found in source code: ", src[0])
                return False


    return tokens

sourceCode = "let hello1 = 122"
tokenList = tokenise(sourceCode)
print(tokenList)