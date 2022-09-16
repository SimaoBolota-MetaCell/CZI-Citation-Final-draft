
import urllib.request
from citation_scraper.htmlScraper import *
import re
import requests
from patterns import *

def get_bibtext(doi, cache={}):
    """Use DOI Content Negotioation (http://crosscite.org/cn/) to retrieve a string
    with the bibtex entry.
    Created using software by Daniel Himmelstein

    Parameters
    ----------
    doi : str
        holds the DOI of the article/book cited in the README.md

    Returns
    -------
    bibtex : str
        bibtex entry of the DOI
   
    """
   
    if doi in cache:
        return cache[doi]
    url = 'https://doi.org/' + urllib.request.quote(doi)
    header = {
        'Accept': 'application/x-bibtex',
    }
    response = requests.get(url, headers=header)
    bibtext = response.text
    if bibtext:
        cache[doi] = bibtext
    return bibtext


def get_citation_from_doi(link):
    """Gathers DOI from the README.md, transforming it into
    a BibTex format citation using DOI Content Negotioation

    Parameters
    ----------
    link : str
        url from where you want to check for citations

    Returns
    -------
    all_bibtex_citations : list
        holds the valid citation information from the BibTex formatted text
        
    """
    
    soup = get_html(link )
    paragraphs = soup.find_all("p", {'dir': 'auto'})
    paragraphs = str(paragraphs)

    lists = soup.find_all("li")
    lists = str(lists)

    p_text_w_citation = re.findall(FULL_DOI_PATERN, paragraphs, flags=re.DOTALL)
    l_text_w_citation = re.findall(FULL_DOI_PATERN, lists, flags=re.DOTALL)

    if(bool(p_text_w_citation)):
            paragraphs = strip_tags(paragraphs)
            citation_doi = re.findall(DOI_IN_HTML_PATTERN, paragraphs, flags=re.DOTALL)
            citation_doi = ''.join(map(str, citation_doi))
            bibtext_text = get_bibtext(citation_doi)
            

    elif(bool(l_text_w_citation)):
            lists = strip_tags(lists)
            citation_doi = re.findall(DOI_IN_HTML_PATTERN, lists, flags=re.DOTALL)
            citation_doi = ''.join(map(str, citation_doi))
            bibtext_text = get_bibtext(citation_doi)

    else:
        bibtext_text = False
    
    if(bool(bibtext_text)):
        print(bibtext_text)
        bibtext_text = re.sub('}},', '},', bibtext_text)
        all_bibtex_citations = re.findall(BIBTEX_PATTERN, bibtext_text, flags=re.DOTALL)
        
        return all_bibtex_citations




