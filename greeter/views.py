from django.shortcuts import redirect, render

from .models import Visitor


def home(request):
    error = None

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        if name:
            # сохраняем имя в базу данных
            Visitor.objects.create(name=name)
            # делаем редирект, чтобы при обновлении страницы (F5)
            # форма не отправилась ещё раз
            return redirect('home')
        else:
            error = 'Имя не может быть пустым!'

    # показываем приветствие для того, кто ввёл имя последним
    last_visitor = Visitor.objects.last()
    greeting_name = last_visitor.name if last_visitor else None

    return render(request, 'greeter/home.html', {
        'error': error,
        'greeting_name': greeting_name,
    })
