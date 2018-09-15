# rmblankpages: A blank pages remover from PDF files - no watermark.

## Getting Started

This simple code separates PDF files in blank and useful pages by calculating the size of all pages. If a page size is smaller than a prefixed threshold, is a blank page. Otherwise, is a useful page. 

### Prerequisites

Before use, install PyPDF2 library. In terminal, type:

    pip install PyDF2

### Usage

Import code and run:

    import rmblankpages as rmbp
    
    newFileWriter, blankPagesWriter = rmbp.sep_blank_from_content('EXAMPLE.pdf')
    with open('NEW_FILE.pdf', 'wb') as f:
        newFileWriter.write(f)

If you want to ensure that useful pages aren't excluded, persist blankPagesWriter object too.

    with open('BLANK_PAGES.pdf', 'wb') as f:
        blankPagesWriter.write(f)
    