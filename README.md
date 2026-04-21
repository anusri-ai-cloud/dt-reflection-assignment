# Daily Reflection Tree Assignment

## Overview
This project implements a deterministic reflection tool that guides users through structured end-of-day thinking.

Instead of using AI at runtime, the system:
- Uses a predefined decision tree
- Ensures consistent and predictable outputs
- Avoids hallucinations and randomness

The goal is to help users reflect clearly on their actions, contribution, and awareness.

---

## Reflection Axes

The system is designed around three psychological dimensions:

1. **Locus of Control (Responsibility)**
2. **Contribution vs Entitlement**
3. **Radius of Concern (Self vs Others)**

---

## Project Files

- `reflection-tree.json` → Core decision tree (Part A)  
- `agent.py` → CLI-based reflection agent (Part B)  
- `write-up.md` → Design explanation  
- `transcripts/` → Sample execution paths  
- `README.md` → Documentation  

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

START[Start: Begin Reflection] --> Q1[How would you describe your day overall?]

Q1 -->|Productive / Mixed| Q2A[What made things go well?]
Q1 -->|Tough / Frustrating| Q2B[What was your reaction to difficulties?]

Q2A --> Q3[How did you handle challenges?]
Q2B --> Q3

Q3 --> R1[Reflection on Responsibility]

R1 --> Q4[Did you contribute to others?]
Q4 --> Q5[What was your focus today?]

Q5 --> R2[Reflection on Contribution]

R2 --> Q6[Who did you think about most?]
Q6 --> Q7[What impact did your actions have?]

Q7 --> R3[Reflection on Awareness]

R3 --> SUMMARY[Final Reflection Summary]
SUMMARY --> END[End Session]
Agent (Part B)

A simple Python CLI agent is provided.

Features
Loads the decision tree from JSON
Displays questions and options
Accepts user input
Moves through the tree deterministically
Shows reflections and summary
How to Run
Requirements
Python 3 installed
Steps
Download or clone this repository
Open terminal in the project folder
Run the following command:
python agent.py
Follow the instructions in the terminal
Sample Transcripts
transcripts/persona1.md → Low agency / external focus
transcripts/persona2.md → High agency / contribution focus

These demonstrate how different inputs produce different reflection paths.

Design Approach
Questions are simple but thought-provoking
Options are realistic and non-judgmental
Flow progresses logically across all three axes
Fully deterministic system (no AI at runtime)
Conclusion

This project demonstrates how structured decision trees can guide meaningful reflection without relying on generative AI, ensuring clarity, consistency, and reliability.
