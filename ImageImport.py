#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Import and register images in the database
#
# (c) Inserm U836 2012-2014 - Manik Bhattacharjee
#
# License GNU GPL v3
#


import sys

# import PyQt5 QtCore and QtGui modules
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

from ImageImportWindow import ImageImportWindow

if __name__ == '__main__':

    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('Image Import')

    # create widget
    w = ImageImportWindow()
    w.setWindowTitle('Image Import - NOT FOR MEDICAL USAGE')
    w.show()

    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))
    # Debug -> evite un pb entre ipython, pdb et qt
    pyqtRemoveInputHook()
    # execute application
    sys.exit(app.exec_())
