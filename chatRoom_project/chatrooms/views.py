from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,View,CreateView,DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SginupForm

from .models import Room,Message
# Create your views here.
# def index(request):
#     return render(request,'index.html',{})
class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request,"Welcome Back😊")
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request, 'Invalid username or password. Please try again.')
            else:
                messages.error(request, 'Form i s not valid. Please check the input.')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
     

class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SginupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request,'Account Created Sucessfully✨.')
        return super().form_valid(form)

    def form_invalid(self, form):
        if 'username' in form.errors:
            username_error= form.errors['username'][0]
            messages.error(self.request,username_error)
        elif 'password2' in form.errors:
            passwords_error = form.errors['password2'][0]
            messages.error(self.request,passwords_error)
        else:
            messages.error(self.request,'Error creating account. Please check your input.')
        return super().form_invalid(form)
    

    

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['rooms'] = Room.objects.all()
        return context




class CreateRoomView(View):
    
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            room_name = request.POST['room_name']
            new_room = Room.objects.create(name=room_name,owner=self.request.user,is_group=True)
            new_room.save()
            messages.success(request,'New Room Added ')
            return HttpResponseRedirect(reverse('home'))
        return render(request,'home.html')


class ChatRoomView(DetailView):
    model= Room
    template_name='chat_room.html'
    context_object_name = 'room'

    def get_object(self,queryset=None):

        return Room.objects.get(room_name_id=self.kwargs['room_name'])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        room = Room.objects.get(room_name_id=self.kwargs['room_name'])  
        context['room_messages'] = Message.objects.filter(room=room)
        return context
