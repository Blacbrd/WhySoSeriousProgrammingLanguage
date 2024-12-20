import sys

class Environment():

    # def __init__(self, parent, variables):
    def __init__(self, parent):
        
        self.parent = parent
        self.variables = {}
    
    def declareVariable(self, variableName, value):

        if variableName in self.variables:
            print(f"Cannot declare variable {variableName}. It is already defined")
            sys.exit(4)

        self.variables[variableName] = value
        return value
    
    def assignVariable(self, variableName, value):

        env = self.resolve(variableName)
        env.variables[variableName] = value
        
        return value

    def lookUpVariable(self, variableName):

        # Checks for variable in the scope
        env = self.resolve(variableName)

        # Returns the value of the variable
        return env.variables.get(variableName)

    # Allows us to traverse the scope
    # It checks all the parents until no parents are left
    def resolve(self, variableName):

        # Check if current scope has it
        if variableName in self.variables:
            return self
        
        # If it has a parent
        if self.parent == None:
            print(f"Cannot resolve {variableName}, as it does not exist")
            sys.exit(4)
        
        # Go to the parent scope and check if it's there
        return self.parent.resolve(variableName)