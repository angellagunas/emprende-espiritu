# emprende-espiritu

correr proyecto en c9:
	python manage.py runserver $IP:$PORT

correr celery en c9:
	python manage.py celery worker 

requerimientos:
    *pip install django-localflavor
    *pip install django_compressor
    *pip install -e git+http://github.com/SmileyChris/django-mailer-2.git#egg=django-mailer-2
    *pip install django-celery

    //Install celery broker
    wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
    sudo apt-key add rabbitmq-signing-key-public.asc
    sudo apt-get install rabbitmq-server