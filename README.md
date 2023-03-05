# hrv_logger
data input from hrv logger app (Altini)

https://www.hrv.tools/hrv-logger-faq.html

## python setup
kernel 3.9.15

## folder structure
    csv_raw --> import folder, folder to copy from
    csv_backup --> backup folder for raw input files
    csv --> workdir

## function declaration
    rename_sub10.py --> fixes issue with missing leading '0' in csv files
    csv_prepare.py --> copy files to workdir, create column measurement, format timestamp
    create_df.py --> create df with all data

## input josef
    3min Messung
    10s Intervall f(Atemzyklusdauer)
    pro Atemzug --> (diff HR max/HR min)Mittelwert

## daily hrv report
    limitations: 2 measurements in select process --> because of rolling median calculation (index via column number from select_measurement dataframe)
    timestamp 1hour false

## workflow
    take measurement with hrv logger app
    export reading in app to folder /downloads/hrv_logger (on smartphone locally)
    foldersync app syncs hrv_logger folder to pcloud (instant sync, one way)
    hrv alias --> starts hrv_morning_check.py
                    quarto --> render daily_hrv.ipynb to html
                    eog --> shows output of cell 8 as png in gnome picture viewer

## quarto - jupyter notebook rendering
    https://quarto.org/docs/tools/jupyter-lab.html

## todo
- [ ] create_df &rarr; column rename function
- [ ] csv_prepare &rarr; implement timezone
- [ ] morgen/abend uebung vertauscht, genau zuordnen
- [ ] compare dehnen/atmen with ortho
- [ ] calculate rmssd with more measurement points