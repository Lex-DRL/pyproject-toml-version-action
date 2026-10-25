<div align="center">

# `pyproject.toml` version 🔢 Action

[![GitHub Release][github-release-shield]][github-release-url]

[github-release-shield]: https://img.shields.io/github/v/release/Lex-DRL/pyproject-toml-version-action?logo=github
[github-release-url]: https://github.com/Lex-DRL/pyproject-toml-version-action/releases/latest

*GitHub action to get version from `pyproject.toml`. Simple as that.*
</div>

## Example

```yaml
# ...

jobs:

  example-job:
    name: "Example"
    runs-on: ubuntu-latest
    timeout-minutes: 5  # Prevent stuck jobs

    steps:
    - name: ♻️ Check out code
      uses: actions/checkout@v7
      # with:
      #   fetch-depth: 0  # Critical for changelog + first-release support

    - name: "Extract version 🔢"
      # Internally, it sets up python and uses pip for its dependencies
      id: extract-version
      uses: Lex-DRL/pyproject-toml-version-action@v1
      # with:
      #   toml-file: 'pyproject.toml'  # What file to read version from
      #   python-version: '3.x'  # What python version to install
      #   skip-python-setup: false  # Skip python installation, if already done by previous steps

    - name: "Example use"
      # Here, we just print the output,
      # but feel free to pas it to an actual useful step: 
      run: |
        echo "Extracted version: ${{ steps.extract-version.outputs.version }}"
```
