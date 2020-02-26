# -*- coding: utf-8 -*-
import arcpy
import os
import sys

import configuration
try:
    reload(configuration)  # Python 2.7
except NameError:
    try:
        import importlib # Python 3.4
        importlib.reload(configuration)
    except Exception:
    	arcpy.AddError('Could not load configuration module')
    	sys.exit()

# Load and refresh the refresh_modules module
from LUCI_EE.lib.external.six.moves import reload_module
import LUCI_EE.lib.refresh_modules as refresh_modules
reload_module(refresh_modules)
from LUCI_EE.lib.refresh_modules import refresh_modules

import LUCI_EE.lib.input_validation as input_validation
refresh_modules(input_validation)

#############
### Tools ###
#############

import LUCI_EE.tool_classes.c_terrestrial_flow as c_terrestrial_flow
refresh_modules(c_terrestrial_flow)
TerrestrialFlow = c_terrestrial_flow.TerrestrialFlow

import LUCI_EE.tool_classes.c_EntryExits as c_EntryExits
refresh_modules(c_EntryExits)
StreamEntryExits = c_EntryExits.StreamEntryExits

import LUCI_EE.tool_classes.c_ChangeUserSettings as c_ChangeUserSettings
refresh_modules(c_ChangeUserSettings)
ChangeUserSettings = c_ChangeUserSettings.ChangeUserSettings

import LUCI_EE.tool_classes.c_PreprocessDEM as c_PreprocessDEM
refresh_modules(c_PreprocessDEM)
PreprocessDEM = c_PreprocessDEM.PreprocessDEM

##########################
### Toolbox definition ###
##########################

class Toolbox(object):

    def __init__(self):
        self.label = u'LUCI Entry Exits'
        self.alias = u'LUCI'
        self.tools = [ChangeUserSettings, TerrestrialFlow, StreamEntryExits, PreprocessDEM]
