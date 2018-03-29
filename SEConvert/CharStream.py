

import os
import sys

if sys.version_info[0] != 3:
    print("This script requires Python version 3.X.")
    sys.exit(1)



class CharStream(object):
    def __init__(self): 
        self.out = []
        self.src = None
        self.pos = 0
        pass

    def read_file(self, file_name):
        f = open(file_name, "rt")
        self.src = f.read()

    def peek_next(self):
        if self.pos < len(self.src):
            res = self.src[self.pos]
            return res  
        return '\0'

    def next(self):
        if self.pos < len(self.src):
            res = self.src[self.pos]
            self.pos += 1
            return res  
        return '\0'

    def match(self, str):

        if self.src[self.pos:].startswith(str):
            self.pos += len(str)
            return True
        return False

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    # Try to partse a section delimtered by start/end. If the start appears w/o
    # end, throw an exception.
    def try_parse(self, start, end = "\n"):
        if self.match(start) == False:
            return None

        result = ""

        while self.match(end) == False:
            c = self.next()

            if c == '\0':
                raise "Unterminated section {0} found without matching {1}".format(start, end)

            result += c
        
        return result