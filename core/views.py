from django.shortcuts import render
from django.views.generic import TemplateView
import uuid


class IndexView(TemplateView):
    template_name = "core/index.html"
    title = "Gerador de UUID 4"
    
    list_uuid = []
    count = 0

    while count < 200:
        list_uuid.append(uuid.uuid4())
        count += 1
    
