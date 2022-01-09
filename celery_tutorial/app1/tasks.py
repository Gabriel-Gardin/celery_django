from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def add(x,y):
    for i in range(1000000):
        x = x + i

    return ((x/100) + y)
