# -*- coding: utf-8 -*-
# Create your views here.

from newsletter.models import *
from news.models import Newslet
from newsletter.views import make_html
from django.template.loader import get_template
from django.views.generic.simple import redirect_to
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from datetime import datetime
import subprocess
import random
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
        link = "http://nspj.bydgoszcz.pl/newsletter/unsubscribe/?email="
        napis = u"Otrzymałeś ten biuletyn, ponieważ Twój ares e-mail został podany na stronie www.nspj.bydgoszcz.pl. Jeśli nie chcesz otrzymywac biuletynu, możesz usunąć swój adres, korzystając z następującego linku: "
#        adresy = Subscriber.objects.all()
        adresy = Probne.objects.all()
#        tresc_txt = Body.objects.all().order_by('sending_date').reverse()[0].text
#        tresc_html = Body.objects.all().order_by('sending_date').reverse()[0].text_html
        tresc = make_html()
        if (not tresc['unsent']):
            print "Nie ma żadnego biuletynu do wysłania"
            return 0 
        tresc_txt = tresc['txt'] 
        tresc_html = tresc['html']
        subject = u"Newsletter portalu www.nspj.bydgoszcz.pl"
        from_email = "admin@liturgia.bydgoszcz.pl"
        wszystkie = 0
        bledy = 0
        adr_bledne =""
        for a in adresy:
            cale = napis + '<a href="' + link + a.email + '">' + link + a.email + '</a>'
            txt = tresc_txt + '\n' + cale
            htm = tresc_html + '<p> </p><p>' + cale + '</p>'
            htm = '<link rel="stylesheet" type="text/css" media="screen" href="http://nspj.bydgoszcz.pl/site_media/css/style.css" />' + htm
            try:
                msg = EmailMultiAlternatives(subject, txt, from_email, [a.email,])
                msg.attach_alternative(htm, "text/html")
                msg.send()
                print "wyslano" + str(wszystkie)
                wszystkie = wszystkie + 1
            except:
                pass
                bledy = bledy+1
                adr_bledne = adr_bledne + a.email + ', '
        n = Newslet.objects.latest('date')
        n.unsent = False
        n.report = u"Wysłanych maili: " + str(wszystkie) + u", błędów: " + str(bledy) + u". Adresy dla których wystąpiły błędy: " 
        n.sent_date = datetime.now()
        n.save()
 
