# ORI Source Code

## Purpose

The `src` directory contains the implementation of ORI.

While the `docs` directory explains the vision behind ORI and the `specs` directory defines its conceptual models, `src` is where those ideas become working software.

Every module within this directory should directly support the Repository Intelligence methodology established by ORI's specifications.

Implementation should always remain faithful to the conceptual models before introducing new functionality.

---

# Engineering Philosophy

ORI is built around understanding before automation.

Every module should have a clearly defined responsibility.

Every component should contribute to Repository Intelligence in a transparent and explainable way.

Complexity should emerge only when necessary.

Clarity should always take priority.

---

# Source Structure

The implementation is organized into several modules.

```
src/

collector/
models/
engine/
evidence/
observations/
reports/
cli/
```

Each module has a single responsibility.

Together they form the complete Repository Intelligence pipeline.

---

# Module Responsibilities

## collector/

Responsible for collecting repository artifacts from supported platforms.

Examples include:

- Repository metadata
- Source code
- Documentation
- Commit history
- Pull requests
- Issues
- Releases

The collector gathers information without interpreting it.

---

## models/

Implements the conceptual models defined within the specifications.

These models provide consistent internal representations of repositories, knowledge, evidence, and observations.

---

## engine/

Contains the reasoning components that transform collected repository information into Repository Intelligence.

The engine connects repository knowledge, evaluates relationships, and produces explainable insights.

---

## evidence/

Responsible for tracing every observation back to supporting repository artifacts.

This module ensures Repository Intelligence remains transparent and verifiable.

---

## observations/

Creates structured observations based on evidence generated throughout the intelligence process.

Observations become the primary outputs consumed by users.

---

## reports/

Transforms observations into human-readable formats.

Future report formats may include:

- Markdown
- JSON
- HTML
- API responses

---

## cli/

Provides the command-line interface for interacting with ORI.

The CLI serves as the initial user interface during early development.

---

# Engineering Principles

Every implementation within ORI should follow these principles.

- One responsibility per module.
- Repository Intelligence before automation.
- Evidence before conclusions.
- Explainability before optimization.
- Simplicity before complexity.

---

# Building ORI

Implementation should follow the specifications.

When uncertainty exists, contributors should consult:

1. Vision
2. Repository Intelligence
3. Principles
4. Architecture
5. Specifications

The source code should express these documents rather than replace them.
