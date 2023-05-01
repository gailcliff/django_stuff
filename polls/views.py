from django.http import HttpResponse

from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Question, Note

import json


def home(request):
    now = timezone.now()
    return HttpResponse("Awoo! Welcome to the Polls! <br>"
                        f"Today's date and time is: {now} <br>"
                        f"7 days ago it was:  {now - timezone.timedelta(weeks=1)} <br>"
                        f"7 days from now it will be:  {now + timezone.timedelta(weeks=1)}")


def get_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(question)


@csrf_exempt
def cliffnotes(request):
    response = {}

    if request.method == 'POST':
        json_dat = json.loads(request.body)

        new_note = Note(
            note=json_dat['note'],
            time=json_dat['time'],
            date=json_dat['date']
        )
        new_note.save()
        note_id = new_note.id

        response = {
            "note_id": note_id
        }
    elif request.method == 'GET':
        notes = Note.objects.all()

        notes = [
            {
                'id': note.id,
                'note': note.note,
                'time': note.time,
                'date': note.date
            } for note in notes
        ]
        notes.reverse()
        response = {
            "notes": notes
        }

    return HttpResponse(json.dumps(response))

@csrf_exempt
def fuud(request):
    return HttpResponse(request.body)


def foo(request, limit):
    arr = []
    for i in range(limit):
        arr.append(i * i)

    return HttpResponse(arr)