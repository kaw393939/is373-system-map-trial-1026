# Recreate the calculator: what was and was not reproduced

**October 26, 2026 — simulated learner trial.** The agreed app source rebuild ran successfully in an isolated Ubuntu24.04 GitHub runner. The whole server was **not** recreated. [SPEC.md](../SPEC.md) links architecture and open gaps.

## Target and inputs

The selected attempt rebuilds [application commit4600202…][app] using its reviewed Dockerfile. No registry login/push, Docker socket mount, Traefik, public hostname, production SSH, updater or private state is used. The runner binds one restricted container to `127.0.0.1:18090`, then runs cleanup for its own container/image; the runner is disposable.

The Mac's ordinary Docker setup was initially unavailable during instructor inspection. A later absolute-path check reached Docker server29.7.2. We retained the already-agreed runner target; this is not evidence that Docker remained stopped or that the Mac recreation was tested. Standard public GitHub Actions runner resources were used; no second paid VPS/domain was created.

## The executed app recreation

| Order / where | Action and expected result | Actual October 26 result |
| --- | --- | --- |
| 1. Documentation clone | Review [trial-only helper](../scripts/recreate_app.py) and [workflow](../.github/workflows/recreate.yml). Commit/push only these files after agreement. | Learner requested commit/push; `6aa0135` triggered the run. Conversation excerpts remained local. |
| 2. Disposable Ubuntu runner | Workflow checks out this repo and the public app at the exact full commit into ignored `.private/recreation-source`. No host SSH key is installed. | Exact source commit verified. This automated public read is separate from the student's SSH clone of the documentation template. |
| 3. Runner, app checkout | Helper builds the actual Dockerfile with `COMMIT_SHA` and a new `BUILT_AT`. | Image built; imageID `sha256:f124e7633c117fef019bc564a8b1664eeae91b57888c8c17009f70a0fe5e1f97`. New source build, **not** the byte-identical tested production artifact: distro update repositories/build time can differ. |
| 4. Runner loopback | Start unique container: UID/GID10001, read-only, all capabilities dropped, no-new-privileges, PID limit128, bounded temporary `/tmp`; bind18090→8000. Wait up to45s for health. | `/health`:200/statusok/production/full expected commit; new build time `2026-10-26T22:50:49Z`. |
| 5. Runner loopback | POST6×7 should return200/result42; POST6÷0 should return400/`division_by_zero`. | Both comparisons passed. These are two joined HTTP/app checks; not the application's complete unit or browser suite. |
| 6. Runner cleanup | Helper's `finally` removes only its unique container/image; GitHub disposes the runner. | Run completed successfully; cleanup commands executed. No live service was started/stopped; the entire runner was disposable. |

**Actual evidence:** [run40415518240](https://github.com/kaw393939/is373-system-map-trial-1026/actions/runs/40415518240), [helper revision6aa0135](https://github.com/kaw393939/is373-system-map-trial-1026/blob/6aa0135f6c9968eb0b7301f0bf3893b94a751c42/scripts/recreate_app.py). To repeat this trial in a separately agreed disposable target, use the workflow's manual run. Read the helper before execution; do not run production lifecycle commands as a shortcut.

## Full-server recreation plan — source-backed, unexecuted

**Stop at missing private inputs or access.** The current live host is not the target. A future owner-approved isolated host, private configuration and backup access are prerequisites; none was created for this trial.

| Order / where | Source-backed action / expected success | Current boundary |
| --- | --- | --- |
| 1. Owner's laptop/private records | Identify host architecture, actual image digest/release, proxy network, site names, DNS/firewall rules, private configuration and backup locations. Inspect current Docker fields through authorized access without raw dumps. | Ubuntu24.04.5/x86_64 and app-path existence observed; privileged Docker access denied. Inventory incomplete. |
| 2. Laptop → isolated host | Obtain [hosting source][hosting] and [app source][app] over existing SSH Git access; pin the recorded commits. Example: `git clone git@github.com:kaw393939/is373_ci_cd.git`, then `git checkout 4600202bad42da0c5ffb11d83ce8364671293d3d`. | Source read; no isolated full host provisioned. Existing app/hosting checkouts stay untouched. |
| 3. Isolated Ubuntu host | Review [Docker installation source][install] and supported class-host prerequisites. Supply Docker/Compose and compatible image platform. | No install/provisioning tested here. Don't assume Mac/runner setup proves a server installation. |
| 4. Isolated hosting checkout | Use [configuration lesson][configuration] and privately supplied host values to produce the proxy/welcome-site configuration. A generator example uses `hosting-web`; September class deployment used `web`. Restore or separately issue private certificate state with correct permissions. Start hosting before attaching the app. | Current generated config/certificate backup not available. Do not blindly substitute example domains, overwrite stores or create competing Apache routes for the calculator hostname. |
| 5. Isolated app checkout | Install [compose.traefik.yaml][adapter] as ignored `compose.override.yaml`; privately set `APP_HOST` and actual `TRAEFIK_NETWORK` in `.env`. Preserve `.state` release/pause/updater credentials and WUD volume when recovering. Validate quietly with `docker compose -f compose.yaml -f compose.override.yaml config --quiet`. | Private values/state not inspected. The adapter does not start another proxy. |
| 6. Isolated app host | After reviewing [Make/runtime][runtime], select a known-good compatible published release; use `make deploy` and `make verify-production` with authorized Docker access. Expect actual container imageID and loopback health to match selected release. | Not run; do not execute on production for this assignment. Pulling the existing published image is different from this trial's source rebuild. |
| 7. Separate client + DNS provider | In a separately approved test hostname/environment, confirm records/firewall80/443, trusted certificate and HTTP→HTTPS; run [release verifier][verifier] with the expected published commit, then a real browser calculation. | No DNS changes, certificate issuance or public routing recreation performed. Existing public HTTPS checks only describe today's original site. |
| 8. GitHub → registry → isolated host | Recreate the documented repository settings/registry secret privately. [Workflow][workflow] verifies native images; only successful current-main push publishes. Inspect WUD selection/pause/configuration and compare running release after an intentionally agreed test update. | No publication, updater exercise, rollback/resume or new app change performed. A green run alone is insufficient. |

## Recovery, findings and limits

Before claiming recovery, an authorized owner must privately back up/restore hosting site/configuration/certificate state, app override/`.env`/`.state`, WUD data, and the selected compatible release. A source checkout cannot reconstruct missing private state. Test restoration into an isolated target and verify release identity plus relevant routes; never restore over production or delete existing volumes.

**Environment adjustment:** the initial Docker limitation led to an explicitly agreed Ubuntu runner target. The guide names its pinned checkout, loopback port, checks and cleanup instead of implying an unspecified local build. Later Docker reachability is recorded rather than hidden; this was an environment decision, not a learner-discovered wording defect.

The rebuilt app verifies only its recorded identity and two API behaviors in that runner. It does not establish identical production bytes, the public proxy/network, certificate renewal, host restart, backup restoration, live automatic delivery or rollback. Learner observation/interpretation is recorded separately in [LEARNING.md](../LEARNING.md).

[app]: https://github.com/kaw393939/is373_ci_cd/tree/4600202bad42da0c5ffb11d83ce8364671293d3d
[hosting]: https://github.com/kaw393939/373_hosting/tree/9d828ad1cf3b72d3c6379e074474683eae0cdd8f
[install]: https://github.com/kaw393939/373_hosting/blob/9d828ad1cf3b72d3c6379e074474683eae0cdd8f/scripts/install-docker.sh
[configuration]: https://github.com/kaw393939/373_hosting/blob/9d828ad1cf3b72d3c6379e074474683eae0cdd8f/book/09-configuration-files.md
[adapter]: https://github.com/kaw393939/373_hosting/blob/9d828ad1cf3b72d3c6379e074474683eae0cdd8f/examples/integrations/calculator/compose.traefik.yaml
[runtime]: https://github.com/kaw393939/is373_ci_cd/blob/4600202bad42da0c5ffb11d83ce8364671293d3d/scripts/runtime.py
[workflow]: https://github.com/kaw393939/is373_ci_cd/blob/4600202bad42da0c5ffb11d83ce8364671293d3d/.github/workflows/ci.yml
[verifier]: https://github.com/kaw393939/373_hosting/blob/9d828ad1cf3b72d3c6379e074474683eae0cdd8f/scripts/verify-release.py
