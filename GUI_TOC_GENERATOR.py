# GUI_TOC_Generator.py

import io
import math
import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter
from pypdf.generic import Destination

def extract_bookmarks(outlines, reader, depth=0):
    bookmarks = []
    for item in outlines:
        if isinstance(item, list):
            bookmarks.extend(extract_bookmarks(item, reader, depth + 1))
        elif isinstance(item, Destination):
            title = item.title
            page_number = reader.get_destination_page_number(item)
            bookmarks.append({
                "depth": depth,
                "title": title,
                "page": page_number
            })
    return bookmarks

def generate_toc_pdf(bookmarks, toc_pages_to_add):
    toc = FPDF()
    toc.add_page()
    toc.set_font("Helvetica", "B", size=18)
    toc.set_title("Table of Contents")
    toc.cell(0, 10, "Table of Contents", align="C")
    toc.ln(10)

    for b in bookmarks[4:]:
        indent = "    " * b["depth"]
        title = f"{indent}{b['title']}"
        page_str = str(b["page"] + toc_pages_to_add + 1)

        if b["depth"] == 0:
            toc.set_font("Helvetica", "B", 12)
        else:
            toc.set_font("Helvetica", "", 12)

        max_width = toc.w - toc.l_margin - toc.r_margin
        title_width = toc.get_string_width(title)
        page_width = toc.get_string_width(page_str)
        dot_width = toc.get_string_width(".")

        dots_needed = int((max_width - title_width - page_width) / dot_width)
        dots = "." * max(0, dots_needed)
        line = f"{title}{dots} {page_str}"
        toc.cell(0, 10, line)
        toc.ln(7.5)

    buffer = io.BytesIO()
    toc.output(buffer)
    buffer.seek(0)
    return buffer

def generate_pdf_with_toc(pdf_path, output_path):
    try:
        reader = PdfReader(pdf_path)
        raw_outlines = reader.outline
        bookmarks = extract_bookmarks(raw_outlines, reader)
        bookmarks.sort(key=lambda b: b["page"])
        TOCPGS = math.ceil(len(bookmarks) / 33)

        toc_buffer = generate_toc_pdf(bookmarks, TOCPGS)
        toc_reader = PdfReader(toc_buffer)

        writer = PdfWriter()
        for page in toc_reader.pages:
            writer.add_page(page)

        writer.append(pdf_path)

        with open(output_path, "wb") as f:
            writer.write(f)

        messagebox.showinfo("Success", "PDF created successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
def browse_pdf():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filepath:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, filepath)

def save_pdf():
    output = filedialog.asksaveasfilename(defaultextension=".pdf",
                                           filetypes=[("PDF Files", "*.pdf")])
    if output:
        generate_pdf_with_toc(input_entry.get(), output)

root = tk.Tk()
root.title("PDF TOC Generator")
root.geometry("400x150")

tk.Label(root, text="Select PDF file:").pack(pady=5)
input_entry = tk.Entry(root, width=40)
input_entry.pack()
tk.Button(root, text="Browse", command=browse_pdf).pack(pady=5)

tk.Button(root, text="Generate TOC and Save PDF", command=save_pdf).pack(pady=10)

root.mainloop()
