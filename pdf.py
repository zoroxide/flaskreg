# Xprinter XP-370B 

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_pdf_with_names_then_print(text1, text2, filename="data.pdf"):
    pdf_width, pdf_height = 350, 300
    
    c = canvas.Canvas(filename, pagesize=(pdf_width, pdf_height))
    
    font_size1 = 35 
    font_size2 = 30  
    
    c.setFont("Helvetica", font_size1)
    
    text1_width = c.stringWidth(text1, "Helvetica", font_size1)
    c.setFont("Helvetica", font_size2)
    text2_width = c.stringWidth(text2, "Helvetica", font_size2)
    text_height = font_size1 
    
    x1 = (pdf_width - text1_width) / 2
    y1 = (pdf_height + text_height) / 2 + 10  
    
    x2 = (pdf_width - text2_width) / 2
    y2 = (pdf_height - text_height) / 2 - 10  
    
    c.setFont("Helvetica", font_size1)
    c.drawString(x1, y1, text1)
    
    c.setFont("Helvetica", font_size2)
    c.drawString(x2, y2, text2)
    
    c.save()
   
    printer_name = "Xprinter XP-370B"
    pdf_file = r"C:\repos\qr_scanner_flask-master\eitesal_regestration-main\api\data.pdf"
    print_settings = "landscape"

    command = f'"SumatraPDF -print-to "{printer_name}" -print-settings "{print_settings}" "{pdf_file}"'
    
    try:
        os.system(command)
        # print("Print command executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# create_pdf_with_names_then_print("Person Name", "Person Company")
