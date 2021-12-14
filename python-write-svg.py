#!python
import svgwrite
'''
pip install svgwrite
svgwrite-1.4.1
'''
svg = svgwrite.Drawing(filename = "test-svgwrite.svg",size =("400px", "200px"))
svg.add(svg.rect(insert = (0, 0),size = ("200px","100px"),stroke_width = "5",stroke = "red",fill = "rgb(255,255,188)"))
svg.add(svg.text("สวัสดี SVG :)",insert = (210, 110)))
svg.save()