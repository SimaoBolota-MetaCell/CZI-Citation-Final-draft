from citation_scraper.bibtexCitation import *
from citation_scraper.apaCitation import *
from citation_scraper.bibtex_from_doi import *
from create_dict import *

DOI_README_LINK = 'https://github.com/SimaoBolota-MetaCell/Citation-Project/blob/main/onlyDOI.md'
APA_README_LINK = 'https://github.com/SimaoBolota-MetaCell/Citation-Project/blob/main/APA.md'
BIBTEX_README_LINK = 'https://github.com/SimaoBolota-MetaCell/Citation-Project/blob/main/bibtextandAPA.md'
NOTHING_README_LINK = 'https://github.com/SimaoBolota-MetaCell/Citation-Project/blob/main/emptyreadme.md'


citation_title = {}
citation_publisher = {}
citation_url = {}
citation_family_names = {}
citation_given_names = {}
citation_year = {}
citation_journal = {}
citation_doi = {}

def test_bibtex_method():
	all_bibtex_citations = get_bibtex_citations(BIBTEX_README_LINK)
	for individual_citation in all_bibtex_citations:
		individual_citation = re.sub('"', '}', individual_citation)
		individual_citation = re.sub('= }', '= {', individual_citation)
		citation_family_names = get_bibtex_family_names(individual_citation)
		citation_given_names = get_bibtex_given_names(individual_citation)
		citation_title = get_bibtex_title(individual_citation)
		citation_year = get_bibtex_year(individual_citation)
		citation_publisher = get_bibtex_publisher(individual_citation)
		citation_journal = get_bibtex_journal(individual_citation)
		citation_url = get_bibtex_url(individual_citation)
		citation_doi = get_bibtex_doi(individual_citation)

	bib_filedict = add_to_dict(citation_family_names, citation_given_names, citation_title, citation_year, citation_url, citation_doi, citation_publisher, citation_journal )
	
	
	assert bool(get_bibtex_citations(BIBTEX_README_LINK)) == True
	assert bool(get_bibtex_citations(APA_README_LINK)) == False
	assert bool(get_bibtex_citations(DOI_README_LINK)) == False


	assert citation_family_names == ['Conrad', 'Narayan']
	assert citation_given_names == ['Ryan', 'Kedar']
	assert citation_title == '{Instance segmentation of mitochondria in electron microscopy images with a generalist deep learning model'
	assert citation_year == '2022'
	assert citation_publisher == 'Cold Spring Harbor Laboratory'
	assert bool(citation_journal) == False
	assert citation_url == ['https://www.biorxiv.org/content/early/2022/03/18/2022.03.17.484806']
	assert citation_doi == '10.1101/2022.03.17.484806'

	assert bib_filedict == {'cff-version': '1.2.0', 'message': 'If you use this plugin, please cite it using these metadata', 'title': '{Instance segmentation of mitochondria in electron microscopy images with a generalist deep learning model', 'authors': [{'family-names': 'Conrad', 'given-names': 'Ryan'}, {'family-names': 'Narayan', 'given-names': 'Kedar'}], 'date-released': '2022-01-01', 'url': 'https://www.biorxiv.org/content/early/2022/03/18/2022.03.17.484806', 'references': [{'type': 'book', 'publisher': 'Cold Spring Harbor Laboratory', 'doi': '10.1101/2022.03.17.484806'}, {'type': 'article', 'title': '{Instance segmentation of mitochondria in electron microscopy images with a generalist deep learning model', 'journal': 'bioRxiv', 'doi': '10.1101/2022.03.17.484806'}]}


	
	
	
	
def test_apa_method():
	APA_text_var, all_apa_authors_var, all_apa_citations_var = get_apa_citations(APA_README_LINK)
	APA_text_var_doi, all_apa_authors_var_doi, all_apa_citations_var_doi = get_apa_citations(DOI_README_LINK)

	for individual_citation in all_apa_citations_var:
		individual_citation = ''.join(map(str, individual_citation))
		individual_citation = re.sub('\(', '', individual_citation)
		individual_citation = all_apa_authors_var + ' ' + individual_citation
		citation_family_names = get_apa_family_names(all_apa_authors_var)
		citation_given_names = get_apa_given_names(all_apa_authors_var)
		citation_year = get_apa_year(individual_citation)
		citation_year = citation_year + '-01-01'
		citation_title = get_apa_title(individual_citation)
		citation_journal = get_apa_journal(citation_title, APA_text_var)
		citation_doi = get_apa_doi(APA_text_var)
	

	assert bool(all_apa_authors_var) == True
	assert bool(all_apa_authors_var_doi) == False

	assert citation_family_names == ['Tyson', 'Fort', 'Rousseau', 'Cossell', 'Tsitoura', 'Lenzi', 'Obenhaus', 'Claudi', 'Branco', 'Margrie']
	assert citation_given_names == ['A.', 'M.', 'C.', 'L.', 'C.', 'S.', 'H.', 'F.', 'T.', 'T.']
	assert citation_title == 'Accurate determination of marker location within whole-brain microscopy images'
	assert citation_year == '2022-01-01'
	assert citation_journal == [' Scientific Reports, 12, 867 ']
	assert citation_doi == ['10.1038/s41598-021-04676-9']

	apa_filedict = add_to_dict(citation_family_names, citation_given_names, citation_title, citation_year, citation_url, citation_doi, citation_publisher, citation_journal )

	assert apa_filedict == {'cff-version': '1.2.0', 'message': 'If you use this plugin, please cite it using these metadata', 'title': 'Accurate determination of marker location within whole-brain microscopy images', 'doi': '10.1038/s41598-021-04676-9', 'authors': [{'family-names': 'Tyson', 'given-names': 'A.'}, {'family-names': 'Fort', 'given-names': 'M.'}, {'family-names': 'Rousseau', 'given-names': 'C.'}, {'family-names': 'Cossell', 'given-names': 'L.'}, {'family-names': 'Tsitoura', 'given-names': 'C.'}, {'family-names': 'Lenzi', 'given-names': 'S.'}, {'family-names': 'Obenhaus', 'given-names': 'H.'}, {'family-names': 'Claudi', 'given-names': 'F.'}, {'family-names': 'Branco', 'given-names': 'T.'}, {'family-names': 'Margrie', 'given-names': 'T.'}], 'date-released': '2022-01-01-01-01', 'url': ['Not Available'], 'references': [{'type': 'article', 'title': 'Accurate determination of marker location within whole-brain microscopy images', 'journal': ' Scientific Reports, 12, 867 ', 'doi': '10.1038/s41598-021-04676-9'}]}




def test_doi_method():
	all_bibtex_citations = get_citation_from_doi(DOI_README_LINK)
	for individual_citation in all_bibtex_citations:
		individual_citation = re.sub('"', '}', individual_citation)
		individual_citation = re.sub('= }', '= {', individual_citation)
		citation_family_names = get_bibtex_family_names(individual_citation)
		citation_given_names = get_bibtex_given_names(individual_citation)
		citation_title = get_bibtex_title(individual_citation)
		citation_year = get_bibtex_year(individual_citation)
		citation_publisher = get_bibtex_publisher(individual_citation)
		citation_journal = get_bibtex_journal(individual_citation)
		citation_url = get_bibtex_url(individual_citation)
		citation_doi = get_bibtex_doi(individual_citation)

	filedict = add_to_dict(citation_family_names, citation_given_names, citation_title, citation_year, citation_url, citation_doi, citation_publisher, citation_journal )

	assert bool(get_citation_from_doi(DOI_README_LINK)) == True
	assert bool(get_citation_from_doi(BIBTEX_README_LINK)) == False
	assert bool(get_citation_from_doi(APA_README_LINK)) == True

	assert bool(citation_family_names) == False
	assert bool(citation_given_names) == False
	assert citation_title == ''
	assert citation_year == '2022'
	assert citation_publisher == 'Springer Science and Business Media '
	assert bool(citation_journal) == False
	assert citation_url == ['https://doi.org/10.1038%2Fs41598-021-04676-9']
	assert citation_doi == '10.1038/s41598-021-04676-9'

	assert filedict == {'cff-version': '1.2.0', 'message': 'If you use this plugin, please cite it using these metadata', 'title': ['Not Available'], 'doi': '10.1038/s41598-021-04676-9', 'authors': [{'family-names': 'Not Available', 'given-names': 'Not Available'}], 'date-released': '2022-01-01', 'url': 'https://doi.org/10.1038%2Fs41598-021-04676-9', 'references': [{'type': 'book', 'title': 'Not Available', 'publisher': 'Springer Science and Business Media ', 'doi': '10.1038/s41598-021-04676-9'}]}
