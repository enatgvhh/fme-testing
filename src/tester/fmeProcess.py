# -*- coding: UTF-8 -*-
#fmeProcess.py
from __future__ import absolute_import, division, print_function, unicode_literals
import os
import subprocess
import logging

class FmeProcess:
    """Klasse FmeProcess dient dazu, um eine FME-Workbenche ueber einen Subprocess laufen zu lassen."""
    
    def __init__(self, fmepath: str, logger: logging.Logger):
        """Konstruktor der Klasse FmeProcess.
        
        Args:
            fmepath: String mit Path zur fme.exe
            logger: Objekt logging.Logger
        """
        self.__fmepath = fmepath
        self.__logger = logger
        
    def callFmeProcess(self, wb: str):
        """Methode startet den FME Subprocess.
        
        Args:
            wb: String with FME Workbench Path (Path/Filename.fmw)
        """
        os.chdir(self.__fmepath)
        fmeCommand = self.__fmepath + "\\fme.exe " + wb #without fme args! <+ " " + fmeargs>
        completed = subprocess.run(fmeCommand, stderr=subprocess.PIPE)
        
        if completed.returncode != 0:
            message = '%s %s %s %s %s' % ('fme transformation', wb, 'failed: <', str(completed.stderr), ">")
            self.__logger.error(message)
        else:
            message = '%s %s %s %s %s' % ('fme transformation', wb, 'successfully: <', str(completed.stderr), ">")
            self.__logger.info(message)
            