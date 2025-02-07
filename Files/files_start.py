#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("test.txt", "w+")

    # Open the file for appending text to the end
    myfile = open("test.txt", "a")

    # write some lines of data to the file
    for i in range(10):
        myfile.write(f"This is line {i+1}\n")

    # lose the file when done
    myfile.close()

    # Open the file back up and read the contents
    myfile = open("test.txt", "r")
    if myfile.mode == "r":
        # content = myfile.read()
        # print(content)
        lines = myfile.readlines()  # readlines reads the individual lines into a list
        # for line in lines:
        #     print(line)
        print(lines)  # print the list of lines
    myfile.close()  # close the file when done

    # Open the file back up and read the contents


if __name__ == "__main__":
    main()
