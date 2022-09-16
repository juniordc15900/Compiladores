from TokenType import TokenType

class Token:
    
    def __init__(self,tipo,lexeme,literal,line) -> None:
        
        self.tipo = TokenType(tipo)
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self) -> str:
        return f"{self.tipo} {self.lexeme} {self.literal}"
    