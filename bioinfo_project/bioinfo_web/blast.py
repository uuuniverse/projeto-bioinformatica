# -*- coding: utf-8 -*-
"""Blast.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZzIa5aiq_XVv31UZzE07hzn8KhEHk-9I
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# https://ftp.ncbi.nlm.nih.gov/refseq/release/viral/ -->Apenas Viral
# https://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/-->Banco Todo
try:

    from Bio.Blast import NCBIXML
    from Bio.Blast import NCBIWWW
    from Bio import SeqIO
except:
    from Bio.Blast import NCBIXML
    from Bio.Blast import NCBIWWW
    from Bio import SeqIO
import time
import os
import platform
START_TIME = 0.0


def tempo():
    global START_TIME
    return [print(time.strftime(
        "%H:%M:%S", time.gmtime(time.time() - START_TIME)))]


def run_blast():

    global START_TIME
    START_TIME = time.time()
    print("Abrindo o Arquivo para analise")
    print("Buscando no Banco Online")
    print("Blast:")
    tempo()
    print("Blast:")
    print("***********")
    path = os.getcwd()
    so = platform.system()

    if so == "Windows":
        path_blast = path + \
            "/bioinfo_web/ncbi-blast-2.9.0+-x64-win64/ncbi-blast-2.9.0+/bin/ "
    elif so == "Linux":
        path_blast = path + "/bioinfo_web/ncbi-blast-2.9.0+/bin"

    myfile = path + "/bioinfo_web/myfile.fasta"
    bd = path + "/bioinfo_web/bd/viral_db"
    out_blast = path + "/bioinfo_web/blast_result"
    os.chdir(path_blast)
    os.system(
        f"blastn -query {myfile} -db {bd} -outfmt 5 -out {out_blast}")
    os.chdir(path)
    res_on = open("bioinfo_web/blast_result")

    resultado = analise(res_on)
    return resultado


def analise(res):
    print("Abrindo o resultado para analise")
    alinhamentos = []
    dados = NCBIXML.parse(res)
    item = next(dados)
    print("Iniciando Analise")
    i = 1
    for a in item.alignments:
        for hsp in a.hsps:
            alinhamentos.append({'alinhamento': i,
                                 'sequencia': a.title,
                                 'tamanho': a.length,
                                 'score': hsp.score,
                                 'identidade': hsp.identities/100
                                 })
            i += 1
    print("***********")
    print("Analise")
    tempo()
    print("Analise")
    return alinhamentos
