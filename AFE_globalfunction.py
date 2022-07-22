import math

# configuration of required Global Parameters

# configuration of Phase Timing Scheme
def AFE_config_phaseTimingScheme(phTmgScheme):
	phaseTiming = phTmgScheme
	if phTmgScheme == STAGGER_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    			  	False)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					False)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	False)
		logWindow_wid.settingLogText("STAGGER Mode is Selected")
		
	elif phTmgScheme == HIGH_PRF_MODE_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    				True)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					False)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	False)
		logWindow_wid.settingLogText("HIGH PRF Mode is Selected")
		
		# set the DIS_DEEP_SLEEP bit to '1' to disable the entry into deep sleep
# 		AFE_modifyRegGlobal(dev1.Page0.DIS_DEEP_SLEEP,					1)
# 		
# 		# set the EN_ALWAYS_ACTIVE bit to '1' to keep the device inactive state throughout the PRF cycle
# 		AFE_modifyRegGlobal(dev1.Page0.EN_ALWAYS_ACTIVE,				1)
# 		
# 		# Set REG_TDEEP_SLEEP_PWRUP and REG_TACTIVE_PWRUP registers to 0 to minimize these timing
# 		# overheads and utilize the PRF cycle more efficiently for accommodating the PPG phase
# 		AFE_modifyRegGlobal(dev1.Page0.REG_TDEEP_SLEEP_PWRUP,    		0)
# 		AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_PWRUP,   			0)
# 		
		
	elif phTmgScheme == MAX_AMB_REJ_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    				False)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					True)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	False)
		logWindow_wid.settingLogText("Maximum Ambient Rejection Mode is Selected")
		
	elif phTmgScheme == DIS_POST_AMB_MAX_AMB_REJ_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    				False)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					False)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	True)
		logWindow_wid.settingLogText('Disable Post Ambient Maximum Ambient Rejection Mode is Selected')

# 
# configuration of External Clock Decimation Factor
def AFE_config_extClkDecimation(decVal):
	if decVal == external_clk_NoDecimation:
		AFE_modifyRegGlobal(dev1.Page0.DIV_CLK_EXT, 	external_clk_NoDecimation)
	elif decVal == external_clk_Decimation_2:
		AFE_modifyRegGlobal(dev1.Page0.DIV_CLK_EXT, 	external_clk_Decimation_2)
	elif decVal == external_clk_Decimation_4:
		AFE_modifyRegGlobal(dev1.Page0.DIV_CLK_EXT, 	external_clk_Decimation_4)


# configuration of all the default parameters
def AFE_config_defaultTimings():
	# configuring Timing parameters associated with the various timing windows
	activePowUp = 24        # (REG_TACTIVE_PWRUP + 1) * tTE
	activePowDn = 1         # (REG_TACTIVE_PWDN + 2) * tTE
	deepSleepPowUp = 71     # (REG_TDEEP_SLEEP_PWRUP + 4.5) * tTE
	deepSleepPowDn = 5      # (REG_TDEEP_SLEEP_PWDN + 1) * tTE
	activeDataRdy = 3       # (REG_TACTIVE_DATA_RDY + 1) * tTE
	widthDataRdy = 0        # (REG_TW_DATA_RDY + 1) * tTE 
	tsep = 0                # REG_TSEP * tTE
	sampSep = 1             # samp window separation 1*tTE
	sepConvStart = 1        # 1*tTE
	
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_PWRUP,    	activePowUp)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_PWDN,     	activePowDn)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TDEEP_SLEEP_PWRUP,    deepSleepPowUp)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TDEEP_SLEEP_PWDN,     deepSleepPowDn)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_DATA_RDY,     activeDataRdy)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TW_DATA_RDY,     		widthDataRdy)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TSEP,     			tsep) #Separation between successive windows
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TSAMP_SEP, 			sampSep)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TSEP_CONV_START, 		sepConvStart)


# configuration of Clocking Mode
def AFE_config_clockingMode(clkMode):
	
	if clkMode == CLK_MODE_INT:
		# Setting all the default values
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			False)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			False)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	False)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			False)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			False)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	False)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	False)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		False)
		
# 		AFE_config_extClkDecimation(external_clk_NoDecimation)

		logWindow_wid.settingLogText('Internal Clock Mode is selected')
		
	elif clkMode == CLK_MODE_EXT:
		
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			True)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			True)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	False)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			False)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			False)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	False)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	False)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		False)
		
		AFE_config_extClkDecimation(external_clk_NoDecimation)
		
		logWindow_wid.settingLogText('External Clock Mode is selected')
		
	elif clkMode == CLK_MODE_SS:
		
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			False)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			False)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	True)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			True)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			False)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	True)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	True)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		False)
		
# 		AFE_config_extClkDecimation(external_clk_NoDecimation)

		logWindow_wid.settingLogText('Single Shot Clock Mode is selected')
		
	elif clkMode == CLK_MODE_MIX:
		
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			False)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			False)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	True)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			False)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			True)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	False)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	True)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		True)
		
# 		AFE_config_extClkDecimation(external_clk_NoDecimation)

		logWindow_wid.settingLogText('Mixed Clock Mode is selected with an external clock of 32.768 KHz')
		
		
	# enabling the timers
# 	AFE_modifyRegGlobal(dev1.Page0.PRF_COUNTER_ENABLE,				True)
# 	AFE_modifyRegGlobal(dev1.Page0.TIMER_ENABLE,				True)
# 	setting all the default timings
	AFE_config_defaultTimings()
	

# configuration of PRF freq and Step Count ( PRPCT parameter )

# default step count is 1

def AFE_config_stepcount(StepCount):
	# STEP_COUNT is derived from the register REG_STEP_COUNT as (REG_STEP_COUNT + 1)
	AFE_modifyRegGlobal(dev1.Page0.REG_STEP_COUNT, 		StepCount-1)
	
def AFE_config_prpct(prf_freq):

	setPRPCT = math.ceil(256000/prf_freq)
	
	# deriving PRPCT based on required PRF frequency
	AFE_modifyRegGlobal(dev1.Page0.PRPCT, 				setPRPCT)
	
	ValuesAssigned = [setPRPCT , 256000/setPRPCT]
	
	return ValuesAssigned
	
def AFE_config_ReConvThre(setReConvThreLEDdc):
	maxVol = 1.2
	oneLSB = maxVol/(pow(2, 21)-1)
	Conv_Thr_LED_DC = setReConvThreLEDdc/oneLSB
	Conv_Thr_LED_DC = Conv_Thr_LED_DC/pow(2,13)
	
	if Conv_Thr_LED_DC< (math.floor(Conv_Thr_LED_DC)+oneLSB):
		Conv_Thr_LED_DC = math.floor(Conv_Thr_LED_DC)
	else:
		Conv_Thr_LED_DC = math.ceil(Conv_Thr_LED_DC)

	AFE_modifyRegGlobal(dev1.Page0.REG_RECONV_THR_LED_DC,     Conv_Thr_LED_DC)
	
	return Conv_Thr_LED_DC
