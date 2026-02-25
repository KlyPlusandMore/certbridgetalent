import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import Course

# Clear existing courses
print("Clearing existing courses...")
Course.objects.all().delete()

courses = [
    ('ISO 45001', 'quality', 'Occupational Health and Safety Management Systems.'),
    ('ISO 22000', 'quality', 'Food Safety Management Systems.'),
    ('ISO 14001', 'quality', 'Environmental Management Systems.'),
    ('Traveaux en hauteur', 'technical', 'Safety protocols for working at heights.'),
    ('Conduite Defensive', 'technical', 'Defensive driving techniques for safety.'),
    ('Espace Confine', 'technical', 'Safety management for confined spaces.'),
    ('ISO 31000', 'quality', 'Risk Management guidelines and principles.'),
]

for title, cat, desc in courses:
    course, created = Course.objects.get_or_create(
        title=title,
        defaults={'category': cat, 'description': desc}
    )
    if created:
        print(f"Created course: {title}")
    else:
        print(f"Course already exists: {title}")

print("Course population complete.")
