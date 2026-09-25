from tokens import Token, TokenType

class Interpreter():
    def __init__(self, program_tree):
        self.program_tree = program_tree
        self.current_node = self.program_tree
        
    def visit(self): # receiver
        return self.current_node.visit()