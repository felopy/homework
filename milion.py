#Million game
import random


def input_name():
    name = input("Enter name: ")
    return name

def open1_file(file):
    f = open(file)
    return f.readlines()


def rand_file(questions):
    milis = random.sample(questions,k = 10)
    return milis


def milion_logic(file):
    point = 0
    for quest in file:
        print(quest[:quest.index("?")+1])
        ma = quest[quest.index("?")+1:-1]
        mas = ma.split(",")
        km = ma.split(",")
        random.shuffle(mas)

        print(",".join(mas))
        user = input("Enter answer: ").lower()

        if user == km[0].lower():
            print("correct")
            point += 1
        else:
            print("wrong answer")
    return point

def result(res,mil):
    if res == 10:
        return "You win"
    else:
        return "game over earned",res,"/",len(mil)

def top_play(file,nam,mil):
    with open(file,"a") as f:
        f.write(nam+":"+str(mil)+" ")

def open2_file(fil):
    top_dict = {}
    with open(fil,"r") as f:
        m = f.read()
        sm = m.split()
        for i in sm:
            top_dict[i[:i.index(":")]] = i[i.index(":")+1:]
    return top_dict

def sort_file(dc):
    mk = list(dc.items())
    mk.sort(key = lambda x:x[1],reverse = True)
    return mk

def write_file(fname,sort_L):
    with open(fname,"w") as f:
        for k ,v in sort_L:
            f.write(k+":" +str(v) +"\n")

def main():
    name = input_name()
    filename = open1_file("quest.txt")
    randfile = rand_file(filename)
    milion = milion_logic(randfile)
    print(result(milion,randfile))
    top_play("top.txt",name,milion)
    opf = open2_file("top.txt")
    sort_list = sort_file(opf)
    write_file("top.txt",sort_list)
if __name__ == "__main__":
    main()

