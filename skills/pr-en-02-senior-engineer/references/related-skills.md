# Related Skills and Coordination

Read this reference when implementation reveals an upstream requirements/design change, calls for a specialized workflow, or benefits from independent final review.

## Installed coordination skills

| Skill | Use | Boundary |
|---|---|---|
| `pr-pm-02-project-manager` | Revise scope, SRS behavior, acceptance, qualification, priority, and stable requirement IDs | Does not implement software |
| `pr-ar-01-project-architect` | Revise architecture/SDD, ownership, interfaces, runtime, deployment, ADRs, and design verification | Does not invent product requirements |
| `pr-en-02-senior-engineer` | Implement approved requirements/design, tests, migration, verification, and handoff | Does not silently change scope or architecture |

Normal sequence:

```text
idea/change request
  -> pr-pm-02-project-manager: approved SRS candidate
  -> pr-ar-01-project-architect: matching SDD candidate
  -> pr-en-02-senior-engineer: implementation and verification
  -> user/pr-pm-02-project-manager: acceptance decision
```

Freeze the SRS before generating or revising the SDD. If implementation evidence invalidates a decision, return to the owning Agent and resume from the new frozen baseline.

## Researched engineering Skill candidates

The following public Skills were reviewed on 2026-08-28. They are references or optional future installations, not dependencies of this Agent.

| Candidate | Useful capability | Adoption decision |
|---|---|---|
| [OpenAI Superpowers: test-driven-development](https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/test-driven-development/SKILL.md) | Failing-test and regression-first cycle | Incorporate behavior-first testing; let project qualification and risk select the test level |
| [OpenAI Superpowers](https://github.com/openai/plugins/blob/main/plugins/superpowers/README.md) | Systematic debugging, verification, planning, review, and worktrees | Incorporate root-cause and evidence principles without forcing the whole methodology |
| [OpenAI Agents Python: implementation-final-review](https://github.com/openai/openai-agents-python/blob/main/.agents/skills/implementation-final-review/SKILL.md) | Requirement-based independent final review and frozen-diff evidence | Use the review principles for high-risk work; repository-specific release steps are not universal |
| [OpenAI Agents Python: runtime-behavior-probe](https://github.com/openai/openai-agents-python/blob/main/.agents/skills/runtime-behavior-probe/SKILL.md) | Controlled runtime case matrices | Use only when ordinary tests cannot resolve bounded runtime uncertainty |
| [Anthropic engineering: code-review](https://github.com/anthropics/knowledge-work-plugins/blob/main/engineering/skills/code-review/SKILL.md) | Correctness, security, performance, maintainability, and test review | Optional independent review lens; not installed automatically |

Recheck current primary-source files before installation. Review executable scripts, permissions, network behavior, licensing, and invocation policy before adding any third-party Skill globally.

## Selection rules

- Use the project manager Agent when the unknown is **what behavior is required**.
- Use the project architect Agent when the unknown is **how approved behavior should be structured or deployed**.
- Use this Agent when the baseline is sufficient and the task is **implement, fix, migrate, verify, or review code**.
- Use runtime probes only for bounded behavioral uncertainty, not as a substitute for tests.
- Use independent review for security, persistent data, public protocol, concurrency, permissions, process execution, or broad cross-module changes when practical.
- Do not install or invoke extra Skills merely because they are related; each must remove a real risk or supply a missing capability.
