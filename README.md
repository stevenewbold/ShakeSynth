# ShakeSynth
ShakeSynth is a two-part system (Nuke gizmo/iOS app) for generating and applying real-world camera shake for use in VFX and feature-animation.

There are a number of very useful third-party Nuke gizmos for applying camera shake, but these usually use procedurally generated noise functions to simulate reality.  ShakeSynth uses real world captured data profiles and allows precise adjustment of individual frequencies to adjust the feel of the camera shake.  The tool also has a number of useful features such as auto scaling, offsets and retimes. 

# ShakeSynth App
This is a dedicated app on the AppStore specifically for generating the .shk profiles that are used within the gizmo.

Simply use your iPhone to sample vibrations, shakes etc using the accelerometers and then review and adjust these directly.  The app will capture X/Y translation along with rotation and then decompose this data into three separate frequencies that can be visualised independently.  You can preview the shake in real time before exporting a .shk file for use within the Nuke Gizmo.

# ShakeSynth Gizmo
The ShakeSynth gizmo is a dedicated camera-shake node specifically designed to import and apply the .shk files created by the phone app.  However, there are a number of useful presets supplied to show you how the tool works.  Unlike many other camera-shake tools, ShakeSynth allows for very precise control over the different shake frequencies to fine tune the end result.

## Installation
The easiest way to install the gizmo is to download the entire ShakeSynth direcroy and add it to somewhere in your NUKE_PATH.  For individuals this is usually the '.nuke' directory in the home directory.  Facilities can install the tool in the same way as any other Nuke gizmo, but its crucial that the gizmo stays inside the ShakeSynth folder, along side the 'profiles' folder and icon files.

Use the following code within your menu.py file to correctly add ShakeSynth to Nuke.

```
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
```

## The Frequencies
The app will split any captured waveform into three pre-defined frequencies that are then recombined to produce the final result.  These frequencies can be amplified or reduced independently.

**Low**
- This is any movement that spans more than 3-4 frames.  Think of this as low-frequency camera float.

**Mid**
- This is movement over 1-2 frames so more of the classic camera rumble/shake, where we see per-frame movement.

**High**
- This is sub-frame movement (ie jitter) that gives very fine vibration detail and subtlety.

## Post Scaling
The Gizmo has a nice feature that will sample the camera-shake and determine the minimum required scale required to cover the shake if required.  Don't forget to reprocess this if you make significant changes to the amplitudes.

## Exporting Transforms
While its perfectly acceptable to use the ShakeSynth gizmo within the Nuke node graph, there is also a feature for exporting a standard Nuke Transform node that completely matches the result of the ShakeSynth tool including all sub-frame keyframes.

# Licence
**Copyright © 2025 Stephen Newbold**
You may use this software for free, including for commercial work.

Please don’t modify it, reverse-engineer it, or make your own versions based on it without permission.

You may share the original files as long as this notice stays with them.

The software is provided as-is, with no guarantees.

# Commercial Use
You are welcome to use ShakeSynth for free for any personal or commercial work (see Licence above) but a lot of time and effort goes into creating these tools so if you find it useful, please consider buying me a coffee at https://buymeacoffee.com/stevenewbold to support maintaining my personal Nuke licence.

<img width="100" height="100" alt="bmc_qr" src="https://github.com/user-attachments/assets/452b4ceb-0ed3-4c05-b60d-5fe49c5630d3" />
