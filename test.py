from github import Github
import json

with open('config.json', 'r') as f:
    config = json.load(f)


# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token(config['github_token'])

# Public Web Github
g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(f'{repo.name} - Private: {repo.private}')
    # repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    # print(dir(repo))