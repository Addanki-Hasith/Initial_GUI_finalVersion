from pyqtgraph.Qt import QtCore
from pyqtgraph.Qt import QtGui
from pyqtgraph.Qt import QtSvg
import sys

# self.userVal1.setStyleSheet("QLineEdit"
# 								"{"
# 								"border :1px solid black;"
# 								"}"
# 								"QLineEdit::focus"
# 								"{"
# 								"border-color : red green blue yellow"
# 								"}")
class Color(QtGui.QWidget):
	def __init__(self,color):
		super(Color,self).__init__()
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(color))

		self.setPalette(palette)

class LogWindow(QtGui.QWidget):
	def __init__(self):
		super(LogWindow,self).__init__()
		self.logWindow = QtGui.QTextEdit()
		self.logWindow.setStyleSheet("background:#aaaaaa; color: white")
# 		logWindow.setStyleSheet('color:white')
		self.title = QtGui.QLabel('LOG WINDOW')
# 		margin-left: 10px; border: 1px solid black; border-radius: 10px;
		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		self.title.setFixedHeight(25)
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		
		layout = QtGui.QVBoxLayout()
		
		layout.addWidget(self.title)
		layout.addWidget(self.logWindow)
		
		self.logWindow.setPlainText('This is the log window')
		self.logWindow.setReadOnly(True)
		self.setLayout(layout)
		self.setFixedHeight(550)
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
		self.setPalette(palette)
		
	def settingLogText(self,s):
# 		self.logWindow.replaceall(s)
		self.logWindow.clear()
		self.logWindow.insertPlainText(s)

logWindow_wid = LogWindow()

class RegWindow(QtGui.QWidget):
	def __init__(self):
		super(RegWindow,self).__init__()
		layout_m = QtGui.QVBoxLayout()		
		self.address_wid = QtGui.QLineEdit()
		self.address_wid.setPlaceholderText('Address')
		self.address_wid.setStyleSheet("QLineEdit"
								"{"
								"margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: black;"
								"}"
								"QLineEdit::focus"
								"{"
								"border-color : red;"
								"background-color : #edf7f8;"
								"}")
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.address_wid.setSizePolicy(sizePolicy)
		
		self.address_wid.setFixedHeight(40)
		self.address_wid.setAlignment(QtCore.Qt.AlignCenter)
		
		self.dec_wid = QtGui.QRadioButton('Dec')
		self.dec_wid.setFixedHeight(20)
		self.dec_wid.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 20px;"
										"height: 20px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:12px;"
										"height: 12px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:9px;"
										"}")
		self.hex_wid = QtGui.QRadioButton('Hex')
		self.hex_wid.setFixedHeight(20)
		self.hex_wid.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 20px;"
										"height: 20px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:12px;"
										"height: 12px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:9px;"
										"}")
		self.read_wid = QtGui.QRadioButton('Read')
		self.write_wid = QtGui.QRadioButton('Write')
		self.read_wid.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 20px;"
										"height: 20px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:12px;"
										"height: 12px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:9px;"
										"}")
		self.write_wid.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 20px;"
										"height: 20px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:12px;"
										"height: 12px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:9px;"
										"}")
		self.data_wid = QtGui.QLineEdit()
		self.data_wid.setPlaceholderText('DATA')
		self.data_wid.setStyleSheet("QLineEdit"
								"{"
								"margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: black;"
								"}"
								"QLineEdit::focus"
								"{"
								"border-color : red;"
								"background-color : #edf7f8;"
								"}")
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.data_wid.setSizePolicy(sizePolicy)
# 		
		self.data_wid.setFixedHeight(40)

		self.data_wid.setAlignment(QtCore.Qt.AlignCenter)
		
		self.reset_wid = QtGui.QLabel('RESET')
		self.reset_wid.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: black;")
		self.reset_wid.setFixedHeight(40)
		self.reset_wid.setAlignment(QtCore.Qt.AlignCenter)

		layout_4 = QtGui.QVBoxLayout()
		layout_5 = QtGui.QVBoxLayout()
		
		layout_6 = QtGui.QHBoxLayout()
		layout_7 = QtGui.QHBoxLayout()
		
		layout_6.addWidget(self.address_wid)
		layout_5.addWidget(self.dec_wid)
		layout_5.addWidget(self.hex_wid)
		layout_6.addLayout(layout_5)
		
		layout_7.addWidget(self.read_wid)
		layout_7.addWidget(self.write_wid)
		
		self.read_write = QtGui.QWidget()
		self.read_write.setLayout(layout_7)
		
		self.reg_label = QtGui.QLabel('Register READ/WRITE')
		self.reg_label.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		self.reg_label.setAlignment(QtCore.Qt.AlignCenter)
		
		layout_4.addWidget(self.reg_label)
		layout_4.addLayout(layout_6)
		layout_4.addWidget(self.read_write)
		
		layout_m.addLayout(layout_4)
		
		layout_8 = QtGui.QHBoxLayout()
		layout_8.addWidget(self.data_wid)
		
		self.page = QtGui.QComboBox()
		self.page.addItems(['Page-?','Page-0','Page-1'])
		self.page.setFixedWidth(75)
		layout_8.addWidget(self.page)
		
		layout_m.addLayout(layout_8)
		layout_m.addWidget(self.reset_wid)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
		self.setPalette(palette)
		self.setLayout(layout_m)
		self.setFixedHeight(260)
		
		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect.setOpacity(0.5)
		self.address_wid.setGraphicsEffect(self.opacity_effect)
		
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		self.data_wid.setGraphicsEffect(self.opacity_effect1)
		
		self.read_write.setEnabled(False)
		self.page.setEnabled(False)
		self.address_wid.setEnabled(False)
		self.data_wid.setEnabled(False)
# 		self.data_wid.setReadOnly(True)
		
		self.hex_wid.clicked.connect(self.hex_selected)
		self.dec_wid.clicked.connect(self.dec_selected)
		
		self.read_wid.clicked.connect(self.read_selected)
		self.write_wid.clicked.connect(self.write_selected)
		
		self.page.currentIndexChanged.connect(self.page_selected)
		
		self.write_text = 'Enter DATA'
	def hex_selected(self):
		self.address_wid.setEnabled(True)
		self.read_write.setEnabled(True)
		self.opacity_effect.setEnabled(False)
		logWindow_wid.settingLogText('Enter hex values between 00 and ff')
	
	def dec_selected(self):
		self.address_wid.setEnabled(True)
		self.read_write.setEnabled(True)
		self.opacity_effect.setEnabled(False)
		logWindow_wid.settingLogText('Enter hex values between 0 and 255')
	
	def read_selected(self):
		self.data_wid.setPlaceholderText('Select Page')
		self.page.setEnabled(True)
		self.page.setCurrentIndex(0)
		self.opacity_effect1.setEnabled(False)
		self.data_wid.setEnabled(False)
		logWindow_wid.settingLogText('Read Operation is implemented')
# 		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect2.setOpacity(0.6)
# 		self.data_wid.setGraphicsEffect(self.opacity_effect2)
		
		
	def write_selected(self):
		self.data_wid.setPlaceholderText(self.write_text)
		self.data_wid.setReadOnly(False)
		self.data_wid.setEnabled(True)
		self.page.setEnabled(True)
		self.opacity_effect1.setEnabled(False)
		logWindow_wid.settingLogText('Write Operation is implemented')
		
	def page_selected(self,id):
		if id == 0:
			logWindow_wid.settingLogText('select correct Page')
		if self.read_wid.isChecked() and self.page.currentIndex()!=0:
			logWindow_wid.settingLogText('Read Operation is implemented')
			self.data_wid.setPlaceholderText('Value in REG')
		
		elif self.write_wid.isChecked() and self.page.currentIndex()!=0 :
			logWindow_wid.settingLogText('Write Operation is implemented')
			self.data_wid.setPlaceholderText(self.write_text)
		
		
		if id == 1 and self.read_wid.isChecked():
			if self.dec_wid.isChecked():
# 				logWindow_wid.settingLogText(self.address_wid.text())
				try:
					a2 = self.address_wid.text()
					logWindow_wid.settingLogText(7*a2)
				except:
					logWindow_wid.settingLogText('Please enter only integer type values')
			elif self.hex_wid.isChecked():
				pass
		
		elif id == 1 and self.write_wid.isChecked():
			if self.dec_wid.isChecked():
				pass
			elif self.hex_wid.isChecked():
				pass
		
		elif id == 2 and self.read_wid.isChecked():
			if self.dec_wid.isChecked():
				pass
			elif self.hex_wid.isChecked():
				pass
		
		elif id == 2 and self.write_wid.isChecked():
			if self.dec_wid.isChecked():
				pass
			elif self.hex_wid.isChecked():
				pass
		
class RegAndLog(QtGui.QWidget):
	def __init__(self):
		super(RegAndLog,self).__init__()
		layout_regNlog = QtGui.QVBoxLayout() 
# 		layout_regNlog.addWidget(QtGui.QLabel('LOG Window'))
		
# 		self.reg_label = QtGui.QLabel('REGISTER READ/WRITE')
	# 		margin-left: 10px; border: 1px solid black; border-radius: 10px;
# 		self.reg_label.setStyleSheet(" background: white; font-weight:bold;	color: rgba(0,124,140)")

# 		self.reg_label.setAlignment(QtCore.Qt.AlignCenter)
# 		layout_regNlog.addWidget(self.reg_label)
		layout_regNlog.addWidget(RegWindow())
		layout_regNlog.addWidget(logWindow_wid)		
		
		self.setLayout(layout_regNlog)
		self.setFixedWidth(250)

class GlobalLayout(QtGui.QWidget):
	def __init__(self):
		super(GlobalLayout,self).__init__()
		
		phase_clock = QtGui.QVBoxLayout()

		self.ReConv_N_AMB =ReConv_N_AMBCancelScheme()
		self.ReConv_N_AMB.setFixedWidth(330)
		self.ReConv_N_AMB.setEnabled(False)
		
		self.timingParam = TimingParameters(self.ReConv_N_AMB)
		self.timingParam.setFixedSize(330,170)
		self.timingParam.setEnabled(False)
		
		self.clock_m = Clocking(self.timingParam)
		self.clock_m.setFixedSize(QtCore.QSize(330,200))
		self.clock_m.setEnabled(False)
		
		self.phase = PhaseTiming(self.clock_m)
		self.phase.setFixedSize(QtCore.QSize(330,185))
		self.phase.setEnabled(False)
		
		phase_clock.addWidget(self.phase)
		phase_clock.addWidget(self.clock_m)
		phase_clock.addWidget(self.timingParam)
		phase_clock.addWidget(self.ReConv_N_AMB)
		
# 		self.addLayout(phase_clock)
# 		self.addWidget(Color('pink'))
		
# 		file = "AFE4460_SVG_GlobalCircuit.svg"
# 		self.svg_wid = QtCore.QSvgWidget(file)
		
		Global_layout = QtGui.QHBoxLayout()
		phase_clock_wid = QtGui.QWidget()
		phase_clock_wid.setLayout(phase_clock)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('white'))

		self.setPalette(palette)
		
		Global_layout.addWidget(phase_clock_wid)
		
		
		svgWidget = QtSvg.QSvgWidget(APP_DIR+"/AFE4460_Global.svg")
		svgWidget.setGeometry(5,0,1000,700)

# 		self.svg_file =QtGui.QPixmap(APP_DIR+"/AFE4460_Global.svg")
# 		self.temp_label = QtGui.QLabel()
# 		self.temp_label.setPixmap(svgWidget)
		Global_layout.addWidget(svgWidget)
# 		Global_layout.addWidget(Color('pink'))
# 		Global_layout.addLayout(temp_lay)
		
		self.setLayout(Global_layout)
		
		
class PerPhaseLayout(QtGui.QWidget):
	def __init__(self):
		super(PerPhaseLayout,self).__init__()
		PerPhase_layout = QtGui.QGridLayout()
		control_wid = control_layout()
		Individual_config_wid = Individual_config_layout()
		Summary_config_wid = Summary_config_layout()
		self.config_wid = QtGui.QStackedWidget()
		
		PerPhase_layout.addWidget(control_wid,0,0)
		PerPhase_layout.addWidget(self.config_wid,1,0)
		
		self.config_wid.addWidget(Individual_config_wid)
		self.config_wid.addWidget(Summary_config_wid)
		
		self.config_wid.setCurrentIndex(0)
		
		control_wid.setFixedHeight(100)
		
		control_wid.individual.clicked.connect(self.View_change_individual)
		control_wid.summary.clicked.connect(self.View_change_summary)
		
# 		PerPhase_layout.addWidget(Color('pink'))
		self.setLayout(PerPhase_layout)
		
	def View_change_individual(self):
		self.config_wid.setCurrentIndex(0)
	def View_change_summary(self):
		self.config_wid.setCurrentIndex(1)

# class PerPhaseLayout(QtGui.QWidget):
# 	def __init__(self):
# 		super(PerPhaseLayout,self).__init__()
# 		
# 		control_wid = control_layout()
# 		Individual_config_wid = Individual_config_layout()
# 		Summary_config_wid = Summary_config_layout()
# 		self.config_wid = QtGui.QStackedWidget()
# 		
# 		self.config_wid.addWidget(Individual_config_wid)
# 		self.config_wid.addWidget(Summary_config_wid)
# 		
# 		self.config_wid.setCurrentIndex(0)
# 		control_wid.individual.clicked.connect(self.View_change_individual)
# 		control_wid.summary.clicked.connect(self.View_change_summary)
# 		
# 		self.PerPhase_lay = QtGui.QVBoxLayout()
# 		self.PerPhase_lay.addWidget(control_wid,1)
# 		self.PerPhase_lay.addWidget(self.config_wid,15)
# 		
# 		
# 		self.setLayout(self.PerPhase_lay)
# 	def View_change_individual(self):
# 		self.config_wid.setCurrentIndex(0)
# 	def View_change_summary(self):
# 		self.config_wid.setCurrentIndex(1)
# 		
# class TimingPowerLayout(QtGui.QWidget):
# 	def __init__(self):
# 		super(TimingPowerLayout,self).__init__()
# 		Timingpower_layout = QtGui.QHBoxLayout()
# 		
# # 		Timingpower_layout.addWidget(Timing_para())
# 		Timingpower_layout.addWidget(Color('pink'))
# 		self.setLayout(Timingpower_layout)


		
class TaskBar(QtGui.QWidget):
	def __init__(self):
		super(TaskBar,self).__init__()
		
# 		layout = QtGui.QHBoxLayout()
		layout = QtGui.QGridLayout()
		self.TexasInst = QtGui.QLabel('TEXAS INSTRUMENTS')
		layout.addWidget(self.TexasInst,0,0)
		self.InnovCreate = QtGui.QLabel('INNOVATE. CREATE. MAKE THE DIFFERENCE')
		layout.addWidget(self.InnovCreate,0,1)
		self.AFEEVMStatus = QtGui.QLabel('AFE4460EVM is connected')
		layout.addWidget(self.AFEEVMStatus,0,2)
		
		self.TexasInst.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.TexasInst.setFixedHeight(50)
# 		self.TexasInst.setFixedSize(QtCore.QSize(500,50))
		self.TexasInst.setAlignment(QtCore.Qt.AlignCenter)
		
		self.InnovCreate.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
# 		self.InnovCreate.setFixedSize(QtCore.QSize(500,50))
		self.InnovCreate.setAlignment(QtCore.Qt.AlignCenter)
		
		self.AFEEVMStatus.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
# 		self.AFEEVMStatus.setFixedSize(QtCore.QSize(500,50))
		self.AFEEVMStatus.setAlignment(QtCore.Qt.AlignCenter)
		
		self.setLayout(layout)
		
		

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
	
		self.setWindowTitle('AFE4460 GUI')

# 		
		layout_main = QtGui.QHBoxLayout()	# the whole main window
# 		
		widget_regNlog =RegAndLog()	# the Register READ & WRITE widget & LOG window
# 		
		layout_main2 = QtGui.QVBoxLayout()		# the second half
# 		layout_main_config_tab = QtGui.QHBoxLayout()		# the configurations tab buttons
		layout_main_config_tab = QtGui.QGridLayout()
	
# 		# making different widgets for each layout
		self.widget_main_Global = GlobalLayout()
# 		
		widget_main_PerPhase = PerPhaseLayout()
# 		
		widget_main_TimingPower  = Color('pink')
# 		

		self.layout_main3 = QtGui.QStackedLayout()		# making a stack for each tab
		self.layout_main3.addWidget(self.widget_main_Global)
		self.layout_main3.addWidget(widget_main_PerPhase)
		self.layout_main3.addWidget(widget_main_TimingPower)
# 		
		self.btn = QtGui.QPushButton('Global Configurations')

		self.btn.setFixedHeight(60)
		layout_main_config_tab.addWidget(self.btn,0,0)
		self.btn1 = QtGui.QPushButton('Per Phase Configurations')
		self.btn1.setFixedHeight(60)

# 		self.btn1.setEnabled(False)
		layout_main_config_tab.addWidget(self.btn1,0,1)
		self.btn2 = QtGui.QPushButton('Timing Diagram and Power')
		self.btn2.setFixedHeight(60)

# 		self.btn2.setEnabled(False)
		layout_main_config_tab.addWidget(self.btn2,0,2)
		
		
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

		
# # 		layout_main2.addWidget(widget_layout_main_config_tab)
# # 		layout_main2.addWidget(widget_layout_main3)
		
		tab_widget_lay = QtGui.QVBoxLayout()
		tab_wid = QtGui.QTabWidget()
		tab_wid.addTab(self.widget_main_Global,"GLOBAL CONFIGURATION")
		tab_wid.addTab(widget_main_PerPhase,"PER PHASE CONFIGURATION")
		tab_wid.addTab(widget_main_TimingPower,"TIMING DIAGRAM AND POWER")
		
		tab_wid.setStyleSheet("QTabBar::tab"
							"{" 
								"width: 350px;" 
								"height: 50px;"
							"}"
							"QTabBar::tab:selected" 
							"{"
								"background-color : #ee0000 ;"
								"color: 'white';"
								"font-weight : bold;"
							"}"
							"QTabBar::tab:!selected" 
							"{"
								"background-color : #efb9b9 ;"
								"color: 'white';"
							"}"
							)
		
		tab_widget_lay.addWidget(tab_wid)
		
# 		tab_wid.setTabEnabled(2,False)
		layout_main2.addLayout(tab_widget_lay)
# 		widget_regNlog.setFixedWidth(200)
		

		layout_main.addWidget(widget_regNlog)
		layout_main.addWidget(widget_layout_main2)
		
		layout_main.setContentsMargins(0,0,0,0)
# 		
# 		# adding Buttons to tabs
		
# 		self.widget_main_Global.setEnabled(False)
		self.widget_main_Global.phase.PhaseEnable()
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
		
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('white'))

		self.setPalette(palette)
		self.btn.setStyleSheet("background-color : #ee0000 ; color:'white'")	
		self.btn1.setStyleSheet("background-color : #ee0000; color:'white'")
		self.btn2.setStyleSheet("background-color : #ee0000; color:'white'")
		
		self.layout_main3.setCurrentIndex(0)
		
		self.setCentralWidget(Main_widget)
		
# 		self.setFixedSize(QtCore.QSize(1680,960))
# 		self.resize(1680,960)
# 		

	def Tab_switch_Global(self):
		self.widget_main_Global.setEnabled(True)
		self.widget_main_Global.phase.PhaseEnable()
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
