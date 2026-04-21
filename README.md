# Daily Reflection Tree Assignment

## Overview
This project implements a deterministic reflection tool that guides users through structured end-of-day thinking.

Instead of using AI at runtime, the system:
- Uses a predefined decision tree
- Ensures consistent and predictable outputs
- Avoids hallucinations

The goal is to help users reflect clearly on their actions, contribution, and awareness.

---

## Reflection Axes

The system is designed around three psychological dimensions:

1. Locus of Control (Responsibility)
2. Contribution vs Entitlement
3. Radius of Concern (Self vs Others)

---

## Project Files

reflection-tree.json → Core decision tree (Part A)  
agent.py → CLI-based reflection agent (Part B)  
write-up.md → Design explanation  
transcripts/ → Sample execution paths  
README.md → Documentation  

---

## Decision Tree (Part A)

The system is built as a structured tree:

- Each node represents a step
- Questions have fixed options
- Decisions are deterministic
- Reflections are predefined

---

## Diagram

```mermaid
graph TD

START --> Q1
Q1 --> Q2A
Q1 --> Q2B
Q2A --> Q3
Q2B --> Q3
Q3 --> Q4
Q4 --> Q5
Q5 --> Q6
Q6 --> Q7
Q7 --> SUMMARY
SUMMARY --> END
