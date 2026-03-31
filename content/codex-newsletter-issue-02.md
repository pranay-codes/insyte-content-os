# Subject Line Options

1. Where Codex Actually Shows Up And Why That Matters
2. Codex Is Not One Interface And That Is The Point
3. The Real Reason Codex Lives In More Than One Place
4. How Codex Fits Into A Real Workflow Instead Of One Screen
5. Before You Use Codex More, Understand Its Surfaces

# Where Codex Actually Shows Up

## Subheading

If you think Codex is one screen, you will miss how it fits into real work.

## Hook

In the previous issue, the problem was simple: what is Codex actually for?

In this issue, the confusion shifts.

You open Codex in one place, read about it in another, see screenshots from a terminal somewhere else, and then hear people mention GitHub reviews, IDE extensions, Slack, and the desktop app. At that point, many non-technical readers make the same mistake. They assume the product is fragmented.

Usually, the opposite is true.

Codex shows up in multiple places because real work shows up in multiple places.

## Introduction

This is Issue 2 of the series on using OpenAI Codex inside real business workflows. In Issue 1, the main idea was that Codex is not just a place to chat. It is an execution-oriented system. That gave us the first mental model.

Now we need the second.

Codex is not meant to live in a single interface because your workflow does not live in a single interface. Work begins in one place, picks up context in another, gets executed somewhere else, and is often reviewed somewhere else again. If you miss that, Codex feels confusing. If you understand it, Codex starts to feel like infrastructure rather than a standalone app.

We are still using the same recurring example workflow: `inbound sales follow-up`. The lead arrives somewhere, the task gets defined somewhere, context gets checked somewhere, work gets executed somewhere, and the result gets reviewed somewhere. This issue is about seeing those places clearly.

## Searchable Key Phrases

1. where does OpenAI Codex work
2. Codex app vs CLI
3. Codex IDE and GitHub
4. Codex surfaces explained
5. Codex workflow interfaces

## This Issue's Insight

Codex appears in multiple surfaces because each surface supports a different kind of work.

That is not a branding detail. It is an operating design choice.

OpenAI said on September 15, 2025 that Codex works where you develop: in the terminal, in the IDE, on the web, in GitHub, and even in the ChatGPT iOS app, all connected by your ChatGPT account. OpenAI then introduced the Codex app on February 2, 2026 as a command center for managing multiple agents and long-running tasks, and later said in the October 6, 2025 general availability announcement that teams could also work with Codex in Slack. Taken together, the message is clear: Codex is designed to move across the places where work already happens. Sources: [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/), [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/), [Codex is now generally available](https://openai.com/index/codex-now-generally-available/)

## Technical Concept Explained

Start with the simplest possible definition.

A surface is the place where you meet the system.

That is all it means. A surface is simply the environment where a certain kind of interaction happens.

The mistake most people make is assuming every surface should be equally good for every job. That is not how useful systems work. Different surfaces exist because different kinds of work need different environments.

If you keep that in mind, the question changes from:

"Why is Codex in so many places?"

to:

"Which place is best for the kind of work I am doing right now?"

That is the more useful question, so let us answer it directly.

### The web and cloud view

For a beginner, the web or cloud surface is usually the easiest place to start. It gives you distance from the technical details and lets you focus on the task itself. You are not worrying about local setup, file paths, or editor state. You are focused on the request and the returned output.

That is its main strength.

The web or cloud view is good for:

- learning the system
- delegating a task
- checking progress
- reviewing outputs
- supervising multiple tasks at once

Its weakness is that it can feel one step removed from the actual working environment. If the task depends heavily on local files, active code context, or hands-on command-line work, the web is often not the most natural place for deeper execution.

So the simplest beginner rule is this:

Use the web or cloud view when you want clarity, supervision, and a clean starting point.

OpenAI's product updates repeatedly position Codex cloud and the app as central places for task management and long-running work. Sources: [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/), [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)

### The desktop app

The desktop app is best understood as a command center.

That is the place you use when the job is no longer "I need one answer." It is "I need to manage work." If you have multiple tasks, multiple agents, or longer-running work that needs monitoring, the app becomes far more useful than a one-off interaction.

Its strengths are:

- visibility across tasks
- easier supervision of long-running work
- a clearer sense of progress
- a better environment for managing multiple streams of work

Its tradeoff is that it is less about immediate hands-on editing and more about orchestration. If you need to be deeply embedded in files and commands, the app may not be the most natural place to stay for the whole job.

So the simple rule is:

Use the app when you want to manage the work, not just trigger it.

OpenAI explicitly describes the Codex app as a command center for agents and long-running tasks. [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)

### The CLI

The CLI is the closest surface to hands-on execution.

If the work depends on files, commands, local tools, environment state, or direct interaction with a project, the CLI is often the strongest surface. It is where Codex can work very close to the underlying system.

Its strengths are:

- direct local execution
- proximity to files and commands
- fast iteration
- strong fit for technical workflows

Its tradeoffs are obvious for a non-technical reader. It is less visually guided, more intimidating, and easier to misuse if you do not understand the environment you are working in. That does not make it bad. It just means it is not the natural starting point for everyone.

So the simple rule is:

Use the CLI when the work is deeply tied to the local environment and you are comfortable being close to that environment.

OpenAI's September 15, 2025 upgrades post positions the CLI around agentic coding workflows with approvals, diffs, to-do tracking, web search, and MCP support. [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)

### The IDE extension

The IDE extension is for people who already live in the editor.

Its biggest advantage is context. If the work depends on the files you are reading, the code you have open, or the local project you are already inside, the extension removes the cost of switching to another tool.

Its strengths are:

- immediate access to local working context
- less tool switching
- a better fit for people already working in the editor
- easier movement between reading, editing, and assigning work

Its tradeoff is that it assumes the editor is already the center of your workflow. For a non-technical operator, that is often not true. If you do not live in VS Code or Cursor, the extension is not the natural entry point.

So the simple rule is:

Use the IDE surface when the editor is already where the work lives.

OpenAI says the extension brings Codex into VS Code, Cursor, and related editors, using open files and selected code as context while supporting cloud task tracking and review. [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)

### GitHub

GitHub is best understood as a review surface.

Its job is not primarily to help you start a task. Its job is to help you inspect, comment on, discuss, and approve work in a structured way. If a workflow ends in a pull request, review thread, or requested revision, GitHub becomes very important.

Its strengths are:

- strong review structure
- clear collaboration and commenting
- good visibility into changes
- a natural home for approval and revision

Its tradeoff is that GitHub is not the most natural place to begin broad exploration. It is strongest when the work already has shape and now needs review.

So the simple rule is:

Use GitHub when the work needs structured review, discussion, and iteration.

OpenAI says Codex can review PRs, comment on them, and implement requested changes from the same thread. [Introducing upgrades to Codex](https://openai.com/index/introducing-upgrades-to-codex/)

### Slack

Slack is a delegation surface.

It is useful when the task starts in conversation and needs to be turned into action without forcing the team to leave its normal communication channel immediately.

Its strengths are:

- low-friction team triggering
- easy handoff from conversation to task
- good fit for collaborative environments

Its tradeoff is that Slack is not where deep execution should usually live. It is better for initiation and coordination than for doing the full job end to end.

So the simple rule is:

Use Slack when the task naturally begins in team conversation.

OpenAI's general availability release says teams can tag `@Codex` in Slack and let it gather context from the thread before routing the task into Codex cloud. [Codex is now generally available](https://openai.com/index/codex-now-generally-available/)

Once you look at the surfaces this way, the confusion starts to disappear.

Codex is not scattered across too many places. It is available in the places that fit different kinds of work.

That is the simpler restatement:

Each surface is good at something. The job is to choose the one that fits the work.

## Why This Is Useful For The Business

This matters for the same reason org charts matter. If the work is happening in the wrong place, it slows down. The wrong surface creates friction. The right surface removes handoff drag.

If a workflow starts with quick delegation and triage, a coordination surface makes sense. If the work depends on deep local context, the editor or terminal makes sense. If the work needs structured review, GitHub makes sense. If a team wants to trigger work from the place where conversations already happen, Slack makes sense.

That reduces two common problems.

First, it reduces tool switching that adds no value. People do not have to force every interaction into the same environment.

Second, it reduces the false choice between convenience and control. The surface can change while the underlying system remains connected.

In business terms, that means smoother handoffs, less rework, clearer review, and a lower barrier to adoption. A tool that fits existing work patterns is much easier to adopt than a tool that demands a whole new ritual.

## What It Means In Practice

The goal in this issue is not to master every Codex surface. It is to learn how to recognize which surface fits which kind of work.

If Issue 1 was about understanding the difference between asking and assigning, Issue 2 is about understanding where those interactions should happen. By the end of this section, you should be able to map one simple workflow across the surfaces that make the most sense for it.

### Step 1: List the places where your workflow already happens

What you should do:

Take the same inbound sales-follow-up example and write down where the work already lives right now. Do not think about Codex yet. Just list the real environments involved. For example: a web form, a CRM, Slack, email, a browser tab, a shared document, GitHub, or an editor.

What you should understand from this step:

This step helps you see that the workflow is already distributed. Codex is not creating complexity here. It is entering an existing flow of work.

What you should have by the end of it:

A short list of the real places where the workflow begins, moves, and gets reviewed.

### Step 2: Mark where understanding happens and where execution happens

What you should do:

For each place in your list, ask a simple question: is this mainly where people try to understand something, or mainly where they try to move the work forward?

For example:

- browser or app view: triage and understanding
- terminal or editor: deeper execution
- GitHub: review and iteration
- Slack: delegation and coordination

What you should understand from this step:

This is the same distinction from Issue 1, but now applied to environments instead of prompts. Different surfaces support different kinds of work.

What you should have by the end of it:

A rough map of which parts of the workflow are for understanding, which are for execution, and which are for review.

### Step 3: Choose one primary surface for starting the task

What you should do:

Pick the place where you would most realistically begin the workflow. For a non-technical operator, that may be the app or the web. For a developer already inside a repository, it may be the editor or terminal. For a team-triggered task, it could start in Slack and move into the cloud.

What you should understand from this step:

You do not need to start everywhere. You need one practical starting point that fits the person doing the work.

What you should have by the end of it:

One chosen starting surface for the workflow.

### Step 4: Choose one surface for deep execution

What you should do:

Now decide where the deeper work should actually happen. If the work depends on local files, commands, or active code context, the terminal or editor is the better home. If the work is better handled as a delegated cloud task, the app or cloud workflow may be a better fit.

What you should understand from this step:

Starting a task and executing a task do not always need to happen in the same place.

What you should have by the end of it:

One chosen execution surface for the workflow.

### Step 5: Choose one surface for review

What you should do:

Decide where a human should inspect the result. If the output is part of a code or change workflow, GitHub may be the cleanest place. If the work stays inside a task thread, the app or related workspace may be enough.

What you should understand from this step:

Review is its own stage. It should happen where comparison, feedback, and approval are easiest.

What you should have by the end of it:

One chosen review surface for the workflow.

### Step 6: Draw the workflow as a surface map

What you should do:

Draw a simple line with arrows. For example:

`Slack or app -> Codex task -> editor or terminal for deeper work -> GitHub or app for review`

Or, if you are keeping it simpler:

`Codex app -> task execution -> review in the same thread`

What you should understand from this step:

Once you can see the surfaces in sequence, Codex stops feeling like too many disconnected tools. It starts to feel like one system meeting the workflow where it already lives.

What you should have by the end of it:

A basic surface map for one workflow.

### Step 7: Decide where you would start first

What you should do:

Choose the one surface you would actually use first if you were testing Codex now. Do not optimize for theoretical completeness. Optimize for realism.

What you should understand from this step:

Adoption usually fails when people try to start everywhere at once. It works better when they start in the surface that already feels natural to them.

What you should have by the end of it:

One realistic first surface to use and one simple workflow path to test.

Here is the practical lesson of the whole workflow:

You do not need to master every Codex surface before you begin. You only need to understand what each one is for and choose the one that best fits the work in front of you.

## Screenshot Plan

Screenshot 1:

- Codex app or web view showing active tasks and threads
- Caption: This is a coordination surface. It helps you see and manage the work.

Screenshot 2:

- CLI or IDE view showing Codex working inside a local environment
- Caption: This is an execution surface. It is where deeper local work happens.

Screenshot 3:

- GitHub review or PR-related Codex view
- Caption: This is a review surface. It is where the work is inspected, discussed, and approved.

## Action Checklist

1. List the places where one real workflow already happens.
2. Mark where understanding happens, where execution happens, and where review happens.
3. Pick one realistic starting surface.
4. Pick one realistic execution surface.
5. Pick one realistic review surface.
6. Draw the workflow as a simple surface map.
7. Choose the one surface you would actually start using first.

## CTA

Reply with the surface you would start with first: app, web, terminal, editor, GitHub, or Slack.

If you want, I will help you map one real workflow across the right Codex surfaces.

## Evidence Map

- Claim: On September 15, 2025, OpenAI said Codex works in the terminal, IDE, on the web, in GitHub, and in the ChatGPT iOS app, connected by a ChatGPT account.
  - Source: https://openai.com/index/introducing-upgrades-to-codex/

- Claim: OpenAI said the Codex IDE extension brings Codex into VS Code, Cursor, and other VS Code forks, and lets users create, track, and review cloud tasks without leaving the editor.
  - Source: https://openai.com/index/introducing-upgrades-to-codex/

- Claim: OpenAI introduced the Codex app on February 2, 2026 as a command center for agents designed to manage multiple agents, run work in parallel, and collaborate over long-running tasks.
  - Source: https://openai.com/index/introducing-the-codex-app/

- Claim: OpenAI said on October 6, 2025 that Codex could be used in Slack by tagging `@Codex` in a channel or thread, where it gathers context and returns a link to the completed task in Codex cloud.
  - Source: https://openai.com/index/codex-now-generally-available/

- Claim: OpenAI’s Codex product page says Codex can be used across multiple surfaces connected by a ChatGPT account, including the app, editor, and terminal.
  - Source: https://openai.com/codex/
