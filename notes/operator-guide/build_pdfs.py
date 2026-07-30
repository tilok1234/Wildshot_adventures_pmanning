#!/usr/bin/env python3
"""Render the operator guide markdown files to styled PDFs.

Usage: python3 build_pdfs.py   (run from this directory)
Regenerate both PDFs after any ruling that changes protocol, so the
committed PDFs never drift from the committed markdown.
"""
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, Frame, HRFlowable, PageTemplate, Paragraph,
    Spacer, Table, TableStyle, KeepTogether,
)

HERE = Path(__file__).parent

INK = colors.HexColor("#1c1e26")
ACCENT = colors.HexColor("#b45309")      # amber — wildshot dusk
ACCENT_DARK = colors.HexColor("#7c3aed") # violet for h3
MUTED = colors.HexColor("#5b5f6e")
BOX_BG = colors.HexColor("#fdf6ec")
BOX_EDGE = colors.HexColor("#e2c99f")
ROW_ALT = colors.HexColor("#f4f2ee")
CODE_BG = colors.HexColor("#f0eee9")

S = {
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=22,
                            leading=26, textColor=INK, spaceAfter=2),
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=14,
                         leading=17, textColor=ACCENT, spaceBefore=14,
                         spaceAfter=5),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11.5,
                         leading=14, textColor=INK, spaceBefore=10,
                         spaceAfter=4),
    "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5,
                         leading=13, textColor=ACCENT_DARK, spaceBefore=8,
                         spaceAfter=3),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.5,
                           leading=13, textColor=INK, spaceAfter=5),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.5,
                             leading=13, textColor=INK, leftIndent=14,
                             bulletIndent=4, spaceAfter=3),
    "num": ParagraphStyle("num", fontName="Helvetica", fontSize=9.5,
                          leading=13, textColor=INK, leftIndent=18,
                          bulletIndent=4, spaceAfter=3),
    "quote": ParagraphStyle("quote", fontName="Helvetica", fontSize=9.5,
                            leading=13, textColor=INK, spaceAfter=0),
    "code": ParagraphStyle("code", fontName="Courier", fontSize=9,
                           leading=12, textColor=INK, leftIndent=10,
                           spaceAfter=6, backColor=CODE_BG,
                           borderPadding=5),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=8.8,
                           leading=11.5, textColor=INK),
    "cellhead": ParagraphStyle("cellhead", fontName="Helvetica-Bold",
                               fontSize=8.8, leading=11.5,
                               textColor=colors.white),
    "foot": ParagraphStyle("foot", fontName="Helvetica", fontSize=8,
                           textColor=MUTED),
}


def inline(text):
    text = (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))
    text = re.sub(r"`([^`]+)`",
                  r'<font face="Courier" backColor="#f0eee9">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<i>\1</i>", text)
    return text


def make_table(rows):
    n = max(len(r) for r in rows)
    data = []
    for i, r in enumerate(rows):
        r = r + [""] * (n - len(r))
        style = S["cellhead"] if i == 0 else S["cell"]
        data.append([Paragraph(inline(c), style) for c in r])
    avail = 6.7 * inch
    t = Table(data, colWidths=[avail / n] * n, repeatRows=1)
    ts = [
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#c9c6bf")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            ts.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    t.setStyle(TableStyle(ts))
    return t


def quote_box(lines):
    para = Paragraph(inline(" ".join(lines)), S["quote"])
    t = Table([[para]], colWidths=[6.7 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BOX_BG),
        ("BOX", (0, 0), (-1, -1), 0.6, BOX_EDGE),
        ("LINEBEFORE", (0, 0), (0, -1), 2.5, ACCENT),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def md_to_story(md, subtitle):
    lines = md.splitlines()
    story = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("```"):
            i += 1
            code = []
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            story.append(Paragraph("<br/>".join(
                l.replace("&", "&amp;").replace("<", "&lt;")
                 .replace(" ", "&nbsp;") for l in code), S["code"]))
            continue
        if line.startswith("    ") and not stripped.startswith(("-", "*")):
            code = []
            while i < n and (lines[i].startswith("    ") or not lines[i].strip()):
                if lines[i].strip():
                    code.append(lines[i][4:])
                i += 1
            story.append(Paragraph("<br/>".join(
                l.replace("&", "&amp;").replace("<", "&lt;")
                 .replace(" ", "&nbsp;") for l in code), S["code"]))
            continue
        if stripped.startswith("# "):
            story.append(Paragraph(inline(stripped[2:]), S["title"]))
            story.append(Paragraph(subtitle, ParagraphStyle(
                "sub", parent=S["body"], textColor=MUTED, fontSize=9.5,
                spaceAfter=8)))
            story.append(HRFlowable(width="100%", thickness=1.6,
                                    color=ACCENT, spaceAfter=10))
            i += 1
            continue
        if stripped.startswith("## "):
            story.append(Paragraph(inline(stripped[3:]), S["h1"]))
            i += 1
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(inline(stripped[4:]), S["h2"]))
            i += 1
            continue
        if stripped.startswith("#### "):
            story.append(Paragraph(inline(stripped[5:]), S["h3"]))
            i += 1
            continue
        if stripped == "---":
            story.append(HRFlowable(width="100%", thickness=0.7,
                                    color=colors.HexColor("#d8d5cd"),
                                    spaceBefore=6, spaceAfter=6))
            i += 1
            continue
        if stripped.startswith(">"):
            q = []
            while i < n and lines[i].strip().startswith(">"):
                q.append(lines[i].strip().lstrip(">").strip())
                i += 1
            story.append(quote_box([x for x in q if x]))
            story.append(Spacer(1, 8))
            continue
        if stripped.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            story.append(make_table(rows))
            story.append(Spacer(1, 7))
            continue
        if stripped.startswith(("- ", "* ")):
            text = [stripped[2:]]
            i += 1
            while i < n and lines[i].strip() and not re.match(
                    r"^(\s*[-*] |#|\||>|```|\s*\d+\. )", lines[i]) \
                    and not lines[i].startswith("    "):
                text.append(lines[i].strip())
                i += 1
            story.append(Paragraph(inline(" ".join(text)), S["bullet"],
                                   bulletText="•"))
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if m:
            text = [m.group(2)]
            i += 1
            while i < n and lines[i].strip() and not re.match(
                    r"^(\s*[-*] |#|\||>|```|\s*\d+\. )", lines[i]) \
                    and not lines[i].startswith("    "):
                text.append(lines[i].strip())
                i += 1
            story.append(Paragraph(inline(" ".join(text)), S["num"],
                                   bulletText=m.group(1) + "."))
            continue
        text = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(
                r"^(\s*[-*] |#|\||>|```|\s*\d+\. |-{3})", lines[i]) \
                and not lines[i].startswith("    "):
            text.append(lines[i].strip())
            i += 1
        story.append(Paragraph(inline(" ".join(text)), S["body"]))
    return story


def build(md_name, pdf_name, subtitle, footer):
    md = (HERE / md_name).read_text(encoding="utf-8")

    def on_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(0.9 * inch, 0.55 * inch, footer)
        canvas.drawRightString(letter[0] - 0.9 * inch, 0.55 * inch,
                               f"page {doc.page}")
        canvas.setStrokeColor(colors.HexColor("#d8d5cd"))
        canvas.setLineWidth(0.5)
        canvas.line(0.9 * inch, 0.7 * inch, letter[0] - 0.9 * inch,
                    0.7 * inch)
        canvas.restoreState()

    doc = BaseDocTemplate(str(HERE / pdf_name), pagesize=letter,
                          leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                          topMargin=0.75 * inch, bottomMargin=0.9 * inch,
                          title=pdf_name.replace(".pdf", ""),
                          author="Wildshot project")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                  id="main")
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame],
                                       onPage=on_page)])
    doc.build(md_to_story(md, subtitle))
    print(f"built {pdf_name}")


if __name__ == "__main__":
    build("OPERATOR_QUICK_CARD.md", "WILDSHOT_OPERATOR_QUICK_CARD.pdf",
          "The one-glance operator reference — derived digest, "
          "snapshot 2026-07-30. Planning docs + Decision Deck win on any "
          "conflict.",
          "Wildshot Operator Quick Card — derived digest 2026-07-30 "
          "— authority: planning docs 16/18 + Decision Deck")
    build("OPERATOR_MANUAL.md", "WILDSHOT_OPERATOR_MANUAL.pdf",
          "How you run the seven-repo machine — derived digest, "
          "snapshot 2026-07-30. Planning docs + Decision Deck win on any "
          "conflict.",
          "Wildshot Operator Manual — derived digest 2026-07-30 "
          "— authority: planning docs 16/18 + Decision Deck")
