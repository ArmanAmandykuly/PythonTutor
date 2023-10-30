class TypeChecker:
    def nonNegative(x):
        x = TypeChecker.isNumber(x)
        if x < 0:
            raise RuntimeError("Number should be non-negative")
        return x
    
    def isNumber(x):
        if type(x) not in [int, float]:
            raise TypeError("This field should be a number(int, float)")
        return x
    
    def nonNull(x):
        if x == None:
            raise RuntimeError("Object should be non null")
        return x
    
    def nonEmpty(x):
        if type(x) != str:
            raise TypeError("This field should be string")
        if x == "":
            raise RuntimeError("String shouldn't be empty")
        
        return x
    
    def integer(x):
        if type(x) != int:
            raise TypeError("This field must be integer")
        return x
    
    def isTypeEq(x, needType):
        if type(x) != needType:
            raise TypeError("This field must be " + str(needType))
        return x
    
    def isDigit(x:str):
        if x.isdigit():
            return x
        raise RuntimeError(x, " should be a number")