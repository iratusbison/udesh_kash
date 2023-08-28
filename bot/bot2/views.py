from django.shortcuts import redirect, render
from django.views import View
from .models import ChatMessage
import nltk
from nltk.tokenize import word_tokenize

class ChatView(View):
    template_name = 'chat.html'

    def get(self, request):
        messages = ChatMessage.objects.all()
        context = {'messages': messages}
        return render(request, self.template_name, context)

    def post(self, request):
        user_input = request.POST.get('user_input')
        bot_response = self.generate_response(user_input)
        ChatMessage.objects.create(content=user_input)
        ChatMessage.objects.create(content=bot_response)
        return redirect('chat')

    def generate_response(self, message):
        message = message.lower()
        tokens = word_tokenize(message)

        if "hello" in tokens or "hi" in tokens:
            return "Hello! How can I assist you?"
        elif any(word in tokens for word in ["how", "are", "you"]):
            return "I'm doing well, thank you! How about you?"
        elif any(word in tokens for word in ["goodbye", "bye"]):
            return "Goodbye! Have a great day!"
        elif any(word in tokens for word in ["weather", "today"]):
            return "The weather today is sunny and warm."
        else:
            return "I'm sorry, I didn't understand that."
