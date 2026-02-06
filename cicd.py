def generate_ci():
    ci_yaml = '''
name: CI Pipeline


on:
  push:
    branches: [ "main" ]


jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install fastapi uvicorn
    - name: Run tests
      run: echo "No tests yet"
'''


    with open("output/.github/workflows/ci.yml", "w") as f:
        f.write(ci_yaml)


    return "output/.github/workflows/ci.yml"