import os
import subprocess
import shutil

print(f"Current working directory: {os.getcwd()}")

# Check if git is available in the PATH
git_path = shutil.which("git")
if not git_path:
    raise EnvironmentError("Git is not found in the system PATH. Please ensure git is installed and accessible.")
else:
    print(f"Using git executable at: {git_path}")

# This script iterates through all folders in the specified base directory and runs a git pull command in each one.
# If a folder contains subdirectories, it will recursively check for Git repositories and log their information.

def update_git_repos(base_dir, md_file):
    for folder in os.listdir(base_dir):
        repo_path = os.path.join(base_dir, folder)
        if os.path.isdir(repo_path):
            git_dir = os.path.join(repo_path, ".git")
            if os.path.isdir(git_dir):  # Check if the directory is a Git repository
                print(f"Updating {repo_path}...")
                subprocess.run([git_path, "-C", repo_path, "pull"])
                
                # Get the last commit information
                result = subprocess.run(
                    [git_path, "-C", repo_path, "log", "-1", "--pretty=format:%h %an %ar %s"],
                    capture_output=True, text=True
                )
                last_commit = result.stdout.strip()
                
                # Write repository info to the Markdown file
                with open(md_file, "a") as f:
                    f.write(f"### Repository: {repo_path}\n")
                    f.write(f"- **Last Commit**: {last_commit}\n\n")
            else:
                # Recursively check subdirectories
                update_git_repos(repo_path, md_file)

base_dir = "/home/charles/myrepos"
md_file = os.path.join(base_dir, "repos_info.md")
print(f"Markdown file path: {md_file}")

# Clear or create the Markdown file
with open(md_file, "w") as f:
    f.write("# Repositories Information\n\n")
print(f"Created or cleared the file: {md_file}")

update_git_repos(base_dir, md_file)
print(f"Repository information has been saved to {md_file}")