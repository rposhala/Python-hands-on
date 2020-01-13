#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[1]:


NAME = "ROHITH KUMAR POSHALA"
COLLABORATORS = ""


# ---

# # Introduction 
# This is the first of four labs that you will do in this course.  In this lab, you will parse a variant call format file (https://en.wikipedia.org/wiki/Variant_Call_Format). This file has one thousand variants in it. Each line after the header lines is a variant. Open the variant file and inspect its contents. You will parse each line and transform it into a JSON. The output will look something like this (I have shortened the output):
# ```
# {
#         "ALT": "G",
#         "CHROM": "4",
#         "FILTER": "PASS",
#         "ID": ".",
#         "INFO": {
#            
#             "Gene.ensGene": "ENSG00000109471,ENSG00000138684",
#             "Gene.refGene": "IL2,IL21",
#             "GeneDetail.ensGene": "dist=38306,dist=117597",
#             "GeneDetail.refGene": "dist=38536,dist=117597"
#         },
#         "POS": 123416186,
#         "QUAL" :23.25,
#         "REF": "A",
#         "SAMPLE": {
#             "XG102": {
#                 "AD": "51,8",
#                 "DP": "59",
#                 "GQ": "32",
#                 "GT": "0/1",
#                 "PL": "32,0,1388"
#             }
#     }
# ```
# The lab will guide you through writing small functions that will be used to generate the JSON above. Note that the method outlined in this lab is not necessarily optimal. It is just one way of parsing the file and teaching you how to break a large problem into small parts. 
# 
# Note that the header which corresponds to the columns starts with one hash/pound (#) symbol. Skip all headers that start with two hashes/pounds (##).

# # Part 1 (3 points)
# Write a function whose input is a string. This function determines the data type of the input string. The data types can be a float, int, or string. 

# In[2]:


def determine_data_type(value):
    """
    The function takes a string input and determines its data type to be either a float, int, or string. 
    """
    # YOUR CODE HERE
    try :
        float_v = float(value)
        try :
            integer = int(value)
            return type(integer)
        except ValueError :
            return type(float_v)
    except ValueError :
        return type(value)
#     raise NotImplementedError()


# In[3]:


assert determine_data_type('1.2') == float
assert determine_data_type('4') == int
assert determine_data_type('EAS503') == str


# # Part 2 (4 points)
# Write a function whose input is a list of strings.  This function determines the correct data type of all the elements in the list. For example, ['1', '2', '3'] is int, ['1.1', '2.2', '3.3'] is float, ['1.1', '2', '3.3'] is also float, and ['1.1', '234String', '3.3'] is str. The purpose of this function to figure out what to cast an array of strings to. Some lists might be all ints, in which case the data type is int. Some might be a mixure of ints and floats, in which case the data type will be float. Some lists might be a mixture of ints, floats, and strings, in which case the data type of the list will be string. 

# In[4]:


def determine_data_type_of_list(values):
    """
    Function takes a list of strings and determines their data type. 

    """
    # YOUR CODE HERE
    list_type = []
    for i in values :
        list_type.append(determine_data_type(i))
    if str in list_type :
        return str
    elif float in list_type:
        return float
    else:
        return int
    raise NotImplementedError()


# In[5]:


assert determine_data_type_of_list(['1', '2', '3']) == int
assert determine_data_type_of_list(['1.1', '2.2', '3.3']) == float
assert determine_data_type_of_list(['1.1', '2', '3.3']) == float
assert determine_data_type_of_list(['1.1', '234String', '3.3']) == str


# # Part 3 (3 points)
# Write a function whose inputs a format field and a sample field. The format field looks like `format_field = 'GT:AD:DP:GQ:PGT:PID:PL'` and
# the sample field looks like
# 
# ```
# sample_field = {'XG102': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
#              'XG103': '1/1:0,52:52:99:.:.:1517,156,0',
#              'XG104': '0/1:34,38:72:99:.:.:938,0,796',
#              'XG202': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
#              'XG203': '1/1:0,52:52:99:.:.:1517,156,0',
#              'XG204': '0/1:34,38:72:99:.:.:938,0,796',
#              'XG302': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
#              'XG303': '1/1:0,52:52:99:.:.:1517,156,0',
#              'XG304': '0/1:34,38:72:99:.:.:938,0,796',
#              'XG402': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
#              'XG403': '1/1:0,52:52:99:.:.:1517,156,0',
#              'XG404': '0/1:34,38:72:99:.:.:938,0,796'}
# ```
# Transform the inputs such that the output looks like this:
# ```
# output = {'XG102': {'AD': '0,76',
#            'DP': '76',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '1|1',
#            'PID': '48306945_C_G',
#            'PL': '3353,229,0'},
#  'XG103': {'AD': '0,52',
#            'DP': '52',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '1517,156,0'},
#  'XG104': {'AD': '34,38',
#            'DP': '72',
#            'GQ': '99',
#            'GT': '0/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '938,0,796'},
#  'XG202': {'AD': '0,76',
#            'DP': '76',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '1|1',
#            'PID': '48306945_C_G',
#            'PL': '3353,229,0'},
#  'XG203': {'AD': '0,52',
#            'DP': '52',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '1517,156,0'},
#  'XG204': {'AD': '34,38',
#            'DP': '72',
#            'GQ': '99',
#            'GT': '0/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '938,0,796'},
#  'XG302': {'AD': '0,76',
#            'DP': '76',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '1|1',
#            'PID': '48306945_C_G',
#            'PL': '3353,229,0'},
#  'XG303': {'AD': '0,52',
#            'DP': '52',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '1517,156,0'},
#  'XG304': {'AD': '34,38',
#            'DP': '72',
#            'GQ': '99',
#            'GT': '0/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '938,0,796'},
#  'XG402': {'AD': '0,76',
#            'DP': '76',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '1|1',
#            'PID': '48306945_C_G',
#            'PL': '3353,229,0'},
#  'XG403': {'AD': '0,52',
#            'DP': '52',
#            'GQ': '99',
#            'GT': '1/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '1517,156,0'},
#  'XG404': {'AD': '34,38',
#            'DP': '72',
#            'GQ': '99',
#            'GT': '0/1',
#            'PGT': '.',
#            'PID': '.',
#            'PL': '938,0,796'}}
# ```
# 

# In[6]:


format_field = "GT:AD:DP:GQ:PGT:PID:PL"
sample_field = {'XG102': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG103': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG104': '0/1:34,38:72:99:.:.:938,0,796',
             'XG202': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG203': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG204': '0/1:34,38:72:99:.:.:938,0,796',
             'XG302': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG303': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG304': '0/1:34,38:72:99:.:.:938,0,796',
             'XG402': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG403': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG404': '0/1:34,38:72:99:.:.:938,0,796'}


def format_sample_fields(format_field, sample_field):
    """
    Format the sample fields given the description above. Data is already provided.
    """
    
    # YOUR CODE HERE
    list_format = format_field.split(":")
    dic = {}
    l_keys = [i for i in sample_field.keys()]
    for i in range(len(l_keys)):
        l_value = sample_field[l_keys[i]].split(":")
        sub_dic = dict(zip(list_format,l_value))
        dic.update({l_keys[i] : sub_dic}) 
    return dic
    
    raise NotImplementedError()


# In[7]:


solution = {'XG102': {'AD': '0,76',
           'DP': '76',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '1|1',
           'PID': '48306945_C_G',
           'PL': '3353,229,0'},
 'XG103': {'AD': '0,52',
           'DP': '52',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '.',
           'PID': '.',
           'PL': '1517,156,0'},
 'XG104': {'AD': '34,38',
           'DP': '72',
           'GQ': '99',
           'GT': '0/1',
           'PGT': '.',
           'PID': '.',
           'PL': '938,0,796'},
 'XG202': {'AD': '0,76',
           'DP': '76',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '1|1',
           'PID': '48306945_C_G',
           'PL': '3353,229,0'},
 'XG203': {'AD': '0,52',
           'DP': '52',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '.',
           'PID': '.',
           'PL': '1517,156,0'},
 'XG204': {'AD': '34,38',
           'DP': '72',
           'GQ': '99',
           'GT': '0/1',
           'PGT': '.',
           'PID': '.',
           'PL': '938,0,796'},
 'XG302': {'AD': '0,76',
           'DP': '76',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '1|1',
           'PID': '48306945_C_G',
           'PL': '3353,229,0'},
 'XG303': {'AD': '0,52',
           'DP': '52',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '.',
           'PID': '.',
           'PL': '1517,156,0'},
 'XG304': {'AD': '34,38',
           'DP': '72',
           'GQ': '99',
           'GT': '0/1',
           'PGT': '.',
           'PID': '.',
           'PL': '938,0,796'},
 'XG402': {'AD': '0,76',
           'DP': '76',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '1|1',
           'PID': '48306945_C_G',
           'PL': '3353,229,0'},
 'XG403': {'AD': '0,52',
           'DP': '52',
           'GQ': '99',
           'GT': '1/1',
           'PGT': '.',
           'PID': '.',
           'PL': '1517,156,0'},
 'XG404': {'AD': '34,38',
           'DP': '72',
           'GQ': '99',
           'GT': '0/1',
           'PGT': '.',
           'PID': '.',
           'PL': '938,0,796'}}

format_field = "GT:AD:DP:GQ:PGT:PID:PL"
sample_field = {'XG102': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG103': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG104': '0/1:34,38:72:99:.:.:938,0,796',
             'XG202': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG203': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG204': '0/1:34,38:72:99:.:.:938,0,796',
             'XG302': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG303': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG304': '0/1:34,38:72:99:.:.:938,0,796',
             'XG402': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
             'XG403': '1/1:0,52:52:99:.:.:1517,156,0',
             'XG404': '0/1:34,38:72:99:.:.:938,0,796'}

format_output = format_sample_fields(format_field, sample_field)

assert format_output['XG102'] == solution ['XG102']
assert format_output['XG302'] == solution ['XG302']
assert format_output['XG404'] == solution ['XG404']


# # Part 4 (10 points) 
# Write a function whose inputs are a list containing the vcf header and a variant line.  The function should return a dictionary using the header as keys and the variant line as values. The function should use the `format_sample_fields` you wrote previously to format the sample fields. The output of the first line looks like this:
# ```
# {'ALT': 'G',
#  'CHROM': '4',
#  'FILTER': 'PASS',
#  'ID': '.',
#  'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2\\x3bIL21;GeneDetail.refGene=dist\\x3d38536\\x3bdist\\x3d117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471\\x3bENSG00000138684;GeneDetail.ensGene=dist\\x3d38306\\x3bdist\\x3d117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END',
#  'POS': '123416186',
#  'QUAL': '23.25',
#  'REF': 'A',
#  'SAMPLE': {'XG102': {'AD': '51,8',
#             'DP': '59',
#             'GQ': '32',
#             'GT': '0/1',
#             'PL': '32,0,1388'},
#        'XG103': {'AD': '47,0',
#             'DP': '47',
#             'GQ': '99',
#             'GT': '0/0',
#             'PL': '0,114,1353'},
#        'XG104': {'AD': '74,0',
#             'DP': '74',
#             'GQ': '51',
#             'GT': '0/0',
#             'PL': '0,51,1827'},
#        'XG202': {'AD': '51,8',
#             'DP': '59',
#             'GQ': '32',
#             'GT': '0/1',
#             'PL': '32,0,1388'},
#        'XG203': {'AD': '47,0',
#             'DP': '47',
#             'GQ': '99',
#             'GT': '0/0',
#             'PL': '0,114,1353'},
#        'XG204': {'AD': '74,0',
#             'DP': '74',
#             'GQ': '51',
#             'GT': '0/0',
#             'PL': '0,51,1827'},
#        'XG302': {'AD': '51,8',
#             'DP': '59',
#             'GQ': '32',
#             'GT': '0/1',
#             'PL': '32,0,1388'},
#        'XG303': {'AD': '47,0',
#             'DP': '47',
#             'GQ': '99',
#             'GT': '0/0',
#             'PL': '0,114,1353'},
#        'XG304': {'AD': '74,0',
#             'DP': '74',
#             'GQ': '51',
#             'GT': '0/0',
#             'PL': '0,51,1827'},
#        'XG402': {'AD': '51,8',
#             'DP': '59',
#             'GQ': '32',
#             'GT': '0/1',
#             'PL': '32,0,1388'},
#        'XG403': {'AD': '47,0',
#             'DP': '47',
#             'GQ': '99',
#             'GT': '0/0',
#             'PL': '0,114,1353'},
#        'XG404': {'AD': '74,0',
#             'DP': '74',
#             'GQ': '51',
#             'GT': '0/0',
#             'PL': '0,51,1827'}}}
#             
# ```
# 
# 

# In[8]:


header = "CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	XG102	XG103	XG104	XG202	XG203	XG204	XG302	XG303	XG304	XG402	XG403	XG404".split('\t')
line = """4	123416186	.	A	G	23.25	PASS	AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2\x3bIL21;GeneDetail.refGene=dist\x3d38536\x3bdist\x3d117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471\x3bENSG00000138684;GeneDetail.ensGene=dist\x3d38306\x3bdist\x3d117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END	GT:AD:DP:GQ:PL	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827"""

def create_dict_from_line(header, line):
    """
    Given the header and a single line, transform them into dictionary as described above. 
    Header and line input are provided in this cell. 
    """
    # YOUR CODE HERE
    l = line.split("\t")
    dic = dict(zip(header,l))
    l_keys = [i for i in dic.keys()]
    w = 'FORMAT'
    f = dic[w]
    del dic[w]
    xg = [i for i in l_keys if 'XG' in i]
    s = dict()
    for i in xg:
        s.update({i:dic[i]})
        del dic[i]
    e = format_sample_fields(f,s)
    dic.update({'SAMPLE': e})
    return dic
    raise NotImplementedError()


# In[9]:


solution = {'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2;IL21;GeneDetail.refGene=dist=38536;dist=117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471;ENSG00000138684;GeneDetail.ensGene=dist=38306;dist=117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END', 'SAMPLE': {'XG404': {'GT': '0/0', 'GQ': '51', 'AD': '74,0', 'DP': '74', 'PL': '0,51,1827'}, 'XG402': {'GT': '0/1', 'GQ': '32', 'AD': '51,8', 'DP': '59', 'PL': '32,0,1388'}, 'XG403': {'GT': '0/0', 'GQ': '99', 'AD': '47,0', 'DP': '47', 'PL': '0,114,1353'}, 'XG303': {'GT': '0/0', 'GQ': '99', 'AD': '47,0', 'DP': '47', 'PL': '0,114,1353'}, 'XG302': {'GT': '0/1', 'GQ': '32', 'AD': '51,8', 'DP': '59', 'PL': '32,0,1388'}, 'XG304': {'GT': '0/0', 'GQ': '51', 'AD': '74,0', 'DP': '74', 'PL': '0,51,1827'}, 'XG202': {'GT': '0/1', 'GQ': '32', 'AD': '51,8', 'DP': '59', 'PL': '32,0,1388'}, 'XG203': {'GT': '0/0', 'GQ': '99', 'AD': '47,0', 'DP': '47', 'PL': '0,114,1353'}, 'XG204': {'GT': '0/0', 'GQ': '51', 'AD': '74,0', 'DP': '74', 'PL': '0,51,1827'}, 'XG103': {'GT': '0/0', 'GQ': '99', 'AD': '47,0', 'DP': '47', 'PL': '0,114,1353'}, 'XG102': {'GT': '0/1', 'GQ': '32', 'AD': '51,8', 'DP': '59', 'PL': '32,0,1388'}, 'XG104': {'GT': '0/0', 'GQ': '51', 'AD': '74,0', 'DP': '74', 'PL': '0,51,1827'}}, 'CHROM': '4', 'POS': '123416186', 'FILTER': 'PASS', 'QUAL': '23.25', 'ALT': 'G', 'REF': 'A', 'ID': '.'}
header = "CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	XG102	XG103	XG104	XG202	XG203	XG204	XG302	XG303	XG304	XG402	XG403	XG404".split('\t')
line = """4	123416186	.	A	G	23.25	PASS	AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2\x3bIL21;GeneDetail.refGene=dist\x3d38536\x3bdist\x3d117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471\x3bENSG00000138684;GeneDetail.ensGene=dist\x3d38306\x3bdist\x3d117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END	GT:AD:DP:GQ:PL	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827"""


assert create_dict_from_line(header, line) == solution


# # Part 5 (10 points)
# Write a function whose input is a filename for a vcf. The function reads the vcf file one variant at a time and transforms it into a dictionary using the create_dict_from_line function. It returns a list containing all the variant dictionaries. 

# In[10]:


def read_vcf_file(filename):
    """
    See description above
    """
    # YOUR CODE HERE
    with open(filename, 'r') as fp:
        header=[]
        line=[]
        for l in fp:
            if l.startswith('##'):
                continue # lines starting with double hash are skipped
            else:
                if l.startswith('#'):
                    header.append(l.strip()[1:])
                else:
                    line.append(l.strip())
    list_variant_dict=[]
    for i in range(len(line)):
        list_variant_dict.append(create_dict_from_line(header[0].split("\t"), line[i]))
      
    return list_variant_dict

#     raise NotImplementedError()


# In[11]:


expected_output = [{'ALT': 'G',
  'CHROM': '4',
  'FILTER': 'PASS',
  'ID': '.',
  'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2\\x3bIL21;GeneDetail.refGene=dist\\x3d38536\\x3bdist\\x3d117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471\\x3bENSG00000138684;GeneDetail.ensGene=dist\\x3d38306\\x3bdist\\x3d117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END',
  'POS': '123416186',
  'QUAL': '23.25',
  'REF': 'A',
  'SAMPLE': {'XG102': {'AD': '51,8',
                       'DP': '59',
                       'GQ': '32',
                       'GT': '0/1',
                       'PL': '32,0,1388'},
             'XG103': {'AD': '47,0',
                       'DP': '47',
                       'GQ': '99',
                       'GT': '0/0',
                       'PL': '0,114,1353'},
             'XG104': {'AD': '74,0',
                       'DP': '74',
                       'GQ': '51',
                       'GT': '0/0',
                       'PL': '0,51,1827'},
             'XG202': {'AD': '51,8',
                       'DP': '59',
                       'GQ': '32',
                       'GT': '0/1',
                       'PL': '32,0,1388'},
             'XG203': {'AD': '47,0',
                       'DP': '47',
                       'GQ': '99',
                       'GT': '0/0',
                       'PL': '0,114,1353'},
             'XG204': {'AD': '74,0',
                       'DP': '74',
                       'GQ': '51',
                       'GT': '0/0',
                       'PL': '0,51,1827'},
             'XG302': {'AD': '51,8',
                       'DP': '59',
                       'GQ': '32',
                       'GT': '0/1',
                       'PL': '32,0,1388'},
             'XG303': {'AD': '47,0',
                       'DP': '47',
                       'GQ': '99',
                       'GT': '0/0',
                       'PL': '0,114,1353'},
             'XG304': {'AD': '74,0',
                       'DP': '74',
                       'GQ': '51',
                       'GT': '0/0',
                       'PL': '0,51,1827'},
             'XG402': {'AD': '51,8',
                       'DP': '59',
                       'GQ': '32',
                       'GT': '0/1',
                       'PL': '32,0,1388'},
             'XG403': {'AD': '47,0',
                       'DP': '47',
                       'GQ': '99',
                       'GT': '0/0',
                       'PL': '0,114,1353'},
             'XG404': {'AD': '74,0',
                       'DP': '74',
                       'GQ': '51',
                       'GT': '0/0',
                       'PL': '0,51,1827'}}}]

result = read_vcf_file('single_variant.vcf')
assert expected_output == result


# # Part 6 (5 points)
# Write a function that extracts the info field from the data dictionary that was created in the previous part. The function should return all the info field dictionaries as list. 
# 

# In[12]:


def extract_info_field(data):
    """
    See description in part 6
    """
    # YOUR CODE HERE
    return [i['INFO'] for i in data]
#     raise NotImplementedError()


# In[13]:


expected_results = open('info_field.vcf', 'r').readline().strip()
info_field = extract_info_field(result)

assert expected_results == info_field[0]


# # Part 7 (10 points)
# You now need to figure out that data types for each of the info fields. 
# Begin by writing a function that first takes the info fields and turns them into a dictionary. Make sure to skip any fields that do not have a value or are missing a value. Also replace \\x3b with a comma and \\x3d with an equal sign.  

# In[14]:


def create_dictionary_of_info_field_values(data):
    """
    See description of part 7
    """
    # YOUR CODE HERE
    dic_info_field_values = {}
    key_list = []
    for i in data:
        info_list = i.split(";")
        for j in info_list:
            if '=' in j :
                int_list = []
                k_v_list = j.split("=")
                k_v_list[1] = k_v_list[1].replace('\\x3b',',')
                k_v_list[1] = k_v_list[1].replace('\\x3d','=')
                if k_v_list[0] not in key_list:
                    key_list.append(k_v_list[0])
                    if k_v_list[1] != '.':
                        int_list.append(k_v_list[1])
                    dic_info_field_values.update({k_v_list[0]:int_list})
                else :
                    if k_v_list[1] != '.':
                        dic_info_field_values[k_v_list[0]].append(k_v_list[1])
    return dic_info_field_values
    
#     raise NotImplementedError()


# In[15]:



info_field = extract_info_field(result)
expected_results = {'AC': ['1'], 'AF': ['0.167'], 'AN': ['6'], 'BaseQRankSum': ['-2.542'], 'ClippingRankSum': ['0'], 'DP': ['180'], 'ExcessHet': ['3.0103'], 'FS': ['0'], 'MLEAC': ['1'], 'MLEAF': ['0.167'], 'MQ': ['52.77'], 'MQRankSum': ['-4.631'], 'QD': ['0.39'], 'ReadPosRankSum': ['1.45'], 'SOR': ['0.758'], 'VQSLOD': ['-8.209'], 'culprit': ['MQ'], 'ANNOVAR_DATE': ['2018-04-16'], 'Func.refGene': ['intergenic'], 'Gene.refGene': ['IL2,IL21'], 'GeneDetail.refGene': ['dist=38536,dist=117597'], 'ExonicFunc.refGene': [], 'AAChange.refGene': [], 'Func.ensGene': ['intergenic'], 'Gene.ensGene': ['ENSG00000109471,ENSG00000138684'], 'GeneDetail.ensGene': ['dist=38306,dist=117597'], 'ExonicFunc.ensGene': [], 'AAChange.ensGene': [], 'cytoBand': ['4q27'], 'gwasCatalog': [], 'tfbsConsSites': [], 'wgRna': [], 'targetScanS': [], 'Gene_symbol': [], 'OXPHOS_Complex': [], 'Ensembl_Gene_ID': [], 'Ensembl_Protein_ID': [], 'Uniprot_Name': [], 'Uniprot_ID': [], 'NCBI_Gene_ID': [], 'NCBI_Protein_ID': [], 'Gene_pos': [], 'AA_pos': [], 'AA_sub': [], 'Codon_sub': [], 'dbSNP_ID': [], 'PhyloP_46V': [], 'PhastCons_46V': [], 'PhyloP_100V': [], 'PhastCons_100V': [], 'SiteVar': [], 'PolyPhen2_prediction': [], 'PolyPhen2_score': [], 'SIFT_prediction': [], 'SIFT_score': [], 'FatHmm_prediction': [], 'FatHmm_score': [], 'PROVEAN_prediction': [], 'PROVEAN_score': [], 'MutAss_prediction': [], 'MutAss_score': [], 'EFIN_Swiss_Prot_Score': [], 'EFIN_Swiss_Prot_Prediction': [], 'EFIN_HumDiv_Score': [], 'EFIN_HumDiv_Prediction': [], 'CADD_score': [], 'CADD_Phred_score': [], 'CADD_prediction': [], 'Carol_prediction': [], 'Carol_score': [], 'Condel_score': [], 'Condel_pred': [], 'COVEC_WMV': [], 'COVEC_WMV_prediction': [], 'PolyPhen2_score_transf': [], 'PolyPhen2_pred_transf': [], 'SIFT_score_transf': [], 'SIFT_pred_transf': [], 'MutAss_score_transf': [], 'MutAss_pred_transf': [], 'Perc_coevo_Sites': [], 'Mean_MI_score': [], 'COSMIC_ID': [], 'Tumor_site': [], 'Examined_samples': [], 'Mutation_frequency': [], 'US': [], 'Status': [], 'Associated_disease': [], 'Presence_in_TD': [], 'Class_predicted': [], 'Prob_N': [], 'Prob_P': [], 'SIFT_converted_rankscore': [], 'SIFT_pred': [], 'Polyphen2_HDIV_score': [], 'Polyphen2_HDIV_rankscore': [], 'Polyphen2_HDIV_pred': [], 'Polyphen2_HVAR_score': [], 'Polyphen2_HVAR_rankscore': [], 'Polyphen2_HVAR_pred': [], 'LRT_score': [], 'LRT_converted_rankscore': [], 'LRT_pred': [], 'MutationTaster_score': [], 'MutationTaster_converted_rankscore': [], 'MutationTaster_pred': [], 'MutationAssessor_score': [], 'MutationAssessor_score_rankscore': [], 'MutationAssessor_pred': [], 'FATHMM_score': [], 'FATHMM_converted_rankscore': [], 'FATHMM_pred': [], 'PROVEAN_converted_rankscore': [], 'PROVEAN_pred': [], 'VEST3_score': [], 'VEST3_rankscore': [], 'MetaSVM_score': [], 'MetaSVM_rankscore': [], 'MetaSVM_pred': [], 'MetaLR_score': [], 'MetaLR_rankscore': [], 'MetaLR_pred': [], 'M-CAP_score': [], 'M-CAP_rankscore': [], 'M-CAP_pred': [], 'CADD_raw': [], 'CADD_raw_rankscore': [], 'CADD_phred': [], 'DANN_score': [], 'DANN_rankscore': [], 'fathmm-MKL_coding_score': [], 'fathmm-MKL_coding_rankscore': [], 'fathmm-MKL_coding_pred': [], 'Eigen_coding_or_noncoding': [], 'Eigen-raw': [], 'Eigen-PC-raw': [], 'GenoCanyon_score': [], 'GenoCanyon_score_rankscore': [], 'integrated_fitCons_score': [], 'integrated_fitCons_score_rankscore': [], 'integrated_confidence_value': [], 'GERP++_RS': [], 'GERP++_RS_rankscore': [], 'phyloP100way_vertebrate': [], 'phyloP100way_vertebrate_rankscore': [], 'phyloP20way_mammalian': [], 'phyloP20way_mammalian_rankscore': [], 'phastCons100way_vertebrate': [], 'phastCons100way_vertebrate_rankscore': [], 'phastCons20way_mammalian': [], 'phastCons20way_mammalian_rankscore': [], 'SiPhy_29way_logOdds': [], 'SiPhy_29way_logOdds_rankscore': [], 'Interpro_domain': [], 'GTEx_V6_gene': [], 'GTEx_V6_tissue': [], 'esp6500siv2_all': [], 'esp6500siv2_aa': [], 'esp6500siv2_ea': [], 'ExAC_ALL': [], 'ExAC_AFR': [], 'ExAC_AMR': [], 'ExAC_EAS': [], 'ExAC_FIN': [], 'ExAC_NFE': [], 'ExAC_OTH': [], 'ExAC_SAS': [], 'ExAC_nontcga_ALL': [], 'ExAC_nontcga_AFR': [], 'ExAC_nontcga_AMR': [], 'ExAC_nontcga_EAS': [], 'ExAC_nontcga_FIN': [], 'ExAC_nontcga_NFE': [], 'ExAC_nontcga_OTH': [], 'ExAC_nontcga_SAS': [], 'ExAC_nonpsych_ALL': [], 'ExAC_nonpsych_AFR': [], 'ExAC_nonpsych_AMR': [], 'ExAC_nonpsych_EAS': [], 'ExAC_nonpsych_FIN': [], 'ExAC_nonpsych_NFE': [], 'ExAC_nonpsych_OTH': [], 'ExAC_nonpsych_SAS': [], '1000g2015aug_all': [], '1000g2015aug_afr': [], '1000g2015aug_amr': [], '1000g2015aug_eur': [], '1000g2015aug_sas': [], 'CLNALLELEID': [], 'CLNDN': [], 'CLNDISDB': [], 'CLNREVSTAT': [], 'CLNSIG': [], 'dbscSNV_ADA_SCORE': [], 'dbscSNV_RF_SCORE': [], 'snp138NonFlagged': [], 'avsnp150': [], 'CADD13_RawScore': ['0.015973'], 'CADD13_PHRED': ['2.741'], 'Eigen': ['-0.3239'], 'REVEL': [], 'MCAP': [], 'ICGC_Id': [], 'ICGC_Occurrence': [], 'gnomAD_genome_ALL': ['0.0003'], 'gnomAD_genome_AFR': ['0.0001'], 'gnomAD_genome_AMR': ['0'], 'gnomAD_genome_ASJ': ['0'], 'gnomAD_genome_EAS': ['0.0007'], 'gnomAD_genome_FIN': ['0.0009'], 'gnomAD_genome_NFE': ['0.0002'], 'gnomAD_genome_OTH': ['0.0011'], 'gerp++gt2': [], 'cosmic70': [], 'InterVar_automated': [], 'PVS1': [], 'PS1': [], 'PS2': [], 'PS3': [], 'PS4': [], 'PM1': [], 'PM2': [], 'PM3': [], 'PM4': [], 'PM5': [], 'PM6': [], 'PP1': [], 'PP2': [], 'PP3': [], 'PP4': [], 'PP5': [], 'BA1': [], 'BS1': [], 'BS2': [], 'BS3': [], 'BS4': [], 'BP1': [], 'BP2': [], 'BP3': [], 'BP4': [], 'BP5': [], 'BP6': [], 'BP7': [], 'Kaviar_AF': [], 'Kaviar_AC': [], 'Kaviar_AN': []}
results = create_dictionary_of_info_field_values(info_field)
assert expected_results == results


# # Part 8 (5 points)
# Write a function whose input is the output from `create_dictionary_of_info_field_values` and uses the previously written function `determine_data_type_of_list` to determine the data type of each of the info fields. The output is a dictionary whose keys are the name of the info fields and values are the data type.  

# In[16]:


def determine_data_type_of_info_fields(data):
    """
    See desription in part 8
    """
    # YOUR CODE HERE
    dict_data_type_of_info = {}
    for i in data.keys():
        if len(data[i]) != 0:
            dict_data_type_of_info.update({i:determine_data_type_of_list(data[i])})
    return dict_data_type_of_info
#     raise NotImplementedError()


# In[17]:


data = {'key1': ['1', '2', '3'], 'key2':['1.1', '2.2', '3.3'], 'key3': ['1.1', '2', '3.3'], 'key4': ['1.1', '234String', '3.3']}
expected_results = {'key1': int, 'key2': float, 'key3': float, 'key4': str}

assert determine_data_type_of_info_fields(data) == expected_results


# # Part 9  (No points)
# Write a function whose first input is the data from  `read_vcf_file` and the second input is the output from `determine_data_type_of_info_fields`. The function converts the info field into a dictionary and uses the data types that you determined to cast each field into the correct data type. Make sure to convert the `POS` to int and `QUAL` to float. Replace any `\\x3b` with a comma and any `\\x3d` with an equal sign. The output will look something like this (I have removed most of the fields):
# 
# The output will look something like this 
# ```
# {
#         "ALT": "G",
#         "CHROM": "4",
#         "FILTER": "PASS",
#         "ID": ".",
#         "INFO": {
#            
#             "Gene.ensGene": "ENSG00000109471,ENSG00000138684",
#             "Gene.refGene": "IL2,IL21",
#             "GeneDetail.ensGene": "dist=38306,dist=117597",
#             "GeneDetail.refGene": "dist=38536,dist=117597"
#         },
#         "POS": 123416186,
#         "QUAL" :23.25,
#         "REF": "A",
#         "SAMPLE": {
#             "XG102": {
#                 "AD": "51,8",
#                 "DP": "59",
#                 "GQ": "32",
#                 "GT": "0/1",
#                 "PL": "32,0,1388"
#             }
#     }
# ```

# In[18]:


def format_data(data, info_field_data_type):
    # YOUR CODE HERE
    formatted_list = []
    a = 0
    b = 0
    c = 0
    for i in data:
        i['POS'] = int(i['POS'])
        i['QUAL'] = float(i['QUAL'])
        dict_info = create_dictionary_of_info_field_values([i['INFO']])
        del_keys = []
        for j in dict_info.keys():
            if len(dict_info[j]) == 1:
                dict_info[j] = info_field_data_type[j](dict_info[j][0])
                c+=1
            elif len(dict_info[j]) == 0:
                del_keys.append(j)
            else :
                for k in range(len(dict_info[j])):
                    k = info_field_data_type[j](k)
        for key in del_keys:
            del dict_info[key]
        i['INFO'] = dict_info
        formatted_list.append(i)
    return formatted_list
#     raise NotImplementedError()


# In[19]:


data = read_vcf_file('lab1_data.vcf')
result = extract_info_field(data)
abc = create_dictionary_of_info_field_values(result)
info_field_data_type = determine_data_type_of_info_fields(abc)
a = format_data(data, info_field_data_type)


# # Part 10 (No Points)
# Write a function whose inputs are a Python dictionary and filename. The function will saves the dictionary as a json file using the filename given. Use the json library. Use these options to correctly format your JSON -- `sort_keys=True, indent=4, separators=(',', ': ')`. 
# Use this function to save your parsed data as a json file. 
# 
# USE THE FOLLOWING FILENAME TO SAVE YOUR FILE: `lab1.json`

# In[20]:



def save_data_as_json(data, filename):
    # YOUR CODE HERE
    import json
    with open(filename, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4, separators=(',',': '))
#     raise NotImplementedError()


# In[21]:


##mine
filename = 'lab1.json'
save_data_as_json(a,filename)


# # Part 11 (10 points)
# Write a function whose input is a filename for a json file. The function should use the filename to read the JSON file in which you saved your final parsed data. 

# In[22]:


def load_data_from_json(filename):
    # YOUR CODE HERE
    import json
    with open(filename, 'r') as fp:
        data = json.load(fp)
    return data
#     raise NotImplementedError()


# In[23]:


test_save_data = {'key1': ['1', '2', '3'], 'key2':['1.1', '2.2', '3.3'], 'key3': ['1.1', '2', '3.3'], 'key4': ['1.1', '234String', '3.3']}
save_data_as_json(test_save_data, 'test_save.json')
results = load_data_from_json('test_save.json')

assert results == test_save_data


# # Part 12 (30 points)
# Write a function whose inputs are `CHROM`, `REF`, `ALT`, `POS`, and `filename`.  Using these inputs, the function should load a JSON file using the given filename and return a list of variants that match 
# the given CHROM, REF, ALT, and POS. 

# In[24]:


def find_variant(CHROM, REF, ALT, POS, filename):
    # YOUR CODE HERE

    data = load_data_from_json(filename)
    list_variants = []
    for i in data :
        if i['CHROM'] == CHROM  and i['REF'] == REF and i['ALT'] == ALT and i['POS'] == POS :
            list_variants.append(i)
    return list_variants
#     raise NotImplementedError()


# In[34]:


result1 = find_variant("13", "T", "G", 56292303, 'lab1.json')


expected_result1 = [{u'INFO': {u'1000g2015aug_eur': 1.0, u'BaseQRankSum': 1.77, u'Gene.refGene': u'MIR5007,PRR20D', u'cytoBand': u'13q21.1', u'gnomAD_genome_FIN': 0.9951, u'1000g2015aug_amr': 0.9841, u'gnomAD_genome_AFR': 0.8475, u'FS': 0.0, u'gnomAD_genome_NFE': 0.9987, u'MQRankSum': 0.0, u'snp138NonFlagged': u'rs4421887', u'gnomAD_genome_ALL': 0.9546, u'DP': 176, u'ExcessHet': 3.0103, u'gnomAD_genome_OTH': 0.9887, u'MLEAF': 1.0, u'culprit': u'MQ', u'1000g2015aug_afr': 0.8313, u'SOR': 0.257, u'VQSLOD': 22.53, u'MQ': 60.0, u'ClippingRankSum': 0, u'Kaviar_AF': 0.0001153, u'AC': 6, u'Kaviar_AC': 3, u'AF': 1.0, u'Kaviar_AN': 26028, u'Func.refGene': u'intergenic', u'AN': 6, u'CADD13_PHRED': 3.712, u'1000g2015aug_all': 0.952676, u'CADD13_RawScore': 0.109684, u'1000g2015aug_sas': 0.9969, u'GeneDetail.ensGene': u'dist=543620,dist=281031', u'ANNOVAR_DATE': u'2018-04-16', u'Func.ensGene': u'intergenic', u'ReadPosRankSum': -0.338, u'gnomAD_genome_ASJ': 0.9834, u'gnomAD_genome_AMR': 0.9843, u'Eigen': -0.7945, u'avsnp150': u'rs4421887', u'MLEAC': 6, u'gnomAD_genome_EAS': 1.0, u'GeneDetail.refGene': u'dist=543620,dist=1422749', u'QD': 28.95, u'Gene.ensGene': u'ENSG00000264387,ENSG00000228611'}, u'SAMPLE': {u'XG404': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'1,70', u'DP': u'71', u'PL': u'2037,202,0'}, u'XG402': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,62', u'DP': u'62', u'PL': u'1796,185,0'}, u'XG403': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,41', u'DP': u'41', u'PL': u'1218,122,0'}, u'XG303': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,41', u'DP': u'41', u'PL': u'1218,122,0'}, u'XG302': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,62', u'DP': u'62', u'PL': u'1796,185,0'}, u'XG304': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'1,70', u'DP': u'71', u'PL': u'2037,202,0'}, u'XG202': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,62', u'DP': u'62', u'PL': u'1796,185,0'}, u'XG203': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,41', u'DP': u'41', u'PL': u'1218,122,0'}, u'XG204': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'1,70', u'DP': u'71', u'PL': u'2037,202,0'}, u'XG103': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,41', u'DP': u'41', u'PL': u'1218,122,0'}, u'XG102': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'0,62', u'DP': u'62', u'PL': u'1796,185,0'}, u'XG104': {u'GT': u'1/1', u'GQ': u'99', u'AD': u'1,70', u'DP': u'71', u'PL': u'2037,202,0'}}, u'REF': u'T', u'POS': 56292303, u'FILTER': u'PASS', u'QUAL': 5037.69, u'ALT': u'G', u'CHROM': u'13', u'ID': u'rs4421887'}]

#without u before the string
# expected_result = [{'INFO': {'1000g2015aug_eur': 1.0, 'BaseQRankSum': 1.77, 'Gene.refGene': 'MIR5007,PRR20D', 'cytoBand': '13q21.1', 'gnomAD_genome_FIN': 0.9951, '1000g2015aug_amr': 0.9841, 'gnomAD_genome_AFR': 0.8475, 'FS': 0.0, 'gnomAD_genome_NFE': 0.9987, 'MQRankSum': 0.0, 'snp138NonFlagged': 'rs4421887', 'gnomAD_genome_ALL': 0.9546, 'DP': 176, 'ExcessHet': 3.0103, 'gnomAD_genome_OTH': 0.9887, 'MLEAF': 1.0, 'culprit': 'MQ', '1000g2015aug_afr': 0.8313, 'SOR': 0.257, 'VQSLOD': 22.53, 'MQ': 60.0, 'ClippingRankSum': 0, 'Kaviar_AF': 0.0001153, 'AC': 6, 'Kaviar_AC': 3, 'AF': 1.0, 'Kaviar_AN': 26028, 'Func.refGene': 'intergenic', 'AN': 6, 'CADD13_PHRED': 3.712, '1000g2015aug_all': 0.952676, 'CADD13_RawScore': 0.109684, '1000g2015aug_sas': 0.9969, 'GeneDetail.ensGene': 'dist=543620,dist=281031', 'ANNOVAR_DATE': '2018-04-16', 'Func.ensGene': 'intergenic', 'ReadPosRankSum': -0.338, 'gnomAD_genome_ASJ': 0.9834, 'gnomAD_genome_AMR': 0.9843, 'Eigen': -0.7945, 'avsnp150': 'rs4421887', 'MLEAC': 6, 'gnomAD_genome_EAS': 1.0, 'GeneDetail.refGene': 'dist=543620,dist=1422749', 'QD': 28.95, 'Gene.ensGene': 'ENSG00000264387,ENSG00000228611'}, 'SAMPLE': {'XG404': {'GT': '1/1', 'GQ': '99', 'AD': '1,70', 'DP': '71', 'PL': '2037,202,0'}, 'XG402': {'GT': '1/1', 'GQ': '99', 'AD': '0,62', 'DP': '62', 'PL': '1796,185,0'}, 'XG403': {'GT': '1/1', 'GQ': '99', 'AD': '0,41', 'DP': '41', 'PL': '1218,122,0'}, 'XG303': {'GT': '1/1', 'GQ': '99', 'AD': '0,41', 'DP': '41', 'PL': '1218,122,0'}, 'XG302': {'GT': '1/1', 'GQ': '99', 'AD': '0,62', 'DP': '62', 'PL': '1796,185,0'}, 'XG304': {'GT': '1/1', 'GQ': '99', 'AD': '1,70', 'DP': '71', 'PL': '2037,202,0'}, 'XG202': {'GT': '1/1', 'GQ': '99', 'AD': '0,62', 'DP': '62', 'PL': '1796,185,0'}, 'XG203': {'GT': '1/1', 'GQ': '99', 'AD': '0,41', 'DP': '41', 'PL': '1218,122,0'}, 'XG204': {'GT': '1/1', 'GQ': '99', 'AD': '1,70', 'DP': '71', 'PL': '2037,202,0'}, 'XG103': {'GT': '1/1', 'GQ': '99', 'AD': '0,41', 'DP': '41', 'PL': '1218,122,0'}, 'XG102': {'GT': '1/1', 'GQ': '99', 'AD': '0,62', 'DP': '62', 'PL': '1796,185,0'}, 'XG104': {'GT': '1/1', 'GQ': '99', 'AD': '1,70', 'DP': '71', 'PL': '2037,202,0'}}, 'REF': 'T', 'POS': 56292303, 'FILTER': 'PASS', 'QUAL': 5037.69, 'ALT': 'G', 'CHROM': '13', 'ID': 'rs4421887'}]

assert expected_result1==result1


# In[27]:







filename = 'lab1_data.vcf' 
data = read_vcf_file(filename) # read vcf file 
info_field_data = extract_info_field(data) # extract all the info fields
info_field_list = create_dictionary_of_info_field_values(info_field_data) # create dictionary from info fields
info_field_data_type = determine_data_type_of_info_fields(info_field_list) # Determine data type of each info field
data = format_data(data, info_field_data_type) # format the data variable -- from data = read_vcf_file(filename)
save_data_as_json(data, 'lab1.json') # save the formatted data
data_loaded = load_data_from_json('lab1.json') # load saved data 

# Now I will fetch three variants using your find_variant function and check that they match my results


# In[ ]:




