from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    polls = Poll.objects.all()
    context = {'polls' : polls}
    return render(request,'poll/home.html',context)

def create_view(request, *args, **kwargs):
    if request.method=="POST":
        form = CreatePollForm(request.POST)
        if form.is_valid:
            form.save()
            print('form saved')
            return redirect('home')
        else:
            print("FOrm Failed")
    else:
        form = CreatePollForm()
        context = {'form' : form}
        return render(request,'poll/create.html',context)

def vote_view(request, poll_id,*args, **kwargs):
    poll_instance = Poll.objects.get(pk=poll_id)
    if request.method == "POST":
        selected_option = request.POST['poll']
        if selected_option=='option1':
            poll_instance.option1count+=1
        elif selected_option=='option2':
            poll_instance.option2count+=1
        elif selected_option=='option3':
            poll_instance.option3count+=1
        else:
            return HttpResponse(400, "Invalid Form")
        poll_instance.save()
        print('saved')
        return redirect('home')

    context = {'poll_instance' : poll_instance}
    return render(request,'poll/vote.html',context)

def results_view(request, poll_id,*args, **kwargs):
    poll_instance = Poll.objects.get(pk=poll_id)
    context = {'poll_instance' : poll_instance}
    return render(request,'poll/results.html',context)
    
def delete_view(request,poll_id,*args,**kwargs):
    poll_instance = Poll.objects.get(pk=poll_id)
    poll_instance.delete()
    return redirect('home')