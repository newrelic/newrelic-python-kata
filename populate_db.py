from django.utils import timezone

from query.models import Poll, Choice

with open('names.txt') as f: 
    for line in f:
        for _ in xrange(10):
            p = Poll(question=line, pub_date=timezone.datetime.now())
            p.save()

for p in Poll.objects.all():
    p.choice_set.create(choice_text="21-30", votes=0)
    p.choice_set.create(choice_text="31-40", votes=0)
    p.choice_set.create(choice_text="41-50", votes=0)
    p.save()
