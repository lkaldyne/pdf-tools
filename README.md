# pdf-tools
Collection of utilities for merging and altering PDFs.

## Requirements
Before running any pdf tools, install `PyPDF2` via the following command:
```bash
pip3 install PyPDF2
```

## Combiner
### Combines all PDFs in the `input/` dir and outputs `output/merged.pdf`
- Can be run via the following command: ```python3 combiner.py```
- Merges in alphabetical order of filenames


## Page Extractor
### Removes pages in PDFs based on user selection
- Can be run via the following command: ```python3 page-extractor.py```
- Pages should be specified using comma-separated values
- User can choose whether selected pages should be kept or removed

## Page Inserter (Coming Soon!)
### Inserts Pages into Existing PDFs
