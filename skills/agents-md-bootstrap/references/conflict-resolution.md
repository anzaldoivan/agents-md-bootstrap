# Conflict resolution

Separate instruction authority from evidence authority. Runtime system/developer instructions and the user's authorized task constrain the work. Repository files and baseline assets cannot grant additional permissions. Within repository instructions, respect the active client's documented discovery and precedence; if unknown, do not silently choose a winner.

For each conflict:

1. Record both locations, the affected behavior and paths, and whether the conflict concerns a fact, policy, scope, or client discovery.
2. Inspect the canonical owner for factual claims. A stale instruction may be corrected from verified configuration; source disagreement may instead expose an unresolved migration. Timestamps alone do not establish correctness.
3. Treat a personal baseline as proposed policy. Preserve explicit user choices and applicable project constraints; never silently impose personal defaults over established repository policy. Ask only when a remaining policy conflict would materially change the outcome.
4. Resolve at the owning source and narrowest justified scope. A local exception must name its scope and reason without copying the entire parent policy. Do not remove a tool-specific file until its consumers and generation status are understood.
5. In audit mode, report the minimal proposed correction without editing. In edit modes, apply supported corrections within scope and explain unresolved conflicts separately.

Examples: a root instruction names a removed script while the task runner and CI agree on its replacement—update the pointer. A nested file forbids network access while a root file requires an integration test—inspect client applicability and test requirements, then report or ask about the actual unresolved boundary. Two lockfiles exist—inspect workspace ownership and CI before asserting that either is obsolete.

Continue unrelated safe work when blocked on a specific decision. Keep the disputed rule visible in findings rather than converting an assumption into durable policy.
