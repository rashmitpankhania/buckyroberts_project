from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import Userform
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Album


class IndexView(generic.ListView):
    model = Album
    template_name = 'index.html'


class DetailsView(generic.DetailView):
    model = Album
    template_name = 'details.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'logo']
    template_name = 'album_form.html'


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'logo']
    template_name = 'album_form.html'


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = Userform  # what type of form u want to use
    template_name = 'templates/registration_form.html'
    # disp-lay blank form

    def get(self, request):
        form = self.form_class(None)
        return render(request,'registration_form.html',{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned normalized the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, 'registration_form.html', {'form': form})
