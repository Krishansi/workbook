from github import Github
import json

# Replace 'YOUR_GITHUB_ACCESS_TOKEN' with your actual GitHub access token.
# If you don't have one, you can create it on GitHub under Developer settings.
#access_token = 'YOUR_GITHUB_ACCESS_TOKEN'
#g = Github(access_token)
g = Github()

# Replace 'owner' and 'repo' with the username and repository name respectively.
owner = 'Krishansi'
repo_name = 'workbook'

# Get the repository object
repo = g.get_repo(f'{owner}/{repo_name}')

# Get all commits for the repository
commits = repo.get_commits()

# List to store commit history data
commit_history = []

# Extract commit data and append to the list
for commit in commits:
    commit_data = {
        "sha": commit.sha,
        "author": commit.author.login if commit.author else "Unknown",
        "message": commit.commit.message,
        "date": commit.commit.author.date.strftime("%Y-%m-%d %H:%M:%S"),
    }
    commit_history.append(commit_data)
    
print(commit_history)

# Save the commit history as a JSON file
with open('commit_history.json', 'w') as json_file:
    json.dump(commit_history, json_file, indent=2)

print("Commit history downloaded and saved in commit_history.json.")
