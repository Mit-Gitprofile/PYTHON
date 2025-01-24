
def file(filename,string):
    with open(filename,"r+") as file:
        file.close()
    with open(filename,"w+") as file:
        file.write(string)
    with open(filename,"r+") as file:
        print(file.read())




