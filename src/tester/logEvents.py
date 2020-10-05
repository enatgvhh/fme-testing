# -*- coding: UTF-8 -*-
#logEvents.py
from __future__ import absolute_import, division, print_function, unicode_literals
import time

class LogEvents:
    """"Klasse LogEvent speichert alle relevanten Events aus einem LogFile."""
    
    def __init__(self, nameWb: str, logFileTime: time.localtime):
        """Konstruktor der Klasse LogEvents.
        
        Args:
            nameWb: Name Workbench.fmw
            logFileTime: Speicherzeitpunkt vom Typ time.localtime
        """
        self.__nameWb = nameWb
        self.__logFileTime = logFileTime
        self.__writerCount = 0
        self.__readerCount = 0
        self.__success = None
        self.__warning = None
        self.__duration = None
        self.__error = None
        
    def setWriterCount(self, writerCount: int):
        """Methode setWriterCount
        
        Args:
            writerCount: int mit Anzahl zu schreibender Feature
        """
        self.__writerCount = writerCount
        
    def setReaderCount(self, readerCount: int):
        """Methode setReaderCount
        
        Args:
            readerCount: int mit Anzahl der gelesenen Feature
        """
        self.__readerCount = readerCount
        
    def setSuccess(self, success: bool):
        """Methode setSuccess
        
        Args:
            success: boolean
        """
        self.__success = success
        
    def setWarning(self, warning: str):
        """Methode setWarning
        
        Args:
            warning: String mit warning
        """
        self.__warning = warning
        
    def setDuration(self, duration: str):
        """Methode setDuration
        
        Args:
            duration: String mit Zeitangabe zur Prozessdauer
        """
        self.__duration = duration
        
    def setError(self, error: str):
        """Methode setError
        
        Args:
            error: String mit dem ersten Error Log aus dem LogFile
        """
        self.__error = error
        
    def getWriterCount(self) -> int:
        """Methode getWriterCount
        
        Returns:
            int mit Anzahl zu schreibender Feature
        """
        return self.__writerCount
        
    def getReaderCount(self) -> int:
        """Methode getReaderCount
        
        Returns:
            int mit Anzahl der gelesenen Feature
        """
        return self.__readerCount
        
    def getSuccess(self) -> bool:
        """Methode getSuccess
        
        Returns:
            boolean for success
        """
        return self.__success
        
    def getWarning(self) -> str:
        """Methode getWarning
        
        Returns:
            String mit warning
        """
        return self.__warning
        
    def getDuration(self) -> str:
        """Methode getDuration
        
        Returns:
            String mit Zeitangabe zur Prozessdauer
        """
        return self.__duration
        
    def getError(self) -> str:
        """Methode getError
        
        Returns:
            String mit dem ersten Error Log aus dem LogFile
        """
        return self.__error
    
    def getNameWb(self) -> str:
        """Methode getNameWb
        
        Returns:
            String mit dem Namen der Workbench.fmw
        """
        return self.__nameWb
    
    def getLogFileTime(self) -> time.localtime:
        """Methode getLogFileTime
        
        Returns:
            time.localtime vom Speicherzeitpunkt des LogFiles
        """
        return self.__logFileTime
    