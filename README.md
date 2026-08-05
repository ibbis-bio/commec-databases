# commec-databases (archived)

> ⚠️ **This repository is archived and no longer maintained.**
>
> It distributed the **commec v1.x** biorisk and low-concern (formerly "benign") databases via Git LFS and tagged releases. As of **commec v2.0**, reference databases are no longer distributed from this repository.
>
> **Get the current databases with `commec setup`**, which downloads them from **[databases.commec.io](https://databases.commec.io)**:
> ```bash
> commec setup -d /path/to/databases
> ```
> See the [commec Install guide](https://github.com/ibbis-bio/common-mechanism/wiki/Install) for details.
>
> This repository is preserved, read-only, for reference by users still running commec v1.x.

---

## About this repository (commec v1.x)

The `commec` package is a tool for DNA sequence screening that is part of the
[Common Mechanism for DNA Synthesis screening](https://ibbis.bio/common-mechanism/).

This repository held the Biorisk and Benign (low-concern) database files used by commec v1.x for the biorisk and benign screening steps — the only databases needed to run commec in the truncated `--skip-tx` mode, where the regulated taxonomy steps are skipped. In v1.x these could be downloaded with `commec setup`, or by downloading `commec-dbs.zip` from a tagged release and pointing `commec` at the extracted files with `-d/--databases` or a YAML config.

<details>
<summary>Historical: v1.x database release &amp; update process</summary>

Updating the databases entailed the following steps:
- Ensure git lfs is installed, and pull using `git lfs pull`
- Update the relevant files inside the `commec-dbs` sub-directory within the repo.
- Create a Pull Request for changes into `main`, which triggered unit tests on the database files.
- On a successfully reviewed pull request, merge into `main`.
- Use the `tag and release` GitHub action, supplying the semantic version, to automate the release.

</details>

## About
The Common Mechanism is a project of [IBBIS](https://ibbis.bio), the International Biosecurity and
Biosafety Initiative for Science. From 2021-2023, the software and databases were developed by a
team of technical consultants working with the Nuclear Threat Initiative, led by Dr. Nicole Wheeler
of the University of Birmingham, and including contributions from Brittany Rife Magalis of the
University of Louisville and Jennifer Lu of the Center for Computational Biology at Johns Hopkins
University. In 2024, IBBIS became the home of the project.
