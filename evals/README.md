# Behavioral evaluations

These cases are reviewable fixtures, not claims of automated agent success. Structural validation only verifies repository invariants. Evaluate decisions separately with a skill-capable agent or a documented manual walkthrough.

## Procedure

1. Create an isolated temporary repository outside this checkout. Materialize the paths and contents described in a case; create no extra source of truth. Commit the starting state, then apply any stated uncommitted change.
2. Make the complete `agents-md-bootstrap` skill available. Give the agent only the case's Request and Repository input, withholding Expected behavior and Failure signals.
3. Capture initial/final status, diff, response, questions, and checks. Do not permit pushes or external mutations. For a blocked question, record the question before supplying any stated follow-up answer.
4. Compare the actual result to the rubric and case expectations. Record agent/client, date, inspected inputs, pass/fail per criterion, and limitations outside the fixture. A manual walkthrough must be labeled as such.
5. For maintain cases, run the same request again against the resulting state; the second run should be a no-op unless new evidence appears.

## Rubric

Pass only if the result preserves user work and requested mode, grounds factual rules in inspected sources, distinguishes selected policy, uses canonical pointers, limits topology to justified files, asks only consequential questions, and reports checks honestly. An invented command, unauthorized audit edit, leaked private baseline detail, or blanket client-precedence assumption is a failure regardless of style.

## Cases

- [Tiny project](cases/tiny-project.md): bootstrap without scaffolding or unnecessary interview.
- [Service project](cases/service-project.md): audit and focused maintenance after a workflow migration; preserve a dirty file and verify no-op behavior.
- [Monorepo](cases/monorepo.md): overlapping scopes, generated instructions, ambiguous clients, and conflicting personal policy.
