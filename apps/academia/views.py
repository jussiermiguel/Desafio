from django.shortcuts import render, get_object_or_404, redirect
from .models import AlunoAcademia
from .forms import AlunoAcademiaForm

def lista_alunos(request):
    alunos = AlunoAcademia.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def detalhe_aluno(request, pk):
    aluno = get_object_or_404(AlunoAcademia, pk=pk)
    return render(request, 'detalhe_aluno.html', {'aluno': aluno})

def criar_aluno(request):
    if request.method == "POST":
        form = AlunoAcademiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoAcademiaForm()
    return render(request, 'criar_aluno.html', {'form': form})

def atualizar_aluno(request, pk):
    aluno = get_object_or_404(AlunoAcademia, pk=pk)
    if request.method == "POST":
        form = AlunoAcademiaForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('detalhe_aluno', pk=aluno.pk)
    else:
        form = AlunoAcademiaForm(instance=aluno)
    return render(request, 'atualizar_aluno.html', {'form': form})

def excluir_aluno(request, pk):
    aluno = get_object_or_404(AlunoAcademia, pk=pk)
    if request.method == "POST":
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'excluir_aluno.html', {'aluno': aluno})
