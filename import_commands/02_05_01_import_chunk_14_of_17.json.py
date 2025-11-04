
# Import batch 1 of 3 from chunk_14_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993254",
    "fields": {
      "question_number": "38",
      "question_text": "The patient with a past medical history of stroke had a full cardiac workup but was negative. He was started on Aspirin which made his chronic epistaxis worse. Picture Attached. What to do next",
      "options": {
        "A": "Lung angiography",
        "B": "C-ANCA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "In patients with a history of stroke and negative cardiac sources of embolism, the occurrence of chronic epistaxis raises suspicion for an underlying systemic vascular disorder, such as Hereditary Hemorrhagic Telangiectasia (HHT). HHT is known for its mucocutaneous telangiectasias and arteriovenous malformations (AVMs), particularly in the lungs.",
        "pathophysiology": "HHT is an autosomal dominant condition characterized by abnormal blood vessel formation. The presence of pulmonary AVMs can facilitate right-to-left shunting, bypassing the pulmonary capillary filter and predisposing individuals to paradoxical emboli, which can cause ischemic strokes. The use of aspirin may exacerbate bleeding from fragile telangiectasias, worsening epistaxis.",
        "clinical_correlation": "This patient\u2019s clinical profile\u2014with a past stroke, a negative cardiac workup, and chronic epistaxis worsened by aspirin\u2014strongly suggests the possibility of pulmonary AVMs secondary to HHT. Identifying a pulmonary AVM is critical since it is a correctable source of cerebral embolism.",
        "diagnostic_approach": "After a negative cardiac workup, lung angiography (via CT angiography of the chest) is the imaging modality of choice to detect pulmonary AVMs. Important differentials include vasculitides (e.g., granulomatosis with polyangiitis) where C-ANCA could be positive, but the clinical constellation in HHT (recurrent nosebleeds, telangiectasias, and paradoxical embolism) is distinct.",
        "classification_and_neurology": "Granulomatosis with polyangiitis (GPA) is classified under the group of ANCA-associated vasculitides (AAV), which includes microscopic polyangiitis (MPA) and eosinophilic granulomatosis with polyangiitis (EGPA). These are systemic necrotizing vasculitides affecting small- to medium-sized vessels. The Chapel Hill Consensus Conference (2012) provides the current nosological framework, defining GPA by granulomatous inflammation and necrotizing vasculitis predominantly affecting respiratory tract and kidneys, with frequent C-ANCA positivity. Stroke secondary to vasculitis falls under secondary cerebrovascular disease, distinct from primary ischemic stroke subtypes. This classification emphasizes the importance of systemic evaluation in stroke patients with atypical features. Competing classification systems have evolved with advances in immunology and pathology, but the Chapel Hill criteria remain widely accepted.",
        "classification_and_nosology": "HHT is classified under vascular dysplasias and is typically inherited in an autosomal dominant pattern. It involves multiple organ systems, frequently affecting the mucocutaneous and pulmonary vasculature.",
        "management_principles": "The cornerstone of management for pulmonary AVMs involves transcatheter embolization, which can reduce the risk of stroke and brain abscess. In patients with HHT, avoiding medications like aspirin that exacerbate bleeding is important. In pregnant or lactating women with HHT, careful evaluation is warranted as pulmonary AVMs may enlarge during pregnancy; embolization is generally deferred until after the first trimester and coordinated with a multidisciplinary team.",
        "option_analysis": "Option A (Lung Angiography) is correct because it is the most direct means of detecting pulmonary AVMs that may be responsible for paradoxical embolic stroke. Option B (C-ANCA) would be used for suspected vasculitis (e.g., granulomatosis with polyangiitis) but does not align with a clinical picture dominated by epistaxis and AVM-related stroke.",
        "clinical_pearls": "\u2022 In patients with cryptogenic stroke and recurrent epistaxis, think of HHT.  \u2022 Pulmonary AVMs facilitate paradoxical embolism and warrant prompt evaluation.  \u2022 Aspirin can exacerbate bleeding in patients with fragile telangiectasias.",
        "current_evidence": "Current international consensus guidelines recommend screening for pulmonary AVMs in patients suspected of having HHT, particularly when there is a history of stroke. Emerging research emphasizes the safety and efficacy of endovascular embolization in reducing stroke risk in these patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993255",
    "fields": {
      "question_number": "39",
      "question_text": "Patient with migraine headaches, father died young from a stroke. To diagnose what should you do",
      "options": {
        "A": "Skin biopsy for eosinophilic inclusions"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy) is an inherited small vessel disease that typically presents with migraine headaches (often with aura), cognitive decline, and a family history of premature stroke. A skin biopsy looking for granular osmiophilic material (eosinophilic inclusions) in the vessel walls is a key diagnostic test.",
        "pathophysiology": "CADASIL is caused by mutations in the NOTCH3 gene, which leads to abnormal accumulation of the NOTCH3 extracellular domain in vascular smooth muscle cells. These deposits result in progressive degeneration of the small penetrating arteries and arterioles, leading to subcortical infarcts, white matter changes, and ultimately, stroke and cognitive impairment.",
        "clinical_correlation": "The presentation of migraine headaches in a patient with a family history of early stroke is highly suggestive of CADASIL. The use of a skin biopsy can reveal the characteristic eosinophilic granular deposits, helping to confirm the diagnosis.",
        "diagnostic_approach": "While genetic testing for NOTCH3 mutations is increasingly used, a skin biopsy remains a reliable diagnostic tool, especially when genetic testing is unavailable or inconclusive. Differential diagnoses include other hereditary small vessel diseases; however, the combination of migraine with aura and a familial pattern strongly points toward CADASIL.",
        "classification_and_neurology": "CADASIL belongs to the broader category of hereditary small vessel diseases of the brain, classified under genetic cerebrovascular disorders. According to the 2017 International Stroke Genetics Consortium and subsequent nosological frameworks, hereditary small vessel diseases are subdivided based on genetic etiology, including NOTCH3 mutations (CADASIL), HTRA1 mutations (CARASIL), and others. CADASIL is an autosomal dominant arteriopathy characterized by subcortical infarcts and leukoencephalopathy. It is distinct from sporadic small vessel disease related to hypertension or aging. Nosological evolution has refined the classification based on molecular genetics and clinical phenotype, emphasizing the importance of genetic testing and histopathology. While CADASIL is the prototype, other hereditary small vessel diseases differ in inheritance, clinical features, and pathology, underscoring the need for precise diagnosis.",
        "classification_and_nosology": "CADASIL is classified as a hereditary arteriopathy and is the most common form of hereditary stroke disorder. It is inherited in an autosomal dominant manner.",
        "management_principles": "Currently, there is no cure for CADASIL and management is primarily supportive, focusing on reducing stroke risk and managing symptoms (e.g., controlling blood pressure, managing migraines). Antiplatelet agents such as aspirin may be used, although their benefit in CADASIL is uncertain. In pregnant or lactating patients, treatment is symptomatic with careful selection of medications that have an acceptable safety profile during pregnancy.",
        "option_analysis": "Option A (Skin biopsy for eosinophilic inclusions) is correct because it tests for the pathognomonic finding in CADASIL\u2014the granular osmiophilic material. Other options were not provided, but given the clinical context, skin biopsy is the appropriate diagnostic step.",
        "clinical_pearls": "\u2022 A family history of early stroke combined with migraine with aura should raise suspicion for CADASIL.  \u2022 Skin biopsy revealing granular osmiophilic material is a hallmark of CADASIL.  \u2022 Early recognition is important for counseling and management, even though disease-specific treatment remains limited.",
        "current_evidence": "Recent advances emphasize the role of genetic testing for NOTCH3 mutations; however, skin biopsy continues to be a valuable diagnostic adjunct. Ongoing research is investigating therapies that might modify the disease course, but current management remains supportive."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993256",
    "fields": {
      "question_number": "40",
      "question_text": "CVT after birth what to do?",
      "options": {
        "A": "CTV",
        "B": "??"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral Venous Thrombosis (CVT) is a form of stroke caused by thrombosis in the cerebral venous sinuses. The postpartum period is a high-risk state for thrombosis due to a transient hypercoagulable state.",
        "pathophysiology": "After childbirth, hormonal changes and a hypercoagulable state predispose patients to thrombus formation within the cerebral venous system. This can lead to impaired venous drainage, increased intracranial pressure, and venous infarction or hemorrhage.",
        "clinical_correlation": "Patients with CVT may present with severe headache, seizures, focal neurological deficits, or signs of raised intracranial pressure. In postpartum patients, CVT should be high on the differential when these symptoms arise.",
        "diagnostic_approach": "The diagnostic imaging of choice for CVT is CT Venography (CTV) or MR Venography (MRV). CTV is widely available, quick, and highly sensitive in detecting venous sinus thrombosis, making it a reasonable first-line diagnostic tool. Differential diagnoses include arterial stroke, intracerebral hemorrhage, and benign postdural puncture headache, but the clinical scenario and imaging findings help clarify the diagnosis.",
        "classification_and_neurology": "CVT is classified under cerebrovascular diseases, specifically within the subgroup of venous stroke or cerebral venous and sinus thrombosis. The International Classification of Diseases (ICD-10) categorizes CVT under I67.6 (nonpyogenic thrombosis of intracranial venous system).   Nosologically, CVT differs from arterial ischemic stroke in etiology, pathophysiology, and clinical presentation. It is part of the broader family of thrombotic disorders influenced by acquired and inherited prothrombotic states. Classification can also be based on the site of thrombosis (e.g., superior sagittal sinus, transverse sinus, cortical veins) or underlying cause (e.g., pregnancy/postpartum, infection, malignancy, thrombophilia).  Current consensus emphasizes the importance of recognizing CVT as a distinct cerebrovascular entity with unique diagnostic and therapeutic approaches, as outlined in the 2017 European Stroke Organization guidelines and AHA/ASA scientific statements.",
        "classification_and_nosology": "CVT is classified among cerebrovascular disorders related to venous outflow obstruction. The postpartum period represents a recognized risk factor within the broader category of hypercoagulable states.",
        "management_principles": "Management of CVT generally involves prompt initiation of anticoagulation (typically with low molecular weight heparin) even in the presence of hemorrhagic infarct. In postpartum patients, anticoagulation is safe and effective, and lactation is not a contraindication. Subsequent treatment may involve transition to oral anticoagulants for a duration guided by risk factors and recurrence risk. Multidisciplinary management including neurology and hematology is important. For breastfeeding mothers, LMWH is preferred due to minimal secretion in breast milk.",
        "option_analysis": "Option A (CTV) is correct because CT Venography is a standard, accessible, and highly accurate imaging modality for diagnosing CVT. Other options (such as MRV) may be used but were not provided here, and the given option A is appropriate for initial evaluation.",
        "clinical_pearls": "\u2022 The postpartum period is a well-recognized risk factor for CVT.  \u2022 Early diagnosis via CT Venography can significantly improve outcomes by facilitating early anticoagulation.  \u2022 Anticoagulation is indicated even if a hemorrhagic component is present.",
        "current_evidence": "Recent guidelines consistently support the use of CTV for rapid diagnosis of CVT. Anticoagulation (with LMWH transitioning to oral agents) remains the mainstay of treatment, and studies have validated its safety in the postpartum and lactating populations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993257",
    "fields": {
      "question_number": "41",
      "question_text": "Cardiac arrest in smoker patient complicated with hypotension and intubated. After 1 month came back to the clinic with chronic headaches, dizziness etc what is pathogenesis?",
      "options": {
        "A": "Hypercapnia",
        "B": "Vasospasm",
        "C": "-"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "After a cardiac arrest\u2014especially in a smoker complicated by hypotension and requiring intubation\u2014the brain undergoes a period of global ischemia. The subsequent delayed neurological complaints such as chronic headaches and dizziness are most consistent with a hypoxic-ischemic injury rather than acute derangements like hypercapnia or vascular phenomena like vasospasm.",
        "pathophysiology": "During cardiac arrest, cerebral blood flow ceases, leading to widespread neuronal hypoxia. Hypotension exacerbates this effect, and upon resuscitation, reperfusion injury (with production of free radicals and inflammatory mediators) may occur. This results in delayed neuronal death and white matter changes\u2014phenomena that are part of hypoxic-ischemic encephalopathy or delayed post-hypoxic leukoencephalopathy. Neither hypercapnia (which is an acute effect due to ventilation issues) nor vasospasm (more typically linked with subarachnoid hemorrhage) explains the delayed symptom picture in this patient.",
        "clinical_correlation": "Patients recovering from cardiac arrest can develop chronic neurological deficits. In this case, persistent headache and dizziness a month later suggest that the brain suffered an ischemic insult with subsequent reperfusion injury. Such deficits are aligned with the areas of the brain that are most vulnerable to low oxygen states.",
        "diagnostic_approach": "The evaluation of post-cardiac arrest patients with chronic neurological symptoms usually involves brain imaging (MRI with diffusion-weighted imaging can reveal watershed or diffuse white matter changes) and sometimes EEG. Differential diagnoses include post-hypoxic encephalopathy, subtle infarcts from embolic events, or metabolic encephalopathy. Clinical context and imaging help differentiate these entities.",
        "classification_and_neurology": "Delayed cerebral vasospasm following global cerebral ischemia such as cardiac arrest fits within the broader classification of **cerebrovascular disorders**, specifically under the category of **secondary cerebral vasospasm**.   - It differs from primary vasospasm seen in subarachnoid hemorrhage but shares pathophysiological features. - It can be classified as a form of **delayed ischemic neurological deficit (DIND)** occurring post-ischemic injury. - The nosology aligns with vascular dysregulation syndromes and post-hypoxic encephalopathies.  Classification systems such as the World Federation of Neurological Surgeons (WFNS) grading for vasospasm primarily address aneurysmal subarachnoid hemorrhage but provide a framework for understanding vasospasm severity. There is ongoing debate about the best terminology and classification for vasospasm outside hemorrhagic contexts, with some advocating for terms like 'delayed cerebral ischemia' to emphasize clinical impact over angiographic findings.",
        "classification_and_nosology": "This complication falls under the umbrella of hypoxic-ischemic encephalopathy, more specifically the delayed neuronal injury seen after global cerebral hypoperfusion.",
        "management_principles": "Management is largely supportive. First-line measures include neurorehabilitation and symptomatic treatments for headaches and dizziness. There is no established pharmacological therapy to reverse hypoxic neuronal loss. In pregnant or lactating patients, conservative symptomatic management is emphasized, ensuring that agents (e.g., acetaminophen for headache) chosen are safe and that neurorehabilitative strategies are adapted appropriately.",
        "option_analysis": "Option A (Hypercapnia) deals with acute ventilation issues and would present with acute rather than chronic symptoms. Option B (Vasospasm) is classically seen in the setting of subarachnoid hemorrhage, not following a cardiac arrest. Option C is intended to refer to the mechanism of hypoxic-ischemic injury (even though the option text was missing), which is the correct pathogenesis in this scenario.",
        "clinical_pearls": "\u2022 Delayed neurological deficits after cardiac arrest are most commonly due to hypoxic, not hypercapnic, injury.  \u2022 Reperfusion injury is a key contributor to delayed symptomatology post-resuscitation.  \u2022 MRI with DWI is useful in detecting early hypoxic changes.",
        "current_evidence": "Recent studies have focused on targeted temperature management during and after cardiac arrest as a means to reduce reperfusion injury. Advances in neuroimaging have enhanced early detection of hypoxic-ischemic changes, and ongoing research is evaluating neuroprotective agents for post-resuscitation care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993395",
    "fields": {
      "question_number": "424",
      "question_text": "Two questions of a patient has horner that does not react with cocaine or amphetamine",
      "options": {
        "A": "Post-ganglionic",
        "B": "Preganglionic"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "After a cardiac arrest\u2014especially in a smoker complicated by hypotension and requiring intubation\u2014the brain undergoes a period of global ischemia. The subsequent delayed neurological complaints such as chronic headaches and dizziness are most consistent with a hypoxic-ischemic injury rather than acute derangements like hypercapnia or vascular phenomena like vasospasm.",
        "pathophysiology": "During cardiac arrest, cerebral blood flow ceases, leading to widespread neuronal hypoxia. Hypotension exacerbates this effect, and upon resuscitation, reperfusion injury (with production of free radicals and inflammatory mediators) may occur. This results in delayed neuronal death and white matter changes\u2014phenomena that are part of hypoxic-ischemic encephalopathy or delayed post-hypoxic leukoencephalopathy. Neither hypercapnia (which is an acute effect due to ventilation issues) nor vasospasm (more typically linked with subarachnoid hemorrhage) explains the delayed symptom picture in this patient.",
        "clinical_correlation": "Patients recovering from cardiac arrest can develop chronic neurological deficits. In this case, persistent headache and dizziness a month later suggest that the brain suffered an ischemic insult with subsequent reperfusion injury. Such deficits are aligned with the areas of the brain that are most vulnerable to low oxygen states.",
        "diagnostic_approach": "The evaluation of post-cardiac arrest patients with chronic neurological symptoms usually involves brain imaging (MRI with diffusion-weighted imaging can reveal watershed or diffuse white matter changes) and sometimes EEG. Differential diagnoses include post-hypoxic encephalopathy, subtle infarcts from embolic events, or metabolic encephalopathy. Clinical context and imaging help differentiate these entities.",
        "classification_and_neurology": "Horner syndrome is classified based on lesion location along the oculosympathetic pathway into central (first-order neuron), preganglionic (second-order neuron), and postganglionic (third-order neuron) types. This classification is entrenched in neuroanatomical and clinical frameworks and guides diagnostic evaluation. Central lesions involve the hypothalamospinal tract and brainstem; preganglionic lesions affect fibers exiting the spinal cord to the superior cervical ganglion; postganglionic lesions involve fibers from the superior cervical ganglion to the eye. This tripartite classification aligns with etiologic categories such as stroke or demyelination (central), thoracic tumors or trauma (preganglionic), and carotid dissection or cavernous sinus lesions (postganglionic). Although alternative approaches exist focusing on clinical syndromes or imaging findings, the anatomical classification remains the standard for clinical practice and research. Some controversies persist regarding the sensitivity and specificity of pharmacologic tests in certain clinical contexts, but the fundamental nosology is well established.",
        "classification_and_nosology": "This complication falls under the umbrella of hypoxic-ischemic encephalopathy, more specifically the delayed neuronal injury seen after global cerebral hypoperfusion.",
        "management_principles": "Management is largely supportive. First-line measures include neurorehabilitation and symptomatic treatments for headaches and dizziness. There is no established pharmacological therapy to reverse hypoxic neuronal loss. In pregnant or lactating patients, conservative symptomatic management is emphasized, ensuring that agents (e.g., acetaminophen for headache) chosen are safe and that neurorehabilitative strategies are adapted appropriately.",
        "option_analysis": "Option A (Hypercapnia) deals with acute ventilation issues and would present with acute rather than chronic symptoms. Option B (Vasospasm) is classically seen in the setting of subarachnoid hemorrhage, not following a cardiac arrest. Option C is intended to refer to the mechanism of hypoxic-ischemic injury (even though the option text was missing), which is the correct pathogenesis in this scenario.",
        "clinical_pearls": "\u2022 Delayed neurological deficits after cardiac arrest are most commonly due to hypoxic, not hypercapnic, injury.  \u2022 Reperfusion injury is a key contributor to delayed symptomatology post-resuscitation.  \u2022 MRI with DWI is useful in detecting early hypoxic changes.",
        "current_evidence": "Recent studies have focused on targeted temperature management during and after cardiac arrest as a means to reduce reperfusion injury. Advances in neuroimaging have enhanced early detection of hypoxic-ischemic changes, and ongoing research is evaluating neuroprotective agents for post-resuscitation care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993396",
    "fields": {
      "question_number": "425",
      "question_text": "The most common first presentation of CJD",
      "options": {
        "A": "movement",
        "B": "Psychiatry"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "After a cardiac arrest\u2014especially in a smoker complicated by hypotension and requiring intubation\u2014the brain undergoes a period of global ischemia. The subsequent delayed neurological complaints such as chronic headaches and dizziness are most consistent with a hypoxic-ischemic injury rather than acute derangements like hypercapnia or vascular phenomena like vasospasm.",
        "pathophysiology": "During cardiac arrest, cerebral blood flow ceases, leading to widespread neuronal hypoxia. Hypotension exacerbates this effect, and upon resuscitation, reperfusion injury (with production of free radicals and inflammatory mediators) may occur. This results in delayed neuronal death and white matter changes\u2014phenomena that are part of hypoxic-ischemic encephalopathy or delayed post-hypoxic leukoencephalopathy. Neither hypercapnia (which is an acute effect due to ventilation issues) nor vasospasm (more typically linked with subarachnoid hemorrhage) explains the delayed symptom picture in this patient.",
        "clinical_correlation": "Patients recovering from cardiac arrest can develop chronic neurological deficits. In this case, persistent headache and dizziness a month later suggest that the brain suffered an ischemic insult with subsequent reperfusion injury. Such deficits are aligned with the areas of the brain that are most vulnerable to low oxygen states.",
        "diagnostic_approach": "The evaluation of post-cardiac arrest patients with chronic neurological symptoms usually involves brain imaging (MRI with diffusion-weighted imaging can reveal watershed or diffuse white matter changes) and sometimes EEG. Differential diagnoses include post-hypoxic encephalopathy, subtle infarcts from embolic events, or metabolic encephalopathy. Clinical context and imaging help differentiate these entities.",
        "classification_and_neurology": "CJD belongs to the family of transmissible spongiform encephalopathies (TSEs), a group of prion diseases affecting humans and animals. Within human prion diseases, CJD is classified into sporadic, familial (genetic), iatrogenic, and variant forms. Sporadic CJD is the most common, with no identifiable source of infection or mutation. Familial CJD is linked to mutations in the PRNP gene encoding prion protein. Variant CJD is associated with bovine spongiform encephalopathy (BSE) exposure. Nosologically, CJD is categorized under neurodegenerative diseases with prion etiology, distinct from other dementias by its rapid progression and pathognomonic prion pathology. Classification systems have evolved to incorporate molecular subtypes based on PRNP codon 129 polymorphism and PrP^Sc typing, refining prognosis and clinical correlations. Controversies remain regarding precise diagnostic criteria and the pathogenic mechanisms distinguishing subtypes.",
        "classification_and_nosology": "This complication falls under the umbrella of hypoxic-ischemic encephalopathy, more specifically the delayed neuronal injury seen after global cerebral hypoperfusion.",
        "management_principles": "Management is largely supportive. First-line measures include neurorehabilitation and symptomatic treatments for headaches and dizziness. There is no established pharmacological therapy to reverse hypoxic neuronal loss. In pregnant or lactating patients, conservative symptomatic management is emphasized, ensuring that agents (e.g., acetaminophen for headache) chosen are safe and that neurorehabilitative strategies are adapted appropriately.",
        "option_analysis": "Option A (Hypercapnia) deals with acute ventilation issues and would present with acute rather than chronic symptoms. Option B (Vasospasm) is classically seen in the setting of subarachnoid hemorrhage, not following a cardiac arrest. Option C is intended to refer to the mechanism of hypoxic-ischemic injury (even though the option text was missing), which is the correct pathogenesis in this scenario.",
        "clinical_pearls": "\u2022 Delayed neurological deficits after cardiac arrest are most commonly due to hypoxic, not hypercapnic, injury.  \u2022 Reperfusion injury is a key contributor to delayed symptomatology post-resuscitation.  \u2022 MRI with DWI is useful in detecting early hypoxic changes.",
        "current_evidence": "Recent studies have focused on targeted temperature management during and after cardiac arrest as a means to reduce reperfusion injury. Advances in neuroimaging have enhanced early detection of hypoxic-ischemic changes, and ongoing research is evaluating neuroprotective agents for post-resuscitation care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993397",
    "fields": {
      "question_number": "426",
      "question_text": "Alzheimer Dementia most commonly related gene mutation",
      "options": {
        "A": "APP",
        "B": "APO.B"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "After a cardiac arrest\u2014especially in a smoker complicated by hypotension and requiring intubation\u2014the brain undergoes a period of global ischemia. The subsequent delayed neurological complaints such as chronic headaches and dizziness are most consistent with a hypoxic-ischemic injury rather than acute derangements like hypercapnia or vascular phenomena like vasospasm.",
        "pathophysiology": "During cardiac arrest, cerebral blood flow ceases, leading to widespread neuronal hypoxia. Hypotension exacerbates this effect, and upon resuscitation, reperfusion injury (with production of free radicals and inflammatory mediators) may occur. This results in delayed neuronal death and white matter changes\u2014phenomena that are part of hypoxic-ischemic encephalopathy or delayed post-hypoxic leukoencephalopathy. Neither hypercapnia (which is an acute effect due to ventilation issues) nor vasospasm (more typically linked with subarachnoid hemorrhage) explains the delayed symptom picture in this patient.",
        "clinical_correlation": "Patients recovering from cardiac arrest can develop chronic neurological deficits. In this case, persistent headache and dizziness a month later suggest that the brain suffered an ischemic insult with subsequent reperfusion injury. Such deficits are aligned with the areas of the brain that are most vulnerable to low oxygen states.",
        "diagnostic_approach": "The evaluation of post-cardiac arrest patients with chronic neurological symptoms usually involves brain imaging (MRI with diffusion-weighted imaging can reveal watershed or diffuse white matter changes) and sometimes EEG. Differential diagnoses include post-hypoxic encephalopathy, subtle infarcts from embolic events, or metabolic encephalopathy. Clinical context and imaging help differentiate these entities.",
        "classification_and_neurology": "Alzheimer's disease is classified within the broader category of neurodegenerative dementias. The National Institute on Aging and Alzheimer's Association (NIA-AA) framework divides AD into preclinical, mild cognitive impairment (MCI) due to AD, and dementia due to AD. Genetically, AD is categorized into early-onset familial AD (EOFAD) and late-onset sporadic AD. EOFAD is primarily associated with mutations in APP, presenilin 1 (PSEN1), and presenilin 2 (PSEN2) genes. The APP mutation is one of the three major genetic causes of EOFAD, representing a small subset of all AD cases but with high penetrance. APOB, in contrast, is not implicated in AD pathology. The classification has evolved from purely clinical to biomarker and genetic-based, enhancing diagnostic precision and therapeutic targeting.",
        "classification_and_nosology": "This complication falls under the umbrella of hypoxic-ischemic encephalopathy, more specifically the delayed neuronal injury seen after global cerebral hypoperfusion.",
        "management_principles": "Management is largely supportive. First-line measures include neurorehabilitation and symptomatic treatments for headaches and dizziness. There is no established pharmacological therapy to reverse hypoxic neuronal loss. In pregnant or lactating patients, conservative symptomatic management is emphasized, ensuring that agents (e.g., acetaminophen for headache) chosen are safe and that neurorehabilitative strategies are adapted appropriately.",
        "option_analysis": "Option A (Hypercapnia) deals with acute ventilation issues and would present with acute rather than chronic symptoms. Option B (Vasospasm) is classically seen in the setting of subarachnoid hemorrhage, not following a cardiac arrest. Option C is intended to refer to the mechanism of hypoxic-ischemic injury (even though the option text was missing), which is the correct pathogenesis in this scenario.",
        "clinical_pearls": "\u2022 Delayed neurological deficits after cardiac arrest are most commonly due to hypoxic, not hypercapnic, injury.  \u2022 Reperfusion injury is a key contributor to delayed symptomatology post-resuscitation.  \u2022 MRI with DWI is useful in detecting early hypoxic changes.",
        "current_evidence": "Recent studies have focused on targeted temperature management during and after cardiac arrest as a means to reduce reperfusion injury. Advances in neuroimaging have enhanced early detection of hypoxic-ischemic changes, and ongoing research is evaluating neuroprotective agents for post-resuscitation care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993288",
    "fields": {
      "question_number": "127",
      "question_text": "Case of stroke within window NIHSS was 3, next step in rx?",
      "options": {
        "A": "DAPT",
        "B": "TPA",
        "C": "Thrombectomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke management, the overall goal is to restore perfusion and prevent further ischemic injury. The treatment choice depends on factors including the time window, stroke severity measured by the NIH Stroke Scale (NIHSS), and whether deficits are disabling. A NIHSS of 3 generally indicates a minor stroke, and if the deficits are non\u2010disabling, aggressive thrombolytic therapy may not be warranted.",
        "pathophysiology": "Ischemic strokes occur from occlusion of cerebral arteries leading to brain tissue ischemia. In mild strokes, the clot may be smaller, and collateral circulation may limit the extent of injury. The risk in these patients is not only the initial infarct but also early recurrent events. Dual antiplatelet therapy (DAPT) works by inhibiting platelet aggregation, thereby reducing the chance of clot extension or new embolic events.",
        "clinical_correlation": "Patients with a minor stroke (NIHSS 3) often present with subtle neurological deficits that do not significantly impair function. In such cases, intravenous thrombolysis (tPA) is not automatically indicated unless even a minor deficit is considered disabling. DAPT is favored in non\u2010disabling minor strokes to reduce the risk of early recurrence.",
        "diagnostic_approach": "Diagnosis begins with prompt neuroimaging (often a non\u2010contrast CT scan) to rule out hemorrhage, followed by vascular imaging as needed. Differential diagnoses include transient ischemic attack (TIA), migraine, and seizure-related deficits. The clinical context and imaging help distinguish these conditions from an ischemic stroke.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases in the ICD and WHO taxonomies. It is further subclassified by etiology using the TOAST classification into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Treatment classification distinguishes acute reperfusion therapies (intravenous thrombolysis, mechanical thrombectomy) from secondary prevention (antiplatelets, anticoagulation). The NIHSS provides a standardized clinical severity scale, influencing therapeutic decisions. Current consensus guidelines from the American Heart Association/American Stroke Association (AHA/ASA) recommend intravenous tPA for eligible patients within 4.5 hours irrespective of mild or moderate NIHSS scores, reflecting an evolution from earlier more restrictive approaches.",
        "classification_and_nosology": "Ischemic strokes are classified by their etiology (large vessel, small vessel, cardioembolic, etc.) and by clinical severity. A minor stroke often refers to those with low NIHSS scores (typically \u22643\u20135) and non\u2010disabling symptoms.",
        "management_principles": "First-line management for acute ischemic stroke within the treatment window involves IV tPA in patients with disabling deficits. However, for minor, non-disabling strokes (NIHSS 3 and not functionally impairing), the current evidence supports the use of DAPT (commonly aspirin plus clopidogrel) for early secondary prevention. Thrombectomy is reserved for large vessel occlusions. In the context of pregnancy or lactation, aspirin is generally considered safe, although clopidogrel data are limited and should be used if the benefits outweigh the risks.",
        "option_analysis": "Option A (DAPT) is correct for non-disabling minor strokes. Option B (TPA) is recommended for patients with disabling symptoms irrespective of stroke severity; however, in a minor, non-disabling stroke, the risks of thrombolysis may outweigh the benefits. Option C (Thrombectomy) is reserved for large vessel occlusion strokes and is not indicated in a minor stroke with an NIHSS of 3.",
        "clinical_pearls": "1) In minor, non-disabling strokes, careful assessment is needed to decide against thrombolysis even when within the window. 2) Short-term use of DAPT has been shown to reduce early recurrence in minor stroke. 3) The decision-making must incorporate both the NIHSS and the functional impact of the deficits.",
        "current_evidence": "Recent trials such as CHANCE and POINT have demonstrated the benefit of short-term DAPT in reducing recurrent stroke in patients with minor, non-disabling ischemic strokes, influencing current guideline recommendations to personalize therapy based on the functional impact rather than solely on the NIHSS score."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993289",
    "fields": {
      "question_number": "128",
      "question_text": "Case of right ICA dissection presented with left sided weakness, what is the treatment in acute setting?",
      "options": {
        "A": "stenting",
        "B": "angioplasty",
        "C": "Medical therapy"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Carotid artery dissection, particularly of the internal carotid artery (ICA), is a common cause of stroke in younger patients. It results from a tear in the arterial wall, leading to the formation of an intramural hematoma and risk of thromboembolism. The standard approach in the acute setting is to prevent thromboembolic complications using medical therapy.",
        "pathophysiology": "Dissection involves a tear in the intimal layer of the artery, allowing blood to enter the vessel wall which creates a false lumen. This can lead to luminal stenosis and an increased risk of thrombus formation, which may embolize and cause cerebral infarction. The main goal of treatment is to prevent further thromboembolic events.",
        "clinical_correlation": "Patients with ICA dissection often present with ipsilateral headache, Horner\u2019s syndrome, or neck pain, and may develop neurological deficits (such as contralateral weakness) due to cerebral ischemia caused by emboli. Recognizing the dissection early is key to preventing stroke progression.",
        "diagnostic_approach": "Diagnosis is typically established by imaging modalities such as CT angiography or MRI/MRA. Differential diagnoses include atherosclerotic disease, fibromuscular dysplasia, and other vasculopathies. The imaging findings along with clinical presentation help confirm the diagnosis of arterial dissection.",
        "classification_and_neurology": "Carotid artery dissection is classified under extracranial arterial dissections, a subgroup of cerebrovascular disorders. It belongs to the broader category of ischemic stroke etiologies, specifically under large artery atherosclerosis and arterial dissection subtypes in TOAST classification. Dissections can be spontaneous or traumatic and may involve the extracranial or intracranial segments. Nosologically, CAD is distinct from other stroke mechanisms due to its unique pathogenesis involving vessel wall injury rather than embolism from cardiac sources or atherosclerotic plaque rupture. Classification systems have evolved to emphasize imaging findings and clinical presentation, with current consensus recognizing CAD as a major cause of stroke in younger adults.",
        "classification_and_nosology": "Carotid dissections are classified as spontaneous or traumatic. They are grouped under non-atherosclerotic arteriopathies that predispose to stroke. The treatment strategies typically involve antithrombotic therapy.",
        "management_principles": "First-line management for ICA dissection is medical therapy using either antiplatelet agents or anticoagulation. Current evidence, including the CADISS trial, has not shown a significant difference in outcomes between the two modalities. The selection depends on individual patient risks and contraindications. Endovascular interventions such as stenting or angioplasty are reserved for cases that fail medical management or in which there is ongoing ischemia. In pregnancy and lactation, heparin (as unfractionated heparin or low molecular weight heparin) is generally preferred due to its safety profile.",
        "option_analysis": "Option C (Medical therapy) is the correct initial treatment for acute carotid artery dissection. Option A (Stenting) and Option B (Angioplasty) are invasive procedures generally considered in refractory cases or if there is significant luminal compromise causing ongoing ischemia, but they are not first-line treatments.",
        "clinical_pearls": "1) Early diagnosis of carotid dissection is essential to prevent thromboembolic stroke. 2) Both antiplatelet and anticoagulant therapies are viable first-line options. 3) Endovascular interventions are considered only if medical therapy fails.",
        "current_evidence": "Recent research, including the CADISS trial, has supported the use of medical management (either antiplatelet or anticoagulation) in carotid dissection, with similar efficacy in preventing recurrent ischemic events. This evidence underpins current therapeutic guidelines."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993290",
    "fields": {
      "question_number": "129",
      "question_text": "Sickler patient with multiple previous strokes, what is the most important preventitive Rx?",
      "options": {
        "A": "Chronic transfusion",
        "B": "Aspirin",
        "C": "Anticoagulation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Patients with sickle cell disease (SCD) are at high risk for ischemic stroke due to the abnormal morphology of red blood cells leading to vascular occlusion and endothelial damage. For secondary prevention in SCD patients who have experienced a stroke, reducing the proportion of sickled red blood cells is key.",
        "pathophysiology": "In SCD, the abnormal hemoglobin S polymerizes under conditions of low oxygen tension, causing red blood cells to sickle. These sickled cells can obstruct microvasculature and cause endothelial injury, which results in a prothrombotic state and predisposes to stroke. Chronic transfusion therapy reduces the proportion of hemoglobin S by diluting it with normal hemoglobin, thereby mitigating these risks.",
        "clinical_correlation": "SCD patients with a history of strokes typically present with recurrent neurological deficits and other complications of vaso-occlusion. Stroke prevention is a major component of the overall management strategy in SCD to reduce mortality and morbidity.",
        "diagnostic_approach": "Evaluation includes neuroimaging (MRI, MRA) to assess for prior infarcts and ongoing cerebrovascular disease, as well as transcranial Doppler ultrasound screening in children with SCD. Differential diagnoses include transient ischemic attack (TIA) and silent cerebral infarcts, which are common in SCD.",
        "classification_and_neurology": "Stroke in SCD is classified under **ischemic cerebrovascular disease** with a distinct etiology related to hemoglobinopathy-induced vasculopathy. The broader classification situates these strokes within **stroke subtypes per TOAST criteria**, typically categorized as 'other determined etiology' due to sickle cell vasculopathy. SCD-related strokes form part of the spectrum of inherited hematological disorders with neurological complications. Nosological frameworks have evolved to emphasize the unique pathophysiology of SCD strokes, differentiating them from typical atherosclerotic or cardioembolic strokes. This distinction is crucial for management, as standard stroke prevention paradigms do not fully apply.",
        "classification_and_nosology": "Stroke in SCD is classified as a vasculopathy-related ischemic event. The condition falls under the broader spectrum of SCD complications resulting from chronic hemolysis and vaso-occlusive phenomena.",
        "management_principles": "Chronic red blood cell transfusion is the first-line preventive strategy for secondary stroke prevention in patients with SCD. The goal is to maintain the percentage of hemoglobin S below 30% to lower the risk of recurrent strokes. First-line management includes regular transfusion regimens with appropriate iron chelation to prevent iron overload. Aspirin or anticoagulation is not considered sufficient for stroke prevention in these patients. In pregnancy and lactation, chronic transfusion plans are continued with careful monitoring of iron levels and fetal well-being, as transfusions are generally considered safe.",
        "option_analysis": "Option A (Chronic transfusion) is correct as it is the standard of care for preventing recurrent strokes in SCD. Option B (Aspirin) and Option C (Anticoagulation) do not address the underlying pathophysiology of sickling and are not recommended as primary preventive strategies in this population.",
        "clinical_pearls": "1) Maintaining hemoglobin S levels below target thresholds is crucial for stroke prevention in SCD. 2) Iron overload is an important complication to monitor in patients on chronic transfusion therapy. 3) Regular neurovascular screening is recommended in children with SCD to preemptively address stroke risk.",
        "current_evidence": "Recent guidelines from hematology societies underscore the importance of chronic transfusion therapy for secondary stroke prevention in SCD. Emerging research is also examining the roles of hydroxyurea and stem cell transplantation, but chronic transfusions remain the cornerstone of management for patients with prior strokes."
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
