# Git Literacy for Product Managers Using Claude Code

## Hybrid PRD / Lesson Plan

-----

## Part 1: Product Requirements

### Problem Statement

Product managers joining our Claude Code pilot need a working mental model of Git and GitHub to pair effectively with the tool. Most have never used Git. They don’t need to memorize commands — Claude Code will execute operations on their behalf — but they *do* need to understand what’s happening, why it matters, and how to recognize when something has gone wrong.

No existing training resource operates at this altitude. Available materials either teach Git commands to developers, or explain GitHub’s web UI without connecting concepts to AI-assisted workflows. We need something purpose-built.

### Target Learner

- Product manager at Capital One
- Comfortable with Google Drive (Docs, Sheets, shared folders, comment/suggestion workflows)
- Lives almost entirely in the cloud — may have no files stored locally on their laptop
- Is accustomed to real-time synchronous collaboration in a single shared document
- Has heard terms like “repo” or “PR” in passing but cannot define them precisely
- Has VS Code installed and Claude Code extension configured
- Has a GitHub Enterprise Cloud account with SSO already working
- Does *not* need to become a Git power user — needs to be a competent *collaborator* and *delegator*

### Learning Goals

After completing this training (~20 minutes, self-paced), the learner can:

1. **Explain the difference between local and remote** — why work happens on your laptop first and then gets shared to the cloud, and how this differs from the Google Drive model they’re used to
1. **Articulate the tradeoffs** — what you give up moving from cloud-native collaboration tools to a Git-based workflow, and what you gain (especially in the context of AI-assisted development)
1. **Explain** what a repository is and find their team’s repos on GitHub.com
1. **Describe** what a commit represents and why commit messages matter
1. **Explain** why work happens on branches instead of directly on `main`
1. **Describe** the purpose of a pull request and who is involved
1. **Prompt** Claude Code to perform common Git operations and understand what it’s doing
1. **Navigate a multi-repo workspace** in VS Code and understand that Claude Code can traverse across repos when given permission
1. **Recognize** when Git is in an error state (merge conflict, detached HEAD, uncommitted changes blocking an operation) and describe the situation clearly enough to get help
1. **Understand** what types of files thrive in GitHub and which don’t — and why that’s okay

### Non-Goals

- Teaching Git command-line syntax
- Covering advanced workflows (rebasing, cherry-picking, squashing, Git internals)
- Teaching GitHub Actions, CI/CD, or DevOps concepts
- Replacing engineer support for complex merge conflicts
- Requiring PMs to abandon Google Drive, Confluence, or other tools for non-code work

### Delivery Format

Self-guided markdown document (convertible to internal wiki, Google Doc, or LMS module). Each section includes a mental model, a “What you’d say to Claude Code” example, a “What happens behind the curtain” explanation, and a quick comprehension check.

-----

## Part 2: Lesson Plan

### How to Use This Training

Read each module in order. The whole thing should take about 20 minutes. Each module follows the same pattern:

- **The concept** — what it is, explained through something you already know
- **What you’d say to Claude Code** — the natural-language prompt you’d actually type
- **What happens behind the curtain** — what Claude Code does on your behalf
- **Check yourself** — a quick question to confirm the concept landed

You don’t need to have VS Code open right now. This is a *reading* exercise that builds the mental model you’ll use when you sit down to work.

-----

### Module 1: Your Work Lives on Your Laptop Now (4 minutes)

#### The concept

This is the single biggest shift in how you’ll work, so we’re starting here.

Right now, almost everything you do lives in the cloud. Your Google Docs, your Sheets, your Slides, your Confluence pages — they exist on a server somewhere and you access them through a browser. If your laptop caught fire, you’d lose nothing. You could log into a new machine and pick up exactly where you left off. Multiple people can edit the same document simultaneously, and everyone sees each other’s cursor in real time.

**That is not how code works.**

When you work with Claude Code, your work lives in files *on your laptop*. Real files in real folders, just like the old days of saving Word documents to your hard drive. This is called working **locally**. The “cloud” equivalent — where the team’s shared, official copy lives — is GitHub.com. That’s called the **remote**.

Here’s the critical mental model:

**Google Drive model:** One copy in the cloud. Everyone connects to it. Changes appear instantly for everyone.

**Git model:** Many copies. Everyone has their own copy on their own laptop. You work on your copy privately. When you’re ready, you deliberately *push* your changes up to the shared copy on GitHub.com. Your teammates *pull* changes down when they want to see what’s new.

#### What you’re giving up

Let’s be honest about this, because it’s real:

- **No real-time co-editing.** You can’t watch someone’s cursor move through code the way you can in Google Docs. Two people can work on the same project simultaneously, but they do it on their own copies and reconcile later.
- **Sync is manual, not automatic.** Changes don’t appear for your teammates until you push. Their changes don’t appear for you until you pull. You’ll need to develop a habit of pushing and pulling regularly.
- **Your laptop matters.** If you make changes locally and don’t push them, they exist only on your machine. (Claude Code will remind you to push, and we’ll talk about this more in the commits module.)
- **It’s more steps.** Editing a Google Doc is: open it, type, done. The Git workflow is: pull the latest, create a branch, make changes, commit, push, open a pull request. Claude Code handles most of these steps for you, but you need to understand the rhythm.

#### What you’re gaining

And the gains are substantial — especially right now, as AI-assisted development reshapes how products get built:

- **Every coding agent speaks Git and GitHub natively.** Claude Code, GitHub Copilot, Cursor, Windsurf — all of them are built around Git workflows. When your work lives in GitHub, these agents can see it, understand it, and help you with it. Anything you bring into a GitHub repo becomes *context your AI collaborator can draw on*. A PRD in a repo isn’t just a document — it’s something Claude Code can reference while building the feature that PRD describes.
- **Precision control over contributions.** Instead of tracking who edited what paragraph in a Google Doc, Git records the exact changes each person (or agent) made, at the line level, with full history. You can review what Claude Code did, approve it, or roll it back — at any level of granularity.
- **You get closer to the product itself.** The code in GitHub *is* the product. By working in the same environment your engineers work in, you’re not reading about what was built in a ticket — you’re looking at it. You can browse the actual files, read the commit messages, and see the pull request discussions that shaped each feature.
- **Safe experimentation is free.** Because everyone works on their own copy, you can try things, break things, and start over without affecting anyone else. In Google Docs, destructive experiments are terrifying. In Git, they’re routine.
- **Every insight and asset you bring into GitHub becomes easier for your coding agents to use** as rich context when they help you understand customer needs, define products, execute your intent, and test its execution.

**The bottom line:** You’re trading the effortlessness of real-time cloud editing for a workflow that gives you version control, safe parallelism, structured review, and — critically — a shared workspace with the most powerful AI coding agents available today. The extra steps are real, but Claude Code absorbs most of them.

> **Check yourself:** You make changes to code on your laptop using Claude Code and then close your laptop for the day. Can your teammate see those changes on GitHub.com? *(Answer: Not unless you pushed them. Your changes are local until you explicitly share them.)* Why would anyone choose this model over Google Docs? *(Answer: Because it gives you safe parallel work, precise version history, structured review — and because AI coding agents are built around Git, so it’s the only way to fully collaborate with them.)*

-----

### Module 2: Repositories — Your Project’s Home (2 minutes)

#### The concept

A **repository** (usually just called a “repo”) is a project folder that remembers everything. It contains all the files for a project *plus* the complete history of every change ever made to those files.

**Google Drive analogy:** Think of a shared Drive folder for a project — it has subfolders, documents, spreadsheets. A repo is like that, but it also contains an invisible, perfect memory of every version of every file. You can’t accidentally “lose” something in a repo the way you can in Drive, because the history is always there.

Now that you understand local vs. remote, here’s how repos work in practice:

|               |Where it lives                      |How you interact with it                                                                        |
|---------------|------------------------------------|------------------------------------------------------------------------------------------------|
|**Remote repo**|GitHub.com (our Enterprise instance)|You browse it in your web browser. This is the shared, official copy.                           |
|**Local repo** |Your laptop, inside a folder        |Claude Code works here. When you open a project in VS Code, you’re working with your local copy.|

The first time you work on a project, you **clone** it — which means downloading the full repo (all files + all history) from GitHub.com to your laptop. After that, you push and pull to keep the two copies in sync.

#### Where to find your team’s repos

1. Go to GitHub.com and sign in with SSO
1. Your team’s repos will be under your organization — click the org name in the left sidebar
1. Use the search bar to filter by project name. Repos are named in lowercase with hyphens: `card-servicing-api`, `chat-experience-frontend`, etc.

#### What you’d say to Claude Code

> “Clone the card-servicing-api repo so I can work on it locally”

#### What happens behind the curtain

Claude Code runs `git clone <url>`, which downloads the entire repo from GitHub.com to a folder on your laptop. VS Code then opens that folder. You only do this once per repo — after that, the local copy persists on your machine.

> **Check yourself:** Someone says “check the repo.” Where do you go? *(Answer: GitHub.com, to look at the remote copy.)* Someone says “I cloned the repo.” What did they do? *(Answer: Downloaded a copy of the project from GitHub.com to their laptop so they can work on it locally.)*

-----

### Module 3: Commits — Deliberate Save Points (3 minutes)

#### The concept

A **commit** is a deliberate save point. It captures the state of every file in the repo at one moment in time, paired with a short description of what changed and why.

**Google Drive analogy:** In Google Docs, version history auto-saves constantly with timestamps. Commits are like *manually creating a named version*. Instead of “March 14, 3:42 PM,” you get “Add error message when user enters expired card.”

**Why deliberate saves?** This connects directly to Module 1. Because Git doesn’t auto-save to the cloud, *you* decide when a set of changes is worth recording. This feels like a burden at first, but it’s actually a powerful form of storytelling. A commit history that reads like a story — “Add validation for card expiration,” “Update error message copy,” “Fix edge case for leap year dates” — is dramatically easier to debug than one that reads “misc changes,” “WIP,” “fixed stuff.”

**Remember:** A commit saves to your *local* repo. It is not visible to anyone else until you *push* it to the remote on GitHub.com. Think of it as writing in a notebook that you haven’t shared yet. Commit often, push when you’re ready to share.

When you work with Claude Code, *you are the author of these commits*. Your name is on them. Claude Code will suggest a commit message, and you should review or edit it to make sure it clearly describes what changed.

#### What you’d say to Claude Code

> “Commit what we have so far — we’ve finished the header and navigation translations”

Or more specifically:

> “Commit with the message ‘Add Spanish language support to welcome screen’”

#### What happens behind the curtain

Claude Code does two things:

1. **Stages the changes** (`git add`) — selects which file changes to include in this save point
1. **Creates the commit** (`git commit -m "Add Spanish language support to welcome screen"`) — records the save point with your message

The commit now exists locally. It is not on GitHub.com yet — that happens when you *push*.

#### What a commit looks like on GitHub.com

Once pushed, you can view any commit on GitHub.com and see:

- **The author** (your name)
- **The date**
- **The message** you wrote
- **A diff** — a line-by-line view showing what was added (highlighted green) and removed (highlighted red)

This diff view is what engineers and reviewers use to understand your change. Worth clicking around on to get comfortable.

> **Check yourself:** You ask Claude Code to make a change and it does. Is that change saved to Git’s history? *(Answer: No. The files on your laptop are modified, but it’s not a commit until you explicitly tell Claude Code to commit.)* After you commit, can your teammate see the change on GitHub.com? *(Answer: Not yet — you also need to push.)*

-----

### Module 4: Branches — Parallel Universes for Safe Experimentation (3 minutes)

#### The concept

A **branch** is a parallel copy of the project where you can make changes without affecting anyone else’s work.

**Google Drive analogy:** Imagine you wanted to experiment with a totally different structure for a PRD, but you didn’t want to mess up the current version. In Google Docs, you might “Make a copy” and work on it separately. A branch is exactly that — but for the *entire project* (all files at once), and with a built-in mechanism to merge your changes back when you’re done.

**The key branch: `main`.** Every repo has a primary branch, almost always called `main`. This is the “official” version. **Nobody works directly on `main`.** Instead:

1. You create a new branch off of `main` (your parallel universe)
1. You make changes and commit them on that branch
1. When ready, you propose merging your branch back into `main` via a pull request (next module)
1. After review and approval, your branch is merged

**Why branches instead of working directly on `main`?** Same reason you wouldn’t edit a live document that stakeholders are reading while you’re mid-draft. Branches give you a private workspace. And because this is Git (everyone has their own local copy), your branch is doubly safe — it’s on *your* machine, on *your* branch, until you push it.

**Branch naming:** Short, descriptive, hyphenated: `add-spanish-translations`, `fix-expired-card-error`, `update-welcome-copy`. Claude Code will suggest a name based on your work.

#### What you’d say to Claude Code

> “Create a new branch for the work we’re about to do on Spanish translations”

> “Switch to the add-spanish-translations branch”

> “Pull the latest from main and create a new branch called update-faq-content”

#### What happens behind the curtain

**Creating a branch:** Claude Code runs `git checkout -b add-spanish-translations`. This creates a new branch starting from wherever you are (usually `main`) and switches you to it. Commits now go to *this branch only*.

**Switching branches:** Claude Code runs `git checkout <branch-name>`. The files in VS Code change to reflect that branch’s state. Files might appear or disappear — this is normal, not data loss.

**Pulling latest:** Claude Code runs `git pull origin main` to download new commits from GitHub.com before you start working.

#### How to see which branch you’re on

In VS Code, look at the **bottom-left corner**. You’ll see a branch icon followed by the branch name. You can click it to switch branches via the GUI.

> **Check yourself:** Your teammate says “I pushed to my branch.” Does that mean their changes are on `main`? *(Answer: No. They’re on their branch on GitHub.com. They need a pull request to get those changes into `main`.)* You’re on branch `fix-login-bug` and a file looks different than expected. Is something wrong? *(Answer: Probably not — files reflect whichever branch you’re on. Check if you need to switch branches.)*

-----

### Module 5: Pull Requests — Proposing Your Changes for Review (3 minutes)

#### The concept

A **pull request** (PR) is a formal proposal: “I’ve made changes on my branch. Here they are. Please review them and, if they look good, merge them into `main`.”

**Google Drive analogy:** A PR is like switching a Google Doc to “Suggesting” mode and tagging reviewers. They see exactly what you changed, leave comments, request revisions, or approve. The key difference: your changes don’t touch the original until someone explicitly approves and merges.

**The lifecycle of a pull request:**

1. **You create it.** Your branch has commits. You open a PR on GitHub.com proposing a merge into `main`. It includes a title, description, and the diff of all changes.
1. **Reviewers examine it.** They see every line added (green) and removed (red). They can comment on specific lines, leave general feedback, or give a formal decision: Approve or Request Changes.
1. **You revise if needed.** Make more changes in VS Code with Claude Code, commit, and push. The PR updates automatically.
1. **Someone merges it.** After approval, someone clicks “Merge pull request” on GitHub.com. Your changes are now part of `main`.
1. **The branch is deleted.** After merging, the branch’s work is done. The commits are preserved in `main`’s history forever.

**What goes in the PR description?** Treat it like a cover letter for your changes. What did you change? Why? Anything tricky the reviewer should watch for? Link to the relevant ticket.

#### What you’d say to Claude Code

> “Push my changes and create a pull request. Title it ‘Add Spanish language support to welcome screen.’ In the description, explain that this adds translated strings for the welcome flow across all five screens.”

#### What happens behind the curtain

1. **Pushes your branch** (`git push`) — uploads your local commits to GitHub.com
1. **Creates the PR** (via GitHub CLI) — opens the pull request on GitHub.com targeting `main`
1. **Returns the PR URL** — click through to view, add reviewers, and monitor feedback

#### Where to manage your PR

On your repo’s GitHub.com page, click the **“Pull requests”** tab. Click yours to see:

- **“Conversation”** tab — comments and review decisions
- **“Files changed”** tab — the full diff (this is the most important tab for reviewers)
- The green **“Merge pull request”** button (visible once approved)

> **Check yourself:** A reviewer comments asking you to change some wording. What do you do? *(Answer: Go to VS Code, ask Claude Code to make the change, commit, push. The PR updates automatically.)* After merge, where do your changes live? *(Answer: On `main` — the official version.)*

-----

### Module 6: What Belongs in GitHub (and What Doesn’t) (2 minutes)

#### The concept

GitHub is built for **text files**. Code, markdown documents, configuration files, JSON data — anything you could open in Notepad and read. For these files, GitHub can show you exactly what changed between versions, line by line, word by word. This is the diff view you see in pull requests, and it’s what makes code review possible.

**Some file types don’t work well in GitHub.** It’s important to know this upfront so you make good choices about where things live:

|File type                   |How GitHub handles it                                                                                          |Recommendation                                                                      |
|----------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
|Code (.js, .py, .html, etc.)|Excellent — full diff, line-by-line review                                                                     |This is GitHub’s sweet spot                                                         |
|Markdown (.md)              |Excellent — renders beautifully, full diff                                                                     |Great for READMEs, documentation, PRDs that Claude Code needs as context            |
|CSV, JSON, YAML             |Good — text-based, diffable                                                                                    |Good for data files and configuration                                               |
|Images (.png, .jpg, .svg)   |Stored but not diffable — GitHub shows old vs. new side by side, but can’t show *what* changed within the image|Store if needed for the project (like UI assets), but don’t expect meaningful review|
|PowerPoint (.pptx)          |Stored but opaque — GitHub sees it as a binary blob, can’t show any diff                                       |Keep in Google Slides or SharePoint. Don’t put these in repos.                      |
|Excel (.xlsx)               |Same as PowerPoint — binary, no diff                                                                           |Keep in Google Sheets or SharePoint                                                 |
|Word (.docx)                |Same — binary, no useful diff                                                                                  |Keep in Google Docs                                                                 |
|PDF                         |Stored but not diffable                                                                                        |Fine as a build artifact, but don’t use as a working document in a repo             |

**This doesn’t mean you need to move everything to GitHub.** Google Drive, Confluence, SharePoint — keep using them for the work they’re good at. The goal is to bring the things that *benefit from being near the code* into GitHub:

- **PRDs or specs that Claude Code should reference while building** → put a markdown version in the repo
- **Content strings, copy, or configuration** → these are text files and work great in Git
- **Research findings or context documents that inform product decisions** → markdown in the repo means Claude Code can read them
- **Slide decks for stakeholder presentations** → keep in Google Slides, they don’t belong in a repo

The principle: **if you want Claude Code to see it and use it as context, it should be in the repo.** If it’s for human consumption only, use whatever tool is best for creating it.

> **Check yourself:** You have a PRD in Google Docs that you want Claude Code to reference while it builds a feature. What do you do? *(Answer: Create a markdown version and put it in the repo. Claude Code can then read it as context.)* Your teammate asks you to commit an Excel spreadsheet to the repo. Is that a good idea? *(Answer: Generally no — GitHub can’t show meaningful diffs for Excel files. Keep it in Google Sheets and, if the data is needed in the repo, export it as CSV.)*

-----

### Module 7: Working Across Multiple Repos (2 minutes)

#### The concept

Most products aren’t one repo — they’re several. A frontend repo, a backend API repo, a shared configuration repo, maybe a documentation repo. As a PM, you may need to work across more than one of these in a single session.

**VS Code handles this naturally.** You can open multiple repos in the same VS Code window using a feature called **Workspaces**. Each repo appears as a top-level folder in the Explorer sidebar on the left. It’s like having multiple project folders open in the same Finder/File Explorer window.

**Claude Code can work across repos in your workspace.** When you have multiple repos open, Claude Code can read files from any of them, understand relationships between them, and make coordinated changes. For example, you might say:

> “The API repo defines an endpoint called /card-status. Can you find where the frontend repo calls that endpoint and update the error handling to match the new response format?”

Claude Code traverses both repos, finds the relevant files, and makes changes in the right places.

#### How to set up a multi-repo workspace

You can do this entirely through the VS Code GUI:

1. Open VS Code
1. **File → Add Folder to Workspace…** — navigate to your first cloned repo
1. Repeat for additional repos
1. **File → Save Workspace As…** — saves this arrangement so you can reopen it later

You’ll see each repo as a separate root folder in the sidebar. The branch indicator in the bottom-left now shows the branch for whichever file you have open — each repo can be on a different branch.

#### What you’d say to Claude Code

> “Look at the API spec in the card-servicing-api repo and make sure the frontend in chat-experience-frontend is handling all the error codes correctly”

> “Search across all the repos in my workspace for anywhere we reference the old card-status endpoint”

#### What happens behind the curtain

Claude Code navigates the file system across all repos in your workspace. It can read, search, and modify files in any of them. Git operations (commits, pushes, branches) are still per-repo — a commit in one repo doesn’t affect another. If Claude Code makes changes in two repos, it will create separate commits in each.

> **Check yourself:** You have the API repo and the frontend repo open in the same VS Code workspace. You ask Claude Code to make a change that involves both. How many commits will that produce? *(Answer: At least two — one in each repo. Git operations are per-repo.)* Can Claude Code read a file in a repo you haven’t opened in your workspace? *(Answer: No — it needs the repo to be cloned to your laptop and open in VS Code.)*

-----

### Module 8: Your Daily Workflow and Troubleshooting (3 minutes)

#### Putting it all together

Here’s how a typical session flows. You don’t need to memorize this — Claude Code will guide you. But understanding the shape means you’ll always know where you are.

#### Starting a session

|If…                       |Say this to Claude Code                |What happens                           |
|--------------------------|---------------------------------------|---------------------------------------|
|First time on this project|“Clone the [repo-name] repo”           |Downloads repo to your laptop          |
|Returning to a project    |“Pull the latest changes from main”    |Updates your local copy from GitHub.com|
|Starting new work         |“Create a new branch for [description]”|Creates a safe parallel workspace      |
|Continuing previous work  |“Switch to the [branch-name] branch”   |Returns to your in-progress work       |

#### While you’re working

Ask Claude Code to build, fix, and modify things. Periodically save your progress:

> “Commit what we have so far — we finished the header translations”

Think of commits like breadcrumbs. If something goes wrong, each commit is a point you can return to.

#### When you’re done (or ready for review)

> “Push my changes and create a pull request for review”

Then switch to GitHub.com to add reviewers, polish the description, and monitor feedback.

#### When things feel wrong

**“Claude Code says there are uncommitted changes blocking something.”**
You have modified files that haven’t been committed. Say: *“Commit my current changes first”* or *“Discard my uncommitted changes”* if you don’t want them.

**“Claude Code mentions a merge conflict.”**
Someone else changed the same lines you changed, and Git can’t automatically combine them. Say: *“Help me resolve this merge conflict — show me what the conflict is.”* Claude Code will show both versions and help you choose. For complex conflicts, loop in an engineer.

**“I’m on the wrong branch” or “I don’t know where I am.”**
Look at the bottom-left of VS Code. Say: *“Which branch am I on? Switch me to [correct branch].”*

**“Something is really wrong and I want to start over.”**
Say: *“Reset my branch back to the last commit”* or *“Abandon this branch and start fresh from main.”* Git’s superpower is that the history is always there — starting over is cheap.

**“I need to explain what’s happening to an engineer.”**
Say: *“Summarize the current git status — what branch am I on, are there uncommitted changes, and is my branch up to date with main?”* Share Claude Code’s answer with the engineer. This gives them everything they need to help.

> **Check yourself:** You’ve been working for an hour. Claude Code has made changes to files. You haven’t committed. Your laptop crashes. What happened to your work? *(Answer: Gone. Uncommitted changes are just modified files on your laptop — they’re not in Git’s history. Commit regularly.)* You open VS Code and the bottom-left says `main`. Should you start making changes? *(Answer: No — create a feature branch first, so your work doesn’t go directly on the official version.)*

-----

## Quick Reference Card

|I want to…                    |Say this to Claude Code                          |
|------------------------------|-------------------------------------------------|
|Start working on a new project|“Clone the [repo-name] repo”                     |
|Get the latest version        |“Pull the latest changes from main”              |
|Start new work                |“Create a new branch for [what you’re doing]”    |
|Save my progress              |“Commit with the message ‘[what you did]’”       |
|Share my work for review      |“Push my changes and create a pull request”      |
|See where I am                |“What branch am I on? Any uncommitted changes?”  |
|Switch to different work      |“Switch to the [branch-name] branch”             |
|Undo recent changes           |“Reset to the last commit”                       |
|Get help when confused        |“Summarize the current git status and explain it”|
|Work across multiple repos    |“Look at [file] in the [other-repo] and…”        |

-----

## Glossary

**Local:** Your laptop. Where you do your work. Files here are private to you until you push.

**Remote:** GitHub.com. The shared, cloud-hosted copy of the repo that your team can see.

**Repository (repo):** A project folder that tracks the complete history of every file change. Exists both locally (your laptop) and remotely (GitHub.com).

**Clone:** Downloading a repo from GitHub.com to your laptop for the first time.

**Commit:** A deliberate save point — a snapshot of file changes with a description. Exists locally until pushed.

**Push:** Uploading your local commits to GitHub.com so others can see them. This is how you go from local → remote.

**Pull:** Downloading the latest changes from GitHub.com to your laptop. This is how you go from remote → local.

**Branch:** A parallel copy of the project where you work without affecting others. Every repo has a `main` branch (the official version). You create feature branches for your work.

**Main:** The primary branch — the “official” version. Don’t work directly on it.

**Pull Request (PR):** A proposal to merge your branch’s changes into `main`. Includes a diff of all changes and a review/approval workflow.

**Diff:** A line-by-line view of what changed. Green = added, red = removed. Only meaningful for text-based files.

**Merge:** Combining one branch’s changes into another. Happens after a PR is approved.

**Merge conflict:** Two people changed the same lines. Git needs a human decision about which version to keep.

**Workspace:** A VS Code setup with multiple repos open at once. Each repo maintains its own branches and history independently.

-----

## Appendix A: How These Concepts Map to What You Already Know

|Concept               |What you already know (Google Drive)|Git equivalent                                             |Key difference                                     |
|----------------------|------------------------------------|-----------------------------------------------------------|---------------------------------------------------|
|Where work lives      |In the cloud, always                |On your laptop first, cloud when you push                  |Git is local-first, not cloud-first                |
|Saving                |Automatic, continuous               |Manual — you choose when to commit                         |Deliberate saves tell a story                      |
|Seeing others’ changes|Instant, real-time                  |Manual — you pull when you want updates                    |No real-time sync, but more control                |
|Sharing your changes  |Instant, as you type                |Manual — you push when ready                               |You decide when to share                           |
|The project folder    |A shared Drive folder               |Repository                                                 |Repo includes full history                         |
|Experimenting safely  |“Make a copy” of a doc              |Create a branch                                            |Branches are lightweight and built for merging back|
|Suggesting changes    |“Suggesting” mode in Docs           |Working on a branch + opening a PR                         |More structured, with formal approval              |
|Reviewer approves     |Accept suggestions in Docs          |Approve and merge a PR                                     |One approval step, then merged                     |
|Conflicting edits     |Handled automatically in real time  |Merge conflict — requires manual resolution                |Trade-off of async parallel work                   |
|What types of files   |Anything Google supports            |Text files work great; binary files (pptx, xlsx) don’t diff|Know what to put where                             |

## Appendix B: Why We’re Doing This

You might be wondering: if Git is more work than Google Docs, why bother?

The short answer is that the tools that will define product management over the next several years — Claude Code, GitHub Copilot, Cursor, and whatever comes next — all think in Git. They read repos. They write commits. They open pull requests. They use the files in your repo as context to understand what you’re building, who you’re building it for, and what you’ve decided along the way.

When you bring a product spec into a GitHub repo as a markdown file, it stops being a document that an engineer reads and interprets — it becomes context that an AI agent can actively reference while writing code. When you write acceptance criteria in a GitHub issue, Claude Code can check its work against your intent. When you review a pull request, you’re not just approving code — you’re participating in a workflow where humans and AI agents collaborate using a shared system of record.

None of this requires you to abandon the tools you’re good at. Google Docs is still the best place to draft a narrative. Confluence is still fine for team wikis. Miro is still great for whiteboarding. The goal isn’t to move *everything* to GitHub — it’s to bring the right things closer to the code, so that the AI agents working alongside your team have the richest possible context for doing their best work.

That starts with understanding how the system works. Which, if you’ve read this far, you now do.
