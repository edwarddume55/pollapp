from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from.models import Question,Choice
from django.contrib import messages

from django.db.models import Sum

#getting all the questions and displaying them
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html',context)

#show specific question and coices of the question
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    total_votes = question.choice_set.aggregate(Sum('votes'))['votes__sum'] or 1  # To avoid division by zero
    choices = question.choice_set.all()

    # for choice in choices:
    #     choice.votes_percentage = (choice.votes / total_votes) * 100
    #     print(f"Choice: {choice.choice_text}, Votes: {choice.votes}, Percentage: {choice.votes_percentage}")

    # print(f"Total Votes: {total_votes}")

    return render(request, 'polls/detail.html', {'question': question, 'choices': choices, 'total_votes': total_votes})
# def detail(request, question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request,'polls/detail.html',{'question':question})

#get question and display results on that question
# def results(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
def results(request):
    # Retrieve all questions from the database
    all_questions = Question.objects.all()

    # You can pass the queryset directly to the template
    return render(request, 'polls/results.html', {'questions': all_questions})

# Vote for a question choice
def vote(request, question_id):

    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        messages.success(request, 'Vote added successfully!')
        return HttpResponseRedirect(reverse('polls:detail', args =(question.id, )))
        

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)

#     # Check if the user has already voted for this question
#     if 'has_voted' in request.session and request.session['has_voted']:
#         messages.error(request, "You've already voted for this question.")
#         return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form with an error message
#         messages.error(request, "You didn't select a choice.")
#         return render(request, 'polls/detail.html', {'question': question})

#     # Update the selected choice's votes
#     selected_choice.votes += 1
#     selected_choice.save()

#     # Mark that the user has voted in the session
#     request.session['has_voted'] = True
#     request.session.save()

#     # Display a success message
#     messages.success(request, 'Vote added successfully!')

#     # Redirect to the detail page
#     return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))