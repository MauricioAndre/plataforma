from django.shortcuts import render
from .models import xmlfile
from .email_utils import send_xml_email
from django.http.response import HttpResponse
import os
from django.conf import settings

def upload_xml(request):
    if request.method == 'POST':
        xml_file = request.FILES['xml_file']

        user_id = "LEBES135"  #aqui vai algum dado da sessao do usuario
        file_name = f"{user_id}_{os.path.basename(xml_file.name)}"
        xml_file.name = file_name

        
        saved_xml_file = xmlfile.objects.create(file=xml_file)
        xml_file_path = os.path.join(settings.MEDIA_ROOT, saved_xml_file.file.name)

        send_xml_email(xml_file_path)


        return HttpResponse("XML enviado com sucesso!") 

    return render(request, 'upload_xml.html')
