mkdir django
cd django
python -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject %1-app .
