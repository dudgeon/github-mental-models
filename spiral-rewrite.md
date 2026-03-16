# Git Literacy for Product Managers Using Claude Code

## Hybrid PRD / Lesson Plan

---

## Part 1: Product Requirements

### Problem Statement

Product managers joining our Claude Code pilot need a working mental model of Git and GitHub to pair effectively with the tool. Most have never used Git. They don't need to memorize commands – Claude Code handles execution – but they *do* need to understand what's happening, why it matters, and how to recognize when something has gone wrong.

No existing training resource operates at this altitude. Available materials either teach Git commands to developers, or explain GitHub's web UI without connecting to AI-assisted workflows. This is purpose-built.

### Target Learner

- Product manager at Capital One
- Comfortable with Google Drive (Docs, Sheets, shared folders, comment/suggestion workflows)
- Lives almost entirely in the cloud – may have no files stored locally
- Accustomed to real-time synchronous collaboration in a single shared document
- Has heard terms like "repo" or "PR" in passing but can't define them precisely
- Has VS Code installed and Claude Code extension configured
- Has a GitHub Enterprise Cloud account with SSO working
- Does *not* need to become a Git power user – needs to be a competent *collaborator* and *delegator*

### Learning Goals

After completing this training (~20 minutes, self-paced), the learner can:

1. **Explain the difference between local and remote** — why work happens on your laptop first and then gets shared to the cloud, and how this differs from Google Drive
1. **Articulate the tradeoffs** — what you give up and what you gain moving to a Git-based workflow, especially in the context of AI-assisted development
1. **Explain** what a repository is and find their team's repos on GitHub.com
1. **Describe** what a commit represents and why commit messages matter
1. **Explain** why work happens on branches instead of directly on `main`
1. **Describe** the purpose of a pull request and who is involved
1. **Prompt** Claude Code to perform common Git operations and understand what it's doing
1. **Navigate a multi-repo workspace** in VS Code and understand that Claude Code can traverse across repos when given permission
1. **Recognize** when Git is in an error state (merge conflict, detached HEAD, uncommitted changes blocking an operation) and describe the situation clearly enough to get help
1. **Know** what types of files belong in GitHub and which don't

### Non-Goals

- Teaching Git command-line syntax
- Covering advanced workflows (rebasing, cherry-picking, squashing, Git internals)
- Teaching GitHub Actions, CI/CD, or DevOps concepts
- Replacing engineer support for complex merge conflicts
- Requiring PMs to abandon Google Drive, Confluence, or other tools for non-code work

### Delivery Format

Self-guided markdown document (convertible to internal wiki, Google Doc, or LMS module). Each section includes a mental model, a "What you'd say to Claude Code" prompt, a "What happens behind the curtain" explanation, and a quick comprehension check.

---

## Part 2: Lesson Plan

### How to Use This Training

Read each module in order. Budget about 20 minutes. Each module follows the same pattern:

- **The concept** — what it is, explained through something you already know
- **What you'd say to Claude Code** — the natural-language prompt you'd actually type
- **What happens behind the curtain** — what Claude Code does on your behalf
- **Check yourself** — a quick question to confirm the concept landed

No need to have VS Code open. This is a *reading* exercise that builds the mental model you'll use when you sit down to work.

---

### Module 1: Your Work Lives on Your Laptop Now (4 minutes)

#### The concept

This is the biggest shift, so we're starting here.

Almost everything you do right now lives in the cloud. Google Docs, Sheets, Slides, Confluence – they exist on servers and you access them through a browser. Multiple people edit the same document simultaneously and everyone sees each other's cursor in real time. Your laptop is just a window.

**Code doesn't work that way.**

When you work with Claude Code, your work lives in files *on your laptop*. Real files in real folders – like the old days of saving Word documents to your hard drive. This is called working **locally**. The cloud equivalent, where the team's shared official copy lives, is GitHub.com. That's the **remote**.

**Google Drive model:** One copy in the cloud. Everyone connects to it. Changes appear for everyone instantly.

**Git model:** Everyone has their own copy on their own machine. You work on yours privately and, when you're ready, *push* your changes to the shared copy on GitHub.com. Teammates *pull* changes down when they want to see what's new.

#### The honest tradeoffs

Git asks you to work differently, and it's worth naming that clearly:

- **No real-time co-editing.** You can't watch someone's cursor move through code. Two people work on their own copies and reconcile later.
- **Sync is manual.** Changes don't reach teammates until you push. Theirs don't reach you until you pull. Build the habit.
- **Your laptop matters.** Uncommitted local changes exist only on your machine. (Claude Code will remind you to push – more on this in the commits module.)
- **More steps.** Editing a Google Doc is: open, type, done. The Git workflow is: pull the latest, create a branch, make changes, commit, push, open a pull request. Claude Code handles most of these automatically, but understanding the rhythm helps.

#### What you're gaining

The gains are substantial – and they matter especially right now:

- **Every serious AI coding agent speaks Git natively.** Claude Code, GitHub Copilot, Cursor, Windsurf – all of them are built around Git workflows. When your work lives in GitHub, these agents can see it and use it. A PRD in a repo isn't just a document anymore – it's something Claude Code can actively reference while building the feature you described.
- **Precision control over every contribution.** Instead of paragraph-level tracked changes, Git records exact modifications each person (or agent) made, at the line level, with complete history. You can review what Claude Code did, approve it, or roll it back – at any granularity.
- **You get closer to the product itself.** The code in GitHub *is* the product. Working in the same environment as your engineers means you're not reading about what was built – you're looking at it directly. The commit messages, the pull request discussions, the actual files.
- **Experimentation is cheap.** Because everyone works on their own copy, you can try things, break things, and start over without affecting anyone else. In Google Docs, destructive experiments are nerve-wracking. In Git, they're routine – almost encouraged.
- **Everything you bring into GitHub becomes richer AI context.** The more your repos contain – specs, copy strings, decisions, architecture notes – the more Claude Code has to work with when helping you build, understand, and test.

**The bottom line:** You're trading effortless real-time editing for version control, safe parallelism, structured review, and a shared workspace with the best AI coding tools available. The extra steps are real, but Claude Code absorbs most of them – and what you get in return is genuine leverage.

> **Check yourself:** You make changes on your laptop with Claude Code, then close the lid for the day. Can your teammate see those changes on GitHub.com? *(No – they're local until you push.)* Why would anyone choose this over Google Docs? *(Safe parallel work, precise version history, structured review – and AI coding agents are built around Git, so it's the only way to fully collaborate with them.)*

---

### Module 2: Repositories – Your Project's Home (2 minutes)

#### The concept

A **repository** (usually just "repo") is a project folder that remembers everything. It contains all a project's files *plus* the complete history of every change ever made to them.

**Google Drive analogy:** A shared Drive folder for a project – subfolders, documents, spreadsheets. A repo is like that, but with a perfect memory of every version of every file. You can't accidentally "lose" something in a repo, because the history is always there.

|               | Where it lives | How you interact with it |
|---------------|----------------|--------------------------|
| **Remote repo** | GitHub.com (your Enterprise instance) | Browse in a web browser – the shared, official copy |
| **Local repo** | Your laptop, inside a folder | Where Claude Code works – your VS Code project folder |

The first time you work on a project, you **clone** it – downloading the full repo (files + all history) from GitHub to your laptop. After that, push and pull keeps the two copies in sync.

#### Where to find your team's repos

1. Go to GitHub.com and sign in with SSO
1. Your team's repos live under your organization – click the org name in the left sidebar
1. Search by project name. Repos are named in lowercase with hyphens: `card-servicing-api`, `chat-experience-frontend`

#### What you'd say to Claude Code

> "Clone the card-servicing-api repo so I can work on it locally"

#### What happens behind the curtain

Claude Code runs `git clone <url>`, downloading the entire repo to a folder on your laptop. VS Code opens that folder. You only do this once per repo.

> **Check yourself:** Someone says "check the repo." Where do you go? *(GitHub.com – the remote copy.)* Someone says "I cloned the repo." What did they do? *(Downloaded a copy from GitHub to their laptop.)*

---

### Module 3: Commits – Deliberate Save Points (3 minutes)

#### The concept

A **commit** is a deliberate save point. It captures the state of every file in the repo at one moment, paired with a short description of what changed and why.

**Google Drive analogy:** Version history auto-saves constantly with timestamps. Commits are *manually named versions*. Instead of "March 14, 3:42 PM," you get "Add error message when user enters expired card."

**Why deliberate saves?** This connects directly to Module 1. Because Git doesn't auto-save to the cloud, *you* decide when a set of changes is worth recording. This sounds like extra friction, but it's actually a powerful form of storytelling. A commit history that reads like progress — "Add validation for card expiration," "Update error message copy," "Fix edge case for leap year dates" — is dramatically easier to debug and understand than "misc changes," "WIP," "fixed stuff."

**Important:** A commit saves to your *local* repo – not visible to anyone else until you *push*. Think of it as writing in a notebook you haven't shared yet. Commit often; push when you're ready to share.

When you work with Claude Code, *you are the author of these commits*. Your name is on them. Claude Code will suggest commit messages – review them and edit to make sure they clearly describe what changed.

#### What you'd say to Claude Code

> "Commit what we have so far – we've finished the header and navigation translations"

> "Commit with the message 'Add Spanish language support to welcome screen'"

#### What happens behind the curtain

Claude Code does two things:

1. **Stages the changes** (`git add`) — selects which file changes to include
1. **Creates the commit** (`git commit -m "..."`) — records the save point with your message

The commit exists locally. It reaches GitHub.com when you *push*.

#### What a commit looks like on GitHub.com

Once pushed, any commit on GitHub shows you:

- **The author** (your name), **date**, and **message**
- **A diff** — line-by-line view of what was added (green) and removed (red)

This diff is what engineers and reviewers use to understand your change. Worth clicking around on to get comfortable.

> **Check yourself:** Claude Code makes a change. Is it in Git's history? *(No – it's still just a modified file until you commit.)* After you commit, can teammates see it on GitHub? *(Not yet – push first.)*

---

### Module 4: Branches – Parallel Universes for Safe Experimentation (3 minutes)

#### The concept

A **branch** is a parallel copy of the project where you make changes without affecting anyone else's work.

**Google Drive analogy:** You want to experiment with a different PRD structure but don't want to wreck the current version, so you "Make a copy" and work on that. A branch is exactly that – except it applies to the *entire project at once*, and has a built-in mechanism to merge your changes back when you're done.

**The key branch: `main`.** Every repo has a primary branch called `main` — the official version. Nobody works directly on `main`. Instead:

1. Create a new branch off `main` (your parallel universe)
1. Make changes and commit on that branch
1. When ready, propose merging your branch back into `main` via a pull request (next module)
1. After review and approval, your branch merges in

**Why not just work directly on `main`?** Same reason you wouldn't edit a live document while stakeholders are reading it mid-draft. Branches give you a private workspace. And because Git is local-first, your branch is doubly safe – it's on your machine, on your branch, until you push.

**Branch naming:** Short, descriptive, hyphenated: `add-spanish-translations`, `fix-expired-card-error`, `update-welcome-copy`. Claude Code will suggest names.

#### What you'd say to Claude Code

> "Create a new branch for the Spanish translations work"

> "Switch to the add-spanish-translations branch"

> "Pull the latest from main and create a new branch called update-faq-content"

#### What happens behind the curtain

**Creating a branch:** `git checkout -b add-spanish-translations` — creates a branch from your current position (usually `main`) and switches you to it. Commits now go only to *this branch*.

**Switching branches:** `git checkout <branch-name>` — files in VS Code change to reflect that branch's state. Files might appear or disappear. That's normal, not data loss.

**Pulling latest:** `git pull origin main` — downloads new commits from GitHub before you start.

#### How to see which branch you're on

VS Code's **bottom-left corner** shows a branch icon and name. Click it to switch branches from the GUI.

> **Check yourself:** Your teammate says "I pushed to my branch." Are their changes on `main`? *(No – they need a pull request for that.)* You're on `fix-login-bug` and a file looks different than expected. Something wrong? *(Probably not – files reflect whichever branch you're on.)*

---

### Module 5: Pull Requests – Proposing Your Changes for Review (3 minutes)

#### The concept

A **pull request** (PR) is a formal proposal: *"I've made changes on my branch. Here they are – please review and, if they look good, merge them into `main`."*

**Google Drive analogy:** Switching a doc to "Suggesting" mode and tagging reviewers. They see exactly what you changed, leave comments, request revisions, or approve. The difference: your changes don't touch the original until someone explicitly approves and merges.

**The lifecycle:**

1. **You create it.** Push your branch, open a PR on GitHub.com. It includes a title, description, and full diff.
1. **Reviewers examine it.** They see every line added (green) and removed (red), comment on specific lines, and give a decision: Approve or Request Changes.
1. **You revise if needed.** Make more changes in VS Code, commit, push. The PR updates automatically.
1. **Someone merges it.** After approval, one click brings your changes into `main`.
1. **The branch is deleted.** Its work is done. The commits live on in `main`'s history.

**PR description tip:** Treat it like a cover letter. What changed? Why? Anything tricky for the reviewer? Link to the ticket.

#### What you'd say to Claude Code

> "Push my changes and create a pull request. Title it 'Add Spanish language support to welcome screen.' Describe that this adds translated strings for the welcome flow across all five screens."

#### What happens behind the curtain

1. Pushes your branch (`git push`)
1. Creates the PR via GitHub CLI, targeting `main`
1. Returns the PR URL – click through to add reviewers and monitor feedback

#### Where to manage your PR

**"Pull requests"** tab on your repo's GitHub page. Inside your PR:

- **"Conversation"** — comments and review decisions
- **"Files changed"** — the full diff (most important tab for reviewers)
- The green **"Merge pull request"** button (appears once approved)

> **Check yourself:** A reviewer asks you to change some wording. What do you do? *(Go to VS Code, ask Claude Code to make the change, commit, push. The PR updates automatically.)* After merge, where do your changes live? *(On `main`.)*

---

### Module 6: What Belongs in GitHub (and What Doesn't) (2 minutes)

#### The concept

GitHub thrives on **text files**: code, markdown, configuration, JSON. For these, it shows exactly what changed between versions, line by line. That's the diff view you see in pull requests – it's what makes code review possible.

Binary files (Office documents, images) work differently. GitHub stores them, but can't show meaningful diffs.

| File type | How GitHub handles it | Recommendation |
|-----------|----------------------|----------------|
| Code (.js, .py, .html) | Full diff, line-by-line review | GitHub's sweet spot |
| Markdown (.md) | Renders beautifully, full diff | Great for READMEs, docs, PRDs Claude Code needs as context |
| CSV, JSON, YAML | Text-based, diffable | Good for data and config |
| Images (.png, .jpg, .svg) | Stored but not diffable | Include if the project needs them (UI assets, etc.) |
| PowerPoint (.pptx) | Binary – no meaningful diff | Keep in Google Slides |
| Excel (.xlsx) | Binary – no meaningful diff | Keep in Google Sheets; export to CSV if data belongs in Git |
| Word (.docx) | Binary – no meaningful diff | Keep in Google Docs |
| PDF | Stored, not diffable | Fine as a build artifact; not as a working document |

You don't need to move everything to GitHub. Use Drive, Confluence, and SharePoint for what they're good at. Bring things into GitHub when they *benefit from being near the code*:

- **PRDs or specs Claude Code should reference while building** → markdown version in the repo
- **Content strings, copy, or configuration** → text files that work natively in Git
- **Research or context documents that inform product decisions** → markdown means Claude Code can read them
- **Stakeholder slide decks** → stay in Google Slides

The principle: **if you want Claude Code to see it and use it as context, put it in the repo.** If it's for human consumption only, use whatever tool creates it best.

> **Check yourself:** You have a PRD in Google Docs that Claude Code should reference while building a feature. What do you do? *(Create a markdown version and put it in the repo.)* Your teammate asks you to commit an Excel file. Good idea? *(Generally no – keep it in Sheets, or export to CSV if the data belongs in Git.)*

---

### Module 7: Working Across Multiple Repos (2 minutes)

#### The concept

Most products span several repos – a frontend, a backend API, shared configuration, maybe documentation. As a PM, you may work across more than one in a single session.

**VS Code handles this naturally** via **Workspaces**. Open multiple repos in the same VS Code window – each appears as a top-level folder in the Explorer sidebar. Multiple project folders, one window.

**Claude Code can work across repos in your workspace.** When you have multiple repos open, Claude Code reads files from any of them, understands their relationships, and makes coordinated changes:

> "The API repo defines an endpoint called /card-status. Find where the frontend repo calls it and update the error handling to match the new response format."

Claude Code traverses both repos, finds the relevant files, and makes changes in the right places.

#### How to set up a multi-repo workspace

1. **File → Add Folder to Workspace…** — navigate to your first cloned repo
1. Repeat for additional repos
1. **File → Save Workspace As…** — saves the arrangement so you can reopen it later

Each repo can be on a different branch. The branch indicator in the bottom-left reflects whichever file you have open.

#### What you'd say to Claude Code

> "Look at the API spec in card-servicing-api and make sure chat-experience-frontend handles all the error codes correctly"

> "Search across all the repos in my workspace for anywhere we reference the old card-status endpoint"

#### What happens behind the curtain

Claude Code navigates the file system across all repos. Git operations (commits, pushes, branches) remain per-repo – a commit in one repo doesn't affect another. Changes across two repos produce separate commits in each.

> **Check yourself:** API repo and frontend repo are open. You ask Claude Code to make a change in both. How many commits? *(At least two – one per repo.)* Can Claude Code read a file in a repo you haven't cloned and opened? *(No – it needs the repo on your laptop and open in VS Code.)*

---

### Module 8: Your Daily Workflow and Troubleshooting (3 minutes)

#### Putting it all together

Here's the shape of a typical session. You don't need to memorize this – Claude Code guides you through it. But knowing the pattern means you always know where you are.

#### Starting a session

| If… | Say this to Claude Code | What happens |
|-----|------------------------|--------------|
| First time on this project | "Clone the [repo-name] repo" | Downloads repo to your laptop |
| Returning to a project | "Pull the latest changes from main" | Updates your local copy from GitHub |
| Starting new work | "Create a new branch for [description]" | Creates a safe parallel workspace |
| Continuing previous work | "Switch to the [branch-name] branch" | Returns to your in-progress work |

#### While you're working

Ask Claude Code to build, fix, and modify things. Periodically save your progress:

> "Commit what we have so far – we finished the header translations"

Think of commits as breadcrumbs. If something goes wrong, each commit is a point you can return to.

#### When you're done (or ready for review)

> "Push my changes and create a pull request for review"

Then switch to GitHub.com to add reviewers, polish the description, and monitor feedback.

#### When things feel wrong

**"Claude Code says there are uncommitted changes blocking something."**
Modified files haven't been committed yet. Say: *"Commit my current changes first"* — or *"Discard my uncommitted changes"* if you want to start clean.

**"Claude Code mentions a merge conflict."**
You and someone else changed the same lines, and Git can't automatically combine them. Say: *"Help me resolve this merge conflict – show me what the conflict is."* Claude Code will show both versions and help you decide. For complex conflicts, loop in an engineer.

**"I'm on the wrong branch" or "I don't know where I am."**
Check the bottom-left of VS Code. Say: *"Which branch am I on? Switch me to [correct branch]."*

**"Something is really wrong and I want to start over."**
Say: *"Reset my branch back to the last commit"* or *"Abandon this branch and start fresh from main."* Git's history is always there. Starting over costs almost nothing.

**"I need to explain this to an engineer."**
Say: *"Summarize the current git status – what branch am I on, are there uncommitted changes, and is my branch up to date with main?"* Share Claude Code's response. Engineers will have everything they need to help.

> **Check yourself:** You've worked for an hour, Claude Code has made changes, but you haven't committed. Your laptop crashes. What happened? *(Uncommitted changes are just modified files – not in Git's history. Commit regularly.)* You open VS Code and the bottom-left says `main`. Should you start making changes? *(Create a feature branch first.)*

---

## Quick Reference Card

| I want to… | Say this to Claude Code |
|------------|------------------------|
| Start working on a new project | "Clone the [repo-name] repo" |
| Get the latest version | "Pull the latest changes from main" |
| Start new work | "Create a new branch for [what you're doing]" |
| Save my progress | "Commit with the message '[what you did]'" |
| Share my work for review | "Push my changes and create a pull request" |
| See where I am | "What branch am I on? Any uncommitted changes?" |
| Switch to different work | "Switch to the [branch-name] branch" |
| Undo recent changes | "Reset to the last commit" |
| Get help when confused | "Summarize the current git status and explain it" |
| Work across multiple repos | "Look at [file] in the [other-repo] and…" |

---

## Glossary

**Local:** Your laptop. Where you do your work. Files here are private until you push.

**Remote:** GitHub.com. The shared, cloud-hosted copy your team can see.

**Repository (repo):** A project folder that tracks the complete history of every file change. Lives both locally (your laptop) and remotely (GitHub.com).

**Clone:** Downloading a repo from GitHub.com to your laptop for the first time.

**Commit:** A deliberate save point – a snapshot of file changes with a description. Local until pushed.

**Push:** Uploading your local commits to GitHub.com. Local → remote.

**Pull:** Downloading the latest changes from GitHub.com to your laptop. Remote → local.

**Branch:** A parallel copy of the project. Every repo has a `main` branch (the official version). You create feature branches for your work.

**Main:** The primary branch – the official version. Don't work directly on it.

**Pull Request (PR):** A proposal to merge your branch into `main`. Includes a full diff and a review/approval workflow.

**Diff:** A line-by-line view of what changed. Green = added, red = removed. Only meaningful for text-based files.

**Merge:** Combining one branch's changes into another. Happens after a PR is approved.

**Merge conflict:** Two people changed the same lines. Git needs a human decision about which version to keep.

**Workspace:** A VS Code setup with multiple repos open at once. Each repo maintains its own branches and history independently.

---

## Appendix A: How These Concepts Map to What You Already Know

| Concept | Google Drive equivalent | Git equivalent | Key difference |
|---------|------------------------|----------------|----------------|
| Where work lives | In the cloud, always | On your laptop first, cloud when you push | Git is local-first |
| Saving | Automatic, continuous | Manual – you choose when to commit | Deliberate saves tell a story |
| Seeing others' changes | Instant, real-time | Manual – you pull when you want updates | More control, less magic |
| Sharing your changes | Instant, as you type | Manual – you push when ready | You decide when to share |
| The project folder | A shared Drive folder | Repository | Repo includes full history |
| Experimenting safely | "Make a copy" of a doc | Create a branch | Branches are lightweight and built for merging back |
| Suggesting changes | "Suggesting" mode in Docs | Working on a branch + opening a PR | More structured, with formal approval |
| Reviewer approves | Accept suggestions in Docs | Approve and merge a PR | One step, then it's in |
| Conflicting edits | Handled automatically in real time | Merge conflict – requires human resolution | The tradeoff of async parallel work |
| File type support | Anything Google supports | Text files excel; binary files (pptx, xlsx) don't diff | Know what to put where |

---

## Appendix B: Why We're Doing This

If Git is more steps than Google Docs, why bother?

Because the tools that will define product management over the next several years – Claude Code, GitHub Copilot, Cursor, and whatever comes next – all think in Git. They read repos. They write commits. They open pull requests. They use the files in your repo as living context: evidence of what you're building, who it's for, and what your team has decided along the way.

When you bring a product spec into a GitHub repo as a markdown file, it stops being a document that an engineer reads and interprets – and becomes context that an AI agent can actively draw on while writing code. When you write acceptance criteria in a GitHub issue, Claude Code can check its own work against your stated intent. When you review a pull request, you're not just approving code – you're participating in a workflow where humans and AI agents collaborate through a shared system of record.

None of this requires abandoning the tools you already use well. Google Docs is still the best place to draft a narrative. Confluence is still fine for team wikis. Miro is still great for whiteboarding. The goal is to bring the *right things* closer to the code – so that the AI agents working alongside your team have the richest possible context for doing their best work.

That starts with understanding how the system works. Which, if you've read this far, you now do.
