from django.shortcuts import render, redirect
from .forms import NoteForm

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')  # Redirect to a page displaying all notes
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})