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

import argparse, sys, os
import time
from datetime import datetime
from SAAVpedia import SAAVpedia

def main(theArgs):

    theStartTime = time.time()
    theSAAVpedia = SAAVpedia()

    # Reading Input file
    print 'Reading the input file...'
    theSAAVpedia.set(file(theArgs.input).read())
    theSAAVpedia.setSplitNum(1)
    #theSAAVpedia.setupToSAAVRetriever()

    if theArgs.output:
        theOutputName = theArgs.output
    else:
        theResultFolder = os.getcwd() + os.sep + 'result'
        if not os.path.exists(theResultFolder):
            os.mkdir(theResultFolder)
        elif not os.path.isdir(theResultFolder):
            theResultFolder += theResultFolder + datetime.now().strftime('-%Y-%m-%d-%Hh-%Mm-%S.%fs')
            os.mkdir(theResultFolder)
        theOutputName = theResultFolder + os.sep + datetime.now().strftime('SAAVretriever-%Y-%m-%d-%Hh-%Mm-%S.%fs.scf')

    print 'Fetching output data...'
    theRESTBegin = time.time()
    theSAAVpedia.applyFilter([])
    theSCFData = theSAAVpedia.data()
    theRESTEnd = time.time()
    print 'Estimated time for fetching data: {0:.3f}s'.format(theRESTEnd-theRESTBegin)

    print 'Writing {0} file...'.format(theOutputName)
    theWriter = file(theOutputName, 'w')
    theWriter.write(theSAAVpedia.getMetaInfo())
    theWriter.write('#'+'\t'.join(theSAAVpedia.header())+'\n')
    for ithData in theSCFData:
        theWriter.write('\t'.join(ithData)+'\n')
    theWriter.close()

    theEndTime = time.time()
    print 'Total estimated time: {0:.3f}s'.format(theEndTime-theStartTime)

    pass

if __name__ == '__main__':
    theParser = argparse.ArgumentParser(description='SAAVpedia: SAAVretriever program')
    theParser.add_argument('--input', dest='input', help='SAAVretriever input file path')
    theParser.add_argument('--output', dest='output', help='SCF output file path')

    theArgs = theParser.parse_args(sys.argv[1:])

    if not theArgs.input:
        theParser.print_help()
    else :
        main(theArgs)
    pass
