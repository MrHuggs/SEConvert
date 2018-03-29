
import os
import sys

if sys.version_info[0] != 3:
    print("This script requires Python version 3.X.")
    sys.exit(1)

# Look at the contents of a file and make a guess as to whether or not is a tex file.
#
# Our heuristic is to check for bad characeters (0 or non-ascii), and then to see
# if it also has the common Tex characters:
#
def is_tex_file(file_name):
    f = open(file_name, "rb")
    
    required_chars = set()
    for c in ['$', '\\', '{', '}']:
        required_chars.add(ord(c))

    try:
        contents = f.read()

        for b in contents:
            if b == 0 or b > 127:
                return False
            
            if b in required_chars:
                required_chars.remove(b)

    finally:
        f.close()

    return len(required_chars) == 0

if __name__ == '__main__':
    file_name = sys.argv[1]    
    print ("{0} is binary: {1}".format(file_name, is_tex_file(file_name)))
