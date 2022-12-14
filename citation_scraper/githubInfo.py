
import git
from patterns import *
import re

def getGitInfo(repo_path):
    """Collects all BibTex formatted citations existent in the README.md

    Parameters
    ----------
    repo_path : str
        path to the repository where the citation is needed

    Returns
    -------
    git_repo_username : str
        holds the GitHub Repository username
    git_repo_name : str
        holds the name of the GitHub Repository
    git_author_family_name  : str
        holds the family name of the GitHub Repository author
    git_author_given_name : str
        holds the given name of the GitHub Repository author
    git_repo_link : str
        holds the link for the GitHub Repository
    git_base_branch : str
        holds the GitHub repository base branch, between master or main

    """
    #collecting the GitHub repository info
    repo = git.Repo(repo_path)
    #collecting the GitHub repository origin
    origin = repo.remote("origin")
    assert origin.exists()
    origin.fetch()
    #collecting the GitHub repository base branch, between master or main
    remote_refs = repo.remote().refs
    for refs in remote_refs:
        refs= str(refs)
        if refs == 'origin/main':
            git_base_branch = 'main'  
        elif(refs == 'origin/master'):
            git_base_branch = 'master'  
    #collecting the GitHub username
    git_repo_username = repo.remotes.origin.url.split('.git')[0].split('/')[-2]
    #collecting the GitHub repository name
    git_repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]
    #collecting the GitHub repository link
    git_repo_link = repo.remotes.origin.url.split('.git')[0]
    #collecting the GitHub repository author
    git_author = repo.git.show("-s", "--format=Author: %an <%ae>")
    #finding the family name from the GitHub author 
    git_author_family_name = re.findall(
            GIT_FAMILY_NAMES_PATTERN, git_author, flags=re.DOTALL)
    git_author_family_name = ''.join(map(str, git_author_family_name))
    
    #finding the given name from the GitHub author 
    GIT_GIVEN_NAMES_PATTERN = '(?<=Author:\\s%s\\s)(.*?)(?=\\s)' % git_author_family_name
    git_author_given_name = re.findall(
            GIT_GIVEN_NAMES_PATTERN, git_author, flags=re.DOTALL)
    git_author_given_name = ''.join(map(str, git_author_given_name))
    #data transformations needed to ensure the correct formatting outcome
    git_author_family_name = git_author_family_name.replace("??", "a")
    git_author_family_name = git_author_family_name.replace("??", "a")
    git_author_family_name = git_author_family_name.replace("??", "o")
    git_author_family_name = git_author_family_name.replace("??", "i")
    git_author_given_name = git_author_given_name.replace("??", "a")
    git_author_given_name = git_author_given_name.replace("??", "a")
    git_author_given_name = git_author_given_name.replace("??", "o")
    git_author_given_name = git_author_given_name.replace("??", "i")

    return git_repo_username, git_repo_name, git_author_family_name, git_author_given_name, git_repo_link,git_base_branch



