import sys
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt


def question2():
    print("Here are the provinces to select from:")
    provinces = [
        "Ontario", "Quebec", "Manitoba", "Saskatchewan", "Nova Scotia",
        "Nunavut", "Northwest Territories", "British Columbia",
        "Newfoundland and Labrador", "New Brunswick",
        "Prince Edward Island", "Yukon", "Alberta"
    ]


    n=1
    for region in provinces:
           print(f"{n} - {region}")
           n+=1
    region = int(input("\nEnter the number for the region you would like to explore exactly as written in the menu: "))
    try:
        filteredData_fh = open("data/filteredData.txt", "r", encoding="utf-8-sig")
    except IOError as err:
            print(f"Error opening file data/filteredData.txt: {err}")
            sys.exit(1)
   
    eduLevel = []
    vacancies = []
   
    filteredDataReader = csv.reader(filteredData_fh)
   
    for data in filteredDataReader:
       refDate = data[0]
       geo = data[1]
       classification = data[2]
       vacancyChar = data[3]
       stats = data[4]
       value = data[5]
     
       if geo.strip().lower() == provinces[region-1].strip().lower() and stats.strip().lower() == "job vacancies":
            if value == "":
               value = "0"
            if vacancyChar not in eduLevel:
                eduLevel.append(vacancyChar)
                vacancies.append(0)
            else:
                index = eduLevel.index(vacancyChar)
                vacancies[index] += int(value)
   
    # Print results
    if eduLevel:
        # Slice the lists to get the relevant data (from index 3 to 12)
        relevant_eduLevel = eduLevel[3:12]
        relevant_vacancies = vacancies[3:12]
       
        plt.figure(figsize=(12, 6))
       
        # Create a scatter plot
        plt.scatter(relevant_eduLevel, relevant_vacancies, s=100)
       
        # Customize plot
        plt.title(f"Minimum Education Level vs Job Vacancies for Occupations within {provinces[region-1]} in 2022")
        plt.xlabel("Minimum Education Level")
        plt.ylabel("Number of Job Vacancies")
        plt.xticks(relevant_eduLevel, rotation=45, ha='right')
       
        # Add value labels
        for i, (char, vac) in enumerate(zip(relevant_eduLevel, relevant_vacancies)):
            plt.annotate(f'{vac}',
                         (char, vac),
                         xytext=(5, 5),
                         textcoords='offset points')
       
        plt.tight_layout()
        plt.savefig("plot2.pdf", bbox_inches='tight')
        plt.show()
    else:
        print("No matching job vacancy data found.")


    filteredData_fh.close()
