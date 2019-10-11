# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputForm
import run_classifier



def convert(request):
    converted = ""
    sentenceData = {}
    if request.method == 'GET':
        form = InputForm()
    else:
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            passage = form.cleaned_data['passage']
            sentenceData = run_classifier.predict(passage)



    #x = {"hi":"lib", "bo":"lib", "BRO":"con", "x":"con"}
    return render(request, 'index.html', {'sentenceData':sentenceData, 'form':form})