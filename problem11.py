# problem: Input a filename and print the extension of that
fileName = input()
file_ext = fileName.split(".")
print("The file extension is ", file_ext[-1])
