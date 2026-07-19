# Release Example

This directory holds the source code for the tutorials published at
**[jpipe.org/tutorials](https://www.jpipe.org/tutorials/)**.

Every tutorial builds on the same running example: deciding whether a version is
ready to ship. The argument starts as four lines and grows, one tutorial at a
time, into a justification that a CI pipeline re-checks on every pull request.

The files here are the finished state of each step. Read them alongside the
tutorial that produces them — on their own they show *what* the language looks
like, but the tutorials explain *why* each construct earns its place.

## Files by tutorial

| Tutorial | Files | What it introduces |
| --- | --- | --- |
| [jPipe 101 — Your first justification](https://www.jpipe.org/tutorials/jpipe101/) | [`release.jd`](release.jd) | A conclusion, a strategy, and the evidence supporting it. |
| [Sub-conclusions: growing your argument](https://www.jpipe.org/tutorials/sub-conclusions/) | [`readiness.jd`](readiness.jd) | Intermediate claims, each with its own supporting argument. |
| [Justification templates](https://www.jpipe.org/tutorials/templates/) | [`template.jd`](template.jd) | `template` and `@support` placeholders, instantiated by `implements`. |
| [Splitting an argument across files](https://www.jpipe.org/tutorials/modularity/) | [`quality.jd`](quality.jd), [`load.jd`](load.jd), [`load_as.jd`](load_as.jd) | `load` a template from another file, plainly or under an alias. |
| [Composing with assemble](https://www.jpipe.org/tutorials/assemble/) | [`assemble.jd`](assemble.jd) | Join independent justifications under one shared conclusion. |
| [Composing with refine](https://www.jpipe.org/tutorials/refine/) | [`refine.jd`](refine.jd) | Expand a single node of a draft into a deeper argument. |
| [Make your justification executable](https://www.jpipe.org/tutorials/runner/) | [`run/`](run/), [`mock/`](mock/) | Back each element with a Python check the runner executes. |
| [Justify every change — CI/CD](https://www.jpipe.org/tutorials/cicd/) | [`../.github/workflows/`](../.github/workflows/) | Re-validate the justification in GitHub Actions. |

## Running the example

The runner needs a compiled diagram and a Python library implementing it:

- [`run/release.jd.json`](run/release.jd.json) — `release.jd` compiled to JSON.
- [`run/release_lib.py`](run/release_lib.py) — one function per element, tied
  back to the diagram by `@jpipe_link` annotations.

The checks read from [`mock/`](mock/) rather than a real build, so the example
stays self-contained: `mock/tests.ok` stands in for a passing test suite, and
`mock/CHANGELOG.md` for a changelog naming the release under review.

Flipping the changelog to an older version is what makes the argument fail —
that is the point of the CI tutorial. See
[Install the Runner](https://www.jpipe.org/tutorials/install/runner/) to get
`jpipe-runner` on your machine.

## Continuous integration

Two workflows in [`../.github/workflows/`](../.github/workflows/) run this
example on GitHub:

- **`release-example.yml`** — dispatched by hand. It writes the mock evidence
  itself, taking the changelog version as an input, so you can watch the
  justification pass at `2.0` and fail at `1.9`.
- **`release-pr.yml`** — runs on every pull request targeting `main`, rendering
  the diagram and commenting it on the PR.
