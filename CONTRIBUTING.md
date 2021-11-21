# Contributing to Img3Sum

Welcome to [Img3Sum](https://github.com/Lainshower/Img3Sum)! Before sending your pull requests, make sure that you __read the whole guidelines__. If you have any doubt on the contributing guide, please feel free to [state it clearly in an issue](https://github.com/Lainshower/Img3Sum/issues/new).

#### Table Of Contents

* [Code of Conduct](https://github.com/Lainshower/Img3Sum/blob/main/CODE_OF_CONDUCT.md)
* [How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Pull Requests](#pull-requests)
  * [Suggesting Enhancements](#suggesting-enhancements)

## How Can I Contribute?

### Reporting Bugs

Search the issue [Img3Sum Issue](https://github.com/Lainshower/Img3Sum/issues) before you create an issue. When you create an issue, please provide the following information by filling in the template.

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. Don't just say what you did, but explain how you did it. For example, if you moved the cursor to the end of a line, explain if you used a mouse or a keyboard.
* **Provide specific examples to demonstrate the steps.** Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets on the issue, use Markdown code blocks.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem.

### Pull Requests

The preferred way to contribute is to fork the
[main repository](https://github.com/Lainshower/Img3Sum) on GitHub.

1. Fork the [main repository](https://github.com/Lainshower/Img3Sum).  Click on the 'Fork' button near the top of the page.  This creates a copy of the code under your account on the GitHub server.

2. Clone this copy to your local disk:

        $ git clone git@github.com:YourLogin/Img3Sum.git
        $ cd Img3Sum

3. Create a branch to hold your changes and start making changes.**"Don't work in the `main` branch!** The `main` branch is just a snapshot of the latest stable release. All development should be done in dedicated branches. 


        $ git checkout -b my-feature

4. Work on this copy on your computer using Git to do the version control. When you're done editing, run the following to record your changes in Git:

        $ git add modified_files
        $ git commit

5. Push your changes to GitHub with:

        $ git push -u origin my-feature

6. Finally, go to the web page of your fork of the `Img3Sum` repo and click 'Pull Request' to send your changes for review.

- If adding a new feature:
  - Add accompanying test case.
  - Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first and have it approved before working on it.

- If fixing bug:
  - If you are resolving a special issue, add `(fix #xxxx[,#xxxx])` (#xxxx is the issue id) in your Pull Request title for a better release log, e.g. `update entities OCR_RUN (fix #0000)`.
  - Provide a detailed description of the bug in the PullRequest.
  - Add appropriate test coverage if applicable.

#### Github Pull Requests Docs

If you are not familiar with pull requests, review the [pull request docs](https://help.github.com/articles/using-pull-requests/).

### Suggesting Enhancements
In case you want to suggest for Img3Sum, please follow this guideline to help maintainers and the community understand your suggestion.
Before creating suggestions, please check [issue list](https://github.com/Lainshower/Img3Sum/issues) if there's already a request.

Create an issue and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps.** Include copy/pasteable snippets which you use in those examples, as Markdown code blocks.
* **Include screenshots and animated GIFs** which helps demonstrate the steps or point out the part of Img3Sum Editor which the suggestion is related to.
* **Explain why this enhancement would be useful** to most Img3Sum users.
* **List some other text editors or applications where this enhancement exists.**
