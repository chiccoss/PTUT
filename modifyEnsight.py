




def main():
    # read file
    file = open("file.txt", "r")
    lines = file.readlines()
    file.close()

    # patterns
    for line in lines:
        print(line)
        print("vcdf")


main()
