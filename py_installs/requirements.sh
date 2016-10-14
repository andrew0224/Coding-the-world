
#Install a virtual environment
tar xvfz virtualenv-1.9.tar.gz
cd virtualenv-1.9
python virtualenv.py ../../venv

#Clear the installation trace
cd ../
rm -rf virtualenv-1.9

#Activate the virtual env
cd ../venv/bin/
source activate.csh

#Install other libraries
pip install Werkzeug
pip install Jinja2
pip install Flask
pip install XlsxWriter

pip install gunicorn
pip install greenlet # Required for both
pip install eventlet # For eventlet workers
pip install gevent # For gevent workers

