
# class ColorQLineEdit(QtGui.QLineEdit):
# 
# 	def focusInEvent(self, event):
# 		print("in")
# 		self.setStyleSheet("background-color: yellow; color: red;")
# 		super().focusInEvent(event)
# 
# 	def focusOutEvent(self, event):
# 		print("out")
# 		self.setStyleSheet("background-color: white; color: black;")
# 		super().focusOutEvent(event)

class PhaseTiming(QtGui.QWidget):
	def __init__(self,clock_m):
		super(PhaseTiming,self).__init__()
		
		self.clk_m = clock_m
		
		self.layout = QtGui.QVBoxLayout()
		self.title = QtGui.QLabel('PHASE TIMING SCHEME')
# 		margin-left: 10px; border: 1px solid black; border-radius: 10px;
		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		
		self.title.setFixedSize(QtCore.QSize(225,25))
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		
		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect.setOpacity(0.5)
		self.title.setGraphicsEffect(self.opacity_effect)
		
		self.stagger_mode = QtGui.QRadioButton("Stagger Mode")
		self.high_prf_mode = QtGui.QRadioButton("High PRF Mode")
		self.max_amb_rej_mode = QtGui.QRadioButton("Max AMB Rej Mode")
		self.dis_post_amb_rej_mode = QtGui.QRadioButton("Dis-POST AMB Rej ")
		
		self.stagger_mode.setStyleSheet("QRadioButton::indicator" 
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
		self.high_prf_mode.setStyleSheet("QRadioButton::indicator" 
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
		self.max_amb_rej_mode.setStyleSheet("QRadioButton::indicator" 
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
		self.dis_post_amb_rej_mode.setStyleSheet("QRadioButton::indicator" 
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
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
		self.setPalette(palette)
		
		self.stagger_mode.clicked.connect(self.mode_0)

		self.high_prf_mode.clicked.connect(self.mode_1)

		self.max_amb_rej_mode.clicked.connect(self.mode_2)

		self.dis_post_amb_rej_mode.clicked.connect(self.mode_3)
		
	def mode_0(self):
# 		self.disable_select()
		AFE_config_phaseTimingScheme(STAGGER_mode)
		self.clk_m.setEnabled(True)
		self.clk_m.opacity_effect1.setEnabled(False)

	def mode_1(self):
# 		self.disable_select()
		AFE_config_phaseTimingScheme(HIGH_PRF_MODE_mode)
		self.clk_m.setEnabled(True)
		self.clk_m.opacity_effect1.setEnabled(False)
		
	def mode_2(self):
# 		self.disable_select()
		AFE_config_phaseTimingScheme(MAX_AMB_REJ_mode)
		self.clk_m.setEnabled(True)
		self.clk_m.opacity_effect1.setEnabled(False)
		
	def mode_3(self):
# 		self.disable_select()		
		AFE_config_phaseTimingScheme(DIS_POST_AMB_MAX_AMB_REJ_mode)
		self.clk_m.setEnabled(True)
		self.clk_m.opacity_effect1.setEnabled(False)
# 	def disable_select(self):
# 		
# 		self.clk_m.setEnabled(True)
# 		
# # 		self.clk_m.opacity_effect1.setEnabled(False)
# # 		self.stagger_mode.setDisabled(True)
# # 		self.high_prf_mode.setDisabled(True)
# # 		self.max_amb_rej_mode.setDisabled(True)
# # 		self.dis_post_amb_rej_mode.setDisabled(True)
	
	def PhaseEnable(self):
		self.setEnabled(True)
		self.opacity_effect.setEnabled(False)
		
		
class Clocking(QtGui.QWidget):
	def __init__(self,timePar):
		super(Clocking,self).__init__()
		
		self.timingParameter = timePar
		
		self.title = QtGui.QLabel('CLOCKING MODE')
# 		margin-left: 10px; border: 1px solid black; border-radius: 10px;
		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		self.title.setFixedSize(QtCore.QSize(225,25))
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		
		self.internal = QtGui.QRadioButton('CLK_MODE_INT')
		self.external = QtGui.QRadioButton('CLC_MODE_EXT')
		self.singleshot = QtGui.QRadioButton('CLC_MODE_SS')
		self.mixedclock = QtGui.QRadioButton('CLC_MODE_MIX')
		
		self.internal.setStyleSheet("QRadioButton::indicator" 
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
		self.external.setStyleSheet("QRadioButton::indicator" 
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
		self.singleshot.setStyleSheet("QRadioButton::indicator" 
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
		self.mixedclock.setStyleSheet("QRadioButton::indicator" 
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
																																	
		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect.setOpacity(0.3)
		
		self.internal.setToolTip('Selecting Internal Clock')
		self.external.setToolTip('Selecting External Clock')
		self.singleshot.setToolTip('Selecting Single Shot Mode Clock')
		self.mixedclock.setToolTip('Selecting Mixed Clock')
		
		self.HBox = QtGui.QHBoxLayout()
		self.ExternalClk = QtGui.QLabel('External Clk Frequency')
# 		self.ExternalClk.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: rgba(0,124,140);")
		self.ExternalClk.setStyleSheet("background: white; color: rgba(0,124,140);")
# 		self.extCLk_lay = QtGui.QStackedLayout()
		self.extCLk_wid = QtGui.QStackedWidget()
# 		self.extCLk_wid.setLayout(self.extCLk_lay)
		
		self.SelExternal = QtGui.QComboBox()
		self.SelExternal_Mix = QtGui.QComboBox()
		
		self.extCLk_wid.addWidget(self.SelExternal)
		self.extCLk_wid.addWidget(self.SelExternal_Mix)
		self.SelExternal.addItems(['256 KHz', '512 KHz', '1024 KHz'])
		self.SelExternal_Mix.addItems(['32.768 KHz'])
		
		self.ExternalClk.setGraphicsEffect(self.opacity_effect)
		self.SelExternal.setEnabled(False)
		
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		
		self.title.setGraphicsEffect(self.opacity_effect1)
		
		self.HBox.addWidget(self.ExternalClk)
		self.HBox.addWidget(self.extCLk_wid)

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
		self.external.clicked.connect(self.timingParEnable)

		self.singleshot.clicked.connect(self.mode_2)
		self.singleshot.clicked.connect(self.timingParEnable)

		self.mixedclock.clicked.connect(self.mode_3)
		self.mixedclock.clicked.connect(self.timingParEnable)
		
		self.setLayout(self.layout)		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
		self.setPalette(palette)
		
		self.SelExternal.currentIndexChanged.connect(self.external_clock_index)
# 		self.SelExternal_Mix.currentIndexChanged.connect(self.mixed_clock_index)
		self.setLayout(self.layout)

	def mode_0(self):
		self.opacity_effect.setEnabled(True)
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(False)
# 		self.disable_select()
		AFE_config_clockingMode(CLK_MODE_INT)
	def mode_1(self):
		self.extCLk_wid.setCurrentIndex(0)
		self.opacity_effect.setEnabled(False)
		self.SelExternal.setEnabled(True)
		self.SelExternal_Mix.setEnabled(False)
		self.SelExternal.currentIndexChanged.connect(self.timingParEnable)
# 		self.disable_select()
		AFE_config_clockingMode(CLK_MODE_EXT)
	def mode_2(self):
		self.opacity_effect.setEnabled(True)
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(False)
		AFE_config_clockingMode(CLK_MODE_SS)
# 		self.disable_select()
	
	def mode_3(self):
		self.extCLk_wid.setCurrentIndex(1)
		self.opacity_effect.setEnabled(False)
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(True)		
		self.timingParEnable()
# 		self.disable_select()		
		AFE_config_clockingMode(CLK_MODE_MIX)
	def disable_select(self):
		
		self.internal.setDisabled(True)
		self.external.setDisabled(True)
		self.singleshot.setDisabled(True)
		self.mixedclock.setDisabled(True)
		
	def external_clock_index(self,i):
		if i == 0:
			AFE_config_extClkDecimation(external_clk_NoDecimation)
			logWindow_wid.settingLogText('External Clock of 256 KHz is selected')
		elif i == 1:
			AFE_config_extClkDecimation(external_clk_Decimation_2)
			logWindow_wid.settingLogText('External Clock of 512 KHz is selected')
		elif i == 2:
			AFE_config_extClkDecimation(external_clk_Decimation_4) 
			logWindow_wid.settingLogText('External Clock of 1024 KHz is selected')
		
		self.SelExternal.setEnabled(True)

# 	def mixed_clock_index(self,i):
# 		self.SelExternal.setEnabled(True)
	
	def timingParEnable(self):
		self.timingParameter.setEnabled(True)
		self.timingParameter.opacity_effect2.setEnabled(False)
	
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
		self.parName2 = QtGui.QLabel('STEP COUNT')
		self.parName2.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		self.parName1.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.parName1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: blue;")
# 		self.parName2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: blue;")
		
		self.parName1.setAlignment(QtCore.Qt.AlignCenter)
		self.parName2.setAlignment(QtCore.Qt.AlignCenter)
		self.userval1 = QtGui.QLineEdit()
		self.userval1.setPlaceholderText('Enter PRF Frequency')
		self.userval1.setToolTip('Enter values between 4Hz and 256 KHz')
		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
		
		self.userval2 = QtGui.QLineEdit()
		self.userval2.setPlaceholderText('Enter Step Count')
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.userval2.setSizePolicy(sizePolicy)
		self.userval1.setSizePolicy(sizePolicy)
		self.userval2.setToolTip('Enter values between 1 and 128')
		self.userval2.setAlignment(QtCore.Qt.AlignCenter)
		
		self.hbox1.addWidget(self.parName1)
		
		self.hbox1.addWidget(self.userval1)
		
		self.hbox2.addWidget(self.parName2)
		self.hbox2.addWidget(self.userval2)

		self.layout.addLayout(self.hbox2)
		self.layout.addLayout(self.hbox1)
		
		
		self.label1.setStyleSheet("margin-left: 10px; border: 1px solid rgba(0,124,140); border-radius: 5px; background: rgba(237,247,248); color: black;")
		self.label2.setStyleSheet("margin-left: 10px; border: 1px solid rgba(0,124,140); border-radius: 5px; background: rgba(237,247,248); color: black;")
		
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
		
		self.userval1.setEnabled(False)
		self.userval2.setEnabled(True)
		self.userval1.editingFinished.connect(self.textChange_1)
		self.userval1.textChanged.connect(self.prf_changing)
		self.userval2.editingFinished.connect(self.textChange_2)
		self.userval2.textChanged.connect(self.stepcount_changing)
		
		self.onlyDouble = QtGui.QDoubleValidator()
		self.userval1.setValidator(self.onlyDouble)
		self.onlyDouble.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble.setRange(4,256000.000,decimals = 3)
		
		self.userval1.setStyleSheet("QLineEdit"
								"{"
								"border :1px solid black;"
								"}"
								"QLineEdit::focus"
								"{"
								"border-color : red ;"
								"background-color : #edf7f8;"
								"}")
		self.userval2.setStyleSheet("QLineEdit"
								"{"
								"border :1px solid black;"
								"}"
								"QLineEdit::focus"
								"{"
								"border-color : red;"
								"background-color : #edf7f8;"
								"}")		
# 		
		self.onlyInt = QtGui.QIntValidator()
		self.userval2.setValidator(self.onlyInt)
		self.onlyInt.setRange(1,128)
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
		self.setPalette(palette)
		self.setLayout(self.layout)
		
		self.prf_assigned = False
		self.stepcount_assigned = False
	
	def prf_changing(self):
		self.opacity_effect3.setEnabled(True)
		self.opacity_effect4.setEnabled(True)	
		self.prf_assigned = False
		
	def stepcount_changing(self):
		self.opacity_effect3.setEnabled(True)
		self.opacity_effect4.setEnabled(True)	
		self.stepcount_assigned = False
	
	def textChange_2(self):
		self.userval2.clearFocus()
		self.stepcount_assigned = True
		if self.prf_assigned:
			self.opacity_effect3.setEnabled(False)
			self.opacity_effect4.setEnabled(False)
		self.opacity_effect1.setEnabled(False)
		self.userval1.setEnabled(True)
		
		val = int(str(self.userval2.text()))
		AFE_config_stepcount(val)
		logWindow_wid.settingLogText('Step Count is assigned with a value of ' + str(val))
		
	def textChange_1(self):
		self.prf_assigned = True
		
		self.opacity_effect3.setEnabled(False)
		self.opacity_effect4.setEnabled(False)	
		self.ReConAmbScheme.opacity_effect1.setEnabled(False)
		self.ReConAmbScheme.setEnabled(True)
		
		val2 = float(str(self.userval1.text()))
		
		finalVal = AFE_config_prpct(val2)
		
		self.label1.setText('PRPCT = ' + str(int(finalVal[0])) )
		self.label2.setText('Exact PRF is ' + str(finalVal[1]) + ' Hz')
		logWindow_wid.settingLogText('PRF assignment')

class ReConv_N_AMBCancelScheme(QtGui.QWidget):
	def __init__(self):
		super(ReConv_N_AMBCancelScheme,self).__init__()
		
		self.layout = QtGui.QVBoxLayout()
		
		self.Hbox1 = QtGui.QHBoxLayout()
		self.Hbox2 = QtGui.QHBoxLayout()
		
		self.ReConvThre = QtGui.QLabel('ReConvergence \nThreshold (V)')
		self.AMBCancel = QtGui.QLabel('AMB Cancellation \nScheme')
		
		self.ReConvThre.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		self.AMBCancel.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.ReConvThre.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: blue;")
# 		self.AMBCancel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: blue;")
		self.ReConvThre.setAlignment(QtCore.Qt.AlignCenter)
		self.AMBCancel.setAlignment(QtCore.Qt.AlignCenter)
		
		self.userVal1 = QtGui.QLineEdit()
		self.userVal2 = QtGui.QComboBox()
		self.userVal1.setAlignment(QtCore.Qt.AlignCenter)
		self.userVal2.addItems(['None', 'ANA-AACM','MCU Ctrl'])
		
		self.userVal1.setPlaceholderText('Enter in Volts')
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.userVal1.setSizePolicy(sizePolicy)

		self.userVal2.currentIndexChanged.connect(self.ABM_index)
		
# 		self.userVal1.setDisabled(True)
		self.userVal2.setEnabled(False)
		self.Hbox1.addWidget(self.ReConvThre)
		self.Hbox1.addWidget(self.userVal1)
		
		self.Hbox2.addWidget(self.AMBCancel)
		self.Hbox2.addWidget(self.userVal2)
		
		self.layout.addLayout(self.Hbox1)
		self.layout.addLayout(self.Hbox2)
# 		self.layout.addWidget(ColorQLineEdit('one'))
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
		self.setPalette(palette)
		
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.3)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.3)
		
		self.ReConvThre.setGraphicsEffect(self.opacity_effect1)
		self.AMBCancel.setGraphicsEffect(self.opacity_effect2)
		
		self.setLayout(self.layout)
		self.userVal1.setStyleSheet("QLineEdit"
								"{"
								"border :1px solid black;"
								"}"
								"QLineEdit::focus"
								"{"
# 								"border :2px solid"
								"border-color : red ;"
								"background-color : #edf7f8;"
								"}")
		
		self.onlyDouble = QtGui.QDoubleValidator()
		self.userVal1.setValidator(self.onlyDouble)
		self.onlyDouble.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble.setRange(0.0,1.200,decimals = 3)
		self.userVal1.setToolTip('Enter values between 0.0 V and 1.2 V')
		
		self.userVal1.editingFinished.connect(self.ReConvTextChanged)
		
		
	def ReConvTextChanged(self):
		self.userVal1.clearFocus()
		self.userVal1.setEnabled(True)
		self.opacity_effect2.setEnabled(False)
		self.userVal2.setEnabled(True)
		
		val = float(str(self.userVal1.text()))
		regVal = AFE_config_ReConvThre(val)
		
		logWindow_wid.settingLogText('Re-Convergence Threshold Voltage is set with REG_RECONV_THR_LED_DC register value at ' + str(int(regVal)))
		
	def ABM_index(self,i):
		
		self.userVal2.setEnabled(True)
		
		
# class Receiver_transmitter(QtGui.QWidget):
# 	def __init__(self):
# 		super(Receiver_transmitter,self).__init__()
# 		
# 		self.MaxTIAs = QtGui.QLabel('Maximum No. of \n TIAs')
# 		self.MaxTIAs.setAlignment(QtCore.Qt.AlignCenter)
# 		self.MaxTIAs.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		
# 		self.MaxTIAsCombo = QtGui.QComboBox()
# 		self.MaxTIAsCombo.addItems(['1','2','3','4'])
# 		
# 		self.MaxTIAsForm = QtGui.QFormLayout()
# 		self.MaxTIAsForm.addRow(self.MaxTIAs,self.MaxTIAsCombo)
# 		
# 		self.TIA1 = QtGui.QRadioButton('TIA1')
# 		self.TIA2 = QtGui.QRadioButton('TIA2')
# 		self.TIA3 = QtGui.QRadioButton('TIA3')
# 		self.TIA4 = QtGui.QRadioButton('TIA4')
# 		self.TIA1.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.TIA2.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.TIA3.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.TIA4.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")																								
# 		self.TIAn = QtGui.QHBoxLayout()
# 		self.TIAn.addWidget(self.TIA1)
# 		self.TIAn.addWidget(self.TIA2)
# 		self.TIAn.addWidget(self.TIA3)
# 		self.TIAn.addWidget(self.TIA4)	
# 		
# 		self.Common_wid = QtGui.QRadioButton('Common')
# 		self.Common_wid.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.TIAnForm = QtGui.QFormLayout()
# 		self.TIAnForm.addRow(self.Common_wid,self.TIAn)
# 		
# 		self.LEDOnTime = QtGui.QLabel('LED ON Time for filter')
# 		self.LEDOnTime.setAlignment(QtCore.Qt.AlignCenter)
# 		self.LEDOnTime.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		
# 		self.LEDOnTimeCombo = QtGui.QComboBox()
# 		self.items_val = ['16 ','23 ','31 ','39 ','47 ','63 ','70 ','78 ','94 ','117 ']
# 		for i in self.items_val:
# 			i = i+unichr(int('b5',16)) +'A'
# 			self.LEDOnTimeCombo.addItems(i)
# 			
# 		self.LEDOnTimeForm = QtGui.QFormLayout()
# 		self.LEDOnTimeForm.addRow(self.LEDOnTime,self.LEDOnTimeCombo)
# 		
# 		self.LEDCommon = QtGui.QRadioButton('Common')
# 		self.LEDSet1 = QtGui.QRadioButton('Set1')
# 		self.LEDSet2 = QtGui.QRadioButton('Set2')
# 		self.LEDCommon.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.LEDSet1.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.LEDSet2.("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 6
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")			
# 										
# 		self.LEDSetn = QtGui.QVBoxLayout()
# 		self.LEDSetn.addWidget(self.LEDCommon)
# 		self.LEDSetn.addWidget(self.LEDSet1)
# 		self.LEDSetn.addWidget(self.LEDSet2)
# 		
# 		self.LED_Filter_Form = QtGui.QFormLayout()
# 		self.LED_Filter_Form.addRow(self.LEDOnTimeForm,self.LED_Filter_Form)
