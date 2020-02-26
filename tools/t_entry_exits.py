import arcpy
import os

import LUCI_EE.lib.log as log
import LUCI_EE.lib.common as common
import LUCI_EE.solo.entry_exits as entry_exits

from LUCI_EE.lib.refresh_modules import refresh_modules
refresh_modules([log, common, entry_exits])

def function(params):

    try:
        pText = common.paramsAsText(params)

        # Get inputs
        outputFolder = pText[1]
        studyMask = pText[3]
        streamNetwork = pText[4]
        facRaster = pText[5]

        # Run system checks
        common.runSystemChecks()

        # Set up logging output to file
        log.setupLogging(outputFolder)

        # Call RUSLE function
        entryExitPoints, streamNetworkFC = entry_exits.function(outputFolder, studyMask, streamNetwork, facRaster)
        
        # Set outputs
        if entryExitPoints is not None:
            arcpy.SetParameter(2, entryExitPoints)

        arcpy.SetParameter(6, streamNetworkFC)
        arcpy.SetParameter(7, studyMask)

        arcpy.SetParameter(0, True)
        log.info("Entry/exits operations completed successfully")

    except Exception:
        log.exception("Entry/exits tool failed")
        raise
