from github3 import login

with open('github-token', 'r') as fh:
    token = fh.readline().strip()

gh = login(token=token)
repo = gh.repository('sigmavirus24', 'github3.py')
print repo.default_branch

# get the most recent commit of the default branch
branch = repo.branch(repo.default_branch)
last_sha = branch.commit.sha
print last_sha

t = repo.tree(last_sha)
for entry in t.tree:
    print "{:25} {}".format(entry.path, entry.url)
