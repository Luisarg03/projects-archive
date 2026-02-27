import os
import re
import json
import img2pdf
from pypdf import PdfWriter
from PIL import Image


def png_to_pdf(list_pngs, pngs_folder, paths_pdf):
    for key, value in list_pngs.items():
        for i in range(len(value)):
            value[i] = f"{pngs_folder}{key}/{value[i]}"
            with Image.open(value[i]) as image:
                pdf = img2pdf.convert(image.filename)

                pdf_filename = f"{paths_pdf}{key}_{i}.pdf"
                print(pdf_filename)

                with open(pdf_filename, "wb") as file:
                    file.write(pdf)

    return True
