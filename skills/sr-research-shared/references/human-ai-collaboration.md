# Human–AI Collaboration Boundaries

## AI may lead reversible preparation

- Structure notes, build comparison tables, expose contradictions and missing fields.
- Propose search terms, alternative hypotheses, counterexamples, controls, analyses, plots, outlines, and draft text.
- Execute approved local calculations, scripts, and bounded experiments with preserved inputs and logs.
- Check consistency among claims, evidence, figures, citations, configuration, and reported conclusions.

## The doctoral researcher must decide

- The research question, scope, novelty position, theoretical assumptions, and main hypothesis.
- Whether data are authentic, admissible, representative, ethically usable, and correctly interpreted.
- Experimental budget, resource allocation, stopping thresholds, exclusions, and reruns.
- Statistical estimand/test choice, practical significance, causal interpretation, and claim strength.
- Commitments to collaborators, authorship or acknowledgment positions, external messages, submissions, patents, and public releases.

## Mandatory intervention points

Pause with a concrete decision brief when any of these occurs:

1. The next action changes the approved research question or scope.
2. Two plausible hypotheses imply materially different experiments.
3. Data inclusion/exclusion, leakage, privacy, ethics, or provenance is disputed.
4. A run exceeds the approved compute, time, sample, equipment, or monetary budget.
5. Evidence conflicts with the expected result or suggests implementation/data failure.
6. A conclusion would become stronger than the available evidence or broader than the tested domain.
7. Work will affect another person, shared system, external service, submission, or public artifact.

Use this brief:

```yaml
human_decision:
  question: ""
  options: []
  evidence_for_each: []
  uncertainty: []
  ai_recommendation: ""
  consequence_of_delay: ""
```

AI recommendations are advisory. Record the researcher's decision and rationale before continuing.
