from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate

def index(request):
    return render(request, 'MainApp/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'all_topics': topics}
    return render(request, 'MainApp/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = Entry.objects.filter(topic=topic).order_by('-date_added')

    context = {'topic': topic, 'entries': entries}
    return render(request, 'MainApp/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            messages.success(request, f'Topic "{new_topic.text}" created successfully!')
            return redirect('MainApp:topics')

    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated successfully!')
            return redirect('MainApp:topic', topic_id=topic.id)
    
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'MainApp/edit_entry.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            messages.success(request, 'New entry added to the topic!')
            return redirect('MainApp:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'MainApp/new_entry.html', context)

# Новые страницы
@login_required
def clear_mind(request):
    return render(request, 'MainApp/clear_mind.html')

@login_required
def history(request):
    topics_count = Topic.objects.filter(owner=request.user).count()
    entries_count = Entry.objects.filter(topic__owner=request.user).count()
    context = {
        'topics_count': topics_count,
        'entries_count': entries_count
    }
    return render(request, 'MainApp/history.html', context)

@login_required
def keep_growing(request):
    # Продвинутая статистика для препода
    user_entries = Entry.objects.filter(topic__owner=request.user)
    
    # Группировка по датам для графика
    chart_data = user_entries.annotate(date=TruncDate('date_added')) \
        .values('date') \
        .annotate(count=Count('id')) \
        .order_by('date')
    
    # Считаем общее количество слов (примерно)
    total_words = sum(len(e.text.split()) for e in user_entries)
    
    # Топ тем по количеству записей
    top_topics = Topic.objects.filter(owner=request.user) \
        .annotate(entries_count=Count('entry')) \
        .order_by('-entries_count')[:5]

    context = {
        'chart_data': chart_data,
        'total_words': total_words,
        'top_topics': top_topics,
        'total_entries': user_entries.count(),
    }
    return render(request, 'MainApp/keep_growing.html', context)
