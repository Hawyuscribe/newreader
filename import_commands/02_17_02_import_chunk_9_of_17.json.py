
# Import batch 2 of 3 from chunk_9_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993271",
    "fields": {
      "question_number": "133",
      "question_text": "22 YO, F, medically free, on Combined OCB, came with headache, CTV showed SSS thrombosis, what is true.",
      "options": {
        "A": "She has clear cause and no need workup",
        "B": "Do thrombophilia workup"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral venous sinus thrombosis (CVST) is a type of stroke resulting from thrombosis in the dural venous sinuses. In young women, the use of combined oral contraceptive pills (COCP) is a well\u2010recognized, reversible risk factor.",
        "pathophysiology": "Exogenous estrogen from COCPs can increase the production of coagulation factors and reduce anticoagulant proteins, tipping the hemostatic balance toward thrombosis. When thrombosis occurs in the superior sagittal sinus, it results in impaired venous drainage and increased intracranial pressure.",
        "clinical_correlation": "CVST commonly presents in young women with headache, seizures, and possibly focal neurological deficits. In this case, a 22\u2010year\u2010old female on COCPs with headache and imaging evidence of superior sagittal sinus thrombosis demonstrates a classic clinical scenario.",
        "diagnostic_approach": "The diagnosis is confirmed through imaging studies such as CT venography (CTV) or MR venography (MRV). Differential diagnoses include migraine, idiopathic intracranial hypertension, and other causes of headache. A thorough history often reveals a provoking factor like COCP use.",
        "classification_and_neurology": "CVST is classified under cerebrovascular diseases in the International Classification of Diseases (ICD-11) and recognized as a distinct subtype of stroke by the American Heart Association/American Stroke Association (AHA/ASA). It belongs to the broader category of venous thromboembolic disorders and is differentiated from arterial ischemic stroke and hemorrhagic stroke.  Etiologically, CVST can be classified into:  - **Provoked CVST:** Associated with identifiable risk factors such as pregnancy, puerperium, OCP use, infection, malignancy, or trauma. - **Unprovoked CVST:** No obvious risk factors, often warranting extensive thrombophilia workup.  This classification guides diagnostic and therapeutic strategies. The classification systems have evolved with advances in imaging and thrombophilia understanding, emphasizing the importance of identifying underlying causes to prevent recurrence.",
        "classification_and_nosology": "CVST is classified as a form of cerebrovascular venous thrombosis and is often categorized based on the presence of provoking factors. When a transient risk factor (such as COCP use) is identified, the event is considered provoked.",
        "management_principles": "The mainstay of treatment for CVST is anticoagulation (typically with low-molecular-weight heparin initially, followed by oral anticoagulants). It is advisable to defer extensive thrombophilia testing during the acute phase because acute phase reactants and anticoagulation can alter results. In pregnant or lactating women, low-molecular-weight heparin is favored due to its safety profile.",
        "option_analysis": "Option A states that because there is a clear provoking factor (COCP use), no further workup is immediately necessary, which is in line with many guidelines. Option B (perform a thrombophilia workup) might be considered in cases with no clear cause or a family history of thrombosis, but in this scenario, the COCP is a sufficient explanation. Testing for thrombophilia is usually deferred until after the acute phase (often several months later) to avoid confounding results.",
        "clinical_pearls": "1. In a young female with CVST and COCP use, the contraceptive is typically the provocative risk factor, and routine thrombophilia screening can usually be deferred. 2. Repeat thrombophilia testing may be performed after the acute phase has resolved, as initial tests can be inaccurate due to the acute event and anticoagulant effects. 3. Anticoagulation remains the cornerstone of CVST management despite any hemorrhagic transformation on imaging.",
        "current_evidence": "Current guidelines, including those from the American Heart Association, suggest that in the setting of a clear provoking factor, extensive thrombophilia evaluation is not mandatory during the acute phase of CVST. This approach helps avoid unnecessary interventions and misinterpretation of results."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993272",
    "fields": {
      "question_number": "134",
      "question_text": "Lady on OCP came with seizure, headache, CT normal, next.",
      "options": {
        "A": "LP",
        "B": "EEG",
        "C": "CTV"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "In women on oral contraceptives presenting with headache and seizures, cerebral venous sinus thrombosis (CVST) is a prime consideration\u2014even when the initial non-contrast CT scan is normal. CVST often requires advanced imaging for diagnosis.",
        "pathophysiology": "CVST results from clot formation in the cerebral venous sinuses, leading to impaired venous drainage, increased intracranial pressure, and potential venous infarctions or hemorrhages. OCP use is a risk factor because it creates a hypercoagulable state that predisposes to thrombosis.",
        "clinical_correlation": "Clinically, patients may present with headache, seizures, focal neurological deficits, or papilledema. A normal CT scan does not exclude CVST; therefore, further imaging with dedicated venographic techniques is warranted.",
        "diagnostic_approach": "When suspicion for CVST remains high despite a normal CT, CT venography (CTV) or MR venography (MRV) should be performed to visualize the venous system and detect the presence of thrombi. Differential diagnoses in such cases include primary seizure disorders and meningitis, but the OCP history directs attention toward thrombotic causes.",
        "classification_and_neurology": "CVST is classified under cerebrovascular diseases affecting venous rather than arterial circulation. It belongs to the broader category of stroke syndromes but differs in pathophysiology and management. The International Classification of Diseases (ICD-11) classifies CVST under 'Cerebral venous thrombosis and sinus thrombosis.' CVST can be idiopathic or secondary to risk factors like prothrombotic states, infections, or trauma. It is distinct from arterial ischemic stroke and hemorrhagic stroke but may cause secondary hemorrhagic infarctions. Classification also considers the location of thrombosis (e.g., superior sagittal sinus, transverse sinus) and clinical severity. Nosological frameworks emphasize the importance of recognizing CVST as a distinct entity due to its unique therapeutic implications. Some controversy exists regarding the best imaging modality for diagnosis, but consensus supports venous imaging in suspected cases.",
        "classification_and_nosology": "CVST is categorized under venous strokes and is further classified based on the involved sinus (in this case, likely the superior sagittal sinus is suspected).",
        "management_principles": "Once CVST is diagnosed, the first-line treatment is anticoagulation (typically with low-molecular-weight heparin followed by warfarin or a direct oral anticoagulant). In cases where the patient is pregnant or lactating, LMWH is the preferred treatment due to its established safety profile in these populations.",
        "option_analysis": "Option A (LP) is not indicated in this scenario because lumbar puncture would not visualize venous clot and may risk herniation if intracranial pressure is high. Option B (EEG) is used to evaluate seizure activity but does not address the underlying etiology. Option C (CTV) is the correct next step to evaluate for CVST. The absence of a fourth option confirms that CTV is the most sensitive and specific noninvasive test in this context.",
        "clinical_pearls": "1. A normal non-contrast CT does not rule out CVST; always consider venography in high-risk patients. 2. In patients on OCPs with new-onset headache and seizures, CVST is a critical diagnosis to exclude. 3. Early diagnosis and management of CVST with appropriate imaging can substantially improve outcomes.",
        "current_evidence": "Recent guidelines emphasize the use of CT venography as a critical tool in the evaluation of suspected CVST, given its high sensitivity and rapid availability. Studies continue to support early anticoagulation as the cornerstone of treatment even if initial CT imaging appears normal."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993273",
    "fields": {
      "question_number": "135",
      "question_text": "This pic patient will came with (image of brain MRI) (Similar but not the same).",
      "options": {
        "A": "Pure motor",
        "B": "Pure sensory",
        "C": "Mixed",
        "D": "Clumsy"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Lacunar strokes are small subcortical infarctions typically caused by occlusion of small perforating arteries. One well\u2010recognized lacunar syndrome is the pure sensory stroke, which is usually due to an infarct in the ventral posterolateral (VPL) nucleus of the thalamus.",
        "pathophysiology": "Chronic hypertension and diabetes can lead to lipohyalinosis of small penetrating arteries. When one of these vessels supplying the thalamus becomes occluded, it disrupts the sensory pathways without affecting motor fibers. This results in an infarct that produces isolated sensory deficits in the contralateral hemibody.",
        "clinical_correlation": "Patients with a pure sensory stroke typically present with sudden onset contralateral numbness or loss of sensory modalities (pain, temperature, proprioception) without motor weakness. An MRI demonstrating a small lacunar infarct in the thalamus correlates with these clinical findings.",
        "diagnostic_approach": "Magnetic resonance imaging (especially DWI) is highly sensitive for detecting lacunar infarcts. Differential diagnoses include: (a) infarcts in the posterior limb of the internal capsule (which cause pure motor deficits), (b) sensorimotor strokes (when both motor and sensory functions are affected) and (c) demyelinating diseases. Detailed clinical history and risk factor assessment help differentiate these entities.",
        "classification_and_neurology": "Lacunar strokes are classified under ischemic stroke subtypes in the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system as 'small vessel occlusion.' This category distinguishes lacunar infarcts from large artery atherosclerosis, cardioembolism, and other causes.  Within lacunar syndromes, the clinical classification includes pure motor, pure sensory, sensorimotor, ataxic hemiparesis, and clumsy hand dysarthria. These syndromes reflect the anatomical location of the infarct and the fiber tracts involved.  Historically, lacunar strokes were first characterized by C. Miller Fisher in the 1960s based on clinical-radiological correlation. Modern imaging with MRI has refined the classification by confirming lesion size and location.  Controversies exist regarding the exact pathophysiological mechanisms, with some arguing microatheroma versus lipohyalinosis predominance, but consensus remains that small vessel disease underlies these strokes. The classification continues to evolve with advances in neuroimaging and molecular pathology.",
        "classification_and_nosology": "Lacunar strokes are classified under small vessel disease. They are further subdivided into pure motor stroke, pure sensory stroke, sensorimotor stroke, and ataxic hemiparesis. A pure sensory stroke is a distinct category typically linked to an infarct of the thalamic VPL region.",
        "management_principles": "Acute management includes antiplatelet therapy (e.g., aspirin), aggressive blood pressure and risk factor control, and secondary prevention strategies. In pregnant or lactating patients with stroke, low-dose aspirin is generally considered safe with careful monitoring, and risk factor modification is essential.",
        "option_analysis": "Option A (Pure motor) is seen with lacunar infarcts in areas like the posterior limb of the internal capsule. Option B (Pure sensory) is correct because a thalamic lacunar infarct typically leads to isolated sensory deficits. Option C (Mixed) would be expected with sensorimotor strokes where both motor and sensory areas are involved. Option D (Clumsy) hints at ataxic hemiparesis, which involves a combination of motor weakness and clumsiness \u2013 not isolated sensory loss.",
        "clinical_pearls": "1. A pure sensory stroke is most commonly due to a lacunar infarct in the thalamic VPL nucleus. 2. Appropriate blood pressure control is crucial in preventing subsequent small vessel damage.",
        "current_evidence": "Recent guidelines emphasize the importance of managing vascular risk factors to prevent lacunar strokes. High-resolution MRI and DWI are the imaging modalities of choice for early detection, and evidence supports the use of antiplatelet agents as part of secondary prevention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_15.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993274",
    "fields": {
      "question_number": "136",
      "question_text": "82 YO female with good functional status although she has mild osteoporosis in her knees related to her age, came with NIHSS = 20 in term of aphasia, right side weakness, she presented within 60 min, CT done within 30 min, BP 220/110, next step.",
      "options": {
        "A": "Give tpa",
        "B": "BP management",
        "C": "CTA",
        "D": "Mechanical Thrombectomy"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke management follows a time\u2010sensitive approach with reperfusion therapy (IV tPA and/or mechanical thrombectomy) being standard treatments. However, proper patient selection \u2013 including blood pressure control \u2013 is critical to avoid complications.",
        "pathophysiology": "Extremely elevated blood pressure in the acute stroke setting increases the risk of hemorrhagic conversion, especially if thrombolytic therapy is administered while BP exceeds recommended thresholds. The concern is that high intravascular pressures can disrupt the blood\u2013brain barrier integrity during reperfusion.",
        "clinical_correlation": "In this elderly patient with a high NIHSS score (indicative of a significant ischemic stroke) and severely elevated blood pressure (220/110 mm Hg), immediate control of BP is mandatory before any reperfusion therapy can be initiated. Elevated BP is both a physiological response to stroke and a modifiable risk factor.",
        "diagnostic_approach": "After non-contrast CT rules out hemorrhage, further vascular imaging like CTA is often used to identify large vessel occlusions. Differential considerations include hypertensive encephalopathy and other causes of intracranial hemorrhage; however, the clinical picture along with CT findings supports ischemic stroke. Blood pressure must be addressed promptly to meet criteria for IV thrombolysis.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases (ICD-10 I63) and further subclassified by etiology (e.g., large artery atherosclerosis, cardioembolism, small vessel occlusion). The NIHSS score stratifies severity and guides management urgency. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify ischemic stroke management into hyperacute (within hours), acute (days), and subacute/chronic phases, with specific interventions for each. Blood pressure management in acute ischemic stroke is a well-defined category within stroke care protocols, emphasizing threshold-based decisions for thrombolysis eligibility.",
        "classification_and_nosology": "This case falls under acute ischemic stroke due to large vessel occlusion within the therapeutic window. The patient\u2019s condition is complicated by malignant hypertension, which must be managed prior to reperfusion strategies.",
        "management_principles": "The first step is to lower the BP to at most 185/110 mm Hg using fast-acting intravenous agents (such as labetalol or nicardipine), as per American Heart Association guidelines. Once BP is controlled, IV thrombolysis (if criteria are met) or mechanical thrombectomy (if a large vessel occlusion is present) can be considered. In pregnancy or lactation, choice of antihypertensive agents requires careful consideration; labetalol is often preferred due to its relatively safe profile in these settings.",
        "option_analysis": "Option A (Give tPA) is contraindicated until BP is lowered below the recommended threshold. Option B (BP management) is correct as immediate blood pressure reduction is essential before reperfusion therapies are safe. Option C (CTA) is important in the evaluation process, but with BP at 220/110 mm Hg, the priority is to manage BP first. Option D (Mechanical Thrombectomy) might be considered later, but only after BP is adequately controlled and vascular imaging confirms eligibility.",
        "clinical_pearls": "1. For IV tPA eligibility, blood pressure must be below 185/110 mm Hg. 2. Rapid control of hypertension in acute stroke is crucial to minimize the risk of hemorrhagic transformation.",
        "current_evidence": "Updated stroke guidelines reinforce that severe hypertension is a contraindication for immediate thrombolysis until it is brought under control. Recent studies support the use of intravenous antihypertensives to safely lower BP in eligible patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993275",
    "fields": {
      "question_number": "137",
      "question_text": "Patient came with left side weakness MRI showed right lacunar stroke, CTA showed severe intracranial right MCA stenosis.",
      "options": {
        "A": "ASA",
        "B": "IV thrombolysis",
        "C": "DAPT",
        "D": "Stent"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Management of intracranial atherosclerotic disease, especially when it is symptomatic, centers on aggressive medical therapy. Dual antiplatelet therapy (DAPT) has been shown to reduce the risk of early recurrent stroke in patients with high-grade stenosis.",
        "pathophysiology": "Intracranial stenosis is primarily due to atherosclerotic plaque buildup, leading to luminal narrowing and an increased risk for thromboembolism. In the setting of a small infarct (here described as a lacunar infarct) with severe MCA stenosis, the culprit lesion is likely due to branch occlusion from atherosclerotic disease.",
        "clinical_correlation": "The patient with left-sided weakness and MRI findings of a right lacunar infarct, in conjunction with CTA showing severe right MCA stenosis, is at high risk for further ischemic events. This scenario requires medical management rather than procedural intervention in the acute phase.",
        "diagnostic_approach": "Diagnosis is achieved through MRI (confirming infarction) and CTA (demonstrating vascular stenosis). Differential diagnoses include cardioembolic stroke, other large vessel atherosclerotic strokes, or small vessel lipohyalinosis without significant stenosis. The comparative evaluation of imaging findings differentiates intracranial atherosclerotic disease from pure lacunar disease.",
        "classification_and_neurology": "Ischemic strokes are classified by etiology using systems such as the TOAST classification, which categorizes stroke into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), other determined, and undetermined causes. This patient\u2019s stroke fits into the 'large artery atherosclerosis' category given the severe MCA stenosis and radiographic lacunar infarct. Intracranial large artery disease is a subset of large artery atherosclerosis distinct from extracranial carotid disease. The lacunar infarct is a small vessel stroke subtype, but here it occurs in the context of large artery stenosis, illustrating overlap. Classification guides treatment decisions and prognosis. Over time, classification systems have evolved to incorporate imaging and vascular studies for precision.",
        "classification_and_nosology": "Intracranial atherosclerotic disease (ICAD) is a subset of large artery atherosclerosis. When symptomatic, it is classified based on the degree of stenosis and has been predominantly managed medically rather than with interventional procedures.",
        "management_principles": "Based on current guidelines and the SAMMPRIS trial, first-line management for symptomatic intracranial stenosis is aggressive medical therapy with dual antiplatelet treatment (typically aspirin plus clopidogrel) for a defined period along with intensive risk factor management (e.g., blood pressure, lipids, diabetes control). Stenting is generally reserved for cases refractory to medical therapy. In pregnant or lactating patients, antiplatelet choices may be modified; low-dose aspirin is acceptable, although clopidogrel use requires careful risk-benefit evaluation.",
        "option_analysis": "Option A (ASA alone) may be insufficient to prevent recurrence in this high-risk scenario. Option B (IV thrombolysis) applies to acute ischemic stroke intervention but does not address the underlying intracranial stenosis once the acute event has passed. Option C (DAPT) is correct, as it aligns with current recommendations for managing symptomatic intracranial stenosis. Option D (Stent) is not the first-line treatment given that studies such as SAMMPRIS have shown that intensive medical management is superior to stenting in the initial management phase.",
        "clinical_pearls": "1. In symptomatic intracranial atherosclerosis, DAPT plays a crucial role in preventing early recurrent strokes. 2. Stenting is typically reserved for patients who have failed optimal medical management.",
        "current_evidence": "Recent landmark trials, including SAMMPRIS, strongly support an initial management strategy of dual antiplatelet therapy combined with risk factor modification in cases of symptomatic intracranial stenosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993276",
    "fields": {
      "question_number": "138",
      "question_text": "Patient came with history of vertigo, nausea DWI showed (image of brain MRI). Which of the following is correct?",
      "options": {
        "A": "Right side ptosis",
        "B": "Lt uvula deviation",
        "C": "Rt uvula deviation",
        "D": "is not provided."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Posterior circulation strokes, particularly those affecting the brainstem, can produce a variety of cranial nerve deficits. Involvement of structures governing the soft palate, such as the nucleus ambiguus, leads to characteristic findings like uvular deviation.",
        "pathophysiology": "Infarction within the lateral medulla (Wallenberg syndrome) often affects the nucleus ambiguus or its associated fibers, which are responsible for the motor innervation of the palate via the vagus nerve (CN X). When these fibers are compromised on one side, the functioning opposite side exerts a greater pull on the soft palate, causing the uvula to deviate away from the side of the lesion.",
        "clinical_correlation": "A patient presenting with vertigo and nausea is often experiencing a posterior circulation event. If the infarct involves the right lateral medulla, one might expect a right-sided weakness of the palatal muscles, resulting in uvular deviation toward the left. Other associated symptoms can include dysphagia, hoarseness, and ipsilateral Horner\u2019s syndrome.",
        "diagnostic_approach": "Diffusion weighted imaging (DWI) is sensitive for detecting acute infarcts in the brainstem. Differential diagnoses include cerebellar infarcts, vestibular neuritis, and other brainstem syndromes. A careful neurological exam helps to distinguish the patterns; for example, uvular deviation typically indicates involvement of the vagal motor fibers.",
        "classification_and_neurology": "Lateral medullary syndrome is classified as a type of brainstem stroke within the ischemic cerebrovascular disease category. It falls under the TOAST classification as a large artery atherosclerosis or artery-to-artery embolism affecting the posterior circulation. The syndrome is part of the posterior circulation stroke family, distinct from anterior circulation strokes by clinical and imaging features. The classification of brainstem strokes has evolved with imaging advances, allowing precise lesion localization and subtype identification. There is consensus to categorize strokes by vascular territory and clinical syndrome to guide management. Some debate persists on the best classification for small vessel versus large artery strokes in the brainstem, but lateral medullary syndrome is well-established as a PICA territory infarct.",
        "classification_and_nosology": "Lateral medullary syndrome (Wallenberg syndrome) is a brainstem stroke typically due to occlusion of the posterior inferior cerebellar artery (PICA). Cranial nerve signs such as uvular deviation are part of its clinical spectrum when the nucleus ambiguus is involved.",
        "management_principles": "Acute management focuses on supportive treatment, secondary prevention with antithrombotic therapy, and aggressive risk factor modification. In pregnant or lactating patients, management follows similar principles, but medication choices (including antiplatelets) must consider fetal and neonatal safety. Rehabilitation for swallowing and speech may also be required.",
        "option_analysis": "Option A (Right side ptosis) may be a feature of Horner\u2019s syndrome seen in lateral medullary infarcts, but it is not the specific sign tested here. Option B (Left uvula deviation) is correct for a right-sided lesion affecting the nucleus ambiguus, as the palate deviates away from the affected side. Option C (Right uvula deviation) would imply a left-sided lesion. Option D is not provided.",
        "clinical_pearls": "1. In lesions affecting the nucleus ambiguus, the uvula deviates away from the side of the lesion. 2. Vertigo and nausea in a stroke patient should prompt evaluation of the posterior circulation and brainstem structures.",
        "current_evidence": "Recent studies and guidelines continue to emphasize the importance of early recognition of posterior circulation strokes. Advanced imaging techniques have enhanced the diagnostic accuracy for brainstem infarcts, and multidisciplinary management remains the standard of care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_15.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993277",
    "fields": {
      "question_number": "139",
      "question_text": "70 YO, M, Came with this MRI.",
      "options": {
        "A": "Watershed",
        "B": "Cardioembolic",
        "C": "Small Vessle Disease",
        "D": "Vasculitis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Watershed infarcts are a type of ischemic stroke that occur in the border zones between two major cerebral arterial territories (eg, between the anterior and middle cerebral arteries or between the middle and posterior cerebral arteries). They typically result from systemic hypoperfusion or severe carotid disease, leading to reduced blood flow in these vulnerable border regions.",
        "pathophysiology": "In watershed strokes, the distal fields of two arterial systems are most vulnerable to a drop in cerebral perfusion pressure. In elderly patients, chronic vascular disease or severe hypotension (or carotid occlusive disease) can lead to these borderzone infarcts. The compromised perfusion in these regions causes ischemia and infarction. Recent evidence underscores the importance of maintaining optimal hemodynamic stability, especially in patients with preexisting carotid disease.",
        "clinical_correlation": "Patients with watershed infarcts may present with symptoms that correlate with the affected borderzone regions. For example, infarcts between the ACA and MCA territories can produce contralateral leg weakness and cognitive disturbances. In an elderly male with a history of vascular disease, an MRI showing a border-zone pattern supports a diagnosis of a watershed infarct.",
        "diagnostic_approach": "Diagnosis usually relies on neuroimaging (MRI is more sensitive than CT in the early phase). Differential diagnoses include: cardioembolic stroke (typically producing cortical infarcts in distinct vascular territories), small vessel (lacunar) infarcts which affect deep structures, and vasculitis which often produces multifocal, scattered lesions. History, risk factor assessment, and imaging characteristics help differentiate these conditions.",
        "classification_and_neurology": "Ischemic strokes are classified by the Trial of ORG 10172 in Acute Stroke Treatment (TOAST) criteria into five major subtypes: large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. Watershed infarcts are often categorized under hemodynamic strokes or large artery disease with hypoperfusion. This classification helps in understanding stroke mechanisms and tailoring secondary prevention. The concept of watershed infarcts is integrated into the broader taxonomy of ischemic strokes emphasizing vascular territory and mechanism. Some controversy exists regarding overlap between embolic and hemodynamic causes in watershed zones, but imaging and clinical context usually clarify the diagnosis.",
        "classification_and_nosology": "Watershed infarcts fall under the broader category of ischemic strokes. According to the TOAST classification, they are considered strokes due to hemodynamic compromise rather than embolic or small vessel occlusions.",
        "management_principles": "Management focuses on correcting the underlying hemodynamic instability. First-line management involves optimizing blood flow, blood pressure control, and supportive care. Secondary prevention includes antiplatelet therapy, statins, and management of risk factors (hypertension, diabetes, etc.). In special populations such as pregnant or lactating women, careful selection of antihypertensives (eg, labetalol or nifedipine) and antiplatelet agents with safety profiles in pregnancy is essential.",
        "option_analysis": "Option A (Watershed) is correct as the imaging is consistent with a border-zone pattern. Option B (Cardioembolic) is typically associated with abrupt cortical infarcts in distinct vascular distributions. Option C (Small Vessel Disease) usually gives lacunar infarcts in deep brain regions. Option D (Vasculitis) generally exhibits multifocal and irregular lesions rather than the classic border-zone pattern.",
        "clinical_pearls": "1. Watershed infarcts occur in areas where arterial territories meet (border zones) and are highly sensitive to drops in perfusion pressure. 2. Management requires strict control of blood pressure and risk factor modification. 3. Neuroimaging is crucial to differentiate watershed infarcts from other types of stroke.",
        "current_evidence": "Recent studies emphasize the importance of perioperative and long\u2010term blood pressure management to prevent watershed infarctions in at-risk populations. Updated guidelines highlight the benefit of aggressive vascular risk factor management in elderly patients with carotid artery disease."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993278",
    "fields": {
      "question_number": "140",
      "question_text": "Patient after severe external carotid stenosis revascularization, 1 day later found confused, CT brain (image shown), what is the mechanism.",
      "options": {
        "A": "hypoperfusion",
        "B": "Hyperperfusion",
        "C": "Autoregulation",
        "D": "Artery to artery"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Hyperperfusion syndrome is a recognized complication following procedures that restore blood flow, such as carotid revascularization. It results from an abrupt increase in cerebral blood flow to previously hypoperfused brain regions that have lost the ability to autoregulate.",
        "pathophysiology": "In chronic stenotic conditions, cerebral blood vessels adapt to low flow, leading to impaired autoregulation. When revascularization (eg, carotid endarterectomy or stenting) suddenly increases the blood supply, the cerebral arterioles cannot constrict adequately. This results in increased capillary pressure, breakdown of the blood-brain barrier, vasogenic edema, and sometimes even intracerebral hemorrhage. The mechanism is well-documented in cases following revascularization procedures.",
        "clinical_correlation": "Patients typically present within hours to a few days after revascularization with symptoms such as headache, confusion, and sometimes seizures or focal deficits. In this case, confusion occurring one day post-procedure is highly suggestive of cerebral hyperperfusion syndrome.",
        "diagnostic_approach": "Clinical diagnosis is supported by imaging (CT or MRI), which may show cerebral edema or hemorrhage. Differential diagnoses include hypoperfusion infarcts (which would present with focal deficits and ischemic changes on imaging), embolic strokes (which often show territorial infarcts), and reperfusion injury. The time course and imaging findings help differentiate hyperperfusion syndrome from these conditions.",
        "classification_and_neurology": "Cerebral hyperperfusion syndrome is classified under **perioperative cerebrovascular complications** following carotid revascularization procedures. It falls within the broader category of cerebrovascular disorders related to **hemodynamic disturbances**. The syndrome is distinct from ischemic complications such as embolic stroke or hypoperfusion infarcts. Nosologically, CHS represents a form of reperfusion injury characterized by failure of cerebral autoregulation. Classification systems for carotid revascularization complications typically separate ischemic, hemorrhagic, and hyperperfusion syndromes, reflecting their differing pathophysiology and management.",
        "classification_and_nosology": "Hyperperfusion syndrome is classified as a type of reperfusion injury seen after carotid revascularization. It is not considered a primary stroke subtype but instead represents a post-procedural complication due to loss of autoregulation.",
        "management_principles": "The cornerstone of management is strict blood pressure control to prevent further increases in cerebral perfusion pressure. First-line treatment involves intravenous antihypertensives such as labetalol or nicardipine. Supportive care and close neurological monitoring are essential. In severe cases with cerebral edema, additional measures like osmotherapy may be required. In pregnant patients, labetalol and hydralazine are considered safe; similar caution applies during lactation with appropriate agent selection.",
        "option_analysis": "Option A (Hypoperfusion) is incorrect as it would result in ischemic infarction rather than the edema seen in hyperperfusion syndrome. Option B (Hyperperfusion) is correct, as it best explains the sudden increase in blood flow following revascularization leading to edema and neurologic symptoms. Option C (Autoregulation) is a normal physiological process that is impaired in this scenario, and Option D (Artery to artery embolism) would typically result in territorial infarcts rather than the diffuse changes seen here.",
        "clinical_pearls": "1. Hyperperfusion syndrome typically manifests within 24-72 hours after carotid revascularization. 2. The key management step is aggressive blood pressure control to mitigate the risk of hemorrhage. 3. Recognition of the syndrome is critical to prevent further neurological deterioration.",
        "current_evidence": "Current guidelines stress the importance of perioperative monitoring of blood pressure following revascularization procedures. Recent research has underscored that using intravenous antihypertensives early post-procedure reduces the incidence and severity of hyperperfusion syndrome."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993398",
    "fields": {
      "question_number": "427",
      "question_text": "Patient has 2 stroke, sensory peripheral neuropathy, skin rash with picture. What is the enzyme involved in this disease.",
      "options": {
        "A": "Alpha-Galactosidase"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X-linked lysosomal storage disorder characterized by a deficiency in the enzyme alpha-galactosidase A. This enzyme deficiency leads to the accumulation of glycosphingolipids, particularly globotriaosylceramide, in various tissues throughout the body.",
        "pathophysiology": "The deficiency of alpha-galactosidase A results in the deposition of glycosphingolipids in the endothelial cells of blood vessels, the nervous system, kidneys, and skin. This accumulation can lead to vascular dysfunction, pain in the extremities (acroparesthesias), and organ damage. The stroke, neuropathy, and characteristic skin findings (angiokeratomas) seen in Fabry disease correlate with the widespread vascular deposition and subsequent tissue ischemia and inflammation.",
        "clinical_correlation": "Patients with Fabry disease often present with a combination of clinical features such as early-onset strokes, peripheral neuropathy (manifesting as burning pain in the hands and feet), and angiokeratomas (small, reddish-purple skin lesions). These signs are crucial for the clinical diagnosis of the disorder.",
        "diagnostic_approach": "Diagnosis is confirmed by measuring alpha-galactosidase A activity in leukocytes or plasma, with genetic testing to identify mutations in the GLA gene. Differential diagnoses include other lysosomal storage disorders (such as Gaucher's disease) and conditions causing stroke in young adults. The pattern of multisystem involvement with characteristic skin lesions and neuropathic pain assists in differentiating Fabry disease from other disorders.",
        "classification_and_neurology": "Fabry disease is classified within the lysosomal storage disorders (LSDs), specifically as a glycosphingolipidosis. It is an X-linked inherited disorder due to mutations of the GLA gene. Within neurology, it falls under neurogenetic disorders causing stroke and peripheral neuropathy. The disease is part of a broader category of inherited metabolic disorders that affect the nervous system via substrate accumulation and vascular injury. Historically, LSDs have been classified by the deficient enzyme and accumulated substrate; Fabry disease is unique due to its X-linked pattern and multisystem involvement. Current nosology emphasizes genotype-phenotype correlations and the spectrum from classic severe disease in males to later-onset or attenuated forms in females. Controversies exist regarding screening and classification of variants of uncertain significance, but consensus supports enzyme assay and genetic confirmation as diagnostic standards.",
        "classification_and_nosology": "Fabry disease is classified as a sphingolipidosis, a subgroup of lysosomal storage disorders. It is inherited in an X-linked manner, affecting predominantly males, although females can be affected due to X-chromosome inactivation.",
        "management_principles": "Management includes enzyme replacement therapy (ERT) with agents such as agalsidase beta or agalsidase alfa to reduce glycosphingolipid accumulation. Adjunctive therapies involve pain management, management of renal involvement, and cardiovascular risk reduction. For pregnant or lactating women, the use of ERT requires careful discussion with specialists because data are limited; however, individualized management is recommended with close monitoring.",
        "option_analysis": "Option A (Alpha-Galactosidase) is correct, as the enzyme deficient in Fabry disease is alpha-galactosidase A. The other options were not provided, but based on the clinical scenario the correct enzyme is clearly indicated.",
        "clinical_pearls": "1. Fabry disease can present with strokes at a younger age compared to typical atherosclerotic disease. 2. Angiokeratomas (small, dark red telangiectatic skin lesions) are a hallmark of the disease. 3. Early diagnosis and intervention with ERT can slow disease progression.",
        "current_evidence": "Recent studies highlight the benefits of early enzyme replacement therapy in Fabry disease to delay the progression of organ damage. Guidelines now recommend family screening and genetic counseling for early identification and management of the condition."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "https://drive.google.com/file/d/1EeHee6W2qvJjiZZi93bMjfVtfpclDJpE/preview"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993399",
    "fields": {
      "question_number": "428",
      "question_text": "Case of Sturge Weber (hint: bort wine on face) asked about what it comes with.",
      "options": {
        "A": "Renal Angiofibroma",
        "B": "Cardiac Rhabdomyosarcoma",
        "C": "Glaucoma"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Sturge-Weber syndrome is a neurocutaneous disorder characterized by a facial capillary malformation (commonly known as a port-wine stain) along the distribution of the trigeminal nerve, leptomeningeal angiomas, and associated ocular abnormalities.",
        "pathophysiology": "The syndrome is thought to arise from a somatic mosaic mutation in the GNAQ gene, leading to abnormal vascular development. The port-wine stain is due to capillary malformations in the skin, and the leptomeningeal angiomas can lead to seizures and neurological deficits. The ocular involvement, particularly glaucoma, is due to increased episcleral venous pressure and abnormal vascular development in the eye.",
        "clinical_correlation": "Patients with Sturge-Weber syndrome typically present with a port-wine stain (often described as a 'port wine' or 'bordeaux wine' appearance) on the face, usually in the V1 distribution of the trigeminal nerve. Glaucoma is a common complication and can lead to vision loss if not managed appropriately. Neurological symptoms such as seizures may also be present due to leptomeningeal angiomatosis.",
        "diagnostic_approach": "Diagnosis is primarily clinical based on the characteristic cutaneous and neurological findings. Neuroimaging (MRI/CT) can help identify leptomeningeal angiomas, and ophthalmologic evaluation is essential for early detection of glaucoma. Differential diagnoses include other phakomatoses like Klippel-Trenaunay syndrome, but the combination of facial port-wine stain and leptomeningeal involvement is specific for Sturge-Weber.",
        "classification_and_neurology": "SWS is classified as a sporadic neurocutaneous syndrome within the phakomatoses, distinct from genetic inherited disorders. It is part of a spectrum of vascular malformation syndromes, including Klippel-Trenaunay and Parkes Weber syndromes, but uniquely involves leptomeningeal angiomas. The Roach classification subdivides SWS into three types: Type I (classic, with facial and leptomeningeal angiomas), Type II (facial angioma without CNS involvement), and Type III (isolated leptomeningeal angioma without facial nevus). This classification aids in prognostication and management. The current consensus emphasizes the somatic mosaic nature of the disease, refining the understanding from purely congenital to post-zygotic mutation-driven pathology. Controversies remain regarding the extent of systemic involvement and optimal classification schemes.",
        "classification_and_nosology": "Sturge-Weber syndrome is classified among the phakomatoses (neurocutaneous syndromes). It is a sporadic condition with no clear hereditary pattern.",
        "management_principles": "Management is multidisciplinary. Seizures are managed with antiepileptic medications with careful consideration in pregnant and lactating patients (eg, lamotrigine or levetiracetam, which have relatively favorable profiles). Glaucoma management is crucial and may include topical medications like beta-blockers (with caution in pregnancy, where agents like timolol require careful risk assessment) or surgical interventions if medical therapy fails. Regular ophthalmologic and neurological monitoring is advised.",
        "option_analysis": "Option A (Renal Angiofibroma) is incorrect as it is not a feature of Sturge-Weber syndrome. Option B (Cardiac Rhabdomyosarcoma) is unrelated to the syndrome. Option C (Glaucoma) is correct because glaucoma is a well-known ocular complication associated with Sturge-Weber syndrome.",
        "clinical_pearls": "1. The port-wine stain in Sturge-Weber syndrome is typically unilateral and follows the distribution of the trigeminal nerve. 2. Glaucoma is a common complication and can develop in early childhood or later in life. 3. Early and regular ophthalmologic evaluations are critical to prevent vision loss.",
        "current_evidence": "Recent research and clinical guidelines emphasize early recognition and intervention for glaucoma in Sturge-Weber patients. Advances in neuroimaging and genetic testing have improved the understanding of the underlying molecular mechanisms, aiding in more tailored management approaches."
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
