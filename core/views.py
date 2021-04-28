from django.shortcuts import render
from django.views.generic import TemplateView
import uuid
import pyperclip


def handleListToClipboard(uuids):
    listString = ''
    for item in uuids:
        listString += str(item) + '\n'
    
    return listString


class IndexView(TemplateView):
    template_name = "core/index.html"
    title = "Gerador de UUID 4"
    
    list_uuid = []
    count = 0

    while count < 20:
        list_uuid.append(uuid.uuid4())
        count += 1
    
    pyperclip.copy(handleListToClipboard(list_uuid))
    
