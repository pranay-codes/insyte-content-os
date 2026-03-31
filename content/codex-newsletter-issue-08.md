# Subject Line Options

1. How Parallel Agents Split The Work
2. The Real Reason Some Work Should Stop Waiting In Line
3. When Codex Should Use More Than One Agent
4. Why Parallel Work Can Speed Up A Workflow And Complicate It
5. How To Tell If A Task Should Stay Sequential Or Split In Parallel

# How Parallel Agents Split The Work

## Subheading

If every part of the workflow waits for the previous part to finish, useful work spends too long sitting in line.

## Hook

Imagine the same inbound lead arriving on a busy day.

The team needs a qualification judgment, a short company note, a first draft of the reply, and a quick fit and risk check before anything moves forward.

In a basic workflow, those steps often happen one after another. First someone qualifies the lead. Then someone researches the company. Then someone drafts the reply. Then someone checks the risks. The work moves, but it moves in a line.

That feels orderly, and sometimes it is the right design.

But in many cases, some of that work does not actually need to wait. Research can happen while drafting is being prepared. A fit check can happen alongside the account summary. Different parts of the task can move at the same time, as long as the outputs are clear and the merge point is controlled.

That is where parallel agents become useful.

## Introduction

This is Issue 8 of the series on using OpenAI Codex inside real business workflows. In Issue 7, the focus was on MCP: the connection layer that helps Codex reach the systems and information outside the immediate prompt. That moved the workflow from static pasted context toward a more connected model.

Now we move from connected information to parallel execution.

Even with strong context, a good playbook, reusable Skills, and the right system connections, a workflow can still be slower than it needs to be if all of the work happens in one long sequence. Some parts of a task genuinely depend on earlier steps. Other parts do not. If you treat everything as sequential, some work waits in line for no good reason.

We are still using the same recurring example workflow: `inbound sales follow-up`. The lead arrives. Context is loaded. Qualification is applied. Company research happens. A draft is created. Risks are checked. A next step is recommended. This issue is about recognizing which parts of that work can happen at the same time, where specialization helps, and how to recombine the outputs without creating confusion.

## Searchable Key Phrases

1. parallel agents explained
2. Codex parallel tasks
3. when to use multiple agents in Codex
4. parallel vs sequential workflows
5. how to split work across agents

## This Issue's Insight

Parallel agents let different parts of the job happen at once instead of one after another.

That matters because many workflows stay slower than they need to be simply because all work is forced into one queue. Teams often assume one task means one stream. In reality, a lot of useful work contains several smaller streams that can run independently for part of the workflow and then come back together for review.

OpenAI introduced Codex on May 16, 2025 as a cloud-based agent that can work on many tasks in parallel. OpenAI later described the Codex app on February 2, 2026 as a command center for managing multiple agents at once and running work in parallel, with separate threads organized by projects. The operational lesson is straightforward: parallel work is not a side feature. It is part of how Codex is designed to be used when the task can be safely split. Sources: [Introducing Codex](https://openai.com/index/introducing-codex/), [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)

## Technical Concept Explained

Start with the simplest possible definition.

Parallel agents are separate workstreams running at the same time on different parts of the same broader job.

That is the plain version.

The deeper version is this: parallel agents let you stop treating one big task as one single line of work when parts of it can be separated, specialized, and recombined later.

That is the problem they solve.

Bring this back to the sales-follow-up workflow. Suppose a new lead comes in and you want four things before a human reviews the case:

- a qualification judgment
- a short company note
- a first follow-up draft
- a quick fit and risk check

In a sequential workflow, one person or one agent may try to do those in order. That can work, especially if the task is small. But once the workflow grows, time gets spent waiting for one stage to finish before another even begins.

The question to ask is not, "Can this workflow be split?"

Almost anything can be split.

The better question is, "Can this workflow be split without creating confusion when the parts come back together?"

That is where decomposition matters.

Parallel work only helps when the work can be divided into streams that are clear enough to run independently for a while. In this example, company research may be one stream. Drafting may be another. Risk checking may be a third. Each stream has a narrower focus, a clearer output, and less internal switching.

That is specialization.

Specialization matters because a narrower stream usually produces a more legible result. A research stream produces a company note. A drafting stream produces the first message. A risk stream produces concerns, exclusions, or escalation flags. Those outputs can then be reviewed together instead of one overloaded stream trying to do everything at once.

That is the upside.

The downside is coordination.

Parallel work creates coordination overhead because once the streams finish, someone has to combine the outputs, check for conflicts, and decide what the final recommendation should be. If the streams are poorly defined, they overlap. If they overlap, they may contradict each other. At that point, the workflow becomes harder to supervise rather than easier.

That is why more agents is not automatically better.

Parallel agents help when:

- the work contains distinct subproblems
- the outputs can be clearly defined
- the streams do not step on each other too much
- the results can be recombined cleanly

Parallel agents complicate work when:

- the steps depend tightly on each other
- the outputs are fuzzy
- ownership is unclear
- the merge point is not defined

This is why the reader should think about parallelism as a design choice, not a speed trick.

OpenAI's product framing supports this view. The Codex app is described as a focused space for multitasking with agents, with separate threads organized by projects so users can switch between tasks without losing context. The point is not just that many agents can run. The point is that the work needs structure so those agents remain supervisable. Source: [Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)

Parallel work also changes the review step.

In a sequential workflow, you review one stream of work. In a parallel workflow, you often review the relationship between multiple outputs. Does the draft reflect the company note? Does the risk check contradict the qualification decision? Did one stream surface something that should change the next-step recommendation?

That is why recombination is part of the design, not something you improvise at the end.

Here is the simpler restatement:

Parallel agents help when one task is really several smaller jobs that can move at the same time and come back together cleanly.

## Why This Is Useful For The Business

This matters because slow workflows are often not slow because the team lacks effort. They are slow because work is waiting in line when it does not need to.

If research, drafting, and fit-checking can happen at the same time, the workflow can reach a useful review point sooner. That does not mean every task should be split. It means the business should stop treating every task as if it has the same shape.

In business terms, good parallel design can create:

- faster turnaround on multi-part tasks
- less idle waiting between stages
- clearer specialization
- better use of operator attention
- more visible handoffs between outputs

But parallelism only pays off when coordination is controlled. If the outputs are muddy or conflicting, the workflow simply trades waiting time for merge confusion.

## What It Means In Practice

The goal in this issue is not to split every workflow into multiple agents. It is to learn how to spot one workflow that is unnecessarily sequential and redesign it into a few clear streams.

If Issue 7 was about helping Codex reach the right information, Issue 8 is about helping Codex handle different parts of the work at the same time when that makes sense. By the end of this section, you should have a simple parallel version of the sales-follow-up workflow, with clear stream ownership, clear outputs, and one review point where the work comes back together.

### Step 1: Identify which parts of the workflow do not need to wait

What you should do:

Look at the sales-follow-up workflow and ask which steps genuinely depend on earlier results and which ones could begin in parallel. For example, company research and a draft outline may be able to start at the same time, while the final next-step recommendation may need to wait until both are complete.

What you should understand from this step:

Parallel work starts by finding real independence inside the workflow. If one step truly depends on another, forcing parallelism onto it usually creates noise instead of speed.

What you should have by the end of it:

One short list of workflow parts that could run at the same time.

### Step 2: Split the work into independent streams

What you should do:

Turn those independent parts into separate streams. For this workflow, you might create:

1. a research stream
2. a drafting stream
3. a fit and risk stream

Keep each stream narrow enough that you can explain its job in one sentence.

What you should understand from this step:

The stream is the unit of parallel work. If a stream is too broad, you have simply recreated the original problem inside a smaller box.

What you should have by the end of it:

Two or three clearly named workstreams.

### Step 3: Define the output of each stream

What you should do:

Write down exactly what each stream should return. For example:

1. research stream -> a short company note
2. drafting stream -> a first follow-up draft
3. fit and risk stream -> a list of fit concerns, exclusions, or escalation flags

What you should understand from this step:

Parallel streams only recombine well when each one leaves behind a concrete output.

What you should have by the end of it:

One output definition for each stream.

### Step 4: Assign ownership to each stream

What you should do:

Decide which stream is responsible for which part of the work. Keep the ownership disjoint. Do not let two streams silently solve the same problem unless there is a clear reason.

What you should understand from this step:

Ownership prevents overlap. Overlap is one of the fastest ways to turn parallel work into conflicting work.

What you should have by the end of it:

One simple ownership map for the streams.

### Step 5: Define the recombination point

What you should do:

Choose the moment where the outputs come back together. In this workflow, that might be a short review step where the company note, draft, and fit-check are read together before the final recommendation is made.

What you should understand from this step:

Parallel work is not finished when the streams stop. It is finished when the outputs are reconciled into one usable next step.

What you should have by the end of it:

One clearly defined merge point in the workflow.

### Step 6: Review conflicts before final action

What you should do:

At the recombination point, look for disagreement between the streams. Does the draft sound too confident given the fit flags? Does the research note suggest a weaker opportunity than the qualification stream implied? Resolve those conflicts before anything is approved.

What you should understand from this step:

This is both the cost of parallelism and the control mechanism. The gain is speed and specialization. The price is that someone has to inspect how the parts fit together.

What you should have by the end of it:

One conflict check step that prevents parallel outputs from pulling in different directions.

### Step 7: Compare the parallel version with the sequential one

What you should do:

Write the old version and the new version side by side.

For example:

`sequential: qualify -> research -> draft -> fit check -> review`

`parallel: research + draft + fit check -> recombine -> review`

Then ask whether the new version is actually clearer and faster, not just more elaborate.

What you should understand from this step:

The goal is not to make the workflow look more advanced. The goal is to reduce unnecessary waiting without making review harder.

What you should have by the end of it:

One practical judgment on whether this workflow benefits from partial parallel execution.

Here is the practical lesson of the whole workflow:

Do not split work just because multiple agents are available. Split it when the parts are genuinely independent enough to move in parallel and come back together cleanly.

## Screenshot Plan

Screenshot 1:

- a sequential workflow map showing research, drafting, and fit-checking in one line
- Caption: The workflow is orderly, but some of the work is waiting unnecessarily.

Screenshot 2:

- multiple agent or thread views handling different streams of the same task
- Caption: Parallel agents help when the work can be separated into narrow streams with clear ownership.

Screenshot 3:

- a simple workstream ownership table or merged review view
- Caption: Parallel execution only works well when the outputs come back together through a defined review point.

## Action Checklist

1. Identify one workflow that may be unnecessarily sequential.
2. Mark which parts can run independently.
3. Split those parts into clear streams.
4. Define the output of each stream.
5. Assign ownership to each stream.
6. Define the merge point.
7. Review conflicts before final action.
8. Compare the parallel version with the sequential one.

## CTA

Reply with one workflow in your business that feels slower than it should because too much work is waiting in line.

If you want, I will help you decide whether it should stay sequential or be split into parallel streams.

## Evidence Map

- Claim: OpenAI introduced Codex on May 16, 2025 as an agent that can work on many tasks in parallel.
  - Source: https://openai.com/index/introducing-codex/

- Claim: OpenAI describes the Codex app as a command center for managing multiple agents at once and running work in parallel.
  - Source: https://openai.com/index/introducing-the-codex-app/

- Claim: The Codex app organizes agents into separate threads so users can switch between tasks without losing context.
  - Source: https://openai.com/index/introducing-the-codex-app/

- Claim: Parallel agents let different parts of the work happen at once when those parts can be separated safely.
  - Source: Series operating definition in `content/codex-newsletter-series/SERIES_SYSTEM.md`
