from django.shortcuts import render, get_object_or_404, redirect
from .models import Music
from django.utils import timezone


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def hobby(request):
    return render(request, 'hobby.html')

def movie(request):
    return render(request, 'movie.html')

def music(request):
    musics= Music.objects.all()
    return render(request,'music.html',{'musics':musics})

def photo(request):
    return render(request, 'photo.html')

def detail(request, id):
    music= get_object_or_404(Music, pk=id)
    return render(request, 'detail.html',{'music':music})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_music= Music()
    new_music.title=request.POST['title']
    new_music.writer=request.POST['writer']
    new_music.body=request.POST['body']
    new_music.pub_date= timezone.now()
    new_music.save()
    return redirect('detail',new_music.id)

def edit(request, id):
    edit_music= Music.objects.get(id=id)
    return render(request, 'edit.html', {'music':edit_music})

def update(request, id):
    update_music=Music.objects.get(id=id)
    update_music.title=request.POST['title']
    update_music.writer=request.POST['writer']
    update_music.body=request.POST['body']
    update_music.pub_date= timezone.now()
    update_music.save()
    return redirect('detail', update_music.id)

def delete(request, id):
    delete_music=Music.objects.get(id=id)
    delete_music.delete()
    return redirect('home')