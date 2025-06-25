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

This repository contains the Biorisk and Benign database files necessary for steps 1 and 4. These are the only databases necessary when running Commec in the truncated `--skip-tx` mode where regulated taxonomy steps are skipped.

These files can be downloaded to a desired location using the `commec setup` command line interface. Alternatively, downloading commec-dbs.zip from the a tagged release, and placing the extracted files in a location to be pointed to with the `-d, --databases` commec cli. Or ensure that the yaml parameters file points to the biorisk and benign directories respectively.

Database Release and Update
===========================
Updating the databases will entail the following steps:
- Ensure git lfs is installed, and pull using `git lfs pull`
- Update the relevant files inside the commec-dbs sub-directory within the repo.
- Create a Pull Request for changes into main, this will trigger unit tests on the database files.
- On a successfully merged pull request, merge into main.
- Use the `tag and release` github action, supply the semantic version, which will automate the release.

About
=====
The Common Mechanism is a project of [IBBIS](https://ibbis.bio), the International Biosecurity and
Biosafety Initiative for Science. From 2021-2023, the software and databases were developed by a
team of technical consultants working with the Nuclear Threat Initiative, led by Dr. Nicole Wheeler
of the University of Birmingham, and including contributions from Brittany Rife Magalis of the
University of Louisville and Jennifer Lu of the Center for Computational Biology at Johns Hopkins
University. In 2024, IBBIS became the home of the project.
