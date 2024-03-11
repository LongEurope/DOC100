#Improving snake, and having a high score. This will be done by writing files.
#Manipulating file systems

#with open('my_file.txt', mode='r'/'w'/'a') as file: yadda yadda yadda

#The reason that the plain file name wasn't working was because the indentation of the file location was 
# always wrong, it is supposed to be in the same indentation as DOC100 folder.

# So just copy as path and use rpath <- this is an absolute path, if the file we're trying to find a file
# that is in the same folder (called the working directory) we can use the relative file path to get to the
# file path. Relative file path is in fomrat of .\file.txt (this searches for the file in the specific
# working directory). i.e. relative path starts from folder, absolute starts from root.