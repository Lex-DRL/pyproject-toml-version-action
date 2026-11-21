<div align="center">

# `pyproject.toml` version 🔢 Action

[![GitHub Release][github-release-shield]][github-release-url]

[github-release-shield]: https://img.shields.io/github/v/release/Lex-DRL/pyproject-toml-version-action?logo=github
[github-release-url]: https://github.com/Lex-DRL/pyproject-toml-version-action/releases/latest

*GitHub action to get version from `pyproject.toml`. Simple as that.*
</div>

> [!NOTE]
> ## Dynamic version support
> aka *"getting version that's not typed in `pyproject.toml` directly but is referenced from a dedicated `*.py` file"*.
> 
> Likely, should work for you, unless you do something unusual. But check the status in the [`pyproject-toml-version` package](https://github.com/Lex-DRL/pyproject-toml-version) which actually implements version extraction.

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

    - name: "Extract version 🔢"
      # Internally, it sets up python and uses pip for its dependencies
      id: extract-version
      uses: Lex-DRL/pyproject-toml-version-action@v1
      # with:
      #   # What file to read version from:
      #   toml-file: 'pyproject.toml'
      #   # If dynamic version is used along with any Fallback backend, what field to read for the dynamic-version-file path from your "*.toml":
      #   dynamic-field: 'tool.my-backend.version.dynamic_path'
      #   # What python version to install:
      #   python-version: '3.x'
      #   # Skip python installation, if already done by previous steps:
      #   skip-python-setup: false

      # It outputs only one value: 'version'
      # Use later in the same job with:
      # ${{ steps.<ID OF THIS STEP - as set above 👆🏻>.outputs.version }}

    - name: "Example use"
      # Here, we just print the output,
      # but feel free to pas it to an actual useful step: 
      run: |
        echo 'Extracted version: ${{ steps.extract-version.outputs.version }}'
```
