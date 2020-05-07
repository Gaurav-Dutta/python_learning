
filepath = "C:\\Python_Learning\\Data\\Example1.txt"

with open(filepath) as myfile:
    content = myfile.read()
    characters = len(content)
    print( f"Number of Characters: {characters}" )

with open(filepath) as myfile:
    lines = myfile.readlines()
    nLines = len(lines)
    print( f"Number of Lines: {nLines}" )

