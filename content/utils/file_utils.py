import os
from django.conf import settings
from django.utils.text import slugify
from docx import Document
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def generate_temporary_txt_file(title, content):
    # Générer le contenu du fichier TXT
    txt_content = content

    # Définir le nom du fichier en utilisant le titre de l'article
    filename = f"{slugify(title)}.txt"

    # Chemin complet pour sauvegarder temporairement le fichier
    filepath = os.path.join(settings.MEDIA_ROOT, "temp", filename)

    # Écrire le contenu dans un fichier texte temporaire
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(txt_content)

    return filepath


def generate_temporary_docx_file(title, content):
    # Générer le contenu du fichier docx
    txt_content = content

    # Définir le nom du fichier en utilisant le titre de l'article
    filename = f"{slugify(title)}.docx"

    # Chemin complet pour sauvegarder temporairement le fichier
    filepath = os.path.join(settings.MEDIA_ROOT, "temp", filename)

    # Écrire le contenu dans un fichier texte temporaire
    doc = Document()
    doc.add_paragraph(txt_content)

    # Enregistrer le document dans un fichier DOCX temporaire
    doc.save(filepath)

    return filepath


def generate_temporary_png_file(filename, titre):
    filepath = settings.MEDIA_ROOT + filename
    filepath_pdf = settings.MEDIA_ROOT + "temp/" + slugify(titre) + ".pdf"
    drawing = svg2rlg(filepath)
    drawing
    renderPDF.drawToFile(drawing, filepath_pdf)
    return filepath_pdf
