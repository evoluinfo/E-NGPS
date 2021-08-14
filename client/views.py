from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Seller as Client
from .form import ClientForm

def client(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Client.objects.filter(phone__icontains=search) or Client.objects.filter(company_name__icontains=search) \
                     or Client.objects.filter(cnpj__icontains=search) or Client.objects.filter(email__icontains=search)
    else:
        data['db'] = Client.objects.all()
        all =  Client.objects.all()
        paginator = Paginator(all, 5)
        pages = request.GET.get('page')
        data['db']= paginator.get_page(pages)
    data['client'] = ClientForm()
    return render(request, 'client.html', data)


def form_client(request):
    data = {}
    data['form_client'] = ClientForm()
    return render(request, 'form_client.html', data)


def create_client(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/app')


def view_client(request, pk):
    data = {}
    data['db'] = Client.objects.get(pk=pk)
    return render(request, 'view_client.html', data)


def edit_client(request, pk):
    data = {}
    data['db'] = Client.objects.get(pk=pk)
    data['form_client'] = ClientForm(instance=data['db'])
    return render(request, 'form_client.html', data)


def update_client(request, pk):
    data: dict = {}
    data['db'] = Client.objects.get(pk=pk)
    form = ClientForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/client')


def delete_client(request, pk):
        db = Client.objects.get(pk=pk)
        db.delete()
        return redirect('/client')