# REF: https://www.sqlitetutorial.net/sqlite-python/
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_student(conn, values):

    sql = ''' INSERT INTO students(last_name,first_name,username,exam1,exam2,exam3)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, values)
    return cur.lastrowid


def select_all_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    return rows


import os, pprint


db_file = 'student_test.db'
if os.path.exists(db_file):
    os.remove(db_file)

create_table_sql = """CREATE TABLE students (last_name TEXT, first_name TEXT, username TEXT, exam1 REAL, exam2 REAL, exam3 REAL);"""

conn = create_connection(db_file)

with conn:
    # create
    create_table(conn, create_table_sql)

    # insert
    for student in open('students.tsv', 'r'):
        values = student.strip().split('\t')
        rid = insert_student(conn, values)

    # select
    rows = select_all_students(conn)

# calculate average of all students
from statistics import mean
student_grades = []
for student in rows:
    username, last_name, first_name, e1, e2, e3 = student
    student_grades.append((username, last_name, first_name, round(mean((e1, e2, e3)),2)))



sorted_grades = sorted(student_grades, key=lambda x: x[-1], reverse=True)
pprint.pprint(sorted_grades)

# ####
rows = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
#####


    with gzip.open(filename,'rt') as fp :
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
    index = [header[0].split("\t").index(i) for i in header[0].split("\t") if i == 'INFO'][0]
    predictor_dict = {}
    key_list = []
    for j in line :
        llist = j.split("\t")
        info_list = llist[index].split(";")
        for k in info_list:
            if '=' in k :
                int_list = []
                k_v_list = k.split("=")
                if k_v_list[0] in keys_save_value :
                    if k_v_list[0] not in key_list:
                        key_list.append(k_v_list[0])
                        if k_v_list[1] != '.':
                            int_list.append(k_v_list[1])
                        predictor_dict.update({k_v_list[0]:int_list})
                    else :
                        if k_v_list[1] != '.' and k_v_list[1] not in predictor_dict[k_v_list[0]]:
                            predictor_dict[k_v_list[0]].append(k_v_list[1])
    return predictor_dict
    
    conn = create_connection(db_file, delete_db=True)
    with conn :
        for i in predictor_values.keys() : 
            if '-' in i :
                i = i.replace('-','_')
            create_table_sql = 'CREATE TABLE ' + i +' ('+ i +'ID INTEGER NOT NULL PRIMARY KEY, ' + 'prediction text NOT NULL);'
            create_table(conn, create_table_sql)


Variants.CHROM,Variants.POS,Variants.ID,Variants.REF,Variants.ALT,Variants.QUAL,Variants.FILTER,
Variants.thousandg2015aug_all,Variants.ExAC_ALL,FATHMM_pred.prediction,LRT_pred.prediction,
MetaLR_pred.prediction,MetaSVM_pred.prediction,MutationAssessor_pred.prediction,
MutationTaster_pred.prediction,PROVEAN_pred.prediction,Polyphen2_HDIV_pred.prediction,
Polyphen2_HVAR_pred.prediction,SIFT_pred.prediction,fathmm_MKL_coding_pred.prediction,
sum(PredictionStats.PredictorValue)


        cur.execute('Variants.CHROM,Variants.POS,Variants.ID,Variants.REF,Variants.ALT,Variants.QUAL,Variants.FILTER,Variants.thousandg2015aug_all,Variants.ExAC_ALL,FATHMM_pred.prediction,LRT_pred.prediction,MetaLR_pred.prediction,MetaSVM_pred.prediction,MutationAssessor_pred.prediction,MutationTaster_pred.prediction,PROVEAN_pred.prediction,Polyphen2_HDIV_pred.prediction,Polyphen2_HVAR_pred.prediction,SIFT_pred.prediction,fathmm_MKL_coding_pred.prediction,sum(PredictionStats.PredictorValue) FROM Variants INNER JOIN FATHMM_pred USING(FATHMM_predID) JOIN LRT_pred USING(LRT_predID) JOIN MetaLR_pred USING(MetaLR_predID) JOIN MetaSVM_pred USING(MetaSVM_predID)    JOIN MutationAssessor_pred USING(MutationAssessor_predID) JOIN MutationTaster_pred USING(MutationTaster_predID)        JOIN PROVEAN_pred USING(PROVEAN_predID) JOIN Polyphen2_HDIV_pred USING(Polyphen2_HDIV_predID) JOIN Polyphen2_HVAR_pred USING(Polyphen2_HVAR_predID) JOIN SIFT_pred USING(SIFT_predID) JOIN fathmm_MKL_coding_pred USING(fathmm_MKL_coding_predID) JOIN PredictionStats USING(VariantID) WHERE Variants.CHROM = {CHROM} and Variants.POS ={POS} and Variants.ID ={ID} and Variants.REF ={REF} and Variants.ALT ={ALT} GROUP BY PredictionStats.VariantID;'.format(CHROM = CHROM, POS=POS, ID=ID, REF=REF, ALT=ALT))