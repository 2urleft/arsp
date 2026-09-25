from collections import deque
from tokens import Token, TokenType
import re
import ast

MACRO_NAMES = ["func", "if", "ifelse", "let", "set", "incr", "decr", "pls", "mns", "mul", "div", "lt", "gt", "le", "ge", "or", "and", "not", "lst"]

class Parser():
    def __init__(self, tokens:list[Token]):
        self.tokens = tokens
        self.program_tree = ast.treeNode()
        self.path = deque() # think of this as a stack of nodes to push/pop for climbing in and out of depths
        self.current_node = self.program_tree
        
    def _add_child(self, node):
        if self.current_node.node_type in ("func", "program", "macro"):
            self.current_node.children.append(node)
        else:
            raise Exception(f"tried to add child {node} to {self.current_node}")
    
    def _walk(self, child_idx=-1):
        if self.current_node.node_type in ("func", "program", "macro"):
            self.path.append(self.current_node)
            self.current_node = self.current_node.children[child_idx]
        else:
            raise Exception(f"tried to walk from {self.current_node}")
    
    def _escape(self):
        self.current_node = self.path[-1]
        return self.path.pop()
    
    def _get_token(self, index):
        return self.tokens[index]
    
    def _get_ttype(self, index):
        return self._get_token(index).ttype
    
    def _comp_ttype(self, index, ttype):
        return self._get_ttype(index) == ttype
    
    def _get_lexeme(self, index):
        return self._get_token(index).lexeme
    
    def parse(self):
        current_index = 0
        while current_index < len(self.tokens):
            if self._comp_ttype(current_index, TokenType.LPAREN):
                current_index += 1 # get function token
                func_name = self._get_lexeme(current_index)
                if func_name in MACRO_NAMES:
                    self._add_child(ast.macroNode(self._get_lexeme(current_index)))
                else:
                    self._add_child(ast.funcNode(self._get_lexeme(current_index)))
                current_index += 1
                self._walk()
            elif self._comp_ttype(current_index, TokenType.RPAREN):
                current_index += 1
                self._escape()
            else:
                # TODO: macro recognition
                if self._comp_ttype(current_index, TokenType.T_NUMBER):
                    self._add_child(ast.numberNode(float(self._get_lexeme(current_index))))
                elif self._comp_ttype(current_index, TokenType.T_STRING):
                    self._add_child(ast.numberNode(re.sub(r"[\"']", '', self._get_lexeme(current_index))))
                elif self._comp_ttype(current_index, TokenType.T_BOOL):
                    value = None
                    if self._get_lexeme(current_index) == "true":
                        value = True
                    elif self._get_lexeme(current_index) == "false":
                        value = False
                    self._add_child(ast.boolNode(value))
                elif self._comp_ttype(current_index, TokenType.T_NIL):
                    self._add_child(ast.nilNode())
                else:
                    self._add_child(ast.identNode(self._get_lexeme(current_index)))
                current_index += 1
                
                
                    
            