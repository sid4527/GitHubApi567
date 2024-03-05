"""
    Module is utilizing the github API 

"""
import requests
def get_user_repositories(user_id):
    """ Function is getting user repositories """

    url = f"https://api.github.com/users/{user_id}/repos"


    response = requests.get(url)


    if response.status_code == 200:
        repositories = response.json()
        repo_commits = []


        for repo in repositories:
            repo_name = repo['name']
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"


            commits_response = requests.get(commits_url)
            if commits_response.status_code == 200:
                commits = commits_response.json()
                num_commits = len(commits)
                repo_commits.append((repo_name, num_commits))

        return repo_commits
    else:

        print(f"Failed to grab repositories for user '{user_id}'. Error: {response.status_code}")


user_id = "sid4527"
repos_with_commits = get_user_repositories(user_id)

if repos_with_commits:
    for repo, num_commits in repos_with_commits:
        print(f"Repo: {repo} Number of commits: {num_commits}")
else:
        print("No repositories found or an error occurred.")
    