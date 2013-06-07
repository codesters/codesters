#Installation Instructions

*Make sure you have Python2.7.3, virtualenv, pip and sqlite3 installed*

1. Download or clone this repo.
2. Go to project home folder and run these commands:

    cp codesters/example_local.py codesters/local_settings.py
    virtualenv venv
    source venv/bin/activate

3. This will create a virtual environment and activate it. Now use pip to install dependencies with:

    pip install -r dev-requirements.txt

4. Now we have to prepare a database:

    python manage.py syncdb

5. It will ask you to provide username, email and password. Give them and run following migrations:

    python manage.py migrate guardian
    python manage.py migrate resources
    python manage.py migrate profiles

5. Run django server and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

6. Create Resource Types named Book, Ebook, Tutorial, Online Course, Other.

7. Go to home page.
