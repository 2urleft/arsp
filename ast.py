class astNode():
    def __init__(self, node_type:str):
        self.node_type = node_type
    
    def visit(self):
        ... # override with other astNodes
    
    def __repr__(self):
        return f"{self.node_type}()"

class treeNode(astNode):
    def __init__(self):
        super().__init__("program")
        self.children = [] # not always initialized first
    
    def __repr__(self):
        return ";\n".join(c.__repr__() for c in self.children)

class numberNode(astNode):
    def __init__(self, value:float):
        super().__init__("num")
        self.value = value
    
    def visit(self):
        return self.value # literal for evaluation
    
    def __repr__(self):
        return f"n({self.value})"

class stringNode(astNode):
    def __init__(self, string:str):
        super().__init__("str")
        self.value = string
    
    def visit(self):
        return self.value # literal for evaluation
    
    def __repr__(self):
        return f"s(\"{self.value}\")"

class boolNode(astNode):
    def __init__(self, value:bool):
        super().__init__("bool")
        self.value = value
    
    def visit(self):
        return self.value # literal for evaluation
    
    def __repr__(self):
        return f"b({self.value})"

class nilNode(astNode):
    def __init__(self):
        super().__init__("nil")
    
    def visit(self):
        return None # can interpreter regard "None" as a value returned by a nil keyword?
        # it can be if the value serves its function of "representing alternative falsy value"
    
    def __repr__(self):
        return "nil"

class identNode(astNode):
    def __init__(self, name:str):
        super().__init__("ident")
        self.name = name
    
    def __repr__(self):
        return f"i({self.name})"

class funcNode(astNode):
    def __init__(self, name:str):
        super().__init__("func")
        self.name = name
        self.children = [] # not always initialized first
        
    def __repr__(self):
        return f"{self.name}({", ".join(c.__repr__() for c in self.children)})"
    
class macroNode(astNode):
    def __init__(self, name:str):
        super().__init__("macro")
        self.name = name
        self.children = [] # not always initialized first
    
    # TODO: add _visit_[macro] functions for each macro and match-case in visit()
    
    def __repr__(self):
        return f"{self.name}!({", ".join(c.__repr__() for c in self.children)})"