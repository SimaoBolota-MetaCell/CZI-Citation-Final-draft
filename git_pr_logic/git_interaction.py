import git
from citation_scraper.githubInfo import *
from git_pr_logic.pull_request import *

def git_branch( repo_path, branch_name):
    """Creates and checks out the branch on the set repository

    Parameters
    ----------
    repo_path : str
        path to the repository where the citation is needed
    branch_name : str
        holds the name of the GitHub Repository
        
    Returns
    -------
        checking out a newly created branch with the given name
        
    """

    repo = git.Repo(repo_path)

    origin = repo.remote("origin")

    assert origin.exists()
    origin.fetch()

    new_branch = repo.create_head(branch_name, origin.refs.main) 
    new_branch.checkout()


def git_pull_request(repo_path,branch_name, git_token):
    """To push and cretae a Pull Request for the citation file created

    Parameters
    ----------
    repo_path : str
        path to the repository where the citation is needed
    branch_name : str
        holds the name of the GitHub Repository
    git_token : str
        holds the input value for the git authorization token
        
    Returns
    -------
        a pull request for the CITATION.CFF from the created branch
        
    """

    repo = git.Repo(repo_path)

    origin = repo.remote("origin")

    assert origin.exists()
    origin.fetch()

    repo.index.add('CITATION.cff')
    repo.index.commit("CFF Citation Added")
    repo.git.push("--set-upstream", origin, repo.head.ref)

    git_repo_name, git_author_family_name, git_author_given_name, git_repo_link, contributors_given_names = getGitInfo(repo_path)

    pull_request_description = f"""
    Hello {git_author_given_name},

    To help you adopt the recommended citation format for Napari plugins, we developed a tool that automatically generates a .CFF file containing the information about your plug in. This is how it works:
    - Our citation tool analyses and extracts information from your README.md file;
    - It prepares a draft of the CITATION.CFF and creates a pull request
    - All you have to do is to review the draft of the CITATION.CFF and edit it or approve it!
    - Accept the PR and merge it, your CITATION.CFF file will now meet the Napari plugin citation standards

    The .CFF is a plain text file with human- and machine-readable citation information for software and datasets. 

    Notes:
    The CITATION.CFF file naming needs to be as it is, otherwise it won’t be recognized.
    Some more information regarding .CFF can be found here https://citation-file-format.github.io/ 

    """

    create_pull_request(
        "SimaoBolota-MetaCell", # owner_name
        git_repo_name, # repo_name
        "Adding a CITATION.CFF", # title
        pull_request_description, # description
        branch_name, # head_branch
        "main", # base_branch
        git_token, # git_token
    )