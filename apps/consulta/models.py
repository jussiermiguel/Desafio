from django.db import models


# Modelo para representar consultas com nutricionista
class ConsultaNutricionista(models.Model):
     # Relacionamento com o modelo Aluno
    alunos = models.ForeignKey('academia.AlunoAcademia',on_delete=models.CASCADE, related_name='consultas')
    cpf = models.CharField(max_length=14, unique=True)
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    data_de_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_consultas = models.PositiveIntegerField()
    retorno = models.DateField()

    def __str__(self):
        return self.alunos.nome