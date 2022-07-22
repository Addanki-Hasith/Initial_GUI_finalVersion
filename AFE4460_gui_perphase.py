		

class phase_type(QtGui.QWidget):
	def __init__(self):
		super(phase_type,self).__init__()
		self.phase_type_lay = QtGui.QGridLayout()
		
		self.title = QtGui.QLabel('PHASE TYPE')
		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.val1 = QtGui.QRadioButton('Explicitly defined AMB')
		self.val2 = QtGui.QRadioButton('LED without Auto AMBs')
		self.val3 = QtGui.QRadioButton('LED with Auto AMBs')
		
		self.val1.setStyleSheet("QRadioButton::indicator" 
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
		self.val2.setStyleSheet("QRadioButton::indicator" 
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
		
		self.val3.setStyleSheet("QRadioButton::indicator" 
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
		
		self.val3_op1 = QtGui.QRadioButton('None')
		self.val3_op2 = QtGui.QRadioButton('Pre AMB')
		self.val3_op3 = QtGui.QRadioButton('Pre and Post AMB')
		
		
# 		self.sub_val_stylesheet = 
		self.val3_op1.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")
		self.val3_op2.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")
																								
		self.val3_op3.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")
		
		
		self.main_grp = QtGui.QButtonGroup()
		self.main_grp.addButton(self.val1)
		self.main_grp.addButton(self.val2)
		self.main_grp.addButton(self.val3)
		
		self.main_lay = QtGui.QVBoxLayout()
		self.main_lay.addWidget(self.val1)
		self.main_lay.addWidget(self.val2)
		self.main_lay.addWidget(self.val3)
		
		self.sub_grp = QtGui.QButtonGroup()
		self.sub_grp.addButton(self.val3_op1)
		self.sub_grp.addButton(self.val3_op2)
		self.sub_grp.addButton(self.val3_op3)
		
		self.sub_lay = QtGui.QVBoxLayout()
		self.sub_lay.addWidget(self.val3_op1)
		self.sub_lay.addWidget(self.val3_op2)
		self.sub_lay.addWidget(self.val3_op3)
		
		self.phase_type_lay.addWidget(self.title,0,0)
		self.phase_type_lay.addWidget(self.val1,1,0,1,2)
		self.phase_type_lay.addWidget(self.val2,2,0,2,2)
		self.phase_type_lay.addWidget(self.val3,3,0,3,2)
		
		self.phase_type_lay.addWidget(self.val3_op1,5,1)
		self.phase_type_lay.addWidget(self.val3_op2,6,1)
		self.phase_type_lay.addWidget(self.val3_op3,7,1)
		
		self.setLayout(self.phase_type_lay)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))

		self.setPalette(palette)
		
class transmitter_config(QtGui.QWidget):
	def __init__(self):
		super(transmitter_config,self).__init__()
		self.title = QtGui.QLabel('TRANSMITTER')
# 		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		
		self.LedOn = QtGui.QLabel('LED ON Time')
		
		self.LedOn.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
		self.LedOn.setAlignment(QtCore.Qt.AlignCenter)
		
		self.FilterSet = QtGui.QLabel('Filter Set Selected')
		self.FilterSet.setAlignment(QtCore.Qt.AlignCenter)
		
		self.FilterSet.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
		
		self.DRV_TXP = QtGui.QLabel('DRV_TXP')
		
		self.DRV_TXP.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
		self.DRV_TXP.setAlignment(QtCore.Qt.AlignCenter)
		
		self.DRV_TXN1 = QtGui.QLabel('DRV_TXN1')
		
		self.DRV_TXN1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
		self.DRV_TXN1.setAlignment(QtCore.Qt.AlignCenter)
		
		self.DRV_TXN2 = QtGui.QLabel('DRV_TXN2')
		
		self.DRV_TXN2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
		self.DRV_TXN2.setAlignment(QtCore.Qt.AlignCenter)
		
		self.ILED_DRV1 = QtGui.QLabel('ILED_DRV1 (mA)')
		
		self.ILED_DRV1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
		self.ILED_DRV1.setAlignment(QtCore.Qt.AlignCenter)
		
		self.ILED_DRV2 = QtGui.QLabel('ILED_DRV2 (mA)')
		
		self.ILED_DRV2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
		self.ILED_DRV2.setAlignment(QtCore.Qt.AlignCenter)
		
		
		self.LedOnCombo = QtGui.QComboBox()
		self.LedOnCombo.addItems(['LED ON Time1','LED ON Time2'])
		self.FilterSetCombo = QtGui.QComboBox()
		self.FilterSetCombo.addItems(['None','Set1','Set2'])
		self.DRV_TXPCombo = QtGui.QComboBox()
		self.DRV_TXPCombo.addItems(['TXP1','TXP2','TXP3','TXP4'])
		self.DRV_TXN1Combo = QtGui.QComboBox()
		self.DRV_TXN1Combo.addItems(['TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
		self.DRV_TXN2Combo = QtGui.QComboBox()
		self.DRV_TXN2Combo.addItems(['TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
		
		self.userval1 = QtGui.QLineEdit()
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.userval1.setSizePolicy(sizePolicy)
		self.userval1.setPlaceholderText('in mA')
		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
		self.userval2 = QtGui.QLineEdit()
		sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.userval2.setSizePolicy(sizePolicy2)
		self.userval2.setPlaceholderText('in mA')
		self.userval2.setAlignment(QtCore.Qt.AlignCenter)
		
		self.LedOn.setFixedWidth(150)
		self.DRV_TXP.setFixedWidth(150)
		self.DRV_TXN1.setFixedWidth(150)
		self.DRV_TXN2.setFixedWidth(150)
		self.ILED_DRV1.setFixedWidth(150)
		self.ILED_DRV2.setFixedWidth(150)
		
		self.LedOnCombo.setFixedWidth(80)
		self.DRV_TXPCombo.setFixedWidth(80)
		self.DRV_TXN1Combo.setFixedWidth(80)
		self.DRV_TXN2Combo.setFixedWidth(80)
		self.userval1.setFixedWidth(80)
		self.userval2.setFixedWidth(80)
		
		
		self.transmitter_config_lay = QtGui.QGridLayout()
		
		self.FilterSetCombo.setEnabled(False)
		
		self.LedOnForm = QtGui.QFormLayout()
		self.LedOnForm.addRow(self.LedOn,self.LedOnCombo)
		self.DRV_TXPForm = QtGui.QFormLayout()
		self.DRV_TXPForm.addRow(self.DRV_TXP,self.DRV_TXPCombo)
		self.DRV_TXN1Form = QtGui.QFormLayout()
		self.DRV_TXN1Form.addRow(self.DRV_TXN1,self.DRV_TXN1Combo)
		self.DRV_TXN2Form = QtGui.QFormLayout()
		self.DRV_TXN2Form.addRow(self.DRV_TXN2,self.DRV_TXN2Combo)
		self.ILED_DRV1Form = QtGui.QFormLayout()
		self.ILED_DRV1Form.addRow(self.ILED_DRV1,self.userval1)
		self.ILED_DRV2Form = QtGui.QFormLayout()
		self.ILED_DRV2Form.addRow(self.ILED_DRV2,self.userval2)

		self.transmitter_config_lay.addWidget(self.title,0,0)
		self.transmitter_config_lay.addLayout(self.LedOnForm,1,0)
		self.transmitter_config_lay.addWidget(self.FilterSet,2,0)
		self.transmitter_config_lay.addLayout(self.DRV_TXPForm,3,0)
		self.transmitter_config_lay.addLayout(self.DRV_TXN1Form,4,0)
		self.transmitter_config_lay.addLayout(self.DRV_TXN2Form,5,0)
		self.transmitter_config_lay.addLayout(self.ILED_DRV1Form,6,0)
		self.transmitter_config_lay.addLayout(self.ILED_DRV2Form,7,0)
		
		self.setLayout(self.transmitter_config_lay)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))

		self.setPalette(palette)

class tia_config(QtGui.QWidget):
	def __init__(self):
		super(tia_config,self).__init__()
		self.title =  QtGui.QLabel('TIA n')
		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		self.subTitle_PD = QtGui.QLabel('PDs connected to TIA : ')
		self.subTitle_PD.setStyleSheet("background: #f7f7f7; color:  rgba(0,124,140);")
		
		self.PD1_checkbox = QtGui.QCheckBox('PD1')
		self.PD2_checkbox = QtGui.QCheckBox('PD2')
		self.PD3_checkbox = QtGui.QCheckBox('PD3')
		self.PD4_checkbox = QtGui.QCheckBox('PD4')
		
		self.RF_label = QtGui.QLabel('RF')
		self.RF_label.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.RF_label.setFixedWidth(150)
		self.RF_label.setAlignment(QtCore.Qt.AlignCenter)
		self.RF_Combo = QtGui.QComboBox()
		self.RF_Combo.addItems(['3.7 KOhm','5 KOhm','10 KOhm','25 KOhm','33.3 KOhm','50 KOhm','71.5 KOhm','100 KOhm','142 KOhm','166 KOhm','200 KOhm','250 KOhm','500 KOhm','1 MOhm'])

		self.CF_ValLabel = QtGui.QLabel('Assigned CF')
		self.CF_ValLabel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.CF_ValLabel.setAlignment(QtCore.Qt.AlignCenter)
		
		ioffdac_str = 'IOFFDAC_LED (' + unichr(int('b5',16))+'A)'
		self.IOFFDAC_LEDLabel = QtGui.QLabel(ioffdac_str)
		self.IOFFDAC_LEDLabel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.IOFFDAC_LEDLabel.setFixedWidth(180)
		self.IOFFDAC_LEDLabel.setAlignment(QtCore.Qt.AlignCenter)
		
		place_holderText = 'in ' + unichr(int('b5',16)) +'A'
		self.IOFFDAC_userval = QtGui.QLineEdit()
		self.IOFFDAC_userval.setPlaceholderText(place_holderText)
		self.IOFFDAC_userval.setAlignment(QtCore.Qt.AlignCenter)
		
		self.EnableDC = QtGui.QLabel('Enable LED DC\n Cancellation')
		self.EnableDC.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.EnableDC.setAlignment(QtCore.Qt.AlignCenter)
		self.EnableDC.setFixedWidth(200)
		self.EnableDCYes = QtGui.QRadioButton('Yes')
		self.EnableDCNo = QtGui.QRadioButton('No')
		self.EnableDCYes.setStyleSheet("QRadioButton::indicator" 
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
		self.EnableDCNo.setStyleSheet("QRadioButton::indicator" 
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
										
		self.PD_GRID = QtGui.QGridLayout()
		self.PD_GRID.addWidget(self.PD1_checkbox,0,0)
		self.PD_GRID.addWidget(self.PD2_checkbox,0,1)
		self.PD_GRID.addWidget(self.PD3_checkbox,1,0)
		self.PD_GRID.addWidget(self.PD4_checkbox,1,1)
		
		self.RF_Form = QtGui.QFormLayout()
		self.RF_Form.addRow(self.RF_label,self.RF_Combo)
		
		self.IOFFDAC_Form = QtGui.QFormLayout()
		self.IOFFDAC_Form.addRow(self.IOFFDAC_LEDLabel,self.IOFFDAC_userval)
		
		self.EnableDCbool = QtGui.QVBoxLayout()
		self.EnableDCbool.addWidget(self.EnableDCYes)
		self.EnableDCbool.addWidget(self.EnableDCNo)
		
		self.EnableDC_Form = QtGui.QFormLayout()
		self.EnableDC_Form.addRow(self.EnableDC,self.EnableDCbool)
		
		self.tia_config_lay = QtGui.QGridLayout()
		self.tia_config_lay.addWidget(self.title,0,0)
		self.tia_config_lay.addWidget(self.subTitle_PD,1,0)
		self.tia_config_lay.addLayout(self.PD_GRID,2,0)
		self.tia_config_lay.addLayout(self.RF_Form,4,0)
		self.tia_config_lay.addWidget(self.CF_ValLabel,5,0)
		self.tia_config_lay.addLayout(self.IOFFDAC_Form,6,0)
		self.tia_config_lay.addLayout(self.EnableDC_Form,7,0)
		
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))

		self.setPalette(palette)
		self.setLayout(self.tia_config_lay)
		
class receiver_config(QtGui.QWidget):
	def __init__(self):
		super(receiver_config,self).__init__()
		self.title = QtGui.QLabel('RECEIVER')
		self.title.setAlignment(QtCore.Qt.AlignCenter)
		self.title.setFixedHeight(40)
		self.title.setFixedWidth(150)
		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		
		self.NoofTIAs = QtGui.QLabel('No. of TIAs')
		self.NoofTIAs.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.NoofTIAs.setFixedWidth(200)
		self.NoofTIAs.setAlignment(QtCore.Qt.AlignCenter)
		
		self.NUMAV = QtGui.QLabel('NUMAV')
		self.NUMAV.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.NUMAV.setFixedWidth(200)
		self.NUMAV.setAlignment(QtCore.Qt.AlignCenter)
		
		self.SchemeforAMB = QtGui.QLabel('Scheme for AMB Cancellation')
		self.SchemeforAMB.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.SchemeforAMB.setFixedWidth(250)
		self.SchemeforAMB.setAlignment(QtCore.Qt.AlignCenter)
		
		self.FIFOCtrl = QtGui.QLabel('FIFO DATA CTRL')
		self.FIFOCtrl.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.FIFOCtrl.setAlignment(QtCore.Qt.AlignCenter)
		
		self.MaskingFactor = QtGui.QLabel('Masking Factor')
		self.MaskingFactor.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.MaskingFactor.setAlignment(QtCore.Qt.AlignCenter)		
		
		self.EnableDRE = QtGui.QLabel('Enable DRE')
		self.EnableDRE.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.EnableDRE.setAlignment(QtCore.Qt.AlignCenter)
		self.EnableDRE.setFixedWidth(150)
		self.DecimationFactor = QtGui.QLabel('Decimation Factor')
		self.DecimationFactor.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
		self.DecimationFactor.setAlignment(QtCore.Qt.AlignCenter)
		
		self.NoofTIAsCombo = QtGui.QComboBox()
		self.no_ofTIAs = 4
		self.No_Of_TIAs = ['1','2','3','4']
		self.NoofTIAsCombo.addItems(self.No_Of_TIAs[0:self.no_ofTIAs])
		self.NoofTIAsCombo.setFixedWidth(40)
		self.NoofTIAs_lay = QtGui.QFormLayout()
		self.NoofTIAs_lay.addRow(self.NoofTIAs,self.NoofTIAsCombo)
		
		self.NUMAVCombo = QtGui.QComboBox()
		self.NUMAVCombo.addItems(['1','2','3','4','8'])
		self.NUMAVCombo.setFixedWidth(40)
		self.NUMAV_lay = QtGui.QFormLayout()
		self.NUMAV_lay.addRow(self.NUMAV,self.NUMAVCombo)
		
		
		self.SchemeforAMBCombo = QtGui.QComboBox()
		self.SchemeforAMBCombo.addItems(['AACM OFF','Estimate and Cancel AACM','Cancel AACM without Estimation'])
		self.SchemeforAMBCombo.setFixedWidth(300)

		self.SchemeforAMB_lay = QtGui.QFormLayout()
		self.SchemeforAMB_lay.addRow(self.SchemeforAMB,self.SchemeforAMBCombo)
		
		self.EnableDRE_bool = QtGui.QFormLayout()
		self.EnableDRE_yes = QtGui.QRadioButton('YES')
		self.EnableDRE_no = QtGui.QRadioButton('NO')
		self.EnableDRE_yes.setStyleSheet("QRadioButton::indicator" 
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
		self.EnableDRE_no.setStyleSheet("QRadioButton::indicator" 
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
										
		self.EnableDRE_bool.addRow(self.EnableDRE_yes,self.EnableDRE_no)
		
		self.EnableDRE_bool_wid = QtGui.QWidget()
		self.EnableDRE_bool_wid.setLayout(self.EnableDRE_bool)
		
		self.EnableDRE_lay = QtGui.QFormLayout()
		self.EnableDRE_lay.addRow(self.EnableDRE,self.EnableDRE_bool_wid)
		
		self.FIFOCtrlCombo = QtGui.QComboBox()
		self.FIFOCtrlCombo.addItems(['None'])
		self.FIFOCtrl.setFixedWidth(200)
		self.FIFOCtrlCombo.setFixedWidth(180)
		self.FIFOCtrlForm = QtGui.QFormLayout()
		self.FIFOCtrlForm.addRow(self.FIFOCtrl,self.FIFOCtrlCombo)
		
		self.MaskingFactorCombo = QtGui.QComboBox()
		self.MaskingFactorCombo.addItems(['None'])
		self.MaskingFactorCombo.setFixedWidth(150)
		self.MaskingFactor.setFixedWidth(200)
		self.MaskingFactorForm = QtGui.QFormLayout()
		self.MaskingFactorForm.addRow(self.MaskingFactor,self.MaskingFactorCombo)
		
		self.DecimationFactorCombo = QtGui.QComboBox()
		self.DecimationFactorCombo.addItems(['NO Decimation','Decimation by 2','Decimation by 4','Decimation by 8','Decimation by 16','Decimation by 32'])
		self.DecimationFactorCombo.setFixedWidth(180)
		self.DecimationFactorForm = QtGui.QFormLayout()
		self.DecimationFactorForm.addRow(self.DecimationFactor,self.DecimationFactorCombo)
		
		self.receiver_config_lay = QtGui.QGridLayout()
	
		self.receiver_config_lay.addWidget(self.title,0,0)
		self.receiver_config_lay.addLayout(self.NoofTIAs_lay,1,0)
		self.receiver_config_lay.addLayout(self.NUMAV_lay,2,0)
		self.receiver_config_lay.addLayout(self.SchemeforAMB_lay,3,0,3,2)
		self.receiver_config_lay.addLayout(self.EnableDRE_lay,3,2)
		self.receiver_config_lay.addLayout(self.FIFOCtrlForm,4,0)
		self.receiver_config_lay.addLayout(self.MaskingFactorForm,4,1)
		self.receiver_config_lay.addLayout(self.DecimationFactorForm,4,2)
		
		
		self.tia1 = tia_config()
		self.tia1.title.setText('TIA1')
		self.tia2 = tia_config()
		self.tia2.title.setText('TIA2')
		self.tia3 = tia_config()
		self.tia3.title.setText('TIA3')
		self.tia4 = tia_config()
		self.tia4.title.setText('TIA4')
	
		self.tiaN_grid = QtGui.QHBoxLayout()
		self.tiaN_grid.addWidget(self.tia1,1)
		self.tiaN_grid.addWidget(self.tia2,1)
		self.tiaN_grid.addWidget(self.tia3,1)
		self.tiaN_grid.addWidget(self.tia4,1)
		
		self.receiver_config_lay.addLayout(self.tiaN_grid,5,0,5,3)
				
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))

		self.setPalette(palette)

		self.setLayout(self.receiver_config_lay)

class Individual_config_layout(QtGui.QWidget):
	def __init__(self):
		super(Individual_config_layout,self).__init__()

		layout = QtGui.QGridLayout()
			
		self.phaseType = phase_type()
		self.phaseType.setFixedHeight(250)
		self.phaseType.setFixedWidth(300)
		layout.addWidget(self.phaseType,0,0)
		layout.addWidget(transmitter_config(),1.25,0)
		layout.addWidget(receiver_config(),0,1,0,5)
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))

		self.setPalette(palette)
		self.setLayout(layout)

class Summary_config_layout(QtGui.QWidget):
	def __init__(self):
		super(Summary_config_layout,self).__init__()
		layout = QtGui.QHBoxLayout()
		layout.addWidget(Color('red'))
		
		self.setLayout(layout)
		
class control_layout(QtGui.QWidget):
	def __init__(self):
		super(control_layout,self).__init__()
		self.view_layout1 = QtGui.QVBoxLayout()
		self.individual = QtGui.QRadioButton('Individual')
		self.summary = QtGui.QRadioButton('Summary')
		self.individual.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")
		self.summary.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")
		self.view_layout1.addWidget(self.individual)
		self.view_layout1.addWidget(self.summary)
		
		self.common_phN = QtGui.QFormLayout()
		self.ph1_8 = QtGui.QHBoxLayout()
		self.ph9_16 = QtGui.QHBoxLayout()
		self.phN = QtGui.QVBoxLayout()
		
		self.phN_arr = []
		for i in range(16):
			ph_str = 'PH' + str(i)
			self.phN_arr.append(QtGui.QRadioButton(ph_str))
			
		for i in range(8):
			self.phN_arr[i].setFixedWidth(70)
			self.phN_arr[i].setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")
			self.ph1_8.addWidget(self.phN_arr[i])
		
		for i in range(8):
			self.phN_arr[i+8].setFixedWidth(70)
			self.phN_arr[i+8].setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")
			self.ph9_16.addWidget(self.phN_arr[i+8])
		
		self.phN.addLayout(self.ph1_8)
		self.phN.addLayout(self.ph9_16)
		
		self.phN_wid = QtGui.QWidget()
		self.phN_wid.setLayout(self.phN)
		
		self.common_wid = QtGui.QRadioButton('Common')
		self.common_wid.setStyleSheet("QRadioButton::indicator" 
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

		self.common_phN.addRow(self.common_wid,self.phN_wid)
		
		self.req_ph_lay = QtGui.QFormLayout()
		self.userval1 = QtGui.QLineEdit()
		self.label1 = QtGui.QLabel('Required \nNo. of Phases')
		
		self.req_ph_lay.addRow(self.label1,self.userval1)
		
		self.viewLabel = QtGui.QLabel('View')
		self.viewLabel.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
				
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
		self.userval1.setSizePolicy(sizePolicy)
	
	
		self.label1.setFixedWidth(160)
		self.label1.setAlignment(QtCore.Qt.AlignCenter)
		self.label1.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
		self.userval1.setFixedWidth(40)
		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
		
		self.control_lay = QtGui.QGridLayout()
		self.control_lay.addLayout(self.req_ph_lay,0,0)
		self.control_lay.addLayout(self.common_phN,0,1,0,4)
		
		self.view_layout1_wid = QtGui.QWidget()
		self.view_layout1_wid.setLayout(self.view_layout1)
		
		self.view_form = QtGui.QFormLayout()
		self.view_form.addRow(self.viewLabel,self.view_layout1_wid)
		self.control_lay.addLayout(self.view_form,0,6)
		
# 		self.common_wid.setEnabled(False)
# 		for i in range(16):
# 			self.phN_arr[i].setEnabled(False)
		
# 		self.summary.setEnabled(False)
		self.individual.setChecked(True)
	
	
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
		self.setPalette(palette)
		self.setLayout(self.control_lay)
		

# class phase_type(QtGui.QWidget):
# 	def __init__(self):
# 		super(phase_type,self).__init__()
# 		self.phase_type_lay = QtGui.QGridLayout()
# 		
# 		self.title = QtGui.QLabel('PHASE TYPE')
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 
# 		self.val1 = QtGui.QRadioButton('Explicitly defined AMB')
# 		self.val1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val2 = QtGui.QRadioButton('LED without Auto AMBs')
# 		self.val2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val3 = QtGui.QRadioButton('LED with Auto AMBs')
# 		self.val3.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		self.val1.setStyleSheet("QRadioButton::indicator" 
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
# 		self.val2.setStyleSheet("QRadioButton::indicator" 
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
# 		
# 		self.val3.setStyleSheet("QRadioButton::indicator" 
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
# 		
# 		self.val3_op1 = QtGui.QRadioButton('None')
# 		self.val3_op2 = QtGui.QRadioButton('Pre AMB')
# 		self.val3_op3 = QtGui.QRadioButton('Pre and Post AMB')
# 		self.val3_op1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val3_op2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.val3_op3.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.val3_op1.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 		self.val3_op2.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 																								
# 		self.val3_op3.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 		self.main_grp = QtGui.QButtonGroup()
# 		self.main_grp.addButton(self.val1)
# 		self.main_grp.addButton(self.val2)
# 		self.main_grp.addButton(self.val3)
# 		
# 		self.main_lay = QtGui.QVBoxLayout()
# 		self.main_lay.addWidget(self.val1)
# 		self.main_lay.addWidget(self.val2)
# 		self.main_lay.addWidget(self.val3)
# 		
# 		self.sub_grp = QtGui.QButtonGroup()
# 		self.sub_grp.addButton(self.val3_op1)
# 		self.sub_grp.addButton(self.val3_op2)
# 		self.sub_grp.addButton(self.val3_op3)
# 		
# 		self.sub_lay = QtGui.QVBoxLayout()
# 		self.sub_lay.addWidget(self.val3_op1)
# 		self.sub_lay.addWidget(self.val3_op2)
# 		self.sub_lay.addWidget(self.val3_op3)
# 		
# 		self.phase_type_lay.addWidget(self.title,0,0)
# 		self.phase_type_lay.addWidget(self.val1,1,0,1,2)
# 		self.phase_type_lay.addWidget(self.val2,2,0,2,2)
# 		self.phase_type_lay.addWidget(self.val3,3,0,3,2)
# 		
# 		self.phase_type_lay.addWidget(self.val3_op1,5,1)
# 		self.phase_type_lay.addWidget(self.val3_op2,6,1)
# 		self.phase_type_lay.addWidget(self.val3_op3,7,1)
# 		
# 		self.phase_type_lay2 = QtGui.QVBoxLayout()
# 		self.phase_type_lay2.addWidget(self.title,2)
# 		self.phase_type_lay2.addWidget(self.val1,2)
# 		self.phase_type_lay2.addWidget(self.val2,2)
# 		self.phase_type_lay2.addWidget(self.val3,2)
# 		
# 		self.phase_type_lay3 = QtGui.QVBoxLayout()
# 		self.phase_type_lay3.addWidget(self.val3_op1)
# 		self.phase_type_lay3.addWidget(self.val3_op2)
# 		self.phase_type_lay3.addWidget(self.val3_op3)
# 		
# 		self.phase_type_lay4 = QtGui.QHBoxLayout()
# 		self.phase_type_lay4.addWidget(Color('#f7f7f7'),1)
# 		self.phase_type_lay4.addLayout(self.phase_type_lay3,2)
# 		
# 		self.phase_type_lay2.addLayout(self.phase_type_lay4)
# 		self.setLayout(self.phase_type_lay2)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)			
# 		
# 
# 
# class transmitter_config(QtGui.QWidget):
# 	def __init__(self):
# 		super(transmitter_config,self).__init__()
# 		self.title = QtGui.QLabel('TRANSMITTER')
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.LedOn = QtGui.QLabel('LED ON Time')
# 		self.LedOn.setWordWrap(True)
# 		self.LedOn.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.LedOn.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
# 		self.LedOn.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.FilterSet = QtGui.QLabel('Filter Set Selected')
# 		self.FilterSet.setWordWrap(True)
# 		self.FilterSet.setAlignment(QtCore.Qt.AlignCenter)
# 		self.FilterSet.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.FilterSet.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		
# 		self.DRV_TXP = QtGui.QLabel('DRV_TXP')		
# 		self.DRV_TXP.setWordWrap(True)
# 		self.DRV_TXP.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.DRV_TXP.setAlignment(QtCore.Qt.AlignCenter)
# 		self.DRV_TXP.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.DRV_TXN1 = QtGui.QLabel('DRV_TXN1')
# 		self.DRV_TXN1.setWordWrap(True)
# 		self.DRV_TXN1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.DRV_TXN1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.DRV_TXN1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 
# 		self.DRV_TXN2 = QtGui.QLabel('DRV_TXN2')	
# 		self.DRV_TXN2.setWordWrap(True)	
# 		self.DRV_TXN2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.DRV_TXN2.setAlignment(QtCore.Qt.AlignCenter)
# 		self.DRV_TXN2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.ILED_DRV1 = QtGui.QLabel('ILED_DRV1 (mA)')
# 		self.ILED_DRV1.setWordWrap(True)	
# 		self.ILED_DRV1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.ILED_DRV1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.ILED_DRV1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.ILED_DRV2 = QtGui.QLabel('ILED_DRV2 (mA)')
# 		self.ILED_DRV2.setWordWrap(True)	
# 		self.ILED_DRV2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
# 		self.ILED_DRV2.setAlignment(QtCore.Qt.AlignCenter)
# 		self.ILED_DRV2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.LedOnCombo = QtGui.QComboBox()
# 		self.LedOnCombo.addItems(['LED 1','LED 2'])
# 		self.LedOnCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.DRV_TXPCombo = QtGui.QComboBox()
# 		self.DRV_TXPCombo.addItems(['TXP1','TXP2','TXP3','TXP4'])
# 		self.DRV_TXPCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.DRV_TXN1Combo = QtGui.QComboBox()
# 		self.DRV_TXN1Combo.addItems(['TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
# 		self.DRV_TXN1Combo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 
# 		self.DRV_TXN2Combo = QtGui.QComboBox()
# 		self.DRV_TXN2Combo.addItems(['TXN1','TXN2','TXN3','TXN4','TXN5','TXN6','TXN7','TXN8'])
# 		self.DRV_TXN2Combo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.userval1 = QtGui.QLineEdit()
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.userval1.setSizePolicy(sizePolicy)
# 		self.userval1.setPlaceholderText('in mA')
# 		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.userval2 = QtGui.QLineEdit()
# 		sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.userval2.setSizePolicy(sizePolicy2)
# 		self.userval2.setPlaceholderText('in mA')
# 		self.userval2.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		
# 		self.LedOnForm = QtGui.QHBoxLayout()
# 		self.LedOnForm.addWidget(self.LedOn,4)
# 		self.LedOnForm.addWidget(self.LedOnCombo,1)
# 		
# 		self.DRV_TXPForm = QtGui.QHBoxLayout()
# 		self.DRV_TXPForm.addWidget(self.DRV_TXP,3)
# 		self.DRV_TXPForm.addWidget(self.DRV_TXPCombo,1)
# 		
# 		self.DRV_TXN1Form = QtGui.QHBoxLayout()
# 		self.DRV_TXN1Form.addWidget(self.DRV_TXN1,3)
# 		self.DRV_TXN1Form.addWidget(self.DRV_TXN1Combo,1)
# 		
# 		self.DRV_TXN2Form = QtGui.QHBoxLayout()
# 		self.DRV_TXN2Form.addWidget(self.DRV_TXN2,3)
# 		self.DRV_TXN2Form.addWidget(self.DRV_TXN2Combo,1)
# 	
# 		self.ILED_DRV1Form = QtGui.QHBoxLayout()
# 		self.ILED_DRV1Form.addWidget(self.ILED_DRV1,3)
# 		self.ILED_DRV1Form.addWidget(self.userval1,1)
# 
# 		self.ILED_DRV2Form = QtGui.QHBoxLayout()
# 		self.ILED_DRV2Form.addWidget(self.ILED_DRV2,3)
# 		self.ILED_DRV2Form.addWidget(self.userval2,1)
# 
# 		self.transmitter_config_lay = QtGui.QVBoxLayout()
# 		
# 		self.transmitter_config_lay.addWidget(self.title)
# 		self.transmitter_config_lay.addLayout(self.LedOnForm)
# 		self.transmitter_config_lay.addWidget(self.FilterSet)
# 		self.transmitter_config_lay.addLayout(self.DRV_TXPForm)
# 		self.transmitter_config_lay.addLayout(self.DRV_TXN1Form)
# 		self.transmitter_config_lay.addLayout(self.DRV_TXN2Form)
# 		self.transmitter_config_lay.addLayout(self.ILED_DRV1Form)
# 		self.transmitter_config_lay.addLayout(self.ILED_DRV2Form)
# 		
# 		self.setLayout(self.transmitter_config_lay)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window,QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)
# 
# class tia_config(QtGui.QWidget):
# 	def __init__(self):
# 		super(tia_config,self).__init__()
# 		self.title =  QtGui.QLabel('TIA n')
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.subTitle_PD = QtGui.QLabel('PDs connected to TIA : ')
# 		self.subTitle_PD.setStyleSheet("background: #f7f7f7; color:  rgba(0,124,140);")
# 		self.subTitle_PD.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.PD1_checkbox = QtGui.QCheckBox('PD1')
# 		self.PD1_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.PD2_checkbox = QtGui.QCheckBox('PD2')
# 		self.PD2_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.PD3_checkbox = QtGui.QCheckBox('PD3')
# 		self.PD3_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.PD4_checkbox = QtGui.QCheckBox('PD4')
# 		self.PD4_checkbox.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 				
# 		self.RF_label = QtGui.QLabel('RF')
# 		self.RF_label.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.RF_label.setAlignment(QtCore.Qt.AlignCenter)
# 		self.RF_label.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		self.RF_Combo = QtGui.QComboBox()
# 		self.RF_Combo.addItems(['3.7 KOhm','5 KOhm','10 KOhm','25 KOhm','33.3 KOhm','50 KOhm','71.5 KOhm','100 KOhm','142 KOhm','166 KOhm','200 KOhm','250 KOhm','500 KOhm','1 MOhm'])
# 		self.RF_Combo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		self.CF_ValLabel = QtGui.QLabel('Assigned CF')
# 		self.CF_ValLabel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.CF_ValLabel.setAlignment(QtCore.Qt.AlignCenter)
# 		self.CF_ValLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		ioffdac_str = 'IOFFDAC_LED (' + unichr(int('b5',16))+'A)'
# 		self.IOFFDAC_LEDLabel = QtGui.QLabel(ioffdac_str)
# 		self.IOFFDAC_LEDLabel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.IOFFDAC_LEDLabel.setAlignment(QtCore.Qt.AlignCenter)
# 		self.IOFFDAC_LEDLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)		
# 		
# 		place_holderText = 'in ' + unichr(int('b5',16)) +'A'
# 		self.IOFFDAC_userval = QtGui.QLineEdit()
# 		self.IOFFDAC_userval.setPlaceholderText(place_holderText)
# 		self.IOFFDAC_userval.setAlignment(QtCore.Qt.AlignCenter)
# 		self.IOFFDAC_userval.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		
# 		self.EnableDC = QtGui.QLabel('Enable LED DC\n Cancellation')
# 		self.EnableDC.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.EnableDC.setAlignment(QtCore.Qt.AlignCenter)
# 		self.EnableDC.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		
# 		self.EnableDCYes = QtGui.QRadioButton('Yes')
# 		self.EnableDCYes.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDCNo = QtGui.QRadioButton('No')
# 		self.EnableDCNo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDCYes.setStyleSheet("QRadioButton::indicator" 
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
# 		self.EnableDCNo.setStyleSheet("QRadioButton::indicator" 
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
# 		self.PD_GRID = QtGui.QGridLayout()
# 		self.PD_GRID.addWidget(self.PD1_checkbox,0,0)
# 		self.PD_GRID.addWidget(self.PD2_checkbox,0,1)
# 		self.PD_GRID.addWidget(self.PD3_checkbox,1,0)
# 		self.PD_GRID.addWidget(self.PD4_checkbox,1,1)
# 		
# 		self.RF_Form = QtGui.QHBoxLayout()
# 		self.RF_Form.addWidget(self.RF_label,3)
# 		self.RF_Form.addWidget(self.RF_Combo,1)
# 		
# 		self.IOFFDAC_Form = QtGui.QHBoxLayout()
# 		self.IOFFDAC_Form.addWidget(self.IOFFDAC_LEDLabel,3)
# 		self.IOFFDAC_Form.addWidget(self.IOFFDAC_userval,1)
# 		
# 		self.EnableDCbool = QtGui.QVBoxLayout()
# 		self.EnableDCbool.addWidget(self.EnableDCYes)
# 		self.EnableDCbool.addWidget(self.EnableDCNo)
# 		
# 		self.EnableDC_Form = QtGui.QHBoxLayout()
# 		self.EnableDC_Form.addWidget(self.EnableDC)
# 		self.EnableDC_Form.addLayout(self.EnableDCbool)
# 		
# 		self.tia_config_lay = QtGui.QGridLayout()
# 		self.tia_config_lay.addWidget(self.title,0,0)
# 		self.tia_config_lay.addWidget(self.subTitle_PD,1,0)
# 		self.tia_config_lay.addLayout(self.PD_GRID,2,0)
# 		self.tia_config_lay.addLayout(self.RF_Form,4,0)
# 		self.tia_config_lay.addWidget(self.CF_ValLabel,5,0)
# 		self.tia_config_lay.addLayout(self.IOFFDAC_Form,6,0)
# 		self.tia_config_lay.addLayout(self.EnableDC_Form,7,0)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)
# 		self.setLayout(self.tia_config_lay)
# 
# 
# class receiver_config(QtGui.QWidget):
# 	def __init__(self):
# 		super(receiver_config,self).__init__()
# 		self.title = QtGui.QLabel('RECEIVER')
# 		self.title.setAlignment(QtCore.Qt.AlignLeft)
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		
# 		self.NoofTIAs = QtGui.QLabel('No. of TIAs')
# 		self.NoofTIAs.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NoofTIAs.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.NoofTIAs.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.NUMAV = QtGui.QLabel('NUMAV')
# 		self.NUMAV.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.NUMAV.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NUMAV.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.SchemeforAMB = QtGui.QLabel('Scheme for AMB Cancellation')
# 		self.SchemeforAMB.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.SchemeforAMB.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.SchemeforAMB.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.FIFOCtrl = QtGui.QLabel('FIFO DATA CTRL')
# 		self.FIFOCtrl.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.FIFOCtrl.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.FIFOCtrl.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.MaskingFactor = QtGui.QLabel('Masking Factor')
# 		self.MaskingFactor.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.MaskingFactor.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.MaskingFactor.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.EnableDRE = QtGui.QLabel('Enable DRE')
# 		self.EnableDRE.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.EnableDRE.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDRE.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.DecimationFactor = QtGui.QLabel('Decimation Factor')
# 		self.DecimationFactor.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color:  rgba(0,124,140);")
# 		self.DecimationFactor.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.DecimationFactor.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.NoofTIAsCombo = QtGui.QComboBox()
# 		self.no_ofTIAs = 4
# 		self.No_Of_TIAs = ['1','2','3','4']
# 		self.NoofTIAsCombo.addItems(self.No_Of_TIAs[0:self.no_ofTIAs])
# 		self.NoofTIAsCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NoofTIAs_lay = QtGui.QHBoxLayout()
# 		self.NoofTIAs_lay.addWidget(self.NoofTIAs,3)
# 		self.NoofTIAs_lay.addWidget(self.NoofTIAsCombo,1)
# 		self.NoofTIAs_lay.addWidget(Color('#f7f7f7'),10)
# 		
# 		self.NUMAVCombo = QtGui.QComboBox()
# 		self.NUMAVCombo.addItems(['1','2','3','4','8'])
# 		self.NUMAVCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.NUMAV_lay = QtGui.QHBoxLayout()
# 		self.NUMAV_lay.addWidget(self.NUMAV,3)
# 		self.NUMAV_lay.addWidget(self.NUMAVCombo,1)
# 		self.NUMAV_lay.addWidget(Color('#f7f7f7'),10)
# 		
# 		self.SchemeforAMBCombo = QtGui.QComboBox()
# 		self.SchemeforAMBCombo.addItems(['AACM OFF','Estimate and Cancel AACM','Cancel AACM without Estimation'])
# 		self.SchemeforAMBCombo.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.SchemeforAMB_lay = QtGui.QHBoxLayout()
# 		self.SchemeforAMB_lay.addWidget(self.SchemeforAMB,3)
# 		self.SchemeforAMB_lay.addWidget(self.SchemeforAMBCombo,1)
# 		self.SchemeforAMB_lay.addWidget(Color('#f7f7f7'),2)
# 		
# 		self.EnableDRE_bool = QtGui.QFormLayout()
# 		self.EnableDRE_yes = QtGui.QRadioButton('YES')
# 		self.EnableDRE_yes.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDRE_no = QtGui.QRadioButton('NO')
# 		self.EnableDRE_no.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
# 		self.EnableDRE_yes.setStyleSheet("QRadioButton::indicator" 
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
# 		self.EnableDRE_no.setStyleSheet("QRadioButton::indicator" 
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
# 										
# 		self.EnableDRE_bool.addRow(self.EnableDRE_yes,self.EnableDRE_no)
# 		
# 		self.EnableDRE_bool_wid = QtGui.QWidget()
# 		self.EnableDRE_bool_wid.setLayout(self.EnableDRE_bool)
# 		
# # 		self.EnableDRE_lay = QtGui.QHBoxLayout()
# # 		self.EnableDRE_lay.addWidget(self.EnableDRE)
# # 		self.EnableDRE_lay.addWidget(self.EnableDRE_bool_wid)
# 		
# 		self.SchemeforAMB_lay.addWidget(self.EnableDRE,2)
# 		self.SchemeforAMB_lay.addWidget(self.EnableDRE_bool_wid,2)
# 		self.FIFOCtrlCombo = QtGui.QComboBox()
# 		self.FIFOCtrlCombo.addItems(['None'])
# 		self.FIFOCtrlForm = QtGui.QHBoxLayout()
# 		self.FIFOCtrlForm.addWidget(self.FIFOCtrl,3)
# 		self.FIFOCtrlForm.addWidget(self.FIFOCtrlCombo,4)
# 		
# 		self.MaskingFactorCombo = QtGui.QComboBox()
# 		self.MaskingFactorCombo.addItems(['None'])
# 		self.MaskingFactorForm = QtGui.QHBoxLayout()
# 		self.FIFOCtrlForm.addWidget(self.MaskingFactor,3)
# 		self.FIFOCtrlForm.addWidget(self.MaskingFactorCombo,4)
# 		
# 		self.DecimationFactorCombo = QtGui.QComboBox()
# 		self.DecimationFactorCombo.addItems(['NO Decimation','Decimation by 2','Decimation by 4','Decimation by 8','Decimation by 16','Decimation by 32'])
# 		self.DecimationFactorForm = QtGui.QHBoxLayout()
# 		self.FIFOCtrlForm.addWidget(self.DecimationFactor,5)
# 		self.FIFOCtrlForm.addWidget(self.DecimationFactorCombo,1)
# 		
# 		self.receiver_config_lay = QtGui.QVBoxLayout()
# 	
# # 		self.receiver_config_lay.addWidget(self.title,0,0)
# # 		self.receiver_config_lay.addLayout(self.NoofTIAs_lay,1,0)
# # 		self.receiver_config_lay.addLayout(self.NUMAV_lay,2,0)
# # 		self.receiver_config_lay.addLayout(self.SchemeforAMB_lay,3,0,3,1)
# # 		self.receiver_config_lay.addLayout(self.EnableDRE_lay,3,2)
# # 		self.receiver_config_lay.addLayout(self.FIFOCtrlForm,4,0)
# # 		self.receiver_config_lay.addLayout(self.MaskingFactorForm,4,1)
# # 		self.receiver_config_lay.addLayout(self.DecimationFactorForm,4,2)
# 		
# 		self.receiver_config_lay.addWidget(self.title)
# 		self.receiver_config_lay.addLayout(self.NoofTIAs_lay)
# 		self.receiver_config_lay.addLayout(self.NUMAV_lay)
# 		self.receiver_config_lay.addLayout(self.SchemeforAMB_lay)
# # 		self.receiver_config_lay.addLayout(self.EnableDRE_lay)
# 		self.receiver_config_lay.addLayout(self.FIFOCtrlForm)
# # 		self.receiver_config_lay.addLayout(self.MaskingFactorForm)
# # 		self.receiver_config_lay.addLayout(self.DecimationFactorForm)
# 		
# 		self.tia1 = tia_config()
# 		self.tia1.title.setText('TIA1')
# 		self.tia2 = tia_config()
# 		self.tia2.title.setText('TIA2')
# 		self.tia3 = tia_config()
# 		self.tia3.title.setText('TIA3')
# 		self.tia4 = tia_config()
# 		self.tia4.title.setText('TIA4')
# 	
# 		self.tiaN_grid = QtGui.QHBoxLayout()
# 		self.tiaN_grid.addWidget(self.tia1,1)
# 		self.tiaN_grid.addWidget(self.tia2,1)
# 		self.tiaN_grid.addWidget(self.tia3,1)
# 		self.tiaN_grid.addWidget(self.tia4,1)
# 		
# 		self.receiver_config_main = QtGui.QVBoxLayout()
# 		self.receiver_config_main.addLayout(self.receiver_config_lay,2)
# 		self.receiver_config_main.addLayout(self.tiaN_grid,3)
# 				
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 
# 		self.setPalette(palette)
# 
# 		self.setLayout(self.receiver_config_main)
# 		
# 											
# class Individual_config_layout(QtGui.QWidget):
# 	def __init__(self):
# 		super(Individual_config_layout,self).__init__()
# 
# 		layout = QtGui.QHBoxLayout()
# 		
# 		sub_lay = QtGui.QVBoxLayout()
# 		self.phaseType = phase_type()
# 		self.transmitter = transmitter_config()
# 		
# 		sub_lay.addWidget(self.phaseType,2)
# 		sub_lay.addWidget(self.transmitter,3)
# 		
# 		layout.addLayout(sub_lay,2)
# 		layout.addWidget(receiver_config(),5)
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 
# # 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.setPalette(palette)
# 		self.setLayout(layout)
# 		
# class Summary_config_layout(QtGui.QWidget):
# 	def __init__(self):
# 		super(Summary_config_layout,self).__init__()
# 		layout = QtGui.QHBoxLayout()
# 		layout.addWidget(Color('red'))
# 		
# # 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.setLayout(layout)
# 		
# class control_layout(QtGui.QWidget):
# 	def __init__(self):
# 		super(control_layout,self).__init__()
# 		
# 		self.individual = QtGui.QRadioButton('Individual')
# 		self.summary = QtGui.QRadioButton('Summary')
# 		self.individual.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.summary.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.individual.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 		self.summary.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 										
# 		self.view_layout1 = QtGui.QVBoxLayout()
# 		self.view_layout1.addWidget(self.individual)
# 		self.view_layout1.addWidget(self.summary)
# 		
# 		self.viewLabel = QtGui.QLabel('View')
# 		self.viewLabel.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.viewLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.view_layout =  QtGui.QFormLayout()
# # 		self.view_layout.addWidget(self.viewLabel,2)
# # 		self.view_layout.addLayout(self.view_layout1,3)
# 		self.view_layout.addRow(self.viewLabel,self.view_layout1)
# 		self.common_phN = QtGui.QHBoxLayout()
# 		self.ph1_8 = QtGui.QHBoxLayout()
# 		self.ph9_16 = QtGui.QHBoxLayout()
# 		self.phN = QtGui.QVBoxLayout()
# 		
# 		self.phN_arr = []
# 		for i in range(16):
# 			ph_str = 'PH' + str(i)
# 			self.phN_arr.append(QtGui.QRadioButton(ph_str))
# 			
# 		for i in range(8):
# 			self.phN_arr[i].setFixedWidth(70)
# 			self.phN_arr[i].setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 			self.ph1_8.addWidget(self.phN_arr[i])
# 			self.phN_arr[i].setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		for i in range(8):
# 			self.phN_arr[i+8].setFixedWidth(70)
# 			self.phN_arr[i+8].setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 15px;"
# 										"height: 15px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:10px;"
# 										"height: 10px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:8px;"
# 										"}")
# 			self.ph9_16.addWidget(self.phN_arr[i+8])
# 			self.phN_arr[i+1].setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 			
# 		self.phN.addLayout(self.ph1_8)
# 		self.phN.addLayout(self.ph9_16)
# 		
# 		self.common_wid = QtGui.QRadioButton('Common')
# 		self.common_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.common_wid.setStyleSheet("QRadioButton::indicator" 
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
# 										
# # 		self.common_phN.addRow(self.common_wid,self.phN)
# 		self.common_phN.addWidget(self.common_wid)
# 		self.common_phN.addLayout(self.phN)
# 		
# 		self.common_ph_group = QtGui.QButtonGroup()
# 		self.common_ph_group.addButton(self.common_wid)
# 		for i in range(16):
# 			self.common_ph_group.addButton(self.phN_arr[i])
# 			
# 		self.req_ph_lay = QtGui.QFormLayout()
# 		self.userval1 = QtGui.QLineEdit()
# 		self.label1 = QtGui.QLabel('Required \nNo. of Phases')
# # 		self.userval1.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
# 		self.label1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.userval1.setSizePolicy(sizePolicy)
# 	
# 		self.label1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.label1.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
# # 		self.userval1.setFixedWidth(40)
# 
# 		self.req_ph_lay.addRow(self.label1,self.userval1)		
# 		
# 		self.control_lay = QtGui.QHBoxLayout()
# 		self.control_lay.addLayout(self.req_ph_lay)
# 		self.control_lay.addLayout(self.common_phN)
# 		self.control_lay.addLayout(self.view_layout)
# 		
# 		self.individual.setChecked(True)
# 		
# # 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		self.setLayout(self.control_lay)
