# commec: a free, open-source, globally available tool for DNA sequence screening

The `commec` package is a tool for DNA sequence screening that is part of the
[Common Mechanism for DNA Synthesis screening](https://ibbis.bio/common-mechanism/).

![Common Mechanism banner](https://ibbis.bio/wp-content/uploads/2024/05/commec-v0.1.0-banner.png)

Introduction : Common Mechanism Databases
============
The Common Mechanism offers DNA sequence screening:
The `screen` command runs an input FASTA through four steps:

  1. Biorisk scan (uses a hmmer search against custom databases)
  2. Regulated protein scan (uses a BLASTX or DIAMOND search against NCBI nr)
  3. Regulated nucleotide scan (uses BLASTN against NCBI nt)
  4. Benign scan (users hmmer, cmscan and BLASTN against custom databases)

This repository contains the Biorisk and Benign database files necessary for steps 1 and 4. These are the only databases necessary when running Commec in the truncated `--fast-mode`.

Simply copy the contents of the commec-dbs folder within this repository to the desired location and use the -databases cli to point to that fold, or ensure that the yaml parameters file points to the biorisk and benign directorys respectively.

Documentation
=============
The online documentation is located at the
[GitHub Wiki](https://github.com/ibbis-screening/common-mechanism/wiki).

Development
=======
Development dependencies are managed through a conda environment. Install conda, then make sure
that [your channels are configured correctly](http://bioconda.github.io/).

```
conda env create -f environment.yml
conda activate commec-dev
```

From here, you should have an interactive version of the package installed via (`pip -e .`) as well
as the necessary shell dependencies.

About
=====
The Common Mechanism is a project of [IBBIS](https://ibbis.bio), the International Biosecurity and
Biosafety Initiative for Science. From 2021-2023, the software and databases were developed by a
team of technical consultants working with the Nuclear Threat Initiative, led by Dr. Nicole Wheeler
of the University of Birmingham, and including contributions from Brittany Rife Magalis of the
University of Louisville and Jennifer Lu of the Center for Computational Biology at Johns Hopkins
University. In 2024, IBBIS became the home of the project