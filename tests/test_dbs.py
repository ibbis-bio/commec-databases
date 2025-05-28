"""
This test ensures that the databases are functional and have been created correctly.
It runs a mock search for each database using the relevant Commec toolset.
Passing this test is a requirement to update the databases for download.
"""

import os
import pytest

from commec.tools.blastn import BlastNHandler
from commec.tools.hmmer import HmmerHandler
from commec.tools.cmscan import CmscanHandler

DATABASE_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "commec-dbs")
TEST_DIRECTORY = os.path.dirname(__file__)

databases_to_test = [
    [BlastNHandler, "benign_db", "benign.fasta"],
    [HmmerHandler, "biorisk_db", "biorisk.hmm"],
    [HmmerHandler, "benign_db", "benign.hmm"],
    [CmscanHandler, "benign_db", "benign.cm"],
]

@pytest.mark.parametrize("input_database", databases_to_test)
def test_databases_can_run(input_database, tmp_path):
    """
    For each database entry, create a screener object,
    run it on the test FASTA file, and verify that:
    - The search runs without error
    - Output file is generated
    - Version information is accessible
    """
    handler_class, db_subdir, db_file = input_database
    db_path = os.path.join(DATABASE_DIRECTORY, db_subdir, db_file)

    # Create mock FASTA file
    fasta_file = tmp_path / "single_record.fasta"
    fasta_file.write_text(">mock_sequence\nATGCGTACTGATCGTACGATCGATCGTACGTAGCTAG\n")

    # Write results into a temp output file in a tmp directory
    output_file = tmp_path / "db.out"

    screener = handler_class(db_path, fasta_file, str(output_file), force=True)
    try:
        screener.search()
    except RuntimeError:
        with open(output_file + ".log.tmp",'r', encoding = 'utf-8') as f:
            output_text = str(f.read())
            assert False, "Failed to run subprocess: Temporary log output: " + output_text


    with open(output_file,'r', encoding = 'utf-8') as f:
        output_text = str(f.read())

    assert output_text, "The output file text failed to generate."
    assert screener.check_output(), "No file was created for tool search."
    assert screener.get_version_information(), "get_version_information() returned empty/None"
