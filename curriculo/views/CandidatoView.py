from curriculo.models import Candidato
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.core.mail import EmailMessage

def pegar_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def inserir_curriculo(request):
    return render(request, template_name="enviar-curriculo.html",  status=200)

def curriculo_enviado(request, id=None):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        cargo_desejado = request.POST.get("cargo_desejado")
        escolaridade = request.POST.get("escolaridade")
        observacoes = request.POST.get("observacoes")
        arquivo = request.FILES.get("arquivo")
        subject = 'Recebemos seu currículo!'
        message = f"""
        Olá, {nome}!

        Obrigado por enviar seu currículo. Aqui estão os dados recebidos:
        Nome: {nome}
        E-mail: {email}
        Telefone: {telefone}
        Cargo Desejado: {cargo_desejado}
        Escolaridade: {escolaridade}
        Observações: {observacoes}

        Em breve, entraremos em contato.

        Atenciosamente,
        UGTSIC - SESAP/RN.
        """
        from_email = 'noreply@gmail.com'
        recipient_list = [email]

        try:
            email_message = EmailMessage(subject, message, from_email, recipient_list)

            if arquivo:
                email_message.attach(arquivo.name, arquivo.read(), arquivo.content_type)

            email_message.send()

            obj_candidato = Candidato(
                nome=nome,
                email=email,
                telefone=telefone,
                cargo_desejado=cargo_desejado,
                escolaridade=escolaridade,
                observacoes=observacoes,
                ip=pegar_ip(request),
                data_hora_envio=timezone.now(),
                arquivo=arquivo.name if arquivo else None
            )

            if arquivo:
                fs = FileSystemStorage()
                nome_arquivo = fs.save(arquivo.name, arquivo)
                obj_candidato.arquivo = nome_arquivo

            obj_candidato.save()

            print(f"Candidato {nome} inserido com sucesso!")

        except Exception as e:
            print(f"Erro ao processar o envio do candidato: {e}")
            return render(request, "erro-curriculo.html", status=200)

        return redirect("curriculo-enviado")

    return render(request, "curriculo-enviado.html", status=200)

def erro_curriculo(request):
    return render(request, "erro-curriculo.html", status=200)