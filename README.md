# Bulk Repo Delete

A Python script to delete multiple GitHub repositories in bulk using the GitHub API.

## Features
- Read a list of repositories from a file (`repos.txt`).
- Delete repositories from your GitHub account.
- Supports user-owned repositories.
- Easy configuration with a `.env` file.

---

## Requirements
- Python 3.6 or later
- GitHub Personal Access Token (PAT) with the `delete_repo` scope.

---

## Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/bulk-repo-delete.git
cd bulk-repo-delete
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Create a `.env` File
Create a `.env` file in the root directory and add your GitHub credentials:
```env
GITHUB_USERNAME=your-username
GITHUB_PAT=your-personal-access-token
```

### Step 4: Use the `list-repos` Script (Optional)
Run the `list-repos` script to generate a list of repositories for deletion:
```bash
python list_repos.py
```
This will create a `repos.txt` file containing the names of your repositories.

**Warning:** Review the generated `repos.txt` file carefully and filter out any essential repositories you want to keep. Only include repositories you are sure you want to delete, as this operation is irreversible.

### Step 5: Create/Edit the `repos.txt` File
If you want to manually create or edit the file, list the names of the repositories you want to delete, one per line:
```plaintext
repo1
repo2
repo3
```

---

## Usage
Run the script to delete repositories:
```bash
python delete_repos.py
```

---

## Notes
- Make sure your `GITHUB_PAT` has the `delete_repo` scope.
- The `repos.txt` file should contain exact repository names.
- Deleted repositories cannot be recovered. Proceed with caution.

---

## License
N/A