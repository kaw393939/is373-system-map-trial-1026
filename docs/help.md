# Help when you need it

The [README](../README.md) is the startup path. You do not need to read all this before beginning. Ask the same AI coach for one small explanation when stuck.

## Which project am I in?

Your **System Map clone** stores the documents and their issue/PR. Your **application repository** contains its code, tests and release workflows. Your **hosting repository or server directory** defines the host/proxy/routing arrangement. Your system may combine some of these. Check `pwd` and the Git remote before edits; never assume a file in this template changes the running application.

Give the application repository URL first. The coach will ask for the live URL and relevant hosting location when needed. If access is unavailable, record the exact gap and the next useful check rather than uploading a complete server dump.

## Evidence has a boundary

| Evidence | What it can establish | What it does not establish alone |
| --- | --- | --- |
| Compose/configuration or workflow source | Intended behavior at that inspected revision | Which revision is running |
| Successful CI checks | Those recorded checks passed on that commit | Image publication or remote deployment |
| Registry image/tag/digest | An image was available at the observation time | The server used that image |
| Dated running-release check | The observed service reported or ran that version | Every route, feature or future deployment works |
| Local recreation | The recorded behavior worked in that environment | Public DNS/TLS, complete host restore or deployment automation |
| Documentation checker | Its limited link/likely-secret rules passed | Factual accuracy, completeness or absence of all secrets |

Use small selected results and links, not copied raw logs. Do not paste `.env`, full container inspections, rendered secret-bearing configuration or certificate stores. A private input belongs in private configuration; the public guide names its purpose and how an authorized operator supplies it.

## Worked example: green Actions, old website

**Fictional example data—not a finding about your server.** Suppose a workflow passes for commit **A**, its publish job records image **A**, but the site's release endpoint still reports **B**.

The evidence supports “checks passed and A was published; the observed site is still B.” It does not support “deployment completed.” Inspect the configured deployment/updater path and its release selection read-only. Possible explanations include a paused updater or a different selected image, but neither is a fact until checked.

A useful guide correction would explain how to compare the intended release with the actual running identity and where to inspect a discrepancy. No production failure needs to be created. If the system lacks a version endpoint, inspect another supported identifier or record that verification gap; do not add an invented endpoint to the documentation.

## Testing efficiently

Positive/negative describe **cases**: an expected route responds; an unsupported route is handled as intended. Unit/integration/end-to-end describe **levels**: a small function, joined components, or a real user journey. They are different distinctions. Use the existing application's checks where relevant; do not reproduce every unit case through a browser or invent new app tests simply to fill a table.

For this documentation task, combine a few meaningful checks: source-to-document comparison, a dated live observation, and the agreed isolated recreation. Explain what each proves and what it leaves open. The supplied checker is instrumentation for document hygiene, not a server test suite.

## Course references

These explain the class examples; inspect your own system before treating them as its configuration.

- [Hosting: architecture, DNS, Docker, HTTPS and operations](https://github.com/kaw393939/373_hosting)
- [Hosting configuration walkthrough](https://github.com/kaw393939/373_hosting/blob/main/book/09-configuration-files.md)
- [Application delivery and public routing handoff](https://github.com/kaw393939/373_hosting/blob/main/book/10-application-delivery.md)
- [Application tests, image releases and updates](https://github.com/kaw393939/is373_ci_cd)
