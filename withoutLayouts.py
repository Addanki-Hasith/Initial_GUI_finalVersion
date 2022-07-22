from pyqtgraph.Qt import QtCore
from pyqtgraph.Qt import QtGui

import sys

class Color(QtGui.QWidget):
	def __init__(self,color):
		super(Color,self).__init__()
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(color))

		self.setPalette(palette)
		

class PhaseTiming(QtGui.QWidget):
	def __init__(self,clock_m):
		super(PhaseTiming,self).__init__()
		
		self.clk_m = clock_m
		
		self.layout = QtGui.QVBoxLayout()
		self.title = QtGui.QLabel('Phase Timing Scheme')
		self.title.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.title.setFixedSize(QtCore.QSize(225,25))
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		
		self.stagger_mode = QtGui.QRadioButton("Stagger Mode")
		self.high_prf_mode = QtGui.QRadioButton("High PRF Mode")
		self.max_amb_rej_mode = QtGui.QRadioButton("Max AMB Rej Mode")
		self.dis_post_amb_rej_mode = QtGui.QRadioButton("Dis-POST AMB Rej ")
		
		self.layout.addWidget(self.title)
		self.layout.addWidget(self.stagger_mode)
		self.layout.addWidget(self.high_prf_mode)
		self.layout.addWidget(self.max_amb_rej_mode)
		self.layout.addWidget(self.dis_post_amb_rej_mode)
		
		self.stagger_mode.setToolTip('Selecting Stagger Mode')
		self.high_prf_mode.setToolTip('Selecting High PRF Mode')
		self.max_amb_rej_mode.setToolTip('Selecting Maximum Ambient Rejection Mode')
		self.dis_post_amb_rej_mode.setToolTip('Selecting Disable-Post Ambient Rejection Mode')
		
		self.setLayout(self.layout)		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('lavender'))
		self.setPalette(palette)
		
		self.stagger_mode.clicked.connect(self.mode_0)

		self.high_prf_mode.clicked.connect(self.mode_1)

		self.max_amb_rej_mode.clicked.connect(self.mode_2)

		self.dis_post_amb_rej_mode.clicked.connect(self.mode_3)
		
	def mode_0(self):
# 		config_phaseTimingScheme(0)
		self.disable_select()
		print('done')

	def mode_1(self):
# 		config_phaseTimingScheme(1)
		self.disable_select()
	
	def mode_2(self):
# 		config_phaseTimingScheme(2)
		self.disable_select()
	
	def mode_3(self):
# 		config_phaseTimingScheme(3)
		self.disable_select()		

	def disable_select(self):
		
		self.clk_m.setEnabled(True)
		
		self.clk_m.opacity_effect1.setEnabled(False)
		self.stagger_mode.setDisabled(True)
		self.high_prf_mode.setDisabled(True)
		self.max_amb_rej_mode.setDisabled(True)
		self.dis_post_amb_rej_mode.setDisabled(True)
		
		
class Clocking(QtGui.QWidget):
	def __init__(self,timePar):
		super(Clocking,self).__init__()
		
		self.timingParameter = timePar
		
		self.title = QtGui.QLabel('Clocking Mode')
		self.title.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.title.setFixedSize(QtCore.QSize(225,25))
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		
		self.internal = QtGui.QRadioButton('CLK_MODE_INT')
		self.external = QtGui.QRadioButton('CLC_MODE_EXT')
		self.singleshot = QtGui.QRadioButton('CLC_MODE_SS')
		self.mixedclock = QtGui.QRadioButton('CLC_MODE_MIX')
		
		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect.setOpacity(0.3)
		
		self.internal.setToolTip('Selecting Internal Clock')
		self.external.setToolTip('Selecting External Clock')
		self.singleshot.setToolTip('Selecting Single Shot Mode Clock')
		self.mixedclock.setToolTip('Selecting Mixed Clock')
		
		self.HBox = QtGui.QHBoxLayout()
		self.ExternalClk = QtGui.QLabel('External Clk Frequency')
		self.ExternalClk.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.SelExternal = QtGui.QComboBox()
		
		self.ExternalClk.setGraphicsEffect(self.opacity_effect)
		self.SelExternal.setEnabled(False)
		
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		
		self.title.setGraphicsEffect(self.opacity_effect1)
		
		self.HBox.addWidget(self.ExternalClk)
		self.HBox.addWidget(self.SelExternal)

		self.layout = QtGui.QVBoxLayout()
		self.layout.addWidget(self.title)
		self.layout.addWidget(self.internal)
		self.layout.addWidget(self.external)
		self.layout.addWidget(self.singleshot)
		self.layout.addWidget(self.mixedclock)
		self.layout.addLayout(self.HBox)
		
		self.internal.clicked.connect(self.mode_0)
		self.internal.clicked.connect(self.timingParEnable)

		self.external.clicked.connect(self.mode_1)
		

		self.singleshot.clicked.connect(self.mode_2)
		self.singleshot.clicked.connect(self.timingParEnable)

		self.mixedclock.clicked.connect(self.mode_3)
		
		
		self.setLayout(self.layout)		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('lavender'))
		self.setPalette(palette)
		
		
		self.setLayout(self.layout)

	def mode_0(self):
# 		config_phaseTimingScheme(0)
		self.disable_select()

	def mode_1(self):
# 		config_phaseTimingScheme(1)
		self.opacity_effect.setEnabled(False)
		self.SelExternal.setEnabled(True)
		self.SelExternal.addItems(["None","256 KHz", "512 KHz", "1024 KHz"])
		
		self.SelExternal.currentIndexChanged.connect(self.external_clock_index)
		self.SelExternal.currentIndexChanged.connect(self.timingParEnable)
		self.disable_select()
	
	def mode_2(self):
# 		config_phaseTimingScheme(2)
		
		self.disable_select()
	
	def mode_3(self):
# 		config_phaseTimingScheme(3)
		self.opacity_effect.setEnabled(False)
		self.SelExternal.setEnabled(True)
		self.SelExternal.addItems(["None","32.768 KHz"])
		
		self.SelExternal.currentIndexChanged.connect(self.mixed_clock_index)
		self.SelExternal.currentIndexChanged.connect(self.timingParEnable)
		self.disable_select()		

	def disable_select(self):
		
		self.internal.setDisabled(True)
		self.external.setDisabled(True)
		self.singleshot.setDisabled(True)
		self.mixedclock.setDisabled(True)
		
	def external_clock_index(self,i):
		
		self.SelExternal.setEnabled(False)

	def mixed_clock_index(self,i):
		
		self.SelExternal.setEnabled(False)
	
	def timingParEnable(self):
		self.timingParameter.setEnabled(True)
		self.timingParameter.opacity_effect1.setEnabled(False)
# 		self.timingParameter.opacity_effect2.setEnabled(False)
# 		self.timingParameter.opacity_effect3.setEnabled(False)
# 		self.timingParameter.opacity_effect4.setEnabled(False)

	
class TimingParameters(QtGui.QWidget):
	def __init__(self,ReConvAMB):
		super(TimingParameters,self).__init__()
		
		self.ReConAmbScheme = ReConvAMB
		
		self.layout = QtGui.QVBoxLayout()
# 		self.layout = QtGui.QGridLayout()
		self.hbox1 = QtGui.QHBoxLayout()
		self.hbox2 = QtGui.QHBoxLayout()
		
		self.label1 = QtGui.QLabel('PRPCT value')
		self.label2 = QtGui.QLabel('Exact PRF assigned')
		
		self.parName1 = QtGui.QLabel('PRF (Hz)')
		self.parName2 = QtGui.QLabel('Step Count')
		self.parName1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: blue;")
		self.parName2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: blue;")
		
		self.parName1.setAlignment(QtCore.Qt.AlignCenter)
		self.parName2.setAlignment(QtCore.Qt.AlignCenter)
		self.userval1 = QtGui.QLineEdit()
		self.userval1.setPlaceholderText('Enter PRF Frequency')
		
		self.userval2 = QtGui.QLineEdit()
		self.userval2.setPlaceholderText('Enter Step Count')
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.userval2.setSizePolicy(sizePolicy)
		self.userval1.setSizePolicy(sizePolicy)
		self.hbox1.addWidget(self.parName1)

		self.hbox1.addWidget(self.userval1)
		
		self.hbox2.addWidget(self.parName2)
		self.hbox2.addWidget(self.userval2)

		self.layout.addLayout(self.hbox1)
		self.layout.addLayout(self.hbox2)
		
		self.label1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: blue;")
		self.label2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: blue;")
		
		self.label1.setAlignment(QtCore.Qt.AlignCenter)
		self.label2.setAlignment(QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.label1)
		self.layout.addWidget(self.label2)
		
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.5)
		self.opacity_effect3 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect3.setOpacity(0.5)
		self.opacity_effect4 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect4.setOpacity(0.5)
		self.parName1.setGraphicsEffect(self.opacity_effect1)
		self.parName2.setGraphicsEffect(self.opacity_effect2)
		
		self.label1.setGraphicsEffect(self.opacity_effect3)
		self.label2.setGraphicsEffect(self.opacity_effect4)
		
# 		self.userval1.setEnabled(True)
		self.userval2.setEnabled(False)
		self.userval1.editingFinished.connect(self.textChange_1)
		self.userval2.editingFinished.connect(self.textChange_2)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('lavender'))
		self.setPalette(palette)
		self.setLayout(self.layout)
	
	def textChange_1(self):
		self.userval1.setEnabled(False)
		self.opacity_effect2.setEnabled(False)
		self.userval2.setEnabled(True)
	
	def textChange_2(self):
		self.userval2.setEnabled(False)
		self.opacity_effect3.setEnabled(False)
		self.opacity_effect4.setEnabled(False)
		self.ReConAmbScheme.opacity_effect1.setEnabled(False)
		self.ReConAmbScheme.setEnabled(True)

class ReConv_N_AMBCancelScheme(QtGui.QWidget):
	def __init__(self):
		super(ReConv_N_AMBCancelScheme,self).__init__()
		
		self.layout = QtGui.QVBoxLayout()
		
		self.Hbox1 = QtGui.QHBoxLayout()
		self.Hbox2 = QtGui.QHBoxLayout()
		
		self.ReConvThre = QtGui.QLabel('ReConvergence \nThreshold (V)')
		self.AMBCancel = QtGui.QLabel('AMB Cancellation \nScheme')
		
		self.ReConvThre.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: blue;")
		self.AMBCancel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: blue;")
		self.ReConvThre.setAlignment(QtCore.Qt.AlignCenter)
		self.AMBCancel.setAlignment(QtCore.Qt.AlignCenter)
		
		self.userVal1 = QtGui.QLineEdit()
		self.userVal2 = QtGui.QComboBox()
		
		self.userVal2.addItems(['None', 'ANA-AACM','MCU Ctrl'])
		
		self.userVal1.setPlaceholderText('Enter in Volts')
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.userVal1.setSizePolicy(sizePolicy)
		
		
		self.userVal1.editingFinished.connect(self.ReConvTextChanged)
		self.userVal2.currentIndexChanged.connect(self.ABM_index)
		
# 		self.userVal1.setDisabled(True)
		self.userVal2.setEnabled(False)
		self.Hbox1.addWidget(self.ReConvThre)
		self.Hbox1.addWidget(self.userVal1)
		
		self.Hbox2.addWidget(self.AMBCancel)
		self.Hbox2.addWidget(self.userVal2)
		
		self.layout.addLayout(self.Hbox1)
		self.layout.addLayout(self.Hbox2)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('lavender'))
		self.setPalette(palette)
		
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.5)
		
		self.ReConvThre.setGraphicsEffect(self.opacity_effect1)
		self.AMBCancel.setGraphicsEffect(self.opacity_effect2)
		
		self.setLayout(self.layout)
		
		
	def ReConvTextChanged(self):
		self.userVal1.setEnabled(False)
		self.opacity_effect2.setEnabled(False)
		self.userVal2.setEnabled(True)
	
	def ABM_index(self,i):
		
		self.userVal2.setEnabled(False)

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		
		self.setWindowTitle('AFE 4460 GUI')

		layout_main = QtGui.QHBoxLayout()

		layout_regNlog = QtGui.QVBoxLayout()
		layout_regNlog.addWidget(Color('pink'))
		reg_writeNlog_win = QtGui.QWidget()
		reg_writeNlog_win.setLayout(layout_regNlog)
# 		reg_writeNlog_win.setFixedSize(QtCore.QSize(192,840))

		layout_main.addWidget(reg_writeNlog_win)

		layout_main2 = QtGui.QVBoxLayout()
		layout_main3 = QtGui.QHBoxLayout()
		layout_main4 = QtGui.QHBoxLayout()

		phase_clock = QtGui.QVBoxLayout()
		
		ReConv_N_AMB = ReConv_N_AMBCancelScheme()
		ReConv_N_AMB.setEnabled(False)
		
		self.timingParam = TimingParameters(ReConv_N_AMB)
		self.timingParam.setEnabled(False)
		
		self.clock_m = Clocking(self.timingParam)
		self.clock_m.setEnabled(False)


		phase = PhaseTiming(self.clock_m)
		
		phase.setFixedSize(QtCore.QSize(330,185))
# 		phase.setFixedWidth(384)
		phase_clock.addWidget(phase)

		clc_rem = Color('lavender')

		clc_rem.setFixedWidth(330)
		
		
		
		self.clock_m.setFixedSize(QtCore.QSize(330,210))
		phase_clock.addWidget(self.clock_m)
		
		
		self.timingParam.setFixedSize(330,220)
		phase_clock.addWidget(self.timingParam)
# 		
		
		ReConv_N_AMB.setFixedWidth(330)
		
		phase_clock.addWidget(ReConv_N_AMB)
# 		phase_clock.addWidget(clc_rem)

		layout_main4.addLayout(phase_clock)
		layout_main4.addWidget(Color('pink'))

		btn = QtGui.QPushButton('Global Configurations')
		btn.setFixedSize(QtCore.QSize(450,60))
		layout_main3.addWidget(btn)
		btn1 = QtGui.QPushButton('Per Phase Configurations')
		btn1.setFixedSize(QtCore.QSize(450,60))
		btn1.setDisabled(True)
		layout_main3.addWidget(btn1)
		btn2 = QtGui.QPushButton('Timing Diagram and Power')
		btn2.setFixedSize(QtCore.QSize(450,60))
		btn2.setDisabled(True)
		layout_main3.addWidget(btn2)

		layout_main2.addLayout(layout_main3)
		layout_main2.addLayout(layout_main4)


		layout_main.addLayout(layout_main2)
		widget = QtGui.QWidget()

		widget.setLayout(layout_main)

		self.setCentralWidget(widget)

		self.setFixedSize(QtCore.QSize(1632,880))
		
		
		
# app = QtGui.QApplication(sys.argv)

window = MainWindow()

window.show()		

# app.exec_()
