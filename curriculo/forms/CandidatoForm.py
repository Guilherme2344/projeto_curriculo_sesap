from curriculo.forms import *

def validar_tamanho_arquivo(arquivo):
    max_tamanho = 1 * 1024 * 1024
    if arquivo.size > max_tamanho:
        raise forms.ValidationError("O arquivo enviado excede o tamanho máximo permitido de 1MB.")

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = [
            'nome', 'email', 'telefone', 'cargo_desejado', 'escolaridade', 'observacoes', 'arquivo_curriculo'
        ]

    arquivo_curriculo = forms.FileField(
        validators=[
            validar_tamanho_arquivo,
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
