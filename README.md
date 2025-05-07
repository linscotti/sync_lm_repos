# Sync Repositories Automation

This repository contains a Python script (`pull_repos.py`) that automates the process of updating multiple Git repositories and logs their information into a Markdown file.

## Features
- Recursively scans a base directory for Git repositories.
- Runs `git pull` to update each repository.
- Logs the last commit information (hash, author, time, and message) for each repository.
- Saves the information in a Markdown file (`repos_info.md`).

## Prerequisites
1. **Python**: Ensure Python 3.x is installed on your system.
   - On Linux Mint, you can install Python with:
     ```bash
     sudo apt update && sudo apt install python3
     ```
2. **Git**: Ensure Git is installed and available in your system's PATH.
   - On Linux Mint, you can install Git with:
     ```bash
     sudo apt update && sudo apt install git
     ```
3. **Base Directory**: Organize your repositories under a base directory (e.g., `/home/username/repos`).
## Setup
1. Clone or download this repository.
2. Place the `pull_repos.py` script in your desired directory.
3. Update the `base_dir` variable in the script to point to your base directory containing the repositories.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing `pull_repos.py`.
3. Run the script using the following command:
   ```bash
   python pull_repos.py

```powershell
uv run pull_repos.py  
``` 

Output
The script will:
Update all Git repositories in the base directory and its subdirectories.
Create or overwrite a Markdown file (repos_info.md) in the base directory.
Log the following information for each repository:
Repository path.
Last commit hash.
Commit author.
Commit time (relative).
Commit message

Example repos_info.md

# Repositories Information

### Repository: /home/charles/myrepos/github/repos
- **Last Commit**: a1b2c3d John Doe 2 days ago Fixed a bug

### Repository: /home/charles/myrepos/gitlab/repos
- **Last Commit**: e4f5g6h Jane Smith 1 week ago Added new feature

Notes
The script skips directories that are not Git repositories.
Subdirectories are recursively scanned for repositories.

Troubleshooting
If you encounter issues, ensure:
The base_dir path is correct.
Git is installed and accessible from the command line.
Python is installed and the script is executed with the correct Python version.

