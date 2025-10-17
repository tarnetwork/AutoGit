import os
import json


def main():
  print("Welcome to the Github Multi-tool!")
  print("Please select an option:")
  print("1. Create a new repository")
  print("2. Update a repository")
  print("3. Exit")
  option = input("Enter your choice: ")

  if option == "1":
    create_repo()
  elif option == "2":
    print("Update a repository (not implemented yet)")
  elif option == "3":
    print("Exiting...")
    return
  else:
    print("Goodbye!")


def create_repo():
  name = input("Enter the name of the repository: ")
  description = input("Enter a description for the repository (optional): ")
  private_input = input(
      "Do you want the repository to be private? (y/n): ").lower()

  if not name:
    print("Please enter a name for the repository.")
    return

  private = True if private_input == "y" else False

  print(f"\nRepository Name: {name}")
  print(f"Repository Description: {description or 'None'}")
  print(f"Repository will be {'private' if private else 'public'}.")

  token = os.getenv("GITHUB_TOKEN")
  if not token:
    token = input("\nEnter your GitHub token (will not be saved): ")

  print("\nCreating a new repository...")

  # Prepare JSON data
  repo_data = {"name": name, "description": description, "private": private}

  # Use os.system safely
  cmd = (f"curl -L -X POST "
         f"-H 'Accept: application/vnd.github+json' "
         f"-H 'Authorization: token {token}' "
         f"-H 'X-GitHub-Api-Version: 2022-11-28' "
         f"https://api.github.com/user/repos "
         f"-d '{json.dumps(repo_data)}'")

  os.system(cmd)


if __name__ == "__main__":
  main()
