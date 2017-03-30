from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Request, Analyst, Database, Stakeholder

def index(req):
    latest_request_list = Request.objects.order_by('-date_created')[:5]
    context = {'latest_request_list': latest_request_list}
    return render(req, 'reqman/index.html', context)

def detail(req, request_id):
    request = get_object_or_404(Request, pk = request_id)
    return render(req, 'reqman/detail.html', {'request': request})

def analyst(req, analyst_id):
    request = get_object_or_404(Analyst, pk = analyst_id)
    return render(req, 'reqman/analyst.html', {'analyst': request})

def analyst_list(req):
    analyst_list = Analyst.objects.all()
    context = {'analyst_list': analyst_list}
    return render(req, 'reqman/analyst_list.html', context)

def db(req, db_id):
    request = get_object_or_404(Database, pk = db_id)
    return render(req, 'reqman/db.html', {'db': request})

def db_list(req):
    db_list = Database.objects.all()
    context = {'db_list': db_list}
    return render(req, 'reqman/db_list.html', context)

def stake(req, stake_id):
    request = get_object_or_404(Stakeholder, pk = stake_id)
    return render(req, 'reqman/stake.html', {'stake': request})

def stake_list(req):
    stake_list = Stakeholder.objects.all()
    context = {'stake_list': stake_list}
    return render(req, 'reqman/stake_list.html', context)
