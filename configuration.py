'''
configuration.py adds the parent directory of the LUCI repo in sys.path so that modules can be imported using "from LUCI_SEEA..."
'''

import arcpy
import sys
import os

try:
    toolbox = "LUCI_EE"

    currentPath = os.path.dirname(os.path.abspath(__file__)) # should go to <base path>\LUCI_EE
    basePath = os.path.dirname(currentPath)

    luciEEPath = os.path.normpath(os.path.join(basePath, "LUCI_EE"))

    libPath = os.path.join(luciEEPath, "lib")
    logPath = os.path.join(luciEEPath, "logs")
    tablesPath = os.path.join(luciEEPath, "tables")
    displayPath = os.path.join(luciEEPath, "display")
    mxdsPath = os.path.join(displayPath, "mxds")
    dataPath = os.path.join(luciEEPath, "data")
    stylesheetsPath = os.path.join(luciEEPath, "stylesheets")

    oldScratchPath = os.path.join(luciEEPath, "LUCIscratch")
    scratchPath = os.path.join(basePath, "LUCIscratch")

    userSettingsFile = os.path.join(luciEEPath, "user_settings.xml")
    filenamesFile = os.path.join(luciEEPath, "filenames.xml")
    labelsFile = os.path.join(luciEEPath, "labels.xml")

    # Add basePath to sys.path so that modules can be imported using "import LUCI_SEEA.scripts.modulename" etc.
    if os.path.normpath(basePath) not in sys.path:
        sys.path.append(os.path.normpath(basePath))

    # Colour ramps
    diverging5ColoursPlusWaterUrban = ['#1a9641', '#a6d96a', '#ffffbf', '#fdae61', '#d7191c', '#00c5ff', '#000000']
    sequentialColours5PlusWaterUrban = ['#006837', '#31a354', '#78c679', '#c2e699', '#ffffcc', '#00c5ff', '#000000']
    qualitativeColours3PlusBlank = ['#ffffff', '#1b9e77', '#d95f02', '#7570b3']

    # Tolerance
    clippingTolerance = 0.00000000001

except Exception:
    arcpy.AddError("Configuration file not read successfully")
    raise
