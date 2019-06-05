from django.shortcuts import render
from django.views.generic import TemplateView
import uuid


class IndexView(TemplateView):
    template_name = "core/index.html"
    title = "UUID Easy"
    
    list_uuid = []
    count = 0

    while count < 50:
        list_uuid.append(uuid.uuid4())
        count += 1