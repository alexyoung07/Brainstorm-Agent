# Brainstorming project

This repository is a dedicated Codex project for direct conversations with a
Brainstorming agent. Use this checked-out repository as the project directory.

Read `.agents/skills/brainstorming/SKILL.md` in full before conducting a
brainstorming or design task, and follow it in the main conversation. Its
supporting files, scripts, and relative directory layout are preserved.

Follow the supplied skill's questions, approach selection, design documentation,
builder review, and design-approval boundary. Respect the explicit opt-out and
authorized spike exceptions described in that skill. User instructions and
higher-priority host instructions take precedence over reference material.

If the user has not supplied an idea or problem, ask what they want to explore.
Research facts with the available host tools and delegate builder review as the
skill specifies; use its own stated fallback when subagents are unavailable.

## Required planning handoff

The bundled skill references `superpowers:writing-plans`, which is not included
in the uploaded ZIP or this repository. Check the actual host's skill catalog
before the handoff. After design approval, invoke that genuine skill if it is
available. If it is unavailable, report the missing dependency and ask the user
how to proceed. Do not claim it was invoked or silently substitute another
workflow. See `DEPENDENCIES.md`.

## Optional visual companion

Offer and obtain the user's acceptance when the supplied skill calls for it.
Then read `.agents/skills/brainstorming/visual-companion.md` before using it.
Check Bash/Node availability, persistent-process support, and a browser-reachable
HTTP/WebSocket route. Cloud HTTPS preview integration has not been verified.
Use text sketches when that optional facility is unavailable. Any integration
adapter requires a separate user request and separate files.

The source archive records no Unix executable bits. Invoke the supplied shell
wrappers with `bash`; their bytes remain unchanged. Keep session keys, runtime
logs, PID files, and `.superpowers/` state out of Git.

## Preservation and scope

Keep `brainstorming.zip` and all eight files under
`.agents/skills/brainstorming/` unchanged. Place project-specific notes and
integration instructions in separate files. Keep external write actions within
the user's authorized GitHub scope unless the user explicitly expands it.

A new cloud task has its own workspace. Read this repository in that task
rather than assuming another conversation's local files are present.
