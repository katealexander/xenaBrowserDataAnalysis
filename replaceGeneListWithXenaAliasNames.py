#!/usr/bin/python
# Replaces gene list for list of genes with expression found in Xena
# Note you need aliases.txt to be in your working directory


import sys, os, re
import xenaPython as xena

def main(args):
	if not len(args) == 3: sys.exit("USAGE: python replaceGeneListWithXenaAliasNames.py cancerType[KIRC] geneList.txt > newGeneList.txt")

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
	f.close()

	#if in Xena, print gene. If not in Xena, determine if gene has an alias that is in Xena
	nGenes = len(genes)
	k = xena.dataset_gene_probe_avg(hub, dataset, samples, genes)
	for i in range(0, nGenes):
		if k[i]['position'] == [] or k[i]['scores'][0][0] == 'NaN':
			# determine if gene has an alias in Xena
			alias = findAliasInXena(hub, dataset, samples, k[i]['gene'])
			if alias != '':
				print alias
		else:
			print k[i]['gene']
			
def findAliasInXena(hub, dataset, samples, gene):
	xenaAlias = ''
	f = open("aliases.txt"); line = f.readline()[:-1]
	while line != "":
		aliases = []
		aliases.append(line.split("\t")[1])
		aliases += line.split("\t")[4].split(',')
		aliases += line.split("\t")[5].split(',')
		if gene in aliases:
			k = xena.dataset_gene_probe_avg(hub, dataset, samples, aliases)
			for i in range(0, len(aliases)):
				if k[i]['position'] != [] and k[i]['scores'][0][0] != 'NaN':
					xenaAlias = k[i]['gene']
			break
		line = f.readline()[:-1]
	f.close()
	return xenaAlias

if __name__ == "__main__": main(sys.argv)

