# ShakeSynth
ShakeSynth is a two-part system (Nuke gizmo/iOS app) for generating and applying real-world camera shake for use in VFX and feature-animation.

There are a number of very useful third-party Nuke gizmos for applying camera shake, but these usually use procedurally generated noise functions to simulate reality.  ShakeSynth uses real world captured data profiles and allows precise adjustment of individual frequencies to adjust the feel of the camera shake.  The tool also has a number of useful features such as auto scaling, offsets and retimes. 


# ShakeSynth App
This is a dedicated app on the AppStore specifically for generating the .shk profiles that are used within the gizmo.

https://apps.apple.com/gb/app/shakesynth/id6756015883

Simply use your iPhone to sample vibrations, shakes etc using the accelerometers and then review and adjust these directly.  The app will capture X/Y translation along with rotation and then decompose this data into three separate frequencies that can be visualised independently.  You can preview the shake in real time before exporting a .shk file for use within the Nuke Gizmo.

<img width="231" height="500" alt="ShakeSynthApp" src="https://github.com/user-attachments/assets/0cf71c0a-9137-4053-a3b1-482a6dc78a86" />

# ShakeSynth Gizmo
The ShakeSynth gizmo is a dedicated camera-shake Nuke node specifically designed to import and apply the .shk files created by the phone app.  However, there are a number of useful presets supplied to show you how the tool works.  Unlike many other camera-shake tools, ShakeSynth allows for very precise control over the different shake frequencies to fine tune the end result.

<img width="1124" height="585" alt="ShakeSynthUI" src="https://github.com/user-attachments/assets/cb9356d0-b683-4837-8ff2-8bfd22ea9d72" />

## Installation
The easiest way to install the gizmo is to download the entire ShakeSynth directory and add it to somewhere in your NUKE_PATH.  For individuals this is usually the '.nuke' directory in the home directory.  Facilities can install the tool in the same way as any other Nuke gizmo, but its crucial that the gizmo stays inside the ShakeSynth folder, along side the 'profiles' folder and icon files.

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


## Adding Custom profiles
Adding profiles to ShakeSynth is as easy as copying a .shk file (created by the free ShakeSynth app) to the 'profiles' directory of your installation.  There are a number of pre-exisiting profiles included to get you started and make the tool useful for those without access to the app.

The .shk files are somewhat human readable so its possible to adjust these in a text editor if required.


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


# Tips and Tricks
It is a deliberate choice not to allow the saving of adjusted profiles within the gizmo as it adds a lot of complexity with permissions if installed facility wide.  However, it is perfectly acceptable to use Nuke's own defaults system to create loadable custom states.  It is also pretty straight forward to create duplicates and variations of profiles by manually adjusting .shk files and giving them unique names.  Of course, saved ShakeSynth nodes will maintain their settings.

It is also suggested to use a sensible naming of presets to allow users to find the most suitable one.  Typically this would start with the type of shake, then any type custom description and a version number.  For instance profiles may be called something like,

```
vibration_carEngine_v001.shk
```
or
```
impact_explosion_v001.shk
```

Use the provided profiles as a guide to what us effective in everyday use, but the tool will pick up any name as long as there are no spaces and has a .shk extension.

Capturing useful waveforms takes a bit of practice, but the following is good advice,
- make sure the phone is held as vertically as possible by propping it up.
- stabilising with your hand can dampen high frequency detail, so avoid this if that is what you are trying to capture
- placing the phone on a hard surface can help capture a full dynamic range of movement
- experiment with adjusting specific frequencies, for instance, killing mid/high frequencies can help create float, or killing low frequencies can help create nice jitter without large translations.


# Licence
**Copyright © 2025 Stephen Newbold**
You may use this software for free, including for commercial work.

Please don’t modify it, reverse-engineer it, or make your own versions based on it without permission.

You may share the original files as long as this notice stays with them.

The software is provided as-is, with no guarantees.


# Commercial Use
You are welcome to use ShakeSynth for free for any personal or commercial work (see Licence above) but a lot of time and effort goes into creating these tools so if you find it useful, please consider buying me a coffee at https://buymeacoffee.com/stevenewbold to support maintaining my personal Nuke licence (and coffee addiction! :) ).

<img width="100" height="100" alt="bmc_qr" src="https://github.com/user-attachments/assets/452b4ceb-0ed3-4c05-b60d-5fe49c5630d3" />
