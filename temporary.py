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
	def __init__(self):
		super(PhaseTiming,self).__init__()
		
# 		self.clk_m = clock_m
		
		self.layout = QtGui.QVBoxLayout()
		self.title = QtGui.QLabel('Phase Timing Scheme')
		self.title.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.title.setFixedSize(QtCore.QSize(225,25))
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		
		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect.setOpacity(0.5)
		self.title.setGraphicsEffect(self.opacity_effect)
		
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
		
# 		self.clk_m.setEnabled(True)
		
# 		self.clk_m.opacity_effect1.setEnabled(False)
		self.stagger_mode.setDisabled(True)
		self.high_prf_mode.setDisabled(True)
		self.max_amb_rej_mode.setDisabled(True)
		self.dis_post_amb_rej_mode.setDisabled(True)
	
	def WidgetEnable(self):
		self.setEnabled(True)
		self.opacity_effect.setEnabled(False)
		
		
class Clocking(QtGui.QWidget):
	def __init__(self):
		super(Clocking,self).__init__()
		
# 		self.timingParameter = timePar
		
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
# 		self.internal.clicked.connect(self.timingParEnable)

		self.external.clicked.connect(self.mode_1)
		

		self.singleshot.clicked.connect(self.mode_2)
# 		self.singleshot.clicked.connect(self.timingParEnable)

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
# 		self.SelExternal.currentIndexChanged.connect(self.timingParEnable)
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
# 		self.SelExternal.currentIndexChanged.connect(self.timingParEnable)
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
	
	
	def WidgetEnable(self):
		self.setEnabled(True)
		self.opacity_effect1.setEnabled(False)
		
		
# 	def timingParEnable(self):
# 		self.timingParameter.setEnabled(True)
# 		self.timingParameter.opacity_effect1.setEnabled(False)
# 		self.timingParameter.opacity_effect2.setEnabled(False)
# 		self.timingParameter.opacity_effect3.setEnabled(False)
# 		self.timingParameter.opacity_effect4.setEnabled(False)

	
class TimingParameters(QtGui.QWidget):
	def __init__(self):
		super(TimingParameters,self).__init__()
		
# 		self.ReConAmbScheme = ReConvAMB
		
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
		self.opacity_effect1.setOpacity(0.3)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.3)
		self.opacity_effect3 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect3.setOpacity(0.3)
		self.opacity_effect4 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect4.setOpacity(0.3)
		self.parName1.setGraphicsEffect(self.opacity_effect1)
		self.parName2.setGraphicsEffect(self.opacity_effect2)
		
		self.label1.setGraphicsEffect(self.opacity_effect3)
		self.label2.setGraphicsEffect(self.opacity_effect4)
		
# 		self.userval1.setEnabled(False)
		self.userval2.setEnabled(False)
		self.userval1.editingFinished.connect(self.textChange_1)
		self.userval2.editingFinished.connect(self.textChange_2)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('lavender'))
		self.setPalette(palette)
		self.setLayout(self.layout)
	
	def textChange_1(self):
		
		if int(self.userval1.text())>0:
# 			self.userval1.setError('Please Enter PRF Frequency')
# 		else:
			self.userval1.setEnabled(False)
			self.opacity_effect2.setEnabled(False)
			self.userval2.setEnabled(True)
	
	def textChange_2(self):
		if int(self.userval2.text())>=1:
			self.userval2.setEnabled(False)
			self.opacity_effect3.setEnabled(False)
			self.opacity_effect4.setEnabled(False)
# 		self.ReConAmbScheme.opacity_effect1.setEnabled(False)
# 		self.ReConAmbScheme.setEnabled(True)
	
	def WidgetEnable(self):
		self.setEnabled(True)
		self.opacity_effect1.setEnabled(False)
		
		
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
		self.opacity_effect1.setOpacity(0.3)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.3)
		
		self.ReConvThre.setGraphicsEffect(self.opacity_effect1)
		self.AMBCancel.setGraphicsEffect(self.opacity_effect2)
		
		self.setLayout(self.layout)
		
		
	def ReConvTextChanged(self):
		if int(self.userVal1.text())>0:
			self.userVal1.setEnabled(False)
			self.opacity_effect2.setEnabled(False)
			self.userVal2.setEnabled(True)
	
	def ABM_index(self,i):
		
		self.userVal2.setEnabled(False)

	def WidgetEnable(self):
		self.setEnabled(True)
		self.opacity_effect1.setEnabled(False)
		
class GlobalLayout(QtGui.QWidget):
	def __init__(self):
		super(GlobalLayout,self).__init__()
		
		phase_clock = QtGui.QVBoxLayout()

		self.ReConv_N_AMB = ReConv_N_AMBCancelScheme()
		self.ReConv_N_AMB.setFixedWidth(330)
		self.ReConv_N_AMB.setEnabled(False)
		
# 		self.timingParam = TimingParameters(self.ReConv_N_AMB)
		self.timingParam = TimingParameters()
		self.timingParam.setFixedSize(330,170)
		self.timingParam.setEnabled(False)
		
# 		self.clock_m = Clocking(self.timingParam)
		self.clock_m = Clocking()
		self.clock_m.setFixedSize(QtCore.QSize(330,200))
		self.clock_m.setEnabled(False)
		
# 		self.phase = PhaseTiming(self.clock_m)
		self.phase = PhaseTiming()
		self.phase.setFixedSize(QtCore.QSize(330,185))
		self.phase.setEnabled(False)
		
		phase_clock.addWidget(self.phase)
		phase_clock.addWidget(self.clock_m)
		phase_clock.addWidget(self.timingParam)
		phase_clock.addWidget(self.ReConv_N_AMB)
		
# 		self.addLayout(phase_clock)
# 		self.addWidget(Color('pink'))

		
		Global_layout = QtGui.QHBoxLayout()
		Global_layout.addLayout(phase_clock)
		Global_layout.addWidget(Color('pink'))
		self.setLayout(Global_layout)
		
		
# 		widget enabling
		self.phase.stagger_mode.clicked.connect(self.ClockingEnable)

		self.phase.high_prf_mode.clicked.connect(self.ClockingEnable)

		self.phase.max_amb_rej_mode.clicked.connect(self.ClockingEnable)

		self.phase.dis_post_amb_rej_mode.clicked.connect(self.ClockingEnable)
		
		
# 		self.internal.clicked.connect(self.mode_0)
		self.clock_m.internal.clicked.connect(self.TimingParametersEnable)

# 		self.external.clicked.connect(self.mode_1)
		self.clock_m.SelExternal.textChanged.connect(self.TimingParametersEnable)

# 		self.singleshot.clicked.connect(self.mode_2)
		self.clock_m.singleshot.clicked.connect(self.TimingParametersEnable)

# 		self.mixedclock.clicked.connect(self.mode_3)
		
		self.timingParam.userval2.editingFinished.connect(self.ReConv_N_AMBCancelSchemeEnable)
	
	def PhaseTimingEnable(self):
		self.phase.WidgetEnable()
		
	def ClockingEnable(self):
		self.clock_m.WidgetEnable()
		
	def TimingParametersEnable(self):
		self.timingParam.WidgetEnable()
		
	def ReConv_N_AMBCancelSchemeEnable(self):
		if int(self.timingParam.userval2.text())>=1:
			self.ReConv_N_AMB.WidgetEnable()	
		
		
class PerPhaseLayout(QtGui.QWidget):
	def __init__(self):
		super(PerPhaseLayout,self).__init__()
		PerPhase_layout = QtGui.QHBoxLayout()
		
		PerPhase_layout.addWidget(Color('pink'))
		self.setLayout(PerPhase_layout)

class TimingPowerLayout(QtGui.QWidget):
	def __init__(self):
		super(TimingPowerLayout,self).__init__()
		Timingpower_layout = QtGui.QHBoxLayout()
		
		Timingpower_layout.addWidget(Color('pink'))
		self.setLayout(Timingpower_layout)

class RegAndLog(QtGui.QWidget):
	def __init__(self):
		super(RegAndLog,self).__init__()
		layout_regNlog = QtGui.QVBoxLayout() 
# 		layout_regNlog.addWidget(QtGui.QLabel('LOG Window'))
		layout_regNlog.addWidget(Color('pink'))	# till changed let it be pink
		
		self.setLayout(layout_regNlog)
		self.setFixedWidth(250)
		
class TaskBar(QtGui.QWidget):
	def __init__(self):
		super(TaskBar,self).__init__()
		
		layout = QtGui.QHBoxLayout()
		self.TexasInst = QtGui.QLabel('TEXAS INSTRUMENTS')
		layout.addWidget(self.TexasInst)
		self.InnovCreate = QtGui.QLabel('INNOVATE. CREATE. MAKE THE DIFFERENCE')
		layout.addWidget(self.InnovCreate)
		self.AFEEVMStatus = QtGui.QLabel('AFE4460EVM is connected')
		layout.addWidget(self.AFEEVMStatus)
		
		self.TexasInst.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.TexasInst.setFixedSize(QtCore.QSize(500,50))
		self.TexasInst.setAlignment(QtCore.Qt.AlignCenter)
		
		self.InnovCreate.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.InnovCreate.setFixedSize(QtCore.QSize(500,50))
		self.InnovCreate.setAlignment(QtCore.Qt.AlignCenter)
		
		self.AFEEVMStatus.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.AFEEVMStatus.setFixedSize(QtCore.QSize(500,50))
		self.AFEEVMStatus.setAlignment(QtCore.Qt.AlignCenter)
		
		self.setLayout(layout)
		
		

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
# 		
		self.setWindowTitle('AFE 4460 GUI')
# 		
# 		widget = GlobalLayout()
# # 		widget.se(GlobalLayout)
# 		
# 		self.setCentralWidget(widget)
# 		self.setFixedSize(QtCore.QSize(1612,900))
# 		
		layout_main = QtGui.QHBoxLayout()	# the whole main window
# 		
		widget_regNlog =RegAndLog()	# the Register READ & WRITE widget & LOG window
# 		
		layout_main2 = QtGui.QVBoxLayout()		# the second half
		layout_main_config_tab = QtGui.QHBoxLayout()		# the configurations tab buttons
	
	
# 		# making different widgets for each layout
		self.widget_main_Global = GlobalLayout()
# 		
		widget_main_PerPhase = PerPhaseLayout()
# 		
		widget_main_TimingPower = TimingPowerLayout()
# 		

		self.layout_main3 = QtGui.QStackedLayout()		# making a stack for each tab
		self.layout_main3.addWidget(self.widget_main_Global)
		self.layout_main3.addWidget(widget_main_PerPhase)
		self.layout_main3.addWidget(widget_main_TimingPower)
# 		
		self.btn = QtGui.QPushButton('Global Configurations')
		self.btn.setFixedSize(QtCore.QSize(450,60))
		layout_main_config_tab.addWidget(self.btn)
		self.btn1 = QtGui.QPushButton('Per Phase Configurations')
		self.btn1.setFixedSize(QtCore.QSize(450,60))
# 		self.btn1.setEnabled(False)
		layout_main_config_tab.addWidget(self.btn1)
		self.btn2 = QtGui.QPushButton('Timing Diagram and Power')
		self.btn2.setFixedSize(QtCore.QSize(450,60))
# 		self.btn2.setEnabled(False)
		layout_main_config_tab.addWidget(self.btn2)
		
		
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.2)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.2)
		
		self.opacity_effect3 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect3.setOpacity(0.2)
		
		self.btn.setGraphicsEffect(self.opacity_effect1)
		self.btn1.setGraphicsEffect(self.opacity_effect2)
		self.btn2.setGraphicsEffect(self.opacity_effect3)
# 		# making all together
# 		
		widget_layout_main_config_tab = QtGui.QWidget()
		widget_layout_main_config_tab.setLayout(layout_main_config_tab)
		
		
# 		
		widget_layout_main3 = QtGui.QWidget()
		widget_layout_main3.setLayout(self.layout_main3)
		
		
		widget_layout_main2 =  QtGui.QWidget()
		widget_layout_main2.setLayout(layout_main2)

		
		layout_main2.addWidget(widget_layout_main_config_tab)
		layout_main2.addWidget(widget_layout_main3)
		
# 		widget_regNlog.setFixedWidth(200)
		

		layout_main.addWidget(widget_regNlog)
		layout_main.addWidget(widget_layout_main2)
		
		layout_main.setContentsMargins(0,0,0,0)
# 		
# 		# adding Buttons to tabs
		
		self.widget_main_Global.setEnabled(False)
		self.btn.clicked.connect(self.Tab_switch_Global)
		self.btn1.clicked.connect(self.Tab_switch_PerPhase)
		self.btn2.clicked.connect(self.Tab_switch_TimingPower)
		
		widget = QtGui.QWidget()
		widget.setLayout(layout_main)
		
		MainLayout = QtGui.QVBoxLayout()
		MainLayout.addWidget(widget)
		MainLayout.addWidget(TaskBar())
		Main_widget = QtGui.QWidget()
		Main_widget.setLayout(MainLayout)
		
		
		self.layout_main3.setCurrentIndex(0)
		
		self.setCentralWidget(Main_widget)
		

		self.setFixedSize(QtCore.QSize(1680,960))
# 		

	def Tab_switch_Global(self):
		self.widget_main_Global.setEnabled(True)
		self.widget_main_Global.PhaseTimingEnable()
		self.opacity_effect1.setEnabled(False)
		self.opacity_effect2.setEnabled(True)
		self.opacity_effect3.setEnabled(True)
		self.layout_main3.setCurrentIndex(0)
		
	def Tab_switch_PerPhase(self):
		self.opacity_effect1.setEnabled(True)
		self.opacity_effect2.setEnabled(False)
		self.opacity_effect3.setEnabled(True)
		self.layout_main3.setCurrentIndex(1)
# 		self.btn.setEnabled(False)
# 		self.btn1.setEnabled(True)
	def Tab_switch_TimingPower(self):
		self.opacity_effect1.setEnabled(True)
		self.opacity_effect2.setEnabled(True)
		self.opacity_effect3.setEnabled(False)
		self.layout_main3.setCurrentIndex(2)
# 		self.btn1.setEnabled(False)
# 		self.btn2.setEnabled(True)
		
		
		

		
# app = QtGui.QApplication(sys.argv)

window = MainWindow()

window.show()		

# app.exec_()
