from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Service, Venue

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        # 🔐 Add authentication logic here (username/password)
        
        # ✅ After successful login → redirect to Services section
        return redirect('/#services')

    return render(request, 'login.html')

# Render wedding page
def wedding_page(request):
    return render(request, "wedding.html")

# Render venue page
def venue_page(request):
    return render(request, "venue.html")

def venue1_page(request):
    return render(request, "venue1.html")

# API: Get all services
def get_services(request):
    services = list(Service.objects.values())
    return JsonResponse(services, safe=False)

# API: Get all venues
def get_venue(request):
    venues = list(Venue.objects.values())
    return JsonResponse(venues, safe=False)

# API: Add a new venue
@csrf_exempt
def add_venue(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Venue.objects.create(
            name=data.get("name"),
            location=data.get("location"),
            price=data.get("price"),
            rating=data.get("rating", 4)
        )
        return JsonResponse({"message": "Venue added successfully"})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()

        # Rule-based responses
        if "hello" in user_message or "hi" in user_message:
            bot_reply = "Hello! Welcome to Evento. How can I help you today?"
        elif "event" in user_message or "types of events" in user_message:
            bot_reply = "We organize marriages, birthdays, and receptions."
        elif "how to book" in user_message or "booking" in user_message:
            bot_reply = (
                "To book an event:\n"
                "1. Choose event type (Marriage, Birthday, Reception).\n"
                "2. Select services (Catering, Decoration, Photography, Entertainment).\n"
                "3. Specify date & time.\n"
                "4. Provide guest count.\n"
                "5. Confirm booking and make payment online or via phone/email.\n"
                "6. Receive confirmation and event updates from our team."
            )
        elif "price" in user_message or "cost" in user_message:
            bot_reply = "Pricing depends on event type and services. Can you specify your event?"
        elif "marriage" in user_message or "wedding" in user_message:
            bot_reply = "Our marriage packages include decoration, catering, and entertainment."
        elif "birthday" in user_message:
            bot_reply = "Birthday packages include themes, cakes, games, and decorations."
        elif "reception" in user_message:
            bot_reply = "Reception events can be customized with seating, lighting, and music."
        elif "catering" in user_message:
            bot_reply = "We provide catering services with veg, non-veg, and dessert options."
        elif "decoration" in user_message:
            bot_reply = "Decoration includes flowers, lighting, stage setup, and theme design."
        elif "photography" in user_message or "photo" in user_message:
            bot_reply = "Professional photographers and videographers are available."
        elif "entertainment" in user_message:
            bot_reply = "We arrange DJs, live music, and performances for your events."
        elif "customize" in user_message or "customization" in user_message:
            bot_reply = "Yes, packages can be customized based on your requirements and budget."
        elif "guest" in user_message or "capacity" in user_message:
            bot_reply = "We handle events from small gatherings to 500+ guests."
        elif "payment" in user_message:
            bot_reply = "Payment can be made via online transfer, UPI, or card."
        elif "venue" in user_message or "location" in user_message:
            bot_reply = "We can recommend venues based on budget, guest count, and event type."
        elif "refund" in user_message or "cancellation" in user_message:
            bot_reply = "Refunds depend on event type and notice period. Contact us for details."
        elif "contact" in user_message or "email" in user_message or "phone" in user_message:
            bot_reply = "You can contact us at contact@evento.com or call +91 9876543210."
        elif "services" in user_message or "offer" in user_message:
            bot_reply = "We offer catering, decoration, entertainment, photography, and event planning."
        elif "review" in user_message or "feedback" in user_message:
            bot_reply = "You can check our client testimonials on our website."
        elif "theme" in user_message:
            bot_reply = "We offer multiple themes for birthday, wedding, and reception events."
        elif "faq" in user_message:
            bot_reply = "You can ask about pricing, venues, booking process, or available services."
        elif "recommendation" in user_message:
            bot_reply = "We can recommend venues, decorators, and caterers based on your budget."
        elif "timing" in user_message or "schedule" in user_message:
            bot_reply = "Events can be scheduled based on your preferred date and time."
        else:
            bot_reply = "We will get back to you soon."

        return JsonResponse({"response": bot_reply})

    return JsonResponse({"response": "Invalid request method."})