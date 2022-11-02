
from typing import List
from Expr import *
from tokenn import Tokenn
from lox import *
from TokenType import TokenType

class ParseError(RuntimeError):
    
    def __init__(self, token: Tokenn, message: str) -> None:
        super().__init__(message)
        self.token = token

class Parser:

    def __init__(self, tokens: List[Tokenn]) -> None:
        self.tokens = tokens
        self.current = 0
        
    def match(self,types:TokenType):
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
        if not self.isAtEnd():
           self.current += 1
           
        return self.previous()
    
    def isAtEnd(self):
        return self.peek().type == TokenType.EOF
    
    def peek(self):
        return self.tokens[self.current]
    
    def previous(self):        
        return self.tokens[self.current-1]

    
    def comparison(self):
        expr = self.term()

        while self.match(
                TokenType.GREATER,
                TokenType.GREATER_EQUAL,
                TokenType.LESS,
                TokenType.LESS_EQUAL,
        ):
            operator = self.previous()
            right = self.term()
            expr = Expr.Binary(expr, operator, right)

        return expr
    
    def term(self):
        
        expr = self.factor()
        
        while (self.match(
            TokenType.MINUS,
            TokenType.PLUS
        )):
            operator = self.previous()
            right = self.factor()
            expr = Expr.Binary(expr, operator, right)
        
        return expr
    
    def factor(self):
        expr = self.unary()
        
        while (self.match(
            TokenType.SLASH,
            TokenType.STAR
        )):
            operator = self.previous()
            right = self.unary()
            expr = Expr.Binary(expr, operator, right)
        
        return expr
    
    def unary(self):
        if self.match(
            TokenType.BANG,
            TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Expr.Unary(operator, right)
        return self.primary()
    
    def primary(self):
        
        if self.match(TokenType.FALSE): return Expr.Literal(False)
        if self.match(TokenType.TRUE): return Expr.Literal(True)
        if self.match(TokenType.NIL): return Expr.Literal(None)
        
        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Expr.Literal(self.previous().literal)
        
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Expr.Grouping(expr)
        raise self.error(self.peek(), 'Expect expression.')
    
    def ternary(self):
        expr = self.comparison()

        if self.match(TokenType.QUESTION):
            condition = self.previous()
            thenCond = self.comparison()
            self.consume(TokenType.COLON, "Expect ':' after expression.")
            elseCond = self.comparison()
            expr = Expr.Ternary(condition, thenCond, elseCond)

        return expr
        
    
    def consume(self, type : TokenType, message):
        if self.check(type):
            return self.advance()
        
        raise self.error(self.peek(), message)

    def error(self, token: Tokenn, message):
        
        return ParseError(token,message)
    
    def synchronize(self):
        
        self.advance()
        
        while ( not self.isAtEnd()):
            if self.previous().type == TokenType.SEMICOLON: return
            
            if self.peek().type in (
                TokenType.CLASS,
                TokenType.FUNCTION,
                TokenType.VAR,
                TokenType.FOR,
                TokenType.IF,
                TokenType.WHILE,
                TokenType.PRINT,
                TokenType.RETURN,
            ):
                return

            self.advance()
            
    def parse(self):
        
        try:
            return Expr
        except:
            return None
            


    