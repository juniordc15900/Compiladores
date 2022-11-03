from tokenn import Tokenn
from TokenType import TokenType

class Scanner():

    def __init__(self,source):
        self.source = source
        self.tokens = []
        self.current = 0
        self.start = 0
        self.line = 1
        self.keywords = {
            "AND": TokenType.AND,
            "CLASS": TokenType.CLASS,
            "ELSE": TokenType.ELSE,
            "FALSE": TokenType.FALSE,
            "FUN": TokenType.FUN,
            "FOR": TokenType.FOR,
            "IF": TokenType.IF,
            "NIL": TokenType.NIL,
            "OR": TokenType.OR,
            "PRINT": TokenType.PRINT,
            "RETURN": TokenType.RETURN,
            "SUPER": TokenType.SUPER,
            "THIS": TokenType.THIS,
            "TRUE": TokenType.TRUE,
            "VAR": TokenType.VAR,
            "WHILE": TokenType.WHILE
        }
    
    def error(self,line,message):
        print(message)
    
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
        if(self.isAtEnd()):
            return '/0'             #final de string em python
        return self.source[self.current]

    def peekNext(self):
        if self.current +1 >= len(self.source):
            return '/0' #final de string
        else:
            return self.source[self.current+1]
    def string(self):
        while(self.peek() != '"' and not self.isAtEnd()):
            if (self.peek() == '\n'):
                self.line +=1
            else:
                self.advance()
        if self.match('"'):
            tipo = TokenType.STRING
            self.addToken(tipo)     
        if self.isAtEnd():
            self.error(self.line, "Unterminated String")
            return


    def isDigit(self,c):
        return c >= '0' and c <= '9'
    
    def isAlpha(self,c):
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_' 
    
    def isAlphaNumeric(self,c):
        return self.isAlpha(c) or self.isDigit(c)
    
    def identifier(self):
        while self.isAlphaNumeric(self.peek()):
            self.advance()
        text = self.source[self.start:self.current]
        try:
            tipo = self.keywords[text.upper()]
        except:
            tipo = TokenType.IDENTIFIER
        self.addToken(tipo)
        

    def number(self):
        while self.isDigit(self.peek()):
            self.advance()
        if self.peek() == '.' and self.isDigit(self.peekNext()):
            self.advance()
            while self.isDigit(self.peek()):
                self.advance()

        self.addToken(TokenType.NUMBER)
    
    def isComment(self):
        while (self.peek() != '*' and not self.isAtEnd()):
            self.advance()
            # if self.peek() == '\n':
            #     self.line += 1
        self.advance()
        if self.match('/'):
            return True

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
        elif c == ">":
            self.addToken(TokenType.GREATER)
        elif c == "<":
            self.addToken(TokenType.LESS)
        elif c == "!":
            self.addToken(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG)
        elif c == "=":
            self.addToken(TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL)
        elif c == "<":
            self.addToken(TokenType.LESS_EQUAL if self.match("=") else TokenType.EQUAL)
        elif c == ">":
            self.addToken(TokenType.GREATER_EQUAL if self.match("=") else TokenType.EQUAL)
        elif c == "?":
            self.addToken(TokenType.QUESTION)
        elif c == ":": 
            self.addToken(TokenType.COLON)
        elif c == "/":
            if self.match('/'):
                while (self.peek() != '/n' and not self.isAtEnd()):
                    self.advance()
            elif self.match('*'):
                if self.isComment():
                    self.addToken(TokenType.COMMENT)

            else:
                self.addToken(TokenType.SLASH)
        elif c == "/n":
            self.line+=1
        elif c == '"':
            self.string()
        elif c == ' ':
            pass
        else:
            if self.isDigit(c):
                self.number()
            elif self.isAlpha(c):
                self.identifier()
            else: 
                self.line=0
                self.error(self.line, "Unespected character")

    
    def scanTokens(self,line=1):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        self.tokens.append(Tokenn(TokenType.EOF,"",None,line))    
        return self.tokens
        #return list of tokens