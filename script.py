#!/usr/bin/python3

import xlsxwriter
import argparse


def open_file(file):
    with open(file, "r") as f:
        return f.readlines()
def print_g_help():
    print("first write the letter -f and write the name of the file from where you need to take people's information, then write the letter -e and write the name of your Excel file, then you can write -s and write the name of the profession you want to move the other sheet and that's it")
def parser_args():
    parser =argparse.ArgumentParser(description = "enter the data")
    parser.add_argument("-f","--filename",required=True,help="file name")
    parser.add_argument("-e","--exelfile",required=True,help="Exel file name")
    parser.add_argument("-s","--separate",help="Enter the profession with the letter -s and place it in a separate sheet")

    g_parser = argparse.ArgumentParser(add_help=False)
    g_parser.add_argument("-g", "--g-help", action="store_true", help="Print help message for the -g option")
    args, _ = g_parser.parse_known_args()
    if args.g_help:
        print_g_help()
        exit()
    return args.filename,args.exelfile,args.separate

def main(file1,outputxl,separate):

    file = open_file(file1)

    workbook = xlsxwriter.Workbook(outputxl)
    worksheet = workbook.add_worksheet()
    worksheet2 = workbook.add_worksheet("sheet2")
    worksheet3 = workbook.add_worksheet("sheet3")

    green_format = workbook.add_format({'bg_color': '#00FF00'})
    yellow_format = workbook.add_format({'bg_color': '#FFFF00'})
    bold_format = workbook.add_format({'bold': True})

    for row_num, line in enumerate(file):
        ml = line.strip().split()
        for col_num, value in enumerate(ml):
            if row_num == 0:
                worksheet.write(row_num, col_num, value, green_format)
            elif  row_num != 0 and int(ml[2]) > 35:
                worksheet.write(row_num, col_num, value, yellow_format)
                worksheet2.write(row_num, col_num, value)
            else:
                worksheet.write(row_num, col_num, value)
            if ml[3].lower() == separate:
                worksheet3.write(row_num,col_num,value)


    workbook.close()
if __name__ == "__main__":
    file,exel,separate = parser_args()
    main(file,exel,separate)


