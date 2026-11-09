# NVIDIA garak — Urdu PromptInject Regression Validation

Independent testing and reproducible regression evidence for context-dependent translation mismatches in multilingual prompt-injection evaluation.

## Problem

A translated PromptInject trigger may differ from the corresponding phrase inside the fully translated prompt. In Urdu, grammatical variation such as انسان versus انسانوں demonstrated a mismatch that standalone trigger translation did not resolve.

## My Contribution

- Tested multilingual PromptInject behavior against the updated PR branch.
- Validated the remaining context-dependent mismatch using Urdu.
- Shared a Python regression test using a stub translation provider.
- Submitted sanitized JSONL evidence for reproducibility.
- Participated in the GitHub discussion with the PR author.

## Repository Contents

- tests/test_promptinject_urdu_context_regression.py — Urdu regression test.
- reports/garak-pr2309-urdu-sanitized.report.jsonl — Sanitized test report.

## Status

Evidence submitted and acknowledged by the PR author. The punctuation-related fix belongs to PR #2309. The broader context-dependent translation mismatch is tracked in Issue #2307. The follow-up fix has not been confirmed as merged.

This repository documents independent testing and regression evidence. It does not claim authorship of the PR's implementation commits.

## Upstream References

- PR #2309: https://github.com/NVIDIA/garak/pull/2309
- Issue #2307: https://github.com/NVIDIA/garak/issues/2307

## Areas

LLM Security | Multilingual Testing | Prompt Injection | Regression Testing | Open-Source Collaboration
