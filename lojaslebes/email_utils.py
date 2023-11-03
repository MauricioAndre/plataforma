from django.core.mail import EmailMessage
import os

def send_xml_email(xml_file_path):
    subject = "Arquivo XML da Nota Fiscal"
    from_email = "intechlog@intechlog.com.br"
    to_email = ["jonatan.rosario@intechlog.com.br"]
    
    email = EmailMessage(subject, 'Segue o xml em anexo.', from_email, to_email)
    
    # Anexar o arquivo XML
    with open(xml_file_path, 'rb') as xml_file:
        email.attach(os.path.basename(xml_file_path), xml_file.read(), 'application/xml')
    
    email.send()