# System Design — interactive local course

A fully local copy of the interactive System Design course, with all 40 lessons, original lesson scenes, step-by-step explanations, course navigation, search, keyboard controls, theme and language selection, and saved progress.

## Run locally

Requirements: Node.js 18 or newer and npm.

```bash
npm install
npm run dev
```

Open the URL printed by the server (by default, `http://127.0.0.1:5173`). The app and its assets are served from this folder; it does not call the reference site or require an API.

## Deploy to Vercel

The project is configured as a static Vercel deployment. From the project root, run:

```bash
npm run build
```

The build writes the deployable site to `dist/`. `vercel.json` selects the **Other** framework preset, runs this build command, and publishes `dist`; no API keys or environment variables are required. In Vercel, set the project root to this folder if the repository contains additional folders.

## Course controls

- Select a lesson in the course sidebar or use search (`Ctrl+K`).
- Use the lesson timeline, Back/Next, or the arrow keys to move between stages.
- The original Play/Pause controls diagram traffic. Added **Play lesson** advances through the lesson’s actual stages, and **Replay lesson** resets the full lesson to stage one.
- The original course stores completed lessons and the last location in local storage. Open the course progress panel and choose **Reset progress** to clear completed lessons and the saved course position.
- Theme and language choices are available in the course header. Translation chunks and fonts are bundled locally.

## Source and preservation

`source-captures/` contains the 41 supplied HTML captures unchanged. They represent 40 unique lessons; the extra file is a duplicate “How a Request Travels” capture. Each capture preserves the original rendered course shell, initial diagram, embedded SVG, lesson copy, and timeline labels. The captures themselves are static snapshots: their original runtime JavaScript was omitted by the SingleFile export.

The local app uses the matching original public runtime and stylesheet from the reference site, along with its translation chunks and web fonts, stored under `assets/`. This restores the full lesson registry, all stage content and scene data, and the original interaction/animation behavior without making runtime requests to the reference website. `lesson-registry.json` inventories all 40 unique lessons in their original module order and records the capture and stage-label sources.

The reference identifies Dilum Sanjaya as the course author. The bundled implementation and lesson content are included here solely to fulfill this local reproduction request. See the source captures for original attribution and metadata.
