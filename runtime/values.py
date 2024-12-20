from enum import Enum

class ValueType(Enum):

    NULLTYPE = "null"
    NUMBERTYPE = "number"
    BOOLEAN = "boolean"

class RuntimeValue():
    type: ValueType

class NullValue(RuntimeValue):
    type: ValueType

    def __init__(self):
        self.type = ValueType.NULLTYPE
        self.value = None
    
    def getJSON(self):

        return {
            "type": self.type.value,
            "value": self.value
        }

class NumberValue(RuntimeValue):
    
    type: ValueType

    def __init__(self, number):
        self.type = ValueType.NUMBERTYPE
        self.value = number
    
    def getJSON(self):

        return {
            "type": self.type.value,
            "value": self.value
        }

class BooleanValue(RuntimeValue):
    
    type: ValueType

    def __init__(self, boolean):
        self.type = ValueType.BOOLEAN
        self.value = boolean
    
    def getJSON(self):

        return {
            "type": self.type.value,
            "value": self.value
        }