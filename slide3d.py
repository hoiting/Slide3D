#!/opt/local/bin/python
from astropy.io import fits
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from scipy.ndimage.filters import median_filter
import sys,getopt
import os.path as path
#import pdb

pg.setConfigOption('leftButtonPan', False)
# Define lookup table (from IDL CT = 13)
'''
r = np.array([0,4,9,13,18,22,27,31,36,40,45,50,54,58,61,64,68,69,72,74,77,79,80,82,83,85,84,86,87,88,86,87,87,87,85,84,84,84,83,79,78,77,76,71,70,68,66,60,58,55,53,46,43,40,36,33,25,21,16,12,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,8,12,21,25,29,33,42,46,51,55,63,67,72,76,80,89,93,97,101,110,114,119,123,131,135,140,144,153,157,161,165,169,178,182,187,191,199,203,208,212,221,225,229,233,242,246,250,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255])
g = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,8,16,21,25,29,38,42,46,51,55,63,67,72,76,84,89,93,97,106,110,114,119,127,131,135,140,144,152,157,161,165,174,178,182,187,195,199,203,208,216,220,225,229,233,242,246,250,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,250,242,238,233,229,221,216,212,208,199,195,191,187,178,174,170,165,161,153,148,144,140,131,127,123,119,110,106,102,97,89,85,80,76,72,63,59,55,51,42,38,34,29,21,17,12,8,0])
b = np.array([0,3,7,10,14,19,23,28,32,38,43,48,53,59,63,68,72,77,81,86,91,95,100,104,109,113,118,122,127,132,136,141,145,150,154,159,163,168,173,177,182,186,191,195,200,204,209,214,218,223,227,232,236,241,245,250,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,246,242,238,233,225,220,216,212,203,199,195,191,187,178,174,170,165,157,152,148,144,135,131,127,123,114,110,106,102,97,89,84,80,76,67,63,59,55,46,42,38,34,25,21,16,12,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
lut = np.vstack((r,g,b)).T
# from matplotlib.cm.jet
r,g,b = list(),list(),list()
import matplotlib.cm as cm
for i in range(256):
	c1,c2,c3,c4 = cm.jet(i)
	r.append(c1)
	g.append(c2)
	b.append(c3)
r, g, b = np.array(r)*255,np.array(g)*255,np.array(b)*255
'''
#for i in g:sys.stdout.write('%s,'%i)
r = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.41935483871,5.64516129032,8.87096774194,12.0967741935,15.3225806452,18.5483870968,21.7741935484,25.0,28.2258064516,31.4516129032,34.6774193548,37.9032258065,41.1290322581,44.3548387097,47.5806451613,50.8064516129,54.0322580645,57.2580645161,60.4838709677,63.7096774194,66.935483871,70.1612903226,73.3870967742,76.6129032258,79.8387096774,83.064516129,86.2903225806,89.5161290323,92.7419354839,95.9677419355,99.1935483871,102.419354839,105.64516129,108.870967742,112.096774194,115.322580645,118.548387097,121.774193548,125.0,128.225806452,131.451612903,134.677419355,137.903225806,141.129032258,144.35483871,147.580645161,150.806451613,154.032258065,157.258064516,160.483870968,163.709677419,166.935483871,170.161290323,173.387096774,176.612903226,179.838709677,183.064516129,186.290322581,189.516129032,192.741935484,195.967741935,199.193548387,202.419354839,205.64516129,208.870967742,212.096774194,215.322580645,218.548387097,221.774193548,225.0,228.225806452,231.451612903,234.677419355,237.903225806,241.129032258,244.35483871,247.580645161,250.806451613,254.032258065,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,254.772727273,250.227272727,245.681818182,241.136363636,236.590909091,232.045454545,227.5,222.954545455,218.409090909,213.863636364,209.318181818,204.772727273,200.227272727,195.681818182,191.136363636,186.590909091,182.045454545,177.5,172.954545455,168.409090909,163.863636364,159.318181818,154.772727273,150.227272727,145.681818182,141.136363636,136.590909091,132.045454545,127.5])
g = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.5,4.5,8.5,12.5,16.5,20.5,24.5,28.5,32.5,36.5,40.5,44.5,48.5,52.5,56.5,60.5,64.5,68.5,72.5,76.5,80.5,84.5,88.5,92.5,96.5,100.5,104.5,108.5,112.5,116.5,120.5,124.5,128.5,132.5,136.5,140.5,144.5,148.5,152.5,156.5,160.5,164.5,168.5,172.5,176.5,180.5,184.5,188.5,192.5,196.5,200.5,204.5,208.5,212.5,216.5,220.5,224.5,228.5,232.5,236.5,240.5,244.5,248.5,252.5,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,252.037037037,248.333333333,244.62962963,240.925925926,237.222222222,233.518518519,229.814814815,226.111111111,222.407407407,218.703703704,215.0,211.296296296,207.592592593,203.888888889,200.185185185,196.481481481,192.777777778,189.074074074,185.37037037,181.666666667,177.962962963,174.259259259,170.555555556,166.851851852,163.148148148,159.444444444,155.740740741,152.037037037,148.333333333,144.62962963,140.925925926,137.222222222,133.518518519,129.814814815,126.111111111,122.407407407,118.703703704,115.0,111.296296296,107.592592593,103.888888889,100.185185185,96.4814814815,92.7777777778,89.0740740741,85.3703703704,81.6666666667,77.962962963,74.2592592593,70.5555555556,66.8518518519,63.1481481481,59.4444444444,55.7407407407,52.037037037,48.3333333333,44.6296296296,40.9259259259,37.2222222222,33.5185185185,29.8148148148,26.1111111111,22.4074074074,18.7037037037,15.0,11.2962962963,7.59259259259,3.88888888889,0.185185185185,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
b = np.array([127.5,132.045454545,136.590909091,141.136363636,145.681818182,150.227272727,154.772727273,159.318181818,163.863636364,168.409090909,172.954545455,177.5,182.045454545,186.590909091,191.136363636,195.681818182,200.227272727,204.772727273,209.318181818,213.863636364,218.409090909,222.954545455,227.5,232.045454545,236.590909091,241.136363636,245.681818182,250.227272727,254.772727273,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,255.0,254.032258065,250.806451613,247.580645161,244.35483871,241.129032258,237.903225806,234.677419355,231.451612903,228.225806452,225.0,221.774193548,218.548387097,215.322580645,212.096774194,208.870967742,205.64516129,202.419354839,199.193548387,195.967741935,192.741935484,189.516129032,186.290322581,183.064516129,179.838709677,176.612903226,173.387096774,170.161290323,166.935483871,163.709677419,160.483870968,157.258064516,154.032258065,150.806451613,147.580645161,144.35483871,141.129032258,137.903225806,134.677419355,131.451612903,128.225806452,125.0,121.774193548,118.548387097,115.322580645,112.096774194,108.870967742,105.64516129,102.419354839,99.1935483871,95.9677419355,92.7419354839,89.5161290323,86.2903225806,83.064516129,79.8387096774,76.6129032258,73.3870967742,70.1612903226,66.935483871,63.7096774194,60.4838709677,57.2580645161,54.0322580645,50.8064516129,47.5806451613,44.3548387097,41.1290322581,37.9032258065,34.6774193548,31.4516129032,28.2258064516,25.0,21.7741935484,18.5483870968,15.3225806452,12.0967741935,8.87096774194,5.64516129032,2.41935483871,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
lut = np.vstack((r,g,b)).T
#lut = np.arange(256) # B/W look-up table


class Slide3D(QtGui.QWidget):
#	pg.setConfigOption('background', 'w')

	im_list = ('p1','p2','p3','p4','p5','p6','p7','p8',)
	# define plot sequence and style
	bSeq        = ('b_cube - b_cont - b_line0'    ,'b_cube'              ,'b_cont'      ,'b_cont+b_line1'    ,'b_cont+b_line2'    ,'b_cont+b_line3'    ,'b_cont+b_line0'    ,)
	bPen        = (pg.mkPen(0.7)                  ,pg.mkPen((30,144,255)), pg.mkPen('c'),pg.mkPen('g')       ,pg.mkPen('m')       ,pg.mkPen('y')       ,pg.mkPen('w')       ,)
	bType       = ('residual'                     ,'data'                ,'fit'         , 'fit'              ,'fit'               ,'fit'               ,'fit'               ,)

	bSeqSubplot = ('b_cube - b_cont - b_line0'    ,'b_cube - b_cont'             ,'b_line1'     ,'b_line2'    ,'b_line3'    ,'b_line0'    ,)
	bPenSubplot = (pg.mkPen(0.7)                  ,pg.mkPen((30,144,255))        , pg.mkPen('g'),pg.mkPen('m'),pg.mkPen('y'),pg.mkPen('w'),)
	bSeqType    = ('residual'                     ,'data'                        ,'fit'         , 'fit'       ,'fit'        ,'fit'        ,)

	rSeq        = ('r_cube - r_cont - r_line0'    ,'r_cube'              ,'r_cont'      ,'r_cont+r_line1'    ,'r_cont+r_line2'    ,'r_cont+r_line3'    ,'r_cont+r_line0'    ,)
	rPen        = (pg.mkPen(0.7)                  ,pg.mkPen('r')         ,pg.mkPen('c') ,pg.mkPen('g')       ,pg.mkPen('m')       ,pg.mkPen('y')       ,pg.mkPen('w')       ,)
	rType       = ('residual'                     ,'data'                ,'fit'         , 'fit'              ,'fit'               ,'fit'               ,'fit'               ,)

	rSeqSubplot = ('r_cube - r_cont - r_line0'    ,'r_cube - r_cont'    ,'r_line1'     ,'r_line2'    ,'r_line3'    ,'r_line0'    , )
	rPenSubplot = (pg.mkPen(0.7)                  ,pg.mkPen('r')        , pg.mkPen('g'),pg.mkPen('m'),pg.mkPen('y'),pg.mkPen('w'), )
	rSeqType    = ('residual'                     ,'data'                        ,'fit'         , 'fit'       ,'fit'        ,'fit',)

	app = QtGui.QApplication([])

	# No 1 window
	mw = QtGui.QMainWindow()
	mw.resize(1400,600) 	# Window size. 
	view = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default
	# No 2 window
	mw2 = QtGui.QMainWindow()
	mw2.resize(800,700) 	
	view2 = pg.GraphicsLayoutWidget()  ## GraphicsView with GraphicsLayout inserted by default


	def __init__(self,data):
		# Load data
		self.data, self.z, self.x, self.y = data, data['z'] ,round(data['b_cube'].shape[2]/2.), round(data['b_cube'].shape[1]/2.)
		# When 1d spectra. special case. 
		if self.x == 1: self.x = 0
		if self.y == 1: self.y = 0

		self.ncomp = data['ncomp']
		self.only_1side = data['only_1side']
		self.p_name = data['p_name']
		self.this_comp = 0 # start with displaying the combined maps
		self.b_channel_width = data['b_lambda'][1] - data['b_lambda'][0] 
		self.r_channel_width = data['r_lambda'][1] - data['r_lambda'][0] 
		self.ysize, self.xsize = data['b_cube'].shape[1:3]

		
		# Overwrite blue Seq/Pen/Type with red if one-sided only
		if self.only_1side == 1:
			self.bSeq = self.rSeq
			self.bPen = self.rPen
			self.bType = self.rType
			self.bSeqSubplot = self.rSeqSubplot
			self.bPenSubplot = self.rPenSubplot
		
		# Setup plots
		self.mw.setWindowTitle('Slide3D:%s'% data['object'])
		self.mw2.setWindowTitle('Slide3D:%s'% data['object'])
		super(Slide3D,self).__init__()

		self.btn0 = QtGui.QRadioButton('All',self)
		self.btn0.setChecked(True)
		self.btn1 = QtGui.QRadioButton('Comp. 1',self)
		self.btn2 = QtGui.QRadioButton('Comp. 2',self)
		self.btn3 = QtGui.QRadioButton('Comp. 3',self)
		
		self.btn0.clicked.connect(self.buttonClicked(0))
		self.btn1.clicked.connect(self.buttonClicked(1))
		self.btn2.clicked.connect(self.buttonClicked(2))
		self.btn3.clicked.connect(self.buttonClicked(3))
		# disable components not available
		for i in range(ncomp+1,4):
			exec('self.btn%d.setCheckable(False)'%i)
			exec('self.btn%d.setEnabled(False)'%i)

		self.upbtn = QtGui.QPushButton("Up",self)
		self.dnbtn = QtGui.QPushButton("Down",self)
		self.lebtn = QtGui.QPushButton("Left",self)
		self.ribtn = QtGui.QPushButton("Right",self)
		self.exitbtn  = QtGui.QPushButton("Close all",self)
		
		self.upbtn.clicked.connect(self.buttonMoveClicked('up'))
		self.dnbtn.clicked.connect(self.buttonMoveClicked('down'))
		self.lebtn.clicked.connect(self.buttonMoveClicked('left'))
		self.ribtn.clicked.connect(self.buttonMoveClicked('right'))
		self.exitbtn.clicked.connect(self.closeIt)

#		import pdb
#		pdb.set_trace()
#		QtCore.QObject.connect(self.view2, QtCore.SIGNAL('triggered()'), self.closeIt)
#		QtCore.QObject.connect(self.view , QtCore.SIGNAL('triggered()'), self.closeIt)

#		self.connect(self.mw2, QtCore.SIGNAL('triggered()'), self.closeIt)
#		self.app.aboutToQuit.connect(self.closeIt) # myExitHandler is a callable
#		self.mw.closeEvent()
		
		# check box for plotting 1 sigma
		self.showSigmaBox = QtGui.QCheckBox('Show 1 Sgima', self)
		self.showSigmaBox.setChecked(True)
		self.showSigmaBox.stateChanged.connect(self.changePlotSigma)
		# check box for plotting fit 
		self.plotFitBox   = QtGui.QCheckBox('Plot Fit', self)
		self.plotFitBox.setChecked(True)
		self.plotFitBox.stateChanged.connect(self.changePlotFit)
		
		# Layout
		cw = QtGui.QWidget()
		self.mw.setCentralWidget(cw)
		vbox = QtGui.QVBoxLayout()
		cw.setLayout(vbox)

		vbox.addWidget(self.view)

		gridbox = QtGui.QGridLayout()

		gridbox.addWidget(self.upbtn,1,2)
		gridbox.addWidget(self.dnbtn,3,2)
		gridbox.addWidget(self.lebtn,2,1)
		gridbox.addWidget(self.ribtn,2,3)

		gridbox.addWidget(self.btn0,0,0)
		gridbox.addWidget(self.btn1,1,0)
		gridbox.addWidget(self.btn2,2,0)
		gridbox.addWidget(self.btn3,3,0)
		gridbox.addWidget(self.exitbtn,3,5)
		
		gridbox.addWidget(self.showSigmaBox,0,5)
		gridbox.addWidget(self.plotFitBox,0,6)
		
#		gridbox.addItem(QtGui.QSpacerItem(10,10),2,7,columnSpan=10)
		vbox.addLayout(gridbox)		
		
		self.statusBar = QtGui.QStatusBar()
		gridbox.addWidget(self.statusBar,3,15,1,1)

		# pyqtgraph pannels
		if only_1side == 0:
			self.blueax = self.view.addPlot(colspan=4,rowspan=1)
			self.redax = self.view.addPlot(colspan=4,rowspan=1)
			self.blueax.setAutoVisible(y=True)
			self.redax.setAutoVisible(y=True)
		else:
			self.redax = self.view.addPlot(colspan=8,rowspan=1)
			self.redax.setAutoVisible(y=True)

			
		self.view.nextRow()
		self.o2ax = self.view.addPlot(colspan=2,rowspan=1)
		self.hbax = self.view.addPlot(colspan=2,rowspan=1)
		self.haax = self.view.addPlot(colspan=2,rowspan=1)
		self.s2ax = self.view.addPlot(colspan=2,rowspan=1)

#		self.view.nextRow()
#		self.p1ax = self.view.addPlot()
#		self.p2ax = self.view.addPlot()
#		self.p3ax = self.view.addPlot()
#		self.p4ax = self.view.addPlot()
#		self.p5ax = self.view.addPlot()
#		self.p6ax = self.view.addPlot()
#		self.p7ax = self.view.addPlot()
#		self.p8ax = self.view.addPlot()


##############################################
		# Layout for window 2
		cw2 = QtGui.QWidget()
		self.mw2.setCentralWidget(cw2)
		vbox2 = QtGui.QVBoxLayout()
		cw2.setLayout(vbox2)
		vbox2.addWidget(self.view2)

		self.exitbtn2  = QtGui.QPushButton("Close all",self)
		self.exitbtn2.clicked.connect(self.closeIt)
		gridbox2 = QtGui.QGridLayout()
		gridbox2.addWidget(self.exitbtn2,0,0)
		gridbox2.addItem(QtGui.QSpacerItem(3,1),0,1,columnSpan=3)

		vbox2.addLayout(gridbox2)
		
		self.p1ax = self.view2.addPlot()
		self.p2ax = self.view2.addPlot()
		self.p3ax = self.view2.addPlot()
		self.p4ax = self.view2.addPlot()
		self.view2.nextRow()
		self.p5ax = self.view2.addPlot()
		self.p6ax = self.view2.addPlot()
		self.p7ax = self.view2.addPlot()
		self.p8ax = self.view2.addPlot()
##############################################

		# Hide subPlot label
		self.p_list  = (self.p1ax,self.p2ax,self.p3ax,self.p4ax,
						self.p5ax,self.p6ax,self.p7ax,self.p8ax,) # panel list

		for ax in (self.o2ax,self.hbax,self.haax,self.s2ax):
			ax.showAxis('left',show=False)
	
		for p,im in zip(self.p_list,self.im_list):
			if not data[im] is None:p.vb.mousePressEvent = self.onClick

		for p in self.p_list:p.setAspectLocked(True,ratio=1) # lock aspect ratio
		# Connect image plots and spectral plots
		self.vb = self.p1ax.vb
		self.vb.mousePressEvent = self.onClick
		# Plotting stuff
		self.subPlotIndex()   # make subPlotIndex
		self.plotSpectra()  # initialize spectral plots
		self.showImages()                # initialize image plots
		self.mw.show()
		self.mw2.show()
		return
	# end of __init__
	def closeIt(self):
		print "Closing...." 
		self.app.closeAllWindows()

	def changePlotFit(self,state):
		bool = state == QtCore.Qt.Checked 
		if only_1side == 0:
			for i,type in enumerate(self.bType):
				if type == 'fit' and self.blueax_item[i] is not None:
					self.blueax_item[i].setVisible(bool)
		for i,type in enumerate(self.rType):
			if type == 'fit' and self.redax_item[i] is not None:
				self.redax_item[i].setVisible(bool)
		for i,type in enumerate(self.bSeqType):
			if type == 'fit' and self.o2ax_item[i] is not None:
				self.o2ax_item[i].setVisible(bool)
				self.hbax_item[i].setVisible(bool)
		for i,type in enumerate(self.rSeqType):
			if type == 'fit' and self.haax_item[i] is not None:
				self.haax_item[i].setVisible(bool)
				self.s2ax_item[i].setVisible(bool)
				
	def changePlotSigma(self,state):
		bool = state == QtCore.Qt.Checked 
		for ax in (self.redax_resid,self.o2ax_resid,self.hbax_resid,self.haax_resid,self.s2ax_resid):
			ax.setVisible(bool)
		if only_1side ==0:
			self.blueax_resid.setVisible(bool)

	def buttonMoveClicked(self,motion):
		def callback():
			if motion == 'up':
				if self.y < self.ysize - 1:
					self.y = self.y + 1
				else:
					msg = "Can't move up anymore."
					print msg
					self.statusBar.showMessage(msg,2000)
			if motion == 'down':
				if self.y > 0:
					self.y = self.y - 1
				else:
					msg = "Can't move down anymore."
					print msg
					self.statusBar.showMessage(msg,2000)			
			if motion == 'left':
				if self.x > 0:
					self.x = self.x - 1
				else:
					msg = "Can't move left anymore."
					print msg
					self.statusBar.showMessage(msg,2000)
			if motion == 'right':
				if self.x < self.xsize - 1:
					self.x = self.x + 1
				else:
					msg = "Can't move right anymore."
					print msg
					self.statusBar.showMessage(msg,2000)
			self.plotSpectra()
			for v,h in zip(self.vLine_list,self.hLine_list):
				v.setPos(self.x + 0.5)
				h.setPos(self.y + 0.5)
			self.posText.setText(text = '(%d,%d)' % (self.x,self.y))
			self.setTitle()
		return callback

	def buttonClicked(self,comp):
		def callback():
			if comp <= ncomp:
				self.this_comp = comp
				self.showImages()
				if comp == 0:
					msg = "Displaying sum of all components"
					print msg
					self.statusBar.showMessage(msg)
				else:
					msg = "Displaying Comp. %d." % comp
					print msg
					self.statusBar.showMessage(msg)
			else:
				msg = "Can't display. There is no Comp. %d." % comp
				print msg
				self.statusBar.showMessage(msg)				
		return callback

	def getData(self,string):
		'''
		Perform +/- calculation according to string and return data
		string format: 'key1 + key2 - key3 ...'
		'''
		def notminusone(x):
			if x == -1: return 999
			return x
		string = string.replace(' ','') # remove spaces
		if not string.startswith('+'):string = '+' + string
		first = True
		while string != '':
			nextpos = min( map(notminusone, (string[1:].find('+'),string[1:].find('-'),len(string[1:]) ) ) )
			if first is False and string[0] == '+':  # add data
				out = out + self.data[string[1:nextpos+1]][:,int(self.y),int(self.x)]
			if first is False and string[0] == '-':  # subtract data
				self.data[string[1:nextpos+1]][:,int(self.y),int(self.x)].shape
				out = out - self.data[string[1:nextpos+1]][:,int(self.y),int(self.x)]
			if first:
				out = self.data[string[1:nextpos+1]][:,int(self.y),int(self.x)]
				first = False
			string = string[nextpos+1:]
		return out
		
	def subPlotIndex(self):
		data = self.data
		ran = 3726*(1+self.z)+np.array([-30,30])
		if only_1side == 0: 
			self.o2indx = np.where(np.logical_and(data['b_lambda'] > ran[0], data['b_lambda'] < ran[1]) )[0]
		else:
			self.o2indx = np.where(np.logical_and(data['r_lambda'] > ran[0], data['r_lambda'] < ran[1]) )[0]			
		ran = 4959*(1+self.z)+np.array([-120,70])
		if only_1side == 0: 
			self.hbindx = np.where(np.logical_and(data['b_lambda'] > ran[0], data['b_lambda'] < ran[1]) )[0]
		else:
			self.hbindx = np.where(np.logical_and(data['r_lambda'] > ran[0], data['r_lambda'] < ran[1]) )[0]
		ran = 6563*(1+self.z)+np.array([-35,40])
		self.haindx = np.where(np.logical_and(data['r_lambda'] > ran[0], data['r_lambda'] < ran[1]) )[0]
		ran = 6731*(1+self.z)+np.array([-30,20])
		self.s2indx = np.where(np.logical_and(data['r_lambda'] > ran[0], data['r_lambda'] < ran[1]) )[0]

	def plotSpectra(self):
		## fix xrange if this is not the first loop
		if self.redax.viewRange()[0] != [0,1]:
			prevXRange = self.redax.viewRange()[0]
		
		def plotSigma(l = 'b_lambda',err = 'b_cube_err', index = None):
			color = pg.mkBrush(0.3)
			if index is None:index = np.arange(self.data[l].shape[0])
			try:
				p1 = pg.PlotDataItem(self.data[l][index],-1 * self.data[err][index,int(self.y),int(self.x)])
				p2 = pg.PlotDataItem(self.data[l][index],     self.data[err][index,int(self.y),int(self.x)])
				p1.curve.path , p2.curve.path = p1.curve.generatePath(*p1.curve.getData()), p2.curve.generatePath(*p2.curve.getData())
				item = pg.FillBetweenItem(p1, p2, brush = color)
			except:
				item = pg.PlotCurveItem(self.data[l][index],self.data[l][index]*0) # return trash
				item.setVisible(False)	
			return item
		data = self.data
		# blueax # blue sequence
		if only_1side == 0:
			self.blueax.clear()
			self.blueax_item = list()
			self.blueax_resid = plotSigma(l = 'b_lambda',err = 'b_cube_err')
			self.blueax.addItem(self.blueax_resid)
			for seq,pen in zip(self.bSeq,self.bPen):
				try:
					x = data['b_lambda']
#					x = np.hstack( (x - self.b_channel_width/2.,x[-1] + self.b_channel_width/2. ))
					item = pg.PlotCurveItem(x,self.getData(seq),pen=pen)
					self.blueax_item.append(item)
					self.blueax.addItem(item)
				except:
					self.blueax_item.append(None)
		#redax
		self.redax.clear()
		self.redax_item = list()
		self.redax_resid = plotSigma(l = 'r_lambda',err = 'r_cube_err')
		self.redax.addItem(self.redax_resid)
		for seq,pen in zip(self.rSeq,self.rPen):
			try:
				x = data['r_lambda']
#				x = np.hstack( (x - self.r_channel_width/2.,x[-1] + self.r_channel_width/2. ))
				item = pg.PlotCurveItem(x,self.getData(seq),pen=pen)
				self.redax_item.append(item)
				self.redax.addItem(item)
			except:
				self.redax_item.append(None)

		# o2ax
		self.o2ax.clear()
		self.o2ax_item = list()
		if only_1side ==0:
			self.o2ax_resid = plotSigma(l = 'b_lambda',err = 'b_cube_err',index = self.o2indx)
		else:
			self.o2ax_resid = plotSigma(l = 'r_lambda',err = 'r_cube_err',index = self.o2indx)			
		self.o2ax.addItem(self.o2ax_resid)
		for seq,pen in zip(self.bSeqSubplot,self.bPenSubplot):
			try:
				x = data['b_lambda'][self.o2indx] if only_1side == 0 else data['r_lambda'][self.o2indx]
				x = np.hstack( (x - self.b_channel_width/2.,x[-1] + self.b_channel_width/2. ))
				item = pg.PlotCurveItem(x,self.getData(seq)[self.o2indx],pen=pen,stepMode=True)
				self.o2ax_item.append(item)
				self.o2ax.addItem(item)
			except:
				self.o2ax_item.append(None)
		# hbax
		self.hbax.clear()
		self.hbax_item = list()
		if only_1side ==0:
			self.hbax_resid = plotSigma(l = 'b_lambda',err = 'b_cube_err', index = self.hbindx)
		else:
			self.hbax_resid = plotSigma(l = 'r_lambda',err = 'r_cube_err', index = self.hbindx)			
		self.hbax.addItem(self.hbax_resid)
		for seq,pen in zip(self.bSeqSubplot,self.bPenSubplot):
			try:
				x = data['b_lambda'][self.hbindx] if only_1side == 0 else data['r_lambda'][self.hbindx]
				x = np.hstack( (x - self.b_channel_width/2.,x[-1] + self.b_channel_width/2. ))
				item = pg.PlotCurveItem(x,self.getData(seq)[self.hbindx],pen=pen,stepMode=True)
				self.hbax_item.append(item)
				self.hbax.addItem(item)
			except:
				self.hbax_item.append(None)

			# haax
		self.haax.clear()
		self.haax_item = list()
		self.haax_resid = plotSigma(l = 'r_lambda',err = 'r_cube_err', index = self.haindx)
		self.haax.addItem(self.haax_resid)
		for seq,pen in zip(self.rSeqSubplot,self.rPenSubplot):
			try:
				x = data['r_lambda'][self.haindx]
				x = np.hstack( (x - self.r_channel_width/2.,x[-1] + self.r_channel_width/2. ))
				item = pg.PlotCurveItem(x,self.getData(seq)[self.haindx],pen=pen,stepMode=True)
				self.haax_item.append(item)
				self.haax.addItem(item)
			except:
				self.haax_item.append(None)				
		# s2ax
		self.s2ax.clear()
		self.s2ax_item = list()
		self.s2ax_resid = plotSigma(l = 'r_lambda',err = 'r_cube_err', index = self.s2indx)
		self.s2ax.addItem(self.s2ax_resid)
		for seq,pen in zip(self.rSeqSubplot,self.rPenSubplot):
			try:
				x = data['r_lambda'][self.s2indx]
				x = np.hstack( (x - self.r_channel_width/2.,x[-1] + self.r_channel_width/2. ))
				item = pg.PlotCurveItem(x,self.getData(seq)[self.s2indx],pen=pen,stepMode=True)
				self.s2ax_item.append(item)
				self.s2ax.addItem(item)
			except:
				self.s2ax_item.append(None)

		self.changePlotSigma(self.showSigmaBox.checkState())
		self.changePlotFit(self.plotFitBox.checkState())
		if only_1side == 0: 
#			self.blueax.enableAutoRange(x=False)
#			self.blueax.enableAutoRange(y=True)
			self.blueax.autoRange(items = self.blueax.items[1:])			
#		self.redax.enableAutoRange(x=False)
#		self.redax.enableAutoRange(y=True)
		self.redax.autoRange(items = self.redax.items[1:])
		self.o2ax.autoRange(items = self.o2ax.items[1:])
		self.hbax.autoRange(items = self.hbax.items[1:])
		self.haax.autoRange(items = self.haax.items[1:])
		self.s2ax.autoRange(items = self.s2ax.items[1:])
		if 'prevXRange' in locals():
			self.redax.setXRange(*prevXRange,padding=0)

	def showImages(self):
		for p in self.p_list:p.clear()
		self.vLine_list,self.hLine_list = list(),list()
		for p,im_key in zip(self.p_list,self.im_list):
			if self.data[im_key] is None:
				im = np.zeros((self.data['r_cube'].shape[1:])[::-1])
				im[0,0] = 1
			else:
				if len(self.data[im_key].shape) == 3:
					im = self.data[im_key][self.this_comp,:,:].copy()
				if len(self.data[im_key].shape) == 2:
					im = self.data[im_key].copy()
			if im_key == 'p7': # velocity field
				ind = np.isnan(im)
				im[ind] = 0 # remove nan			
				mim = median_filter(im,size=(5,5),mode='wrap') # median filter to remove outliers
				im[ind] = np.nanmin(im) # remove nan
				min,max = np.nanmin(mim),np.nanmax(mim)
				p.addItem(pg.ImageItem(im,lut=lut,levels=(min,max),border=pg.mkPen('w')))
			elif im_key == 'p8': # velocity dispersion 
				im[np.isnan(im)] = 0 # remove nan
				mim = median_filter(im,size=(5,5),mode='wrap') # median filter to remove outliers
				min,max = np.nanmin(mim),np.nanmax(mim)
				p.addItem(pg.ImageItem(im,lut=lut,levels=(min,max),border=pg.mkPen('w')))
			else:	
				im[np.isnan(im)] = 0 # remove nan			
				mim = median_filter(im,size=(5,5),mode='wrap') # median filter to remove outliers
				min,max = np.nanmin(mim),np.nanmax(mim)
				p.addItem(pg.ImageItem(im,lut=lut,levels = (min,max),border=pg.mkPen('w')))
			vLine = pg.InfiniteLine(angle=90, movable=False)
			hLine = pg.InfiniteLine(angle=0, movable=False)
			self.vLine_list.append(vLine)
			self.hLine_list.append(hLine)
			p.addItem(vLine, ignoreBounds=True)
			p.addItem(hLine, ignoreBounds=True)
#			p.setRange(xRange = (0,25),yRange = (0,38))
#			p.setAspectLocked(False)
			vLine.setPos(self.x + 0.5)
			hLine.setPos(self.y + 0.5)
			p.setMouseEnabled(False,False)


		# x,y position	
		self.posText = pg.TextItem( text = "(%d,%d)" % (self.x,self.y), anchor = (0.1,0.8))
		self.p1ax.addItem(self.posText)
		# title
		self.setTitle()

	def setTitle(self):
		for p,im_key in zip(self.p_list,self.im_list):
			if self.data[im_key] is None:
				p.setTitle('<p>%s<br>%.2e<br>S/N:%.1f<\p>'% ('None',np.nan,np.nan))
			else:
				if len(self.data[im_key].shape) == 3:
					im = self.data[im_key][self.this_comp,:,:] 
					im_err = self.data[im_key+'_ERR'][self.this_comp,:,:] 
				if len(self.data[im_key].shape) == 2:
					im = self.data[im_key][:,:] 
					im_err = self.data[im_key+'_ERR'][:,:] 
				if im_key != 'p7' and im_key != 'p8':
					p.setTitle('<p>%s<br>%.2e<br>S/N:%.1f<\p>'% 
					           (self.p_name[im_key],im[int(self.x),int(self.y)],abs(im[int(self.x),int(self.y)]/im_err[int(self.x),int(self.y)])))
				else:
					p.setTitle('<p>%s<br>%.2e<br>ERR:%.1f<\p>'% 
					           (self.p_name[im_key],im[int(self.x),int(self.y)],im_err[int(self.x),int(self.y)]) )

	def onClick(self,ev):
		if (ev.button() == QtCore.Qt.LeftButton):
			self.x =  round(self.vb.mapToView(ev.pos()).x())
			self.y =  round(self.vb.mapToView(ev.pos()).y())

			if 0 <= self.x < self.data['r_cube'].shape[2] and 0 <= self.y < self.data['r_cube'].shape[1]: 
				self.plotSpectra()
				for v,h in zip(self.vLine_list,self.hLine_list):
					v.setPos(self.x + 0.5)
					h.setPos(self.y + 0.5)
				self.posText.setText(text = '(%d,%d)' % (self.x,self.y))
				self.setTitle()
				ev.accept()


##################################### MAIN ##########################################
if __name__=='__main__':
	# get key variables from input
	version = "Slid3d v5 (by I-Ting Ho; Jan 7 2017)"
	scale_factor =1.
	data_path = './'
	usage = '''
	slid3d.py -c [configuration file] 
	          -p [path to data = ./] 
	          -z [redshift = 0.05 or from Z_LZIFU in LZIFU_CUBE_FILE header0] 
	          -s [scale factor = 1. normally not required.]
	          -h [= --help] -v [= --version]
	          B_CUBE_FILE R_CUBE_FILE LZIFU_CUBE_FILE  (for 2-sided data)
	          or 
	          CUBE_FILE LZIFU_CUBE_FILE (for 1-sided data)
	FILE can be .fits or .fits.gz (slower to launch)
	'''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"c:z:s:p:vh",["version","help"])
	except getopt.GetoptError:
		print usage
		sys.exit()
	for opt, arg in opts:
		if opt in ('-h','--help'):
			print usage
			sys.exit()
		elif opt in ("-c"):
			config_file = arg
		elif opt in ("-z"):
			z = float(arg)
		elif opt in ("-s"):
			scale_factor = float(arg)
		elif opt in ("-p"):
			data_path = arg + '/'
		elif opt in ("-v","--version"):
			print version
			sys.exit()
	if len(args) == 3:
		only_1side = 0 # 2-sided data
		b_cube_name = args[0]
		r_cube_name = args[1]
		lzifu_cube_name = args[2]
	elif len(args) == 2:
		only_1side = 1 # 1-sided data
		r_cube_name = args[0]
		b_cube_name = 'NaN'
		lzifu_cube_name = args[1]
	else:
		print usage
		sys.exit()
	if config_file is None or b_cube_name is None or r_cube_name is None or lzifu_cube_name is None:
		print usage
		sys.exit()

	# Load in red and blue cubes
	try:
		if only_1side == 0: b_hdu = fits.open(data_path + b_cube_name,do_not_scale_image_data=True)
	except:
		print "Cannot open "+ data_path + b_cube_name
		sys.exit()
	try:
		r_hdu = fits.open(data_path + r_cube_name,do_not_scale_image_data=True)
	except:
		print "Cannot open "+ data_path + r_cube_name
		sys.exit()

	r_hdr  = r_hdu[0].header
	r_cube = r_hdu[0].data
	r_cube_err = np.sqrt( r_hdu[1].data )
	r_hdu.close()
	r_cube,r_cube_err = r_cube * scale_factor,r_cube_err * scale_factor
	if only_1side == 0:
		b_hdr  = b_hdu[0].header
		b_cube = b_hdu[0].data
		b_cube_err = np.sqrt( b_hdu[1].data )
		b_hdu.close()
		b_cube,b_cube_err = b_cube* scale_factor,b_cube_err * scale_factor
	else:
		b_cube = np.zeros((2,r_cube.shape[1],r_cube.shape[2]))
		b_cube_err = np.zeros((2,r_cube.shape[1],r_cube.shape[2]))
	
	# construct wavelength vector
	if only_1side == 0:
	 	if not 'CRPIX3' in b_hdr.keys():
 			b_hdr['CRPIX3'] = 0
	if not 'CRPIX3' in r_hdr.keys():
		r_hdr['CRPIX3'] = 0
	
	if only_1side == 0:
		b_lambda = (np.arange(b_hdr['NAXIS3']) + 1 -b_hdr['CRPIX3']) * b_hdr['CDELT3'] + b_hdr['CRVAL3']
	else:
		b_lambda = np.zeros(2)
	r_lambda = (np.arange(r_hdr['NAXIS3']) + 1 -r_hdr['CRPIX3']) * r_hdr['CDELT3'] + r_hdr['CRVAL3']


	# read in cubes in lzifu_cube
	try:
		lzifu_hdu = fits.open(lzifu_cube_name)
	except:
		print "Cannot open " + lzifu_cube_name
		sys.exit()
	lzifu_hdr = lzifu_hdu[0].header
	if only_1side == 0:
		b_cont = lzifu_hdu['B_CONTINUUM'].data
		r_cont = lzifu_hdu['R_CONTINUUM'].data
	else:
		b_cont = np.zeros((2,r_cube.shape[1],r_cube.shape[2]))
		r_cont = lzifu_hdu['CONTINUUM'].data

#	b_cont_mask,r_cont_mask = lzifu_hdu['B_CONT_MASK'].data,lzifu_hdu['R_CONT_MASK'].data
	if not 'z' in locals() :
		if 'Z_LZIFU' in lzifu_hdr.keys():
			z = lzifu_hdr['Z_LZIFU']
			print 'No input redshift. Take from FITS header Z_LZIFU = %6.5f' % z
		else:
			z = 0.05 # Default z 
			print 'No input redshift. Take default value = %6.5f' % z

	try:
		object = lzifu_hdr['OBJECT']
	except:
		object = 'NONAME'

	ncomp = int(lzifu_hdr['NCOMP'])	
	b_line,r_line = list(),list()
	if only_1side == 0:
		b_line.append(lzifu_hdu['B_LINE'].data)
		r_line.append(lzifu_hdu['R_LINE'].data)
	else:
		b_line.append(np.zeros((2,r_cube.shape[1],r_cube.shape[2])))
		r_line.append(lzifu_hdu['LINE'].data)		
	for i in range(1,ncomp+1):
		if only_1side == 0:
			b_line.append(lzifu_hdu['B_LINE_COMP%d'% (i)].data)
			r_line.append(lzifu_hdu['R_LINE_COMP%d'% (i)].data)
		else:
			b_line.append(np.zeros((2,r_cube.shape[1],r_cube.shape[2])))
			r_line.append(lzifu_hdu['LINE_COMP%d'% (i)].data)

	# [br]_line = (total, comp1,comp2...)

	# initialize panel keys and extnames
	p_keys = ['p1','p2','p3','p4','p5','p6','p7','p8']
	p_ext  = dict()
	for key in p_keys:
		p_ext[key] = '#@@#'

	# read in configuration file and put then in fits_suffix and panel_label
	f = open(config_file, 'r')
	for string in f:
		if string[0] !='#':
			dum = string.strip().split(',')
			if len(dum) == 2 and dum[0] in p_ext.keys():
				p_ext[dum[0]] = dum[1].upper()
	
	def rot_images(image):
	# pyqtgraph has strange x,y arrangement. rotate images.
		if len(image.shape) == 3:
			out = np.zeros((image.shape[0],image.shape[2],image.shape[1]))
			for i in range(image.shape[0]):out[i,:,:] = np.flipud(np.rot90(image[i,:,:],1))
		if len(image.shape) == 2:
#			out = np.zeros((image.shape[2],image.shape[1]))
			out = np.flipud(np.rot90(image[:,:],1))
		return out
		
	# Put images in p_images
	p_images = dict()

	for p,extname in p_ext.iteritems():
		if extname is '':
			print "%s is not set in the config file." % (p)
			p_images[p] = None
			continue
		try:
			p_images[p] = rot_images(lzifu_hdu[extname].data)
			try:
				p_images[p+'_ERR'] = rot_images(lzifu_hdu[extname+'_ERR'].data)
			except:
				p_images[p+'_ERR'] = np.zeros(p_images[p].shape) + np.nan
		except:
			print "Can't load %s into %s." %(extname,p)
			p_images[p] = None


	# Finish loading data Close the HDU.
	lzifu_hdu.close()
	# Create master data dictionary
	data = {'b_lambda':b_lambda,'b_cube':b_cube,'b_cube_err':b_cube_err,'b_cont':b_cont, 
			'r_lambda':r_lambda,'r_cube':r_cube,'r_cube_err':r_cube_err,'r_cont':r_cont, 
			'z':z,'ncomp':ncomp,'p_name':p_ext ,'object'    :object    ,'only_1side':only_1side}
	data = dict(data,**p_images)
	for i in range(0,ncomp+1):
		data['b_line%d'%(i)] = b_line[i]
		data['r_line%d'%(i)] = r_line[i]
	# Send to Slide3D
	slide3d = Slide3D(data)

	QtGui.QApplication.instance().exec_()
