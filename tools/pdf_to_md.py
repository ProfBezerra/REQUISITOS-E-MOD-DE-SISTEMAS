import sys
import os
import argparse
from pdfminer.high_level import extract_text


def normalize_text(text: str) -> str:
    # Basic cleanup: normalize line breaks and multiple spaces
    lines = [l.rstrip() for l in text.splitlines()]
    cleaned = []
    prev_blank = False
    for l in lines:
        s = l.strip()
        if not s:
            if not prev_blank:
                cleaned.append("")
            prev_blank = True
            continue
        prev_blank = False
        # Convert common bullet characters to markdown dashes
        if s.startswith(("•", "-", "–", "*")):
            s = s.lstrip("•–*- ")
            s = f"- {s}"
        cleaned.append(s)
    return "\n".join(cleaned)


def convert_pdf_to_md(input_pdf: str, output_md: str) -> None:
    text = extract_text(input_pdf)
    md = normalize_text(text)
    # Add a simple header with source filename
    header = f"# {os.path.basename(input_pdf)}\n\n"
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(md)


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown (text-only)")
    parser.add_argument("input_pdf", help="Path to input PDF")
    parser.add_argument("output_md", nargs="?", help="Path to output Markdown file")
    args = parser.parse_args()

    input_pdf = os.path.abspath(args.input_pdf)
    if not os.path.isfile(input_pdf):
        print(f"Error: file not found: {input_pdf}")
        sys.exit(1)

    if args.output_md:
        output_md = os.path.abspath(args.output_md)
    else:
        base = os.path.splitext(os.path.basename(input_pdf))[0]
        output_md = os.path.join(os.path.dirname(input_pdf), base + ".md")

    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    convert_pdf_to_md(input_pdf, output_md)
    print(f"Converted: {input_pdf} -> {output_md}")


if __name__ == "__main__":
    main()
