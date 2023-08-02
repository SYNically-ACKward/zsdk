# Contributing to Zscaler SDK (zsdk)

We welcome contributions to the Zscaler SDK! This document provides guidelines to make the contribution process smooth and efficient.

## Getting Started

1. **Fork the Repository**: Click the 'Fork' button on the top-right corner of the repository's GitHub page. This creates a copy of the repository under your GitHub account.

2. **Clone Your Fork**: Clone the forked repository to your local machine by running:

   \`\`\`bash
   git clone https://github.com/SYNically-ACKward/zsdk.git
   \`\`\`

3. **Create a New Branch**: Before making changes, create a new branch to work on. This helps to keep work on different features or issues isolated.

   \`\`\`bash
   git checkout -b my-new-feature
   \`\`\`

4. **Set Up the Development Environment**: Ensure you have Poetry installed, then run the following to install dependencies:

   \`\`\`bash
   poetry install
   \`\`\`

5. **Make Your Changes**: Write code, add tests, and update documentation as needed.

6. **Commit Your Changes**: Use meaningful commit messages that describe the changes made.

   \`\`\`bash
   git add .
   git commit -m "Add a new feature"
   \`\`\`

7. **Push Your Changes**: Push the changes to your fork on GitHub.

   \`\`\`bash
   git push origin my-new-feature
   \`\`\`

8. **Open a Pull Request**: Go to the original repository on GitHub, click 'New pull request', and select your fork and the new feature branch.

## Code Style and Best Practices

- Follow PEP 8, the Python style guide.
- Write unit tests for new code.
- Include comments and documentation for non-trivial functions and methods.
- Ensure that all tests pass before submitting a pull request.

We follow the PEP 8 style guide for Python code, with the exception of the line length limit. In this project, we use a line length limit of 120 characters instead of the standard 79.

Please ensure your code adheres to this limit and use tools such as `flake8` with the appropriate configuration to check your code for style compliance.

## Questions or Problems?

Feel free to open an issue or contact the maintainers. We're here to help!

Thank you for contributing to the Zscaler SDK!
