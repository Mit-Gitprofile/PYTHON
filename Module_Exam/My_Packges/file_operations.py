
def create_file(filename):              #crate a file
    print("Create:\n")
    file=open(filename,"a")
    file.close()
    print(f"File '{filename} created successfully...'")


def write_file(filename,str):           #write in file
    print("Write:\n")
    file=open(filename,"w")
    file.write(str+"\n")
    file.close()
    print(f"File '{filename} Written successfully...'")


def append_file(filename,content):      #append in file
    print("Append:\n")
    file=open(filename,"a")
    file.write(content+"\n")
    file.close()
    print(f"in file '{filename} Content Append successfully...'")
    

def read_file(filename):                #read a file
    print("Read:\n")
    file=open(filename,"r")
    print(file.read())
    file.close()
    print(f"File '{filename} read successfully...'")