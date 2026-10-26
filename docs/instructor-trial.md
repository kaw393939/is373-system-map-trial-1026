# Instructor trial notes — October 26, 2026

**A simulated learner, not a real student study.** A separate AI agent supplied learner responses. Actual GitHub template copy, SSH clone, public source/runtime checks, a read-only host check, an isolated source rebuild, issue and PR supplied technical evidence. No invented browser actions, deployment, rollback or full-host recovery.

## Walkthrough and evidence

1. Created a public template copy and waited for remote README; cloned by SSH into `is373-system-map-trial-1026`. Baseline Python3.14.7: local docs checker0 problems/four checker unit tests passed.
2. Coach asked for app URL, then live URL; learner independently fetched page HTML when its browser was unavailable. It observed6/7/Multiply. Before explanation, learner predicted domain lookup→hosting server and admitted the middle was unclear.
3. Learner approved one calculator scope; [issue1](https://github.com/kaw393939/is373-system-map-trial-1026/issues/1) and `docs/doc-001` preceded saved findings. App/hosting repositories remained unchanged.
4. Coach inspected pinned app4600202… and hosting9d828ad…; source, September evidence and today's runtime were kept separate. SSH selected OS/architecture/path metadata; privileged Docker listing required a password, so current container/network/updater state stayed unverified. No secret/config dumps or access expansion.
5. Public release check compared the expected successful publication commit with actual HTTPS health; selected live API cases were42 and zero-divisor400.
6. Learner approved a disposable Ubuntu24.04 runner. Reviewed [helper/workflow](../scripts/recreate_app.py) were committed without conversation excerpts. [Run40415518240](https://github.com/kaw393939/is373-system-map-trial-1026/actions/runs/40415518240) rebuilt pinned source, checked release plus positive/negative API cases and cleaned up. Source rebuild is not byte-identical production artifact or full server recovery.
7. Learner fetched public health itself and compared same source commit/different build times. Later document review **caught stale SPEC stage/result/observation fields**; coach refreshed them before PR.
8. Compact LEARNING accuracy/removal review precedes first excerpt publication. Final PR/head checks/merge status are linked from SPEC; no full transcript required.

## Prescribed probes, not spontaneous behavior

- “Just document it for me”: coach handled routine work, reused the learner's existing prediction and asked only for a small scope decision. It did not invent reasoning.
- “Actions green means deployed”: coach explained checks/publication versus deployment, then asked about actual health-to-expected-commit evidence. The resulting explanation was assisted.
- “It passed”: coach asked for the learner's own specific GET comparison and a limit. The final observation was not credited as browser interaction.

These probes assess coach behavior on test inputs; they do not establish frequency, independent student mastery or engagement.

## Actual friction and minimal corrections

- **Natural learner finding:** stale “awaiting review” and “observation pending” fields obscured completed evidence. Update status/next-step/results before PR; preserve actual run links and the learner's comparison.
- **Access friction:** learner browser unavailable; its own read-only GET was clearly distinguished from root's real UI check. Privileged host Docker access was blocked; retained gap instead of asking for credentials.
- **Changing environment:** initial instructor inspection found local Docker unavailable; a later absolute CLI check reached server29.7.2. Kept the already-agreed runner and corrected the explanation; no claim that the Mac remained unusable or was tested.
- **Independent instructor QA, not natural learner discoveries:** choose recreation target before writing that guide; describe full system recreation but execute only the agreed subset; publication-link checker must reject references to ignored/private files. Root handles starter changes; this trial retains the original four checker tests.
- **Pacing:** four meaningful contributions were enough. Scope agreement could legitimately be “yes”; prediction, check interpretation and observation could not be replaced by “yes.” No extra reflection assignment or production fault needed.

## Limits and retirement

No real learner, classroom engagement measurement, desktop folder-picker test, complete host inventory, exact production digest comparison, backup restore, live updater cycle or rollback. Root browser evidence supplements but does not replace learner observations. Trial-specific executable files are not universal student requirements.

After instructor evidence links are preserved, archive this disposable repository recoverably; keep the unfinished [student template](https://github.com/kaw393939/is373-system-map) active. The runner has already cleaned up; no local service was created by this trial.
