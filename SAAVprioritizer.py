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

import argparse, sys
import time
from datetime import datetime
from SAAVpedia.ClassSAAVpedia import SAAVpedia

def main(theArgs):

    theStartTime = time.time()
    theSAAVpedia = SAAVpedia()

    # Reading Input file
    print 'Reading the input file...'
    #theSAAVpedia.set(file(theArgs.input).read())
    theSAAVpedia.openSCF(theArgs.input)
    #theSAAVpedia.setupToIdentifier()

    if theArgs.output:
        theOutputName = theArgs.output
    else :
        theOutputName = datetime.now().strftime('SAAVprioirtizer-%Y-%m-%d-%Hh-%Mm-%S.%fs.scf')

    print 'Fetching output data...'
    theSAAVpedia.applyFilter([])
    theSCFData = theSAAVpedia.data()

    print 'Writing {0} file...'.format(theOutputName)
    theWriter = file(theOutputName, 'w')
    for ithData in theSCFData:
        theWriter.write('\t'.join(ithData)+'\n')
    theWriter.close()

    theEndTime = time.time()
    print 'Estimated time: {0:.3f}s'.format(theEndTime-theStartTime)

    pass

if __name__ == '__main__':
    theParser = argparse.ArgumentParser(description='SAAVpedia: SAAVprioritizer program')
    theParser.add_argument('--input', dest='input', help='SCF input file path')
    theParser.add_argument('--dta', dest='dta_select', help='DTASelect-filter.txt file(s) path: ex)\"path1/file1;path2/file2;...;lastpath/last-file\"')
    theParser.add_argument('--efo', dest='efo_id', help='EFO ontology ID')
    theParser.add_argument('--output', dest='output', help='SCF output file path')
    #theParser.add_argument('--vsc_oid',action='store_true', help='EFO ontology ID of VSC_Phenotype')

    theArgs = theParser.parse_args(sys.argv[1:])

    if not theArgs.input:
        theParser.print_help()
    else :
        main(theArgs)
    pass
