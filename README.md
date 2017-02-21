# SimpleBlog

ASSUMPTIONS:
------------
We are assuming that you have installed higher than or python2.7 version already, runnning on Windows/Linux.
Note: We have tested this application with windows/linux.

INSTALLATION:
-------------
Follow the below steps to configure the application.
1. pip install virtualenv

2. virtualenv \<env\>

3. cd \<env\>

4. for Linux: run source bin/activate

   for windows: run Scripts/activate.bat

5. pip install --upgrade pip

6. git clone https://github.com/rparthiban/SimpleBlog.git

7. cd SimpleBlog

8. pip install -r requirements.txt


USAGE:
------
1. To activate your blog model, run

	python manage.py makemigrations

2. To construct your blog model, run

	python manage.py migrate

3. To setup admin account, run below command and fill its expectations

	python manage.py createsuperuser

4. To startup the dev server

	python manage.py runserver \<port\>

NAVIGATION:
-----------
1.For anonymous user you can navigate the below url

	http://localhost:<port>/

2.For admin, you can navigate the below url

	http://localhost:<port>/admin
