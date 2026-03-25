import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()
for topic in topics:
    print(topic.id , topic.text, topic.date_added)

topic = Topic.objects.get(id=1)
print(topic)
print(topic.date_added)

entries = Entry.objects.filter(topic=topic)
for entry in entries:
    print(entry)