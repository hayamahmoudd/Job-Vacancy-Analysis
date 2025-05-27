#!/usr/bin/env python3

'''
main.py
    Author(s): Haya Mahmoud for menu options 1 and 3 and another student for menu option 2

    Project: Lab Week 13 - Mile Stone 3
    Date of Last Update: March 26, 2025

    Functional Summary
        main.py takes in a CSV (comma separated version) file
            and filters the file by only printing out the 2022 data that is needed for each question.
            i.e. Q1 asks the user for an industry and prints only that industry accross different regions 
                 Q2 asks the user for a region and prints the data for all indrustries in that region
                 Q3 asks the user for an industry but compares the data from two different datasets and prints the unemployement rates for the industry accross all regions

            There are 17 header fields within the file.
            Those included in our final output are:
                    1. REF_DATE (reference date)
                    2. GEO (geographical region)
                    3. National Occupational Classification (one of 692 categories)
                    4. Job vacancy characteristics ("Full-time", "Part-time", "Bachelor's degree", etc.)
                    5. Statistics ("job vacancies", "proportion of job vacancies", etc.)
                    6. VALUE (Value being recorded in fixed decimal notation)


            The given file represents data collected by Statistics Canada on job vacancies in different industries across different regions in Canada.

         Commandline Parameters: 2
                argv[0] = name of this file
'''

import sys
import csv
import os
from question1 import question1
from question2 import question2
from question3 import question3

def main(argv):        
    # if len(argv) != 2:
    #     print("Usage: python script.py <csv_filename>")
    #     sys.exit(1)
    filename = "data/14100328.csv"

    # Ensure the 'data' directory exists
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", "filteredData.txt")
    
    line_number = 0

    # Try opening input CSV file
    try:
        with open(filename, encoding="utf-8-sig") as data_fh:
            fileReader = csv.reader(data_fh)

            # Check if output file exists and is empty
            file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0

            if file_size == 0:
                with open(file_path, "w", encoding="utf-8") as fwrite:
                    for data in fileReader:
                        if len(data) > 12:  # Prevent IndexError
                            refDate = data[0]
                            geo = data[1]
                            classification = data[3]
                            vacancyChar = data[4]
                            stats = data[5]
                            value = data[12]
                            # refDate, geo, classification, vacancyChar, stats, value = (
                            #     data[0], data[1], data[3], data[4], data[5], data[12]
                            # )
                            if (refDate.startswith("2022") and stats.strip() == "Job vacancies" and stats.strip() != "Proportion of job vacancies" and stats.strip() != "Average offered hourly wage"):
                                fwrite.write(f'"{refDate}","{geo}","{classification}","{vacancyChar}","{stats}","{value}"\n')
                        else:
                            continue

    except FileNotFoundError:
        print(f"File '{filename}' not found")
        sys.exit(1)
    except IOError as err:
        print(f"Error opening file '{filename}': {err}")
        sys.exit(1)
        
    data_fh.close()
    usrInp = -1
    if (usrInp == -1):
        print("\nWelcome to Buenos Aires Term Project Program!\n")
        print("******************************************************* Questions to Explore *******************************************************\n")
        print("Question 1: How do job vacancies in certain industries differ across provinces and territories within Canada?\n")
        print("Question 2: Is there a correlation between the minimum level of education and job vacancies within a region across sectors?\n")
        print("Question 3: Is there a correlation between job vacancies and high unemployment rates within an industry across regions?\n")
        print("************************************************************************************************************************************\n")
    while (usrInp != 4):
        try:
            usrInp = int(input("Enter 1 for Q1, 2 for Q2, 3 for Q3, 4 to exit: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, 3 or 4).")
            continue
        if usrInp == 1:
            question1()
        elif usrInp == 2:
            question2()
        elif usrInp == 3:
            question3()
        elif usrInp == 4:
            print("Exiting program.")
            sys.exit(1)

main(sys.argv)