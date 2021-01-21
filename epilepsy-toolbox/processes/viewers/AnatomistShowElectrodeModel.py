# -*- coding: utf-8 -*-
#  This software and supporting documentation are distributed by
#      Institut des Neurosciences de Grenoble
#      France
#
# This software is governed by the CeCILL license version 2 under
# French law and abiding by the rules of distribution of free software.
# You can  use, modify and/or redistribute the software under the 
# terms of the CeCILL license version 2 as circulated by CEA, CNRS
# and INRIA at the following URL "http://www.cecill.info". 
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or 
# data to be ensured and,  more generally, to use and operate it in the 
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license version 2 and that you accept its terms.

from brainvisa.processes import *
from brainvisa import anatomist
import pickle
#from editor import ElectrodeEditorDialog

name = 'Anatomist Show Electrode Model'
userLevel = 0
roles = ('viewer',)

def validation():
    anatomist.validation()

signature = Signature(
    'model', ReadDiskItem( 'Electrode Model', 'Electrode Model format' ),
)


def initialization( self ):
  pass

def execution( self, context ):
  self.cylinders = {}
  self.currentColorHue = 0
  self.typeColors = {}

  a = anatomist.Anatomist()
  w = a.createWindow('Sagittal')
  wins = [w,]
  meshes = []
  modelFile = open(self.model.fullPath(), 'r')
  cylinders = pickle.load(modelFile)
  modelFile.close()
  for name in cylinders.keys():
    t = cylinders[name]['type']
    p = cylinders[name]['position']
    v = cylinders[name]['vector']
    r = cylinders[name]['diameter']/2.0
    pEnd = p[0] + v[0]*cylinders[name]['length'], p[1] + v[1]*cylinders[name]['length'], p[2] + v[2]*cylinders[name]['length']
    #print "New cylinder mesh at %.2f, %.2f, %.2f,  radius=%.2f" % (p[0], p[1], p[2], r)
    newCyl = a.toAObject(aims.SurfaceGenerator.cylinder(aims.Point3df(p[0], p[1], p[2]), aims.Point3df(pEnd), r, r, 24, True, True))
    
    # Couleur automatique par catégorie
    if t not in self.typeColors:
        self.currentColorHue = (self.currentColorHue + 40) % 256
        self.typeColors[t] = QtGui.QColor.fromHsv(self.currentColorHue, 245, 220, 255);
    color = self.typeColors[t]
    a.setMaterial(newCyl, diffuse=[color.redF(), color.greenF(), color.blueF(), color.alphaF()])
    meshes.append(newCyl)
    
  a.addObjects(meshes, wins)
      
      #a.addObjects(meshes, [w,])
      #return (w, elec, meshes)
  return (wins,)


