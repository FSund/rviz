#!/usr/bin/env python

import roslib; roslib.load_manifest('rviz')
import sys
setattr(sys, 'SELECT_QT_BINDING', 'pyside') # Shiboken
#setattr(sys, 'SELECT_QT_BINDING', 'pyqt') # SIP
import python_qt_binding.QtBindingHelper # @UnusedImport

from QtGui import *
from QtCore import *
import rviz

c = rviz.Config()
foo = c.makeChild( "foo" )
foo.setValue( 17 )
bar = c.makeChild( "bar" )
bar.setValue( "seventeen" )
biff = foo.makeChild( "biff" )
biff.setValue( "3.14159" )
print c.getChild( "foo" ).getValue()
print c.getChild( "bar" ).getValue()
print c.getChild( "baz" ).getValue()
print c.getChild( "foo" ).getChild( "biff" ).getValue()
# print c.getChild( "goo" ).getChild( "biff" ).getValue() # crashes because "goo" does not exist, so getChild("biff") can't be called.

s = c.makeSequence()
s.makeNext().setValue( "a" );
s.makeNext().setValue( "b" );
s2 = c.getSequence()
while s2.hasNext():
    print s2.getNext().getValue()

c.makeChild( "chunk" )
s3 = c.getSequence()
while s3.hasNext():
    print "s3 should not have anything...", s3.getNext().getValue()
print "done"
