

def create_file():
    file=open("file_test.txt", 'w')
    file.write("Cyber Threat")
    file.close()

    read=open("file_test.txt", 'r')
    read_file=read.read()
    print(read_file)

create_file()


def list():
    list=["1 2 3 4 ", "5 4 3 2"]
    f=open("file_using_list.txt", 'w')
    f.writelines(list)
    f.close

list()


def create_file_using_with():
    with open("file.with.txt", 'w') as w:
        data=("create file using with")
        w.write(data)

    with open("file.with.txt", 'r') as r:
        data=r.read()
        print(data)

create_file_using_with()

