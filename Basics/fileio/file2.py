#files can be read by using open/read/close sequence, however, forgetting to cal close may cause memory leaks
#python has a way to automatically close a file after usage by using the "with" keyword

filepath = "C:\\Python_Learning\\Data\\Example1.txt"
with open(filepath) as myfile:
    c = myfile.read()
    print(c)
    