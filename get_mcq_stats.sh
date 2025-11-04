#!/bin/bash

echo "MCQ STATISTICS FROM HEROKU WEBSITE"
echo "=================================="
echo "Website: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/dashboard/"
echo "=================================="

echo -e "\n1. TOTAL MCQs:"
heroku run --app radiant-gorge-35079 --no-tty "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; print(MCQ.objects.count())'" | tail -1

echo -e "\n2. EXAM TYPES:"
heroku run --app radiant-gorge-35079 --no-tty "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; from django.db.models import Count; types = MCQ.objects.values(\"exam_type\").annotate(count=Count(\"id\")); [print(f\"{t[\"exam_type\"]}: {t[\"count\"]}\") for t in types]'" 2>/dev/null | grep -v Running | grep -v "^\[" | grep ":"

echo -e "\n3. EXAM YEARS:"
heroku run --app radiant-gorge-35079 --no-tty "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; from django.db.models import Count; years = MCQ.objects.values(\"exam_year\").annotate(count=Count(\"id\")); [print(f\"{y[\"exam_year\"]}: {y[\"count\"]}\") for y in years]'" 2>/dev/null | grep -v Running | grep -v "^\[" | grep ":"

echo -e "\n4. TOP 10 SUBSPECIALTIES:"
heroku run --app radiant-gorge-35079 --no-tty "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; from django.db.models import Count; subs = MCQ.objects.values(\"subspecialty\").annotate(count=Count(\"id\")).order_by(\"-count\")[:10]; [print(f\"{s[\"subspecialty\"] or \"Not specified\"}: {s[\"count\"]}\") for s in subs]'" 2>/dev/null | grep -v Running | grep -v "^\[" | grep ":"

echo -e "\n5. SUBSPECIALTY COUNT:"
heroku run --app radiant-gorge-35079 --no-tty "cd /app/django_neurology_mcq && python manage.py shell -c 'from mcq.models import MCQ; print(f\"Total subspecialties: {MCQ.objects.values(\"subspecialty\").distinct().count()}\")'" | tail -1

echo -e "\n=================================="
echo "END OF REPORT"
echo "==================================