from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from polls.models import Note

api_router = APIRouter()


class NoteModel(BaseModel):
    note: str
    date: str
    time: str


@api_router.post('/cliffnotes')
def add_note(note: NoteModel):
    new_note = Note(note=note.note, date=note.date, time=note.time)

    new_note.save()
    note_id = new_note.id

    return {
        "note_id": note_id
    }


@api_router.get("/cliffnotes")
def read_items():
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

    return {
        "notes": notes
    }
