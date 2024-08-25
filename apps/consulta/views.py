from django.shortcuts import render, get_object_or_404, redirect
from .models import ConsultaNutricionista
from .forms import ConsultaNutricionistaForm

def lista_consultas(request):
    consultas = ConsultaNutricionista.objects.all()
    return render(request, 'lista_consultas.html', {'consultas': consultas})

def detalhe_consulta(request, pk):
    consulta = get_object_or_404(ConsultaNutricionista, pk=pk)
    return render(request, 'detalhe_consulta.html', {'consulta': consulta})

def criar_consulta(request):
    if request.method == "POST":
        form = ConsultaNutricionistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaNutricionistaForm()
    return render(request, 'criar_consulta.html', {'form': form})

def atualizar_consulta(request, pk):
    consulta = get_object_or_404(ConsultaNutricionista, pk=pk)
    if request.method == "POST":
        form = ConsultaNutricionistaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('detalhe_consulta', pk=consulta.pk)
    else:
        form = ConsultaNutricionistaForm(instance=consulta)
    return render(request, 'atualizar_consulta.html', {'form': form})

def excluir_consulta(request, pk):
    consulta = get_object_or_404(ConsultaNutricionista, pk=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect('lista_consultas')
    return render(request, 'excluir_consulta.html', {'consulta': consulta})