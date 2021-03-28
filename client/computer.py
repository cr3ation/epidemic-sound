#!/usr/bin/python

import datetime
import json
import os
from pathlib import Path
import plistlib
import subprocess
import sys


def WriteToLog(logMessage):
    print(logMessage)


class ComputerNotBoundError(Exception):
    pass


class Computer:
    '''
    Creates an object class which returns computer information
    '''

    def __init__(self, allUsers=False):
        try:
            self.computerNames = self.__GetLocalComputerNames()
            self.fileVault = self.__GetFileVault()
            self.firewall = self.__GetFirewall()
            self.operatingSystem = self.__GetOperatingSystem()
            self.users = self.__GetLocalUsers(allUsers)
            self.serialNumber = self.__GetSerialNumber()
            # ------ DON'T LIKE THIS -----------
            self.googleChrome = self.__GetApplication(title="GoogleChrome")
            self.microsoftOffice = self.__GetApplication(
                title="MicrosoftOutlook")

        except:
            raise

    def __GetApplication(self, title=""):
        try:
            fileName = ""
            attributes = []

            if not title:
                return None
            elif title == "GoogleChrome":
                home = str(Path.home())
                fileName = "{0}/Library/Preferences/com.google.Chrome.plist".format(
                    home)
                attributes.append("HomepageLocation")
                attributes.append("ShowHomeButton")
            elif title == "MicrosoftOutlook":
                # See posibile settings https://docs.microsoft.com/en-us/deployoffice/mac/deploy-preferences-for-office-for-mac
                home = str(Path.home())
                fileName = "{0}/Library/Preferences/com.microsoft.Outlook.plist".format(
                    home)
                attributes.append("DefaultEmailAddressOrDomain")
                attributes.append("DisableSkypeMeeting")
            else:
                return None

            # Return none if plist dosn't exist
            if not os.path.isfile(fileName):
                return None

            application = {}

            for attribute in attributes:
                with open(fileName, 'rb') as fp:
                    plist = plistlib.load(fp)
                application.update({attribute: plist[attribute]})
            return application
        except:
            WriteToLog('[application]: unable to get info for %s' % title)
            raise

    def __GetLocalComputerNames(self):
        computerNames = {'ComputerName': None,
                         'LocalHostName': None, 'HostName': None}
        for nameType in computerNames:
            try:
                computerNames[nameType] = subprocess.check_output(
                    ['scutil', '--get', nameType],
                    stderr=subprocess.STDOUT).decode().strip('\n')
            except:
                computerNames[nameType] = None
        return computerNames

    def __GetLocalUsers(self, allUsers):
        try:
            users = []

            output = subprocess.check_output(
                ['dscacheutil', '-q', 'user'],
                stderr=subprocess.STDOUT).decode().strip('\n')
            output = output.split('\n\n')

            for item in output:
                user = {
                    "name": item.split('\n')[0].split(': ')[1],
                    "id": int(item.split('\n')[2].split(': ')[1]),
                }
                if allUsers or user["id"] > 500:
                    users.append(user)
            return users
        except:
            WriteToLog(
                '[users]: error retrieving serial number with system_profiler')
            raise

    def __GetFileVault(self):
        try:
            output = subprocess.check_output(
                ['fdesetup', 'status']).decode().strip('\n')
            return "Enabled" if "On" in output else "Disabled"
        except:
            WriteToLog(
                '[encryption]: error retrieving FileVault status')

    def __GetFirewall(self):
        try:
            # sudo defaults write /Library/Preferences/com.apple.alf globalstate -integer 1
            fileName = "/Library/Preferences/com.apple.alf.plist"
            with open(fileName, 'rb') as fp:
                plist = plistlib.load(fp)
            return "Off" if plist["globalstate"] == 0 else "On"
        except Exception as err:
            WriteToLog(
                '[firewall]: error retrieving firewall status. Error: %s' % err)

    def __GetOperatingSystem(self):
        try:
            serialOutput = subprocess.check_output(
                ['sw_vers', '-productVersion']).decode().strip('\n')
            return serialOutput
        except:
            WriteToLog(
                '[operatingSystem]: error retrieving operating system with "sw_vers -productVersion"')
            raise

    def __GetSerialNumber(self):
        try:
            serialOutput = subprocess.check_output(
                ['system_profiler', 'SPHardwareDataType']).decode().split('\n')
            serialOutput = [row.strip() for row in serialOutput]
            for row in serialOutput:
                if row.startswith('Serial Number'):
                    serialNumber = row.split(':')
                    if serialNumber[1].strip():
                        return serialNumber[1].strip()
        except:
            WriteToLog(
                '[localhost]: error retrieving serial number with system_profiler')

    def Print(self):
        try:
            WriteToLog('  [general]:')
            WriteToLog('    [firewall]: {}'.format(self.firewall))
            WriteToLog('    [names]: {}'.format(self.computerNames))
            WriteToLog('    [os]: {}'.format(self.operatingSystem))
            WriteToLog('    [serial]: {}'.format(self.serialNumber))
            WriteToLog('  [storage]:')
            WriteToLog('    [encryption]: {}'.format(self.fileVault))
            WriteToLog('  [users]: ')
            for user in self.users:
                WriteToLog('    [user]: {0} ({1})'.format(
                    user["name"], user["id"]))
            WriteToLog('  [applications]:')
            WriteToLog('    [googleChrome]: {}'.format(self.googleChrome))
            WriteToLog('    [microsoftOffice]: {}'.format(
                self.microsoftOffice))

        except:
            WriteToLog(
                '[localhost]: error converting inventory data as string')
