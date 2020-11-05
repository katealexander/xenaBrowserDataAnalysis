#!/usr/bin/python
# make a table of expression from gene list of any cancer type available from Xena browser


import sys, os, re
import xenaPython as xena

def main(args):
	if not len(args) == 3: sys.exit("USAGE: python getExpressionFromXena.py cancerType[KIRC] geneList.txt  > outFile")

	# TCGA hub
	hub = "https://tcga.xenahubs.net"

	# PanCan normalized dataset
	dataset = "TCGA." + str(args[1]) + ".sampleMap/HiSeqV2_PANCAN"

	# get sample IDs
	samples = xena.dataset_samples(hub, dataset, None)

	#read geneList into list
	f = open(args[2]); line = f.readline()[:-1]
	genes = []
	while line != "":
		gene = line
		genes.append(gene)
		line = f.readline()[:-1]

	#print header
	print 'Gene\t' + '\t'.join(samples)

	#print expression
	nGenes = len(genes)
	k = xena.dataset_gene_probe_avg(hub, dataset, samples, genes)
	for i in range(0, nGenes):
		geneName = k[i]['gene']
		scores = k[i]['scores'][0]
		print geneName + '\t' + '\t'.join(str(x) for x in scores)

if __name__ == "__main__": main(sys.argv)

