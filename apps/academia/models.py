from django.db import models


class AlunoAcademia(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    data_de_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    SEXO_CHOICES = (      
                  
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    mensalidade_paga = models.BooleanField(default=True, help_text="Indica se a mensalidade do aluno está paga ou não.")
   
    
    def __str__(self):
        return self.nome