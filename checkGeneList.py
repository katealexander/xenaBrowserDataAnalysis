#!/usr/bin/python
# checks gene names in Xena; prints names that are not found in Xena


import sys, os, re
import xenaPython as xena

def main(args):
	if not len(args) == 2: sys.exit("USAGE: python checkGeneList.py geneList.txt  > outFile")

	# TCGA hub
	hub = "https://tcga.xenahubs.net"

	# PanCan normalized dataset
	dataset = "TCGA.KIRC.sampleMap/HiSeqV2_PANCAN"

	# get sample IDs
	samples = xena.dataset_samples(hub, dataset, None)

	#read geneList into list
	f = open(args[1]); line = f.readline()[:-1]
	genes = []
	while line != "":
		gene = line
		genes.append(gene)
		line = f.readline()[:-1]

	#print expression
	nGenes = len(genes)
	k = xena.dataset_gene_probe_avg(hub, dataset, samples, genes)
	for i in range(0, nGenes):
		if k[i]['position'] == []:
			print k[i]['gene']

if __name__ == "__main__": main(sys.argv)

