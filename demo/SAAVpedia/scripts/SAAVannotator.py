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
    #theSAAVpedia.set(file(theArgs.input).read())
    theSAAVpedia.openSCF(theArgs.input)

    if theArgs.output:
        theOutputName = theArgs.output
    else:
        theResultFolder = os.getcwd() + os.sep + 'result'
        if not os.path.exists(theResultFolder):
            os.mkdir(theResultFolder)
        elif not os.path.isdir(theResultFolder):
            theResultFolder += theResultFolder + datetime.now().strftime('-%Y-%m-%d-%Hh-%Mm-%S.%fs')
            os.mkdir(theResultFolder)
        theOutputName = theResultFolder + os.sep + datetime.now().strftime('SAAVannotator-%Y-%m-%d-%Hh-%Mm-%S.%fs.scf')

    print 'Fetching output data...'
    theRESTBegin = time.time()
    theSAAVpedia.applyFilter(theArgs._get_kwargs())
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
    theParser = argparse.ArgumentParser(description='SAAVpedia: SAAVannotator program')
    theParser.add_argument('--input', dest='input', help='SCF input file path')
    theParser.add_argument('--output', dest='output', help='Functional Annotation with SCF output file path')

    theParser.add_argument('--snv_1000g_oc', action='store_true', help='Occurring(OC) in the 1000 Genomes variant list.')
    theParser.add_argument('--snv_1000g_t_maf', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome population.')
    theParser.add_argument('--snv_1000g_eas_maf', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome East Asian population.')
    theParser.add_argument('--snv_1000g_amr_maf', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome American population.')
    theParser.add_argument('--snv_1000g_eur_maf', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome European population.')
    theParser.add_argument('--snv_1000g_afr_maf', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome African population.')
    theParser.add_argument('--snv_1000g_sas_maf', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome South Asian population.')
    theParser.add_argument('--snv_vt', action='store_true', help='Variant Type(VT)')
    theParser.add_argument('--snv_esp_oc', action='store_true', help='Occurring(OC) in the Exome Sequencing Project(ESP) variant list.')
    theParser.add_argument('--snv_esp_af_maf', action='store_true', help='Minor allele frequency(MAF) in the ESP African(AF) population.')
    theParser.add_argument('--snv_esp_eu_maf', action='store_true', help='Minor allele frequency(MAF) in the ESP European(EU) population.')
    theParser.add_argument('--snv_exac_oc', action='store_true', help='Occurring(OC) in the Exome Aggregation Consortium(ExAC) variant list.')
    theParser.add_argument('--snv_phenotype', action='store_true', help='Phenotype term.')
    theParser.add_argument('--snv_source', action='store_true', help='Reference database of SNV_Phenotype.')
    theParser.add_argument('--snv_oid', action='store_true', help='EFO ontology ID(OID) of SNV_Phenotype.')
    theParser.add_argument('--snv_phe_cls', action='store_true', help='EFO phenotype class(CLS) name of SNV_Phenotype.')
    theParser.add_argument('--snv_db', action='store_true', help='Drug bank(DB) ID.')
    theParser.add_argument('--snv_dn', action='store_true', help='Drug name(DN)')
    theParser.add_argument('--snv_dt', action='store_true', help='Drug type(DT)')
    theParser.add_argument('--snv_pgt', action='store_true', help='Pharmacological gene type')
    theParser.add_argument('--ptm', action='store_true', help='Post-Translational Modification')
    theParser.add_argument('--efo', action='store_true', help='EFO ID')
    theParser.add_argument('--ptm-filter', dest='PTM', help='Filter by Post-Translational Modification')
    theParser.add_argument('--efo-filter', dest='EFO_ID', help='Filter by EFO ID')
    theParser.add_argument('--protein_uniplot', action='store_true', help='Uniplot identifier')
    theParser.add_argument('--protein_nextprot', action='store_true', help='NextProt identifier')
    theParser.add_argument('--protein_pdb', action='store_true', help='Protein Data Bank(PDB) identifier')
    theParser.add_argument('--protein_ensembl_pro', action='store_true', help='Ensembl protein(Pro) identifier')
    theParser.add_argument('--transcript_ensembl_tra', action='store_true', help='Ensembl transcript(Tra) identifier')
    theParser.add_argument('--gene_ensembl_gen', action='store_true', help='Ensembl Gene(Gen) identifier')
    theParser.add_argument('--gene_gf', action='store_true', help='Gene Families(GF)')
    theParser.add_argument('--gene_gd', action='store_true', help='Gene description(GD)')
    theParser.add_argument('--gene_gs', action='store_true', help='Gene Symbol(GS)')
    theParser.add_argument('--gene_hgnc', action='store_true', help='HGNC ID')
    theParser.add_argument('--gene_ucsc', action='store_true', help='UCSC ID')
    theParser.add_argument('--gene_cosmic', action='store_true', help='Cosmic Gene ID')
    theParser.add_argument('--gene_entrez', action='store_true', help='Entrez ID')
    theParser.add_argument('--gene_refseq', action='store_true', help='Reference Sequence (RefSeq) accession number.')
    theParser.add_argument('--disease_omim', action='store_true', help='Omim ID')
    theParser.add_argument('--drug_pharmgkb', action='store_true', help='PharmGKB ID')
    theParser.add_argument('--drug_chembl', action='store_true', help='CHEMBL ID')
    theParser.add_argument('--literature_pmid', action='store_true', help='Pubmed ID')
    theParser.add_argument('--biological_function_string', action='store_true', help='STRING ID')
    theParser.add_argument('--biological_function_vega', action='store_true', help='Vega ID')
    theParser.add_argument('--biological_function_ena', action='store_true', help='European Nucleotide Archive ID')

    '''
        theParser.add_argument('--SNV_1000G_OC', action='store_true', help='Occurring(OC) in the 1000 Genomes variant list.')
    theParser.add_argument('--SNV_1000G_T_MAF', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome population.')
    theParser.add_argument('--SNV_1000G_EAS_MAF', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome East Asian population.')
    theParser.add_argument('--SNV_1000G_AMR_MAF', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome American population.')
    theParser.add_argument('--SNV_1000G_EUR_MAF', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome European population.')
    theParser.add_argument('--SNV_1000G_AFR_MAF', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome African population.')
    theParser.add_argument('--SNV_1000G_SAS_MAF', action='store_true', help='Minor allele frequency(MAF) in the 1000Genome South Asian population.')
    theParser.add_argument('--SNV_VT', action='store_true', help='Variant Type(VT)')
    theParser.add_argument('--SNV_ESP_OC', action='store_true', help='Occurring(OC) in the Exome Sequencing Project(ESP) variant list.')
    theParser.add_argument('--SNV_ESP_AF_MAF', action='store_true', help='Minor allele frequency(MAF) in the ESP African(AF) population.')
    theParser.add_argument('--SNV_ESP_EU_MAF', action='store_true', help='Minor allele frequency(MAF) in the ESP European(EU) population.')
    theParser.add_argument('--SNV_ExAC_OC', action='store_true', help='Occurring(OC) in the Exome Aggregation Consortium(ExAC) variant list.')
    theParser.add_argument('--SNV_Phenotype', action='store_true', help='Phenotype term.')
    theParser.add_argument('--SNV_Source', action='store_true', help='Reference database of SNV_Phenotype.')
    theParser.add_argument('--SNV_OID', action='store_true', help='EFO ontology ID(OID) of SNV_Phenotype.')
    theParser.add_argument('--SNV_Phe_CLS', action='store_true', help='EFO phenotype class(CLS) name of SNV_Phenotype.')
    theParser.add_argument('--SNV_DB', action='store_true', help='Drug bank(DB) ID.')
    theParser.add_argument('--SNV_DN', action='store_true', help='Drug name(DN)')
    theParser.add_argument('--SNV_DT', action='store_true', help='Drug type(DT)')
    theParser.add_argument('--SNV_PGT', action='store_true', help='Pharmacological gene type')
    theParser.add_argument('--PTM', action='store_true', help='Post-Translational Modification')
    theParser.add_argument('--EFO', action='store_true', help='EFO IDs')
    theParser.add_argument('--PROTEIN_Uniplot', action='store_true', help='Uniplot identifier')
    theParser.add_argument('--PROTEIN_Nextprot', action='store_true', help='NextProt identifier')
    theParser.add_argument('--PROTEIN_PDB', action='store_true', help='Protein Data Bank(PDB) identifier')
    theParser.add_argument('--PROTEIN_Enembl_Pro', action='store_true', help='Ensembl protein(Pro) identifier')
    theParser.add_argument('--TRANSCRIPT_Enembl_Tra', action='store_true', help='Ensembl transcript(Tra) identifier')
    theParser.add_argument('--GENE_Enembl_Gen', action='store_true', help='Ensembl Gene(Gen) identifier')
    theParser.add_argument('--GENE_GF', action='store_true', help='Gene Families(GF)')
    theParser.add_argument('--GENE_GD', action='store_true', help='Gene description(GD)')
    theParser.add_argument('--GENE_GS', action='store_true', help='Gene Symbol(GS)')
    theParser.add_argument('--GENE_HGNC', action='store_true', help='HGNC ID')
    theParser.add_argument('--GENE_UCSC', action='store_true', help='UCSC ID')
    theParser.add_argument('--GENE_Cosmic', action='store_true', help='Cosmic Gene ID')
    theParser.add_argument('--GENE_Entrez', action='store_true', help='Entrez ID')
    theParser.add_argument('--GENE_RefSeq', action='store_true', help='Reference Sequence (RefSeq) accession number.')
    theParser.add_argument('--Disease_Omim', action='store_true', help='Omim ID')
    theParser.add_argument('--DRUG_PharmGKB', action='store_true', help='PharmGKB ID')
    theParser.add_argument('--DRUG_CHEMBL', action='store_true', help='CHEMBL ID')
    theParser.add_argument('--Literature_PMID', action='store_true', help='Pubmed ID')
    theParser.add_argument('--Biological_function_STRING', action='store_true', help='STRING ID')
    theParser.add_argument('--Biological_function_Vega', action='store_true', help='Vega ID')
    theParser.add_argument('--Biological_function_ENA', action='store_true', help='European Nucleotide Archive ID')
    '''

    theArgs = theParser.parse_args(sys.argv[1:])

    if not theArgs.input:
        theParser.print_help()
    else :
        main(theArgs)
    pass
