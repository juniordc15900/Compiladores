from token import Token
class Scanner():

    def __init__(self,source):
        self.source = source
        tokens = [Token()]
    
    def isAtEnd(self,current):
        return current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    def addTokens(self,type,lexeme,literal,line):
        self.addToken(type,None)
    
    def addToken(self,type,lexeme,literal,start,current,line):
        text = self.source[start:current]
        self.tokens.append(Token(type,text,literal,line))

    def scanTokens(self,start=0,current=0,line=1):
        while not self.isAtEnd():
            start = current
            self.scanToken()
        self.tokens.append(Token("EOF","",None,line))    
        return self.tokens
        #return list of tokens
    
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