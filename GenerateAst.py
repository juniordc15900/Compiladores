from sys import argv

class GenerateAst():

    def __init__(self):
        self.outputDir = ''

    def main(self,args):
        if (len(args)!=1):
            print('Usage....')
            exit()
        self.outputDir = args[0]
        self.__defineAst(self.outputDir,"Expr",["Binary : Expr left, Token operator, Expr right",
                                          "Grouping:Expr expression",
                                           "Unary:Token operator, Expr right",
                                           "Literal:Object value"])


   

    @staticmethod
    def defineAst(outputDir,baseName,types):
        print(outputDir)
        path = f'{outputDir}/{baseName}.py'
        arq = open(f'{baseName}.py','w')
        arq.write(f'class {baseName}():')

        for type in types:
            className = type.split(':')[0].strip()
            fields = type.split(':')[1].strip()
            self.defineType(arq,baseName,className,fields)
        arq.close()

    @staticmethod
    def defineType(self,arq,baseName,className,fields):
        arq.write(f" class {className}({baseName}):")
        #construtor
        arq.write("     def __init__(): ")
        arq.write(f"        super(). ")
        fields = fields.split(',')
        for field in fields:
            name = field.splt(' ')[1]
            arq.write(f"        self.{name} = {name}")
    
    

    

if __name__ == '__main__':
    generate = GenerateAst()
    generate.main(argv[0:])