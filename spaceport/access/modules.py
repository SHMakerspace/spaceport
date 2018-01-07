import after_response
import paho.mqtt.client as mqtt
from access.models import AccessLog, SecurityNode
from django.utils import timezone
from datetime import datetime
import json


def LogAccessRequest(User, NodeID):
    try:
        # Exit
        Log = AccessLog.objects.get(User=User, Node_id=NodeID, Out__isnull=True)
        Log.Out = timezone.now()
        Log.save()

        Node = SecurityNode.objects.get(id=NodeID)
        # Site is closing
        if Node.Site_Open and not AccessLog.objects.filter(Node_id=NodeID, Out__isnull=True):
            MqttHandler(User, Node, "Exit", SiteClose=True)
        else:
            MqttHandler(User, Node, "Exit")
    except:
        # Entry
        Node = SecurityNode.objects.get(id=NodeID)
        if Node.Site_Open and not AccessLog.objects.filter(Node_id=NodeID, Out__isnull=True):
            MqttHandler(User, Node, "Enter", SiteOpen=True)
        else:
            MqttHandler(User, Node, "Enter")
        AccessLog.objects.create(User=User, Node_id=NodeID, In=timezone.now())



def MqttHandler(User, Node, Direction, SiteOpen=False, SiteClose=False, Misc=None, NonRequest=False):
    host, topic = Node.ReturnMqttParams()
    if host and topic:
        payload = ReturnAccessJson(User, Node, Direction, SiteOpen, SiteClose, Misc)
        if NonRequest:
            MqttPublish(host, topic, payload)
        else:
            MqttPublish.after_response(host, topic, payload)

def ReturnAccessJson(User, Node, Direction, SiteOpen=False ,SiteClose=False, Misc=None):
    data = {"user": User.username, "Node": Node.Name, "NodeID": Node.id, "Direction": Direction, "DateTime": datetime.now().isoformat()}
    if SiteOpen:
        data["SiteStatus"] = "Open"
    elif SiteClose:
        data["SiteStatus"] = "Closed"
    else:
        data["SiteStatus"] = "Null"
    if Misc:
        data["Misc"] = Misc
    else:
        data["Misc"] = "Null"
    return json.dumps(data)

@after_response.enable
def MqttPublish(host, topic, data):
    client = mqtt.Client()
    client.connect(host)
    client.publish(topic, data)
    client.disconnect()
