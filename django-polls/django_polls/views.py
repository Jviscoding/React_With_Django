from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


# ============================================================================
# Index View
# ============================================================================

def index(request):
    """
    Display the latest five published questions.
    """

    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    

    context = {
        "latest_question_list": latest_question_list,
    }

    return render(request, "polls/index.html", context)


# ============================================================================
# Detail View
# ============================================================================

def detail(request, question_id):
    """
    Display a single published question.
    """

    question = get_object_or_404(
        Question.objects.filter(pub_date__lte=timezone.now()),
        pk=question_id,
    )

    context = {
        "question": question,
    }

    return render(request, "polls/detail.html", context)


# ============================================================================
# Results View
# ============================================================================

def results(request, question_id):
    """
    Display the voting results for a question.
    """

    question = get_object_or_404(
        Question,
        pk=question_id,
    )

    context = {
        "question": question,
    }

    return render(request, "polls/results.html", context)


# ============================================================================
# Vote View
# ============================================================================

def vote(request, question_id):
    """
    Process a user's vote.
    """

    question = get_object_or_404(
        Question,
        pk=question_id,
    )

    try:

        # Same as:
        #
        # SELECT *
        # FROM choice
        # WHERE question_id = question.id;
        #
        # Django automatically creates:
        # question.choice_set

        selected_choice = question.choice_set.get(
            pk=request.POST["choice"]
        )

    except (KeyError, Choice.DoesNotExist):

        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )

    else:

        # Atomic increment
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        # Redirect to results page
        return HttpResponseRedirect(
            reverse(
                "polls:results",
                args=(question.id,),
            )
        )