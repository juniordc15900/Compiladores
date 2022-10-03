from sys import argv
import os

class GenerateAst():

    def __init__(self):
        self.outputDir = ''

    def main(self,args):
        if (len(args)!=1):
            print('Usage....')
            exit()
        self.outputDir = args[0]
        self.defineAst(self.outputDir,"Expr",{"Binary" :"left: Expr ,operator: Token ,right: Expr",
                                          "Grouping":"expression: Expr",
                                           "Unary":"operator: Token,right: Expr",
                                           "Literal":"value: Object"})


   

    def defineAst(self,outputDir,baseName,types):
        path = f'{outputDir}/{baseName}.py'
        arq = open(f'{baseName}','w')
        arq.write(f'class {baseName}():')
        arq.write('\n')
        

        for type in types:
            className = type
            fields = str(types[type]).split(',')
            self.defineType(arq,baseName,className,fields)
        arq.close()

    def defineType(self,arq,baseName,className,fields):
        
        arq.write('\n')
        arq.write(f"    class {className}({baseName}):")
        arq.write('\n')
        #construtor
    
        arq.write(f"        def __init__(self,{','.join(fields)}):")
        arq.write('\n')
        arq.write(f"            super().__init__()")
        arq.write('\n')
        for field in fields:
            name = field[:field.find(':')]
            arq.write(f"            self.{name} = {name}")
            arq.write('\n')
            
    
    

    

if __name__ == '__main__':
    generate = GenerateAst()
    generate.main('tool')