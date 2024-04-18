#Milion game
import random
import os

#We enter the name of the player
def input_name():
    name = input("Enter name: ")
    return name

#we take the questions and answers from the file and return them as a list
def open1_file(file):
    if os.path.exists(file):
        with open(file,encoding="utf-8") as file_quest:
            return file_quest.readlines()
    return None
#returns 10 questions with their answers in random order
def random_file(questions):
    milis = random.sample(questions,k = 10)
    return milis

#The game logic
def game_logic(file):
    try:
        point = 0
        for quest in file:
            print(quest[:quest.index("?")+1])
            answer = quest[quest.index("?")+1:-1]
            answer1 = answer.split(",")
            answer2 = answer.split(",")
            random.shuffle(answer1)
            print(",".join(answer1))
            user = input("Enter answer: ").lower()

            if user == answer2[0].lower():
                print("correct")
                point += 1
            else:
                print("wrong answer")
        return point
    except IndexError as index_error:
        print(index_error)
    return None
#Player results

def result(result_1,question_1):
    if result_1 == 10:
        return "You win"

    return "game over earned",result_1,"/",len(question_1)

#The player's name and score are entered in the new file
def top_play(file,name,point):
    if os.path.exists(file):
        with open(file,"a",encoding="utf-8") as file_1:
            file_1.write(name+":"+str(point)+" ")
#We pass the player name and scores to the library dictionary
def open2_file(file):
    try:
        top_dict = {}
        with open(file,"r",encoding="utf-8") as file_2:
            file_read = file_2.read()
            file_list = file_read.split()
            for i in file_list:
                top_dict[i[:i.index(":")]] = i[i.index(":")+1:]
        return top_dict
    except (IndexError,NameError) as error_1:
        print("error to index or nameerror",error_1)
    return None
#We sort the dictionary by values and sort in descending order
def sort_file(top_dict):
    top_list = list(top_dict.items())
    top_list.sort(key = lambda x:x[1],reverse = True)
    return top_list

#We pass the dictionary values back to the file
def write_file(fname,sort_list):
    if os.path.exists(fname):
        with open(fname,"w",encoding="utf-8") as file:
            for key,value in sort_list:
                file.write(key+":" +str(value) +"\n")

#In this function we pass the other functions
def main():
    try:
        name = input_name()
        filename = open1_file("quest.txt")
        randfile = random_file(filename)
        milion = game_logic(randfile)
        print(result(milion,randfile))
        top_play("top.txt",name,milion)
        opf = open2_file("top.txt")
        sort_list = sort_file(opf)
        write_file("top.txt",sort_list)
    except NameError as name_error:
        print(name_error)
if __name__ == "__main__":
    main()
