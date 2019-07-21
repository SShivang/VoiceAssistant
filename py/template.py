smartList = [
{
'Step' : 0,
'Text' : "Finished with diagnostics. Continue?",
'YES'  : 0,
'NO'   : 0,
'Value-Required' : 'NO',
'Display-table':'NO'

},

{
  'Step' : 1,
  'Text' : "This is the Wiring Harness Guided Diagnostic with fault code SPN 3563 / FMI 3. Would you like to continue?",
  'YES'  : 2,
  'NO'   : 2,
  'Value-Required' : 'NO',
  'Display-table':'NO'

},

{
  'Step' : 2,
  'Text' : "Disconnect the intake manifold pressure/temperature sensor and inspect the harness side for bent, spread, or corroded terminals. Is any damage to the harness found?",
  'YES'  : 3,
  'NO'   : 4,
  'Value-Required' : 'YES',
  'Display-table':'NO'
},

{
  'Step' : 3,
  'Text' : "Repair the wiring harness as needed. Advance to TechLane for repair and SRT information.",
  'YES'  : 0,
  'NO'   : 0,
  'Value-Required' : 'NO',
  'Display-table':'NO'

},

{
  'Step' : 4,
  'Text' : "Turn on ignition. Say continue when ready.",
  'YES'  : 5,
  'NO'   : 5,
  'Value-Required' : 'NO',
  'Display-table':'NO'

},

{
  'Step' : 5,
  'Text' : "Use the link below to determine the correct diagnostic probe part number for the Intake Manifold Pressure/Temperature Sensor. Measure the voltage between pin 1 of the intake manifold pressure/temperature sensor harness connector and ground. Enter the voltage below. Is the voltage less than or equal to 6 V?",
  'YES'  : 3,
  'NO'   : 6,
  'Value-Required' : 'YES',
  'Display-table':'YES'

},

{
  'Step' : 6,
  'Text' : "Check for the presence of voltage between pins 2 and 4 on the intake manifold pressure/temperature sensor harness connector. Is voltage present?",
  'YES'  : 7,
  'NO'   : 3,
  'Value-Required' : 'YES',
  'Display-table':'NO'

},

{
  'Step' : 7,
  'Text' : "This component troubleshooting is complete with no trouble found. Go to the next component.",
  'YES'  : 0,
  'NO'   : 0,
  'Value-Required' : 'NO',
  'Display-table':'NO'

},
]