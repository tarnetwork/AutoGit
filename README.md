# GitHub Multi-tool

A simple, interactive command-line tool for managing GitHub repositories directly from your terminal.

## Features

- **Create New Repositories**: Quickly create public or private GitHub repositories
- **Interactive CLI**: User-friendly prompts guide you through the process
- **Secure Token Management**: Supports both environment variables and direct input for GitHub authentication

## Prerequisites

- Python 3.11 or higher
- A GitHub account
- GitHub Personal Access Token with `repo` scope

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Configuration

### GitHub Token Setup

You'll need a GitHub Personal Access Token to use this tool. You can provide it in two ways:

**Option 1: Environment Variable (Recommended)**
```bash
export GITHUB_TOKEN=your_github_token_here
```

**Option 2: Enter when prompted**
The tool will ask for your token if it's not set as an environment variable.

### Creating a GitHub Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name
4. Select the `repo` scope
5. Click "Generate token"
6. Copy the token immediately (you won't be able to see it again)

## Usage

Run the tool:
```bash
python main.py
```

### Available Options

1. **Create a new repository**
   - Enter repository name
   - Add an optional description
   - Choose public or private visibility
   - The tool will create the repository using the GitHub API

2. **Update a repository** _(Coming soon)_
   - Feature in development

3. **Exit**
   - Close the application

## Example

```bash
$ python main.py

Welcome to the Github Multi-tool!
Please select an option:
1. Create a new repository
2. Update a repository
3. Exit
Enter your choice: 1

Enter the name of the repository: my-awesome-project
Enter a description for the repository (optional): A great new project
Do you want the repository to be private? (y/n): n

Repository Name: my-awesome-project
Repository Description: A great new project
Repository will be public.

Creating a new repository...
✓ Repository created successfully!
```

## Project Structure

```
.
├── main.py           # Main application file
└── README.md         # This file
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open source and available under the MIT License.

## Roadmap

- [ ] Update repository functionality
- [ ] Delete repository option
- [ ] List user repositories
- [ ] Repository settings management
- [ ] Batch operations support

---

Made for GitHub users
