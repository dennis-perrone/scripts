#!/usr/bin/python

####################################################################
# Script Name : hamlog.py
# Description : This is intended to be the first draft of a logger
#               for ham radio. It will save the files as a tabbed csv
#               and format in adif. It will also eventually act as a
#               CLI logging program that will ideally log everything
#               in a flat file without needing an extra database.
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

import os
import sys
from datetime import date, datetime, timezone
#from datetime import datetime
from pathlib import Path
import csv
import configparser
#import pandas as pd

home = str(Path.home())
config_dir = f'{home}/.config/hamlog'
config_file = f'{config_dir}/hamlog.ini'
log_dir = f'{home}/hamlog/station_logs'
date = date.today().isoformat()
#data = pd.read_csv(f'{home}/hamlog.csv')

# write config files to .config/hamlog/hamlog.conf
# write log files to /var/log/hamlog.log

#print (home)
#print (config_file)

def main():
    if not os.path.isfile(config_file):
        print ("It looks like this is your first time using this program.")
        program_setup = input ("Initialize setup? [Y/N]: ")
        program_setup = program_setup.lower()
        if program_setup in ('y', 'yes'):
            print ("generating config file")
            config_generation()
        elif program_setup in ('n', 'no'):
            print ("exiting program")
            sys.exit(1)
        else:
            print ("Please select a valid option.")
            sys.exit(1)
    load_config()
    menu()

def config_generation():
    global station_call
    os.makedirs(config_dir)
    station_call = input ("Enter station call sign: ")
    station_call = station_call.upper()
    station_radio = input ("Enter the radio being utilized: ")
    station_qth = input ("Enter the stations QTH: ")
    f = open(config_file,"w+")
    filecontent = [f"# Station configuration information generated "\
            f"on {date}\n\n","[general_settings]\n",\
            f"station_call={station_call}\n", "station_radio="\
            f"{station_radio}\n",f"station_qth={station_qth}\n"]
    f.writelines(filecontent)
    f.close()
    
    #config = configparser.ConfigParser()
    #config.add_section("general_settings")
    #config.set("general_settings","station_call",station_call)
    #cfgfile = open(config_file, 'w')
    #config.write(cfgfile)
    #cfgfile.close()

def load_config():
    global station_call
    global station_qth
    config = configparser.ConfigParser()
    config.read(config_file)
    station_call = config.get("general_settings","station_call")
    station_qth = config.get("general_settings","station_qth")

def menu():
    menu_options = ['Create new log', 'Edit station log(s)', \
            'View station log(s)', 'Delete log(s)', 'Export log(s)', 'Quit program']
    item_count = 0
    opt_count = 1
    print ()
    print (f"{station_call} Station Log")
    print ("-----------------------------")
    print ()
    for i in menu_options:
        print (f'{opt_count}. {(menu_options[item_count])}')
        item_count += 1
        opt_count += 1
    print ()
    #choice = int(input(f"Please select the desired action [1-{str(len(menu_options))}]: "))
    choice = input(f"Please select the desired action [1-{str(len(menu_options))}]: ")
    if choice == "1":
        log_create()
    elif choice == "2":
        log_edit()
    elif choice == "3":
        log_view()
    elif choice == "4":
        print ("You choose four")
    elif choice == "5":
        print ("You choose five")
    elif choice == "6" or choice.lower() == "q":
        print ("Quit")
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("No changes have been made")
        print ()
        menu()
    
def log_create():
    global new_log
    os.system('cls' if os.name == 'nt' else 'clear')
    print ()
    print (f"The default log name is {station_call}_general.")
    print ()
    log_name = input("Enter log name: ") or f'{station_call}_general'
    new_log = f'{log_dir}/{log_name}.csv'

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    if os.path.exists(new_log):
        #append_write = 'a'
        os.system('cls' if os.name == 'nt' else 'clear')
        print (f"A log named {log_name} already exists.")
        print ()
        print ("Please select another name.")
        main()

    logfile = open(new_log, 'w', newline='')
    w = csv.writer(logfile)

#    if os.path.exists(new_log) and append_write == 'w':
    if os.path.exists(new_log):
#        with open(new_log, append_write, newline='') as logfile:
        with open(new_log, 'w', newline='') as logfile:
            headers = ['contact_number', 'call_sign', 'date_iso', 'time_utc',\
                'frequency', 'band', 'mode', 'power', 'rst_sent', 'rst_rcvd',\
                'op_name', 'qth_country', 'qth_state']
            w.writerow(headers)
    print ()
    print (f"A log with the name of {log_name}.csv has been "\
        "created successfully!")
    print ()

def log_edit():
    log_finder()
    if os.path.exists(log_select):
        append_write = 'a'
    elif os.path.exists(log_dir):
        append_write = 'w'
    else:
        os.makedirs(log_dir)
        append_write = 'w'
    
    logfile = open(log_select, append_write, newline='')
    w = csv.writer(logfile)

    while True:
        # Need to figure out how to increment this based on lines in a file.
        #contact_number = int(0)
        print ()
        callsign = input("Enter callsign: ")
        callsign = callsign.upper()
        while True:
            try:
                band = int(input("Enter band (ex. 40): "))
                band = str(band) + str("m")
                break
            except:
                print ("Please enter band numbers only")
        while True:
            try:
                frequency = int(input("Enter frequency (MHz): "))
                # Adjust the zfill number if logging Hz
                frequency = str(frequency).zfill(5)
                break
            except:
                print ("Please enter the frequency numbers only.")
        date = datetime.now().strftime('%Y-%m-%d')
        time_utc = datetime.now(timezone.utc).strftime("%H:%M")
        #mode = input("Enter communication mode: ")
        #power = int(input("Enter power (w): "))
        #rst_sent = int(input("Enter the sending RST: "))
        #rst_rcvd = int(input("Enter the received RST: "))
        #op_name = input("Enter operator's name: ")
        #qth_country = input("Enter operator's country: ")
        #qth_state = input("Enter the operator's state: ")
        print ()
        finish = input("Append information to log? [Y/N/Q]: ")
        if finish.lower() == "y":
            w.writerow([callsign, date, frequency, band, time_utc])
            print ("Log updated")
            more_entries = input("Add another entry [Y/N]: ")
            if not more_entries == "y":
                break
        elif finish.lower() == "n":
            print ("Skipping. Restarting ...")
        elif finish.lower() == 'q':
            print ('Not writing anymore. Stopping!')
            logfile.close()
            exit()
        else:
            print ("Invalid entry. Restarting the program.")
    
#    data = []
#    while True:
#        print ("Log input: ")

#        date_iso = date

def log_finder():
    global log_select
    os.system('cls' if os.name == 'nt' else 'clear')
    print ()
    print ("Available Logs:")
    print ("---------------")
    print ()
    log_list = os.listdir(log_dir)
    #log_dir = f'{home}/projects/scripts/python/csv-generator/station_logs'
    item_count = 0
    opt_count = 1
    for i in log_list:
        print (f'\t{opt_count}. {(log_list[item_count])}')
        item_count += 1
        opt_count += 1
    print ()
    choice = int(input("Select log to view: "))
    log_select = log_list[choice-1]
    os.chdir(log_dir)

def log_view():
    log_finder()
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(log_select) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} was worked {row[1]} on {row[2]} MHz at {row[4]} UTC.')
                line_count += 1
        print(f"Processed {line_count} log entries.")

if __name__ == "__main__":
    main()