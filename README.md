# Xena Browser Data Analysis
This repository is a set of python scripts implementing the [xenaPython](https://github.com/ucscXena/xenaPython) library to access cancer datasets.

### Install xenaPython
'''
pip install xenaPython
'''
### Upgrade installation
'''
pip install --upgrade xenaPython
'''

## Determine whether all your genes of interest are found in the dataset
If any genes in your gene list of interest are not found in Xena browser, they will be printed in the following script. You can then check if they may have alternative names.
'''
python checkGeneList.py geneList.txt
'''
