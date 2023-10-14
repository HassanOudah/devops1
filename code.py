from github import Github
# credentials.yml contains your usr/repo and PAT created in step 11 above
# So we load the data into a YML object
data = yaml.safe_load(open('username-credentials.yml'))
# Extract the user and token from the data object
# 0. Complete these 2 lines below
# user = HassanOudah
# token = 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
# using an access token
g = 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
repo = g.get_repo(HassanOudah)
## Complete your tasks from here
# 1. Get all branches you have created for your public repo
repo = g.get_repo("HassanOudah/devops1")
branches = list(repo.get_branches())
for branch in branches:
    print(branch.name)
# 2. Get all pull requests you have created
pull_requests = g.search_issues('is:pr is:open repo:HassanOudah/devops1')
for pr in pull_requests:
    print(pr.title)
    print(pr.html_url)
# 3. Get a list of commits you have created in your `main` branch
commits = repo.get_commits(sha="main")
for commit in commits:s
    if commit.author.login == "HassanOudah":
        print(commit.sha, commit.commit.message)