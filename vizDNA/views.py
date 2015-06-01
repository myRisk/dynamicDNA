#!/usr/bin/python
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import subprocess
import os

# TOOD: helper/functions file
def append_risk(request, paramName):
    print request.POST[paramName];
    if (request.POST[paramName]!= ""):
        request.session['risk_data'].append(int(request.POST[paramName]))
        request.session.modified = True
        print request.session['risk_data']
    else:
        return HttpResponse("Please make a selection")
    

# Calculate risk from currentAge until 90 yrs
def riskCalc(var):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    filename = path + "\\NCI.DCEG.BCRA.ConsoleSample.exe"
    outFile = path + "\\riskCalc.txt"
    
    subprocess.call([filename, outFile, str(var[0]), str(var[1]), str(var[2]), str(var[3]), str(var[4]), str(var[5]), str(var[6]), str(var[7])])
    print "RISK CALC DONE"


# get 5 yr risk from riskCalc.txt
def get5YearRisk():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    filename = path + "\\riskCalc.txt"
    
    with open(filename) as fh: 
        yourRisk = fh.readline()
        popRisk = fh.readline()
    return [float(yourRisk), float(popRisk)]

# gets the user's risk at age 90
def getTerminalRisk():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    filename = path + "\\riskCalc.txt"
    yourRisk = 0.0
    popRisk = 0.0

    with open(filename) as fh:
        while True:
            line = fh.readline()
            if not line: break
            yourRisk = popRisk
            popRisk = line
    return [float(yourRisk), float(popRisk)]

def get_risk_result(counselorInput):
    # TODO: pass results array to algo
    # return array of doubles for template consumption
    return [0.2, 0.5]



# Create views here # 
# def viewname(request): creates the views 
def index(request):
    context_dict = {'boldmessage': "Stay Strong"}
    return render(request, 'index.html', context_dict)

def about(request):
    context_about = {'boldmessage': "Stay Strong"}
    return render(request, 'about.html', context_about)

def contact(request):
    context_contact = {'boldmessage': "Genetic Counselors and BioInformaticists"}
    return render(request, 'contact.html', context_contact)

def risk(request):
    request.session['risk_data'] = []

    return render(request, 'risk.html',)

def risk2(request):
    if request.method == 'POST':
        append_risk(request, 'currentAge')

    return render(request, 'risk2.html',)

def risk3(request):
    if request.method == 'POST':
        append_risk(request, 'menarcheAge')

    return render(request, 'risk3.html',)

def risk4(request):
    if request.method == 'POST':
        append_risk(request, 'firstLiveBirthAge')

    return render(request, 'risk4.html',)

def risk5(request):
    if request.method == 'POST':
        append_risk(request, 'firstDegreeRel')

    return render(request, 'risk5.html',)

def risk6(request):
    if request.method == 'POST':
        append_risk(request, 'risk5')

    return render(request, 'risk6.html',)

def risk7(request):
    if request.method == 'POST':
        append_risk(request, 'numBiopsy')

    return render(request, 'risk7.html',)

def risk8(request):
    if request.method == 'POST':
        append_risk(request, 'risk7')

    return render(request, 'risk8.html',)

def viz1(request):
    counselor_input = request.session['risk_data']
    results = get5YearRisk()
    results2 = getTerminalRisk()
    yourRisk = float(results[0]);
    popRisk = float(results[1]);
    age = request.session['risk_data'][0];

    risk_result_dict = {'you': yourRisk, 'pop': popRisk, 'you90': results2[0], 'pop90': results2[1], 'age': age}
    return render(request, 'viz1.html', risk_result_dict)

def viz2(request):
    counselor_input = request.session['risk_data']
   ###################################################################FIX
    results = get5YearRisk()
    results2 = getTerminalRisk()

    yourRisk = float(results[0]);
    popRisk = float(results[1]);
    print request.session['risk_data'][0];
    age = request.session['risk_data'][0];

    risk_result_dict = {'you': yourRisk, 'pop': popRisk, 'you90': results2[0], 'pop90': results2[1], 'age': age}
    return render(request, 'viz2.html', risk_result_dict)

def viz3(request):
    if request.method == 'POST':
        append_risk(request, 'race')
        counselor_input = request.session['risk_data']
        riskCalc(counselor_input)

        results = get5YearRisk()
        results2 = getTerminalRisk()
        age = request.session['risk_data'][0];
        print request.session['risk_data'][0];

        
    risk_result_dict = {'you': results[0], 'pop': results[1], 'you90': results2[0], 'pop90': results2[1], 'age': age}
    return render(request, 'viz3.html', risk_result_dict)

def feedback(request):
    context_about = {'boldmessage': "Stay Strong"}
    return render(request, 'feedback.html', context_about)
