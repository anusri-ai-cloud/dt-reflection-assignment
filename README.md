# Daily Reflection Tree

## Diagram

```mermaid
graph TD

START[Start: Begin Reflection] --> Q1[Q1: How was your day?]

Q1 -->|Productive / Mixed| Q2A[Q2A: What helped your day?]
Q1 -->|Tough / Frustrating| Q2B[Q2B: What went wrong?]

Q2A --> Q3[Q3: How did you handle challenges?]
Q2B --> Q3

Q3 --> R1[Reflection: Responsibility & Agency]

R1 --> Q4[Q4: Did you help someone?]
Q4 --> Q5[Q5: What was your focus?]

Q5 --> R2[Reflection: Contribution]

R2 --> Q6[Q6: Who did you think about?]
Q6 --> Q7[Q7: Impact on others]

Q7 --> R3[Reflection: Awareness]

R3 --> SUMMARY[Summary: Your Reflection]
SUMMARY --> END[End]
