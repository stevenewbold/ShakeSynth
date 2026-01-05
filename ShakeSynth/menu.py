import nuke

### LOAD SHAKESYNTH /W CODE FOR REFRESHING PROFILES ###

nuke.pluginAddPath('ShakeSynth')

toolbar = nuke.menu('Nodes')

SS_menu = toolbar.addMenu(
    'ShakeSynth',
    icon='ShakeSynthMenu.png'
)

SS_menu.addCommand(
    'ShakeSynth',
    'nuke.createNode("ShakeSynth")'
)

def refreshProfiles():

    n = nuke.thisNode()
    k = n.knob("refreshProfiles")
    k.execute()

nuke.addOnCreate(refreshProfiles, nodeClass="ShakeSynth")

###