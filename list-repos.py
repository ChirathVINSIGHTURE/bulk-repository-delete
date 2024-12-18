import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get GitHub username and PAT from environment variables
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_PAT")

if not USERNAME or not TOKEN:
    print("Error: Missing GITHUB_USERNAME or GITHUB_PAT in the .env file.")
    exit(1)

# GitHub API endpoint for fetching user repositories
url = f"https://api.github.com/user/repos"

# To list organization repositories only, you can use the GET /orgs/{org}/repos endpoint
# https://api.github.com/orgs/{organization}/repos


# Parameters for pagination and visibility
params = {
    "per_page": 100,  # Maximum allowed by GitHub API
    "type": "owner",  # Only fetch repositories owned by the user
    "page": 1
    # "visibility": "private"  #To filter by visibility (e.g., public, private), add the visibility parameter
}

all_repos = []

while True:
    response = requests.get(url, auth=(USERNAME, TOKEN), params=params)
    if response.status_code != 200:
        print(f"Failed to fetch repositories: {response.status_code} {response.text}")
        break

    repos = response.json()
    if not repos:
        break

    # Append repository names to the list
    all_repos.extend([repo["name"] for repo in repos])

    # Move to the next page
    params["page"] += 1

# Save repository names to a text file
with open("repos.txt", "w") as file:
    file.write("\n".join(all_repos))

print(f"Successfully saved {len(all_repos)} repositories to repos.txt.")
