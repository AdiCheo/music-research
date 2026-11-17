# Contributing to the music vault

Read [Music workspace](index.md) and the relevant workflow before editing. Keep authored notes in plain Markdown with relative links. Use lowercase hyphenated filenames. Add a link from an existing index when you add a page.

- **Research** — record the official source, a demo or reproducible test where available, intended device or OS, input and output formats, cloud versus local processing, and verification status. Record an exact version and model when a test is actually run. Distinguish source-verified, installed and tested.
- **Songs** — use the [song template](templates/song.md). Identify the exact recording, distinguish sounding chords from capo shapes, and label machine estimates until checked against the audio. Keep source audio, stems, recordings, full imported lyrics and private charts outside the published vault unless cleared for redistribution.
- **Skills** — use stable IDs from the [skill tree](learning/skill-tree.md). Each new item needs prerequisites, a lesson, a song or exercise, a measurable pass check and a way to capture evidence.
- **App work** — start with the [vocal app integration brief](projects/vocal-training.md). Verify the existing app and record its source, license, build commands and data formats before changing or copying it.
- **Git** — commit coherent changes as they become reviewable. Check staged files for private media, generated output, secrets and rights metadata. Check relative links with `python3 scripts/check-links.py` and run `git diff --check` before committing.

Keep the public navigation in [index.md](index.md). Track personal progress using the [practice template](templates/practice-session.md) in a private location.
