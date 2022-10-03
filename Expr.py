class Expr():



class exprVisitor(ABC):

    @abstractmethod
    def visit_binary_expr(self,expr: Expr):
        pass

    @abstractmethod
    def visit_grouping_expr(self,expr: Expr):
        pass

    @abstractmethod
    def visit_unary_expr(self,expr: Expr):
        pass

    @abstractmethod
    def visit_literal_expr(self,expr: Expr):
        pass

    class Binary(Expr):
        def __init__(self,left: Expr ,operator: Token ,right: Expr):
            super().__init__()
            self.left = left
            self.operator = operator
            self.right = right

    class Grouping(Expr):
        def __init__(self,expression: Expr):
            super().__init__()
            self.expression = expression

    class Unary(Expr):
        def __init__(self,operator: Token,right: Expr):
            super().__init__()
            self.operator = operator
            self.right = right

    class Literal(Expr):
        def __init__(self,value: Any):
            super().__init__()
            self.value = value
