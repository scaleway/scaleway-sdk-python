# Contribute to `scaleway-sdk-python`

`scaleway-sdk-pythom` is Apache 2.0 licensed and accepts contributions via GitHub.
This document will cover how to contribute to the project and report issues.

## Topics

- [Reporting Security Issues](#reporting-security-issues)
- [Reporting Issues](#reporting-issues)
- [Suggesting feature](#suggesting-feature)
- [Contributing Code](#contributing-code)
- [Community Guidelines](#community-guidelines)

## Reporting security issues

Please refer to our [security policy](../SECURITY.md).

## Reporting issues

A great way to contribute to the project is to send a detailed report when you encounter a bug.
We always appreciate a well-written, thorough bug report, and will thank you for it!
Before opening a new issue, we appreciate you reviewing open issues to see if there are any similar requests.
If there is a match, thumbs up the issue with a 👍 and leave a comment if you have additional information.

When reporting an issue, please include the `scaleway-sdk-python` version information

## Suggesting a feature

When requesting a feature, some of the questions we want to answer are:

- What value does this feature bring to end users?
- How urgent is the need (nice to have feature or need to have)?
- Does this align with the goals of `scaleway-sdk-python`?

## Contributing code

Before contributing to the code, make sure you have read about the [continuous code deployment](docs/CONTINUOUS_CODE_DEPLOYMENT.md) process we are using on this repo.

### Submit code

To submit code:

- Create a fork of the project
- Create a topic branch from where you want to base your work (usually master)
- Add tests to cover contributed code
- Push your commit(s) to your topic branch on your fork
- Open a pull request against `scaleway-sdk-python` `main` branch that follows [PR guidelines](#pull-request-guidelines)

The [maintainers](MAINTAINERS.md) of `scaleway-sdk-python` use a "Let's Get This Merged" (LGTM) message in the pull request to note that the commits are ready to merge.
After one or more maintainer states LGTM, we will merge.
If you have questions or comments on your code, feel free to correct these in your branch through new commits.

### Pull Request Guidelines

The goal of the following guidelines is to have Pull Requests (PRs) that are fairly easy to review and comprehend, and code that is easy to maintain in the future.

- **Pull Request title should respect [conventional commits](https://www.conventionalcommits.org/en/v1.0.0) specifications** and be clear on what is being changed.
  The scope is the namespace on which the changes are made or `core` for changes which concern the whole SDK. Examples:
    - A fix for the InstanceAPI.create_server method will be titled `fix(instance): ...`
    - A change in authentication handling will be titled fix(core): ...
    - A new instance feature will be title `feat(instance): ...`
- **Keep it readable for human reviewers** and prefer a subset of functionality (code) with tests and documentation over delivering them separately
- **Don't forget commenting code** to help reviewers understand and to keep [our Go Report Card](https://goreportcard.com/report/github.com/scaleway/scaleway-sdk-go) at A+
- **Notify Work In Progress PRs** by prefixing the title with `[WIP]`
- **Please, keep us updated.**
  We will try our best to merge your PR, but please notice that PRs may be closed after 30 days of inactivity.

Your pull request should be rebased against the `main` branch.

Keep in mind only the **pull request title** will be used as commit message as we stash all commits on merge.

## Community guidelines

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Thank you for reading through all of this, if you have any question feel free to [reach us](README.md#reach-us)!

## Developer documentation

### Code style

Code formatting and linting are enforced with Ruff
Our CI checks formatting automatically with Ruff, so please ensure your code passes the same checks locally before submitting.

### Testing

We use pytest for testing.
All new features and bug fixes should include corresponding tests.

