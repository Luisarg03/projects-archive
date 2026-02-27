import re
from markdown_pdf import MarkdownPdf, Section


def crete_index(list_pngs, index_correction=0):
    index = {}
    page_index = 1 + index_correction
    for key, value in list_pngs.items():
        index[key] = {}
        for i in range(len(value)):
            index[key][f"{page_index}"] = value[i]
            page_index += 1
    return index


def create_pdf_index(index, path_pdf):
    pdf = MarkdownPdf(toc_level=1)
    index_text = '### Table of Contents \n\n'

    for key, value in index.items():

        value = [str('- '+k+'_'+re.sub(r"^.{0,2}", ' ', v)).replace('.png', '') for k, v in value.items()]
        value = re.sub(r"[\[\]']", '', str(value))
        value = value.replace(',', '\n')
        key = re.sub(r"^.{0,3}", '', key)
        value = equal_dots(value)
        index_text += f'''#### {key} \n {value} \n'''

    pdf.add_section(Section(index_text))
    pdf.save(f"{path_pdf}00_index.pdf")


def equal_dots(text):
    new_text = ''
    for line in text.split('\n'):
        dot_value = 45
        line = line.strip()
        dot_limit = re.sub(r"\..*$", '', line)
        dot_limit = re.findall(r"\d+", dot_limit)

        if len(dot_limit[0]) == 1:
            dot_value = dot_value + 1

        line = line.replace('_', '.'*dot_value, 1)

        new_text += line+'\n'

    return new_text
