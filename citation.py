from citation_scraper.bibtexCitation import *
from citation_scraper.apaCitation import *
from citation_scraper.bibtex_from_doi import *
from create_dict import *
from git_pr_logic.pull_request import *
import yaml
import git
import json
import requests
import warnings
from patterns import *
import sys
from ruamel.yaml import *
from tkinter import *
from tkinter import messagebox
from citation_scraper.githubInfo import *
from git_pr_logic.git_interaction import *
import os

"""
    ----------
   The main code works as the following:
   - first checks for BibTex citations in the GitHub Repo's README.md page
   - then checks for APA citations in the GitHub Repo's README.md page
   - If none of the first was found, checks for a DOI in the GitHub Repo's README.md,
   and using a DOI scraper produces a BibTex citation which is converted to the CFF formatting
   - In the case that no citation was found in the README.md page, a warning
   is issued


   CITATION.CFF format:

    ----------

"""

repo_path = os.path.dirname(__file__)
#setting branch name fromnwhich the citation will be pushed
branch_name = 'citation_branch'

# get the current GitHub Repository info
git_repo_name, git_author_family_name, git_author_given_name, git_repo_link = getGitInfo(repo_path)
# get the current GitHub Repository README.md link, in which the search for citation will happen
README_LINK = git_repo_link + '/blob/main/README.md'

#creating the branch where the CITATION.CFF will be pushed from
# git_branch( repo_path, branch_name)
#getting the GitHub authorization token as input, to be used for the PR
# git_token = input("Enter the authentication git token: ")

#Initializing the citation fields
citation_title = {}
citation_publisher = {}
citation_url = {}
citation_family_names = {}
citation_given_names = {}
citation_year = {}
citation_journal = {}
citation_doi = {}


#first check if there's any BibTex citation information in the README.md
if (bool(get_bibtex_citations(README_LINK))):
    print('BibTex Citation')
    all_bibtex_citations = get_bibtex_citations(README_LINK)

    for individual_citation in all_bibtex_citations:
        #data transformations needed to ensure the correct formatting outcome
        individual_citation = re.sub('"', '}', individual_citation)
        individual_citation = re.sub('= }', '= {', individual_citation)
        individual_citation = individual_citation + '}'
        #collecting all citation fields from the BibTex READ.ME citation
        citation_family_names = get_bibtex_family_names(individual_citation)
        citation_given_names = get_bibtex_given_names(individual_citation)
        citation_title = get_bibtex_title(individual_citation)
        citation_year = get_bibtex_year(individual_citation)
        citation_publisher = get_bibtex_publisher(individual_citation)
        citation_journal = get_bibtex_journal(individual_citation)
        citation_url = get_bibtex_url(individual_citation)
        citation_doi = get_bibtex_doi(individual_citation)

        # # print(individual_citation)
        # print(citation_family_names)
        # print(citation_given_names)
        # print(citation_title)
        # print(citation_year)
        # print(citation_publisher)
        # print(citation_journal)
        # print(citation_url)
        # print(citation_doi)


    #creating the dict that serves as a template for the CITATION.CFF
    filedict = add_to_dict(
            git_repo_name, 
            git_author_family_name, 
            git_author_given_name, 
            git_repo_link,
            citation_family_names, 
            citation_given_names, 
            citation_title, 
            citation_year, 
            citation_url, 
            citation_doi, 
            citation_publisher, 
            citation_journal )

    print('\n')
    print(filedict)
    print('\n')
    #dump the dict contents into the final YAML file CITATION.CFF
    with open(r'{}/CITATION.cff'.format(repo_path), 'w') as file:
            documents = yaml.dump(filedict, file, sort_keys=False)



#then check if there's any APA citation information in the README.md
elif bool(get_bibtex_citations(README_LINK))==False and bool(get_apa_citations(README_LINK)):
    
    
    APA_text, all_apa_authors, all_apa_citations = get_apa_citations(
        README_LINK)
    
    if (bool(all_apa_citations)):
        print('APA Citation')
        APA_text, all_apa_authors, all_apa_citations = get_apa_citations(
            README_LINK)

        for individual_citation in all_apa_citations:
            #data transformations needed to ensure the correct formatting outcome
            individual_citation = ''.join(map(str, individual_citation))
            individual_citation = all_apa_authors + ' ' + individual_citation
            #collecting all citation fields from the APA READ.ME citation
            citation_family_names = get_apa_family_names(all_apa_authors)
            citation_given_names = get_apa_given_names(all_apa_authors)
            citation_year = get_apa_year(individual_citation)
            citation_year = citation_year
            citation_title = get_apa_title(individual_citation)
            citation_journal = get_apa_journal(citation_title, APA_text)
            citation_doi = get_apa_doi(APA_text)

        #creating the dict that serves as a template for the CITATION.CFF
        filedict = add_to_dict(
            git_repo_name, 
            git_author_family_name, 
            git_author_given_name, 
            git_repo_link,
            citation_family_names, 
            citation_given_names, 
            citation_title, 
            citation_year, 
            citation_url, 
            citation_doi, 
            citation_publisher, 
            citation_journal )

        print('\n')
        print(filedict)
        print('\n')
        #dump the dict contents into the final YAML file CITATION.CFF
        with open(r'{}/CITATION.cff'.format(repo_path), 'w') as file:
                documents = yaml.dump(filedict, file, sort_keys=False)

    # when no citation information is found, check for an APA formatted DOI
    else:
        print('DOI Citation')
        #using a DOI scraper, get a BibTex citation from the DOI found
        all_bibtex_citations = get_citation_from_doi(README_LINK)
        for individual_citation in all_bibtex_citations:
            #data transformations needed to ensure the correct formatting outcome
            individual_citation = re.sub('"', '}', individual_citation)
            individual_citation = re.sub('= }', '= {', individual_citation)
            individual_citation = individual_citation + '}}'
            #collecting all citation fields from the BibTex READ.ME citation
            citation_family_names = get_bibtex_family_names(individual_citation)
            citation_given_names = get_bibtex_given_names(individual_citation)
            citation_title = get_bibtex_title(individual_citation)
            citation_year = get_bibtex_year(individual_citation)
            citation_publisher = get_bibtex_publisher(individual_citation)
            citation_journal = get_bibtex_journal(individual_citation)
            citation_url = get_bibtex_url(individual_citation)
            citation_doi = get_bibtex_doi(individual_citation)

           
        print('\n')
        print(citation_family_names)
        print(citation_given_names)
        print(citation_title)
        print(citation_year)
        print(citation_publisher)
        print(citation_journal)
        print(citation_url)
        print(citation_doi)

        #creating the dict that serves as a template for the CITATION.CFF
        filedict = add_to_dict(
            git_repo_name, 
            git_author_family_name, 
            git_author_given_name, 
            git_repo_link,
            citation_family_names, 
            citation_given_names, 
            citation_title, 
            citation_year, 
            citation_url, 
            citation_doi, 
            citation_publisher, 
            citation_journal )


        print('\n')
        print(filedict)
        print('\n')
        #dump the dict contents into the final YAML file CITATION.CFF
        with open(r'{}/CITATION.cff'.format(repo_path), 'w') as file:
                documents = yaml.dump(filedict, file, sort_keys=False)


else:
    #warning in the console, since no citation or DOI was found
    print('\n')
    warnings.warn("Warning...........Please insert citation or DOI ")

    #creating the dict that serves as a template for the CITATION.CFF
    filedict = add_to_dict(
            git_repo_name, 
            git_author_family_name, 
            git_author_given_name, 
            git_repo_link,
            citation_family_names, 
            citation_given_names, 
            citation_title, 
            citation_year, 
            citation_url, 
            citation_doi, 
            citation_publisher, 
            citation_journal )
    
    print('\n')
    print(filedict)
    print('\n')
    #dump the dict contents into the final YAML file CITATION.CFF
    with open(r'{}/CITATION.cff'.format(repo_path), 'w') as file:
            documents = yaml.dump(filedict, file)
    
#creating pull request with the CITATION.CFF
# git_pull_request(repo_path,branch_name, git_token )
