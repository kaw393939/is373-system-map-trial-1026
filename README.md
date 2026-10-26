# Completed IS373 System Map simulation

**New students: start with the unfinished [IS373 System Map template](https://github.com/kaw393939/is373-system-map).** This separate repository contains a completed simulated learner example using the instructor's existing calculator system.

- [System specification](SPEC.md): request path, components/state and CI/CD handoff, with source/runtime evidence kept distinct.
- [Recreation guide](docs/recreate.md): an actual isolated app rebuild plus untested full-host steps and gaps.
- [Learning record](LEARNING.md): short, accuracy-reviewed contributions and help; AI role-play, not real student learning evidence.
- [DOC-001 issue](https://github.com/kaw393939/is373-system-map-trial-1026/issues/1).
- [Actual isolated recreation run](https://github.com/kaw393939/is373-system-map-trial-1026/actions/runs/40415518240).

The Ubuntu runner built pinned public source, ran a restricted container only on loopback, verified release identity and two API cases, then removed its resources. It neither changed production nor recreated the public host, certificates, updater or backups.

This is an ordinary Markdown documentation project; it needs no application server or live reload. Prepared hygiene checks:

```sh
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

They check local document links, selected likely secrets and the checker's behavior. Passing does not establish factual accuracy, complete secret protection or server recovery. Trial-specific helper/workflow files belong to this completed example; they are not required additions to every student's project.

[Instructor trial notes](docs/instructor-trial.md) distinguish prescribed evaluation probes, actual checks, remaining gaps and instruction improvements.
