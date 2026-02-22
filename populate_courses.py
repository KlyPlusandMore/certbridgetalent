import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import Course

courses = [
    ('ISO/IEC 27001 Lead Auditor', 'security', 'Master Information Security Management System auditing.'),
    ('ISO/IEC 27001 Lead Implementer', 'security', 'Learn to implement robust security frameworks.'),
    ('ISO 9001 Lead Auditor', 'quality', 'Drive organizational excellence through quality management.'),
    ('ISO 31000 Risk Manager', 'quality', 'Identify, assess, and mitigate complex organizational risks.'),
    ('ISO 22301 Lead Implementer', 'resilience', 'Prepare exhaustive business continuity strategies.'),
    ('Lead Cybersecurity Manager', 'security', 'Advanced management of cybersecurity programs.'),
    ('ISO 45001 Lead Auditor', 'quality', 'Master Occupational Health and Safety Management Systems.'),
    ('ISO 14001 Lead Auditor', 'quality', 'Lead organizations in environmental management excellence.'),
    ('ISO 22000 Lead Auditor', 'quality', 'Ensure food safety standards across the supply chain.'),
    ('Traveaux en hauteur', 'technical', 'Safety protocols and techniques for working at heights.'),
    ('Conduite Defensive', 'technical', 'Practical defensive driving techniques for operational safety.'),
    ('Espace Confiné', 'technical', 'Safety management for working in confined spaces.'),
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
