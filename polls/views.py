from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from polls.models import Question, Choice


# Create your views here.

def index(request):
    last_five_questions = Question.objects.order_by('pub_date')[:5]
    printable_questions_string = ', '.join(q.question_text for q in last_five_questions)
    index_template = loader.get_template('polls/index.html')
    context = {
        'last_five_questions': last_five_questions
    }
    return HttpResponse(render(request, 'polls/index.html', context))


def detail(request, question_id):
    context = {
        'question': get_object_or_404(Question, pk=question_id)
    }
    return HttpResponse(render(request, 'polls/details.html', context))


def result(request, question_id):
    return HttpResponse('You are looking at results of question ' + str(question_id))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You did not select a choice",
        }
        return render(request, 'polls/details.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponse('Vote Successfully Registered. Thank you!')
