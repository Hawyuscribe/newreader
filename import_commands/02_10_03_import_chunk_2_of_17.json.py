
# Import batch 3 of 3 from chunk_2_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993022",
    "fields": {
      "question_number": "115",
      "question_text": "74-year-old male with CT brain image showing large hemorrhage in the cortex what to do next",
      "options": {
        "A": "MRI",
        "B": "CTA",
        "C": "conventional angio"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "In a 74\u2010year\u2010old male presenting with a cortical hemorrhage on CT, determining the cause of the hemorrhage is paramount. CT angiography (CTA) is the recommended next step, as it enables evaluation for underlying vascular abnormalities such as aneurysms, arteriovenous malformations (AVMs), or the presence of active bleeding (spot sign).",
        "pathophysiology": "Intracerebral hemorrhages result from the rupture of abnormal or diseased vessels. In elderly patients, lobar hemorrhages may also be related to cerebral amyloid angiopathy; however, when the hemorrhage is large and cortical, evaluation for other vascular abnormalities is warranted. CTA can rapidly detect vascular anomalies that might have contributed to the bleed.",
        "clinical_correlation": "The patient\u2019s clinical presentation along with the CT finding of a cortical hemorrhage suggests the need for urgent vascular imaging. CTA not only assists in identifying potential causes but also guides further management decisions (e.g., surgical intervention or conservative treatment).",
        "diagnostic_approach": "Following a non-contrast CT that identifies hemorrhage, the differential includes hypertensive hemorrhage, amyloid angiopathy, vascular malformations, and aneurysmal rupture. CTA helps differentiate these entities by visualizing the vascular structure. MRI can be useful later for parenchymal details, while conventional angiography is typically reserved for cases where CTA is non-diagnostic or for therapeutic intervention planning.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified by location (lobar/cortical, deep basal ganglia, brainstem, cerebellar) and etiology (hypertensive, amyloid angiopathy, vascular malformations, coagulopathy, tumor-related). The widely accepted classification distinguishes hypertensive hemorrhages (typically deep) from lobar hemorrhages often related to cerebral amyloid angiopathy or vascular malformations. The American Heart Association/American Stroke Association (AHA/ASA) guidelines incorporate this classification to guide diagnostic and therapeutic pathways. There is some debate regarding the role of routine vascular imaging in all ICH cases, but consensus favors targeted vascular imaging in lobar hemorrhages or atypical presentations to exclude underlying vascular abnormalities.",
        "classification_and_nosology": "This hemorrhage falls under the category of intracerebral hemorrhage. Lobar hemorrhages (as opposed to deep or infratentorial hemorrhages) often prompt evaluation for vascular malformations, particularly when the bleeding pattern is atypical for hypertensive bleeds.",
        "management_principles": "Immediate management involves stabilization of the patient, blood pressure control, and reversal of anticoagulation if indicated. Guidelines suggest that CTA should be performed promptly to delineate the vascular anatomy and identify potential bleeding sources. In pregnant patients or lactating mothers, the risks and benefits of contrast exposure should be considered, but in life-threatening hemorrhage, maternal stabilization is prioritized.",
        "option_analysis": "Option B (CTA) is correct because it provides a rapid, non-invasive method to evaluate the vascular anatomy in the setting of intracerebral hemorrhage. Option A (MRI) is less ideal in an acute hemorrhagic setting due to time constraints, while conventional angiography (Option C) is invasive and generally reserved for cases when non-invasive imaging is inconclusive or if endovascular therapy is contemplated.",
        "clinical_pearls": "1. CTA is critical in the acute evaluation of intracerebral hemorrhage to identify potential vascular abnormalities. 2. Lobar hemorrhages in the elderly warrant careful investigation for amyloid angiopathy and other vascular lesions. 3. Time is brain - rapid imaging guides management.",
        "current_evidence": "Current stroke guidelines support the use of CTA following detection of intracerebral hemorrhage on CT to detect a bleeding source or vascular anomaly. It is now a standard component in the acute stroke imaging protocol, with recent studies validating its role in predicting hematoma expansion via the 'spot sign'."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_12.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993023",
    "fields": {
      "question_number": "116",
      "question_text": "Patient with small left internal capsule infarction and right-sided weakness for 2 days found to have PFO (not mentioned if there was a specific feature of it) HTN with uncontrolled BP. What is the treatment?",
      "options": {
        "A": "Aspirin",
        "B": "Warfarin",
        "C": "PFO closure",
        "D": "Aspirin and plavix"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This patient presents with a small left internal capsule infarction and right-sided weakness. Although a patent foramen ovale (PFO) is detected, the clinical context (lacunar infarct with uncontrolled hypertension) strongly favors a small vessel (lacunar) infarct due to hypertensive arteriopathy rather than an embolic event from a paradoxical embolism through the PFO.",
        "pathophysiology": "Lacunar infarcts occur due to occlusion of small penetrating arteries, typically as a consequence of chronic hypertension leading to arteriolosclerosis. While PFO can be a conduit for paradoxical emboli, its prevalence in the general population and the presence of significant vascular risk factors (like uncontrolled high blood pressure) point to a hypertensive etiology. Recent research emphasizes proper patient selection for PFO closure, typically in young patients with cryptogenic stroke.",
        "clinical_correlation": "The location of the infarct (internal capsule) and the clinical picture of pure motor stroke are classic for a lacunar event. In this context, the incidental finding of a PFO is unlikely to be the culprit. The focus should be on antiplatelet therapy and rigorous blood pressure control to prevent further lacunar events.",
        "diagnostic_approach": "Diagnosis of a lacunar stroke is made based on clinical features and supported by imaging (often CT or MRI showing a small deep infarct). Differential diagnoses include embolic strokes (which typically involve cortical areas) and large artery atherosclerosis. A detailed cardiac evaluation and sometimes transesophageal echocardiography can be performed to assess the significance of a PFO, but only in selected cases of cryptogenic stroke in younger patients.",
        "classification_and_neurology": "Ischemic strokes are classified by TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This patient fits the small vessel occlusion category given the infarct location and risk factors. PFO-related strokes fall under cardioembolic strokes but require evidence of paradoxical embolism and high-risk PFO features (e.g., large shunt, atrial septal aneurysm). The presence of PFO alone does not reclassify the stroke unless clinical correlation supports embolism. Classification guides secondary prevention strategy, emphasizing the importance of comprehensive evaluation.",
        "classification_and_nosology": "Stroke subtypes are classified based on the TOAST criteria. Lacunar strokes fall under small vessel disease, whereas strokes related to PFO would be categorized as cardioembolic/cryptogenic if no other source is found. Here, the presence of uncontrolled hypertension makes this a classic lacunar infarct.",
        "management_principles": "First-line management for lacunar stroke involves antiplatelet therapy, with aspirin being the standard agent. Concurrently, aggressive management of hypertension is required to reduce recurrence risk. Dual antiplatelet therapy (aspirin plus clopidogrel) is generally not indicated beyond the acute period except in specific scenarios. PFO closure is reserved for younger patients (<60 years) with cryptogenic stroke and high-risk PFO characteristics. In pregnancy and lactation, low-dose aspirin is often considered safe under guidance, but blood pressure management remains the priority.",
        "option_analysis": "Option A (Aspirin) is correct. Warfarin (Option B) is not indicated in lacunar strokes without a cardioembolic source, and PFO closure (Option C) is generally not recommended in older patients with a clear alternative stroke mechanism. Option D (aspirin and clopidogrel) is not part of standard long-term management for lacunar strokes in this scenario.",
        "clinical_pearls": "1. Lacunar strokes are typically due to small vessel disease related to uncontrolled hypertension. 2. An incidental PFO in an elderly patient with classic lacunar findings is not an indication for closure. 3. Strict control of blood pressure is critical to preventing recurrent lacunar strokes.",
        "current_evidence": "Recent trials and meta-analyses underscore that PFO closure benefits are confined to younger patients with cryptogenic stroke and high-risk anatomical features. The current approach in older patients or those with clear alternative etiologies (like hypertension-induced small vessel disease) remains antiplatelet therapy and risk factor modification."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993024",
    "fields": {
      "question_number": "117",
      "question_text": "Alexia without agraphia with hemianopia",
      "options": {
        "A": "PCA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Alexia without agraphia, often termed 'pure alexia,' is a disconnection syndrome where a patient loses the ability to read but retains the ability to write. This syndrome is most commonly associated with infarction in the territory of the posterior cerebral artery (PCA), particularly affecting the left occipital lobe and the splenium of the corpus callosum.",
        "pathophysiology": "The left occipital lobe is responsible for processing visual input, and the splenium of the corpus callosum connects the visual cortex to language areas in the dominant hemisphere. When both are compromised\u2014commonly due to an occlusion of the left PCA\u2014the patient can still write (as language production centers are intact) but cannot comprehend written words because visual input is not adequately relayed to these centers.",
        "clinical_correlation": "Patients present with homonymous hemianopia (usually right-sided if the left PCA is involved) and a striking disassociation: the ability to write remains preserved while reading is impaired. This clinical presentation is pathognomonic for alexia without agraphia.",
        "diagnostic_approach": "Imaging, particularly MRI, will reveal infarction in the left occipital lobe and may show involvement of the splenium. Differential diagnoses include other forms of aphasia; however, the preservation of writing ability distinguishes alexia without agraphia. Additional evaluations, such as formal neuropsychological testing and visual field assessments, aid in confirmation.",
        "classification_and_neurology": "Alexia without agraphia is classified as a type of **disconnection syndrome** within neuropsychology and cerebrovascular disease taxonomy. It belongs to the family of language disorders (aphasias) but is distinguished by its unique mechanism\u2014disconnection rather than direct cortical language area damage. The lesion is typically in the **posterior cerebral artery (PCA) territory**. The syndrome contrasts with other alexia variants such as: - **Pure alexia (alexia without agraphia)**: classic lesion in left occipital lobe and splenium - **Alexia with agraphia**: lesions in dominant angular gyrus - **Global aphasia**: lesions in perisylvian language areas Classification systems have evolved to emphasize network and connectivity disruptions rather than solely cortical localization. The current consensus integrates vascular territory localization with neuropsychological syndromes.",
        "classification_and_nosology": "Alexia without agraphia is classified as a disconnection syndrome and is most commonly seen as a sequela of a posterior cerebral artery infarct. It is a subcategory of visual or disconnection aphasias.",
        "management_principles": "Acute management of PCA stroke is similar to other ischemic strokes, where the focus is on reperfusion strategies (if within the thrombolytic window), antiplatelet therapy, and supportive care. Long-term management includes risk factor modification. In pregnant or lactating patients, thrombolytic therapy is considered only after careful risk\u2013benefit analysis and usually in specialized centers; antiplatelet therapies such as low-dose aspirin are generally considered safe under medical supervision.",
        "option_analysis": "Option A (PCA) is correct as the syndrome is a classic presentation of a stroke in the distribution of the posterior cerebral artery, particularly affecting the left side. The other options, if presented, would not align with the vascular territory involved in this specific disconnection syndrome.",
        "clinical_pearls": "1. Alexia without agraphia is a classic disconnection syndrome resulting from left occipital and splenium involvement. 2. A key feature is the loss of reading ability in the presence of preserved writing skills. 3. It is most commonly associated with infarction of the PCA territory.",
        "current_evidence": "Recent stroke management guidelines continue to emphasize the importance of rapid diagnosis and reperfusion in acute ischemic strokes, including PCA infarcts. Advances in neuroimaging have improved the accuracy of localizing the infarct and predicting outcomes in disconnection syndromes such as alexia without agraphia."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993025",
    "fields": {
      "question_number": "118",
      "question_text": "Patient with ataxia and vomiting CT attached (showing hypodensity at the whole right cerebellum at the level of the midbrain)",
      "options": {
        "A": "SCA",
        "B": "PCA",
        "C": "PICA",
        "D": "AICA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This question evaluates the understanding of cerebellar vascular territories and their infarction patterns. The cerebellum is supplied by three major arteries: the Superior Cerebellar Artery (SCA), Anterior Inferior Cerebellar Artery (AICA), and Posterior Inferior Cerebellar Artery (PICA). A lesion seen at the level of the midbrain in the cerebellum is most consistent with the SCA territory.",
        "pathophysiology": "An infarction in the SCA territory occurs when there is occlusion, typically due to thromboembolism or local atherosclerotic disease, leading to ischemia of the superior aspect of the cerebellum. This ischemia disrupts cerebellar circuits responsible for coordination, resulting in ataxia, and can also affect vestibular integration, contributing to symptoms like vomiting.",
        "clinical_correlation": "Clinically, a patient with an SCA infarct usually presents with acute cerebellar symptoms such as ataxia, imbalance, and vomiting. CT imaging will demonstrate hypodensity within the affected cerebellar region. The midbrain level slice implicates the superior portion of the cerebellum, which is supplied by the SCA.",
        "diagnostic_approach": "The diagnosis is initially established using non-contrast CT to identify hypodense areas indicating ischemia. MRI (especially diffusion-weighted imaging) is more sensitive in the acute setting. Differential diagnoses include hemorrhagic stroke, cerebellar tumors, demyelinating lesions, and infarctions in other cerebellar territories (PICA or AICA infarcts), which are distinguished by their specific vascular distribution and imaging characteristics.",
        "classification_and_neurology": "Cerebellar infarcts are classified based on the vascular territory involved: SCA, AICA, and PICA. This categorization aligns with the TOAST classification for ischemic stroke subtypes, which includes large artery atherosclerosis affecting posterior circulation.   - **PICA infarcts** belong to the posterior circulation stroke family and often overlap clinically with lateral medullary syndrome. - **AICA infarcts** involve the anterior inferior cerebellum and lateral pons. - **SCA infarcts** affect the superior cerebellar hemisphere and dentate nucleus.  This vascular territory classification has evolved with advances in neuroimaging and angiography, allowing more precise localization. Controversies remain regarding overlapping territories and collateral circulation, but consensus supports this tripartite division as the clinical standard for cerebellar strokes.",
        "classification_and_nosology": "This condition is classified as an ischemic cerebrovascular accident specifically affecting the cerebellum. Within cerebellar strokes, infarctions are sub-classified based on the involved vascular territory (SCA, PICA, or AICA).",
        "management_principles": "Management begins with acute stroke protocols including IV thrombolysis if within the time window, supportive care, and monitoring for complications like edema and hydrocephalus. In selected cases, neurosurgical decompression may be indicated. In pregnant patients, the risk\u2010benefit assessment for thrombolytics is critical, with a preference for imaging modalities and treatments that minimize fetal radiation exposure. For lactating mothers, treatment adjustments may be needed to avoid transmission of potentially teratogenic agents.",
        "option_analysis": "Option A (SCA) is correct because the CT at the level of the midbrain with whole cerebellar involvement on the right side fits the SCA infarction pattern. Option B (PCA) is incorrect because the PCA supplies the occipital lobe. Option C (PICA) typically affects the inferior cerebellum, and Option D (AICA) supplies the anterior inferior portion of the cerebellum, neither matching the described imaging level.",
        "clinical_pearls": "1. In cerebellar strokes, early identification is key due to the risk of brainstem compression and hydrocephalus. 2. A CT slice at the midbrain level that shows cerebellar hypodensity is most suggestive of an SCA infarct. 3. Vomiting and ataxia without significant long tract signs point toward a localized cerebellar event.",
        "current_evidence": "Recent guidelines emphasize early neuroimaging and prompt thrombolytic therapy, if appropriate, for ischemic stroke. Advances in MRI techniques help differentiate among cerebellar infarctions and assess for mass effect. Research continues to refine the management of posterior circulation strokes, particularly regarding surgical interventions in cases of cerebellar edema."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993026",
    "fields": {
      "question_number": "119",
      "question_text": "Lady with 2 abortions came with stroke what to order",
      "options": {
        "A": "protein c def",
        "B": "Antithrombin 3",
        "C": "Antiphospholipid syndrome",
        "D": "Protein glycoprotein 20220"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This question centers on the evaluation of hypercoagulable states leading to both thrombotic events (such as stroke) and recurrent pregnancy loss. Antiphospholipid syndrome (APS) is a prime example where autoimmune antibodies create a proclivity for thrombosis, manifesting in both obstetric and vascular complications.",
        "pathophysiology": "In APS, autoantibodies (including lupus anticoagulant, anticardiolipin, and anti-\u03b22 glycoprotein I) interact with phospholipids and coagulation factors, leading to endothelial dysfunction and a hypercoagulable state. This results in thrombosis in both arteries and veins, as well as placental thrombosis, which can cause recurrent miscarriages.",
        "clinical_correlation": "A young woman with a history of two abortions who now presents with a stroke fits the clinical picture of APS. The dual presentation of recurrent pregnancy loss and arterial thrombosis is highly suggestive of this syndrome, prompting evaluation with antiphospholipid antibody testing.",
        "diagnostic_approach": "The diagnostic workup includes testing for lupus anticoagulant, anticardiolipin antibodies, and anti-\u03b22 glycoprotein I antibodies, with repeat testing 12 weeks apart to confirm persistent positivity. Differential diagnoses include other thrombophilias such as Protein C deficiency, Protein S deficiency, and Factor V Leiden mutation; however, these rarely present with recurrent abortions to the degree seen in APS.",
        "classification_and_neurology": "APS is classified as a systemic autoimmune thrombophilia within the broader category of hypercoagulable disorders. The 2006 revised Sapporo criteria (Sydney criteria) are the current consensus for diagnosis, requiring at least one clinical and one laboratory criterion. It is considered a secondary cause of stroke under the category of non-atherosclerotic vasculopathies and thrombophilias. APS can be primary or secondary to systemic lupus erythematosus (SLE). The classification distinguishes between inherited thrombophilias (e.g., protein C, protein S, antithrombin III deficiencies) and acquired ones like APS. Protein glycoprotein 20210 mutation (likely a typographical error for factor V Leiden or prothrombin G20210A mutation) belongs to inherited thrombophilias. APS is unique in combining thrombosis and pregnancy morbidity, setting it apart in nosology and guiding specific management.",
        "classification_and_nosology": "APS is classified as an acquired thrombophilia and is further divided into primary APS (occurring in isolation) and secondary APS (associated with systemic autoimmune diseases like systemic lupus erythematosus).",
        "management_principles": "Management of APS involves long-term anticoagulation. For a patient with a stroke, warfarin with a goal INR of 2.5-3.0 is often used; however, in women of childbearing age, especially during pregnancy, warfarin is contraindicated. In pregnancy, low molecular weight heparin in combination with low-dose aspirin is recommended to reduce both thrombotic and obstetric complications. Breastfeeding mothers are generally safely managed with heparin therapy.",
        "option_analysis": "Option A (Protein C deficiency) and Option B (Antithrombin 3 deficiency) are inherited thrombophilias that can cause thrombosis but are less commonly associated with recurrent miscarriages. Option D (Protein glycoprotein 20220 mutation) is associated with thrombosis but again, the combination of stroke and recurrent abortions is most suggestive of APS, making Option C the correct choice.",
        "clinical_pearls": "1. Recurrent pregnancy loss combined with thrombotic events is a classic presentation of APS. 2. Confirmatory testing for APS requires demonstration of persistent positivity for antiphospholipid antibodies on two occasions, at least 12 weeks apart. 3. Management strategies differ drastically during pregnancy, with a shift toward heparin-based therapies.",
        "current_evidence": "Recent guidelines from the American College of Rheumatology and hematology recommend aggressive anticoagulation in APS patients with thrombotic events. There is increasing evidence to support the combination of low-molecular-weight heparin and low-dose aspirin in pregnant patients to reduce both thrombotic risk and miscarriage rates. Additionally, DOACs are being evaluated but have not yet supplanted warfarin or heparin in high-risk APS, especially in a pregnant population."
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
