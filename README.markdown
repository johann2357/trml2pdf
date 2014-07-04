Open source implemenaton of RML (Report Markup Language) from ReportLab for Django

[RML User Guide](http://www.reportlab.com/docs/rml2pdf-userguide.pdf)  (or [beginner tutorial](http://www.reportlab.com/docs/rml-for-idiots.pdf))

Not all tags are supported, but most of them work.
 

Examples
--------

Create a PDF file:

Use it as a python module:
```python
	import trml2pdf
	print trml2pdf.parseString(file('file.rml','r').read())
```
 
This version 1.1 is only for Django, you can simply mark up an .rml file with the template system and then render it.

You have to define a variable called FONTS_DIR in your settings.py, pointing to the fonts location in your project ... and thats it!
