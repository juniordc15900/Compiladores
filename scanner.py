from tokenn import Tokenn
from tokentype import TokenType


class Scanner():

    def __init__(self,source):
        self.source = source
        self.tokens = []
        self.current = 0
        self.start = 0
    
    def isAtEnd(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    def addTokens(self,tipo,lexeme,literal,line):
        self.addToken(tipo)
    
    def addToken(self,tipo,literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Tokenn(tipo,text,literal,line=1))

    def match(self,expected):
        if self.isAtEnd():
            return False
        elif self.source[self.current] != expected:
            return False
        else:
            self.current+=1
            return True

    def peek(self):
        if(self.isAtEnd):
            return '\0'             #final de string em python
        return self.source(self.current)
    
    def string(self):
        while(self.peek() != '"' and not self.isAtEnd):
            if (self.peek() == '\n'):
                line +=1
            else:
                self.advance()
        if self.isAtEnd():
            Scanner.error(line, "Unterminated String")
            return

    def isDigit(c):
        return c >= '0' and c <= '9'

    def number(self):
        while self.isDigit(self.peek()):
            self.advance()
        if self.peek() == '.' and self.isDigit(self.peekNext()):
            self.advance()
            while self.isDigit(self.peek()):
                self.advance()

        self.addToken(NUMBER, float(source.substring(self.start, self.current)))
    def peekNext(self):
        if self.current +1 >= len(self.source):
            return '/0' #final de string

    def scanToken(self):
        c = self.advance()
        
        if c == "(":
            self.addToken(TokenType.LEFT_PAREN)
        elif c == ")":
            self.addToken(TokenType.RIGHT_PAREN)
        elif c == "{":
            self.addToken(TokenType.LEFT_BRACE)
        elif c == "}":
            self.addToken(TokenType.RIGHT_BRACE)
        elif c == ",":
            self.addToken(TokenType.COMMA)
        elif c == ".": 
            self.addToken(TokenType.DOT)
        elif c == "-":  
            self.addToken(TokenType.MINUS)
        elif c == "+":  
            self.addToken(TokenType.PLUS)
        elif c == ";":  
            self.addToken(TokenType.SEMICOLON)
        elif c == "*":  
            self.addToken(TokenType.STAR)
        elif c == "!":
            self.addToken(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG)
        elif c == "=":
            self.addToken(TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL)
        elif c == "<":
            self.addToken(TokenType.LESS_EQUAL if self.match("=") else TokenType.EQUAL)
        elif c == ">":
            self.addToken(TokenType.GREATER_EQUAL if self.match("=") else TokenType.EQUAL)
        elif c == "/":
            if self.match('/'):
                while (self.peek() != '/n' and not self.isAtEnd()):
                    self.advance()
            else:
                self.addToken(TokenType.SLASH)
        elif c == "/n":
            line+=1
        elif c == '"':
            self.string()
        else:
            if self.isDigit(c):
                self.number()
            else: 
                line=0
            Scanner.error(line, "Unespected character")

    
    def scanTokens(self,line=1):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        self.tokens.append(Tokenn(TokenType.EOF,"",None,line))    
        return self.tokens
        #return list of tokens