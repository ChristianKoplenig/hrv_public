# <center> Analyse Heartratevariability Data  <center>

## hrv_logger
data input from hrv logger app (Altini)

https://www.hrv.tools/hrv-logger-faq.html

## python setup
kernel 3.9.15
seaborn objects plot library

## folder structure
    csv_raw --> import folder, folder to copy from
    csv_backup --> backup folder for raw input files
    csv --> workdir

## function declaration
    csv_prepare.py --> copy files to workdir, create column measurement, format timestamp
    create_df.py --> create df with all data

## daily hrv report
limitations: 2 measurements in select process --> because of rolling median calculation (index via column number from select_measurement dataframe)

## workflow
use Polar H10 HR-Belt
take measurement with hrv logger app
export reading in app to folder /downloads/hrv_logger (on smartphone locally)
foldersync app syncs hrv_logger folder to cloud (manuall sync, one way)
input folder for python is the target folder for foldersync app (csv_raw)
copy csv files to python workdirectory via script (csv_prepare)
analyse data in python and generate .png outputfile
in obsidian load python output via cli tool 
view sematic data and hrv logger data in myHealth.md