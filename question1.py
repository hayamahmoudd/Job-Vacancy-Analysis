import sys
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt

def question1():
    print("********************************************** Industry sectors **********************************************")
    file_path = os.path.join("data", "sector.txt")
    os.makedirs("data", exist_ok=True)
    
    if not os.path.exists(file_path):
        try:
            filteredData_fh = open("data/filteredData.txt", "r", encoding="utf-8")
        except IOError as err:
            print(f"Error opening file data/filteredData.txt: {err}")
            sys.exit(1)
        
        filteredDataReader = csv.reader(filteredData_fh)
        sectors = []
        
        for data in filteredDataReader:
            classification = data[2]
            if classification not in sectors:
                sectors.append(classification) 
        
        with open(file_path, "w", encoding="utf-8") as fwrite:
            for sector in sectors:
                fwrite.write(f'{sector}\n')
        
        filteredData_fh.close()
    else:
        sectors = []
        with open(file_path, "r", encoding="utf-8") as fread:
            for line in fread:
                sectors.append(line.strip())
    
    for i in range(len(sectors)):
        print(f"{i+1} - {sectors[i]}")
    print("***************************************************************************************************************\n")
    
    try:
        userInp = int(input("\nWhich industry sector would you like to select?: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)
    
    selected_sector = sectors[userInp - 1]
    
    try:
        filteredData_fh = open("data/filteredData.txt", "r", encoding="utf-8")
    except IOError as err:
        print(f"Error opening file data/filteredData.txt: {err}")
        sys.exit(1)
    
    filteredDataReader = csv.reader(filteredData_fh)
    data_to_plot = []
    for data in filteredDataReader:
        refDate = data[0]
        geo = data[1]
        classification = data[2]
        vacancyChar = data[3]
        stats = data[4]
        value = data[5]
        
        if classification.strip().lower() == selected_sector.strip().lower() and stats.strip().lower() == "job vacancies" and geo != "Canada":
            if value == "":
                value = "0"
            value = int(value)
            data_to_plot.append((refDate, geo, value))
    
    filteredData_fh.close()
    
    # Calculate the average job vacancies per province
    province_totals = {}
    province_counts = {}
    
    for refDate, geo, value in data_to_plot:
        if geo not in province_totals:
            province_totals[geo] = 0
            province_counts[geo] = 0
        province_totals[geo] += value
        province_counts[geo] += 1
    
    province_averages = {geo: province_totals[geo] / province_counts[geo] for geo in province_totals}
    
    # Convert data to a DataFrame for plotting
    import pandas as pd
    df = pd.DataFrame(list(province_averages.items()), columns=["Province", "Average Job Vacancies"])
    
    # Create a bar plot using Seaborn
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="Province", y="Average Job Vacancies")
    
    # Set the title and handle long titles
    title = f"Average Job Vacancies In {selected_sector.title()} Across Regions In Canada In 2022"
    if len(title) > 60:
        words = title.split()
        first_line = ""
        second_line = ""
        for word in words:
            if len(first_line) + len(word) + 1 <= 60:
                first_line += word + " "
            else:
                second_line += word + " "
        title = first_line.strip() + '\n' + second_line.strip()
    plt.title(title, ha='center')
    
    plt.xlabel("Province")
    plt.ylabel("Job Vacancies")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot to a PDF file
    plt.savefig("plot1.pdf")
    plt.show()
