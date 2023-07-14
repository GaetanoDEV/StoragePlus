@echo off
echo Installazione di Python 3.11.4...
cd etc 
python-3.11.4-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
echo Installazione delle dipendenze...
pip install mysql-connector-python
pip install requests
pip install bs4
pip install screeninfo