
# Import batch 1 of 3 from chunk_7_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993178",
    "fields": {
      "question_number": "167",
      "question_text": "Case scenario of patient with new onset slurred speech and left sided weakness. Symptoms started in the morning, he came to ER in the evening. Brain CT: right hemispheric stroke. BP was 180/95 mmHg. What is the best next step for BP control?",
      "options": {
        "A": "IV Hydralazine",
        "B": "IV Labetalol",
        "C": "No intervention needed",
        "D": "Oral Amlodipine"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke is frequently accompanied by a stress-related elevation in blood pressure. Permissive hypertension is a well\u2010recognized compensatory mechanism to maintain cerebral perfusion in the ischemic penumbra.",
        "pathophysiology": "After an ischemic stroke, cerebral autoregulation may be impaired. The elevated blood pressure helps maintain blood flow to the ischemic regions. Aggressive blood pressure reduction could diminish perfusion to these vulnerable areas, potentially expanding the infarct.",
        "clinical_correlation": "This patient\u2019s blood pressure of 180/95 mmHg is below the thresholds (typically >220/120 mmHg in non-thrombolysed patients) at which immediate pharmacologic lowering is indicated. His presentation, with a right hemispheric infarct on CT and onset several hours earlier, fits the picture where blood pressure is allowed to remain elevated.",
        "diagnostic_approach": "In acute stroke, the differential for hypertension includes a stress response to stroke versus pre-existing chronic hypertension. Blood pressure is carefully monitored and only managed if it exceeds thresholds or if the patient is a candidate for thrombolytic therapy (which requires lower BP).",
        "classification_and_neurology": "This case fits within the classification of acute ischemic stroke, specifically a non-thrombolysis candidate due to delayed presentation (>4.5 hours). Ischemic strokes are classified by etiology (e.g., large artery atherosclerosis, cardioembolism, small vessel disease) and clinical syndrome (e.g., cortical vs lacunar). BP management falls under acute stroke care protocols, which are standardized by organizations such as the American Heart Association/American Stroke Association (AHA/ASA). The classification of stroke severity and timing guides therapeutic interventions, including BP control strategies. Over time, classification systems have evolved to integrate imaging, clinical, and pathophysiological criteria to optimize individualized care.",
        "classification_and_nosology": "Acute ischemic stroke management guidelines distinguish between patients with elevated blood pressures who are eligible for thrombolysis (requiring controlled BP) and those with non-thrombolytic strokes who can be managed with permissive hypertension.",
        "management_principles": "Current guidelines recommend not lowering the blood pressure acutely in ischemic stroke patients who are not candidates for thrombolysis, unless systolic BP is >220 mmHg or diastolic BP is >120 mmHg. In pregnant or lactating patients, similar thresholds apply, with careful selection of antihypertensive agents when required. The best approach is often supportive management rather than aggressive BP reduction.",
        "option_analysis": "Option A (IV Hydralazine) and Option B (IV Labetalol) are antihypertensives that are used if blood pressure exceeds safety thresholds or in patients undergoing thrombolysis. Option D (Oral Amlodipine) is not appropriate in the acute management phase due to its slower onset. Hence, Option C (No intervention needed) is correct given the patient\u2019s BP relative to guideline thresholds.",
        "clinical_pearls": "1. Permissive hypertension in acute ischemic stroke is critical to maintaining perfusion in the ischemic penumbra. 2. Only in patients eligible for thrombolysis or with severely elevated pressures should BP lowering be initiated acutely.",
        "current_evidence": "Recent stroke guidelines continue to support a strategy of permissive hypertension in the absence of thrombolysis, emphasizing that overzealous BP lowering may worsen outcomes by reducing perfusion in the ischemic brain."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_3.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993179",
    "fields": {
      "question_number": "168",
      "question_text": "Case scenario of patient with symptomatic ICA stenosis. He underwent carotid endarterectomy. Few days later developed new onset confusion and decreased level of consciousness. Urgent brain CT attached. What could explain his current condition?",
      "options": {
        "A": "Malignant MCA transformation",
        "B": "Cerebral venous thrombosis",
        "C": "Hyperperfusion",
        "D": "provided."
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral hyperperfusion syndrome (CHS) is a recognized complication following carotid endarterectomy. It results from a sudden increase in blood flow in cerebral territories that have lost their autoregulatory capacity due to chronic hypoperfusion.",
        "pathophysiology": "In patients with severe carotid stenosis, cerebral vessels distal to the stenosis are chronically dilated to maintain perfusion. After revascularization, these vessels may not be able to constrict appropriately, leading to hyperperfusion. This may result in cerebral edema, hemorrhage, and neurologic deterioration, which explains the patient\u2019s confusion and decreased level of consciousness.",
        "clinical_correlation": "The onset of symptoms a few days after carotid endarterectomy, in a patient with prior symptomatic ICA stenosis, is highly suggestive of CHS rather than thromboembolic events. The clinical picture of altered mental status corresponds with the expected manifestations of hyperperfusion-induced brain injury.",
        "diagnostic_approach": "Diagnosis is made clinically, supplemented by imaging studies. CT or MRI may show cerebral edema or even hemorrhage in severe cases, differentiating CHS from other complications such as thromboembolic stroke or malignant MCA infarction. Differential diagnoses include malignant middle cerebral artery (MCA) infarction and cerebral venous thrombosis, but the timing (post-endarterectomy) fits best with hyperperfusion.",
        "classification_and_neurology": "Cerebral hyperperfusion syndrome after carotid revascularization is classified as a reperfusion injury syndrome within the broader category of cerebrovascular complications of carotid interventions. It is distinct from ischemic stroke and hemorrhagic stroke but can overlap clinically and radiologically with hemorrhagic transformation of infarcts. Nosologically, it falls under post-procedural cerebrovascular syndromes in stroke classification systems such as the TOAST classification (Trial of ORG 10172 in Acute Stroke Treatment) which classifies strokes by etiology but also considers procedure-related complications. The syndrome is recognized in vascular neurology and neurocritical care taxonomies as a distinct entity requiring specific management. Classification systems have evolved to emphasize the importance of hemodynamic factors and autoregulatory failure in stroke pathophysiology, and CHS exemplifies this concept. There remains some debate about diagnostic criteria and thresholds for hyperperfusion on imaging modalities such as transcranial Doppler or perfusion MRI, reflecting ongoing refinement in nosology.",
        "classification_and_nosology": "CHS falls under the category of post-revascularization complications. It is distinct from other post-surgical complications such as embolic stroke or hemorrhagic conversion, with its hallmark being impaired cerebral autoregulation.",
        "management_principles": "Management involves careful blood pressure control to mitigate the risk and severity of hyperperfusion. First-line management includes tight BP control using short-acting intravenous antihypertensives (e.g., labetalol or nicardipine), along with supportive care. In pregnant or lactating patients who undergo carotid procedures (rare), BP management must consider fetal safety, often using agents with well-established safety profiles. Monitoring in an intensive care setting is typically required, and early recognition is paramount to prevent intracerebral hemorrhage.",
        "option_analysis": "Option A (Malignant MCA transformation) usually presents with significant mass effect and midline shift; Option B (Cerebral venous thrombosis) has a different clinical and radiologic profile; Option C (Hyperperfusion) is correct as it exactly explains the post-operative scenario. There was no Option D provided.",
        "clinical_pearls": "1. After carotid endarterectomy, new neurological deficits with altered mental status should raise the suspicion for cerebral hyperperfusion syndrome. 2. Prevention by meticulous blood pressure control post-surgery is key to reducing the incidence of CHS.",
        "current_evidence": "Recent literature supports the use of strict blood pressure management protocols post-carotid revascularization to prevent CHS. Updated guidelines underscore the importance of early detection and management, utilizing continuous BP monitoring and rapidly titratable antihypertensive agents."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_3.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993180",
    "fields": {
      "question_number": "169",
      "question_text": "Scenario of acute ischemic stroke, started on IV tPA, 30 minutes later he has headache, vomiting, lethargy, BP 180/100 mmHg. What is the best next step?",
      "options": {
        "A": "Brain CT",
        "B": "Stop tPA",
        "C": "IV Labetalol",
        "D": "Close observation"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the recognition and prompt management of a hemorrhagic complication during intravenous thrombolytic therapy (IV tPA) for acute ischemic stroke. The clinical scenario is designed to alert you to the signs of a potential intracerebral hemorrhage developing soon after tPA administration.",
        "pathophysiology": "tPA works by promoting fibrinolysis to dissolve clots; however, it also disrupts the blood\u2013brain barrier and local hemostasis. In some patients, especially when blood pressures are high or vessel integrity is compromised, this can lead to a hemorrhagic transformation. The sudden onset of headache, vomiting, and lethargy, along with an elevation in blood pressure, are red flags for intracranial bleeding.",
        "clinical_correlation": "The patient\u2019s neurologic deterioration (lethargy) combined with symptoms of increased intracranial pressure (headache, vomiting) soon after commencement of tPA strongly suggests a hemorrhagic complication. The elevated blood pressure further increases the risk of bleeding. It is essential to act immediately to prevent further hemorrhage.",
        "diagnostic_approach": "In suspected hemorrhagic transformation post-tPA, the immediate step is to stop the tPA infusion to prevent additional thrombolysis and ongoing bleeding. This is then followed by emergent neuroimaging\u2014typically a noncontrast CT scan\u2014to confirm the presence and extent of intracerebral hemorrhage. Differential diagnoses might include reperfusion injury or a stroke progression, but the clinical picture here is most consistent with hemorrhage.",
        "classification_and_neurology": "Hemorrhagic transformation after ischemic stroke is classified based on radiological and clinical criteria. The European Cooperative Acute Stroke Study (ECASS) classification divides hemorrhagic transformation into hemorrhagic infarction (HI) and parenchymal hematoma (PH), with further subtypes (HI1, HI2, PH1, PH2) reflecting extent and severity. Symptomatic intracerebral hemorrhage (sICH) is defined by neurological deterioration attributable to hemorrhage, often confirmed radiographically. This classification guides prognosis and management decisions. Intracerebral hemorrhage secondary to thrombolysis is a subtype of secondary hemorrhagic stroke. The classification systems have evolved to standardize reporting in clinical trials and practice, with ongoing debate regarding optimal definitions of sICH. Current consensus emphasizes the importance of radiologic confirmation combined with clinical correlation.",
        "classification_and_nosology": "This scenario pertains to an adverse effect of IV tPA, specifically symptomatic intracerebral hemorrhage (sICH), which is a known complication. It is classified as a hemorrhagic transformation of an ischemic stroke induced by thrombolytic therapy.",
        "management_principles": "Immediate management involves: 1) Stopping the tPA infusion to prevent further bleeding, 2) Urgently obtaining a noncontrast CT scan to confirm hemorrhage, 3) If hemorrhage is confirmed, initiating measures to reverse the fibrinolytic state (commonly via administration of cryoprecipitate or antifibrinolytics) and controlling blood pressure. Guidelines recommend rapidly discontinuing tPA when intracranial hemorrhage is suspected. In pregnant or lactating patients, while imaging (CT scan) is still indicated, appropriate shielding and risk/benefit discussion should be undertaken.",
        "option_analysis": "\u2022 Option A (Brain CT): Although CT imaging is essential, it is not the very first step because the tPA infusion must be halted immediately to avoid further bleeding. \\n\u2022 Option B (Stop tPA): This is correct since the immediate cessation of thrombolytic therapy is the highest priority upon suspicion of hemorrhage. \\n\u2022 Option C (IV Labetalol): While blood pressure control is important, using antihypertensives before stopping tPA does not address the ongoing thrombolytic effect. \\n\u2022 Option D (Close observation): Observation is insufficient given the high risk of a life\u2010threatening hemorrhage; immediate intervention is required.",
        "clinical_pearls": "\u2022 Any neurological deterioration or signs of raised intracranial pressure during tPA infusion should prompt immediate discontinuation of the drug. \\n\u2022 Elevated BP and symptoms such as headache and vomiting in this setting are highly suspicious for intracerebral hemorrhage.",
        "current_evidence": "Recent American Heart Association/American Stroke Association guidelines stress the importance of rapid recognition and management of tPA-induced hemorrhagic complications. Immediate cessation of tPA is universally recommended, followed by urgent neuroimaging to verify the diagnosis and allow for timely intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993181",
    "fields": {
      "question_number": "170",
      "question_text": "Direct case scenario of thunderclap headache, CT shows subarachnoid bleed. CTA identified PCom artery aneurysm. Patient is medically free in her 40s. What is the best intervention?",
      "options": {
        "A": "Endovascular coiling",
        "B": "Surgical clipping",
        "C": "Annual follow up"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the recognition and prompt management of a hemorrhagic complication during intravenous thrombolytic therapy (IV tPA) for acute ischemic stroke. The clinical scenario is designed to alert you to the signs of a potential intracerebral hemorrhage developing soon after tPA administration.",
        "pathophysiology": "tPA works by promoting fibrinolysis to dissolve clots; however, it also disrupts the blood\u2013brain barrier and local hemostasis. In some patients, especially when blood pressures are high or vessel integrity is compromised, this can lead to a hemorrhagic transformation. The sudden onset of headache, vomiting, and lethargy, along with an elevation in blood pressure, are red flags for intracranial bleeding.",
        "clinical_correlation": "The patient\u2019s neurologic deterioration (lethargy) combined with symptoms of increased intracranial pressure (headache, vomiting) soon after commencement of tPA strongly suggests a hemorrhagic complication. The elevated blood pressure further increases the risk of bleeding. It is essential to act immediately to prevent further hemorrhage.",
        "diagnostic_approach": "In suspected hemorrhagic transformation post-tPA, the immediate step is to stop the tPA infusion to prevent additional thrombolysis and ongoing bleeding. This is then followed by emergent neuroimaging\u2014typically a noncontrast CT scan\u2014to confirm the presence and extent of intracerebral hemorrhage. Differential diagnoses might include reperfusion injury or a stroke progression, but the clinical picture here is most consistent with hemorrhage.",
        "classification_and_neurology": "Ruptured intracranial aneurysms causing SAH fall under the broader category of hemorrhagic stroke. The World Federation of Neurosurgical Societies (WFNS) grading scale and Hunt and Hess scale are commonly used to classify severity based on clinical presentation. Aneurysms are classified by morphology (saccular, fusiform), location (anterior vs posterior circulation), and rupture status. The International Subarachnoid Aneurysm Trial (ISAT) and other studies have shaped current nosology by stratifying patients for endovascular versus surgical management. The classification of SAH also includes perimesencephalic nonaneurysmal SAH, which has a more benign course. The current consensus favors early intervention to secure ruptured aneurysms, differentiating from unruptured aneurysm management strategies.",
        "classification_and_nosology": "This scenario pertains to an adverse effect of IV tPA, specifically symptomatic intracerebral hemorrhage (sICH), which is a known complication. It is classified as a hemorrhagic transformation of an ischemic stroke induced by thrombolytic therapy.",
        "management_principles": "Immediate management involves: 1) Stopping the tPA infusion to prevent further bleeding, 2) Urgently obtaining a noncontrast CT scan to confirm hemorrhage, 3) If hemorrhage is confirmed, initiating measures to reverse the fibrinolytic state (commonly via administration of cryoprecipitate or antifibrinolytics) and controlling blood pressure. Guidelines recommend rapidly discontinuing tPA when intracranial hemorrhage is suspected. In pregnant or lactating patients, while imaging (CT scan) is still indicated, appropriate shielding and risk/benefit discussion should be undertaken.",
        "option_analysis": "\u2022 Option A (Brain CT): Although CT imaging is essential, it is not the very first step because the tPA infusion must be halted immediately to avoid further bleeding. \\n\u2022 Option B (Stop tPA): This is correct since the immediate cessation of thrombolytic therapy is the highest priority upon suspicion of hemorrhage. \\n\u2022 Option C (IV Labetalol): While blood pressure control is important, using antihypertensives before stopping tPA does not address the ongoing thrombolytic effect. \\n\u2022 Option D (Close observation): Observation is insufficient given the high risk of a life\u2010threatening hemorrhage; immediate intervention is required.",
        "clinical_pearls": "\u2022 Any neurological deterioration or signs of raised intracranial pressure during tPA infusion should prompt immediate discontinuation of the drug. \\n\u2022 Elevated BP and symptoms such as headache and vomiting in this setting are highly suspicious for intracerebral hemorrhage.",
        "current_evidence": "Recent American Heart Association/American Stroke Association guidelines stress the importance of rapid recognition and management of tPA-induced hemorrhagic complications. Immediate cessation of tPA is universally recommended, followed by urgent neuroimaging to verify the diagnosis and allow for timely intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_3.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993182",
    "fields": {
      "question_number": "171",
      "question_text": "Scenario of 65 years old male with multiple cardiovascular risk factors and afib, with 1 day history of right sided dense plegia and aphasia. His brain CT attached. Clinically he is lethargic and poorly communicating. Best next treatment option to consider?",
      "options": {
        "A": "Anticoagulation",
        "B": "Osmotic therapy",
        "C": "Craniotomy/decompression",
        "D": "Aspirin"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the recognition and prompt management of a hemorrhagic complication during intravenous thrombolytic therapy (IV tPA) for acute ischemic stroke. The clinical scenario is designed to alert you to the signs of a potential intracerebral hemorrhage developing soon after tPA administration.",
        "pathophysiology": "tPA works by promoting fibrinolysis to dissolve clots; however, it also disrupts the blood\u2013brain barrier and local hemostasis. In some patients, especially when blood pressures are high or vessel integrity is compromised, this can lead to a hemorrhagic transformation. The sudden onset of headache, vomiting, and lethargy, along with an elevation in blood pressure, are red flags for intracranial bleeding.",
        "clinical_correlation": "The patient\u2019s neurologic deterioration (lethargy) combined with symptoms of increased intracranial pressure (headache, vomiting) soon after commencement of tPA strongly suggests a hemorrhagic complication. The elevated blood pressure further increases the risk of bleeding. It is essential to act immediately to prevent further hemorrhage.",
        "diagnostic_approach": "In suspected hemorrhagic transformation post-tPA, the immediate step is to stop the tPA infusion to prevent additional thrombolysis and ongoing bleeding. This is then followed by emergent neuroimaging\u2014typically a noncontrast CT scan\u2014to confirm the presence and extent of intracerebral hemorrhage. Differential diagnoses might include reperfusion injury or a stroke progression, but the clinical picture here is most consistent with hemorrhage.",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology (TOAST classification): large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), other determined etiology, and undetermined etiology. This patient\u2019s atrial fibrillation places him in the cardioembolic stroke category. From a clinical subtype perspective, this is a large vessel occlusion affecting the MCA territory. Stroke severity and complications further stratify patients into those with malignant MCA infarction, characterized by large infarct volume and risk of life-threatening edema. The concept of malignant MCA infarction is recognized in stroke classifications due to its distinct clinical course and management implications. Over time, classification systems have evolved to incorporate imaging biomarkers and clinical severity to guide therapy, including decompressive hemicraniectomy.",
        "classification_and_nosology": "This scenario pertains to an adverse effect of IV tPA, specifically symptomatic intracerebral hemorrhage (sICH), which is a known complication. It is classified as a hemorrhagic transformation of an ischemic stroke induced by thrombolytic therapy.",
        "management_principles": "Immediate management involves: 1) Stopping the tPA infusion to prevent further bleeding, 2) Urgently obtaining a noncontrast CT scan to confirm hemorrhage, 3) If hemorrhage is confirmed, initiating measures to reverse the fibrinolytic state (commonly via administration of cryoprecipitate or antifibrinolytics) and controlling blood pressure. Guidelines recommend rapidly discontinuing tPA when intracranial hemorrhage is suspected. In pregnant or lactating patients, while imaging (CT scan) is still indicated, appropriate shielding and risk/benefit discussion should be undertaken.",
        "option_analysis": "\u2022 Option A (Brain CT): Although CT imaging is essential, it is not the very first step because the tPA infusion must be halted immediately to avoid further bleeding. \\n\u2022 Option B (Stop tPA): This is correct since the immediate cessation of thrombolytic therapy is the highest priority upon suspicion of hemorrhage. \\n\u2022 Option C (IV Labetalol): While blood pressure control is important, using antihypertensives before stopping tPA does not address the ongoing thrombolytic effect. \\n\u2022 Option D (Close observation): Observation is insufficient given the high risk of a life\u2010threatening hemorrhage; immediate intervention is required.",
        "clinical_pearls": "\u2022 Any neurological deterioration or signs of raised intracranial pressure during tPA infusion should prompt immediate discontinuation of the drug. \\n\u2022 Elevated BP and symptoms such as headache and vomiting in this setting are highly suspicious for intracerebral hemorrhage.",
        "current_evidence": "Recent American Heart Association/American Stroke Association guidelines stress the importance of rapid recognition and management of tPA-induced hemorrhagic complications. Immediate cessation of tPA is universally recommended, followed by urgent neuroimaging to verify the diagnosis and allow for timely intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_3.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993183",
    "fields": {
      "question_number": "172",
      "question_text": "Elderly female admitted with stroke. Attached her brain MRI. What else you will find?",
      "options": {
        "A": "Left Horner syndrome",
        "B": "Left facial sensory loss",
        "C": "Left uvula deviation",
        "D": "Facial nerve palsy"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the recognition and prompt management of a hemorrhagic complication during intravenous thrombolytic therapy (IV tPA) for acute ischemic stroke. The clinical scenario is designed to alert you to the signs of a potential intracerebral hemorrhage developing soon after tPA administration.",
        "pathophysiology": "tPA works by promoting fibrinolysis to dissolve clots; however, it also disrupts the blood\u2013brain barrier and local hemostasis. In some patients, especially when blood pressures are high or vessel integrity is compromised, this can lead to a hemorrhagic transformation. The sudden onset of headache, vomiting, and lethargy, along with an elevation in blood pressure, are red flags for intracranial bleeding.",
        "clinical_correlation": "The patient\u2019s neurologic deterioration (lethargy) combined with symptoms of increased intracranial pressure (headache, vomiting) soon after commencement of tPA strongly suggests a hemorrhagic complication. The elevated blood pressure further increases the risk of bleeding. It is essential to act immediately to prevent further hemorrhage.",
        "diagnostic_approach": "In suspected hemorrhagic transformation post-tPA, the immediate step is to stop the tPA infusion to prevent additional thrombolysis and ongoing bleeding. This is then followed by emergent neuroimaging\u2014typically a noncontrast CT scan\u2014to confirm the presence and extent of intracerebral hemorrhage. Differential diagnoses might include reperfusion injury or a stroke progression, but the clinical picture here is most consistent with hemorrhage.",
        "classification_and_neurology": "Brainstem strokes are classified based on vascular territory and clinical syndrome. The lateral medullary syndrome (Wallenberg syndrome) is a classic brainstem stroke syndrome involving the posterior inferior cerebellar artery territory. The classification of brainstem strokes includes medial versus lateral syndromes at each brainstem level (midbrain, pons, medulla) and is based on the anatomical structures involved. This nosology helps clinicians predict clinical signs and plan management. The current consensus in cerebrovascular neurology emphasizes syndromic classification supported by neuroimaging, allowing precise localization and prognostication.",
        "classification_and_nosology": "This scenario pertains to an adverse effect of IV tPA, specifically symptomatic intracerebral hemorrhage (sICH), which is a known complication. It is classified as a hemorrhagic transformation of an ischemic stroke induced by thrombolytic therapy.",
        "management_principles": "Immediate management involves: 1) Stopping the tPA infusion to prevent further bleeding, 2) Urgently obtaining a noncontrast CT scan to confirm hemorrhage, 3) If hemorrhage is confirmed, initiating measures to reverse the fibrinolytic state (commonly via administration of cryoprecipitate or antifibrinolytics) and controlling blood pressure. Guidelines recommend rapidly discontinuing tPA when intracranial hemorrhage is suspected. In pregnant or lactating patients, while imaging (CT scan) is still indicated, appropriate shielding and risk/benefit discussion should be undertaken.",
        "option_analysis": "\u2022 Option A (Brain CT): Although CT imaging is essential, it is not the very first step because the tPA infusion must be halted immediately to avoid further bleeding. \\n\u2022 Option B (Stop tPA): This is correct since the immediate cessation of thrombolytic therapy is the highest priority upon suspicion of hemorrhage. \\n\u2022 Option C (IV Labetalol): While blood pressure control is important, using antihypertensives before stopping tPA does not address the ongoing thrombolytic effect. \\n\u2022 Option D (Close observation): Observation is insufficient given the high risk of a life\u2010threatening hemorrhage; immediate intervention is required.",
        "clinical_pearls": "\u2022 Any neurological deterioration or signs of raised intracranial pressure during tPA infusion should prompt immediate discontinuation of the drug. \\n\u2022 Elevated BP and symptoms such as headache and vomiting in this setting are highly suspicious for intracerebral hemorrhage.",
        "current_evidence": "Recent American Heart Association/American Stroke Association guidelines stress the importance of rapid recognition and management of tPA-induced hemorrhagic complications. Immediate cessation of tPA is universally recommended, followed by urgent neuroimaging to verify the diagnosis and allow for timely intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_3.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993184",
    "fields": {
      "question_number": "173",
      "question_text": "They brought the same scenario in question 28, but they added that: symptoms start to improve, she became following the commands but still has mild weakness and dysarthria. Next step?",
      "options": {
        "A": "IV tPA",
        "B": "Brain CTA",
        "C": "Thrombectomy",
        "D": "Dual antiplatelets"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke management, the severity of deficits is critical in guiding therapy. Patients with minor, non\u2010disabling deficits (e.g., mild weakness and dysarthria) who show early improvement are usually managed with secondary prevention measures rather than aggressive reperfusion therapies.",
        "pathophysiology": "The patient\u2019s initial ischemic insult likely led to a partially occluded vessel. Spontaneous reperfusion can occur, resulting in early clinical improvement. However, there remains residual ischemic injury causing mild deficits. The pathophysiologic basis of most minor strokes involves small clot propagation or embolization with limited infarct core.",
        "clinical_correlation": "An improving neurological exam (following commands, residual dysarthria, and mild weakness) suggests that the major ischemic core is potentially limited and the penumbra has been salvaged. This clinical picture classifies her presentation as a minor stroke rather than a severe event that would warrant advanced recanalization imaging or interventions.",
        "diagnostic_approach": "The initial workup in stroke always includes a noncontrast CT to rule out hemorrhage. In patients with severe deficits and suspected large vessel occlusion, CTA plays an essential role. However, in minor strokes with clinical improvement, extensive vascular imaging (like CTA) may not alter immediate management. Differential diagnoses include transient ischemic attack (if symptoms resolve completely), stroke mimics (seizure, migraine, hypoglycemia), or progressive lacunar infarcts, and these are differentiated through detailed history, exam, and imaging.",
        "classification_and_neurology": "AIS falls under the broader category of cerebrovascular diseases and is classified etiologically using systems such as the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification. TOAST categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This classification aids in guiding secondary prevention. The management of AIS also follows time-based classifications: hyperacute (within 6 hours), acute (up to 24 hours), and subacute phases. Treatment decisions, especially regarding reperfusion therapies, depend on timing, clinical status, and imaging findings. The evolution of stroke classification systems reflects advances in neuroimaging and understanding of stroke mechanisms. Contemporary guidelines emphasize individualized assessment integrating clinical and radiological data rather than rigid categories alone. Controversies remain regarding optimal management of minor strokes and transient ischemic attacks (TIAs), highlighting the importance of nuanced classification.",
        "classification_and_nosology": "This case is classified as an ischemic stroke with minor, non\u2010disabling symptoms. Current stroke guidelines delineate strokes based on severity (minor vs. major) and the presence or absence of large vessel occlusion.",
        "management_principles": "For minor strokes with non\u2010disabling deficits, the current guidelines recommend initiation of antithrombotic therapy for secondary stroke prevention. A tiered approach is used: first\u2010line therapy is dual antiplatelet therapy (typically aspirin plus clopidogrel) initiated within 24 hours of symptom onset for a short duration (usually 21 to 90 days) based on trials such as CHANCE and POINT. Pregnancy and lactation considerations: Low\u2010dose aspirin is generally considered safe during pregnancy and lactation, though clopidogrel is used with caution and typically avoided in pregnancy unless clearly indicated.",
        "option_analysis": "A: IV tPA \u2013 Not indicated here since the patient has already shown improvement and the deficits are minor; tPA\u2019s risk\u2010benefit ratio does not favor its use in minor, non-disabling deficits. B: Brain CTA \u2013 Although vascular imaging is useful in patients suspected of large vessel occlusion, in the context of minor deficits with improvement, CTA is unlikely to change management. C: Thrombectomy \u2013 Reserved for patients with large vessel occlusions and significant deficits, not for minor strokes. D: Dual antiplatelets \u2013 Correct because secondary prevention with dual antiplatelet therapy is the current guideline-recommended approach for minor stroke patients.",
        "clinical_pearls": "1) Rapid clinical improvement in stroke does not eliminate the risk of subsequent events; secondary prevention is mandatory. 2) Reperfusion therapies (IV tPA and thrombectomy) are generally reserved for patients with disabling deficits. 3) Dual antiplatelet therapy has been shown to reduce the risk of early recurrent stroke in patients with minor non\u2010disabling ischemic stroke.",
        "current_evidence": "Recent large-scale trials (e.g., CHANCE and POINT) have confirmed that short-term dual antiplatelet therapy reduces the risk of recurrent stroke in patients with minor stroke or TIA. Contemporary guidelines support conservative management (antiplatelet therapy) in patients who demonstrate early neurological improvement rather than escalating to advanced imaging like CTA that is geared towards interventional decision-making."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993185",
    "fields": {
      "question_number": "174",
      "question_text": "82 years old female, DM/HTN/DLP. Presented with sudden left gaze preference, aphasia, dense right hemiplegia. Her basic labs and INR are fine. She has no contraindications for tPA. Brain CT attached (normal). What is next? NB: time from symptoms onset to ER arrival was 30 minutes.",
      "options": {
        "A": "IV tPA",
        "B": "Brain CTA",
        "C": "Thrombectomy",
        "D": "Dual antiplatelets"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke is often diagnosed using a combination of clinical evaluation and imaging. In patients within the therapeutic window (typically within 4.5 hours), IV thrombolysis (tPA) remains the mainstay treatment if no contraindications exist.",
        "pathophysiology": "The occlusion of a cerebral artery leads to a cascade of ischemia, resulting in neuronal injury. In this case, the dense right hemiplegia, aphasia, and left gaze preference suggest a left hemispheric large vessel occlusion. The CT is normal because early ischemic changes might not be visible immediately.",
        "clinical_correlation": "The patient exhibits classical signs of a left middle cerebral artery (MCA) stroke: right hemiplegia, expressive/receptive aphasia, and gaze deviation. The absence of hemorrhage on CT and the clear time window (30 minutes from symptom onset) support the use of IV tPA.",
        "diagnostic_approach": "The initial evaluation involves a rapid noncontrast CT scan to rule out hemorrhage. Differential diagnoses include stroke mimics (e.g., seizure, migraine, hypoglycemia) and hemorrhagic stroke. In this situation, the clinical exam in conjunction with imaging confirms an ischemic stroke.",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology, vascular territory, and clinical syndrome. The TOAST classification categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This patient likely has a large artery atherosclerotic or embolic stroke affecting the left MCA territory. The classification informs secondary prevention strategies but does not delay acute treatment. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify acute ischemic stroke based on timing and eligibility for reperfusion therapies. This patient fits the category of acute ischemic stroke within the therapeutic window for intravenous thrombolysis. Understanding these classifications helps tailor management and prognostication.",
        "classification_and_nosology": "This patient is classified as having an acute ischemic stroke. Strokes are typically subdivided into thrombotic, embolic, and lacunar subtypes. Given her clinical presentation and risk factors, a thromboembolic mechanism is highly likely.",
        "management_principles": "For eligible patients within 4.5 hours from symptom onset and without contraindications, IV tPA is the first-line therapy. This patient fits those criteria. In addition to thrombolysis, attention should be given to secondary prevention, including antiplatelet therapy, statin therapy, and risk factor modification. Pregnancy and lactation considerations are not applicable in this 82-year-old patient; however, in pregnant patients, IV tPA has been used cautiously when benefits outweigh risks and in the absence of contraindications.",
        "option_analysis": "A: IV tPA \u2013 Correct, as the patient is within the time window, has no contraindications and a normal CT ruling out hemorrhage. B: Brain CTA \u2013 While useful in assessing for large vessel occlusion, the primary next step is thrombolysis given her eligibility. C: Thrombectomy \u2013 Reserved for patients with large vessel occlusion who have significant deficits; although it may be considered if CTA shows a treatable occlusion, IV tPA is first-line here. D: Dual antiplatelets \u2013 Secondary prevention is important, but the immediate priority in this acute setting is reperfusion with IV tPA.",
        "clinical_pearls": "1) In acute ischemic stroke, time is critical; administering IV tPA within the window significantly improves outcomes. 2) A normal CT does not rule out ischemia; early ischemic changes may take time to appear. 3) Always rule out contraindications before thrombolytic therapy.",
        "current_evidence": "Landmark trials such as NINDS and ECASS III have validated the efficacy of IV tPA in acute ischemic stroke when administered within 4.5 hours of symptom onset. Current American Heart Association/American Stroke Association guidelines continue to support this management strategy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_3.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993186",
    "fields": {
      "question_number": "175",
      "question_text": "Elderly female with sudden onset of left gaze preference. She is DM/HTN/DLP. On examination she has persisted left sided gaze preference that couldn't be overcome. What else you might find in her examination?",
      "options": {
        "A": "Rt LMN Facial palsy",
        "B": "Lt LMN Facial palsy",
        "C": "Rt UMN Facial palsy",
        "D": "Lt UMN Facial palsy"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Conjugate gaze deviation is a common finding in cortical strokes involving the frontal eye field. In such strokes, the eyes deviate toward the side of the lesion due to loss of contralateral gaze control.",
        "pathophysiology": "The frontal eye field is responsible for directing the eyes contralaterally. When there is an acute infarct (often in the territory of the middle cerebral artery), the loss of inhibitory input causes the eyes to deviate toward the side of the lesion. Moreover, due to the crossing of the corticobulbar pathways, the contralateral lower face exhibits an upper motor neuron (UMN) pattern of weakness.",
        "clinical_correlation": "In this elderly female patient with vascular risk factors, a persistent left gaze preference suggests a left hemispheric cortical involvement. As a result, the right-sided lower facial weakness (UMN type) would be expected. This aligns with the classical neurological examination findings in an MCA distribution stroke.",
        "diagnostic_approach": "The evaluation includes detailed neurological examination and neuroimaging. Differential diagnoses to consider include brainstem lesions, which can also cause gaze abnormalities but typically present with additional cranial nerve deficits, and peripheral facial nerve palsies, which present with lower motor neuron (LMN) patterns.",
        "classification_and_neurology": "This clinical scenario falls within the classification of ischemic stroke under cerebrovascular diseases. According to the TOAST classification, strokes are categorized based on etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. The described presentation is most consistent with a large artery atherosclerotic stroke in the MCA territory. The gaze preference and facial palsy help localize the lesion anatomically rather than etiologically. The classification of facial palsy distinguishes UMN lesions (supranuclear) from LMN lesions (nuclear or infranuclear). This distinction is critical for clinical localization. Current stroke classification systems emphasize clinical syndromes combined with imaging and vascular studies.",
        "classification_and_nosology": "This represents an ischemic cerebrovascular accident affecting the left hemisphere, likely in the MCA territory. Strokes are classified based on location (cortical vs. subcortical) and mechanism (embolic, thrombotic, lacunar).",
        "management_principles": "Management of ischemic strokes includes acute thrombolytic therapy when appropriate, followed by secondary prevention strategies including antiplatelet therapy, risk factor modification, and rehabilitation. In pregnant or lactating patients, while thrombolytic therapy is used with caution, the overall management principles remain similar with adjustments based on risk-benefit assessments.",
        "option_analysis": "A: Right LMN Facial palsy \u2013 Incorrect; LMN lesions affect the entire half of the face and are not typically associated with cortical strokes. B: Left LMN Facial palsy \u2013 Incorrect for the same reason and does not correlate with the side of the lesion. C: Right UMN Facial palsy \u2013 Correct; in a left hemispheric stroke, the contralateral (right) lower facial weakness due to an upper motor neuron lesion is the typical finding. D: Left UMN Facial palsy \u2013 Incorrect as this would imply a right hemispheric lesion, conflicting with the left gaze deviation.",
        "clinical_pearls": "1) In cortical strokes, gaze deviation is typically toward the side of the lesion. 2) UMN facial weakness spares the forehead due to bilateral cortical innervation. 3) A careful neuro exam correlates well with the affected vascular territory.",
        "current_evidence": "Recent studies and guideline recommendations continue to emphasize the importance of correlating clinical findings with imaging to accurately localize strokes. The pattern of gaze preference combined with contralateral UMN facial weakness is a classic and still widely taught sign in acute stroke assessment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993188",
    "fields": {
      "question_number": "271",
      "question_text": "What you can see with RCVS",
      "options": {
        "A": "Low glucose"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Reversible Cerebral Vasoconstriction Syndrome (RCVS) is characterized by sudden, severe (\u201cthunderclap\u201d) headaches and reversible segmental narrowing of cerebral arteries. Recognizing its typical imaging findings is crucial for diagnosis.",
        "pathophysiology": "RCVS reflects transient dysregulation of cerebrovascular tone, often triggered by vasoactive substances, the postpartum state, or certain medications. The fluctuating vasospasm produces a characteristic pattern of multifocal arterial narrowing that reverses over time.",
        "clinical_correlation": "Patients with RCVS typically present with sudden-onset, severe headaches. Some may develop focal neurologic deficits or experience seizures. Importantly, imaging often reveals the hallmark multifocal and segmental narrowing of cerebral vessels.",
        "diagnostic_approach": "Diagnosis relies on neuroimaging. Magnetic resonance angiography (MRA), computed tomography angiography (CTA), or digital subtraction angiography (DSA) typically reveal a \u2018string-of-beads\u2019 appearance due to alternating constriction and dilation. Differential diagnoses include aneurysmal subarachnoid hemorrhage, primary angiitis of the central nervous system, and cerebral vasculitis.",
        "classification_and_neurology": "RCVS is classified under non-inflammatory cerebral vasculopathies and is part of the broader group of transient vasospastic disorders. It is distinct from primary angiitis of the central nervous system (PACNS), which is an inflammatory vasculitis.  The diagnosis is based on clinical and radiographic criteria, such as the RCVS2 score, which integrates clinical features and angiographic findings to differentiate RCVS from CNS vasculitis.  Historically, RCVS was often confused with PACNS, leading to inappropriate immunosuppressive treatment. Advances in imaging and clinical characterization have led to consensus criteria distinguishing these entities. The International Classification of Headache Disorders (ICHD-3) recognizes thunderclap headache attributed to RCVS as a distinct headache disorder.  Controversies remain regarding overlap syndromes and the relationship between RCVS and PRES, as well as their shared pathophysiological mechanisms.",
        "classification_and_nosology": "RCVS is considered a primary headache syndrome with vascular involvement. It is differentiated from inflammatory vasculitides by its reversibility and lack of significant inflammatory markers in cerebrospinal fluid analysis.",
        "management_principles": "Management is predominantly supportive. First\u2010line treatment includes removal of any offending agents and symptomatic management. Calcium channel blockers (such as nimodipine or verapamil) may be used to alleviate vasoconstriction. In pregnant or lactating patients, careful drug selection is essential; for example, although many calcium channel blockers are category C, they may be used if the benefits outweigh the potential risks.",
        "option_analysis": "Option A (Low glucose) is not a feature of RCVS and does not reflect the underlying vascular abnormality. Although the other options were not explicitly provided, the correct answer should highlight the reversible vasoconstrictive changes seen on imaging \u2013 corresponding to Option B.",
        "clinical_pearls": "1. RCVS is most commonly identified by its thunderclap headache and reversible, multifocal segmental vasoconstriction on angiographic studies. 2. It is important not to confuse RCVS with primary vasculitis, as the treatment strategies differ markedly.",
        "current_evidence": "Recent research emphasizes early and accurate imaging to differentiate RCVS from other cerebral vasculopathies. Updated guidelines advocate for supportive management with avoidance of triggers, reinforcing that abnormal glucose levels are not a feature of this condition."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  }
]

# Import MCQs
with transaction.atomic():
    imported = 0
    for mcq_data in fixture_data:
        try:
            # Create MCQ from fixture data
            model_name = mcq_data['model']
            if model_name != 'mcq.mcq':
                continue
                
            # Get fields
            fields = mcq_data['fields']
            mcq_id = mcq_data['pk']
            
            # Create or update the MCQ
            mcq, created = MCQ.objects.update_or_create(
                id=mcq_id,
                defaults=fields
            )
            
            imported += 1
        except Exception as e:
            print(f"Error importing MCQ: {e}")
    
    print(f"Successfully imported {imported} MCQs")
