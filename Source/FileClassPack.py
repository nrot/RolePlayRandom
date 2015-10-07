__author__ = 'nrot'

# -*- coding: utf-8 -*-

import os
import time
"""import shutil
import xml.etree.ElementTree as XMLElementTree
import glob"""


# from lxml import etree


class DoubleLog(object):
    def __init__(self, inpath, namefile):
        self.path = os.path.expanduser(inpath)
        try:
            if os.path.getsize(self.path + namefile) > 10240:
                os.remove(self.path + namefile)
        except:
            if os.path.exists(self.path) == 0:
                os.mkdir(self.path)
        try:
            self.objlogfile = open(str(self.path + namefile), 'a')
            self.objlogfile.write(time.ctime(time.time()))
            self.objlogfile.write('\n')
            self.Error = 'Done'
        except:
            print('Can`t open ', self.path, namefile)
            # self.CommandToKdeError = 'kdialog --error \'Can`t open file ' + self.path + namefile + ' \n Program will close. \' --title \'New Fons\''
            # print(self.CommandToKdeError)
            # os.system(self.CommandToKdeError)
            self.Error = 'Open Error'

    def __del__(self):
        self.objlogfile.close()

    def write(self, atype='simple', text='nothing', atime=10):
        if atype == 'connect':
            print('Can`t connect to ', str(text), '\nwait ' + str(atime) + 'min and i try connect again.\n')
            self.objlogfile.write(
                'Can`t connect to ' + str(text) + '\nwait ' + str(atime) + ' min and i try connect again.\n')
            self.objlogfile.write(
                '#################################################'
                '######################################################\n')
            self.objlogfile.write('\n')
        elif atype == 'simple':
            print(text)
            self.objlogfile.write(text)
            self.objlogfile.write('\n')
        return 'Done'

    def save(self):
        self.objlogfile.flush()


"""class OPtionsFileClass(object):
    def __init__(self):
        self.path = './'
        self.namefile = 'Option.xml'
        self.originpath = "./OriginFile.xml"
        if os.path.exists(self.path) == 0:
            os.mkdir(self.path)
        try:
            self.originfile = open(self.originpath, 'r')
        except:
            print('Can`t open ', self.path, self.namefile)
            #self.CommandToKdeError = 'kdialog --error \'Can`t open file ' + self.originpath + '\nProgram will close. \' --title \'New Fons\''
            #print(self.CommandToKdeError)
            #os.system(self.CommandToKdeError)
            self.Error = 'Open Error'
        try:
            if os.path.exists(self.path + self.namefile) == True:
                self.optionsfile = open(str(self.path + self.namefile), 'r')
            else:
                shutil.copy(self.originpath, self.path + self.namefile)
            self.Error = 'Done'
        except:
            print('Can`t open ', self.path, self.namefile)
            #self.CommandToKdeError = 'kdialog --error \'Can`t open file ' + self.path + self.namefile + '\nProgram will close. \' --title \'New Fons\''
            #print(self.CommandToKdeError)
            #os.system(self.CommandToKdeError)
            self.Error = 'Open Error'
        print(self.path + self.namefile)
        self.parser = etree.XMLParser(recover=True)
        if self.path == './':
            self.parsedoption = XMLElementTree.parse(self.namefile, parser=self.parser)
        else:
            self.parsedoption = XMLElementTree.parse(self.path + self.namefile, parser=self.parser)
        self.parsedorigin = XMLElementTree.parse(self.originpath, parser=self.parser)

        self.OriginVersion = self.parsedorigin.findall('Version')[0].text
        self.OptionVersion = self.parsedoption.findall('Version')[0].text
        if self.OriginVersion != self.OptionVersion:
            self.Warning = 'Different version'

    def __del__(self):
        try:
            self.optionsfile.close()
            self.originfile.close()
        except:
            self.Error = 'Bag close'

    def GetOptiions(self):
        try:
            self.PathToImage = os.path.expanduser(self.parsedoption.findall('PathToImage')[0].text)
            #self.PathToImage = unicodedata.normalize('NFKD', self.PathToImage).encode('ascii', 'ignore')
            if os.path.exists(self.PathToImage) != True:
                os.makedirs(self.PathToImage)
            if self.OriginVersion != self.OptionVersion:
                self.Version = 'Different version.'
            else:
                self.Version = self.OptionVersion
            self.OptionPathLog = os.path.expanduser(self.parsedoption.findall('PathLog')[0].text)
            self.OriginPathLog = os.path.expanduser(self.parsedorigin.findall('PathLog')[0].text)
            self.TimeToSleep = int(self.parsedoption.findall('time')[0].text)
            self.AmountImageSave = int(self.parsedoption.findall('amountImageSave')[0].text)
            self.ImageAmount = int(self.parsedoption.findall('amountImage')[0].text)
        except:
            self.Error = 'second parsed error'
    def EditOptions(self, Setting, NewValue):
        if self.parsedoption.findall(str(Setting)) == []:
          return 'Not Have yhis Setting'
        else:
            #self.cachestr = unicodedata.normalize('NFKD', str(self.AmountImageSave)).encode('ascii', 'ignore')
            self.cachestr = self.parsedoption.findall(str(Setting))[0]
            self.cachestr.text = str(NewValue)
            self.GetOptiions()
            del self.cachestr
            return True
    def FindImage(self):
        os.chdir(self.PathToImage)
        self.jpgAmount = len(glob.glob('*.jpg'))
        self.jpgAmount += len(glob.glob('*.jpeg'))
        self.pngAmount = len(glob.glob('*.png'))
        self.EditOptions('amountImage', self.jpgAmount+self.pngAmount)
        del self.jpgAmount, self.pngAmount """
