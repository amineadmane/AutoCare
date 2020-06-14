# AutoCare
Installation Steps :\
if you already cloned this repo localy :\
git pull origin master\
else:\
cd Desktop/\
git clone https://github.com/amineadmane/AutoCare.git\
\
then : ____________________________\
pip3 install -r requirements.txt\
Create postgres Database : "autocare"\
python3 manage.py makemigrations\
python3 manage.py migrate\
python3 manage.py createsuperuser\
