from django.contrib import messages
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice, Customer

from django.template import loader




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def formsubmit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        selectedata = Customer()
        selectedata.name = request.POST['name']
        selectedata.email = request.POST['email']
        selectedata.contact = request.POST['contact']
        try:
            selectedata.save()
        except Exception:
            messages.info(request, 'You\'ll be contacted shortly')
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:index'))


def displayCustomer(request):
    customer = Customer.objects.all()
    context = {'customer': customer}
    return render(request, 'polls/forms.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})