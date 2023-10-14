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
# main default
# my-new-branch
# 2. Get all pull requests you have created
# HassanOudahpushed 2 commits to my-new-branch • 2d87b5f…c78c263 • 10 minutes ago
# 3. Get a list of commits you have created in your `main` branch
# Merge pull request #1 from HassanOudah/main
# Pull request merge
# HassanOudahpushed 2 commits to my-new-branch • 2d87b5f…c78c263 • 10 minutes ago
# Add files via upload
# HassanOudahpushed 1 commit to main • 2d87b5f…aca9f8f • 23 minutes ago
# add first commit
# HassanOudahcreated my-new-branch • 2d87b5f • 33 minutes ago
# add first commit
# HassanOudahcreated main • 2d87b5f • 35 minutes ago
