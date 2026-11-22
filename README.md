# Mini-VulnFinBot — Secure CI/CD Pipeline

## 1. Project Description

Mini-VulnFinBot is a Flask-based mock financial assistant developed to demonstrate the integration of automated security testing into a CI/CD pipeline.

The project focuses on identifying security vulnerabilities in application code, dependencies, and Docker container images. It also includes AI-specific security test scenarios.

The application currently uses a mock assistant response instead of a real Large Language Model (LLM).

## 2. Technologies Used

- Python 3.13
- Flask
- pytest
- Bandit
- Semgrep
- pip-audit
- Docker
- Trivy
- OWASP ZAP
- GitHub Actions

## 3. Project Architecture

The project consists of the following main components:

- `app/` — Flask application and API routes.
- `tests/` — unit tests and AI-specific security tests.
- `security/semgrep/` — custom Semgrep security rules and controlled test cases.
- `reports/` — generated security reports.
- `.github/workflows/` — GitHub Actions CI/CD configuration.
- `Dockerfile` — Docker image configuration.
- `run.py` — application entry point.
- `requirements.txt` — Python dependencies.

### Security Pipeline Architecture

1. Source code is checked out from GitHub.
2. Python dependencies are installed.
3. Unit and AI security tests are executed.
4. Bandit and Semgrep analyze application code.
5. pip-audit checks dependencies.
6. Docker builds the application image.
7. Trivy scans the Docker image.
8. The application container is started and its health endpoint is checked.
9. OWASP ZAP performs a baseline scan.
10. Security reports are uploaded as GitHub Actions artifacts.

## 4. Installing Dependencies

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd vulnfinbot-secure-pipeline
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pytest bandit semgrep pip-audit
```

Docker Desktop is required for local container operations.

## 5. Running the Application

Start the Flask application:

```bash
python run.py
```

The application runs on:

```text
http://localhost:5000
```

Check application health:

```text
http://localhost:5000/health
```

The API endpoint is:

```text
POST /api/chat
```

Example request:

```json
{
  "message": "Hello"
}
```

## 6. Executing Tests

Run the complete test suite:

```bash
pytest -v
```

Run unit tests separately:

```bash
pytest tests/test_app.py -v
```

Run AI-specific security tests:

```bash
pytest tests/test_ai_security.py -v
```

The project contains 11 automated tests. All 11 tests passed during the final validation.

## 7. CI/CD Pipeline

GitHub Actions automatically executes the security pipeline when changes are pushed to the `main` branch or when a pull request targets `main`.

The workflow includes:

- Dependency installation
- Unit testing
- AI security testing
- Static Application Security Testing (SAST)
- Dependency vulnerability auditing
- Docker image building
- Container vulnerability scanning
- Dynamic Application Security Testing (DAST)
- Security report collection

The final workflow execution completed successfully.

## 8. Integrated Security Tools

### Bandit

Analyzes Python source code for common security issues.

### Semgrep

Uses custom security rules to identify insecure code patterns.

### pip-audit

Checks Python dependencies for known vulnerabilities.

### Trivy

Scans Docker images for vulnerable operating system packages and dependencies.

### OWASP ZAP

Performs a baseline security scan against the running Flask application.

### AI Security Tests

Tests five AI-related security scenarios:

- Instruction override
- System prompt disclosure
- Sensitive information disclosure
- Unauthorized tool usage
- Output validation

These tests currently use a mock application. They do not establish protection against these threats in a real LLM integration.

## 9. Accessing Security Reports

All security reports are stored in the `reports/` directory.

| Tool | Report |
|---|---|
| Bandit | `bandit-report.json` |
| Semgrep | `semgrep-report.json` |
| pip-audit | `dependency-report.json` |
| Trivy | `trivy-report.json` |
| OWASP ZAP | `zap-report.json` |
| AI Security Tests | `ai-security-report.md` |

Reports are uploaded to GitHub Actions as an artifact named:

`vulnfinbot-security-reports`

To access the reports:

1. Open the GitHub repository.
2. Select the Actions tab.
3. Open a successful workflow execution.
4. Find the Artifacts section.
5. Download `vulnfinbot-security-reports`.

## 10. Identified Vulnerabilities and Remediation Recommendations

### Trivy

The initial container scan identified:

- 48 HIGH
- 115 MEDIUM
- 68 LOW
- 9 UNKNOWN

After updating system packages and rebuilding the image, the results were:

- 47 HIGH
- 114 MEDIUM
- 68 LOW
- 9 UNKNOWN

The reduction indicates that updating packages resolved some findings. Remaining vulnerabilities require further investigation and dependency updates.

### OWASP ZAP

The baseline scan identified four alert types:

- Server version information disclosure
- Missing Content Security Policy header
- Missing Permissions Policy header
- Cacheable content

Recommended actions include configuring appropriate HTTP security headers, removing unnecessary server version information, and reviewing caching policies.

### Semgrep

A controlled test containing the Python `eval()` function was detected by the custom Semgrep rule.

The use of `eval()` can allow arbitrary code execution when untrusted input is evaluated.

Recommended remediation:

- Avoid using `eval()` with user-controlled input.
- Use safer parsing methods, such as `ast.literal_eval()` when only Python literals are required.
- Validate and restrict accepted input.

The vulnerable example was isolated in a security test file and was not part of the production application code.

### AI Security Testing

All five AI security test cases passed execution. However, the current mock application does not include a real LLM, confidential data source, or external tool integrations.

Further testing is required before deploying a real AI-powered financial assistant.

### General Recommendations

- Regularly update application dependencies.
- Rebuild and rescan Docker images.
- Configure HTTP security headers.
- Review security findings after every pipeline execution.
- Keep security test cases separate from production code.
- Perform additional security testing before integrating a real LLM.

## Conclusion

The project demonstrates an integrated security CI/CD pipeline using automated testing, static analysis, dependency auditing, container scanning, and dynamic security testing.

GitHub Actions automates the security checks and collects generated reports as downloadable artifacts.

The final pipeline execution completed successfully, providing a foundation for continuous security monitoring and further improvements.