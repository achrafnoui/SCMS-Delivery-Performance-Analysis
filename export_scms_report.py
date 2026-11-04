from pathlib import Path
import sys
import nbformat
from nbconvert import HTMLExporter
from traitlets.config import Config
from weasyprint import HTML

notebook_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("SCMS_Executive_Research_Notebook.ipynb")
if not notebook_path.exists():
    raise FileNotFoundError(f"Notebook not found: {notebook_path}")

notebook = nbformat.read(notebook_path, as_version=4)
config = Config()
config.HTMLExporter.exclude_input = True
config.HTMLExporter.exclude_output_prompt = True
config.HTMLExporter.exclude_input_prompt = True
config.HTMLExporter.embed_images = True

exporter = HTMLExporter(config=config)
exporter.template_name = "classic"
body, resources = exporter.from_notebook_node(notebook)

css = """
<style>
@page { size: A4; margin: 17mm 16mm 18mm 16mm;
  @bottom-left { content: "SCMS DELIVERY PERFORMANCE | EXECUTIVE RESEARCH"; color: #667085; font-size: 8pt; }
  @bottom-right { content: "Page " counter(page); color: #667085; font-size: 8pt; }
}
html, body { font-family: Arial, Helvetica, sans-serif; color: #1f2937; font-size: 10pt; line-height: 1.48; }
body { max-width: 100%; margin: 0 auto; }
#notebook-container { box-shadow: none !important; width: 100% !important; padding: 0 !important; }
h1, h2, h3 { page-break-after: avoid; }\nimg { page-break-inside: avoid; }
h1 { color: #17324d; font-size: 27pt; line-height: 1.12; margin-top: 8pt; }
h2 { color: #17324d; font-size: 17pt; border-bottom: 1px solid #d8e1ea; padding-bottom: 5pt; margin-top: 22pt; }
h3 { color: #24506f; font-size: 12pt; margin-top: 14pt; }
p, li { orphans: 3; widows: 3; }
blockquote { border-left: 3px solid #2e6b8a; background: #f1f5f9; padding: 8px 12px; margin-left: 0; }
table { border-collapse: collapse; width: 100%; font-size: 8.5pt; margin: 8pt 0 14pt; }
th { background: #17324d; color: white; text-align: left; }
th, td { border: 1px solid #d8e1ea; padding: 5px 7px; vertical-align: top; }
tr:nth-child(even) td { background: #f6f8fa; }
img { max-width: 100% !important; height: auto !important; display: block; margin: 10pt auto; }
pre, code { display: none !important; }
.output_stderr, .output_error { display: none !important; }
a { color: #24506f; text-decoration: none; }
hr { border: 0; border-top: 1px solid #d8e1ea; }
</style>
"""
# Remove any input blocks as a second guard, then insert print CSS.
import re
body = re.sub(r'<div class="input">.*?</div>\\s*</div>', '', body, flags=re.S)
if "</head>" in body:
    body = body.replace("</head>", css + "</head>", 1)
else:
    body = css + body

html_path = notebook_path.with_name("SCMS_Executive_Research_Report.html")
pdf_path = notebook_path.with_name("SCMS_Executive_Research_Report.pdf")
html_path.write_text(body, encoding="utf-8")
HTML(string=body, base_url=str(notebook_path.parent)).write_pdf(str(pdf_path))
print(f"Created: {html_path}")
print(f"Created: {pdf_path}")
