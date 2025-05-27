import sys
import csv
import os
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def question3():
    joined_file_path = os.path.join("data", "joinedData.txt")
    os.makedirs("data", exist_ok=True)
    
    try:
        big_data_fh = open("data/filteredData.txt", "r", encoding="utf-8")
    except IOError as err:
        print(f"Error opening file data/filteredData.txt: {err}")
        sys.exit(1)
        
    try:
        data_fh = open("data/q3Data.csv", "r", encoding="utf-8")
    except IOError as err:
        print(f"Error opening file data/q3Data.csv: {err}")
        sys.exit(1)
        
    dataReader = csv.reader(data_fh)
    
    line_number = 0
    
    if not os.path.exists(joined_file_path):
        with open(joined_file_path, "w", encoding="utf-8") as fwrite:
            for data in dataReader:
                # Skip lines that do not have enough columns
                if len(data) < 13:
                    continue

                # Read header
                if line_number == 0:
                    refDate1 = data[0]
                    geo1 = data[1]
                    classification1 = data[4]
                    vacancyChar1 = data[3]
                    unemployementValue = data[12]
                else:
                    refDate1 = data[0]
                    geo1 = data[1]
                    classification1 = data[4]
                    vacancyChar1 = data[3]
                    unemployementValue = data[12]

                line_number += 1

                # Reset big_data_reader to the beginning
                big_data_fh.seek(0)
                big_data_reader = csv.reader(big_data_fh)
    
                for data2 in big_data_reader:
                    if len(data2) < 6:
                        continue  # Skip lines that do not have enough columns
                    refDate2 = data2[0]
                    geo2 = data2[1]
                    classification2 = data2[2]
                    vacancyChar2 = data2[3]
                    stats2 = data2[4]
                    jobVacancy = data2[5]
                    if classification1.strip().lower() == classification2.strip().lower() and stats2 == "Job vacancies" and geo1 == geo2:
                        fwrite.write(f"{classification1},{geo1},{unemployementValue},{jobVacancy}\n")
    
    try:
        joinedData_fh = open("data/joinedData.txt", "r", encoding="utf-8")
    except IOError as err:
        print(f"Error opening file data/joinedData.txt: {err}")
        sys.exit(1)
    
    joined_data_reader = csv.reader(joinedData_fh)
    data_to_plot = []
    provinces = []
    classifications = []
    for data in joined_data_reader:
        geo = data[1]
        classification = data[0]
        unemployementValue = data[2]
        jobVacancy = data[3]
        if classification not in classifications:
            classifications.append(classification)

        if unemployementValue.strip() == "":
            unemployementValue = "0"
        if jobVacancy.strip() == "":
            jobVacancy = "0"
        jobVacancy = float(jobVacancy)
        unemployementValue = float(unemployementValue)
        if geo not in provinces:
            provinces.append(geo)
        data_to_plot.append((geo, classification, unemployementValue, jobVacancy))

    joinedData_fh.close()
    
    print("\n********************************************** Industry sectors **********************************************")
    for i in range(len(classifications)):
        print(f"{i+1} - {classifications[i]}")
    print("**************************************************************************************************************")
    
    try:
        userInp = int(input("\nWhich industry sector would you like to select?: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)
    selected_sector = classifications[userInp - 1]
    # Calculate the average job vacancies and unemployment rate per province
    province_totals = {}
    province_counts = {}
    #to ensure that each region only has 1 value for job vacancy and unemployment rate
    for geo, classification, unemployementValue, jobVacancy in data_to_plot:
        if geo not in province_totals:
            province_totals[geo] = {"jobVacancy": 0, "unemployementValue": 0}
            province_counts[geo] = 0
        province_totals[geo]["jobVacancy"] += jobVacancy
        province_totals[geo]["unemployementValue"] += unemployementValue
        province_counts[geo] += 1

    province_averages = {
        geo: {
            "jobVacancy": province_totals[geo]["jobVacancy"] / province_counts[geo],
            "unemployementValue": province_totals[geo]["unemployementValue"] / province_counts[geo]
        }
        for geo in province_totals
    }

    # Create a DataFrame for plotting
    df = pd.DataFrame([
        {"Province": geo, "Unemployment Value": averages["unemployementValue"], "Job Vacancy": averages["jobVacancy"]}
        for geo, averages in province_averages.items()
    ])

    # Create a scatter plot using Seaborn
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x="Unemployment Value", y="Job Vacancy", hue="Province", palette="deep", s=100)
    
    # Create a title with the first line and center the rest if it exceeds the space
    title = f"Average Job Vacancies vs Average Unemployment Rate In {selected_sector.title()} Across Regions In Canada In 2022"
    if len(title) > 60:
        title_lines = title.split(' ')
        first_line = ' '.join(title_lines[:10])
        second_line = ' '.join(title_lines[10:])
        plt.title(f"{first_line}\n{second_line}", ha='center')
    else:
        plt.title(title, ha='center')
    
    plt.xlabel("Unemployment Rate")
    plt.ylabel("Job Vacancies")
    plt.legend(title="Province")
    plt.tight_layout()

    # Save the plot to a PDF file
    plt.savefig("plot3.pdf")
    plt.show()