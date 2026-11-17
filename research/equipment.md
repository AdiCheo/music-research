# Equipment checklist

The model and OS affect cable, power and driver choices. Start by filling in the following inventory.

| Gear | Confirm on the device |
| --- | --- |
| MacBook, iPad, iPhone | Exact model, OS and port. Confirm Apple silicon vs Intel on the Mac and USB-C vs Lightning on the mobile devices. |
| Windows workstation | Windows version, CPU, RAM and GPU model/VRAM. Record the GPU backend supported by each audio model, then compare with CPU using the same clip. |
| Pixel | Model, Android version, USB-C adapter and the app's ability to select or use USB input. |
| Keyboard | Model, whether it sends USB MIDI, 5-pin MIDI or audio, and whether the main output is mono or stereo. |
| Plug-in electroacoustic guitar | Pickup/preamp output type, battery if applicable and the connector. |
| Scarlett “2i mini” | Exact name and generation from the underside or rear label. A Solo and a 2i2 can have different usable input combinations. |
| RØDE Wireless PRO ×2 | Count receivers and transmitters, identify which belong to each kit and record firmware plus cables. Confirm whether “×2” means two transmitters in one kit or two complete kits. |

## First routes to test

| Goal | Signal path | Test |
| --- | --- | --- |
| Record guitar on Mac or Windows | Guitar pickup → Scarlett instrument-capable ¼-inch input in INST mode → computer → DAW. Headphones from the Scarlett. | Verify input routing in the DAW, play hard and check that peaks have headroom. On Windows, try the Focusrite driver and ASIO if the exact interface supports it. [Focusrite support](https://support.focusrite.com/) |
| Record guitar on iPad | Scarlett → iPad with a data cable or the compatible powered adapter or hub specified for that model. | Check the exact Focusrite compatibility entry before testing. Record ten seconds and confirm the DAW received the guitar input. [iOS/iPadOS compatibility](https://support.focusrite.com/hc/en-gb/articles/14071293233810-iOS-and-iPadOS-Compatibility) · [USB-C iPad setup](https://support.focusrite.com/hc/en-gb/articles/360002662100-Using-an-audio-interface-with-a-USB-C-iPad-Pro) |
| Play keys or capture their sound | USB MIDI → host and a virtual instrument if the keyboard supports MIDI. Keyboard audio out → Scarlett line input for the keyboard's own sound. Stereo requires two available line inputs. | Record separate MIDI and audio passes if inputs are limited. Check sustain and velocity for MIDI and left/right routing for audio. [GarageBand iPad audio and MIDI import](https://support.apple.com/en-gb/guide/garageband-ipad/-chsab9d208e/ipados) |
| Capture vocals or rehearsal video | RØDE receiver → host via supported USB or the analog route described in its guide. Start with one receiver and two transmitters in split mode to capture one per channel. | Say “one” into the first mic and “two” into the second. Play the result back and verify the app preserved both channels. If using two kits, test the second separately before trying a four-mic setup. Try transmitter onboard WAVs and a clap for alignment when the capture app only sees one receiver. [RØDE Wireless PRO guide](https://rode.com/en-us/user-guides/wireless-pro) |
| Use iPhone/Pixel while practicing | Phone for quick recording, metronome, chart or Moises. Try the phone's built-in mic first, then repeat with the RØDE USB receiver. | Make a short recording in the actual app. Speaking near the transmitter with the handset farther away helps confirm which mic was recorded. Repeat after unplugging and reconnecting. [RØDE guide](https://rode.com/en-us/user-guides/wireless-pro) |
| Monitor and perform | Audio interface headphone monitoring during recording. iPad or phone for charts. Use a separate backing playback test and confirm routing into the performance setup. | Try chart and backing offline. Check count-in, routing, level and recovery after unplugging. Use a wired monitoring path for pitch and timing tests. |

When combining the Scarlett and RØDE, start with separate capture passes or the receiver's analog output routed to suitable line inputs with the correct breakout cable and output level. A split stereo output needs separate left/right channels, and a single balanced mono input is a different wiring scheme. Verify left/right, channel count and gain before committing to a recording.

For each test, record device/model, OS/app versions, cable and power, selected input, observed channels, and whether playback and monitoring worked. Carry the same WAV between the iPad, Mac and PC for comparison.
