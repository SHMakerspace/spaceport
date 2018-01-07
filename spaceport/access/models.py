# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone


# Create your models here.

class Tag(models.Model):
    User = models.ForeignKey(User, blank=True, null=True)
    Uuid = models.CharField(max_length=64)
    Date_Added = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def ReturnUserOrNone(Uuid):
        try:
            tag = Tag.objects.get(Uuid=Uuid)
            #Debug log - tag found
            return tag.User

        except Tag.DoesNotExist:
            # Debug log - tag not found
            return None

class SecurityNode(models.Model):
    Name = models.CharField(max_length=50)
    Group = models.ForeignKey(Group)
    Site_Open = models.BooleanField(default=False)

    def __str__(self):
        return '{} ID: {} '.format(self.Name, self.id)

    def ReturnMqttParams(self):
        return self.Group.Mqtt_Broker, self.Group.Mqtt_Topic

class AccessLog(models.Model):
    User = models.ForeignKey(User)
    Node = models.ForeignKey(SecurityNode)
    In = models.DateTimeField()
    Out = models.DateTimeField(blank=True, null=True)
    Force_Out = models.BooleanField(default=False)

class Acl(models.Model):
    user = models.OneToOneField(User)
    Allowed_Nodes = models.ManyToManyField(SecurityNode)

def AllowedAccess(self, NodeId):
    try:
        self.acl.Allowed_Nodes.get(id=NodeId)
        return True
    except SecurityNode.DoesNotExist, Acl.DoesNotExist:
        return False
User.add_to_class("AllowedAccess", AllowedAccess,)


if not hasattr(Group, 'Mqtt_Broker'):
    Mqtt_Broker = models.CharField(max_length=64, blank=True)
    Mqtt_Broker.contribute_to_class(Group, 'Mqtt_Broker')
if not hasattr(Group, 'Mqtt_Topic'):
    Mqtt_Topic = models.CharField(max_length=64, blank=True)
    Mqtt_Topic.contribute_to_class(Group, 'Mqtt_Topic')
