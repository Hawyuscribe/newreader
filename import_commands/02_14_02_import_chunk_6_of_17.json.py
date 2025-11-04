
# Import batch 2 of 3 from chunk_6_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993163",
    "fields": {
      "question_number": "152",
      "question_text": "Elderly female brought to ER with \u2193 level of consciousness. Unknown history. Her labs showed INR of 3. Brain CT attached. What is the best next step?",
      "options": {
        "A": "vitamin K",
        "B": "PCC",
        "C": "idarucizumab",
        "D": "FFP"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In patients with intracranial hemorrhage associated with anticoagulation therapy, immediate reversal of the coagulopathy is the primary goal. Elevated INR suggests a warfarin-related bleed, and prompt reversal is imperative.",
        "pathophysiology": "Warfarin acts by inhibiting vitamin K-dependent clotting factors (II, VII, IX, and X). An elevated INR indicates that the clotting cascade is impaired, thereby predisposing to bleeding. Prothrombin complex concentrate (PCC) rapidly supplies the deficient clotting factors, offering faster normalization of coagulation compared to vitamin K alone.",
        "clinical_correlation": "The elderly female with a decreased level of consciousness, an INR of 3, and a brain CT revealing hemorrhage is most consistent with warfarin-associated intracranial hemorrhage. In such emergencies, immediate correction of the INR is crucial to prevent hematoma expansion and further neurological decline.",
        "diagnostic_approach": "Diagnosing warfarin-associated intracranial hemorrhage involves a combination of clinical evaluation and imaging studies. Differential diagnoses include hemorrhage from other causes such as amyloid angiopathy or traumatic brain injury. A careful review of the medication history and laboratory values (INR) is essential.",
        "classification_and_neurology": "Intracerebral hemorrhage is classified within hemorrhagic strokes, distinct from ischemic strokes. The classification systems, such as the American Heart Association/American Stroke Association (AHA/ASA) guidelines, categorize ICH by etiology (hypertensive, amyloid angiopathy, anticoagulant-associated), location (lobar, deep, brainstem, cerebellar), and severity. Anticoagulant-associated ICH is a recognized subtype with specific management protocols. The classification has evolved to emphasize etiology-driven treatment approaches. Nosologically, this condition belongs to the cerebrovascular disease family, specifically hemorrhagic stroke, and is further subclassified by precipitating factors (e.g., anticoagulation). Controversies exist regarding the best reversal agent and timing, but consensus supports rapid correction of coagulopathy in anticoagulant-related ICH.",
        "classification_and_nosology": "This condition falls under anticoagulant-associated intracranial hemorrhage. It is categorized based on the underlying etiology (warfarin-induced) rather than based solely on the location or size of the hemorrhage.",
        "management_principles": "The first-line management in warfarin-related ICH involves rapid reversal of anticoagulation. The current guidelines favor four-factor prothrombin complex concentrate (PCC) due to its rapid onset of action. Vitamin K (typically 10 mg IV) should be administered concurrently to ensure sustained reversal, as its effect takes several hours. Although Fresh Frozen Plasma (FFP) is an option, it is generally less preferred because of slower correction, risk of volume overload, and preparation delays. In pregnancy or lactation, vitamin K is considered safe; however, the use of PCC should be carefully weighed as data are more limited in these populations, though the life\u2010threatening nature of hemorrhage necessitates rapid intervention.",
        "option_analysis": "Option A (vitamin K) is important but inadequate as a monotherapy in an emergency because its effect is delayed. Option B (PCC) is correct because it rapidly corrects the coagulopathy, which is critical in the setting of intracranial hemorrhage. Option C (idarucizumab) is an antidote for dabigatran, not warfarin. Option D (FFP) is a viable alternative but is less favored compared to PCC in terms of speed and efficacy.",
        "clinical_pearls": "1) In warfarin-associated ICH, rapid reversal of anticoagulation is critical; PCC is preferred over FFP due to its speed and efficiency. 2) Always administer vitamin K alongside PCC to maintain reversal of coagulopathy. 3) Always consider the type of anticoagulant when selecting the reversal agent (e.g., idarucizumab is specific for dabigatran).",
        "current_evidence": "Recent guidelines and studies from stroke and neurocritical care societies emphasize the urgent use of four-factor PCC for the management of warfarin-associated intracranial hemorrhage. Ongoing research continues to refine protocols to minimize hematoma expansion and improve outcomes, with a growing body of evidence supporting PCC over FFP due to faster and more reliable correction of INR."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993164",
    "fields": {
      "question_number": "153",
      "question_text": "57 years old male, DM, HTN, DLP, smoker, admitted under stroke with left sided weakness and facial asymmetry. Brain CT: right capsular infarction. Brain CTA: significant intracranial ICA stenosis. What is the best management?",
      "options": {
        "A": "medical therapy",
        "B": "ICA stenting",
        "C": "ICA endarterectomy",
        "D": "craniotomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case focuses on a patient with an acute ischemic stroke secondary to intracranial atherosclerotic disease. Intracranial ICA stenosis (as opposed to extracranial disease) is best managed medically rather than with surgical or endovascular interventions.",
        "pathophysiology": "Risk factors such as diabetes, hypertension, dyslipidemia, and smoking contribute to atherosclerotic plaque formation within the intracranial vessels. The plaque can narrow the lumen of the artery, reducing cerebral blood flow and leading to infarction, as seen in the right capsular region in this patient.",
        "clinical_correlation": "The patient\u2019s presentation with left\u2010sided weakness and facial asymmetry correlates with an infarction in the right basal ganglia/capsular region. The brain CT confirms an established infarct while the CTA reveals significant stenosis of the intracranial ICA, which is the likely culprit lesion.",
        "diagnostic_approach": "Standard evaluation includes non\u2010contrast CT to rule out hemorrhage and CT angiography (CTA) to visualize the vascular anatomy. Differential diagnoses include small vessel lacunar infarcts due to chronic hypertension versus embolic strokes from other sources; however, the CTA findings of significant focal stenosis point to a large vessel etiology.",
        "classification_and_neurology": "Intracranial ICA stenosis falls under the broader category of intracranial large artery atherosclerosis, classified within ischemic stroke subtypes by the Trial of Org 10172 in Acute Stroke Treatment (TOAST) criteria as 'large artery atherosclerosis.' This classification distinguishes it from cardioembolic, small vessel (lacunar), and other stroke etiologies. Intracranial stenosis differs from extracranial carotid artery disease anatomically and pathophysiologically, with distinct therapeutic implications. The classification has evolved with advanced imaging allowing precise localization of stenosis, emphasizing the need for targeted therapy.",
        "classification_and_nosology": "Intracranial atherosclerotic disease is classified separately from extracranial carotid stenosis. For extracranial carotid disease, carotid endarterectomy or stenting may be options; for intracranial lesions, aggressive medical management is the cornerstone of treatment.",
        "management_principles": "According to current guidelines (e.g., SAMMPRIS trial), the first\u2010line management for patients with intracranial stenosis is aggressive medical therapy. This includes antiplatelet therapy (often dual therapy initially), high\u2010dose statins, and rigorous risk factor modification (blood pressure control, glycemic control, lipid management, smoking cessation). In pregnancy and lactation, medications must be chosen carefully \u2013 for instance, aspirin and certain statins have specific guidelines regarding use; risk\u2013benefit assessments are crucial when managing cardiovascular risk factors in pregnant or breastfeeding patients.",
        "option_analysis": "A: Medical therapy \u2013 Correct. B: ICA stenting \u2013 Typically considered for extracranial lesions and has a high periprocedural risk in intracranial disease. C: ICA endarterectomy \u2013 Also reserved for extracranial carotid stenosis. D: Craniotomy \u2013 Not indicated for ischemic stroke due to atherosclerotic disease.",
        "clinical_pearls": "1. Intracranial atherosclerotic disease is managed conservatively with aggressive medical therapy. 2. Risk factor modification is essential to prevent recurrence. 3. Interventional approaches are generally reserved for refractory cases.",
        "current_evidence": "Recent trials (SAMMPRIS and VISSIT) have demonstrated that optimal medical therapy is superior to interventional procedures in patients with intracranial atherosclerotic disease. Guidelines continue to emphasize intensive control of vascular risk factors and the use of antiplatelet/antithrombotic therapy as the mainstay of treatment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993165",
    "fields": {
      "question_number": "154",
      "question_text": "36 years old female referred to neurology clinic for issues with forgetting the events. She has chronic migraine headache and had suffered stroke in the past. Her father died at age of 65 with dementia. Brain MRI: subcortical WM changes likely microvascular lacunes. DX?",
      "options": {
        "A": "Moyamoya",
        "B": "MELAS",
        "C": "CADASIL",
        "D": "Susac disease"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case focuses on a patient with an acute ischemic stroke secondary to intracranial atherosclerotic disease. Intracranial ICA stenosis (as opposed to extracranial disease) is best managed medically rather than with surgical or endovascular interventions.",
        "pathophysiology": "Risk factors such as diabetes, hypertension, dyslipidemia, and smoking contribute to atherosclerotic plaque formation within the intracranial vessels. The plaque can narrow the lumen of the artery, reducing cerebral blood flow and leading to infarction, as seen in the right capsular region in this patient.",
        "clinical_correlation": "The patient\u2019s presentation with left\u2010sided weakness and facial asymmetry correlates with an infarction in the right basal ganglia/capsular region. The brain CT confirms an established infarct while the CTA reveals significant stenosis of the intracranial ICA, which is the likely culprit lesion.",
        "diagnostic_approach": "Standard evaluation includes non\u2010contrast CT to rule out hemorrhage and CT angiography (CTA) to visualize the vascular anatomy. Differential diagnoses include small vessel lacunar infarcts due to chronic hypertension versus embolic strokes from other sources; however, the CTA findings of significant focal stenosis point to a large vessel etiology.",
        "classification_and_neurology": "CADASIL is classified under hereditary small vessel diseases of the brain, specifically as a monogenic arteriopathy caused by NOTCH3 mutations. It belongs to the broader category of cerebral small vessel diseases (CSVD), which include both sporadic and hereditary forms. The sporadic forms are often related to vascular risk factors like hypertension and aging, whereas hereditary forms include CADASIL, CARASIL, and COL4A1-related angiopathies. The diagnosis of CADASIL falls within the domain of genetic cerebrovascular disorders. Nosologically, CADASIL is distinct from mitochondrial diseases (like MELAS), inflammatory vasculopathies (like Susac syndrome), and large vessel occlusive diseases (like Moyamoya). Classification systems have evolved from purely clinical to include genetic and imaging criteria, emphasizing the importance of molecular diagnosis. There is consensus that CADASIL is the most common hereditary CSVD, with well-defined genetic and clinical diagnostic criteria.",
        "classification_and_nosology": "Intracranial atherosclerotic disease is classified separately from extracranial carotid stenosis. For extracranial carotid disease, carotid endarterectomy or stenting may be options; for intracranial lesions, aggressive medical management is the cornerstone of treatment.",
        "management_principles": "According to current guidelines (e.g., SAMMPRIS trial), the first\u2010line management for patients with intracranial stenosis is aggressive medical therapy. This includes antiplatelet therapy (often dual therapy initially), high\u2010dose statins, and rigorous risk factor modification (blood pressure control, glycemic control, lipid management, smoking cessation). In pregnancy and lactation, medications must be chosen carefully \u2013 for instance, aspirin and certain statins have specific guidelines regarding use; risk\u2013benefit assessments are crucial when managing cardiovascular risk factors in pregnant or breastfeeding patients.",
        "option_analysis": "A: Medical therapy \u2013 Correct. B: ICA stenting \u2013 Typically considered for extracranial lesions and has a high periprocedural risk in intracranial disease. C: ICA endarterectomy \u2013 Also reserved for extracranial carotid stenosis. D: Craniotomy \u2013 Not indicated for ischemic stroke due to atherosclerotic disease.",
        "clinical_pearls": "1. Intracranial atherosclerotic disease is managed conservatively with aggressive medical therapy. 2. Risk factor modification is essential to prevent recurrence. 3. Interventional approaches are generally reserved for refractory cases.",
        "current_evidence": "Recent trials (SAMMPRIS and VISSIT) have demonstrated that optimal medical therapy is superior to interventional procedures in patients with intracranial atherosclerotic disease. Guidelines continue to emphasize intensive control of vascular risk factors and the use of antiplatelet/antithrombotic therapy as the mainstay of treatment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993166",
    "fields": {
      "question_number": "155",
      "question_text": "Case scenario of patient admitted with subarachnoid hemorrhage. After 2 days he was lethargic, BP 104/52, serum Na 123, \u2191 urine Na and urine osmolality. What is the best next step in management?",
      "options": {
        "A": "fluid restriction",
        "B": "fluid hydration",
        "C": "mannitol",
        "D": "oral Na tablet"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case focuses on a patient with an acute ischemic stroke secondary to intracranial atherosclerotic disease. Intracranial ICA stenosis (as opposed to extracranial disease) is best managed medically rather than with surgical or endovascular interventions.",
        "pathophysiology": "Risk factors such as diabetes, hypertension, dyslipidemia, and smoking contribute to atherosclerotic plaque formation within the intracranial vessels. The plaque can narrow the lumen of the artery, reducing cerebral blood flow and leading to infarction, as seen in the right capsular region in this patient.",
        "clinical_correlation": "The patient\u2019s presentation with left\u2010sided weakness and facial asymmetry correlates with an infarction in the right basal ganglia/capsular region. The brain CT confirms an established infarct while the CTA reveals significant stenosis of the intracranial ICA, which is the likely culprit lesion.",
        "diagnostic_approach": "Standard evaluation includes non\u2010contrast CT to rule out hemorrhage and CT angiography (CTA) to visualize the vascular anatomy. Differential diagnoses include small vessel lacunar infarcts due to chronic hypertension versus embolic strokes from other sources; however, the CTA findings of significant focal stenosis point to a large vessel etiology.",
        "classification_and_neurology": "Hyponatremia in neurology is classified based on volume status and etiology. The major categories relevant here are: - Hypovolemic hyponatremia (e.g., CSW) - Euvolemic hyponatremia (e.g., SIADH) - Hypervolemic hyponatremia (e.g., heart failure, cirrhosis) The distinction between SIADH and CSW has been debated, but current consensus favors recognizing CSW as a distinct entity, especially in neurosurgical and neurocritical care contexts. The International Classification of Disorders (ICD-11) and neurology textbooks now acknowledge CSW under hypovolemic hyponatremia related to central nervous system pathology. This classification aids in guiding treatment strategies. Controversies remain regarding diagnostic criteria and overlap between SIADH and CSW, but volume status remains the cornerstone of differentiation.",
        "classification_and_nosology": "Intracranial atherosclerotic disease is classified separately from extracranial carotid stenosis. For extracranial carotid disease, carotid endarterectomy or stenting may be options; for intracranial lesions, aggressive medical management is the cornerstone of treatment.",
        "management_principles": "According to current guidelines (e.g., SAMMPRIS trial), the first\u2010line management for patients with intracranial stenosis is aggressive medical therapy. This includes antiplatelet therapy (often dual therapy initially), high\u2010dose statins, and rigorous risk factor modification (blood pressure control, glycemic control, lipid management, smoking cessation). In pregnancy and lactation, medications must be chosen carefully \u2013 for instance, aspirin and certain statins have specific guidelines regarding use; risk\u2013benefit assessments are crucial when managing cardiovascular risk factors in pregnant or breastfeeding patients.",
        "option_analysis": "A: Medical therapy \u2013 Correct. B: ICA stenting \u2013 Typically considered for extracranial lesions and has a high periprocedural risk in intracranial disease. C: ICA endarterectomy \u2013 Also reserved for extracranial carotid stenosis. D: Craniotomy \u2013 Not indicated for ischemic stroke due to atherosclerotic disease.",
        "clinical_pearls": "1. Intracranial atherosclerotic disease is managed conservatively with aggressive medical therapy. 2. Risk factor modification is essential to prevent recurrence. 3. Interventional approaches are generally reserved for refractory cases.",
        "current_evidence": "Recent trials (SAMMPRIS and VISSIT) have demonstrated that optimal medical therapy is superior to interventional procedures in patients with intracranial atherosclerotic disease. Guidelines continue to emphasize intensive control of vascular risk factors and the use of antiplatelet/antithrombotic therapy as the mainstay of treatment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993167",
    "fields": {
      "question_number": "156",
      "question_text": "Young girl with congenital heart disease presented with fever and right sided weakness. She has signs of stroke on examination. What is the best diagnostic test?",
      "options": {
        "A": "Blood culture",
        "B": "Brain CT",
        "C": "Contrasted brain CT",
        "D": "LP"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In an acute stroke scenario, rapid neuroimaging is critical. A noncontrast CT scan is the standard initial test to rapidly differentiate between ischemic and hemorrhagic stroke, which is essential for guiding emergent management. In a young patient with congenital heart disease and fever, septic embolism from possible infective endocarditis is a concern, but the immediate priority is to evaluate the brain for stroke.",
        "pathophysiology": "Patients with congenital heart disease are at increased risk for infective endocarditis. Vegetations on the valves can embolize, causing septic emboli that lead to ischemic infarcts (and sometimes hemorrhagic conversion) in the brain. Identification of such infarcts is best achieved initially through brain imaging.",
        "clinical_correlation": "The patient\u2019s presentation with fever and right-sided weakness suggests an embolic stroke, potentially from infective endocarditis. While the fever urges evaluation for an infectious source (with blood cultures and echocardiography), the neurological deficits require immediate brain imaging to determine the nature of the stroke.",
        "diagnostic_approach": "The initial evaluation of stroke involves a noncontrast CT scan of the brain to rapidly rule out hemorrhage and confirm ischemic stroke. Differential diagnoses include septic embolic stroke, primary hemorrhagic stroke, brain abscess, and other central nervous system infections. Blood cultures, while crucial for diagnosing infective endocarditis, do not address the immediate need to characterize the stroke.",
        "classification_and_neurology": "Stroke is classified broadly into ischemic and hemorrhagic types. Ischemic strokes are further subclassified by etiology using systems like the TOAST classification: large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. In this case, cardioembolic stroke due to congenital heart disease fits into the cardioembolism category. Infective endocarditis-related strokes represent a subset of cardioembolic strokes with infectious etiology. Hemorrhagic strokes include intracerebral hemorrhage and subarachnoid hemorrhage. Classification systems have evolved to incorporate imaging findings and etiological factors to guide treatment. The current consensus emphasizes rapid imaging to classify stroke type as the first diagnostic step in acute stroke management.",
        "classification_and_nosology": "Stroke is broadly classified into ischemic and hemorrhagic types. In cases of infective endocarditis-induced septic emboli, ischemic infarcts are common, though hemorrhagic conversion can occur. The clinical scenario here fits into the stroke spectrum associated with embolic phenomena from endocarditis.",
        "management_principles": "According to current stroke guidelines, the rapid assessment of stroke via a noncontrast brain CT scan is paramount to determine therapeutic options, including potential thrombolysis. In cases where infective endocarditis is suspected, adjunctive tests such as blood cultures and echocardiography are performed subsequently. In pregnancy or lactation, noncontrast CT can be performed with appropriate fetal shielding, as it minimizes radiation exposure and is still considered the imaging modality of choice in the acute setting.",
        "option_analysis": "Option A (Blood culture) is critical for diagnosing the underlying infective cause but is not the best test to evaluate acute neurological deficits. Option D (Lumbar puncture) is contraindicated in the setting of stroke due to the risk of herniation if intracranial pressure is elevated. Option C (Contrasted brain CT) is not the first-line imaging modality since the use of contrast can obscure the distinction between hemorrhage and ischemic areas in the acute stroke setting. Option B (Brain CT), understood as noncontrast CT, is the appropriate and immediate test for stroke evaluation.",
        "clinical_pearls": "\u2022 In the acute evaluation of stroke, always prioritize a noncontrast head CT to differentiate hemorrhagic from ischemic stroke quickly. \u2022 In patients with congenital heart disease presenting with fever and stroke signs, septic emboli secondary to infective endocarditis should be suspected. \u2022 While blood cultures and echocardiography are essential for diagnosing infective endocarditis, they follow the urgent imaging required to manage acute neurological deficits.",
        "current_evidence": "Guidelines from the American Heart Association (AHA) and the American Stroke Association consistently recommend noncontrast CT as the first-line imaging modality in suspected stroke cases due to its speed, accessibility, and ability to reliably detect hemorrhage. Recent studies reinforce that even when infective endocarditis is in the differential, immediate brain imaging is essential for stroke management and is not altered by the need for subsequent infectious work-up."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993168",
    "fields": {
      "question_number": "157",
      "question_text": "57 years old male presented with acute onset nausea, vomiting, vertigo and unsteady gait. He is diabetic and hypertensive. His examination was evident for right sided ptosis and miosis with ataxia and tendency to fall towards right side. NOTE vessel is affected?",
      "options": {
        "A": "PICA",
        "B": "AICA",
        "C": "SCA",
        "D": "Middle cerebral artery"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case describes a patient with acute onset of nausea, vomiting, vertigo, unsteady gait, ipsilateral ptosis, and miosis. These findings are hallmark features of lateral medullary syndrome (Wallenberg syndrome), typically due to occlusion of the Posterior Inferior Cerebellar Artery (PICA). The presence of ipsilateral Horner's syndrome (ptosis and miosis) reinforces the involvement of the descending sympathetic fibers in this region.",
        "pathophysiology": "Occlusion of the PICA leads to infarction in the lateral medulla. This affects various neural structures: the vestibular nuclei (causing vertigo and nausea), the inferior cerebellar peduncle (producing ataxia and balance disturbances), and the descending sympathetic fibers (resulting in ipsilateral Horner's syndrome). Additionally, involvement of the nucleus ambiguus may lead to dysphagia and hoarseness, although these were not specified in the current case.",
        "clinical_correlation": "The clinical picture in this patient\u2014acute vertigo, nausea, vomiting, ataxia with a tendency to fall towards the affected side, and features of Horner's syndrome\u2014is highly suggestive of a PICA infarct. Differential diagnoses include lateral pontine syndrome (often due to AICA occlusion), which tends to be associated with additional features such as facial paralysis, hearing loss, and loss of facial sensation. The absence of these latter symptoms supports the diagnosis of lateral medullary syndrome.",
        "diagnostic_approach": "Diagnosis is established primarily by clinical assessment complemented by neuroimaging. MRI with diffusion-weighted imaging is the modality of choice to confirm infarction in the PICA territory. Differential diagnosis should consider ischemic events in the AICA or SCA territories. Vascular imaging (CTA, MRA, or DSA) may further delineate the involved vessel.",
        "classification_and_neurology": "This stroke falls under the classification of **ischemic strokes of the posterior circulation**, specifically within the **lateral pontine syndrome subtype**.   The widely accepted **TOAST classification** categorizes ischemic strokes based on etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined, or undetermined). Posterior circulation strokes can be further classified by vascular territory:  - **AICA territory infarcts** (lateral pontine syndrome) - **PICA territory infarcts** (lateral medullary syndrome) - **SCA territory infarcts** (superior cerebellar syndrome)  This nosology aids in clinical diagnosis, prognosis, and management decisions. Current consensus emphasizes the importance of vascular imaging to confirm the involved artery. Some controversy exists in differentiating AICA and PICA syndromes clinically due to overlapping features, but imaging clarifies diagnosis.",
        "classification_and_nosology": "This syndrome falls under posterior circulation strokes. Specifically, it is classified as lateral medullary (Wallenberg) syndrome, which is most commonly due to occlusion of the Posterior Inferior Cerebellar Artery (PICA).",
        "management_principles": "Management of acute ischemic stroke in the PICA territory involves standard stroke protocols including antiplatelet therapy, risk factor management (e.g., blood pressure, diabetes, lipids), and supportive care. Thrombolytic therapy may be considered within the appropriate time window. In pregnant or lactating patients, decisions on thrombolysis require careful risk-benefit analysis; low molecular weight heparin and aspirin remain options with proper obstetrical consultation. Early rehabilitation, especially balance and swallowing therapy, is crucial. Current guidelines emphasize multidisciplinary management to optimize recovery while minimizing complications.",
        "option_analysis": "The options provided were: A) PICA, B) AICA, C) SCA, and D) Middle Cerebral Artery. PICA is the correct answer because its infarction causes the clinical syndrome described. AICA infarcts (lateral pontine syndrome) typically include hearing loss and facial sensory deficits. SCA infarcts generally result in cerebellar symptoms without Horner's syndrome, and MCA strokes affect the cerebral hemispheres rather than the brainstem.",
        "clinical_pearls": "Ipsilateral Horner's syndrome (ptosis and miosis) in a stroke patient is a vital clue pointing towards a lateral medullary infarct. The combination of vestibular symptoms, ataxia, and autonomic dysfunction in the context of cerebrovascular risk factors like hypertension and diabetes should prompt evaluation for posterior circulation stroke.",
        "current_evidence": "Recent studies and updated stroke management guidelines underscore the importance of rapid neuroimaging and early intervention in posterior circulation strokes. Evidence supports the use of antithrombotic therapies and aggressive risk factor management. In special populations such as pregnant or lactating women, treatment guidelines recommend individualized care with attention to the safety profiles of thrombolytic agents and antiplatelet medications."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993169",
    "fields": {
      "question_number": "158",
      "question_text": "Case scenario of a patient was admitted in stroke unit, no clinical features provided but they attached his brain CT. The patient's CT is shown SCA territory infarction at level of midbrain, which artery is affected?",
      "options": {
        "A": "PICA",
        "B": "AICA",
        "C": "SCA",
        "D": "Middle cerebral artery"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests knowledge of neurovascular territories. The CT image shows an infarct in the region supplied by the Superior Cerebellar Artery (SCA), which can extend to adjacent midbrain areas. Recognizing the vascular territories on imaging is critical in stroke diagnosis.",
        "pathophysiology": "Occlusion of the SCA, which typically originates from the basilar artery just below the origin of the Posterior Cerebral Artery (PCA), leads to ischemia in its distribution \u2013 the superior aspect of the cerebellum and parts of the midbrain. The resulting infarct is due to compromised blood flow, leading to neuronal injury via energy failure and excitotoxicity.",
        "clinical_correlation": "Patients with an SCA infarct may present with symptoms such as ataxia, vertigo, dysmetria, and cranial nerve deficits affecting ocular movement if midbrain structures are involved. Even though the clinical details are not provided, CT evidence supports the involvement of the SCA territory.",
        "diagnostic_approach": "The initial evaluation of suspected stroke involves non-contrast CT imaging to differentiate between ischemic and hemorrhagic events. Further vascular imaging (like CT angiography) is used to confirm vessel occlusion. Differential diagnoses include infarctions in the territories supplied by PICA (posterior inferior cerebellar artery) and AICA (anterior inferior cerebellar artery), which affect different cerebellar regions.",
        "classification_and_neurology": "Cerebellar strokes are classified based on the arterial territory involved: SCA, AICA, and PICA infarctions constitute the three primary cerebellar stroke syndromes. This classification is part of the broader ischemic stroke taxonomy, which categorizes strokes by vascular territory and etiology (e.g., large artery atherosclerosis, cardioembolism). The TOAST classification system is commonly used for ischemic stroke subtyping but does not specify cerebellar subterritories. The SCA infarction is a subset of posterior circulation strokes, which represent approximately 20% of ischemic strokes. Nosologically, SCA strokes are distinguished from AICA and PICA strokes by their unique vascular supply and clinical features. There is consensus on these vascular territories based on angiographic and pathological studies, although overlap and collateral circulation can sometimes blur boundaries.",
        "classification_and_nosology": "Ischemic strokes are classified based on the vascular territory involved. This case falls under the posterior circulation strokes, specifically the SCA territory infarction.",
        "management_principles": "Acute management of ischemic stroke follows guidelines from bodies such as the AHA/ASA, emphasizing rapid reperfusion therapy (IV thrombolysis if within the therapeutic window) and consideration of endovascular therapy where appropriate. In pregnant patients, the risks of thrombolytic therapy must be balanced against the potential for maternal and fetal harm, though IV tPA can be considered after thorough risk\u2013benefit analysis. For lactating women, antithrombotic therapies are generally regarded as compatible with breastfeeding, but individualized evaluation is essential.",
        "option_analysis": "Option A (PICA) supplies the inferior part of the cerebellum; Option B (AICA) is involved with the lateral pons and inner ear structures; Option D (Middle cerebral artery) supplies the lateral aspects of the cerebral hemispheres. Option C (SCA) is the most appropriate given the CT findings indicating an SCA territory infarction at the midbrain level.",
        "clinical_pearls": "Understanding the unique vascular territories of the brain is vital in stroke localization. SCA occlusions, while less common than MCA territory strokes, can manifest with combined cerebellar and midbrain findings. Always integrate clinical and imaging data for accurate diagnosis.",
        "current_evidence": "Recent guidelines underscore the importance of rapid imaging and intervention in ischemic stroke. Evidence supports the use of IV thrombolysis and mechanical thrombectomy in eligible patients. Special populations such as pregnant or lactating women require modifications, including minimizing radiation exposure and carefully assessing medication risks. Current practices involve multidisciplinary collaboration for optimal outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_1.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993170",
    "fields": {
      "question_number": "159",
      "question_text": "36 years old male, sustained MVA, presented with acute blurred vision. On examination he has right homonymous hemianopia. His brain CT reported left occipital acute infarction. What could explain the stroke mechanism in his case?",
      "options": {
        "A": "Large vessel atherosclerosis",
        "B": "Artery-artery embolism",
        "C": "Cardioembolic",
        "D": "Small lacune"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case focuses on stroke mechanism in a young trauma victim. After a motor vehicle accident (MVA), the patient presents with a visual deficit that localizes to the left occipital lobe, which is supplied by the posterior cerebral artery. The clinical scenario is suggestive of an embolic event resulting from dissection caused by trauma.",
        "pathophysiology": "Trauma from an MVA can lead to dissection of cervical arteries (e.g., vertebral or internal carotid arteries). In such dissections, intimal disruption occurs, predisposing to thrombus formation. Pieces of the thrombus can then embolize (artery-to-artery embolism) to distal vessels such as the posterior cerebral artery, resulting in an infarct in the occipital region.",
        "clinical_correlation": "The patient\u2019s blurred vision and right homonymous hemianopia correlate with an occipital lobe infarct. In younger patients, and particularly after trauma, cervical artery dissection is an important etiology to consider, contrasting with more common atherosclerotic mechanisms seen in older populations.",
        "diagnostic_approach": "Initial imaging with CT can demonstrate the infarct, but further evaluation with vascular imaging (CT angiography, MR angiography, or Digital Subtraction Angiography) is critical to assess for arterial dissection. Differential considerations include cardioembolic sources, intracranial hemorrhage, or small vessel lacunar strokes, but these are less likely given the patient\u2019s age and the traumatic context.",
        "classification_and_neurology": "Ischemic strokes are classified according to the TOAST (Trial of Org 10172 in Acute Stroke Treatment) criteria into five major subtypes:  1. Large artery atherosclerosis 2. Cardioembolism 3. Small vessel occlusion (lacunar) 4. Stroke of other determined etiology 5. Stroke of undetermined etiology  This classification aids in etiological diagnosis and management. Artery-to-artery embolism falls under large artery atherosclerosis subtype but specifically refers to emboli originating from proximal large artery plaques.   The classification has evolved with advances in imaging and vascular diagnostics, allowing more precise identification of embolic sources. Although some overlap exists, the TOAST system remains the most widely used framework in clinical practice and research. Competing systems like CCS (Causative Classification of Stroke) provide automated algorithms but share similar categories.",
        "classification_and_nosology": "Stroke classification according to the TOAST criteria distinguishes among large vessel atherosclerosis, cardioembolism, small vessel occlusion, and strokes due to other determined etiologies including dissection. In this case, the mechanism fits within the artery-to-artery embolism category, commonly arising from a traumatic dissection.",
        "management_principles": "Management involves immediate antithrombotic therapy with either antiplatelet agents or anticoagulation (the choice is individualized based on recent guidelines and clinical context). For patients who are pregnant or lactating, low-molecular-weight heparin is typically preferred due to its established safety profile. Additional steps include vascular imaging for confirmation, risk factor modification, and stroke rehabilitation. In cases of dissection, long-term management and secondary stroke prevention are critical.",
        "option_analysis": "Option A (Large vessel atherosclerosis) is less likely in a 36-year-old without significant risk factors. Option C (Cardioembolic) would imply a primary cardiac source, which is not indicated here. Option D (Small lacune) is not consistent with an occipital infarct, which is usually not a lacunar distribution. Option B (Artery-artery embolism) correctly identifies the likely mechanism after a traumatic dissection leading to embolism.",
        "clinical_pearls": "\u2022 Always consider cervical artery dissection as a cause of stroke in young patients post-trauma. \u2022 The posterior cerebral artery is particularly vulnerable following embolic events from arterial dissections. \u2022 Early vascular imaging is essential for proper diagnosis. \u2022 In pregnant or lactating patients, consider LMWH for antithrombotic therapy.",
        "current_evidence": "Recent studies and guidelines underscore the importance of early recognition of arterial dissection and the use of appropriate neuroimaging techniques. Evidence supports both antiplatelet and anticoagulant therapies in the management of dissection-induced stroke, with current recommendations tailored to individual patient profiles, including adjustments for pregnancy and lactation where LMWH is preferred."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_1.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993171",
    "fields": {
      "question_number": "160",
      "question_text": "WOTF clinical features seen in superior cerebellar artery infarction?",
      "options": {
        "A": "Ipsilateral Horner",
        "B": "Ipsilateral trochlear palsy",
        "C": "Truncal Hypoalgesia",
        "D": "Ipsilateral abducens palsy"
      },
      "correct_answer": "None",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Superior cerebellar artery (SCA) infarction classically produces cerebellar dysfunction \u2013 primarily ipsilateral limb dysmetria, dysdiadochokinesia, and gait ataxia. Its territory is devoted to the coordination and motor planning aspects rather than primary sensory or isolated cranial nerve functions.",
        "pathophysiology": "Occlusion of the SCA leads to ischemia in the superior parts of the cerebellum (including parts of the cerebellar hemispheres and occasionally the superior vermis). This damage disrupts the cerebellar circuits involved in fine motor coordination. Unlike strokes affecting adjacent brainstem structures, the infarct does not typically impair pathways mediating pain perception or cranial nerve nuclei unrelated to the cerebellum.",
        "clinical_correlation": "Patients with SCA infarction present with acute cerebellar signs such as ipsilateral limb ataxia, dysmetria, loss of coordination, and sometimes nausea or vomiting. They do not usually manifest sensory deficits (e.g., hypoalgesia) or isolated cranial nerve palsies like those of the trochlear or abducens nerves.",
        "diagnostic_approach": "The diagnosis is based on clinical examination supported by neuroimaging \u2013 preferably MRI with diffusion\u2010weighted imaging (DWI) \u2013 which reveals infarction in the SCA territory. Differential diagnoses include infarctions in adjacent vascular territories such as the PICA (which may cause lateral medullary syndrome with ipsilateral Horner syndrome and contralateral pain and temperature loss) or AICA (which may also involve cranial nerve deficits like hearing loss).",
        "classification_and_neurology": "Superior cerebellar artery infarction is classified under ischemic strokes within the posterior circulation stroke category. The posterior circulation includes the vertebral arteries, basilar artery, and their branches (including the SCA, anterior inferior cerebellar artery [AICA], and posterior inferior cerebellar artery [PICA]). The TOAST classification system categorizes strokes by etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.), but the vascular territory classification is essential for clinical localization. SCA infarcts belong to the large vessel territory infarcts of the posterior circulation. Understanding this vascular taxonomy is critical for diagnosis and management. Some controversies exist regarding the overlap of clinical syndromes between SCA and AICA infarcts, but trochlear palsy remains a distinguishing feature of SCA involvement.",
        "classification_and_nosology": "SCA infarction is classified as a type of posterior circulation ischemic stroke involving the cerebellum. It is managed following the general guidelines for acute ischemic strokes but with particular attention to posterior fossa dynamics.",
        "management_principles": "Management generally involves acute stroke care, considering thrombolytic therapy if within the therapeutic window, and vigilant monitoring for complications such as mass effect or edema. In pregnant or lactating patients, decisions about thrombolysis and advanced imaging (MRI is preferred over CT when possible due to lower radiation exposure) require balancing maternal benefits and fetal risks in accordance with current guidelines (e.g., from ACOG and stroke management bodies).",
        "option_analysis": "Option A (Ipsilateral Horner syndrome) is typically associated with lateral medullary syndrome (PICA infarct) rather than SCA infarction. Option B (Ipsilateral trochlear palsy) and Option D (Ipsilateral abducens palsy) are cranial nerve deficits more commonly seen in isolated brainstem or raised intracranial pressure syndromes, not in SCA strokes. Option C (Truncal hypoalgesia) incorrectly describes a sensory deficit; SCA strokes lead to impaired coordination (such as truncal ataxia), not diminished pain sensation. Thus, none of the options accurately capture the typical clinical features of an SCA infarct.",
        "clinical_pearls": "When evaluating posterior circulation strokes, emphasis should be on motor coordination deficits (eg, ataxia, dysmetria) rather than sensory abnormalities or isolated cranial nerve palsies. Distinguishing SCA infarction from PICA or AICA strokes is essential because the latter may involve additional features such as Horner syndrome or hearing loss.",
        "current_evidence": "Recent literature and stroke management guidelines underscore the importance of early MRI imaging for posterior circulation strokes. The standard management \u2013 including consideration for thrombolysis \u2013 applies to SCA infarction, and similar principles are extended to pregnant and lactating patients with due caution to minimize fetal exposure while ensuring optimal maternal care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993172",
    "fields": {
      "question_number": "161",
      "question_text": "Long case scenario, patient admitted in stroke unit. He is diabetic, hypertensive, dyslipidemic. They didn't give specific details. Examination: left sided hemiparesis. MRI DWI attached. WOTF is the expected mechanism of his stroke?",
      "options": {
        "A": "Vasculitis",
        "B": "Cardioembolic",
        "C": "Watershed",
        "D": "Hypercoagulable state"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Watershed strokes occur in border-zone regions between two major arterial territories (e.g., between the ACA and MCA or MCA and PCA territories) where blood supply is most vulnerable to drops in perfusion. In patients with vascular risk factors such as diabetes, hypertension, and dyslipidemia, atherosclerotic narrowing and episodes of hypotension can lead to these characteristic infarcts.",
        "pathophysiology": "Due to advanced atherosclerotic changes, the distal branches of major cerebral arteries receive marginal blood flow. During periods of systemic hypotension or when there is significant carotid stenosis, these border zones are most at risk for ischemia. Recent evidence emphasizes that hemodynamic compromise rather than embolic occlusion leads to the wedge\u2010shaped infarctions seen in watershed regions.",
        "clinical_correlation": "This patient\u2019s left-sided weakness accompanied by DWI abnormalities on MRI that show a rostro\u2010caudal or wedge\u2010shaped pattern in a border zone region fits a watershed infarct. The risk factor profile further supports a mechanism based on compromised perfusion to distal vascular territories.",
        "diagnostic_approach": "Neuroimaging with MRI (especially DWI) is essential to identify the infarct pattern. Vascular imaging (carotid Doppler, CT angiography) is used to assess for carotid stenosis. Differential diagnoses include cardioembolic stroke (which generally presents with multiple cortical infarcts) and lacunar infarcts (from small vessel occlusion). The infarct distribution distinguishes watershed from these other etiologies.",
        "classification_and_neurology": "Ischemic strokes are classified etiologically by the TOAST criteria into five major categories: large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology (including vasculitis), and stroke of undetermined etiology. Watershed infarcts fall under the large artery atherosclerosis or hypoperfusion category, often related to hemodynamic compromise. Vasculitis is classified separately as an inflammatory vasculopathy. Hypercoagulable states are considered under other determined etiologies when identified. This classification aids in guiding diagnostic workup and management. Over time, classification systems have evolved to incorporate imaging patterns and molecular markers, but TOAST remains widely used clinically. Some controversies exist regarding overlap between mechanisms and mixed etiologies.",
        "classification_and_nosology": "Watershed strokes are classified as ischemic strokes occurring in border zones, separate from embolic strokes and small vessel (lacunar) infarcts. They represent a distinct entity related predominantly to hemodynamic failure.",
        "management_principles": "Acute management involves standard stroke protocols including antiplatelet therapy (e.g., aspirin \u00b1 clopidogrel in the acute phase), blood pressure stabilization, and aggressive risk factor modification. In patients with significant carotid stenosis, revascularization may be considered. For pregnant or lactating patients, low-dose aspirin is generally safe and blood pressure agents (like labetalol) can be used with fetal safety in mind.",
        "option_analysis": "\u2022 A: Vasculitis is less likely in an older patient with consistent atherosclerotic risk factors.  \u2022 B: Cardioembolic strokes typically result in cortical infarcts and are often associated with arrhythmias such as atrial fibrillation.  \u2022 C: Watershed is correct given the context of hemodynamic compromise in border zones.  \u2022 D: A hypercoagulable state is also less likely given the patient\u2019s age and risk profile.",
        "clinical_pearls": "\u2022 Watershed infarcts are located at the junctions of major arterial territories. \u2022 They are typically due to hemodynamic compromise rather than embolic phenomena. \u2022 MRI with DWI is the gold standard to identify the specific infarct pattern.",
        "current_evidence": "Recent guidelines stress the importance of advanced neuroimaging to differentiate stroke subtypes. There is also evolving evidence on the benefits of dual antiplatelet therapy in high-risk TIA and stroke prevention in patients with significant carotid stenosis."
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
