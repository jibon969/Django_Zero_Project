from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        # messages.add_message(request, messages.warning, 'Message Successfully Sent')
        return redirect('home')
    if form.errors:
        errors = form.errors
    context = {
        'form': form,
        'errors': errors
    }
    return render(request, 'contacts/contacts.html', context)
