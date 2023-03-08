# <center> Analyse Heartratevariability (HRV) Data  <center>
## Introduction
Static snapshot of the data exploration setup for analysis of heartrate related data. So far the focus is on time-domain values (heartrate (hr) / root mean square of successive differences (rmssd)) because these are the most intuitive values. In this setup no data analysis is implemented, it's sole use is for exploring the input data and generating a simple daily/weekly overview of trends for hr/rmssd values.

## Python setup
Kernel 3.9.15  
Seaborn version 0.12 needed for obsidian plots  
https://seaborn.pydata.org/tutorial/objects_interface  

## Folder structure
    csv_raw --> shared import folder for raw hrv_logger output
    csv_backup --> backup folder for raw input files
    csv --> python working directory

## Function declaration
    csv_prepare.py --> copy files to workdir, create column measurement, format timestamp
    create_df.py --> create main dataframe with all input data 

## Workflow
- Smartphone
    - Use Polar H10 HR-Belt  
    - Take measurement with hrv logger app  
    - Export reading from app to local folder on phone   
- Cloud
    - Foldersync app syncs hrv_logger folder to cloud (autosync, one way)  
    - Input folder for Python is the target folder for Foldersync app (csv_raw)  
- Python
    - Copy csv files to Python workdirectory via script (csv_prepare)  
    - Explore data in Python and generate .png outputfile  
- Obsidian
    - Load Python output via cli tool  
    - View sematic data and hrv logger data in dynamically generated markdown file  

## Hrv_logger app
Documentation for app and sience background information on Hrv data  
https://www.hrv.tools/hrv-logger-faq.html


## Limitations
- 2 measurements in select process --> because of rolling median calculation (index via column number from select_measurement dataframe)
- Seaborn.objects interface uses UTC timestamps
- Last measurement --> evening measurement x-label not correct