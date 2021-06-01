#/usr/bin/python3

####################################################################
# Script Name : convert-docs.py
# Description : Utilizes pandoc to convert between two file types.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import os
import sys

if len(sys.argv) <= 1:
    print (f"Execute this command with the following arguments:")
    print (f"python3 {sys.argv[0]} <input file name>.extension")
    sys.exit(1)

def main():
    file_in()
    file_out()
    os.system(f'pandoc -f {file_ext} -t {flavor} -o {file_name}.md {sys.argv[1]}')
    #print (f'(os.system(pandoc -f {file_ext} -t {flavor} -o {file_name}.md {sys.argv[1]}')

def file_in():
    global file_ext
    global file_name
    ingest = sys.argv[1]
    ingest_ext = ingest.split('.')
    file_name = (ingest_ext[0])
    file_ext = (ingest_ext[-1])

def file_out():
    global flavor
    os.system('cls' if os.name == 'nt' else 'clear')
    print ()
    print (f"Markdown Flavors")
    print (f"----------------")
    print (f"1.) Github Markdown")
    print (f"2.) Traditional Markdown")
    print ()
    flavor = input ("Please select which flavor of markdown desired for conversion [1-2]: ")
    if flavor == "1":
        flavor = "gfm"
    elif flavor == "2":
        flavor = "markdown"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ()
        print ("Please select a valid extension")
        print ("No changes have been made")
        exit(1)


if __name__ == "__main__":
    main()


#pandoc -f docx -t gfm -o test.md test.docx

# pandoc -f {file_ext} -t {flavor} -o {file_name}.md {sys.argv[1]}