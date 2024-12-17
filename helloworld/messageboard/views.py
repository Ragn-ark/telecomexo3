# messageboard/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

# Function to handle message submission
def submit_message(request):
    if request.method == 'POST':
        sender = request.POST.get('sender_name')
        receiver = request.POST.get('receiver_name')
        message = request.POST.get('message_text')
        
        if sender and receiver and message:
            new_message = Message(sender_name=sender, receiver_name=receiver, message_text=message)
            new_message.save()
            return JsonResponse({'status': 'Message submitted successfully!'})
        else:
            return JsonResponse({'status': 'All fields are required.'})
    return render(request, 'submit_message.html')

# Function to get the latest 20 messages for a specific user
def get_messages(request):
    if request.method == 'GET':
        user_name = request.GET.get('user_name')
        
        if user_name:
            messages = Message.objects.filter(sender_name=user_name).order_by('-timestamp')[:20]
            message_list = [{'sender': msg.sender_name, 'message': msg.message_text, 'timestamp': msg.timestamp} for msg in messages]
            return JsonResponse({'messages': message_list})
        else:
            return JsonResponse({'status': 'User name is required.'})
