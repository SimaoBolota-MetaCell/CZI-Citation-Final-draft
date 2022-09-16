from bibtexCitation import *
from apaCitation import *
from bibtex_from_doi import *
from create_dict import *
from pull_request import *
import yaml
import git
import json
import requests
import warnings
from patterns import *
import sys
from ruamel.yaml import *
import tkinter
from tkinter import *
from tkinter import messagebox
from githubInfo import *
from git_interaction import *


repo_path = '/Users/simaosa/Desktop/MetaCell/Projects/CZI/FinalCode_Citation_project/CZI-Citation-Final-draft'

branch_name = 'branch_name3'


######################### GIT INTERACTIONS #########################

git_repo_name, git_author_family_name, git_author_given_name, git_repo_link, contributors_given_names = getGitInfo(repo_path)

git_readme_link = git_repo_link + '/blob/main/README.md'

README_LINK = git_readme_link


######################### GIT BRANCH #########################

git_branch( repo_path, branch_name)

git_token = input("Enter the authentication git token: ")


######################### INITIALIZATIONS #########################

citation_title = {}
citation_publisher = {}
citation_url = {}
citation_family_names = {}
citation_given_names = {}
citation_year = {}
citation_journal = {}
citation_doi = {}

# #########################  BIBTEX CITATION  ##########################

if (bool(get_bibtex_citations(README_LINK))):
    print('BibTex Citation')
    all_bibtex_citations = get_bibtex_citations(README_LINK)

    for individual_citation in all_bibtex_citations:
        #data transformations needed to enasure the correct formatting outcome
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
            contributors_given_names,
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
    with open(r'./CZI-Citation-Final-draft/CITATION.cff', 'w') as file:
            documents = yaml.dump(filedict, file, sort_keys=False)


#########################  APA CITATION  ##########################


elif bool(get_bibtex_citations(README_LINK))==False and bool(get_apa_citations(README_LINK)):
    
    
    APA_text, all_apa_authors, all_apa_citations = get_apa_citations(
        README_LINK)
    
    if (bool(all_apa_citations)):
        print('APA Citation')
        APA_text, all_apa_authors, all_apa_citations = get_apa_citations(
            README_LINK)

        for individual_citation in all_apa_citations:
            individual_citation = ''.join(map(str, individual_citation))
            individual_citation = all_apa_authors + ' ' + individual_citation
            citation_family_names = get_apa_family_names(all_apa_authors)
            citation_given_names = get_apa_given_names(all_apa_authors)
            citation_year = get_apa_year(individual_citation)
            citation_year = citation_year
            citation_title = get_apa_title(individual_citation)
            citation_journal = get_apa_journal(citation_title, APA_text)
            citation_doi = get_apa_doi(APA_text)

        filedict = add_to_dict(
            contributors_given_names,
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
        with open(r'./CZI-CItation-Final-draft/CITATION.cff', 'w') as file:
                documents = yaml.dump(filedict, file, sort_keys=False)

#########################  ONLY DOI  ##########################

    else:
        print('DOI Citation')
        all_bibtex_citations = get_citation_from_doi(README_LINK)
        for individual_citation in all_bibtex_citations:
            # print(individual_citation)
            individual_citation = re.sub('"', '}', individual_citation)
            individual_citation = re.sub('= }', '= {', individual_citation)
            individual_citation = individual_citation + '}}'

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


        filedict = add_to_dict(
            contributors_given_names,
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
        with open(r'./CZI-CItation-Final-draft/CITATION.cff', 'w') as file:
                documents = yaml.dump(filedict, file, sort_keys=False)


#################### No CITATION INFO - USE GIT AUTHOR INFO ####################

else:
    # #warning pop up message box
    # root = Tk()
    # inFront = Toplevel(root) # (Manually put toplevel in front of root)
    # messagebox.showwarning("Warning", "No Citation information found on the READ.MD",parent=inFront)

    #warning in the console
    print('\n')
    warnings.warn("Warning...........Please insert citation or DOI ")


    filedict = add_to_dict(
            contributors_given_names,
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

    with open(r'./CZI-CItation-Final-draft/CITATION.cff', 'w') as file:
            documents = yaml.dump(filedict, file)
    


#########################  PUSH COMMITS and PULL REQUEST  ##########################

git_pull_request(repo_path,branch_name, git_token )
