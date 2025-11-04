
# Import batch 1 of 3 from chunk_15_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993013",
    "fields": {
      "question_number": "145",
      "question_text": "Which of the following best describes the evidence for use of decompressive craniectomy in the management of malignant edema following large hemispheric stroke?",
      "options": {
        "A": "Decompressive craniotomy improves functional outcomes but disability persists among survivors.",
        "B": "Decompressive craniotomy is not associated with survival benefit in any age group.",
        "C": "Decompressive craniotomy outcomes are improved when done more than 72 hours from stroke onset.",
        "D": "Older patients (more than 60 years of age) have better outcomes after decompressive craniotomy than younger patients.",
        "E": "Smaller decompressive craniotomy resection is associated with improved outcomes."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Decompressive craniectomy is a surgical intervention used in cases of malignant cerebral edema following large hemispheric strokes (often malignant MCA infarction). The procedure is intended to alleviate increased intracranial pressure (ICP) and prevent fatal herniation.",
        "pathophysiology": "After a large hemispheric stroke, cytotoxic and vasogenic edema can develop rapidly resulting in increased ICP. Decompressive craniectomy creates space for the swollen brain to expand without being compressed against the rigid skull, thereby reducing the risk of herniation. However, while mortality is reduced, many survivors are left with significant neurological deficits.",
        "clinical_correlation": "Clinically, patients with malignant MCA infarction typically deteriorate neurologically within hours to days after the initial stroke onset. Decompressive craniectomy has been shown to reduce mortality in these patients, yet survivors often have moderate to severe disability. Early intervention (ideally within 48 hours) is associated with better outcomes compared to delayed surgery.",
        "diagnostic_approach": "Diagnosis involves neuroimaging, typically with CT, demonstrating a large infarct area with significant cerebral edema and midline shift. Differential diagnoses include large hemorrhagic strokes (which are managed differently), cerebral edema from other causes (e.g., traumatic brain injury or meningitis), and tumor-associated edema.",
        "classification_and_neurology": "Malignant MCA infarction is classified as a subset of large hemispheric strokes with life-threatening edema formation. It falls under the cerebrovascular disease category in the WHO ICD-11 classification. The condition is distinguished from smaller territorial strokes by extent of infarction (>50% MCA territory) and clinical severity. Decompressive craniectomy is considered a surgical intervention within neurocritical care and stroke management guidelines. The classification of DC outcomes is often described using the modified Rankin Scale (mRS) to quantify disability. Historically, classification of malignant edema has evolved with advances in neuroimaging and surgical techniques. Current consensus guidelines (e.g., AHA/ASA) incorporate clinical, radiological, and temporal criteria to define indications for DC. Controversies remain regarding patient selection, timing, and age cutoffs, reflecting ongoing refinement of nosological frameworks in neurovascular care.",
        "classification_and_nosology": "Malignant MCA syndrome represents a severe form of ischemic stroke characterized by life-threatening cerebral edema. It is classified based on infarct size, clinical deterioration, and radiological findings of mass effect.",
        "management_principles": "Current guidelines recommend early decompressive hemicraniectomy in selected patients (typically younger than 60\u201370 years) with malignant MCA infarction. This tiered approach is as follows: First-line management includes supportive care and osmotherapy; if neurological deterioration occurs, early surgical decompression is recommended. For pregnant or lactating patients, decompressive craniectomy is performed following the same principles with multidisciplinary involvement (including obstetrics and anesthesia) to ensure maternal and fetal safety.",
        "option_analysis": "Option A is correct: multiple randomized controlled trials (including DECIMAL, DESTINY, and HAMLET) have shown that decompressive craniectomy improves survival and yields better functional outcomes compared to medical management alone, although significant disability frequently persists among survivors. Option B is incorrect because there is a clear survival benefit in certain age groups (especially younger patients). Option C is false because the benefit is greatest when surgery is performed early (within 48 hours), not delayed beyond 72 hours. Option D is incorrect since younger patients tend to have better outcomes compared to older patients. Option E is not supported by evidence; an adequately large decompressive procedure is required to be effective.",
        "clinical_pearls": "1. Decompressive craniectomy markedly improves survival in malignant MCA infarction, but many survivors have residual disability. 2. Timing is critical; earlier surgery (preferably within 48 hours) yields better outcomes. 3. Patient selection (with consideration of age and baseline function) is essential for optimal results.",
        "current_evidence": "The latest clinical trials and meta-analyses affirm that decompressive craniectomy significantly reduces mortality in malignant MCA infarction. However, survivors often endure moderate to severe disability, underscoring the need for comprehensive post-operative neurological rehabilitation and patient counseling regarding long-term outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993014",
    "fields": {
      "question_number": "146",
      "question_text": "ICH, which is correct:",
      "options": {
        "A": "ICH score is for mortality, including age, GCS, IVH volume and coagulopathy age risk factor",
        "B": "Spot sign ..... Is not beneficial for reverse anticoagulation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Intracerebral hemorrhage (ICH) scoring systems are used to predict mortality and guide clinical decision-making in patients presenting with spontaneous ICH. The ICH score is one of the best-known prognostic tools in this setting.",
        "pathophysiology": "ICH leads to direct brain injury from the hematoma and secondary injury due to mass effect and increased intracranial pressure. The ICH score integrates clinical and imaging parameters that reflect the severity of hemorrhage and the risk of poor outcomes.",
        "clinical_correlation": "Clinically, the ICH score helps clinicians stratify patients based on the risk of mortality. This tool is useful for discussions regarding prognosis with families and in guiding the intensity of care. Although factors like coagulopathy are important in the management of ICH (especially when considering reversal therapy in anticoagulated patients), they are not part of the original ICH score.",
        "diagnostic_approach": "The assessment of ICH includes noncontrast CT imaging to evaluate hematoma size, location, and the presence of intraventricular hemorrhage (IVH), along with clinical evaluation (notably Glasgow Coma Scale [GCS]) and patient age. Differential diagnoses include secondary causes of hemorrhage such as vascular malformations, tumors, or hemorrhagic conversion of an ischemic stroke.",
        "classification_and_neurology": "ICH is classified under hemorrhagic strokes, distinct from ischemic strokes and subarachnoid hemorrhage. The classification considers etiology (hypertensive, amyloid angiopathy, anticoagulant-related, vascular malformations), location (lobar, deep, cerebellar, brainstem), and clinical severity. The ICH score is a validated prognostic classification system introduced by Hemphill et al. (2001) that stratifies patients based on five variables: GCS score, hematoma volume, presence of IVH, infratentorial origin, and age >80 years. This score predicts 30-day mortality and is widely used in clinical and research settings. Other classification systems include the FUNC score for functional outcome prediction. The 'spot sign' is a radiographic marker rather than a classification but fits within risk stratification frameworks. Nosology continues to evolve with advances in imaging and molecular biomarkers, though the ICH score remains a cornerstone for outcome prediction.",
        "classification_and_nosology": "The ICH score, first introduced by Hemphill et al., typically includes five components: GCS score, ICH volume (>30 cc), presence of IVH, infratentorial origin, and age \u226580 years. It is primarily used to predict 30-day mortality in spontaneous ICH.",
        "management_principles": "Management of ICH is guided by supportive care, blood pressure control, and reversal of coagulopathy when present. Although the ICH score is prognostic, treatment decisions (such as surgical intervention) also consider clinical context, patient wishes, and overall health. In pregnant or lactating patients with ICH, management principles are similar\u2014with careful coordination among neurology, neurosurgery, and obstetrics to minimize harm to both the mother and fetus or neonate. The ICH score itself does not alter acute management but provides prognostic information.",
        "option_analysis": "Option A is considered correct in that the ICH score is used to predict mortality in ICH patients and incorporates clinical variables such as age, GCS, and aspects of the hemorrhage visible on imaging (i.e., volume and presence of IVH). Note, however, that the original ICH score does not include coagulopathy as a factor\u2014the traditional components are age (\u226580 years), GCS, ICH volume (>30 cc), presence of IVH, and infratentorial location. Option B, regarding the spot sign, is incorrect because while the CTA spot sign is a marker for hematoma expansion, its presence does not affect the process of reversing anticoagulation, which is indicated based on clinical and laboratory findings irrespective of the spot sign.",
        "clinical_pearls": "1. The ICH score remains a valuable tool for predicting 30\u2010day mortality in spontaneous intracerebral hemorrhage. 2. Despite its usefulness, the original score does not include coagulopathy as a parameter. 3. The 'spot sign' on CT angiography is a predictor of hematoma expansion but is not used to guide reversal strategies.",
        "current_evidence": "Recent studies continue to validate the prognostic value of the ICH score. While there are ongoing efforts to refine prognostic models\u2014some proposing additional factors such as coagulopathy\u2014the widely accepted version still incorporates age, GCS, ICH volume, IVH, and infratentorial location. Current guidelines emphasize rapid reversal of anticoagulation in ICH patients when indicated, independent of the presence of a spot sign."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993015",
    "fields": {
      "question_number": "147",
      "question_text": "Young female (case about CVT), Possible risk factor:",
      "options": {
        "A": "HTN",
        "B": "DM",
        "C": "UC",
        "D": "migraine"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral venous thrombosis (CVT) is an uncommon type of stroke in which clot formation within the cerebral venous sinuses impairs venous drainage, leading to intracranial hypertension and venous infarction. It most frequently presents in young females and is associated with several prothrombotic risk factors.",
        "pathophysiology": "In CVT, hypercoagulable states cause thrombosis in the cerebral venous system. Ulcerative colitis (UC), an inflammatory bowel disease, is known to create a systemic prothrombotic environment due to increased inflammatory cytokines and altered coagulation factors. This predisposes patients to venous thrombosis, including in the cerebral sinuses, increasing the risk of CVT.",
        "clinical_correlation": "Patients with CVT typically present with headache, seizures, visual disturbances, focal neurological deficits, and symptoms of increased intracranial pressure. In a young female with UC, the inflammatory state can trigger clot formation, making UC an important risk factor. Other conditions like HTN or DM are less strongly linked to CVT compared to inflammatory and hypercoagulable conditions.",
        "diagnostic_approach": "The diagnosis of CVT is usually confirmed by neuroimaging, such as MRI/MRV or CT venography. Differential diagnoses include meningitis, intracranial hemorrhage, and migraine with aura. A detailed history (including risk factors like oral contraceptive use and autoimmune diseases) along with neuroimaging helps to distinguish CVT from these other disorders.",
        "classification_and_neurology": "CVT is classified under cerebrovascular diseases, specifically venous stroke, distinct from arterial ischemic stroke. It belongs to the broader category of thrombotic disorders affecting the central nervous system. The International Classification of Diseases (ICD-11) and stroke classification systems (e.g., TOAST for arterial strokes) do not have a dedicated subclassification for CVT; however, it is recognized as a distinct entity due to unique pathophysiology and clinical features. CVT etiologies are subclassified into inherited thrombophilias, acquired prothrombotic states (including systemic inflammatory diseases like UC), infections, and mechanical causes. The classification of risk factors has evolved, with increasing appreciation of systemic inflammatory diseases as significant contributors.",
        "classification_and_nosology": "CVT is categorized under cerebrovascular disorders and represents a form of venous stroke, distinct from the more common arterial ischemic strokes.",
        "management_principles": "The current first-line management of CVT is anticoagulation with low-molecular-weight heparin (LMWH), even if there is hemorrhagic transformation. For patients who are pregnant or lactating, LMWH is preferred because it does not cross the placenta and is considered safe during lactation. Subsequent long-term management involves transitioning to oral anticoagulants and addressing any underlying prothrombotic state, including active management of UC.",
        "option_analysis": "Option A (HTN) and Option B (DM) are more typically associated with arterial strokes rather than CVT. Option D (migraine) is not established as a significant risk factor for CVT. Option C (UC) is correct because inflammatory bowel diseases like ulcerative colitis are well-recognized for increasing the risk of venous thrombosis due to a hypercoagulable state.",
        "clinical_pearls": "1. CVT often presents in young women with risk factors such as oral contraceptive use, pregnancy, postpartum state, or inflammatory conditions. 2. Neuroimaging (MRV/CTV) is essential for prompt diagnosis. 3. Anticoagulation is the cornerstone of treatment, even in the presence of hemorrhage.",
        "current_evidence": "Recent guidelines emphasize the early initiation of anticoagulation treatment in CVT patients. Studies have also highlighted the significant role of inflammatory conditions, such as UC, in the pathogenesis of CVT, reinforcing the need for clinicians to evaluate these risk factors in young female patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993016",
    "fields": {
      "question_number": "148",
      "question_text": "Case about young patient and malignant MCA stroke. Next step:",
      "options": {
        "A": "hemicraniectomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Malignant middle cerebral artery (MCA) infarction is a severe ischemic stroke characterized by extensive infarction of the MCA territory that leads to significant cerebral edema and increased intracranial pressure. In young patients, rapid neurological deterioration is common if the edema is not managed actively.",
        "pathophysiology": "After a large MCA infarction, cytotoxic and vasogenic edema develop rapidly, leading to a mass effect, midline shift, and potential herniation. The resultant increase in intracranial pressure can compromise cerebral perfusion and cause further neurological decline.",
        "clinical_correlation": "Clinically, patients with malignant MCA strokes exhibit worsening neurological deficits, decreased level of consciousness, and signs of raised intracranial pressure. Neuroimaging typically demonstrates extensive infarction with edema and compression of adjacent brain structures. The deteriorating clinical status despite medical treatment often necessitates surgical intervention.",
        "diagnostic_approach": "Diagnosis is primarily made with non-contrast CT or MRI showing extensive infarction with mass effect. Differential diagnoses include large territorial ischemic strokes without malignant edema, intracerebral hemorrhage, and cerebellar infarction. Careful radiologic assessment differentiates these conditions.",
        "classification_and_neurology": "Malignant MCA infarction is classified as a large territory ischemic stroke with secondary malignant cerebral edema. According to the TOAST classification, this stroke subtype often results from cardioembolism or large artery atherosclerosis causing proximal MCA occlusion. The term 'malignant' refers to the clinical and radiological severity due to space-occupying edema rather than a distinct etiological subtype. In stroke classification systems, malignant MCA stroke is recognized as a complication of large vessel ischemic stroke. The concept of malignant MCA infarction emerged to identify patients at high risk for fatal edema who may benefit from decompressive surgery. Current consensus classifies it under large hemispheric infarctions with malignant edema, emphasizing the importance of early detection and intervention. There is general agreement on this classification, though ongoing research refines criteria for surgical candidacy.",
        "classification_and_nosology": "Malignant MCA infarction falls under the umbrella of ischemic strokes and is specifically classified as a large territory stroke complicated by malignant edema.",
        "management_principles": "First-line management involves aggressive supportive care, including osmotherapy (e.g., mannitol) to reduce intracranial pressure; however, in malignant MCA strokes, these measures are often insufficient. The current guideline-recommended treatment is early decompressive hemicraniectomy (typically within 48 hours) for eligible patients. In pregnant patients, decompressive surgery is also considered safe with multidisciplinary coordination and fetal monitoring. Second-line strategies may include further ICU care and symptomatic management.",
        "option_analysis": "Option A (hemicraniectomy) is correct because decompressive surgery has been shown to reduce mortality and improve functional outcomes in malignant MCA strokes. Other potential options, if they had been listed, would not address the underlying mass effect and are less effective in this acute setting.",
        "clinical_pearls": "1. Decompressive hemicraniectomy is a life-saving intervention in malignant MCA stroke when performed within the therapeutic window. 2. Rapid neuroimaging and early intervention are critical due to the aggressive nature of malignant edema. 3. Even in younger patients, timely surgery can significantly alter the outcome.",
        "current_evidence": "Current research, including large randomized controlled trials (e.g., DESTINY, HAMLET), supports early decompressive hemicraniectomy for malignant MCA infarction, demonstrating improved survival rates and functional outcomes when compared with conservative medical management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993017",
    "fields": {
      "question_number": "149",
      "question_text": "Case scenario about Lateral medullary syndrome. What is the diagnosis? (Clear).",
      "options": {},
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Lateral medullary syndrome, also known as Wallenberg syndrome, is a distinct brainstem stroke resulting from occlusion of the posterior inferior cerebellar artery (PICA) or vertebral artery. It produces a recognizable set of neurological deficits due to involvement of specific medullary structures.",
        "pathophysiology": "The lateral medulla houses several important neural structures, including the spinal trigeminal nucleus, vestibular nuclei, nucleus ambiguus, and descending sympathetic fibers. Infarction in this area disrupts these pathways, causing a constellation of symptoms such as dysphagia, hoarseness, ataxia, vertigo, and the hallmark crossed sensory deficits.",
        "clinical_correlation": "Patients with lateral medullary syndrome typically experience ipsilateral facial pain or temperature loss along with contralateral loss of pain and temperature sensation in the body. Additional features may include dysphagia, dysphonia, vertigo, ataxia, and Horner syndrome. These clinical signs are considered pathognomonic for lateral medullary involvement.",
        "diagnostic_approach": "Diagnosis is primarily clinical, supported by MRI of the brainstem which confirms lateral medullary infarction. Differential diagnoses include medial medullary syndrome (characterized by contralateral hemiparesis and tongue deviation), cerebellar infarction, anterior spinal artery syndrome, and rarely a multiple sclerosis flare. Distinguishing features, such as the pattern of crossed sensory loss and cranial nerve involvement, help differentiate lateral from other brainstem syndromes.",
        "classification_and_neurology": "LMS is classified under brainstem stroke syndromes, specifically as a lateral medullary infarct. Stroke classification systems such as the TOAST criteria categorize it as a large artery atherosclerosis or artery-to-artery embolism subtype when related to vertebral artery disease. LMS belongs to the broader category of ischemic cerebrovascular syndromes affecting the posterior circulation. Nosologically, it is distinguished from medial medullary syndrome (Dejerine syndrome) based on lesion location and clinical features. The evolution of stroke classification emphasizes vascular territory and mechanism, aiding in targeted management. While LMS is well-defined clinically and radiologically, some overlapping syndromes may occur with variable involvement of adjacent structures, leading to variant presentations.",
        "classification_and_nosology": "Lateral medullary syndrome is classified under posterior circulation strokes and specifically as a form of brainstem infarction.",
        "management_principles": "Management is mainly supportive and involves secondary stroke prevention measures such as antiplatelet therapy, blood pressure control, and rehabilitation. In select cases, if an embolic cause is suspected (e.g., dissection), additional interventions may be warranted. For pregnant or lactating patients, the use of antiplatelet agents is generally safe, though decisions should be individualized with obstetric consultation to balance maternal and fetal risks.",
        "option_analysis": "The marked correct answer is lateral medullary syndrome, which is supported by the clinical picture provided. Other options, such as medial medullary syndrome or cerebellar infarction, would present with significantly different findings (e.g., prominent motor deficits or different sensory loss patterns) and therefore do not match the described syndrome.",
        "clinical_pearls": "1. Crossed sensory findings (ipsilateral facial and contralateral body deficits) are a key diagnostic clue for brainstem strokes like lateral medullary syndrome. 2. Wallenberg syndrome most commonly results from occlusion of the PICA. 3. Early recognition and supportive management are essential for optimal recovery.",
        "current_evidence": "Recent advances in neuroimaging have enhanced the diagnosis and localization of brainstem infarcts. Current stroke guidelines emphasize the importance of early rehabilitation and risk factor management in patients with lateral medullary syndrome to optimize long-term outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993018",
    "fields": {
      "question_number": "150",
      "question_text": "65-year-old man presents with an abrupt severe headache and drowsiness. His past medical history is remarkable for alcohol and tobacco abuse. On admission, his blood pressure is 150/90 mm hg, GCS score is 13, and the pupils are both 3 mm and reactive. A non-contrast CT of the head reveals a 10 cm right basal ganglia hemorrhage with extension into the right lateral and third ventricles. Two hours later he is noted to be poorly responsive, and his GCS falls to 9. Repeat CT shows no change in hematoma size but marked enlargement of the third and lateral ventricles. Which of the following interventions is most likely to improve this patient's clinical status?",
      "options": {
        "A": "Administration of mannitol",
        "B": "Administration of thiamine",
        "C": "External ventricular drainage",
        "D": "Hypothermia"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Intracerebral hemorrhage, particularly when it involves the basal ganglia with extension into the ventricular system, can lead to obstructive hydrocephalus. This complication is a critical emergency because it causes a rapid increase in intracranial pressure and neurological deterioration.",
        "pathophysiology": "In hemorrhagic strokes with intraventricular extension, blood can obstruct cerebrospinal fluid (CSF) pathways, resulting in hydrocephalus. Elevated intracranial pressure from ventricular enlargement leads to decreased cerebral perfusion and subsequent decline in neurological status. In this case, the initial bleed is stable, but the secondary hydrocephalus causes the deterioration.",
        "clinical_correlation": "The patient\u2019s falling Glasgow Coma Scale (GCS) score, despite no change in hematoma size, is indicative of the deleterious effects of hydrocephalus. This clinical picture necessitates urgent intervention to relieve the CSF obstruction and reduce intracranial pressure.",
        "diagnostic_approach": "Serial non-contrast CT scans are used to monitor for changes in hematoma size and ventricular enlargement. Differential diagnoses include expanding hematoma, cerebral edema, or re-bleeding. When CT shows marked ventricular enlargement without hematoma progression, hydrocephalus is identified as the cause of the decline.",
        "classification_and_neurology": "Intracerebral hemorrhage is classified under hemorrhagic strokes, distinct from ischemic strokes. The hemorrhage here is spontaneous, non-traumatic, and secondary to small vessel disease (hypertensive arteriopathy). The presence of intraventricular hemorrhage (IVH) and obstructive hydrocephalus are important subclassifications influencing prognosis and management. The American Heart Association/American Stroke Association (AHA/ASA) stroke guidelines classify ICH based on location (lobar, deep, cerebellar, brainstem), volume, and presence of IVH. Hydrocephalus is recognized as a complication rather than a separate disease entity, but it significantly impacts treatment decisions. Advances in classification emphasize integrating clinical, radiological, and pathophysiological data to guide management and predict outcomes.",
        "classification_and_nosology": "This case is classified as a hemorrhagic stroke with secondary obstructive hydrocephalus. It represents a common complication of intraventricular hemorrhage.",
        "management_principles": "The first-line intervention in obstructive hydrocephalus secondary to intraventricular hemorrhage is external ventricular drainage (EVD), which directly relieves intracranial pressure by diverting excess CSF. Medical treatments like mannitol may reduce cerebral edema but are not effective in resolving ventricular obstruction. In pregnant or lactating patients, EVD placement can be performed safely with appropriate multidisciplinary support and monitoring.",
        "option_analysis": "Option A (Administration of mannitol) may lower intracranial pressure via osmotic effects but does not relieve CSF obstruction. Option B (Administration of thiamine) is irrelevant to the emergency scenario. Option D (Hypothermia) is not standard of care for hydrocephalus. Option C (External ventricular drainage) is correct as it directly addresses the obstructive hydrocephalus and improves CSF outflow.",
        "clinical_pearls": "1. Intracerebral hemorrhage with intraventricular extension is high risk for developing obstructive hydrocephalus, which can rapidly impair consciousness. 2. EVD is the definitive treatment for hydrocephalus in this setting. 3. Serial imaging is critical in detecting complications even if the primary hemorrhage remains unchanged.",
        "current_evidence": "Recent research continues to support the use of EVD in cases of intraventricular hemorrhage with hydrocephalus, with studies noting improved outcomes when drainage is implemented promptly. Guidelines advocate for aggressive management of hydrocephalus to prevent secondary brain injury."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_4.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993019",
    "fields": {
      "question_number": "151",
      "question_text": "Patient was playing tennis then brought to emergency room after car accident was fine, doing well. CT brain and labs comes up normal BP160/95. Two hours later developed left hemianopia. he had history of migraine since age of 15, with recurrent episode every 6 months. What is the diagnosis?",
      "options": {
        "A": "Vert dissection",
        "B": "RCVS",
        "C": "PRESS",
        "D": "ICA stenosis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Arterial dissection refers to a tear in the vessel wall, allowing blood to enter the arterial wall and form an intramural hematoma. This process can result in luminal narrowing, thrombus formation, or embolization, eventually leading to ischemic events. In the context of trauma, even minor injuries can precipitate such dissections, involving either the cervical internal carotid or vertebral arteries.",
        "pathophysiology": "In a vertebral dissection the trauma (in this case, a car accident) may produce an intimal tear in the vertebral artery. Blood then enters the vessel wall, causing a hematoma that may narrow the lumen or generate emboli. Embolic events can travel to the posterior cerebral circulation (via the basilar artery and posterior cerebral arteries) and result in focal cerebral ischemia, such as an occipital infarct producing homonymous hemianopia.",
        "clinical_correlation": "The patient\u2019s development of a left homonymous hemianopia (loss of the left visual field in both eyes) suggests a right-sided occipital lobe stroke. Given the history of trauma and the potential for arterial injury (even in the setting of a normal initial CT scan), vertebral dissection is a strong consideration. Although the patient has a long history of migraine, this is likely a red herring in the context of a new vascular insult.",
        "diagnostic_approach": "Initial imaging with a non-contrast CT head can be normal in early dissection. When suspicion remains high, vascular imaging with CT angiography (CTA) or MR angiography (MRA) of the neck is indicated to evaluate for arterial dissection. Differential diagnoses include carotid artery dissection (which often presents with ipsilateral neck pain and Horner\u2019s syndrome), PRES (Posterior Reversible Encephalopathy Syndrome, usually associated with severe hypertension and vasogenic edema on MRI), and Reversible Cerebral Vasoconstriction Syndrome (RCVS, which usually presents with thunderclap headaches and multifocal vasospasm).",
        "classification_and_neurology": "Vertebral artery dissection is classified under **cervical artery dissections (CADs)**, which include dissections of the internal carotid and vertebral arteries. CADs are a subset of ischemic strokes, specifically under the category of **stroke of other determined etiology** in the TOAST classification system.   - CADs are distinguished from other stroke etiologies by their unique mechanism involving arterial wall injury. - The classification of dissections depends on anatomical location (extracranial vs intracranial), vessel involved (vertebral vs carotid), and clinical presentation. - **Reversible cerebral vasoconstriction syndrome (RCVS)** and **posterior reversible encephalopathy syndrome (PRES)** are distinct clinical entities with different pathophysiology and clinical course. - The nosology has evolved with advances in imaging and molecular understanding, emphasizing the importance of vascular imaging for accurate diagnosis.",
        "classification_and_nosology": "Cervico\u2010cranial arterial dissections fall under cerebrovascular disorders. They are classified by the arterial territory involved \u2013 either carotid or vertebral \u2013 and are important causes of stroke in younger patients, especially following trauma.",
        "management_principles": "The mainstay of treatment for vertebral dissection is antithrombotic therapy to reduce the risk of thromboembolic stroke. Options include antiplatelet agents (such as aspirin) or anticoagulation with heparin followed by warfarin. Current guidelines suggest that there is no clear superiority between antiplatelet and anticoagulant therapy \u2013 the choice is individualized. In pregnant or lactating patients, low molecular weight heparin is generally preferred due to its safety profile, and low-dose aspirin can be considered if antiplatelet therapy is indicated.",
        "option_analysis": "Option A (Vertebral dissection) is correct because the clinical scenario (trauma followed by delayed onset of a focal posterior circulation deficit) is most consistent with a vertebral arterial dissection. Option B (RCVS) is typically associated with thunderclap headache and multifocal vasospasm rather than focal visual deficits. Option C (PRESS, likely referring to PRES) is linked to severe hypertension and vasogenic edema typically seen on MRI rather than a sudden focal deficit following trauma. Option D (ICA stenosis) is usually a chronic process and does not fit the acute traumatic setting.",
        "clinical_pearls": "1. Always consider arterial dissection in patients with recent trauma, even if the initial CT scan is normal. 2. Posterior circulation strokes, like those producing homonymous hemianopia, may result from vertebral artery injury. 3. A history of migraine can mislead but should not distract from an evaluation for stroke in the context of trauma.",
        "current_evidence": "Recent studies and updated stroke guidelines support a high index of suspicion for cervico\u2010cranial dissections in trauma patients. There is ongoing research regarding the optimal antithrombotic management (antiplatelet versus anticoagulant) with current evidence suggesting similar outcomes, thus favoring individualized treatment approaches."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993060",
    "fields": {
      "question_number": "100",
      "question_text": "patient with acute stroke on dabigatrin for AF, the patient underwent for thrombectomy, the patient developed hemorrhage over MCA territory, what to give:",
      "options": {
        "A": "Vit K.",
        "B": "Idarocizumab."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Arterial dissection refers to a tear in the vessel wall, allowing blood to enter the arterial wall and form an intramural hematoma. This process can result in luminal narrowing, thrombus formation, or embolization, eventually leading to ischemic events. In the context of trauma, even minor injuries can precipitate such dissections, involving either the cervical internal carotid or vertebral arteries.",
        "pathophysiology": "In a vertebral dissection the trauma (in this case, a car accident) may produce an intimal tear in the vertebral artery. Blood then enters the vessel wall, causing a hematoma that may narrow the lumen or generate emboli. Embolic events can travel to the posterior cerebral circulation (via the basilar artery and posterior cerebral arteries) and result in focal cerebral ischemia, such as an occipital infarct producing homonymous hemianopia.",
        "clinical_correlation": "The patient\u2019s development of a left homonymous hemianopia (loss of the left visual field in both eyes) suggests a right-sided occipital lobe stroke. Given the history of trauma and the potential for arterial injury (even in the setting of a normal initial CT scan), vertebral dissection is a strong consideration. Although the patient has a long history of migraine, this is likely a red herring in the context of a new vascular insult.",
        "diagnostic_approach": "Initial imaging with a non-contrast CT head can be normal in early dissection. When suspicion remains high, vascular imaging with CT angiography (CTA) or MR angiography (MRA) of the neck is indicated to evaluate for arterial dissection. Differential diagnoses include carotid artery dissection (which often presents with ipsilateral neck pain and Horner\u2019s syndrome), PRES (Posterior Reversible Encephalopathy Syndrome, usually associated with severe hypertension and vasogenic edema on MRI), and Reversible Cerebral Vasoconstriction Syndrome (RCVS, which usually presents with thunderclap headaches and multifocal vasospasm).",
        "classification_and_neurology": "Hemorrhagic transformation of ischemic stroke is classified into hemorrhagic infarction (HI) and parenchymal hematoma (PH) types, with subtypes based on imaging characteristics and clinical severity. Anticoagulant-associated hemorrhages constitute a distinct subgroup within intracerebral hemorrhages, requiring tailored management. Dabigatran belongs to the class of direct oral anticoagulants (DOACs), specifically direct thrombin inhibitors, distinct from vitamin K antagonists (VKAs) like warfarin. The classification of anticoagulant-related hemorrhages has evolved with the advent of DOACs, necessitating new reversal strategies and guidelines. Current consensus emphasizes specific reversal agents over nonspecific treatments to optimize outcomes and reduce complications.",
        "classification_and_nosology": "Cervico\u2010cranial arterial dissections fall under cerebrovascular disorders. They are classified by the arterial territory involved \u2013 either carotid or vertebral \u2013 and are important causes of stroke in younger patients, especially following trauma.",
        "management_principles": "The mainstay of treatment for vertebral dissection is antithrombotic therapy to reduce the risk of thromboembolic stroke. Options include antiplatelet agents (such as aspirin) or anticoagulation with heparin followed by warfarin. Current guidelines suggest that there is no clear superiority between antiplatelet and anticoagulant therapy \u2013 the choice is individualized. In pregnant or lactating patients, low molecular weight heparin is generally preferred due to its safety profile, and low-dose aspirin can be considered if antiplatelet therapy is indicated.",
        "option_analysis": "Option A (Vertebral dissection) is correct because the clinical scenario (trauma followed by delayed onset of a focal posterior circulation deficit) is most consistent with a vertebral arterial dissection. Option B (RCVS) is typically associated with thunderclap headache and multifocal vasospasm rather than focal visual deficits. Option C (PRESS, likely referring to PRES) is linked to severe hypertension and vasogenic edema typically seen on MRI rather than a sudden focal deficit following trauma. Option D (ICA stenosis) is usually a chronic process and does not fit the acute traumatic setting.",
        "clinical_pearls": "1. Always consider arterial dissection in patients with recent trauma, even if the initial CT scan is normal. 2. Posterior circulation strokes, like those producing homonymous hemianopia, may result from vertebral artery injury. 3. A history of migraine can mislead but should not distract from an evaluation for stroke in the context of trauma.",
        "current_evidence": "Recent studies and updated stroke guidelines support a high index of suspicion for cervico\u2010cranial dissections in trauma patients. There is ongoing research regarding the optimal antithrombotic management (antiplatelet versus anticoagulant) with current evidence suggesting similar outcomes, thus favoring individualized treatment approaches."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993061",
    "fields": {
      "question_number": "101",
      "question_text": "patient with acute stroke received tpa then developed ICH what to give:",
      "options": {
        "A": "Cryoprecipitate."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Arterial dissection refers to a tear in the vessel wall, allowing blood to enter the arterial wall and form an intramural hematoma. This process can result in luminal narrowing, thrombus formation, or embolization, eventually leading to ischemic events. In the context of trauma, even minor injuries can precipitate such dissections, involving either the cervical internal carotid or vertebral arteries.",
        "pathophysiology": "In a vertebral dissection the trauma (in this case, a car accident) may produce an intimal tear in the vertebral artery. Blood then enters the vessel wall, causing a hematoma that may narrow the lumen or generate emboli. Embolic events can travel to the posterior cerebral circulation (via the basilar artery and posterior cerebral arteries) and result in focal cerebral ischemia, such as an occipital infarct producing homonymous hemianopia.",
        "clinical_correlation": "The patient\u2019s development of a left homonymous hemianopia (loss of the left visual field in both eyes) suggests a right-sided occipital lobe stroke. Given the history of trauma and the potential for arterial injury (even in the setting of a normal initial CT scan), vertebral dissection is a strong consideration. Although the patient has a long history of migraine, this is likely a red herring in the context of a new vascular insult.",
        "diagnostic_approach": "Initial imaging with a non-contrast CT head can be normal in early dissection. When suspicion remains high, vascular imaging with CT angiography (CTA) or MR angiography (MRA) of the neck is indicated to evaluate for arterial dissection. Differential diagnoses include carotid artery dissection (which often presents with ipsilateral neck pain and Horner\u2019s syndrome), PRES (Posterior Reversible Encephalopathy Syndrome, usually associated with severe hypertension and vasogenic edema on MRI), and Reversible Cerebral Vasoconstriction Syndrome (RCVS, which usually presents with thunderclap headaches and multifocal vasospasm).",
        "classification_and_neurology": "Hemorrhagic transformation after ischemic stroke is classified based on radiological appearance and clinical severity. The ECASS (European Cooperative Acute Stroke Study) classification divides HT into hemorrhagic infarction (HI) types 1 and 2 (petechial hemorrhages without mass effect) and parenchymal hematoma (PH) types 1 and 2 (more confluent hematomas with mass effect). Symptomatic ICH post-thrombolysis falls under PH2 in many cases. This condition is considered a complication of ischemic stroke and thrombolytic therapy rather than a primary hemorrhagic stroke subtype. Nosologically, it resides within cerebrovascular diseases, specifically ischemic stroke complications. Classification systems have evolved to improve prognostication and treatment decisions, with current consensus emphasizing clinical context and imaging features.",
        "classification_and_nosology": "Cervico\u2010cranial arterial dissections fall under cerebrovascular disorders. They are classified by the arterial territory involved \u2013 either carotid or vertebral \u2013 and are important causes of stroke in younger patients, especially following trauma.",
        "management_principles": "The mainstay of treatment for vertebral dissection is antithrombotic therapy to reduce the risk of thromboembolic stroke. Options include antiplatelet agents (such as aspirin) or anticoagulation with heparin followed by warfarin. Current guidelines suggest that there is no clear superiority between antiplatelet and anticoagulant therapy \u2013 the choice is individualized. In pregnant or lactating patients, low molecular weight heparin is generally preferred due to its safety profile, and low-dose aspirin can be considered if antiplatelet therapy is indicated.",
        "option_analysis": "Option A (Vertebral dissection) is correct because the clinical scenario (trauma followed by delayed onset of a focal posterior circulation deficit) is most consistent with a vertebral arterial dissection. Option B (RCVS) is typically associated with thunderclap headache and multifocal vasospasm rather than focal visual deficits. Option C (PRESS, likely referring to PRES) is linked to severe hypertension and vasogenic edema typically seen on MRI rather than a sudden focal deficit following trauma. Option D (ICA stenosis) is usually a chronic process and does not fit the acute traumatic setting.",
        "clinical_pearls": "1. Always consider arterial dissection in patients with recent trauma, even if the initial CT scan is normal. 2. Posterior circulation strokes, like those producing homonymous hemianopia, may result from vertebral artery injury. 3. A history of migraine can mislead but should not distract from an evaluation for stroke in the context of trauma.",
        "current_evidence": "Recent studies and updated stroke guidelines support a high index of suspicion for cervico\u2010cranial dissections in trauma patients. There is ongoing research regarding the optimal antithrombotic management (antiplatelet versus anticoagulant) with current evidence suggesting similar outcomes, thus favoring individualized treatment approaches."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993062",
    "fields": {
      "question_number": "102",
      "question_text": "what is the mechanism of the following antiplatelets is correct:",
      "options": {
        "A": "Ticagrelor antagonist of p2y12"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Arterial dissection refers to a tear in the vessel wall, allowing blood to enter the arterial wall and form an intramural hematoma. This process can result in luminal narrowing, thrombus formation, or embolization, eventually leading to ischemic events. In the context of trauma, even minor injuries can precipitate such dissections, involving either the cervical internal carotid or vertebral arteries.",
        "pathophysiology": "In a vertebral dissection the trauma (in this case, a car accident) may produce an intimal tear in the vertebral artery. Blood then enters the vessel wall, causing a hematoma that may narrow the lumen or generate emboli. Embolic events can travel to the posterior cerebral circulation (via the basilar artery and posterior cerebral arteries) and result in focal cerebral ischemia, such as an occipital infarct producing homonymous hemianopia.",
        "clinical_correlation": "The patient\u2019s development of a left homonymous hemianopia (loss of the left visual field in both eyes) suggests a right-sided occipital lobe stroke. Given the history of trauma and the potential for arterial injury (even in the setting of a normal initial CT scan), vertebral dissection is a strong consideration. Although the patient has a long history of migraine, this is likely a red herring in the context of a new vascular insult.",
        "diagnostic_approach": "Initial imaging with a non-contrast CT head can be normal in early dissection. When suspicion remains high, vascular imaging with CT angiography (CTA) or MR angiography (MRA) of the neck is indicated to evaluate for arterial dissection. Differential diagnoses include carotid artery dissection (which often presents with ipsilateral neck pain and Horner\u2019s syndrome), PRES (Posterior Reversible Encephalopathy Syndrome, usually associated with severe hypertension and vasogenic edema on MRI), and Reversible Cerebral Vasoconstriction Syndrome (RCVS, which usually presents with thunderclap headaches and multifocal vasospasm).",
        "classification_and_neurology": "Antiplatelet agents are classified based on their molecular targets and mechanisms: cyclooxygenase inhibitors (aspirin), P2Y12 receptor antagonists (clopidogrel, prasugrel, ticagrelor), glycoprotein IIb/IIIa inhibitors, phosphodiesterase inhibitors, and others. Ticagrelor belongs to the class of direct-acting, reversible P2Y12 receptor antagonists, distinct from thienopyridines which are irreversible prodrugs. The classification of antiplatelets is important for selecting therapy based on patient-specific factors such as genetic polymorphisms affecting drug metabolism (e.g., CYP2C19 variants impacting clopidogrel activation). Nosologically, antiplatelet agents are integral to secondary prevention in ischemic stroke, classified under cerebrovascular pharmacotherapy within neurology and cardiology guidelines. Over time, classification systems have evolved with the introduction of novel agents like ticagrelor and cangrelor, reflecting advances in pharmacodynamics and clinical trial evidence. Some debate exists regarding optimal agent selection in stroke prevention, especially comparing monotherapy versus dual antiplatelet regimens.",
        "classification_and_nosology": "Cervico\u2010cranial arterial dissections fall under cerebrovascular disorders. They are classified by the arterial territory involved \u2013 either carotid or vertebral \u2013 and are important causes of stroke in younger patients, especially following trauma.",
        "management_principles": "The mainstay of treatment for vertebral dissection is antithrombotic therapy to reduce the risk of thromboembolic stroke. Options include antiplatelet agents (such as aspirin) or anticoagulation with heparin followed by warfarin. Current guidelines suggest that there is no clear superiority between antiplatelet and anticoagulant therapy \u2013 the choice is individualized. In pregnant or lactating patients, low molecular weight heparin is generally preferred due to its safety profile, and low-dose aspirin can be considered if antiplatelet therapy is indicated.",
        "option_analysis": "Option A (Vertebral dissection) is correct because the clinical scenario (trauma followed by delayed onset of a focal posterior circulation deficit) is most consistent with a vertebral arterial dissection. Option B (RCVS) is typically associated with thunderclap headache and multifocal vasospasm rather than focal visual deficits. Option C (PRESS, likely referring to PRES) is linked to severe hypertension and vasogenic edema typically seen on MRI rather than a sudden focal deficit following trauma. Option D (ICA stenosis) is usually a chronic process and does not fit the acute traumatic setting.",
        "clinical_pearls": "1. Always consider arterial dissection in patients with recent trauma, even if the initial CT scan is normal. 2. Posterior circulation strokes, like those producing homonymous hemianopia, may result from vertebral artery injury. 3. A history of migraine can mislead but should not distract from an evaluation for stroke in the context of trauma.",
        "current_evidence": "Recent studies and updated stroke guidelines support a high index of suspicion for cervico\u2010cranial dissections in trauma patients. There is ongoing research regarding the optimal antithrombotic management (antiplatelet versus anticoagulant) with current evidence suggesting similar outcomes, thus favoring individualized treatment approaches."
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
