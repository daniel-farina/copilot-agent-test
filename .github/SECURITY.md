# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please open a GitHub issue or contact the repository owner directly.

## Security Posture

### Configuration Files

- **`.env.example`**: Contains only placeholder/fake values for documentation purposes. No real credentials are stored in version control.
- **`.github/copilot-instructions.md`**: Defines the coding standards and security verification protocol for contributors.

### Secrets and Credentials

- Real secrets and credentials must **never** be committed to this repository.
- Use environment variables for all sensitive configuration values.
- The `.env.example` file documents the required environment variables with fake placeholder values only.

### Dependency Security

- Dependencies should be kept up to date and reviewed for known vulnerabilities.
- Use tools such as `npm audit`, `pip-audit`, or equivalent for the project's ecosystem when applicable.

## Security Verification Checklist

Contributors must complete the following steps when opening a pull request:

1. Confirm no real API keys, tokens, or passwords are present in any committed file.
2. Review any new configuration files to ensure they do not contain secrets.
3. Include a **Security Check** section in the PR description summarizing the results.
