# Xena Browser Data Analysis
This repository is a set of python scripts written in Python 2.7 that implement the [xenaPython](https://github.com/ucscXena/xenaPython) library to access and analyze cancer datasets.

### Install xenaPython
```
pip install xenaPython
```
### Upgrade installation
```
pip install --upgrade xenaPython
```

## Get expression data from TCGA PANCAN studies for a list of genes

#### Determine whether all your genes of interest are found in the dataset
If any genes in your gene list of interest are not found in Xena browser, they will be printed in the following script. You can then check if they may have alternative names.
```
python checkGeneList.py geneList.txt
```
There are two types of genes here: those that are not found (and maybe have other gene names) and those that have undetectable expression (NaN gene expression scores).

#### Replace your gene list with a list of genes that have expression found in Xena browser
From above, if there are a number of genes without expression data, you can generate a new gene list file that either finds their gene alias that is in Xena browser, or excludes the gene if an alias with Xena browser expression cannot be found. Note that some of the genes will be excluded just because they are not detected in the dataset, so the same gene list may have different genes excluded depending on the cancer type.
```
python replaceGeneListWithXenaAliasNames.py KIRC testGeneList.txt > xenaAliasGeneList.txt
```
This script will exclude all genes with undetectable expression and try to find aliases for genes where the names are different in Xena browser.

#### Get expression data from gene list
The following returns a table of the PANCAN normalized expression for any cancer study of interest. Rows are genes, columns are patients.
```
python getExpressionFromXena.py KIRC testGeneList.txt > outfile.txt
```
Replace KIRC with [any cancer type from TCGA PANCAN study that is in Xena browser](https://xenabrowser.net/datapages/). Replace testGeneList.txt with a list of your genes of interest.
