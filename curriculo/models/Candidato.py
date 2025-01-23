from curriculo.models import *

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cargo_desejado = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=50)
    observacoes = models.CharField(max_length=300, blank=True, null=True)
    arquivo = models.FileField(
        upload_to="curriculos/",
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
        ]
    )
    ip = models.GenericIPAddressField()
    data_hora_envio = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.nome}"