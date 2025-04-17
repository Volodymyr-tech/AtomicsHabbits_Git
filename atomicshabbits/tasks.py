from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from .models import Habbits
from .services import SendMessageTelegram


@shared_task
def send_notification():
    now = timezone.now()

    # We get all the tasks that have a set time and the completion time has already arrived
    tasks_to_notify = Habbits.objects.filter(time__isnull=False, time__lte=now, tg_chat_id__isnull=False)

    for habit in tasks_to_notify:
        # Forming a notification message
        message = f"Пора выполнить задачу: {habit.action}."

        # Sending a notification
        rep = SendMessageTelegram(message, habit.user.tg_chat_id)
        rep()

        # If the periodicity field is set (and must be at least once a week)
        if habit.periodicity and habit.periodicity >= 1:
            # Calculate the interval between notifications in days:
            # 7 days per week divided by the number of repetitions per week.
            interval_days = 7 / habit.periodicity

            # Update the time for the next notification
            habit.time = habit.time + timedelta(days=interval_days)
            habit.save()
        else:
            pass
