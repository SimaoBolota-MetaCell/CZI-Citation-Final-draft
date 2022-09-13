"""
Created using software by Daniel Himmelstein and released under CC0 1.0. 
"""

import urllib.request
from htmlScraper import *
import re
import requests
from patterns import *


def shorten(doi, cache={}, verbose=False):
    """
    Get the shortDOI for a DOI. Providing a cache dictionary will prevent
    multiple API requests for the same DOI.
    """
    if doi in cache:
        return cache[doi]
    quoted_doi = urllib.request.quote(doi)
    url = 'http://shortdoi.org/{}?format=json'.format(quoted_doi)
    try:
        response = requests.get(url).json()
        short_doi = response['ShortDOI']
    except Exception as e:
        if verbose:
            print(doi, 'failed with', e)
        return None
    cache[doi] = short_doi
    return short_doi


def get_bibtext(doi, cache={}):
    """
    Use DOI Content Negotioation (http://crosscite.org/cn/) to retrieve a string
    with the bibtex entry.
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
        all_bibtex_citations = re.findall(BIBTEX_PATTERN, bibtext_text, flags=re.DOTALL)
        return all_bibtex_citations




print(get_citation_from_doi('https://github.com/SimaoBolota-MetaCell/Citation-Project/blob/main/README.md'))