from django.shortcuts import render

# Create your views here.

def home(request):
    data = [
        {'name': "Rohan", 'age': 23},
        {'name': "Ram", 'age': 2},
        {'name': "Shyam", 'age': 22},
        {'name': "Sita", 'age': 31},
        {'name': "Gita", 'age': 16},

    ]
    text = '''
    Welcome to The Complete Django Web Development Course. The most comprehensive Django course available online. Covering all the fundamental concepts regarding Django development, using the latest Django 4.0 version.

    I’ve built this course over months, perfecting the curriculum to ensure that you come out of this course as a fully-fledged Django developer. I’ll take you from scratch and make you into a skilled Django developer with a strong knowledge of building full-stack web applications.
    ''',
    return render(request, 'index.html',{"name": "Bholi", "age": 23, 'peoples': data, 'text': text, 'title': 'Homepage', })

def aboutpage(request):
    return render(request, 'about.html', {'title':'About Us'})


