import argparse
import os



def argparsemodule():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--filname",required=True)
    args = parser.parse_args()
    file = args.filname
    return file


def open_file(file):
    with open(file,"r") as f:
        return f.readlines()

def sort_dir(file):
    kwd = os.getcwd()
    with open("output.txt","w") as f:
        f.write("directorian ka"+"\n")
        for i in file:
           km = kwd + "/"+i.strip()
           if os.path.exists(km):
               f.write(i.strip() + "\n")
        f.write("directorian chka"+"\n")
        for i in file:
            lm = kwd + "/"+i.strip()
            if not os.path.exists(lm):
                os.makedirs(lm)
                f.write(i.strip()+"\n")

def main():

        km = argparsemodule()
        ls = open_file(km)
        sort_dir(ls)

if __name__ == "__main__":
    main()

