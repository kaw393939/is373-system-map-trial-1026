# IS373 System Map

**Could you recreate the system you already built—and explain how a code change reaches it?** Work with an AI coach to turn your existing website, server configuration and CI/CD process into a concise, evidence-based specification and recreation guide.

This is a documentation project. Your application and hosting stay in their existing repositories. You are not buying another VPS, replacing your working server, or building a new application.

**A short, visible record:** the coach maintains [LEARNING.md](LEARNING.md) using your actual explanations, observations and help received. It is AI-drafted, not a transcript or grade, and may be public. Review, correct or remove excerpts before they are committed or pushed. Your instructor uses the project and this [simple rubric](docs/assessment.md) together.

## Start here

1. On [this template](https://github.com/kaw393939/is373-system-map), choose **Use this template → Create a new repository** in your own account. Name it `my-system-map`, choose **Public**, and wait until your new repository shows its README/files. A template copy does not copy the instructor's issues.
2. Use your existing class terminal and SSH setup. Replace `YOUR-USERNAME`; replace `my-system-map` too if you chose a different name. Run one command at a time and stop if it fails.

   ```sh
   git clone git@github.com:YOUR-USERNAME/my-system-map.git
   cd my-system-map
   pwd
   git remote -v
   ```

3. Open this cloned folder as a **local project** in ChatGPT desktop/Codex, or another AI agent that can read/edit local files and run terminal commands. Browser control helps with review but is insufficient alone. VS Code is optional; no extra agent CLI or editor extension is required. Start one chat:

   > Read README.md, AGENTS.md and SPEC.md. Guide me through documenting my existing system one small step at a time. Confirm this folder and my SSH remote first. Ask for my existing application repository, then help me inspect the live system. Do not change my server or fill gaps with guesses.

4. Let the agent confirm the folder and SSH remote identify **your documentation copy**, check that `python3` is available, and run:

   ```sh
   python3 scripts/check_docs.py
   python3 -m unittest discover -s tests -v
   ```

   No dependency installation or new application server is required for this template. If Python is unavailable, ask the agent for help with your existing class environment before continuing.

**First checkpoint:** your agent can read the clone without uploads, the prepared checks pass, and you understand that they check documentation hygiene—not whether your system description is true or complete. The agent asks for your existing application repository URL first, then your public website URL. It will help locate hosting configuration when needed. You do not need to collect everything before starting.

Use the same chat throughout. It will inspect relevant source/configuration and the live site with you, asking one meaningful question at a time. Keep passwords, tokens, private keys, certificate stores and raw environment output out of the chat and repository. Help with missing access is part of the exercise; never replace missing evidence with a plausible story.

## Try → Decide → Build → Check → Keep

1. **Try your existing system.** Open the live site and describe one thing you actually observe. Before explaining the architecture, the coach asks you to predict how that request reaches your application. A short guess is useful; you can ask for a hint.
2. **Decide what to investigate.** Agree on `DOC-001`: the request path, running components and state, and the path from a code change to the running release. Create its issue and a documentation branch in **this repository** before saving findings. The agent can draft the issue; review it before posting.
3. **Build the map from evidence.** Fill [SPEC.md](SPEC.md) one section at a time, linking the actual configuration, workflow and observations. Then fill [docs/recreate.md](docs/recreate.md) with ordered steps, where to run each one, and what success should look like. Keep source configuration separate from what is verified on the running server. “Not configured” and “Not yet verified” are useful findings.
4. **Check before you keep.** The agent reviews the documents against the evidence and runs the prepared checks first. It shows one actual system check and asks what it establishes. Then agree on a small, isolated recreation attempt using your real stack. Follow the guide, inspect the result yourself, and describe a missing step, discrepancy or verification limit. Improve the documents and repeat the relevant check.
5. **Keep a version you can explain.** Review the short LEARNING.md record for accuracy before its excerpts are committed or pushed. Review the documentation diff, commit and push the branch, and open a PR linking `Closes #N` to your issue. Save the actual PR and CI run URLs in SPEC.md, push that record update, and wait for checks on the latest commit. Explain whether to revise or keep it, then merge when you are ready.

**Done means the claim matches the evidence.** The PR is merged, its issue is closed, and the documents link the system's features to their configuration and actual checks. State what was recreated and what remains unverified. Starting the application locally does not prove public DNS, HTTPS, server recovery or automatic deployment. A green workflow does not prove the remote server updated. A blocked step stays a documented gap; it is not a completed rebuild.

Initial investigation is read-only. Never introduce a fault into production, stop existing services, change DNS, deploy, roll back, or restore over live data for this exercise. The coach will propose an isolated recreation plan and explain its boundaries before executing it. No second paid server or domain is required.

## What is here

| File | Purpose |
| --- | --- |
| [SPEC.md](SPEC.md) | Your system map, features, evidence and open gaps |
| [docs/recreate.md](docs/recreate.md) | Ordered recreation and recovery instructions |
| [AGENTS.md](AGENTS.md) | Conversational coaching and evidence rules |
| [LEARNING.md](LEARNING.md) | Short, reviewable record of your contributions and help |
| [docs/help.md](docs/help.md) | Examples, evidence limits and course references |

`python3 scripts/check_docs.py` checks local Markdown links and a small set of likely secret patterns. It is not a comprehensive secret scanner, architecture reviewer, live-system test, or completion detector. The unit tests check that tool's behavior; passing them does not validate your server. Review every file before sharing.

**Returning later:** reopen the same clone and chat. Ask the agent to read SPEC.md and LEARNING.md and resume the recorded next step. Do not normally clone again. This template needs no live-reload server; preview its ordinary Markdown locally or on GitHub.

**Next, with less guidance:** choose one useful improvement exposed by your investigation—perhaps clearer recovery instructions or a missing release-identity check. Write a small request and expected evidence, then use a new issue and PR. Do not implement it as part of DOC-001.
