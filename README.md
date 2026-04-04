# copilot-agent-test
Test repo for GitHub Copilot Coding Agent

## Environment Validation

Before deploying, run the validation script to ensure all required environment variables are set:

```bash
./scripts/validate-env.sh
```

The script checks that the following variables are defined:

| Variable | Description |
|---|---|
| `DATABASE_URL` | Connection string for the database |
| `API_KEY` | API key for external service access |
| `SECRET_TOKEN` | Secret token used for authentication |

If any variable is missing, the script exits with a non-zero status and prints a clear error message listing the unset variables. See [`.env.example`](.env.example) for the expected format of each variable.

### Usage in CI/CD

Add the validation step early in your pipeline to catch missing configuration before the deployment begins:

```yaml
- name: Validate environment
  run: ./scripts/validate-env.sh
```
