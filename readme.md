# If you do NOT use a virtual environment, all installed Python packages (Django, DRF, Pillow, etc.) are installed globally for that Python installation.

# Where you see them depends on your OS and how Python is installed.

# Since you are not using a virtual environment:

❌ Package version conflicts can happen
❌ Upgrading Django may break other projects
❌ Hard to reproduce environment on server

""#
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Linux/Mac
source venv/Scripts/activate # Windows bash
deactivate # Windows bash
python -m pip install --upgrade pip
pip install -r ./requirements.txt

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py populate_db
//GraphvizOnline
python ./manage.py graph_models api > models.dot

# Simple JWT can be installed with pip

# see the documentation https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html

pip install djangorestframework-simplejwt

# Documenting your API

# see the documentation https://github.com/tfranzel/drf-spectacular/

pip install drf-spectacular
python manage.py spectacular --color --file schema.yml

### Optimization query

# see the documentation https://github.com/jazzband/django-silk

pip install django-silk

# see the documentation https://django-filter.readthedocs.io/en/latest/guide/usage.html

pip install django-filter

# To apply silk would be apply to model

python ./manage.py migrate

# To create supper admin

python manage.py createsuperuser

# Username: superuser

# Email address: super@gmail.com

# My git repository

echo "# rest-freamework" >> README.md
git init
git add README.md
git commit -m "init"
git branch -M main
git remote add origin https://github.com/samirbiswas47/rest-freamework.git
git push -u origin main

# or push an existing repository from the command line

git remote add origin https://github.com/samirbiswas47/rest-freamework.git
git branch -M main
git push -u origin main

git config user.name && git config user.email
git log --format="%an <%ae>" -5

git config user.name "samirbiswas47"
git commit --amend --author="samirbiswas47 <samir@gmail.com>" --no-edit
git push --force

### Topic
