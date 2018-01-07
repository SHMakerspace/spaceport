# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from access.models import Tag, AccessLog
from modules import *
import logging
logger = logging.getLogger(__name__)


#def error404(request):
 #   return render(request, '404.html')

def index(request):
    return render(request, 'index.html')

class AccessRequest(APIView):
    """
    Determines if a user has access to a node.
    """
    def get(self, request, node, uuid):
        User = Tag.ReturnUserOrNone(uuid)
        if User:
            result = User.AllowedAccess(node) and User.is_active
            username = User.username
        else:
            result = False
            username = "none"

        if result:
            LogAccessRequest(User, node)

        logger.info([{"user": username, "uuid": uuid, "result": result, "node": node}])

        return Response([{"user": username, "uuid": uuid, "result": result}])


class ValidateAdmin(APIView):
    """
    Determines if a user is 'admin' (staff)
    """
    def get(self, request, uuid):
        User = Tag.ReturnUserOrNone(uuid)
        if User:
            result = User.is_staff and User.is_active
            username = User.username
        else:
            result = False
            username = "none"
        logger.info([{"user": username, "uuid": uuid, "result": result,}])
        return Response([{"user": username, "uuid": uuid, "result": result}])


class RegisterTag(APIView):
    """
    Registers a new tag ready to assign to a user
    """

    def get(self, request, uuid):
        obj, created = Tag.objects.get_or_create(Uuid=uuid)
        #Implement debug log write
        return Response([{"user": "none", "uuid": uuid, "result": created}])


class ApiCatchAll(APIView):
    """
    Catch all API response
    """

    def get(self, request,):
        return Response([{"data": "API endpoint not found", "result": "False"}])
