from django.shortcuts import render
from .models import xmlfile
from django.http.response import HttpResponse

def upload_xml(request):
    if request.method == 'POST':
        xml_file = request.FILES['xml_file']
        xmlfile.objects.create(file=xml_file)
        return HttpResponse("XML enviado com sucesso!") 

    return render(request, 'upload_xml.html')
