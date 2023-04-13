# -*- coding: utf-8 -*-
"""
Paths to main resources and resource management.

Due to the size limits of git and pypi the large resources
cannot be managed/included in git and pypi.
These resources have to be loaded from online resources on
first import.

The source data structure:
---+ BRENDAPY_DATA_DIR
   |---+ brenda/
   |   |--- brenda_download.txt
   |---+ ncbi/
   |   |---+ taxdump/
   |   |--- ...(unzipped *.dmp files) ...
   |---+ bto
   |   |--- bto.owl
   |---+ chebi
   |   |--- chebi.obo

"""
import os


BASE_PATH = os.path.dirname(os.path.realpath(__file__))
BRENDAPY_DATA_DIR = os.getenv("BRENDAPY_DATA_DIR")
if not BRENDAPY_DATA_DIR:
    raise Exception("Environment variable BRENDAPY_DATA_DIR is not set")

BRENDA_FILE = os.path.join(BRENDAPY_DATA_DIR, "brenda", "brenda_download.txt")
TAXONOMY_DIR = os.path.join(BRENDAPY_DATA_DIR, "ncbi", "taxdump")
TAXONOMY_DATA = os.path.join(TAXONOMY_DIR, "taxonomy.json")
BTO_DATA = os.path.join(BRENDAPY_DATA_DIR, "bto", "bto.owl")
CHEBI_OBO_DATA = os.path.join(BRENDAPY_DATA_DIR, "chebi", "chebi.obo")
CHEBI_JSON_DATA = os.path.join(BRENDAPY_DATA_DIR, "chebi", "chebi.json")
