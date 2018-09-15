import os
from PyPDF2 import PdfFileWriter, PdfFileReader

TEMP_PAGE = 'temp_page.pdf'


def _getPageSize(page):
    """
    Return the size (in bits) from a simple page.
    """
    fileWriter = PdfFileWriter()
    fileWriter.addPage(page)
    with open(TEMP_PAGE, 'wb') as f:
        fileWriter.write(f)
    size = os.stat(TEMP_PAGE).st_size
    os.remove(TEMP_PAGE)
    return size


def sep_blank_from_content(filename, threshold=60000):
    """
    Receiving a a PDF file, it returns two files. First, a new file with useful
    pages. At last, a PDF file with only blank pages - just for check.
    """
    file = open(filename, 'rb')
    fileReader = PdfFileReader(file)
    blankPagesWriter = PdfFileWriter()
    newFileWriter = PdfFileWriter()

    for number in range(fileReader.getNumPages()):
        page = fileReader.getPage(number)
        page_size = _getPageSize(page)
        if page_size <= threshold:
            blankPagesWriter.addPage(page)
        else:
            newFileWriter.addPage(page)

    file.close()
    return newFileWriter, blankPagesWriter
