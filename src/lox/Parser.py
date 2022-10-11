class Parser:

    def match(types: TokenType):
        for type in types:
            if check(type):
                advance()
                return True
        return False
    
    def check(type:TokenType):
        if isAtEnd():
            return False
        return peek().type == type
    
    def advance(self):
        if isAtEnd():
            current += 1
        return previous()
    
    def isAtEnd():
        return peek().type == 'EOF'
    
    def peek():
        return Tokkens.get(current)
    
    def previous():
        return Tokkens.get(current-1)
    
    def comparision():
        return None