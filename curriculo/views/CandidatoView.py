from curriculo.models import Candidato
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def inserir_curriculo(request, id=None):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        cargo_desejado = request.POST.get("cargo_desejado")
        escolaridade = request.POST.get("escolaridade")
        observacoes = request.POST.get("observacoes")
        arquivo = request.POST.get("arquivo")
        ip = request.POST.get("ip")
        data_hora_envio = request.POST.get("data_hora_envio")
        try:
            obj_candidato = Candidato()
            obj_candidato.nome = nome
            obj_candidato.email = email
            obj_candidato.telefone = telefone
            obj_candidato.cargo_desejado = cargo_desejado
            obj_candidato.escolaridade = escolaridade
            obj_candidato.observacoes = observacoes
            obj_candidato.ip = ip
            obj_candidato.data_hora_envio = data_hora_envio
            if request.FILES is not None:
                num_files = len(request.FILES.getlist('arquivo'))
                if num_files > 0:
                    arquivo = request.FILES['arquivo']
                    fs = FileSystemStorage()
                    nome_arquivo = fs.save(arquivo.name, arquivo)
                    if nome_arquivo is not None and nome_arquivo != "":
                        obj_candidato.arquivo = nome_arquivo
            obj_candidato.save()
            print(f"Candidato {nome} inserido com sucesso!")
        except Exception:
            print(f"Erro ao inserir o candidato")
        return redirect("/curriculo")
    return render(request, template_name="enviar-curriculo.html")