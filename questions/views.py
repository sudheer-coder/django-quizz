from datetime import datetime, timezone

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Test, Results, Time
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def questionview(request,id):
    qid = int(id)+1
    question = Test.objects.get(pk=qid)
    return render(request,'questions/question.html',{"question":question})

def checkanswer(request):
    resultofquestion = ""
    marks=0
    id = request.POST['qid']
    userid = request.session.get('userid')
    question = Test.objects.get(pk=id)
    user = User.objects.get(pk=userid)
    ans = request.POST['name']
    if question.answer == ans:
        resultofquestion="correct"
        marks=10
    else:
        resultofquestion="incorrect"
    result = Results(user=user,questions=question,scores=marks,resultofquestion=resultofquestion)
    result.save()
    return HttpResponse("hi")

def finishquizz(request):
    userid = request.session.get('userid')
    timeid = request.session.get('timeid')
    timebefore = Time.objects.get(pk=timeid)
    results = Results.objects.all()
    score=0
    correct = 0
    incorrect = 0
    max=0
    timenow = datetime.now(timezone.utc)
    for results in results:
        if results.user.id == userid and max < 10:
            score = score+results.scores
            if results.resultofquestion == 'correct':
                correct = correct+1
            else:
                incorrect = incorrect+1
            max=max+1
    timebefore = timebefore.time
    duration = timenow-timebefore
    if score >= 50:
        status = "yay! passed"
    else:
        status = "oops! failed"
    context = {
        "scores":score,
        "correct":correct,
        "incorrect":incorrect,
        "duration":duration,
        "status":status
    }
    del request.session['userid']
    del request.session['timeid']
    logout(request)
    return render(request,"questions/Results.html",{"context":context})
