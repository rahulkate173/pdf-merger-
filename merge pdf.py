

from pypdf import PdfWriter
def merge_pdf(lst_pdf):
    merger = PdfWriter()
    for pdf in lst_pdf:
        merger.append(pdf)

    merger.write("merged pdf.pdf")
    merger.close()

def main():
    lst_pdf=[]
    print(' PDF MERGER ')
    while True:
        pdf_name = input("Enter the name of pdf to merge : ")
        
        condition = input(" Press \"y\" to keep merging : ")
        if condition == "y" or "Y" :
            lst_pdf.append(f'{pdf_name}.pdf')
        else :

    
            break

    merge_pdf(lst_pdf)

if __name__ == "__main__":
    main()