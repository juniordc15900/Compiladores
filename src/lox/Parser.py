from parser import ParserError
from tokenn import Tokenn
from lox import Lox
from TokenType import TokenType
class Parser:

    def __init__(self):
        self.parseError = ParserError()
        self.tokens = []
        self.current = 0
        
    def match(self,types):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False
    
    def check(self,type:TokenType):
        if self.isAtEnd():
            return False
        return self.peek().type == type
    
    def advance(self):
        if self.isAtEnd():
            current += 1
        return self.previous()
    
    def isAtEnd(self):
        return self.peek().type == 'EOF'
    
    def peek():
        return Tokenn.get(current)
    
    def previous():
        return Tokenn.get(current-1)
    
    def comparision():
        return None
    
    def consume(self, type : TokenType, message):
        if self.check(type):
            return self.advance()
        raise self.error(self.peek(), message)

    def error(self, token: Tokenn, message):
        Lox.error(token,message)
        return self.parseError
    
    def synchronize(self):
        self.advance()
        while (self.isAtEnd()):
            if self.previous().type == TokenType.SEMICOLON: return
            


    