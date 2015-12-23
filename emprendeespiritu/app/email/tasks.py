# -*- coding: utf-8 -*-
import datetime

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from celery import shared_task, task


def send_mail_from_page(fullname, email, msg):
    """
    change when use Mandrill

        merge_vars = {}
        merge_vars[email] = {
            'FNAME': fullname,
            'EMAIL': email,
            'MSG':msg
        }
        msg = EmailMessage(to=['angel.david.lagunas@gmail.com'])
        msg.template_name = 'solicitud_informacion'
        msg.merge_vars = merge_vars
        msg.send()
    """
    plaintext = get_template('email/email.txt')
    htmly = get_template('email/email.html')

    d = Context({'fullname': fullname, 'email': email, 'msg': msg})

    subject = 'Mensaje de la pagina'
    from_email = email
    to = ['pruebas.emprende.espiritu@gmail.com']
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_weekly_courses(recipients):
    plaintext = get_template('email/daily_invitation.txt')
    htmly = get_template('email/daily_invitation.html')

    subject = 'Mensaje de la pagina'
    from_email = email
    text_content = plaintext.render()
    html_content = htmly.render()
    msg = EmailMultiAlternatives(subject, text_content, from_email, recipients)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

# Celery tasks


@task
def send_mail(fullname, email, msg):
    """
        the user request info
    """
    send_mail_from_page(fullname, email, msg)


@task
def send_daily_mails():
    """
    send weekly courses to email
    """
    print('HEEEEEEEEEEEEEEREEEEEEEEEEEEEEEE')
    recipients = ['angel.david.lagunas@gmail.com', 'al@vincoorbis.com', 'emprendetuespiritu@gmail.com ']
    send_weekly_courses(recipients)
