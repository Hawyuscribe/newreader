Reasoning Modal Prompting (Resident-Focused, Guideline-Aware)

Overview
- Upgrades the clinical reasoning modal to return highly readable, structured teaching notes that explicitly name cognitive bias, correct inaccurate claims, justify the correct answer with neurologic reasoning, show exact guideline quotations (from curated context only), and include an algorithm and comparative table.

What Changed
- New system prompt with required sections: Overview, Cognitive Bias, What Was Incorrect, Why Correct Answer Is Supported, Guideline Evidence (exact quotes only), Algorithm, Comparative Table, Resident Next Steps.
- GuidelineContext is now injected into the model prompt and must be the source for any quoted statements. If none is available, the model states “No direct guideline quotation available.” This prevents hallucinated quotes.
- A lightweight retriever (mcq/guideline_context.py) selects curated quotes for specific topics via keyword matching and loads them from mcq/guidelines/curated_quotes.json.

How To Add/Update Guideline Quotes
1. Edit mcq/guidelines/curated_quotes.json
2. Add/replace the quotes for a topic with exact sentence(s) from a trusted source. Keep quotes short and verbatim.
3. Include a source label, year, and link where possible.
4. If a topic is missing, add a new key and expand mcq/guideline_context.py keyword matcher accordingly.

Safety and Anti‑Hallucination Guardrails
- The model is explicitly instructed to use only the provided GuidelineContext for the “Guideline Evidence” section and to avoid inventing quotes.
- If no context is provided, the model must state that no direct quotation is available.

Developer Pointers
- Prompt definitions live in mcq/clinical_reasoning_prompt.py
- Guideline retrieval lives in mcq/guideline_context.py
- The analyzer wires these into the Celery flow via mcq/cognitive_analysis_openai.py

Resident Experience Goals
- Short, scannable sections with concrete bias labeling and claim checks.
- Actionable diagnostic/treatment algorithm (ordered list).
- Small comparative table using the actual MCQ options.

