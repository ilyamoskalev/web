from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def init():
    questions = []
    for i in range(0, 100):
        questions.append({
            'title': 'Question Title' + str(i),
            'id': i,
            'text': 'text' + str(i),
            'likes': 5,
            'tags': ['Tag1', 'Tag2', 'Tag3'],
            'count_answers': 2,
            'answers': [{'text': 'answer1', 'isCorrect': 1, 'likes': 5},
                        {'text': 'answer2', 'isCorrect': 0, 'likes': 5}],
        })
    hot_tags = ['Tag1', 'Tag2', 'Tag3']
    Authorized = 0
    return {'questions': questions, 'hot_tags': hot_tags, 'Authorized': Authorized}

init_list = init()

def pagination(request):
    paginator = Paginator(init_list['questions'], 20)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return articles


def index(request):
    tag = init_list['hot_tags'][0]
    return render_to_response('index.html', {'tags': init_list['hot_tags'], 'questions': pagination(request),
                                             'isAuthorized': init_list['Authorized']})


def hot(request):
    return render_to_response('hot_questions.html', {'tags': init_list['hot_tags'], 'questions': pagination(request),
                                                     'isAuthorized': init_list['Authorized']})


def questions_by_tag(request, tag):
    return render_to_response('question_by_tag.html',
                              {'tags': init_list['hot_tags'], 'questions': pagination(request), 'tag': tag,
                               'isAuthorized': init_list['Authorized']})


def question(request, id):
    return render_to_response('question.html',
                              {'tags': init_list['hot_tags'], 'question': init_list['questions'][int(id)],
                               'isAuthorized': init_list['Authorized']})


def login(request):
    tag = init_list['hot_tags'][0]
    return render_to_response('login.html', {'isAuthorized': 0})


def signup(request):
    return render_to_response('signup.html', {'isAuthorized': 0})


def ask(request):
    return render_to_response('ask.html', {'tags': init_list['hot_tags'], 'isAuthorized': init_list['Authorized']})


def settings(request):
    return render_to_response('settings.html', {'tags': init_list['hot_tags'], 'isAuthorized': init_list['Authorized']})
