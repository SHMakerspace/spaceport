
from django.core.management.base import BaseCommand
from django.utils import timezone

from access.models import AccessLog
from access.modules import *

class Command(BaseCommand):

    help = 'Logs all currently logged in users out.'

    def handle(self, *args, **options):

        Logs = AccessLog.objects.filter(Out__isnull=True)

        for Log in Logs:
            print "loopy"
            MqttHandler(Log.User, Log.Node, "Exit", SiteClose=True, Misc="Naughty", NonRequest=True)

        Logs.update(Out=timezone.now(), Force_Out=True)

