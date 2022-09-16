from token import Token


class Scanner():

    def __init__(self,source):
        self.source = source
        self.tokens = []
        self.current = 0
    
    def isAtEnd(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    def addTokens(self,tipo,lexeme,literal,line):
        self.addToken(tipo)
    
    def addToken(self,tipo,start=0):
        text = self.source[start:self.current]
        self.tokens.append(Token(tipo,text,literal,line=0))

    def match(self,expected):
        if self.isAtEnd():
            return False
        elif self.source(self.current) != expected:
            return False
        else:
            self.current+=1
            return True


    
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
        else:
            line=0
            Scanner.error(line,"Unspected character")
    
    def scanTokens(self,start=0,line=1):
        while not self.isAtEnd():
            start = self.current
            self.scanToken()
            self.tokens.append(Token("EOF","",None,line))    
            return self.tokens
        #return list of tokens