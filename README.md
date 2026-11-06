# Brainstorming agent for Codex Cloud

A separate Codex main-chat agent using the original Brainstorming skill package.
It explores context and intent, asks focused questions, compares approaches,
writes a design for approval, and hands approved work to a planning skill.

Repository: https://github.com/alexyoung07/Brainstorm-Agent

## Start without uploading the ZIP again

Start a new Codex chat, choose **Work in > Cloud**, and select a published cloud
environment. Send:

```text
Use https://github.com/alexyoung07/Brainstorm-Agent as this chat's project.
Check out the repository if needed. Read AGENTS.md, START_HERE.md, and
DEPENDENCIES.md, verify the original package, then start Brainstorming in this
main conversation. Ask what idea, problem, or design I want to explore.
```

The host must be able to access this GitHub repository. To have it checked out
automatically in future cloud tasks, include it in the environment's setup and
publish or republish that setup. New cloud tasks get isolated workspaces.
Publishing files to GitHub does not itself change the cloud configuration.

## Included package

All eight original files are under `.agents/skills/brainstorming/`:

```text
SKILL.md
builder-check-prompt.md
visual-companion.md
scripts/
  frame-template.html
  helper.js
  server.cjs
  start-server.sh
  stop-server.sh
```

`brainstorming.zip` is the original uploaded archive. `AGENTS.md`, this README,
`START_HERE.md`, and `DEPENDENCIES.md` are separate integration documents.
No supplied skill content was rewritten. No optional interface metadata was
present in this archive.

## Handoff and visual companion

The required `superpowers:writing-plans` handoff skill is not bundled. The agent
checks the host's catalog and reports a missing dependency before handoff.

The optional visual companion requires separate acceptance and a compatible
Bash/Node and browser connection. Its cloud preview integration has not been
verified; text brainstorming remains available. See `DEPENDENCIES.md` for the
specific runtime constraints and what was checked.

## Verify preservation

Use your existing virtual environment's Python to run `verify_skill.py`. In a
fresh checkout, a minimal verification environment can be created with:

```bash
python3 -m venv .venv
.venv/bin/python verify_skill.py
```

The checker compares every installed file with its original ZIP entry and the
recorded SHA-256 digest. The original archive digest is:

```text
c6b40c553191f74aa7fcd8c0ac52edf762f46d0549aad9086716893858b3bcf8
```

`.gitattributes` preserves exact bytes during Git checkout. `.gitignore` excludes
the virtual environment and visual-companion runtime state. Keep future notes
and adaptations outside the preserved skill directory.
