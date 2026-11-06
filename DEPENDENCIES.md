# Runtime and handoff requirements

## Main conversation

Codex supplies the model, tools, and conversation. No separate Python application
or API key is required by this package. The skill can explore ideas, ask
questions, compare approaches, and write a design using the host's tools.

## Planning handoff

The supplied SKILL.md requires `superpowers:writing-plans` after the design is
approved. That skill is not present in this ZIP and was not found in the current
host's exposed skill catalog. This repository does not include an invented
replacement or claim to install the genuine dependency. A future host may
already provide it; the agent checks availability before handoff and reports a
missing dependency explicitly. Adding a companion skill can be a separate step
without modifying the preserved Brainstorming files.

## Optional visual companion

The included scripts use Bash, Unix command-line utilities, and Node.js built-in
modules. They contain no npm dependency manifest. The ZIP records no Unix
executable modes; invoke the .sh wrappers with Bash rather than relying on an
executable bit.

Using the companion needs a persistent server process and a browser-reachable
HTTP and WebSocket route. The supplied client uses ws:// and the server checks
an http:// origin. A typical HTTPS-only cloud preview is not confirmed compatible
and may require a separately implemented adapter. Binding to 0.0.0.0 alone does
not create a public preview URL. The agent must get the user's visual-companion
acceptance before starting it; text brainstorming works without that server.

Runtime session files under .superpowers/ can contain session keys and are
ignored by Git. The supplied server can suppress its external logo request with
SUPERPOWERS_DISABLE_TELEMETRY=1; source edits are not required.

The preparation checks are package-integrity and static syntax checks. No
visual server or cloud browser preview was launched during packaging.
