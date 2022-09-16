
import git
from patterns import *
import re
import requests

def getGitInfo(repo_path):
    """Collects all BibTex formatted citations existent in the README.md

    Parameters
    ----------
    repo_path : str
        path to the repository where the citation is needed

    Returns
    -------
    git_repo_name : str
        holds the name of the GitHub Repository
    git_author_family_name  : str
        holds the family name of the GitHub Repository author
    git_author_given_name : str
        holds the given name of the GitHub Repository author
    git_repo_link : str
        holds the link for the GitHub Repository
    contributors_given_names : list
        holds the names of the GitHub Repository contributors

    """

    repo = git.Repo(repo_path)

    origin = repo.remote("origin")

    assert origin.exists()
    origin.fetch()

    git_repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]

    git_repo_link = repo.remotes.origin.url.split('.git')[0]
    
    git_author = repo.git.show("-s", "--format=Author: %an <%ae>")

    git_author_family_name = re.findall(
            GIT_FAMILY_NAMES_PATTERN, git_author, flags=re.DOTALL)

    git_author_family_name = ''.join(map(str, git_author_family_name))

    GIT_GIVEN_NAMES_PATTERN = '(?<=Author:\\s%s\\s)(.*?)(?=\\s)' % git_author_family_name

    git_author_given_name = re.findall(
            GIT_GIVEN_NAMES_PATTERN, git_author, flags=re.DOTALL)

    git_author_given_name = ''.join(map(str, git_author_given_name))
    
    all_contributors = list()
    contributors_given_names = []
    page_count = 1
    while True:
        contributors = requests.get("https://api.github.com/repos/SimaoBolota-MetaCell/CZI-Citation-Final-draft/contributors?page=%d"%page_count)
        if contributors != None and contributors.status_code == 200 and len(contributors.json()) > 0:
                all_contributors = all_contributors + contributors.json()
        else:
                break
        page_count = page_count + 1
    count=len(all_contributors)
    print('----------')
    print(count)
    if(count>0):
        contributors_dict = all_contributors[0:(len(all_contributors))][0:(len(all_contributors))]
        for single_contributor_dict in contributors_dict:
                contributors_given_names.append(single_contributor_dict['login'])

    return git_repo_name, git_author_family_name, git_author_given_name, git_repo_link, contributors_given_names



