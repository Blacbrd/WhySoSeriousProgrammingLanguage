# I got to 7:20!!!


from values import RuntimeValue
import sys

class Envirmonment():

    def __init__(self, parent, variables):
        
        self.parent = parent
        self.variables = {}
    
    def declareVariable(self, variableName, value):

        if self.variables[variableName]:
            raise f"Cannot declare variable {variableName}. It is already defined"

        self.variables[variableName] = value
        return value
    
    def assignVariable(self, variableName, value):

        
        pass

    # Allows us to traverse the scope
    def resolve(self, variableName):

        # Global scope
        if self.variables[variableName]:
            return self
        
        # Parent scope
        if self.parent == None:
            raise f"Cannot resolve {variableName}, as it does not exist"
        
        return self.parent.resolve(variableName)