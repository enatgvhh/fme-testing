# -*- coding: UTF-8 -*-
#testFmeWb.py
from __future__ import absolute_import, division, print_function, unicode_literals
import os
import re
import pathlib
import time
import pandas as pd
from tester import compare
from tester import fmeProcess
from tester import logEvents

def readLogFile(logFile: str, nameWb: str, logFileTime: time.localtime) -> logEvents.LogEvents:
    """Methode readLogFile scannt das uebergebene LogFile und gibt ein Objekt der Klasse LogEvents zurueck.
    
    Args:
            logFile: String with LogFile (Path/Filename.log)
            nameWb: String mit Namen der Workbench.fmw
            logFileTime: Speicherzeitpunkt vom Typ time.localtime
            
    Returns:
            Objekt der Klasse logEvents.LogEvents
    """
    ob = logEvents.LogEvents(nameWb, logFileTime)
    error = 0
    
    with open(logFile, 'r') as reader:
        for line in reader:
            #Total Features Written = substitutional counter
            if re.search(r"Total `@Count' Invocations: (.*)",str(line)):
                match = re.search(r"Total `@Count' Invocations: (.*)",str(line))
                value = int(match.group(1).strip())
                ob.setWriterCount(value)
            #Total Features Read
            elif re.search(r'Total Features Read (.*)',str(line)):
                match = re.search(r'Total Features Read (.*)',str(line))
                value = int(match.group(1).strip())
                ob.setReaderCount(value)
            #Translation was SUCCESSFUL
            elif re.search(r'Translation was SUCCESSFUL (.*)',str(line)):
                ob.setSuccess(True)
                match = re.search(r'Translation was SUCCESSFUL (.*)',str(line))
                strGroup = match.group(1)
                ob.setWarning(strGroup)
            #FME Session Duration
            elif re.search(r'FME Session Duration: (.*). \(',str(line)):
                match = re.search(r'FME Session Duration: (.*). \(',str(line))
                strGroup = match.group(1)
                ob.setDuration(strGroup)
            #Translation FAILED
            elif re.search(r'Translation FAILED (.*)',str(line)):
                ob.setSuccess(False)
                match = re.search(r'Translation FAILED (.*)',str(line))
                strGroup = match.group(1)
                ob.setWarning(strGroup)
            #Error - only first log entry
            elif re.search(r'ERROR (.*)',str(line)) and error == 0:
                ob.setSuccess(False)
                error += 1
                match = re.search(r'ERROR (.*)',str(line))
                strGroup = match.group(1).strip("|")
                ob.setError(strGroup)
                
    reader.close()
    return ob
    
def main():
    fileDir = r'D:\Testing\TestFolder'
    fileExtWb = '*.fmw'
    fmePath = r'C:\Program Files (x86)\FME_Desktop'
    fmeProcLog = r'D:\Testing\app\fme_report.log'
    fmeProc = fmeProcess.FmeProcess(fmePath, fmeProcLog)
    df = pd.DataFrame()
    #filePathCsv = r'D:\Testing\testResult.csv'
    #filePathHtml = r'D:\Testing\testResult.html'
    filePathJson =  r'D:\Testing\app\data\testResult.json'
    
    if os.path.exists(fileDir) == True:
        if os.path.isdir(fileDir) == True:
            objects = list(pathlib.Path(fileDir).glob(fileExtWb))         
            if objects:
                for element in objects:
                    logFile = str(element).replace('.fmw', '.log')
                    
                    logFileTime = time.localtime(os.path.getmtime(logFile))                   
                    logStart = readLogFile(logFile, element.name, logFileTime)                   
                    fmeProc.callFmeProcess(str(element))                   
                    logFileTime = time.localtime(os.path.getmtime(logFile))                      
                    logEnd = readLogFile(logFile, element.name, logFileTime)
                    
                    comp = compare.Compare(logStart, logEnd)
                    df = df.append(comp.compare())
                    
            df = df.reset_index()
            df = df.drop(columns='index')                                                
            #df.to_csv(filePathCsv, sep=';', na_rep='NaN', index=True)
            #df.to_html(filePathHtml, na_rep='NaN', index=True, classes='dfStyle')
            df.to_json(filePathJson, orient="records")
            
if __name__ == '__main__':
    main()