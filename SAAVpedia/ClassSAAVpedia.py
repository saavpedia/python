#!/usr/bin/env python

################################################################################
# Copyright 2018 Young-Mook Kang <ymkang@thylove.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

#from db import LocalDB
from db import OnlineDB

class SAAVpedia(object) :

    def __init__(self):
        self.__itsDB = OnlineDB()
        self.__isOnlineDB = True
        self.__itsKeyMap = dict()
        self.__isFilterChanged = False
        self.__itsFilteredHeader = []
        self.__itsFilteredData = []
        self.__itsSCFLength = 15

        pass

    def __applyKeyMap(self):
        theKeyMap = dict()
        theIndex = 0
        theHeader = self.__itsDB.getHeader()
        for ithKey in theHeader:
            theKeyMap[str(ithKey).lower()] = theIndex
            theIndex += 1
            pass
        self.__itsKeyMap = theKeyMap
        pass

    def set(self, theInputText):
        self.__itsDB.set(theInputText)
        pass

    def open(self, theInputFile):
        with open(theInputFile, 'r') as theReader:
            self.__itsDB.set(theReader.read())
        pass

    def openSCF(self, theSCFFile):
        with open(theSCFFile, 'r') as theReader:
            theString = ''
            theSplitedLines = theReader.read().strip().replace('\r','').split('\n')
            for ithLine in theSplitedLines:
                theID = ithLine.split('\t')[0]
                #print theID
                theString += (theID + '\n')
            self.__itsDB.set(theString)
        pass

    def setupToSNVRetriever(self):
        self.__itsDB.setupToSNVRetriever()
        pass

    def setupToSAAVRetriever(self):
        self.__itsDB.setupToSAAVRetriever()
        pass

    def setupToRetriever(self):
        self.__itsDB.setupToRetriever()
        pass

    def setupToIdentifier(self):
        self.__itsDB.setupToIdentifier()
        pass


    def data(self):
        return self.getData()

    def header(self):
        return self.getHeader()

    def getData(self):
        theHeader, theData = self.getHeaderAndData()
        return theData

    def getHeader(self):
        theHeader, theData = self.getHeaderAndData()
        return theHeader

    def getHeaderAndData(self):
        if self.__isFilterChanged:
            return self.__itsFilteredHeader, self.__itsFilteredData
        theHeader, theData = self.__itsDB.getHeaderAndData()
        return theHeader, theData

    def toString(self, theLength = -1):
        return self.__itsDB.toString(theLength)


    def __str__(self):
        #return str(self.getHeaderAndData())
        return self.__itsDB.toString(2048)


    def applyFilter(self, theArgList = []):
        self.__isFilterChanged = True
        self.__applyKeyMap()
        theHeader = self.__itsDB.getHeader()
        theData = self.__itsDB.getData()

        theNewFilteredHeader = []
        theNewFilteredData = []
        for idx in range(self.__itsSCFLength):
            theNewFilteredHeader.append(theHeader[idx])
            pass

        for ithElement in theData:
            theNewElement = []
            for idx in range(self.__itsSCFLength):
                print idx, theData
                theNewElement.append(ithElement[idx])
                pass
            theNewFilteredData.append(theNewElement)
            pass

        theKeySet = set()
        for ithKey in theHeader:
            theKeySet.add(str(ithKey).lower())
        theKeyMapSet = set()
        for ithArg in theArgList:
            theKey = str(ithArg[0]).lower()
            if ithArg[1] and (theKey in theKeySet):
                #print self.__itsKeyMap
                theKeyMapSet.add(self.__itsKeyMap[theKey])
                pass
            pass
        theKeyMapList = list(theKeyMapSet)
        theKeyMapList.sort()
        for idx in theKeyMapList:
            theNewFilteredHeader.append(theHeader[idx])
            pass
        for ei in range(len(theData)):
            for ki in theKeyMapList:
                theNewFilteredData[ei].append(theData[ei][ki])
        self.__itsFilteredData = theNewFilteredData
        self.__itsFilteredHeader = theNewFilteredHeader
        pass




if __name__ == '__main__':
    theInput = "NDVDCAYLR\n" \
               "WLEAK"

    theSAAVpedia = SAAVpedia()

    theSAAVpedia.set(theInput)
    theSAAVpedia.setupToIdentifier()

    '''
    theSAAVpedia.applyFilter([('brp_chembl', True),
                              ('brp_ENA', True),
                              ('brp_ensembl_gen', True),
                              ('brp_ensembl_pro', True),
                              ('brp_ensembl_tra', True),
                              ('brp_entrez', True),
                              ('brp_gcosmic', True),
                              ('brp_gd', True), ('brp_gf', True), ('brp_gs', True), ('brp_hgnc', True),
                              ('vsn_exac_Oc', True), ('vsn_vt', True)])
    '''
    print theSAAVpedia
    print theSAAVpedia.header()
    print theSAAVpedia.data()

    pass

