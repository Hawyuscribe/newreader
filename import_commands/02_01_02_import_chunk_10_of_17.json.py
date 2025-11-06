
# Import batch 2 of 3 from chunk_10_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993320",
    "fields": {
      "question_number": "349",
      "question_text": "Patient with sickle cell anemia wants to check on himself because his brother is also sickler and had previous stroke. How to predict:",
      "options": {
        "A": "Transcranial doppler",
        "B": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In patients with sickle cell disease (SCD), the risk of cerebrovascular complications including stroke is significantly heightened. Transcranial Doppler (TCD) ultrasound is the validated screening tool designed to measure cerebral blood flow velocities, which are correlated with stroke risk.",
        "pathophysiology": "Sickle cell anemia leads to chronic endothelial injury and vasculopathy, resulting in arterial stenosis. As vessels narrow, blood flow velocity increases, which can be detected by TCD. Elevated velocities indicate a compensatory mechanism for reduced lumen diameter and predict an increased risk of ischemic stroke.",
        "clinical_correlation": "Screening with TCD is particularly important in children with SCD, as early identification of abnormal flow velocities allows for timely intervention (e.g., chronic transfusion therapy) to reduce stroke risk. Even in adult patients, TCD may help in risk assessment if there is a concerning family or personal history of stroke.",
        "diagnostic_approach": "TCD is non-invasive, cost-effective, and has no radiation exposure, making it ideal for repeated screening. Alternative imaging (such as CTA or MRA) may further delineate vascular anatomy but are not used for routine screening due to risks associated with radiation and contrast use.",
        "classification_and_nosology": "Cerebrovascular complications of sickle cell disease are classified based on their risk for stroke. TCD screening is a cornerstone of preventive neurology in pediatric sickle cell populations and is used in risk stratification protocols.",
        "management_principles": "If TCD screening reveals elevated cerebral blood flow velocities, the first-line management is typically the initiation of a chronic red cell transfusion program to reduce the risk of stroke. Hydroxyurea is another option that may be used to reduce sickling. In pregnant or lactating patients, careful management is needed to balance the benefits of transfusion therapy with potential complications, and non-ionizing imaging like TCD remains the preferred screening modality.",
        "option_analysis": "Option A (Transcranial Doppler) is correct because it is the standard, widely recommended screening tool for predicting stroke risk in individuals with sickle cell disease. Option B (CTA) is less favored due to the exposure to radiation and contrast agents, and it is not validated as a screening tool in this population.",
        "clinical_pearls": "\u2022 TCD screening in children with sickle cell disease has significantly reduced the incidence of first strokes.\n\u2022 Elevated cerebral blood flow velocities on TCD are a strong predictor of stroke risk.\n\u2022 TCD is safe for repeated use and is especially valuable in the pediatric population.",
        "current_evidence": "Seminal trials such as STOP and STOP II have validated the use of TCD screening to identify high-risk patients and guide preventative interventions. Current guidelines continue to recommend TCD as the cornerstone screening tool for stroke prevention in sickle cell disease."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993321",
    "fields": {
      "question_number": "350",
      "question_text": "Scenario of stroke with normal CT what do next (not thrombolysis):",
      "options": {
        "A": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In the acute stroke setting, a non-contrast CT scan is typically the first imaging modality used to exclude hemorrhage. However, early in ischemic stroke, CT may appear normal due to the time lag before radiographic changes become evident. Thus, vascular imaging such as CT angiography (CTA) is critical to evaluate the cerebral vessels for occlusions or stenoses, especially when thrombolysis isn\u2019t an option.",
        "pathophysiology": "Ischemic strokes result from an interruption of blood flow, often due to an occlusive thrombus or embolus. In the hyperacute phase, cytotoxic edema has not yet produced clear changes on CT. CTA, by visualizing the cerebral vasculature, can detect large vessel occlusions which underlie the infarct and help determine patient eligibility for interventions such as thrombectomy.",
        "clinical_correlation": "Patients presenting with clinical signs of stroke may have a normal CT scan if imaged very early. CTA is then utilized to assess for large vessel occlusions that may not be evident on non-contrast CT, guiding further management decisions. Recognizing that a normal CT can be misleading is key to timely diagnosis and treatment.",
        "diagnostic_approach": "The differential diagnosis includes transient ischemic attack (TIA), migraine with aura, and other conditions mimicking stroke. The diagnostic approach generally begins with a non-contrast CT to exclude hemorrhage, followed by CTA or CT perfusion studies to evaluate ischemic tissue and vascular status.",
        "classification_and_nosology": "Stroke is broadly classified into ischemic and hemorrhagic types. Ischemic strokes can be further categorized based on the vessel involved (large vessel occlusion versus small vessel disease). CTA is particularly useful in identifying occlusions in large vessels such as the MCA or ICA.",
        "management_principles": "Current guidelines recommend rapid imaging in suspected stroke. When CT is normal in a patient with stroke symptoms, a CTA is indicated to identify occlusions that could be amenable to endovascular therapy. In patients who are pregnant or lactating, the benefits of CTA (with appropriate shielding) outweigh the risks, as early detection and intervention are critical.",
        "option_analysis": "Option A (CTA) is correct because it offers detailed visualization of the cerebral arteries. The other options are not provided, but among available choices, CTA is the most appropriate next investigation when the initial non-contrast CT is normal.",
        "clinical_pearls": "1. A normal CT in the hyperacute phase does not exclude ischemic stroke. 2. CTA is essential for diagnosing large vessel occlusion. 3. Rapid vascular imaging guides potential subsequent interventions.",
        "current_evidence": "Recent AHA/ASA guidelines emphasize the role of CTA in the early evaluation of ischemic stroke, particularly when CT findings are inconclusive and large vessel occlusion is suspected. Studies support that CTA enables rapid decision-making for possible endovascular therapy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993322",
    "fields": {
      "question_number": "351",
      "question_text": "Scenario about Wernicke aphasia which artery:",
      "options": {
        "A": "Inferior division of MCA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Wernicke\u2019s aphasia is characterized by impaired language comprehension paired with fluent but often nonsensical speech. It results from damage to the language processing center, typically located in the posterior portion of the superior temporal gyrus.",
        "pathophysiology": "Wernicke\u2019s area is predominantly supplied by the inferior division of the middle cerebral artery (MCA) in the dominant hemisphere\u2014most often the left. Occlusion or infarction in this region disrupts language comprehension while sparing speech fluency, producing the classical picture of Wernicke\u2019s aphasia.",
        "clinical_correlation": "Clinically, patients with Wernicke\u2019s aphasia present with fluent speech that may include paraphasias and neologisms, along with significant comprehension deficits. Recognizing the vascular territory affected helps correlate the clinical syndrome with its underlying vascular pathology.",
        "diagnostic_approach": "The differential diagnosis includes other aphasic syndromes such as Broca\u2019s aphasia, conduction aphasia, and transcortical sensory aphasia. Neuroimaging (typically MRI with appropriate sequences) confirms the infarct location and its vascular distribution.",
        "classification_and_nosology": "Aphasias are classified based on the affected language domains and the location of the lesion. Wernicke\u2019s aphasia falls under fluent aphasias, and its association with MCA's inferior division helps differentiate it from non-fluent types like Broca\u2019s aphasia.",
        "management_principles": "Management of stroke affecting Wernicke\u2019s area follows standard ischemic stroke protocols, including considerations for thrombolysis or thrombectomy if within the treatment window. For pregnant or lactating patients, similar stroke protocols apply with adjustments to imaging and medication selection. Subsequent rehabilitation with speech and language therapy is crucial.",
        "option_analysis": "Option A (Inferior division of MCA) is correct because this artery supplies Wernicke\u2019s area. Other options, though not listed here, do not accurately correspond to the vascular supply of the language comprehension center.",
        "clinical_pearls": "1. Wernicke's aphasia presents with fluent but nonsensical speech and impaired comprehension. 2. It is most commonly due to infarction in the territory of the inferior division of the left MCA. 3. Detailed neuroimaging is essential to confirm the lesion\u2019s location.",
        "current_evidence": "Current neuroimaging studies and stroke guidelines consistently affirm that the inferior division of the MCA supplies Wernicke's area. Emerging research continues to refine our understanding of aphasia subtypes and optimal rehabilitation strategies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993323",
    "fields": {
      "question_number": "352",
      "question_text": "Patient with Sickle Cell Anemia who with symptoms of infarction, in investigation he was found to have severe intracranial MCA stenosis what would you do",
      "options": {
        "A": "ASA",
        "B": "Stenting",
        "C": "DAPT",
        "D": "Exchange transfusion"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Patients with sickle cell disease (SCD) are at increased risk for cerebrovascular complications, including stroke. The underlying hemoglobinopathy leads to chronic hemolysis and vaso-occlusion, predisposing patients to both infarcts and vascular stenoses.",
        "pathophysiology": "In SCD, repeated sickling episodes cause endothelial damage and intimal hyperplasia, resulting in vascular stenosis or occlusion. Severe intracranial stenosis, particularly in the middle cerebral artery (MCA), can precipitate cerebral infarction due to impaired blood flow. Exchange transfusion reduces the proportion of abnormal hemoglobin (HbS) and improves oxygen delivery.",
        "clinical_correlation": "Clinically, SCD patients presenting with stroke symptoms and evidence of intracranial stenosis require prompt treatment to prevent further ischemic injury. Exchange transfusion is the frontline therapy aimed at reducing HbS levels while minimizing blood viscosity and the risk of further vaso-occlusive events.",
        "diagnostic_approach": "Differential diagnoses in this context include thrombotic stroke due to other causes (like cardioembolism or atherosclerosis) and vasculitic processes. Neuroimaging (MRI/MRA) combined with a thorough hematologic evaluation helps differentiate SCD-related stroke from other etiologies.",
        "classification_and_nosology": "Strokes in SCD are classified based on underlying pathology. The vascular complications in SCD, including moyamoya-type vasculopathy and large vessel stenosis, require distinct management strategies compared to atherosclerotic strokes.",
        "management_principles": "The current standard of care for an SCD patient with stroke involves urgent exchange transfusion, which rapidly decreases the HbS concentration and reduces ongoing ischemia. This is supported by guidelines and studies (such as the STOP trials) and is considered first-line therapy. In pregnancy and lactation, transfusion therapy remains the mainstay, with careful monitoring and matched blood products to avoid alloimmunization and other complications.",
        "option_analysis": "Option D (Exchange transfusion) is correct because it directly addresses the underlying sickling and vaso-occlusion process by reducing HbS levels. Option A (ASA) is not sufficient for the acute management of SCD stroke; Option B (Stenting) and Option C (DAPT) have not been shown to be effective or safe primary treatments in this unique patient population.",
        "clinical_pearls": "1. SCD increases the risk of stroke due to repeated vascular injury. 2. Exchange transfusion is critical in rapidly reducing pathological HbS levels during an acute stroke. 3. Chronic transfusion therapy may be required for secondary stroke prevention.",
        "current_evidence": "Recent updates and clinical trials (including the STOP trial series) reinforce exchange transfusion as the primary intervention in SCD-related stroke. Guidelines from hematology and neurology societies emphasize rapid reduction of HbS via exchange transfusion to mitigate further ischemic injury."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993324",
    "fields": {
      "question_number": "353",
      "question_text": "Scenario about CVT what will confirm diagnosis:",
      "options": {
        "A": "CTV",
        "B": "If mri choose it"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral venous thrombosis (CVT) is a condition where thrombus formation in the cerebral venous sinuses leads to impaired cerebral venous drainage. Its clinical presentation can be subtle and variable, making imaging critical for confirmation.",
        "pathophysiology": "In CVT, thrombus formation within the cerebral venous system results in venous congestion, increased intracranial pressure, and potentially venous infarctions or hemorrhages. The disruption of normal venous drainage may be due to hypercoagulable states, infections, or other risk factors.",
        "clinical_correlation": "Patients with CVT often present with headache, focal neurological deficits, seizures, or signs of increased intracranial pressure such as papilledema. Accurate diagnosis is essential to initiate appropriate anticoagulation therapy and prevent complications.",
        "diagnostic_approach": "The differential diagnosis for CVT includes intracerebral hemorrhage, arterial ischemic stroke, and benign intracranial hypertension. MRI with MR venography (MRV) is typically the modality of choice because of its high sensitivity and specificity, while CT venography (CTV) is a reasonable alternative when MRI is unavailable.",
        "classification_and_nosology": "CVT is classified under cerebrovascular diseases distinct from arterial strokes. It can be further categorized based on the location of the thrombus (e.g., superior sagittal sinus, lateral sinus, deep venous system).",
        "management_principles": "Once diagnosed, the mainstay of treatment for CVT is anticoagulation, typically initiated with heparin (unfractionated or low-molecular-weight) even in the presence of hemorrhage. For pregnant or lactating patients, low-molecular-weight heparin is preferred due to its safety profile. Long-term management may include oral anticoagulants. Confirmatory imaging with MRI/MRV guides these decisions.",
        "option_analysis": "Option B (If MRI choose it) is interpreted as advocating for an MRI-based approach (typically MRI with MR venography), which is the preferred modality for confirming CVT given its superior soft-tissue contrast and ability to directly visualize the thrombus. Option A (CTV) is also acceptable but is generally considered second-line when MRI is accessible.",
        "clinical_pearls": "1. CVT can present with nonspecific symptoms, making advanced imaging essential. 2. MRI with MR venography is the gold standard for diagnosing CVT. 3. Early anticoagulation improves outcomes in CVT even when a hemorrhagic component is present.",
        "current_evidence": "Latest guidelines by the AHA/ASA and various neuroimaging consensus statements highlight that MRI with MRV is the confirmatory imaging of choice for CVT due to its high sensitivity and absence of radiation, although CT venography remains a good alternative in settings where MRI is not feasible."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993325",
    "fields": {
      "question_number": "354",
      "question_text": "Scenario with attached Angio (suggestive of FM-DYSPLASIA) what to do:",
      "options": {
        "A": "Renal angio",
        "B": "Alpha 1 antitrypsin"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Fibromuscular dysplasia (FMD) is a nonatherosclerotic, noninflammatory arteriopathy affecting medium\u2010sized arteries, most classically the renal and carotid arteries. Its angiographic hallmark is the 'string-of-beads' appearance. When an angiogram \u2014 even if originally obtained from a cerebrovascular source \u2014 is suggestive of FMD, it is important to examine other vascular beds that may be involved.",
        "pathophysiology": "FMD is believed to result from abnormal cellular proliferation within the arterial wall (most commonly the media), leading to alternating areas of stenosis and aneurysmal dilatation. Although the exact cause remains unclear, hormonal factors (given its predilection for middle\u2010aged women) and genetic factors are thought to contribute. This multifocal vascular involvement means that both cerebral and renal arteries can be affected.",
        "clinical_correlation": "Clinically, FMD may present with symptoms related to cerebrovascular events (such as transient ischemic attacks or strokes if the carotid arteries are involved) or with renovascular hypertension if the renal arteries are affected. The finding on a cerebral angiogram consistent with FMD should prompt an evaluation for concomitant renal artery involvement, which can have significant implications in blood pressure management.",
        "diagnostic_approach": "The initial diagnosis is usually made by imaging \u2013 typically using duplex ultrasound, CT angiography, MR angiography, or catheter-based digital subtraction angiography. Differential diagnoses include atherosclerotic disease (which tends to produce smooth, concentric stenoses without the beadlike pattern) and vasculitis (which would show inflammatory signs both clinically and on laboratory work-up). Once FMD is suspected in one vascular bed, further evaluation (such as a renal angiogram) is warranted.",
        "classification_and_nosology": "FMD is typically classified by its histopathological or angiographic appearance. The most common type, medial fibroplasia, produces the classic 'string-of-beads' appearance. It is categorized separately from other arterial disorders such as atherosclerosis and vasculitis.",
        "management_principles": "Management focuses on controlling blood pressure and mitigating stroke risk. In cases with significant renal artery involvement, percutaneous transluminal angioplasty may be recommended. First-line treatments include risk factor modification and medical management with antihypertensives. In pregnant or lactating women, blood pressure control is crucial and agents such as labetalol or methyldopa (which have better safety profiles in pregnancy) should be considered. Secondary interventional procedures are reserved for severe or refractory cases.",
        "option_analysis": "Option A, 'Renal angio,' is appropriate because once FMD is suspected (based on the cerebral angiogram in this scenario), imaging of the renal arteries is indicated to assess possible multisystem involvement. Option B (Alpha 1 antitrypsin) is unrelated, as it pertains to a genetic deficiency primarily linked to lung and liver disease. Options C and D are not provided.",
        "clinical_pearls": "1) FMD predominantly affects middle-aged women and is often discovered incidentally or after investigation of a stroke or hypertension. 2) The 'string-of-beads' sign on angiography is pathognomonic. 3) Once FMD is diagnosed in one vascular territory, evaluation for additional involvement (especially of the renal arteries) is essential.",
        "current_evidence": "Recent guidelines and consensus statements from vascular and radiologic societies recommend a comprehensive vascular workup in patients with FMD. Advances in non-invasive imaging techniques allow for earlier and more accurate detection, which in turn informs risk factor management and the need for possible revascularization procedures."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993326",
    "fields": {
      "question_number": "355",
      "question_text": "Scenario of lateral medullary:",
      "options": {
        "A": "PICA",
        "B": "no vertebral artery in options"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Lateral medullary syndrome, also known as Wallenberg syndrome, is a classic brainstem stroke syndrome that affects the lateral portion of the medulla oblongata. It is most commonly related to ischemia in the territory of the Posterior Inferior Cerebellar Artery (PICA).",
        "pathophysiology": "An occlusion of the PICA leads to infarction in the lateral medulla. This infarction compromises multiple neural structures including the vestibular nuclei, spinal trigeminal nucleus, nucleus ambiguus, and sympathetic pathways. The resultant deficits reflect the loss of these structures\u2019 functions.",
        "clinical_correlation": "Patients typically present with sudden onset of vertigo, nausea, vomiting, dysphagia, hoarseness, ipsilateral facial hypoalgesia (loss of pain and temperature sensation), and contralateral body sensory deficits for pain and temperature. These constellation of symptoms are pathognomonic for lateral medullary syndrome due to PICA occlusion.",
        "diagnostic_approach": "Diagnosis is made clinically and confirmed with neuroimaging (CT/MRI) showing infarction in the lateral medulla. Vascular imaging (CTA, MRA, or catheter angiography) can identify the occluded vessel. Differential diagnoses include lateral pontine syndrome (often due to AICA occlusion) and other posterior circulation strokes, which can be differentiated based on both imaging and the specific neurological deficits present.",
        "classification_and_nosology": "Wallenberg syndrome falls under the broader category of ischemic strokes involving the brainstem. It is specifically categorized by its distinct clinical syndrome and the vascular territory \u2013 that of the PICA \u2013 involved in the infarct.",
        "management_principles": "Acute management follows standard stroke care with consideration for intravenous thrombolytic therapy if the patient presents within the appropriate window. Secondary prevention includes the use of antiplatelet agents and management of vascular risk factors. In pregnancy, special care must be taken when considering thrombolysis \u2013 weighing maternal benefits against fetal risks \u2013 and medications with proven safety profiles should be selected.",
        "option_analysis": "Option A, 'PICA,' is the correct choice because occlusion of the Posterior Inferior Cerebellar Artery is the most frequent cause of lateral medullary syndrome. Option B mentioning the 'no vertebral artery in options' distracts from the core pathology. Options C and D are not provided.",
        "clinical_pearls": "1) Lateral medullary syndrome is characterized by a cross-sensory deficit (ipsilateral facial, contralateral body pain/temperature loss). 2) Occlusion of the PICA is the prototypical cause of this syndrome. 3) Early recognition is crucial for timely intervention, particularly regarding acute stroke management.",
        "current_evidence": "Current guidelines emphasize rapid neuroimaging and prompt initiation of acute stroke therapies. Recent studies support the use of advanced imaging techniques that enhance early detection of posterior circulation strokes, and further refine selection criteria for thrombolytic or endovascular therapies even in the complex anatomical region of the brainstem."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993327",
    "fields": {
      "question_number": "356",
      "question_text": "CSF finding in RCVS:",
      "options": {
        "A": "slightly high protein",
        "B": "other choices was clearly wrong"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Reversible Cerebral Vasoconstriction Syndrome (RCVS) is characterized by sudden, severe ('thunderclap') headaches and segmental constriction of cerebral arteries that is reversible over time. It typically lacks the inflammatory or infectious changes seen in other CNS vasculopathies.",
        "pathophysiology": "RCVS is thought to result from transient disturbances in the regulation of cerebral arterial tone. This leads to multifocal vasoconstriction without the accompanying blood\u2013brain barrier disruption or significant inflammatory response that one would see in infections or primary angiitis of the central nervous system.",
        "clinical_correlation": "Clinically, patients with RCVS present with recurrent thunderclap headaches. Neurological deficits may arise if the vasoconstriction results in ischemic injury. Since the underlying process is noninflammatory, CSF studies are typically normal or near-normal.",
        "diagnostic_approach": "The workup includes careful neuroimaging (CT, MRI, MRA, or catheter angiography) to document the segmental vasoconstriction and repeat studies to confirm reversibility. A lumbar puncture is performed primarily to exclude subarachnoid hemorrhage or CNS vasculitis. Differential diagnoses include subarachnoid hemorrhage, primary angiitis of the CNS (which usually shows pleocytosis and a more marked protein elevation), and central nervous system infections.",
        "classification_and_nosology": "RCVS falls into the category of non-inflammatory vasculopathies. It is distinct from primary CNS vasculitis both in its reversible nature and in its typical CSF profile, which lacks significant inflammatory markers.",
        "management_principles": "First-line management generally includes calcium channel blockers (such as nimodipine) to help relieve vasoconstriction and supportive care including pain management. Avoidance of triggers (e.g., vasoactive substances like serotonergic drugs) is also recommended. In pregnant or lactating patients, the use of medications must be carefully considered; agents with more favorable safety profiles (and consultation with maternal\u2013fetal medicine) are preferred.",
        "option_analysis": "Option A, 'slightly high protein,' is acceptable in this context. Although RCVS is classically associated with normal CSF, minor nonspecific protein elevation (without significant pleocytosis) can occasionally be observed. The other options (not detailed here) are clearly less representative of the typical CSF findings in RCVS.",
        "clinical_pearls": "1) RCVS is best known for its thunderclap headaches and reversible vascular changes on imaging. 2) The CSF in RCVS is typically normal or nearly normal, which helps distinguish it from inflammatory vasculopathies such as primary angiitis of the CNS. 3) Prompt recognition and differentiation from other causes of severe headache are critical to prevent complications.",
        "current_evidence": "Recent studies have confirmed that mild CSF protein elevation (if present) in RCVS does not indicate an inflammatory process. Emerging research continues to refine diagnostic criteria and optimal management strategies for RCVS, emphasizing the importance of multimodal imaging and careful clinical monitoring."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993328",
    "fields": {
      "question_number": "357",
      "question_text": "Scenario about CADASIL:",
      "options": {
        "A": "CADASIL"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "CADASIL stands for Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy. It is a hereditary small vessel disease caused by mutations in the NOTCH3 gene, leading to distinctive clinical and radiographic features.",
        "pathophysiology": "The disease is caused by mutations in the NOTCH3 gene, which lead to abnormal accumulation of granular osmiophilic material in the smooth muscle cells of small arteries. This accumulation results in progressive arteriopathy, with consequent subcortical infarcts and white matter changes. The pathophysiological process underpins the clinical signs of migraine, recurrent strokes, and cognitive decline.",
        "clinical_correlation": "Patients with CADASIL typically present in early to mid-adulthood with migraine (often with aura), recurrent lacunar strokes, mood disturbances, and a progressive subcortical dementia. MRI findings classically reveal white matter hyperintensities involving the periventricular areas and the anterior temporal lobes.",
        "diagnostic_approach": "The diagnosis of CADASIL is based on a characteristic clinical picture, typical MRI findings, and can be confirmed with genetic testing for NOTCH3 mutations. A skin biopsy demonstrating granular osmiophilic material can also support the diagnosis. Differential diagnoses include other causes of small vessel disease and leukoencephalopathies such as multiple sclerosis or vascular dementia, which can be distinguished based on imaging, family history, and specific clinical features.",
        "classification_and_nosology": "CADASIL is categorized as a genetic microangiopathy and falls within the group of hereditary cerebral small vessel diseases. It is distinct due to its autosomal dominant inheritance pattern and the unique involvement of the NOTCH3 signaling pathway.",
        "management_principles": "There is no curative treatment for CADASIL, so management is primarily supportive. This includes aggressive control of vascular risk factors (such as hypertension and hyperlipidemia), antiplatelet therapy for secondary stroke prevention, and symptomatic management of migraines and mood disturbances. Genetic counseling is crucial for affected individuals and family members. In pregnant or lactating women, special attention to blood pressure control and medication safety is required, with agents selected based on their safety profile in pregnancy (e.g., labetalol for hypertension).",
        "option_analysis": "Option A, 'CADASIL,' is the correct answer as it directly names the condition characterized by the clinical and radiological features described in the scenario. The other options, which are not provided in this context, do not align with the classic findings of CADASIL.",
        "clinical_pearls": "1) CADASIL should be suspected in patients with a history of migraine with aura, subcortical strokes, and a family history of early-onset dementia or stroke. 2) The anterior temporal pole involvement on MRI is highly suggestive of CADASIL. 3) Genetic confirmation is key for diagnosis and family counseling.",
        "current_evidence": "Recent advances emphasize the importance of genetic testing for NOTCH3 mutations in patients with suspected CADASIL. While no disease-modifying treatments exist, ongoing research is focused on potential targeted therapies. Current guidelines stress the importance of risk factor management and genetic counseling to optimize long-term outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993329",
    "fields": {
      "question_number": "358",
      "question_text": "Common question, SCENARIO about progressive symptoms of spinal fistula with attached MRI for spine:",
      "options": {
        "A": "DAVF",
        "B": "Cavernoma",
        "C": "AVM",
        "D": "AVF best fits the clinical scenario of progressive symptoms related to a spinal fistula."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Spinal dural arteriovenous fistula (DAVF) is the most common type of spinal vascular malformation. It involves an abnormal connection between a dural artery and a bridging medullary vein, leading to venous congestion and progressive myelopathy.",
        "pathophysiology": "In DAVF, arterial blood is shunted directly into the venous system without the normal capillary bed. This results in elevated venous pressure, impaired venous drainage, and subsequent spinal cord ischemia. The resulting venous congestion leads to chronic spinal cord edema and neurological deficits.",
        "clinical_correlation": "Patients with spinal DAVF typically present with slowly progressive weakness and sensory disturbances in the lower extremities, along with gait abnormalities. The condition is most commonly seen in middle-aged to elderly males. MRI findings often reveal hyperintensity on T2-weighted images in the spinal cord (indicative of edema) and serpiginous flow voids representing dilated vessels.",
        "diagnostic_approach": "Initial assessment with MRI of the spine is essential, as it can suggest the diagnosis by showing cord edema and abnormal flow voids. However, spinal angiography remains the gold standard for definitive diagnosis, allowing precise localization and characterization of the fistula. Differential diagnoses include intramedullary arteriovenous malformations (AVMs) and cavernomas, but these have differing clinical and imaging features.",
        "classification_and_nosology": "Spinal vascular malformations are generally classified into dural arteriovenous fistulas (DAVFs), intramedullary AVMs, and cavernous malformations. DAVFs are distinct due to their location (usually in the dura) and their mechanism of causing venous congestion, unlike AVMs which are intramedullary and more prone to hemorrhage.",
        "management_principles": "The treatment of spinal DAVF typically involves endovascular embolization or microsurgical disconnection to interrupt the abnormal shunt. In pregnant patients or those who are lactating, careful risk\u2013benefit assessment is necessary as angiographic procedures involve radiation and contrast agents, which may be deferred or managed with modifications based on current guidelines. Multidisciplinary management is crucial to optimize neurological outcomes.",
        "option_analysis": "The options provided were DAVF, cavernoma, and AVM. Cavernomas are usually benign vascular lesions that may present with hemorrhages but do not lead to venous congestion as seen in DAVF. Intramedullary AVMs often present with hemorrhage rather than the progressive myelopathic symptoms typical of DAVF. Thus, the option DAVF best fits the clinical scenario of progressive symptoms related to a spinal fistula.",
        "clinical_pearls": "Early recognition of spinal DAVF is essential as treatment can prevent irreversible spinal cord damage. Clues on MRI such as cord signal hyperintensity and flow voids should lead to angiographic confirmation. A multidisciplinary approach, including neurosurgery and interventional neuroradiology, is recommended.",
        "current_evidence": "Current guidelines support endovascular embolization as a first-line treatment for spinal DAVF when feasible, with surgical intervention as an alternative in selected cases. Recent studies emphasize the importance of early intervention to halt progression of myelopathy and improve long-term outcomes. Special considerations for pregnant or lactating patients include minimizing fetal radiation exposure and using alternative imaging modalities or protective measures when necessary."
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
