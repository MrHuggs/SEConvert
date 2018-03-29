import os
import sys
from charstream import CharStream


if sys.version_info[0] != 3:
    print("This script requires Python version 3.X.")
    sys.exit(1)

TEX_HEADER = r"""
\documentclass[a4paper]{article}

%% Language and font encodings
\usepackage[english]{babel}
\usepackage[utf8x]{inputenc}
\usepackage[T1]{fontenc}

%% Sets page size and margins
\usepackage[a4paper,top=3cm,bottom=2cm,left=.5cm,right=.5cm,marginparwidth=1.75cm]{geometry}

%% Useful packages
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage[colorinlistoftodos]{todonotes}
\usepackage[colorlinks=true, allcolors=blue]{hyperref}
\setlength{\parskip}{1em}
"""

TEX_FOOTER = r"""\end{document}"""



class SEParser(object):
    def __init__(self): 
        output = ""
        pass


    def _try_parse_inline_math(self):
        math = self.char_stream.try_parse("$", "$")
        if math == None:
            return False

        print ("Inline math:", math)
        self.output += "${0}$".format(math)


    def _try_parse_display_math(self):
        math = self.char_stream.try_parse("$$", "$$")
        if math == None:
            return False

        self.output +=  "\\begin{{align}}{0}\n\\end{{align}}".format(math)
        print ("Math:", math)

        return True


    def _try_parse_section(self):
        section = self.char_stream.try_parse("**", "**")
        if section == None:
            return False

        self.output +=  "\\section{{{0}}}".format(section)
        print ("Section:", section)
        return True


    def parse(self, char_stream):
        self.char_stream = char_stream

        self.output = TEX_HEADER

        while True:
            if self._try_parse_display_math():
                continue
            if self._try_parse_inline_math():
                continue
            if self._try_parse_section():
                continue

            c = self.char_stream.next()

            if c == '\0':
                break;

            print(c)
            self.output += c



        self.output += TEX_FOOTER
        return self.output


if __name__ == '__main__':
    str = sys.argv[1]    

    c = CharStream();
    c.read_file(str)


    parser = SEParser()
    output = parser.parse(c)

    out = open("output.tex", "wt")
    out.write(output)

                      

  

