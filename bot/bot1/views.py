from django.shortcuts import render
from .models import User,Message
import nltk

#from nltk.tokenize import word_tokenize

#nltk.download('punkt', quiet=True)

#nltk.download('all', quiet=True)


def generate_response(message):
    message= message.lower()
    #message = word_tokenize()

    if "hello" in message or "hi" in message:
        return "soluda ena venum "
    elif "how are you" in message:
        return "nan epdi iruntha unaku ena mooditu po"
    elif "goodbye" in message or "bye" in message:
        return " eppa ozunji po da tholla panatha"
    elif "weather" in message and "today" in message:
        return "ethuva irunthalum ne onum pana porathu ila"
    
    else:
        return "lusu mathri ethana pesitu irukatha mooditu poriya"
       

def chat_view(request):
    if request.method == 'POST':
        user = User.objects.get_or_create(name= 'User1')[0]
        content = request.POST.get('message')
        message = Message(user=user,content=content)
        message.save()

        bot_response = generate_response(content)

        return render(request, 'chatbot/chat.html' , {'bot_response':bot_response})
    
    return render(request,'chatbot/chat.html')