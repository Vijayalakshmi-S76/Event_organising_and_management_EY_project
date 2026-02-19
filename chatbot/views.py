from django.shortcuts import render
from .models import ChatBot

def chatbot(request):
    reply = ""

    if request.method == "POST":
        msg = request.POST.get("message")

        try:
            data = ChatBot.objects.get(question__icontains=msg)
            reply = data.answer
        except:
            reply = "Sorry, I didn't understand"

    return render(request, "chatbot.html", {"reply": reply})
