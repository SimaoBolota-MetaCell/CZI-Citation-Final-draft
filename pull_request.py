import requests
import git
import json
def create_pull_request(project_name, repo_name, title, description, head_branch, base_branch, git_token):
    """Creates the pull request for the head_branch against the base_branch"""
    git_pulls_api = "https://api.github.com/repos/{0}/{1}/pulls".format(
        project_name,
        repo_name)
    headers = {
        "Authorization": "token {0}".format(git_token),
        "Content-Type": "application/vnd.github+json"}

    payload = {
        "title": title,
        "body": description,
        "head": head_branch,
        "base": base_branch,
    }

    r = requests.post(
        git_pulls_api,
        headers=headers,
        data=json.dumps(payload))

    if not r.ok:
        print("Request Failed: {0}".format(r.text))