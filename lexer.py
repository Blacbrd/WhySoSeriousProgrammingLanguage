# The lexer grabs whatever syntax you've written, and outputs an array of tokens
# For example, if your script had :  WHY so = serious:)
# Lexer : [TypeToken, IdentifierToken, EqualsToken, NumberToken]

from enum import Enum

# Used to allow the return of arrays
from typing import List

class TokenType(Enum):
    NUMBER = None
    IDENTIFIER = None
    EQUALS = None
    OPENPARENTHASIS = None
    CLOSEPARENTHASIS = None
    BINARYOPERATION = None

    # For now I will use let, i will later change this to accept data types
    LET = None

class Token:

    def __init__(self, value : str, tokenType : TokenType):

        self.value = value
        self.tokenType = tokenType

# This specifies that the return type has to be specifically an array of tokens
def tokenise (sourceCode: str) -> List[Token]:

    tokens = []

    # Every character of the source code will be split up into an array
    src = sourceCode.split("")

    # 
    while len(src) > 0:
        pass


    return tokens