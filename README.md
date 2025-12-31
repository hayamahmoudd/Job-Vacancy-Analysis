# Job Vacancy Analysis Project

A Python based data analysis tool that explores job vacancy trends across Canadian provinces and territories using Statistics Canada data from 2022.

![Demo](demo.gif)

## Overview

This project analyzes job vacancy data to answer three key research questions:
1. **Question 1**: How do job vacancies in certain industries differ across provinces and territories within Canada?
2. **Question 2**: Is there a correlation between the minimum level of education and job vacancies within a region across sectors?
3. **Question 3**: Is there a correlation between job vacancies and high unemployment rates within an industry across regions?

## Features

- Interactive menu driven interface for selecting research questions
- Automated data filtering from large CSV datasets
- Visual analysis using Seaborn and Matplotlib
- Province by province comparison of job vacancies
- Industry sector selection and analysis
- PDF output of generated visualizations

## Requirements

- Python 3.x
- Required libraries:
  - `csv` (built-in)
  - `sys` (built-in)
  - `os` (built-in)
  - `seaborn`
  - `matplotlib`
  - `pandas`

## Installation

1. Clone this repository or download the project files
2. Install required dependencies:
```bash
pip install seaborn matplotlib pandas
```

## Usage

Run the main program:
```bash
python main.py
```

Follow the interactive prompts:
1. Select a question (1, 2, 3, or 4 to exit)
2. Choose an industry sector from the displayed list
3. View the generated analysis and visualization

The program will:
- Automatically filter data from the CSV file on first run
- Cache filtered data for faster subsequent runs
- Generate visualizations saved as PDF files
- Display interactive plots

## Data Source

This project uses data from **Statistics Canada** (Table 14-10-0328-01) on job vacancies across different:
- Geographic regions (provinces and territories)
- Industry sectors (692 National Occupational Classification categories)
- Job characteristics (full-time, part-time, education requirements, etc.)

## Output

- **Question 1**: Generates `plot1.pdf` showing average job vacancies by province for selected industry
- **Question 2**: In development
- **Question 3**: Analyzes correlation between job vacancies and unemployment rates

## Authors

- **Haya Mahmoud** - Question 1 and Question 3 implementation
- Additional contributor - Question 2 implementation

## Project Information

- **Course**: CIS2250
- **Last Updated**: March 16, 2025

## License

This project uses publicly available data from Statistics Canada.