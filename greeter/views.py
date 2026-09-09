from django.shortcuts import redirect, render

from .forms import VisitorForm
from .models import Visitor


def home(request):
    """Главная страница: форма ввода имени и персонализированное приветствие.

    GET  -- показывает форму и (если есть) последнее сохранённое имя;
    POST -- валидирует введённое имя, сохраняет его в базу данных и
             отображает приветствие. При ошибке валидации (в первую очередь --
             пустое поле) форма возвращается с сообщением об ошибке,
             ничего не сохраняется.
    """
    greeting_name = None

    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            greeting_name = visitor.name
            # Redirect-after-POST (Post/Redirect/Get) -- защищает от повторной
            # отправки формы при обновлении страницы (F5) пользователем.
            return redirect(f"/?greeted={visitor.pk}")
        # Форма невалидна (например, пустое имя) -- отрисовываем её заново
        # вместе с ошибками, ничего в базу не пишем.
    else:
        form = VisitorForm()
        greeted_id = request.GET.get("greeted")
        if greeted_id:
            visitor = Visitor.objects.filter(pk=greeted_id).first()
            if visitor:
                greeting_name = visitor.name

    return render(
        request,
        "greeter/home.html",
        {"form": form, "greeting_name": greeting_name},
    )
