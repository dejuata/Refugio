from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from app.mascota.forms import MascotaForm
from app.mascota.models import Mascota

# Create your views here.
def index(request):
    return render(request, 'mascota/index.html')
    
def listado(request):
	lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre','sexo'])
	return HttpResponse(lista, content_type='application/json')
    
def mascota_view(request):
    if request.method == 'POST':
	    form = MascotaForm(request.POST)
	    if form.is_valid():
		    form.save()
	    return redirect('mascota:mascota_list')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form':form})
    
def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)
	
def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_list')
	return render(request, 'mascota/mascota_form.html', {'form':form})
	
def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:mascota_list')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})
	
class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'
	paginate_by = 5
	
class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_list')
	
class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_list')
	
class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_list')