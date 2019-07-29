import pytest
import os
from brendapy import parser

base_path = os.path.dirname(os.path.realpath(__file__))
brenda_file = os.path.join(base_path, "..", "..", 'data', 'brenda_download.txt')


def test_parsing():
	brenda = parser.BRENDAparser(brenda_file)
	assert brenda
	assert "1.1.1.1" in brenda.ec_text


def test_protein():
	""" Test the proteinBRENDA module """
	brenda = parser.BRENDAparser(brenda_file)

	ec = "1.1.1.1"
	proteins = brenda.parse_proteins(ec)
	assert proteins
	assert len(proteins) == 167


def test_protein_detail1():
	brenda = parser.BRENDAparser(brenda_file)
	ec = "1.1.1.1"
	ec_str = brenda.ec_text[ec]
	protein = parser.BRENDAProtein(ec=ec, id=1, ec_string=ec_str)
	assert protein
	assert 'liver' in protein.source_tissue
	assert protein.organism == "Gallus gallus"

	print(protein)
	assert 44 in protein.references
	assert len(protein.pubmed) == 1


def test_protein_detail2():
	brenda = parser.BRENDAparser(brenda_file)
	ec = "1.1.1.1"
	ec_str = brenda.ec_text[ec]
	protein = parser.BRENDAProtein(ec=ec, id=4, ec_string=ec_str)
	assert protein
	print(protein)
	assert 'liver' in protein.source_tissue
	assert protein.organism == "Drosophila melanogaster"

	assert 8 in protein.references
	assert len(protein.pubmed) == 7


def test_all_proteins():
	brenda = parser.BRENDAparser(brenda_file)
	for ec in brenda.keys():
		print(ec)
		proteins = brenda.parse_proteins(ec)
