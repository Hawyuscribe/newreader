# Simplified Clinical Reasoning Coach Prompt

SIMPLIFIED_REASONING_PROMPT_INCORRECT = """
## REASONING PAL ANALYSIS

### 1. Analysis of Your Pre-conception
{selected_answer} seemed logical because {analyze_reasoning}, but this reasoning overlooks {key_gap}.

### 2. Why This is Incorrect
The critical error: {specific_mistake}. This led to selecting {selected_answer} instead of recognizing {correct_pattern}.

### 3. Question Deconstruction
- **Key stem elements**: {critical_info}
- **What's being tested**: {concept}
- **Discriminating features**: {differentiators}

### 4. Deep Analysis of Option Differences
| Feature | {selected_answer} | {correct_answer} | Critical Difference |
|---------|-------------------|------------------|-------------------|
| Clinical | | | |
| Timing | | | |
| Lab/Imaging | | | |

### 5. Paraclinical Comparison
| Test | Finding in {selected_answer} | Finding in {correct_answer} |
|------|----------------------------|----------------------------|
| | | |

### 6. Latest Guidelines
"{guideline_quote}" - {source}, {year}
- Level of evidence: {level}
- Key recommendation: {recommendation}

### 7. Knowledge Consolidation
Remember: {key_principle}. The pattern is: {pattern}.

### 8. Differential Diagnosis
| Condition | Key Features | Major Differences |
|-----------|-------------|------------------|
| {correct_answer} | | |
| {selected_answer} | | |
| {other_option} | | |
"""

SIMPLIFIED_REASONING_PROMPT_CORRECT = """
## REASONING PAL ENHANCEMENT

### 1. Strengths in Your Reasoning
You correctly identified {key_insight} and applied {principle}. Consider deepening analysis of {improvement_area}.

### 2. Question Deconstruction
- **Core concept**: {concept}
- **Critical elements**: {elements}
- **Common pitfalls**: {pitfalls}

### 3. Deep Analysis of Why Options Differ
| Feature | {correct_answer} | Other Options | Key Discriminator |
|---------|------------------|---------------|------------------|
| Clinical | | | |
| Course | | | |
| Response | | | |

### 4. Paraclinical Evidence
| Investigation | Gold Standard Finding | Sensitivity/Specificity |
|---------------|---------------------|----------------------|
| | | |

### 5. Current Guidelines (2024-2025)
"{guideline_quote}" - {source}
- Evidence level: {level}
- Clinical application: {application}

### 6. Knowledge Consolidation
Core principle: {principle}. Advanced consideration: {advanced_concept}.

### 7. Related Differentials
| Condition | Overlap with {correct_answer} | Key Differences |
|-----------|------------------------------|-----------------|
| | | |

### 8. Board Exam Pearls
- High-yield association: {association}
- Common trap: {trap}
- Memory tool: {mnemonic}
"""