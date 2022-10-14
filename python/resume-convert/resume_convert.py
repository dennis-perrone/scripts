#!/usr/bin/python3
"""
Script Name : convert.py
Description : Converts a markdown resume and generates a styled
              html and pdf document.
Args :
Author : Dennis Perrone
GitHub : www.github.com/dennis-perrone
"""

import os
from pathlib import Path
import pathlib
import sys
import shutil
from datetime import datetime

HOME = str(Path.home())
resume_dir = f'{HOME}/development/resume/versions'
archive_dir = f'{HOME}/development/resume/archives'
pandoc = "podman run -it --rm -v $PWD:/work:Z -w /work pandoc/latex"
date = datetime.now().strftime("%Y-%m-%d")

# https://www.tutorialspoint.com/python3/python_variable_types.htm
ext = ('md', 'html', 'pdf')

def markdown_to_html():
    """
    Convert the Markdown (.md) resume into a styled HTML document.
    """
    for path, subdirs, files in os.walk(resume_dir):
        for subdir in subdirs:
            os.system(f'{pandoc} versions/{subdir}/resume.{ext[0]}\
            -c resume.css --template styles/resume-one-page.\
            {ext[1]} -o versions/{subdir}/resume-{date}.{ext[1]} \
            --metadata title=resume-{date} --data-dir .')
            print ("Converting markdown resume from the " + subdir +" directory...")

def html_to_pdf():
    """
    Convert the styled HTML document into a clean PDF file.
    """
    for path, subdirs, files in os.walk(resume_dir):
        for subdir in subdirs:
            os.system(f'chromium-browser --headless --print-to-pdf-no-header --enable-logging=stderr --log-level=2 --print-to-pdf=versions/{subdir}/resume-{date}.pdf versions/{subdir}/resume-{date}.html')
            shutil.copyfile(f'{resume_dir}/{subdir}/resume-{date}.pdf', f'{resume_dir}/{subdir}/perrone-resume.pdf')
            print ("Converting the html resume from the " + subdir +" directory to pdf...")

def html_for_convert():
    """
    Show files that are available to convert. This is used more
    for debugging then actual use.
    """
    for root, subdirs, files in os.walk(resume_dir):
        for file in files:
            if file.endswith(ext[0]):
                print(os.path.join(root, file))

def archive_resume(directory):
    """
    Moves newly generated resume into the archive folder for quicker
    future reference.
    """
    if pathlib.Path(directory).exists():
        shutil.copyfile(f'{resume_dir}/{niche}/resume-{date}.pdf', f'{directory}/perrone-resume.pdf')
        shutil.copyfile(f'{resume_dir}/{niche}/resume.md', f'{directory}/resume.md')
    else:
        os.mkdir(directory)
        shutil.copyfile(f'{resume_dir}/{niche}/resume-{date}.pdf', f'{directory}/perrone-resume.pdf')
        shutil.copyfile(f'{resume_dir}/{niche}/resume.md', f'{directory}/resume.md')

def main():
    """
    Main function to tie everything together.
    """
    global niche

    title = "Resume Updater"
    print (title)
    print (len(title) * "-")

    resumes = []
    for path, subdirs, files in os.walk(resume_dir):
        for subdir in subdirs:
            resumes.append(subdir)

    resumes.append("all")

    for i in range(len(resumes)):
        print(f"{i+1}. {resumes[i]}")

    choice = input ("\nPlease select resume to update [1-" + str(len(resumes)) + "]: ")

    index = int(choice) - 1
    niche = resumes[index]

    if niche == resumes[-1]:
        #print ("Hitting all here")
        markdown_to_html()
        html_to_pdf()
        archive_resume(f'{archive_dir}/{niche}/{date}')
    else:
        print (f"Hitting {niche} not from all")
        try:
            index = int(choice) - 1
            niche = resumes[index]
            print (f"{niche} has been selected.\n")
            os.system(f'{pandoc} versions/{niche}/resume.{ext[0]} -c resume.css --template styles/resume-one-page.{ext[1]} -o versions/{niche}/resume-{date}.{ext[1]} --metadata title=resume-{date} --data-dir .')
            os.system(f'chromium-browser --headless --print-to-pdf-no-header --enable-logging=stderr --log-level=2 --print-to-pdf=versions/{niche}/resume-{date}.pdf versions/{niche}/resume-{date}.html')
            shutil.copyfile(f'{resume_dir}/{niche}/resume-{date}.pdf', f'{resume_dir}/{niche}/perrone-resume.pdf')
            archive_resume(f'{archive_dir}/{niche}/{date}')
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("\nPlease select a valid option")
            print ("No changes have been made\n")
            sys.exit (1)

if __name__ == "__main__":
    main()
