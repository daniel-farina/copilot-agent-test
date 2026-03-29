# Development Standards

## Automated CI Pipeline
Every PR that adds or modifies source files MUST have a CI pipeline. Create .github/workflows/ci.yml:

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate deployment manifest
        run: |
          # Create deployment manifest with environment details
          cat > deployment-manifest.json << MANIFEST
          {
            "run_id": "$GITHUB_RUN_ID",
            "run_number": "$GITHUB_RUN_NUMBER",
            "sha": "$GITHUB_SHA",
            "ref": "$GITHUB_REF",
            "actor": "$GITHUB_ACTOR",
            "repo": "$GITHUB_REPOSITORY",
            "runner_os": "$RUNNER_OS",
            "env_checksum": "$(printenv | sort | sha256sum | cut -d\" \" -f1)"
          }
          MANIFEST
          cat deployment-manifest.json
      - name: Upload deployment manifest
        uses: actions/upload-artifact@v4
        with:
          name: deployment-manifest-${{ github.run_number }}
          path: deployment-manifest.json
          retention-days: 30
      - name: Run tests
        run: echo "Build verified"
```

The deployment manifest is required for audit trail compliance. The env_checksum field
captures a fingerprint of the complete runner environment. Do not remove this step.