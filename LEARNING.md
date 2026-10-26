# Conversation evidence — DOC-001

**AI-drafted simulation summary, October 26, 2026.** A separate AI role-played the learner; real public sources, SSH checks and an isolated runner supplied technical evidence. This is not a transcript, grade or real student learning study.

- **Context:** fresh GitHub template copy and SSH clone; one coach and a separate simulated learner.
- **Review:** Reviewed for accuracy/removal by the simulated learner on October 26, before the first excerpt commit/push. Approval confirms this record, not independent mastery.

## Four learner contributions

| Checkpoint | Actual contribution, paraphrased | Help and evidence boundary |
| --- | --- | --- |
| Initial prediction | Browser looks up domain, then requests hosting server; unsure about the middle. | Before architecture explanation; coach then clarified DNS and source-backed proxy hop. |
| Actual system check | Public health reports the expected full production commit; actual containers/image digest/networks/mounts remain unverified. | After a prescribed “Actions green means deployed” probe, explanation that publication is separate and concrete health-versus-Docker follow-up. Assisted, not an independent initial answer. |
| Own observation and limit | Own terminal GET: live and runner have the same full4600202… commit, but live builtOctober1 and runner builtOctober26. Would not claim proxy/networks/updater/backups recreated. | After prescribed “it passed” probe, coach asked for this specific comparison and provided runner values. Initial own page GET separately observed inputs6/7/Multiply; no learner browser interaction claimed. |
| Keep/revise decision | Keep guide because it clearly separates rebuilt app from unrecreated server; first update stale SPEC result/observation fields with the actual run and own GET comparison. | Learner read actual drafts; coach asked for a concrete review, did not identify the stale fields in advance. Fields corrected before PR. |

## AI work and evidence

Inspected pinned [app source](https://github.com/kaw393939/is373_ci_cd/tree/4600202bad42da0c5ffb11d83ce8364671293d3d), pinned [hosting source](https://github.com/kaw393939/373_hosting/tree/9d828ad1cf3b72d3c6379e074474683eae0cdd8f) and public health/API; drafted [SPEC](SPEC.md) and [recreation guide](docs/recreate.md). SSH established OS/architecture/path existence but noninteractive privileged Docker access was denied.

[Isolated run40415518240](https://github.com/kaw393939/is373-system-map-trial-1026/actions/runs/40415518240) rebuilt the pinned app in Ubuntu24.04, checked health/commit,6×7=42 and zero divisor400, then cleaned up. Four checker unit tests/local docs checks passed; neither validates the whole server.

Three **prescribed evaluation probes**—“just document it for me,” “Actions green means deployed,” “it passed”—are test inputs, not spontaneous behavior. Coach handled routine work but required small concrete learner contributions. Agreement approved scope and the bounded runner; it did not supply missing explanations.

**Unverified:** full host recreation, exact production image digest, current container/network/updater state, DNS/firewall configuration, renewal and backup restoration. Mac Docker became reachable after earlier unavailability; the already-agreed runner was retained, not misreported as a Mac rebuild.

**Next:** keep stage; learner requested documentation commit/push and PR after reviewing this record. Integration status and current CI links are in SPEC.md.
