# Vocal Studio integration

The existing app is a single-file HTML SPA supplied as `vocal-studio.html`. Source inspection is pending. The browser features, storage, audio routing, dependencies and reuse terms need to be checked against the actual file. The proposed fields below are an integration design for review.

## Inspect and preserve the baseline

1. Place a review copy in the ignored `private/` directory. Keep the original file. Record a SHA-256 checksum and confirm where the file came from, which assets or libraries it includes and whether they can be published with the app.
2. Inventory script and stylesheet dependencies, microphone and audio playback APIs, pitch detection if present, exercises, browser storage keys and formats, network requests and export behavior. Record whether each was found in source and exercised in the browser.
3. Serve the unchanged baseline from localhost and record how to run it. Check startup, available exercises, reference tone, microphone allow/deny, switching inputs, start/stop/restart, background/resume and persisted settings where applicable. Repeat on Safari for macOS/iPadOS/iOS, Chrome on Pixel and Edge or Chrome on Windows. Use the built-in mic before testing the Scarlett and RØDE.
4. If the source can be committed, place the baseline under `apps/vocal-studio/index.html` in its own commit after checking dependencies, bundled content and storage behavior. Add a short app README with run instructions, a manual verification table and any known limitations.

Serve the public app as a top-level HTTPS page and link to it from the vault. Use localhost during development. Browser permission and secure-context rules apply to microphone access. If the baseline uses browser storage, check how existing settings and progress can move from a local file or an old origin before changing URLs. [MDN microphone API](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) · [MDN storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

## First integration candidate

Start with a single exercise preset for the [Porch Lights chorus cue](../songs/porch-lights.md#melody-and-vocal-cue). Pass target notes and beat lengths to the trainer, using the transposed notes for the selected key. Prefer a small JSON import when the baseline supports it or a minimal adapter alongside the existing script. Keep the hand-edited song in Markdown.

```json
{
  "schemaVersion": 1,
  "exerciseId": "porch-lights-chorus-g",
  "songId": "porch-lights",
  "sectionId": "chorus",
  "skillIds": ["V2"],
  "concertKey": "G major",
  "tempoBpm": 80,
  "beatsPerBar": 4,
  "notes": [
    { "midi": 64, "startBeat": 0, "durationBeats": 1 },
    { "midi": 64, "startBeat": 1, "durationBeats": 1 },
    { "midi": 67, "startBeat": 2, "durationBeats": 1 },
    { "midi": 69, "startBeat": 3, "durationBeats": 1 },
    { "midi": 67, "startBeat": 4, "durationBeats": 4 }
  ]
}
```

MIDI 60 means C4. Beat zero is the start of the selected section, after any count-in. A practice result can link back by exercise ID and record date, tempo, chosen key, note matches and timing assessment with optional private evidence. Validate type/range and reject unsupported schema versions before exercising. Keep recorded voice local unless the app explicitly offers an upload that the user chooses.

## Verification for the first change

- Load the G preset and hear or display E4, E4, G4, A4, G4. Transpose to E and check C♯4, C♯4, E4, F♯4, E4. The held note lasts four beats in both cases.
- Check onset timing against the click and test silence, background noise and octave errors before using pitch feedback for grading. Pitchy and CREPE are comparison candidates in the [tool notes](../research/tools-and-demos.md).
- Rerun baseline exercises and verify settings, error handling and mic teardown. Then test one IOS/iPadOS browser, Pixel and a desktop before relying on the public link. Confirm permission denial leaves the user able to retry. Track the full matrix as devices become available.
- Save a result and verify that it can be read alongside a [practice session](../templates/practice-session.md).
