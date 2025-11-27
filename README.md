# ShakeSynth
ShakeSynth is a two-part system for generating and applying real-world camera shake for use in compositing for VFX and feature-animation.

# ShakeSynth App
This is a dedicated app on the AppStore specifically for generating .shk profiles.

Simply use your iPhone to sample vibrations, shakes etc using the acceleromters and then review and adjust these directly.  The app will capture X/Y translation along with rotation and then decompose this capture into three seperate frequencies that can be visualised independently.  You can preview the shake in real time before exporting a .shk file for use within the Nuke Gizmo.

# ShakeSynth Gizmo
The ShakeSynth gizmo is a dedicated camera-shake node specifically designed to import and apply the .shk files created by the phone app.  However, there are a number of useful presets supplied to show you how the tool works.  Unlike many other camera-shake tools, ShakeSynth allows for very precise control over the different shake frequencies to fine tune the end result.

## The Frequencies
The app will split any captured waveform into three pre-defined frequencies that are then recombined to produce the final result.  These frequencies can be amimplified or reduced independently.

**Low**
- This is any movement that spans a 3-4 frame or more.  Think of this as low-frequency camera float.

**Mid**
- This is movement over 1-2 frames so more of the classic camera rumble/shake, where we see per-frame movement.

**High**
- This is sub-frame movement (ie jitter) that gives very fine vibration detail and subtlety.

## Post Scaling
The Gizmo has a nice feature that will sample the camera-shake and determine the minimum required scale required to cover the shake if required.

## Exporting Transforms
While its perfectly acceptable to use the ShakeSynth gizmo within the Nuke node graph, there is also a feature for exporting a standard Nuke Transform node that completely matches the result of the ShakeSynth tool including all sub-frame keyframes.
