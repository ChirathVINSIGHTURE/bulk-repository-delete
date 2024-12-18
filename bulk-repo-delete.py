import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get environment variables
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_PAT")

if not USERNAME or not TOKEN:
    print("Error: Missing GITHUB_USERNAME or GITHUB_PAT in the .env file.")
    exit(1)

# Read list of repositories from repos.txt
try:
    with open("repos.txt", "r") as file:
        repos_to_delete = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("Error: repos.txt file not found.")
    exit(1)

if not repos_to_delete:
    print("No repositories found in repos.txt.")
    exit(1)

# Delete the repositories
for repo in repos_to_delete:
    url = f"https://api.github.com/repos/{USERNAME}/{repo}"
    response = requests.delete(url, auth=(USERNAME, TOKEN))
    if response.status_code == 204:
        print(f"Deleted {repo}")
    else:
        print(f"Failed to delete {repo}: {response.status_code} {response.text}")
