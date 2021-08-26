# python has a built in function called open which can be used to open files.
myfile = open('test.txt')
content = myfile.read()  # this function will read the file.
# resets the cursor back to beginning of text file so we can read it again.
myfile.seek(0)
print(content)


content = myfile.readlines()
myfile.seek(0)

for line in content:
    print(line)

myfile.close()  # always close the file after you've read.

# w+ is the mode which allows us to read and write.
# w and w+ should be used with caution as it overwrites the underlying file completely.
myfile = open('test.txt', 'w+')

myfile.write("The new Text")

content = myfile.read()
print(content)

myfile.close()

# APPEND TO A FILE

# a+ allows us to append to a file and if file does not exists, a+ will create a new file.
myfile = open('test.txt', 'a+')
myfile.write('MY FIRST LINE IS A+ OPENING')
myfile.close()

myfile = open('test.txt')
content = myfile.read()
print(content)
myfile.close()

# with is a context manager which automatically closes the file for us.
with open('test.txt', 'r') as mynewfile:
    myvariable = mynewfile.readlines()
