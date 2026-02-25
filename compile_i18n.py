import polib
import os

po_path = 'locale/fr/LC_MESSAGES/django.po'
mo_path = 'locale/fr/LC_MESSAGES/django.mo'

if os.path.exists(po_path):
    po = polib.pofile(po_path)
    po.save_as_mofile(mo_path)
    print(f"Successfully compiled {po_path} to {mo_path}")
else:
    print(f"Error: {po_path} does not exist.")
