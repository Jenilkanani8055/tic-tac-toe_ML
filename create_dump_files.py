# unpack data dump back to an array
def unpack_txt_file(text):
    text = text.split("\n")
    temp = []
    for i in text[:-1]:
        temp.append(list(map(int, i[2:-1].split(", "))))
    return temp

# append array in file:
def write_dump_in(name,who_won, data):
    f = open(name, "a")
    f.write(who_won + str(data) + "\n")
    f.close()

# read the file:
def read_file(name):
    f = open(name, "r")
    lst = unpack_txt_file(f.read())
    return lst
    f.close