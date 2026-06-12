cd "$(dirname "$0")"

# Creating directory 
mkdir -p src

# Creating files
touch src/__init__.py
touch src/helper.py 
touch src/prompt.py

touch app.py 
touch requirements.txt
touch README.md
touch pyproject.toml


echo "Directory and files created successfully!."