# TODO How to open an existing text file and read the contents on it


# create a file - use the absolute path to file - but for this example we will use the content path
file = open("file.txt", 'r')  # by default it opens the file in r - read mode

# grab the text inside the file
print(file.read())

# remember to close the file
file.close()  # must close file after opening

# TODO ANOTHER WAY TO READ THE FILE USING WITH
with open('file.txt', 'r') as file:  # open file as ' file '
    print(file.read())  # once ran through indent block of code --> file will automatically close

# using readlines()- gives a list
with open('file.txt') as file:
    # print(file.readlines())
    line1 = file.readlines()[0]  # since this is a list extract the first line of the file
    print([line1])
