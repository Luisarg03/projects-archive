import os
from pypdf import PdfWriter

from modules.move_notes import copy_folder
from modules.create_book import png_to_pdf
from modules.clear_path import clear_path
from modules.create_index import crete_index, create_pdf_index


merger = PdfWriter()
book_name = 'aws_solutions_architect_associate_notes'
notes_folder = "../notes/"
pngs_folder = "../pngs/"
correction = 2
paths_pdf = ["../pdfs/", "../book/"]


def get_pngs_list(pngs_folder):
    pngs_list = {}
    for root, dirs, files in os.walk(pngs_folder):
        for file in files:
            if not file.endswith(".png"):
                continue
            root_key = root.split("/")[-1]

            if root_key not in pngs_list:
                pngs_list[root_key] = [file]
            else:
                pngs_list[root_key].append(file)

    return pngs_list


if __name__ == "__main__":
    for path in paths_pdf:
        if not os.path.exists(path):
            os.makedirs(path)

    copy_folder(notes_folder, pngs_folder)
    clear_path(pngs_folder, removefiles=True, extensions=['.md', '.excalidraw'], removesubfolders=True, subfolders=['img'])
    list_pngs = get_pngs_list(pngs_folder)
    index = crete_index(list_pngs, correction)
    create_pdf_index(index, paths_pdf[0])
    png_to_pdf(list_pngs, pngs_folder, paths_pdf[0])

    pdfs = os.listdir(paths_pdf[0])
    pdfs.sort()

    for pdf in pdfs:
        path_pdf = f'{paths_pdf[0]}{pdf}'
        merger.append(path_pdf)

    merger.write(f"{paths_pdf[1]}{book_name}.pdf")
    merger.close()

    clear_path(paths_pdf[0], removefiles=True, extensions=['.pdf'])
    clear_path('../', removesubfolders=True, subfolders=['pdfs'])
