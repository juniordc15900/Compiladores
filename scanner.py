from token import Token
from lox import Lox
class Scanner():

    def __init__(self,source):
        self.source = source
        self.tokens = [Token()]
        self.current = 0
    
    def isAtEnd(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    def addTokens(self,tipo,lexeme,literal,line):
        self.addToken(tipo)
    
    def addToken(self,tipo):
        text = self.source[start:self.current]
        self.tokens.append(Token(tipo,text,literal,line))

    def match(self,expected):
        if self.isAtEnd():
            return False
        elif self.source(self.current) != expected:
            return False
        else:
            self.current+=1
            return True

    def peek(self):
        if(self.isAtEnd):
            return '\0'             #final de string em python
        return source(self.current)
    
    def string(self):
        while(self.peek() != '"' and not self.isAtEnd):
            if (self.peek() == '\n'):
                line +=1
            else:
                self.advance()
        if self.isAtEnd():
            Lox.error(line, "Unterminated String")
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

        self.addToken(NUMBER, float(source.substring(start, current)))
    def peekNext(self):
        if self.current +1 >= len(self.source):
            return '/0' #final de string

    def scanToken(self):
        c = self.advance()
        
        if c == "(":
            self.addToken("LEFT_PAREN")
        elif c == ")":
            self.addToken("RIGHT_PAREN")
        elif c == "{":
            self.addToken("LEFT_BRACE")
        elif c == "}":
            self.addToken("RIGHT_BRACE")
        elif c == ",":
            self.addToken("COMMA")
        elif c == ".": 
            self.addToken("DOT")
        elif c == "-":  
            self.addToken("MINUS")
        elif c == "+":  
            self.addToken("PLUS")
        elif c == ";":  
            self.addToken("SEMICOLON")
        elif c == "*":  
            self.addToken("STAR")
        elif c == "!":
            self.addToken("BANG_EQUAL" if self.match("=") else "BANG")
        elif c == "=":
            self.addToken("EQUAL_EQUAL" if self.match("=") else "EQUAL")
        elif c == "<":
            self.addToken("LESS_EQUAL" if self.match("=") else "EQUAL")
        elif c == ">":
            self.addToken("GREATER_EQUAL" if self.match("=") else "EQUAL")
        elif c == "/":
            if match('/'):
                while (self.peek() != '/n' and not self.isAtEnd()):
                    self.advance()
            else:
                self.addToken("SLASH")
        elif c == "/n":
            line+=1
        elif c == '"':
            self.string()
        else:
            if self.isDigit(c):
                number()
            else: 
                Lox.error(line, "Unespected character")

    
    def scanTokens(self,start=0,line=1):
        while not self.isAtEnd():
            start = self.current
            self.scanToken()
            self.tokens.append(Token("EOF","",None,line))    
            return self.tokens
        #return list of tokens