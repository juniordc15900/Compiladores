from lox import Lox
from TokenType import TokenType

class Token:
    
    def __init__(self,lexeme,literal,line) -> None:
        
        type = TokenType()
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self) -> str:
        return f"{type} {self.lexeme} {self.literal}"
    