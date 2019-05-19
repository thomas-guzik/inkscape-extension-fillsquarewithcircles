# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Programme permettant l'ajout de petits points gris dans des rectangles créés à l'aide d'Inkscape.

# Thomas Guzik, thomas.guzik@laposte.net
# Leo 130 contact@avilab.fr
# Corentin Bettiol - corentin-bettiol@hotmail.fr

#  -Creative Commons License
#  -This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#  -http://creativecommons.org/licenses/by-nc-sa/4.0/

import inkex
from lxml import etree

def recup(selection,attrib):
	l = []
	for i in xrange(len(selection)):
		selec = selection[i]
		valr = selec.get(attrib)
		l.append(valr)
	return l

def generCircle(y,x,r):
	circle = etree.Element('{http://www.w3.org/2000/svg}circle')
	circle.set('cy',str(y))
	circle.set('cx',str(x))
	circle.set('r',str(r))
	circle.set('fill','#000000')
	circle.set('stroke','#000000')
	circle.set('stroke-width','0')
	return circle

#def onlyRect(selection): A coder !

def toFloat(l):
	for i in xrange(len(l)):
		l[i] = float(l[i])
	return l

class Circle(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)
		self.OptionParser.add_option('--rayon', action = 'store', type = 'float', dest = 'rayon', default = 3.0, help = 'Rayon a entrer')
		self.OptionParser.add_option('--marg', action = 'store', type = 'float', dest = 'marg', default = 10.0, help = 'Marge a entrer')
		self.OptionParser.add_option('--space', action = 'store', type = 'float', dest = 'space', default = 30.0, help = 'Espace a rentrer')

	def effect(self):
		# svg = self.document.getroot()
		# layer = etree.SubElement(svg, 'g')
		# layer.set(inkex.addNS('label', 'inkscape'), 'Layer')
		# layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
		# Faut il ajouter les cercles sur une feuille de calque différente ?

		rayon = self.options.rayon
		marg = self.options.marg
		space =  self.options.space

		selection = (self.selected).values()

		y,x,height,width = [], [], [], []

		if (len(selection))>0:
			y = toFloat(recup(selection,'y'))
			x = toFloat(recup(selection,'x'))
			height = toFloat(recup(selection,'height'))
			width = toFloat(recup(selection,'width'))

			for i in xrange(len(selection)):
				xC = x[i] + marg
				yC = y[i] + marg

				while xC < (x[i] + width[i] - marg):
					while yC < (y[i] + height[i] - marg):
						self.current_layer.append(generCircle(yC,xC,rayon))
						yC += (space + rayon)

					xC += space + rayon
					yC = y[i] + marg

c = Circle()
c.affect()
