from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        corpo = f"Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}"

        send_mail(
            subject=f"{nome} entrou em contato pelo site!",
            message=corpo,
            from_email=email,
            recipient_list=['seuemail@gmail.com'],
            fail_silently=False,
        )

        # Mensagem automática para o remetente
        send_mail(
            subject="Recebemos sua mensagem!",
            message=f"{nome}, obrigado por entrar em contato. Em breve retornaremos sua mensagem!",
            from_email='seuemail@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('contato')

    return render(request, 'contato.html')


def enviar_email_adocao(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail(
            'Obrigado por escolher adotar!',
            f'{email}, obrigado por escolher um dos nossos animais para adoção! Em breve entraremos em contato.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('adote')
    

def adote(request):
    return render(request, 'adote.html')

def doe(request):
    return render(request, 'doe.html')

def ben(request):
    return render(request, 'ben.html')

