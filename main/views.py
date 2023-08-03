from django.shortcuts import render

def index(request):
    data = {
        'title': 'Junior Python developer',
        'values': ['Прошу посмотреть данный сайт-резюме,', 'оценить и дать обратную связь!', 'Огромное спасибо)']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def education(request):
    return render(request, 'main/education.html')

def skills(request):
    return render(request, 'main/skills.html')

def contacts(request):
    return render(request, 'main/contacts.html')
