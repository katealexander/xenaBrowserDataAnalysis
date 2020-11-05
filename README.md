# Xena Browser Data Analysis
This repository is a set of python scripts implementing the [xenaPython](https://github.com/ucscXena/xenaPython) library to access and analyze cancer datasets.

### Install xenaPython
```
pip install xenaPython
```
### Upgrade installation
```
pip install --upgrade xenaPython
```

## Determine whether all your genes of interest are found in the dataset
If any genes in your gene list of interest are not found in Xena browser, they will be printed in the following script. You can then check if they may have alternative names.
```
python checkGeneList.py geneList.txt
```

## Get expression data from TCGA PANCAN studies for a list of genes
The following returns a table of the PANCAN normalized expression for any cancer study of interest. Rows are genes, columns are patients.
```
python getExpressionFromXena.py KIRC testGeneList.txt > outfile.txt
```
Replace KIRC with [any cancer type from TCGA PANCAN study that is in Xena browser](https://xenabrowser.net/datapages/). Replace testGeneList.txt with a list of your genes of interest.
