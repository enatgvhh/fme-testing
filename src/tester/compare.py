# -*- coding: UTF-8 -*-
#compare.py
from __future__ import absolute_import, division, print_function, unicode_literals
import time
import pandas as pd
import numpy as np
from tester import logEvents

class Compare:
    """Klasse Compare fuehrt einen Vergleich zwischen 2 Objekten der Klasse LogEvents aus
    und gibt eien pandas DataFrame mit den Informationen zurueck.
    """

    def __init__(self, logStart: logEvents.LogEvents, logEnd: logEvents.LogEvents):
        """Konstruktor der Klasse Compare.
        
        Args:
            logStart: Objekt der Klasse logEvents.LogEvents
            logEnd: Objekt der Klasse logEvents.LogEvents
        """
        self.logStart = logStart
        self.logEnd = logEnd
        self.__events = []
        
    def compare(self):
        """Methode compare fuehrt einen Vergleich zwischen 2 Objekten der Klasse LogEvents aus
        und gibt eien pandas DataFrame mit den Informationen zurueck.
        
        Returns:
            Objekt der Klasse pandas.DataFrame
        """
        #name wb
        self.__events.append(self.logStart.getNameWb())
        #logFile start
        self.__events.append(time.strftime("%d.%m.%Y %H:%M:%S", self.logStart.getLogFileTime()))
        self.__events.append(self.logStart.getReaderCount())
        self.__events.append(self.logStart.getWriterCount())
        self.__events.append(self.logStart.getSuccess())
        self.__events.append(self.logStart.getWarning())
        self.__events.append(self.logStart.getDuration())
        self.__events.append(self.logStart.getError())
        #logFile end
        self.__events.append(time.strftime("%d.%m.%Y %H:%M:%S", self.logEnd.getLogFileTime()))
        self.__events.append(self.logEnd.getReaderCount())
        self.__events.append(self.logEnd.getWriterCount())
        self.__events.append(self.logEnd.getSuccess())
        self.__events.append(self.logEnd.getWarning())
        self.__events.append(self.logEnd.getDuration())
        self.__events.append(self.logEnd.getError())
        #count prozent
        countReader1 = self.logStart.getReaderCount()
        countWriter1 = self.logStart.getWriterCount()
        countReader2 = self.logEnd.getReaderCount()
        countWriter2 = self.logEnd.getWriterCount()
        
        if countReader1 > 0:
            prozentReader = countReader2 * 100 / countReader1
        else:
            prozentReader = 0
            
        if countWriter1 > 0:
            prozentWriter = countWriter2 * 100 / countWriter1
        else:
            prozentWriter = 0
            
        self.__events.append(prozentReader)        
        self.__events.append(prozentWriter)
        
        #status
        if self.logEnd.getSuccess() == False or self.logEnd.getError() != None:
            self.__events.append('failed')
        elif prozentReader < 70 or prozentWriter < 70 or self.logStart.getLogFileTime() == self.logEnd.getLogFileTime():
            self.__events.append('manual')
        else:
            self.__events.append('passed')
            
        df = pd.DataFrame(np.array([self.__events]),columns=['Workbench',
                                                             'Start-Zeit', 'Start-Reader-Count', 'Start-Writer-Count', 'Start-Success', 'Start-Warning', 'Start-Duration', 'Start-Error',
                                                             'End-Zeit', 'End-Reader-Count', 'End-Writer-Count', 'End-Success', 'End-Warning', 'End-Duration', 'End-Error',
                                                             'Prozent-Reader', 'Prozent-Writer', 'Status'])           
        return df
    