from django.shortcuts import render

# Create your views here.
from .models import Agent

def agents_list(request):
    agents_list = Agent.objects.all()
    template = 'agents/agents.html'
    context = {
        'agent_list' : agents_list,
    }

    return render(request, template, context)