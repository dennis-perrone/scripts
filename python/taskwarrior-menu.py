#!/usr/bin/python3

import os
from pathlib import Path

############################################################
# TODO
# Create submenus for options with final option being to enter manually
# Create way to reiterate over "x" number for school_project for number of discussion posts per week
# Have tech projects create a working directory (possible git backups to github)
# Complete the actual processes required for travel (passport, iteniary, research flight prices or tolls, packing list, etc.)
# Add color to some options (like notes, etc.)
############################################################

os.system('clear')

def main():

    choice = '0'

    print ()
    print ("###################################################")
    print ("#####      TaskWarrior Project Generator      #####")
    print ("###################################################")
    print ()
    print ("   1.) Create a home project")
    print ("   2.) Create a school project")
    print ("   3.) Create a technology project")
    print ("   4.) Create a research project")
    print ("   5.) Create a travel project")
    print ("   6.) Create a blog project")
    print ()
    print ("   q.) Exit script")
    print ()

    choice = input ("Please select a choice: ")
    print()

    if choice == "1":
        home_project()
    elif choice == "2":
        school_project()
    elif choice == "3":
        tech_project()
    elif choice == "4":
        research_project()
    elif choice == "5":
        travel_project()
    elif choice == "6":
        blog_project()
    elif choice == "q":
        exit()
    else:
        print ("Please select a valid choice")
        os.system('clear')
        main()

def home_project():
    os.system ('clear')
    # add option for recuring tasks (mowing, filters, etc or one off things). This should be a simple if question
    proj_main = "home"
    print ()
    print ("NOTE: If project topic has multiple words, use \"_\" instead of \"-\" to separate words")
    print ()
    print (f'Select {proj_main} project category')
    print ()
    print ("   1.) Garage")
    print ("   2.) Lawncare")
    print ("   3.) Home repair")
    print ("   4.) Home maintenance")
    print ("   5.) Project category not listed")
    print ()
    print ("   e.) Exit to main menu")
    print ("   q.) Quit script")
    print ()
    proj_category = input (f'Please enter the {proj_main} project category: ')
    if proj_category == "1":
        proj_category = "garage"
    elif proj_category == "2":
        proj_category = "lawncare"
    elif proj_category == "3":
        proj_category = "home_repair"
    elif proj_category == "4":
        proj_category = "home_maintenance"
    elif proj_category == "5":
        proj_category = input (f'Please enter project category: ')
    elif proj_category == "e":
        os.system('clear')
        main()
    elif proj_category == "q":
        os.system('clear')
        exit()
    else:
        home_project()
    os.system('clear')
    print ()
    print (f'Select {proj_category} project details: ')
    print ()
    print ("   1.) Initial research for project")
    print (f"   2.) This {proj_category} project is recurring")
    print (f"   3.) This {proj_category} project is a one-time project")
    print ()
    print ("   e.) Exit to main menu")
    print ("   q.) Quit script")
    print ()
    proj_recur = input ("Please select project recurrence: ")
    print ()
    if proj_recur == "1":
        proj_topic = input (f'Please enter a name for the {proj_category} project (ex. storage, mowing, etc.): ')
        create_dir = input (f"Create working directory for {proj_topic} research [Y/N]: ")
        if create_dir == "y":
            # Below is the code that creates a directorys from the loop
            home = str(Path.home())
            working_dir = f"{home}/documents/house/projects/{proj_category}/{proj_topic}"
            Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
            subfolders = ['01-archive', '02-misc', '03-quotes']
            subfiles = ['outline.md', 'bill-of-materials.md']
            for subfolder in subfolders:
                os.makedirs(os.path.join(f'{working_dir}', subfolder))
            for subfile in subfiles:
                os.mknod(os.path.join(f'{working_dir}', subfile))
            print ()
            print ("Directories created successfully")
            print ()
        elif create_dir == "n":
            print ()
            print ("Not creating working directories, just tasks")
            print ()
        else:
            print ("Please select a valid option")
            home_project()
        os.system(f'task add conduct research for {proj_topic} +{proj_category} +research pro:{proj_main}.{proj_category}.{proj_topic}')
    elif proj_recur == "2":
        proj_topic = input (f'Please enter a name for the {proj_category} project (ex. storage, mowing, etc.): ')
        proj_periodicity = input (f'How often does {proj_category} occur (ex. daily, weekly, etc.): ')
        proj_day = input (f'What day will {proj_topic} be completed: ')
        proj_due = input (f'When does this project begin: ')
        proj_end = input (f'When does {proj_category} end (ex. add actual date or month): ')
        create_dir = input (f"Create working directory for {proj_topic} research [Y/N]: ")
        if create_dir == "y":
            # Below is the code that creates a directorys from the loop
            home = str(Path.home())
            working_dir = f"{home}/documents/house/projects/{proj_category}/{proj_topic}"
            Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
            subfolders = ['01-archive', '02-misc', '03-quotes']
            subfiles = ['outline.md', 'bill-of-materials.md']
            for subfolder in subfolders:
                os.makedirs(os.path.join(f'{working_dir}', subfolder))
            for subfile in subfiles:
                os.mknod(os.path.join(f'{working_dir}', subfile))
            print ()
            print ("Directories created successfully")
            print ()
        elif create_dir == "n":
            print ()
            print ("Not creating working directories, just tasks")
            print ()
        else:
            print ("Please select a valid option")
            home_project()
        os.system(f'task add conduct research for {proj_topic} +{proj_category} +research pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add create parts list and get costs to complete {proj_topic} project  +{proj_category} +materials pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add complete {proj_topic} project +{proj_category} proj:{proj_main}.{proj_category}.{proj_topic} recur:{proj_periodicity} due:{proj_due} until:{proj_end}')
    elif proj_recur == "3":
        proj_topic = input (f'Please enter a name for the {proj_category} project (ex. storage, mowing, etc.): ')
        due_date = input (f'Does this {proj_category} have a due date [Y/N]: ')
        create_dir = input (f"Create working directory for {proj_topic} research [Y/N]: ")
        if create_dir == "y":
            # Below is the code that creates a directorys from the loop
            home = str(Path.home())
            working_dir = f"{home}/documents/house/projects/{proj_category}/{proj_topic}"
            Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
            subfolders = ['01-archive', '02-misc', '03-quotes']
            subfiles = ['outline.md', 'bill-of-materials.md']
            for subfolder in subfolders:
                os.makedirs(os.path.join(f'{working_dir}', subfolder))
            for subfile in subfiles:
                os.mknod(os.path.join(f'{working_dir}', subfile))
            print ()
            print ("Directories created successfully")
            print ()
        elif create_dir == "n":
            print ()
            print ("Not creating working directories, just tasks")
            print ()
        else:
            print ("Please select a valid option")
            home_project()
        os.system(f'task add conduct research for {proj_topic} +{proj_category} +research pro:{proj_main}.{proj_category}.{proj_topic}')
        if due_date == "y":
            proj_due = input (f'When is this project due (ex. day of week (monday, sunday) or date (YYYY-MM-DD): ')
            os.system(f'task add conduct research for {proj_topic} +{proj_category} +research pro:{proj_main}.{proj_category}.{proj_topic}')
            os.system(f'task add create parts list and get costs to complete {proj_topic} project  +{proj_category} +materials pro:{proj_main}.{proj_category}.{proj_topic}')
            os.system(f'task add complete {proj_topic} project +{proj_category} proj:{proj_main}.{proj_category}.{proj_topic} due:{proj_due}')
        elif due_date == "n":
            os.system(f'task add conduct research for {proj_topic} +{proj_category} +research pro:{proj_main}.{proj_category}.{proj_topic}')
            os.system(f'task add create parts list and get costs to complete {proj_topic} project  +{proj_category} +materials pro:{proj_main}.{proj_category}.{proj_topic}')
            os.system(f'task add complete {proj_topic} project +{proj_category} proj:{proj_main}.{proj_category}.{proj_topic}')
        else:
            print ("Please select a valid option")
            home_project()
    elif proj_recur == "e":
        os.system('clear')
        main()
    elif proj_recur == "q":
        os.system('clear')
        exit()
    else:
        print("Please select a valid option.")
        os.system('clear')
        home_project()

def school_project():
    os.system ('clear')
    proj_main = "school"
    print ()
    print ("NOTE: If project topic has multiple words, use \"_\" instead of \"-\" to separate words")
    print ()
    print (f'Select a {proj_main} project category')
    print ()
    print ("   1.) Class")
    print ("   2.) Administrative")
    print ("   3.) Other")
    print ()
    print ("   e.) Exit to main menu")
    print ("   q.) Quit script")
    print ()
    proj_category = input (f'Please enter the {proj_main} category: ')
    print ()
    if proj_category == "1":
        proj_category = "class"
        proj_topic = input (f'Please enter the {proj_category} name: ')
        date_start = input ("Enter the class start date (YYYY-MM-DD): ")
        date_end = input ("Enter the class finish date (YYYY-MM-DD): ")
        class_session = input (f'What is the {proj_category} semester and session (ex. f2020, s2021, etc.): ')
        init_discussion = input ("Enter day initial discussion post is due (ex. monday, tuesday, etc.): ")
        if init_discussion == 'monday':
            init_discussion = "0d"
        elif init_discussion == 'tuesday':
            init_discussion = "1d"
        elif init_discussion == 'wednesday':
            init_discussion = "2d"
        elif init_discussion == 'thursday':
            init_discussion = "3d"
        elif init_discussion == 'friday':
            init_discussion = "4d"
        elif init_discussion == 'saturday':
            init_discussion = "5d"
        elif init_discussion == 'sunday':
            init_discussion = "6d"
        else:
            print ("Please select a valid option")
        resp_discussion = input ("Enter day response response post is due (ex. monday, tuesday, etc.): ")
        if resp_discussion == 'monday':
            resp_discussion = "0d"
        elif resp_discussion == 'tuesday':
            resp_discussion = "1d"
        elif resp_discussion == 'wednesday':
            resp_discussion = "2d"
        elif resp_discussion == 'thursday':
            resp_discussion = "3d"
        elif resp_discussion == 'friday':
            resp_discussion = "4d"
        elif resp_discussion == 'saturday':
            resp_discussion = "5d"
        elif resp_discussion == 'sunday':
            resp_discussion = "6d"
        else:
            print ("Please select a valid option")
            school_project()
        class_dir = input (f'Create a working directory for {proj_topic} [Y/N]: ')
        if class_dir == "y":
            home = str(Path.home())
            working_dir = f"{home}/documents/{proj_main}/classes/{class_session}-{proj_topic}"
            Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
            subfolders = ['01-syllabus', '03-notes', '04-resources', '05-assignments', '06-quizes']
            weekly_dir = ['02-discussions']
            weekly_sub = ['week-01', 'week-02', 'week-03', 'week-04', 'week-05', 'week-06', 'week-07', 'week-08']
            discussions = ['post-01-initial.docx', 'post-02-initial.docx', 'post-01-response.docx', 'post-02-response.docx']
            subfiles = ['outline.md']
            for subfolder in subfolders:
                os.makedirs(os.path.join(f'{working_dir}', subfolder))
                for subfile in subfiles:
                    os.mknod(os.path.join(f'{working_dir}', subfolder, subfile))
            for w in weekly_dir:
                os.makedirs(os.path.join(f'{working_dir}', w))
                for x in weekly_sub:
                    os.makedirs(os.path.join(f'{working_dir}', w, x))
                    for y in discussions:
                        os.mknod(os.path.join(f'{working_dir}', w, x, y))
        elif class_dir == "n":
            print ()
            print ("Okay, just making tasks")
            print ()
        else:
            print ("Please select a valid option")
            school_project()
        #init_discussion_number = input ("Enter number of initial discussion posts that are required for this class: ")
        #resp_discussion_number = input ("Enter number of response disuession posts that are required for this class: ")
        os.system(f'task add print syllabus for {proj_topic} +{proj_topic} +syllabus pro:{proj_main}.{proj_category}.{proj_topic}')
        # add for loop to repeat number provided in init and resp discussion number
        os.system(f'task add weekly initial discussion post due +{proj_topic} +discussion pro:{proj_main}.{proj_category}.{proj_topic} recur:weekly due:{date_start}+{init_discussion} scheduled:{date_start} wait:{date_start} until:{date_end}')
        os.system(f'task add weekly response discussion post due +{proj_topic} +discussion pro:{proj_main}.{proj_category}.{proj_topic} recur:weekly due:{date_start}+{resp_discussion} scheduled:{date_start} wait:{date_start} until:{date_end}')
    elif proj_category == "2":
        proj_category = "admin"
        print (f'{proj_category} was selected')
    elif proj_category == "3":
        print ()
        print ("No templates for this option. Please create tasks manually.")
        print ()
    elif proj_category == "e":
        os.system('clear')
        main()
    elif proj_category == "q":
        os.system('clear')
        exit()
    else:
        print (f'No template created for {proj_category}. Please create tasks manually.')

def tech_project():
    os.system ('clear')
    proj_main = "tech"
    print ()
    print ("NOTE: If project topic has multiple words, use \"_\" instead of \"-\" to separate words")
    print ()
    print (f'Select {proj_main} project category')
    print ()
    print ("   1.) Home Lab")
    print ("   2.) Home Automation")
    print ("   3.) Amateur Radio")
    print ("   4.) Technology Research")
    print ("   5.) Certifications")
    print ("   6.) Other")
    print ()
    print ("   e.) Exit to main menu")
    print ("   q.) Quit script")
    print ()
    proj_category = input (f'Please enter the {proj_main} project category: ')
    if proj_category == "1":
        proj_category = "lab"
        proj_topic = input (f'Please enter the {proj_category} project name: ')
        os.system(f'task add conduct initial research for {proj_topic} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add determine requirements for {proj_topic} {proj_category} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add determine desired outcome for {proj_topic} {proj_category} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
    elif proj_category == "2":
        proj_category = "home_automation"
        proj_topic = input (f'Please enter the {proj_category} project name: ')
        os.system(f'task add conduct initial research for {proj_topic} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add determine requirements for {proj_topic} {proj_category} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add determine desired outcome for {proj_topic} {proj_category} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
    elif proj_category == "3":
        proj_category = "ham_radio"
        print (proj_category)
    elif proj_category == "4":
        proj_category = "research"
        proj_topic = input (f'Please enter {proj_main} topic to research: ')
        create_dir = input (f'Create directoriy for {proj_topic} research [Y/N]: ')
        if create_dir == "y":
            home = str(Path.home())
            working_dir = f"{home}/documents/{proj_main}/{proj_category}/{proj_topic}"
            Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
            subfolders = ['sources', 'draft-documents', 'misc']
            subfiles = ['outline.md']
            for subfolder in subfolders:
                os.makedirs(os.path.join(f'{working_dir}', subfolder))
                for subfile in subfiles:
                    os.mknod(os.path.join(f'{working_dir}', subfolder, subfile))
        ##
        ## Add task add commands to add tasks once directories have been created
        ##
        print (proj_category)
    elif proj_category == "5":
        proj_category = "certification"
        print (proj_category)
    elif proj_category == "6":
        proj_category = input ("Please enter a project topic name: ")
        print (f'There is no template for {proj_category}')
        print ()
    elif proj_category == "e":
        os.system('clear')
        main()
    elif proj_category == "q":
        os.system('clear')
        exit()
    else:
        print ("Please select a valid option")
        home_menu = input ("Go back to main menu? [Y/N]: ")
        if home_menu == "y":
            os.system('clear')
            main()
        elif home_menu == "n":
            os.system('clear')
            exit()
        else:
            print ("Please select a valid option.")
            os.system('clear')
            tech_project()

def research_project():
    proj_main = "research"
    os.system ('clear')
    print ()
    print ("NOTE: If project topic has multiple words, use \"_\" instead of \"-\" to separate words")
    print ()
    print (f'{proj_main} project options')
    print ()
    print (f'   1.) Create {proj_main} project with just tasks.')
    print (f'   2.) Create {proj_main} project with tasks and working directory')
    print ()
    print ("   e.) Exit to main menu")
    print ("   q.) Quit script")
    print ()
    proj_category = input (f'Please select {proj_main} category: ')
    print ()
    if proj_category == "1":
        proj_category = input (f'Please enter the {proj_main} category: ')
        proj_topic = input (f'Please enter the {proj_category} topic: ')
        os.system(f'task add gather initial {proj_topic} research resources +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add determine desired outcome of {proj_topic} research +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add validate resources on {proj_topic} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
    elif proj_category == "2":
        proj_category = input (f'Please enter the {proj_main} category: ')
        proj_topic = input (f'Please enter the {proj_category} topic: ')
        os.system(f'task add gather initial {proj_topic} research resources +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add determine desired outcome of {proj_topic} research +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add validate resources on {proj_topic} +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        os.system(f'task add ensure {proj_topic} project has working directory created +{proj_category} +{proj_topic} pro:{proj_main}.{proj_category}.{proj_topic}')
        # Below is the code that creates a directorys from the loop
        create_dir = input (f'Create directoriy for {proj_topic} research [Y/N]: ')
        home = str(Path.home())
        working_dir = f"{home}/documents/{proj_main}/{proj_category}-{proj_topic}"
        Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
        subfolders = ['sources', 'draft-documents', 'misc']
        subfiles = ['outline.md']
        for subfolder in subfolders:
            os.makedirs(os.path.join(f'{working_dir}', subfolder))
            for subfile in subfiles:
                os.mknod(os.path.join(f'{working_dir}', subfolder, subfile))
    elif proj_category == "e":
        os.system ('clear')
        main()
    elif proj_category == "q":
        os.system('clear')
        exit()
    else:
        os.system ('clear')
        print ("Please select a valid option")
        research_project()

def travel_project():
    proj_main = "travel"
    os.system ('clear')
    print ()
    print ("NOTE: If project topic has multiple words, use \"_\" instead of \"-\" to separate words")
    print ()
    print (f'Select {proj_main} area')
    print ()
    print ("   1.) CONUS")
    print ("   2.) OCONUS")
    print ()
    print ("   e.) Exit to main menu")
    print ("   q.) Quit script")
    print ()
    travel_area = input (f'Please enter the {proj_main} project category: ')
    print ()

    if travel_area == "1":
        travel_area = "conus"
        travel_state = input ("What is the destination state or us territory: ")
        travel_city = input ("What is the destination city (if multiple, enter \"multiple\"): ")
        travel_flying = input ("Does trip require flying [Y/N]: ")
        travel_driving = input ("Does trip require driving [Y/N]: ")
        create_dir = input (f'Create directoriy for {travel_area} {proj_main} [Y/N]: ')
        if create_dir == "y":
            home = str(Path.home())
            working_dir = f"{home}/documents/{proj_main}/trip-planning/{travel_area}/{travel_state}-{travel_city}"
            Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
            subfolders = ['01-archive']
            subfiles = ['outline.md', 'flying-info.md', 'driving-info.md', 'attractions.md', 'accomadations.md', 'checklist.md']
            for subfolder in subfolders:
                os.makedirs(os.path.join(f'{working_dir}', subfolder))
            for subfile in subfiles:
                os.mknod(os.path.join(f'{working_dir}', subfile))
        print ()
        print ("Directories created successfully")
        print ()
        if travel_flying == "y" and travel_driving == "y":
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
            os.system(f'task add research flying to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
            os.system(f'task add research driving to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
        elif travel_flying == "y" and travel_driving == "n":
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
            os.system(f'task add research flying to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
        elif travel_flying == "n" and travel_driving == "y":
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
            os.system(f'task add research driving to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
        elif travel_flying == "n" and travel_driving == "n":
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_state}.{travel_city}')
    if travel_area == "2":
        travel_area = "oconus"
        travel_country = input ("What is the destination country or non-us territory: ")
        travel_city = input ("What is the destination city (if multiple, enter \"multiple\"): ")
        travel_flying = input ("Does trip require flying [Y/N]: ")
        travel_driving = input ("Does trip require driving [Y/N]: ")
        if travel_flying == "y" and travel_driving == "y":
            os.system(f'task add ensure passport is present and valid +{proj_main} +passport pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
            os.system(f'task add research flying to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
            os.system(f'task add research driving to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
        elif travel_flying == "y" and travel_driving == "n":
            os.system(f'task add ensure passport is present and valid +{proj_main} +passport pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
            os.system(f'task add research flying to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
        elif travel_flying == "n" and travel_driving == "y":
            os.system(f'task add ensure passport is present and valid +{proj_main} +passport pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
            os.system(f'task add research driving to {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
        elif travel_flying == "n" and travel_driving == "n":
            os.system(f'task add research activities in {travel_city} +{proj_main} +research pro:{proj_main}_{travel_area}.{travel_country}.{travel_city}')
    elif travel_area == "e":
        os.system('clear')
        main()
    elif travel_area == "q":
        os.system('clear')
        exit()
    else:
        os.system('clear')
        travel_project()

def blog_project():
    proj_main = "blog"
    os.system ('clear')
    print ()
    print (f'Select a {proj_main} category')
    print ()
    print (f'   1.) Cyber Security')
    print (f'   2.) DevOps/DevSecOps')
    print (f'   3.) Automation')
    print (f'   4.) Project Management')
    print (f'   5.) System Engineering')
    print ()
    print (f'   e.) Exit to main menu')
    print (f'   q.) Quit script')
    print ()
    proj_category = input (f'What is the {proj_main} category: ')
    print ()
    if proj_category == "1":
        proj_category = "cyber_security"
        print ()
        proj_topic = input (f'What is the {proj_category} topic: ')
        print ()
    elif proj_category == "2":
        proj_category = "devops"
        print ()
        proj_topic = input (f'What is the {proj_category} topic: ')
        print ()
    elif proj_category == "3":
        proj_category = "automation"
        print ()
        proj_topic = input (f'What is the {proj_category} topic: ')
        print ()
    elif proj_category == "4":
        proj_category = "project_management"
        print ()
        proj_topic = input (f'What is the {proj_category} topic: ')
        print ()
    elif proj_category == "5":
        proj_category = "syseng"
        print ()
        proj_topic = input (f'What is the {proj_category} topic: ')
        print ()
    elif proj_category == "e":
        os.system('clear')
        main()
    elif proj_category == "q":
        os.system('clear')
        exit()
    else:
        print ("Please select a valid option.")
        blog_project()

    create_dir = input (f'Create working directory for {proj_category} [Y/N]: ')
    if create_dir == "y":
        home = str(Path.home())
        working_dir = f"{home}/documents/{proj_main}/{proj_category}/0XX-{proj_topic}"
        Path(f"{working_dir}").mkdir(parents=True, exist_ok=True)
        subfolders = ['03-screenshots', '02-misc', '01-archive']
        subfiles = ['outline.md', 'first-draft.md', 'final-draft.md', 'final-post-checklist.md']
        for subfolder in subfolders:
            os.makedirs(os.path.join(f'{working_dir}', subfolder))
        for subfile in subfiles:
            os.mknod(os.path.join(f'{working_dir}', subfile))
    elif create_dir == "n":
        print ()
        print ("Not creating directories, just tasks.")
        print ()
    else:
        print ("Please select a valid option")
        blog_topic()
    print ()
    print ("Creating directories")
    print ()
    os.system(f'task add conduct research for {proj_topic} post +{proj_main} +research +{blog_id} pro:{proj_main}_{blog_id}.{proj_category}.{proj_category}')
    os.system(f'task add create outline for {proj_topic} post +{proj_main} +outline +{blog_id} pro:{proj_main}_{blog_id}.{proj_category}.{proj_category}')
    os.system(f'task add create working directory for {proj_topic} post +{proj_main} +{blog_id} +organization pro:{proj_main}_{blog_id}.{proj_category}.{proj_category}')
    os.system(f'task add write first draft of {proj_topic} post +{proj_main} +{blog_id} +draft pro:{proj_main}_{blog_id}.{proj_category}.{proj_category}')
    os.system(f'task add write final draft of {proj_topic} post +{proj_main} +{blog_id} +draft pro:{proj_main}_{blog_id}.{proj_category}.{proj_category}')
    os.system(f'task add take screenshots for {proj_topic} post +{proj_main} +{blog_id} +screenshots pro:{proj_main}_{blog_id}.{proj_category}.{proj_category}')
    os.system(f'task add upload final {proj_topic} post +{proj_main} +{blog_id} +post pro:{proj_main}_{blog_id}.{proj_category}.{proj_category}')

main()
