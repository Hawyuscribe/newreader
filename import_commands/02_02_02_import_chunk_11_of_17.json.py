
# Import batch 2 of 3 from chunk_11_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993133",
    "fields": {
      "question_number": "251",
      "question_text": "Old patient k/c of DM, HTN, ESRD, came with decrease LOC, her wife mentioned that he told her that he was seeing animals then deteriorated; CT showed left occipital hypodensity, what you will do?",
      "options": {
        "A": "CTA",
        "B": "EEG"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This case involves an elderly patient with multiple vascular risk factors (diabetes, hypertension, ESRD) presenting with altered level of consciousness accompanied by visual hallucinations (\u201cseeing animals\u201d). The CT scan showing a left occipital hypodensity suggests an ischemic insult in the occipital region. In patients with strokes affecting the visual cortex, seizures\u2014especially occipital seizures that manifest as visual hallucinations\u2014can occur. An EEG is indicated to assess for nonconvulsive seizure activity.",
        "pathophysiology": "Ischemic injury in the occipital lobe disrupts normal neuronal activity. This disruption may predispose the affected area to hyperexcitability, leading to seizures. In elderly patients especially, even subtle strokes can precipitate nonconvulsive status epilepticus. The electrical instability may manifest clinically as visual hallucinations and further deterioration in consciousness.",
        "clinical_correlation": "The presentation of visual hallucinations combined with a depressed level of consciousness raises the suspicion for seizure activity rather than just a static deficit from infarction. The CT findings provide structural evidence of an occipital stroke, which is a common trigger for post\u2010stroke seizures. An EEG is the diagnostic method of choice to confirm ongoing or intermittent epileptic activity.",
        "diagnostic_approach": "In similar presentations, the workup includes neuroimaging (CT/MRI) to identify structural lesions and an EEG to evaluate for seizure activity. Differential diagnoses include metabolic encephalopathy due to ESRD, delirium, and other stroke complications. The absence of a hemorrhage on CT helps steer management toward seizure evaluation rather than solely stroke management.",
        "classification_and_neurology": "This case falls under the classification of ischemic cerebrovascular disease, specifically acute ischemic stroke involving the posterior cerebral artery territory. The International Classification of Diseases (ICD) and the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system categorize strokes by etiology and vascular territory. Additionally, post-stroke seizures are classified as acute symptomatic seizures if occurring within 7 days of stroke onset, or as remote symptomatic seizures if later. Recognizing seizure disorders secondary to stroke is crucial for prognosis and management. The nosology includes ischemic stroke complicated by acute symptomatic seizures, a recognized subtype within cerebrovascular disease and epilepsy classifications. This dual classification guides diagnostic and therapeutic approaches.",
        "classification_and_nosology": "This scenario falls under the category of post\u2010ischemic stroke seizures. The ictal events here are related to an occipital infarct, which is categorized as focal onset seizures, and when they alter consciousness, can be classified within the spectrum of nonconvulsive status epilepticus.",
        "management_principles": "According to current guidelines, if EEG confirms seizure activity, the first-line management involves antiepileptic drugs (AEDs) such as levetiracetam or phenytoin. It is essential to treat seizures secondary to stroke to prevent further neurological deterioration. In cases where patients are pregnant or lactating, medications such as levetiracetam are preferred because of a more favorable safety profile during pregnancy and breastfeeding, but therapy must always be individualized.",
        "option_analysis": "Option A (CTA) would be useful if there were a need to evaluate for large vessel occlusion or an active vascular lesion suitable for intervention, but it is not indicated in the evaluation of suspected post-stroke seizures. Option B (EEG) is the appropriate next step to assess for seizure activity, making it correct. (No options C/D were provided.)",
        "clinical_pearls": "1. Occipital lobe infarcts can precipitate seizures, frequently manifesting with visual hallucinations. 2. Nonconvulsive status epilepticus should be suspected in stroke patients with unexplained decreased consciousness. 3. EEG is the diagnostic gold standard for identifying seizure activity in such patients.",
        "current_evidence": "Recent guidelines emphasize the importance of early detection and treatment of post-stroke seizures. Studies have shown that timely EEG evaluation in patients with altered mental status post-stroke improves outcomes by allowing appropriate initiation of AEDs, which is in agreement with current best practices."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993138",
    "fields": {
      "question_number": "256",
      "question_text": "pt with cardioembolic stroke, ECG showed AF, Echo: nonvalvular cardiac disease, what to give:",
      "options": {
        "A": "aspirin",
        "B": "warfarin",
        "C": "factor X inhibitor",
        "D": "is not provided.)"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses stroke secondary to cardioembolism in the context of atrial fibrillation (AF). In patients with nonvalvular AF, the risk of thrombus formation in the atria leads to embolic strokes. Current guidelines favor the use of direct oral anticoagulants (DOACs), including direct factor Xa inhibitors, for stroke prevention in this population.",
        "pathophysiology": "Atrial fibrillation results in ineffective atrial contraction and blood stasis, particularly in the left atrial appendage. This stasis predisposes to thrombus formation. Embolization of these clots can result in an ischemic stroke. Factor Xa inhibitors interrupt the coagulation cascade at a key amplification step, reducing clot propagation.",
        "clinical_correlation": "The patient\u2019s ECG showing AF and echocardiogram demonstrating nonvalvular heart disease is classical for a cardioembolic source. Anticoagulation is crucial in preventing further embolic events. Factor Xa inhibitors such as rivaroxaban or apixaban are now often preferred over warfarin because they have a predictable pharmacokinetic profile and lower risk of intracranial bleeding.",
        "diagnostic_approach": "The diagnosis of cardioembolic stroke rests on correlating clinical findings (ECG/echo) with neuroimaging evidence of stroke. Differential diagnoses include atherothrombotic stroke, small vessel disease, and other causes of embolism; however, in the presence of AF, cardioembolism is most likely.",
        "classification_and_neurology": "Cardioembolic stroke is classified under ischemic strokes according to the TOAST criteria (Trial of ORG 10172 in Acute Stroke Treatment), which categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Within cardioembolic stroke, further subclassification distinguishes valvular versus nonvalvular AF. This classification impacts therapeutic decisions, particularly anticoagulation choice. The evolution of classification systems has incorporated advances in cardiac imaging and biomarkers, refining risk stratification. Current consensus emphasizes the importance of identifying cardioembolic sources due to their high recurrence risk and distinct management compared to other stroke subtypes.",
        "classification_and_nosology": "This condition is classified under cardioembolic strokes, with AF being the most common etiology. Nonvalvular AF distinguishes patients who do not have valvular abnormalities, which is key in determining the appropriate anticoagulation regimen.",
        "management_principles": "Recent guidelines from the AHA and ESC recommend DOACs (such as factor Xa inhibitors) as first-line therapy for stroke prevention in patients with nonvalvular AF. These agents are favored over warfarin due to a wider therapeutic window and fewer dietary and drug interactions. Pregnancy and lactation considerations: DOACs are contraindicated during pregnancy; if a woman with AF is pregnant, LMWH is recommended during pregnancy with a switch to warfarin postpartum during lactation if anticoagulation is needed, although bridging protocols and risk\u2013benefit analysis are crucial.",
        "option_analysis": "Option A (aspirin) does not provide sufficient stroke prevention in AF. Option B (warfarin) is an acceptable alternative but is generally less preferred due to monitoring requirements and drug interactions. Option C (factor Xa inhibitor) is the current first-line treatment for nonvalvular AF-related stroke prevention, making it the correct answer. (Option D is not provided.)",
        "clinical_pearls": "1. In nonvalvular AF, DOACs, including factor Xa inhibitors, are preferred over warfarin. 2. Anticoagulation significantly reduces the risk of recurrent cardioembolic events. 3. Always assess patient-specific factors and contraindications, especially regarding pregnancy.",
        "current_evidence": "Recent randomized trials and meta-analyses have consistently shown that factor Xa inhibitors reduce stroke and systemic embolism risk with fewer bleeding complications compared to warfarin. These findings have been incorporated into current guidelines from major cardiovascular societies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993139",
    "fields": {
      "question_number": "257",
      "question_text": "stroke with NIHSS 3, what is the treatment:",
      "options": {
        "A": "Warfarin",
        "B": "Aspirin",
        "C": "factor X inhibitor"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question pertains to the management of an ischemic stroke with a National Institutes of Health Stroke Scale (NIHSS) score of 3, which indicates a mild stroke. In many cases, mild ischemic strokes are managed with antiplatelet therapy rather than aggressive thrombolysis or anticoagulation unless there is a clear cardioembolic source.",
        "pathophysiology": "An ischemic stroke results from the occlusion of a cerebral artery leading to a localized loss of blood flow and subsequent infarction. In mild strokes, the area of infarction is limited, and the neurological deficits may be less severe. Platelet aggregation plays a significant role in the formation of these arterial occlusions, which is why antiplatelet therapy helps prevent lesion progression and secondary events.",
        "clinical_correlation": "A low NIHSS score (3) suggests minor deficits. In the absence of indications for thrombolytic therapy (e.g., severe deficits or within a narrow time window for intervention), management with antiplatelet agents such as aspirin is standard.",
        "diagnostic_approach": "The diagnosis of an ischemic stroke is based on clinical evaluation and neuroimaging (typically CT or MRI). Differential diagnoses include transient ischemic attack (TIA), hemorrhagic stroke (ruled out by CT), and stroke mimics such as seizure-related deficits. In mild strokes, the focus is on preventing recurrence rather than acute intervention.",
        "classification_and_neurology": "Ischemic stroke is classified based on etiology using systems such as the TOAST classification: large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This classification guides treatment choices. Antithrombotic therapy is categorized broadly into antiplatelet agents (e.g., aspirin, clopidogrel) and anticoagulants (e.g., warfarin, direct oral anticoagulants including factor Xa inhibitors). The NIHSS is a standardized tool for stroke severity assessment and prognostication but not a classification system per se. Current consensus supports antiplatelet therapy for mild non-cardioembolic ischemic strokes and anticoagulation for cardioembolic strokes. Controversies remain regarding optimal timing and choice of agents in certain subgroups.",
        "classification_and_nosology": "Ischemic strokes are classified by etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.). A mild stroke with an NIHSS of 3 generally falls under non-disabling, small vessel or cryptogenic strokes where antiplatelet therapy is the cornerstone of management.",
        "management_principles": "Current guidelines recommend initiating antiplatelet therapy (aspirin) as first-line treatment for acute non-cardioembolic ischemic stroke in patients who are not candidates for thrombolysis. For patients with mild strokes, or when no other high-risk source is identified, aspirin is sufficient. In pregnancy, aspirin is generally considered safe in low doses, although the benefits and risks still need to be balanced.",
        "option_analysis": "Option A (Warfarin) is indicated primarily for cardioembolic strokes (usually related to atrial fibrillation) and is not appropriate in this context. Option B (Aspirin) is the correct treatment for most mild ischemic strokes of non-cardioembolic origin. Option C (factor Xa inhibitor) is reserved for cardioembolic etiologies and is not indicated here. (Option D is not provided.)",
        "clinical_pearls": "1. Mild strokes in patients with low NIHSS scores are typically managed with antiplatelet therapy. 2. Aspirin is effective in reducing the risk of early recurrent stroke in non-cardioembolic strokes. 3. Timely initiation of therapy is key to reducing future stroke risk.",
        "current_evidence": "Recent stroke guidelines emphasize the early use of antiplatelet therapy in mild strokes to prevent recurrence. Data supports that in patients with minor deficits, aggressive thrombolysis does not offer additional benefits over aspirin, subject to patient-specific factors."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993141",
    "fields": {
      "question_number": "259",
      "question_text": "Pregnant lady had headache her CT showed ICH, what is the treatment?",
      "options": {
        "A": "start Heparin",
        "B": "Warfarin"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question describes a pregnant patient with headache and CT findings of intracerebral hemorrhage (ICH). Although ICH generally triggers concerns about bleeding, in the context of pregnancy the possibility of cerebral venous sinus thrombosis (CVST) must be considered. CVST is a common cause of hemorrhagic infarctions in pregnant women and typically presents with headache. The standard treatment for CVST, even in the presence of hemorrhage, is anticoagulation with heparin.",
        "pathophysiology": "Pregnancy is a hypercoagulable state that predisposes women to thrombotic events such as CVST. In CVST, clot formation in the cerebral venous sinuses impairs venous drainage, increasing intracranial pressure and sometimes leading to hemorrhagic conversion of venous infarcts. Paradoxically, anticoagulation prevents further propagation of the clot and facilitates recanalization, thereby improving outcomes.",
        "clinical_correlation": "In pregnant women, a severe headache and neuroimaging findings consistent with hemorrhage should raise suspicion for CVST, particularly if clinical features such as papilledema or focal neurological deficits are present. The presence of hemorrhage does not contraindicate anticoagulation in CVST, which is an important clinical nuance.",
        "diagnostic_approach": "The evaluation of suspected CVST should include neuroimaging with CT venography or MR venography to confirm the diagnosis. Differential diagnoses include primary intracerebral hemorrhage from hypertensive causes, aneurysmal bleed, and eclamptic encephalopathy. The clinical context of pregnancy and the typical headache presentation guide the diagnosis toward CVST.",
        "classification_and_neurology": "ICH is classified under hemorrhagic stroke within the broader cerebrovascular disease taxonomy. It can be subclassified by location (lobar, deep, cerebellar, brainstem), etiology (hypertensive, amyloid angiopathy, vascular malformation, coagulopathy), and clinical severity. Pregnancy-associated ICH falls under secondary hemorrhagic stroke due to pregnancy-related conditions (e.g., preeclampsia, eclampsia, cerebral venous thrombosis with hemorrhagic transformation). The American Heart Association/American Stroke Association (AHA/ASA) guidelines categorize stroke types to guide management. Nosology has evolved with better imaging and understanding of pathogenesis, but pregnancy-specific stroke remains a distinct clinical entity due to unique pathophysiology and management challenges.",
        "classification_and_nosology": "CVST is classified as a type of cerebrovascular disease that affects the venous system rather than the arterial system. It is particularly noted in populations with increased risk factors such as pregnancy, the postpartum period, and thrombophilic disorders.",
        "management_principles": "Current guidelines recommend initiating anticoagulation with heparin (preferably low-molecular-weight heparin, LMWH) as first-line therapy in cases of CVST\u2014even when hemorrhagic lesions are present. Warfarin is contraindicated in pregnancy due to teratogenicity and adverse fetal outcomes. For pregnant patients, LMWH is safe and is the standard of care. During lactation, heparin does not pass into breast milk in significant amounts, making it suitable for breastfeeding mothers.",
        "option_analysis": "Option A (start Heparin) is the correct treatment as it aligns with current guidelines for managing CVST in pregnant patients. Option B (Warfarin) is contraindicated in pregnancy because of its teratogenic effects and is not recommended for acute management of CVST. (Options C/D are not provided.)",
        "clinical_pearls": "1. In CVST, anticoagulation with heparin is indicated even in the presence of hemorrhagic infarction. 2. Pregnancy is a hypercoagulable state that increases the risk for CVST. 3. Warfarin is contraindicated in pregnant patients due to its teratogenic potential.",
        "current_evidence": "Latest research and guidelines from the American Heart Association and other neurological societies reaffirm the safety and efficacy of LMWH in the treatment of CVST during pregnancy, emphasizing improved outcomes with early initiation of anticoagulation despite hemorrhagic findings on imaging."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993143",
    "fields": {
      "question_number": "261",
      "question_text": "Patient with multiple Hg in the brain he was on aspirin; lips showed petechiae, what you will do? Case of osler weber rendu",
      "options": {
        "A": "pulmonary CT Angoi"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Osler-Weber-Rendu syndrome, also known as hereditary hemorrhagic telangiectasia (HHT), is a genetic disorder characterized by abnormal blood vessel formation leading to mucocutaneous telangiectasias and arteriovenous malformations (AVMs) in various organs. In this case, the patient has multiple brain hemorrhages, likely exacerbated by aspirin, and classic mucosal findings (petechiae on the lips) that are hallmarks of HHT.",
        "pathophysiology": "HHT is typically caused by mutations in genes like ENG, ACVRL1, or SMAD4, which are involved in angiogenesis. These mutations lead to defective vessel wall formation, resulting in fragile telangiectasias and AVMs. In the lungs, pulmonary AVMs can allow venous blood to bypass the capillary network, predisposing the patient to paradoxical emboli and recurrent cerebral hemorrhages.",
        "clinical_correlation": "Patients with HHT usually present with recurrent epistaxis and mucocutaneous telangiectasias (often on the lips, oral mucosa, and fingertips). The presence of multiple brain hemorrhages in a patient on aspirin should raise suspicion that the bleeding diathesis is due to an underlying vascular disorder such as HHT, especially when accompanied by visible telangiectatic lesions.",
        "diagnostic_approach": "Diagnosis of HHT is based on the Cura\u00e7ao criteria, which include recurrent epistaxis, mucocutaneous telangiectasias, visceral lesions (including pulmonary AVMs), and a positive family history. In this scenario, after initial neurologic management, the next diagnostic step is to screen for pulmonary AVMs. CT pulmonary angiography is the imaging modality of choice, as it has high sensitivity and specificity for detecting these vascular malformations. Differential diagnoses may include other bleeding disorders but are less likely when mucocutaneous telangiectasia is present.",
        "classification_and_neurology": "HHT belongs to the group of hereditary vascular malformation syndromes characterized by autosomal dominant inheritance with variable penetrance. It is classified under vascular anomalies as per the International Society for the Study of Vascular Anomalies (ISSVA) classification. HHT is subdivided based on genetic mutations: HHT1 (ENG mutation) often has more pulmonary and cerebral AVMs, and HHT2 (ACVRL1 mutation) more hepatic involvement. The disease is part of the broader category of neurovascular disorders involving AVMs, distinct from sporadic AVMs due to its genetic basis and systemic manifestations. Over time, classification has evolved with advances in molecular genetics, improving diagnosis and guiding management. Controversies remain regarding screening intervals and management thresholds for asymptomatic AVMs.",
        "classification_and_nosology": "HHT is classified as a vascular dysplasia and is a hereditary condition affecting the vasculature. It falls under the group of genetic arteriovenous malformation syndromes.",
        "management_principles": "Management involves a multidisciplinary approach. First-line treatment focuses on preventing bleeding complications. In the case of pulmonary AVMs, once identified by CT angiography, management typically involves embolization therapy. Avoidance of medications that impair platelet function (like aspirin) is recommended. For pregnant patients, the risk of AVM rupture increases, so careful monitoring with noninvasive imaging and timely intervention is crucial. Specific treatment regimes are adjusted to ensure fetal safety, with embolization considered when benefits outweigh the risks.",
        "option_analysis": "Option A (Pulmonary CT Angio) is correct as it directly addresses the need to evaluate for pulmonary AVMs in a patient suspected of having HHT. The other options were not specified and do not provide the necessary work\u2010up for this condition.",
        "clinical_pearls": "1) HHT is synonymous with Osler-Weber-Rendu syndrome and is characterized by mucocutaneous telangiectasias and AVMs. 2) Pulmonary AVMs pose a risk for paradoxical emboli, which can lead to cerebral events. 3) Aspirin may exacerbate bleeding in patients with HHT.",
        "current_evidence": "Recent guidelines advocate for the use of CT pulmonary angiography in the screening of pulmonary AVMs in patients with suspected or confirmed HHT. There is ongoing research into the role of novel angiogenesis inhibitors, but embolization remains the mainstay of treatment for pulmonary AVMs. Updated recommendations stress the avoidance of antiplatelet agents in these patients to minimize hemorrhagic complications."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993147",
    "fields": {
      "question_number": "265",
      "question_text": "Patient came with left side weakness; CT showed right semiovale hypodensity; what is the next step:",
      "options": {
        "A": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke, rapid identification of vascular occlusions is essential for guiding revascularization therapies. A noncontrast CT scan is usually performed initially to exclude hemorrhage; subsequent vascular imaging such as CT angiography (CTA) is used to detect vessel occlusions or stenoses.",
        "pathophysiology": "Ischemic stroke occurs due to interruption of blood flow to a part of the brain, resulting in infarction of cerebral tissue. A hypodensity seen in the right semiovale area on CT is indicative of a region of infarction, likely due to partial ischemia. Performing a CTA helps identify the location and extent of vascular stenosis or occlusion that may be amenable to thrombolytic therapy or endovascular intervention.",
        "clinical_correlation": "A patient presenting with left sided weakness is clinically suggestive of a right hemispheric stroke. The CT findings of hypodensity (indicative of ischemia) necessitate further evaluation with CTA to assess for a large vessel occlusion, which might make him a candidate for mechanical thrombectomy.",
        "diagnostic_approach": "After an initial noncontrast CT to rule out hemorrhage, CTA is the next step to evaluate the cerebral vasculature. Differential diagnoses include lacunar infarcts due to small vessel disease, which may not always be accessible to endovascular treatment, versus large vessel occlusions which can be targeted with specific interventions.",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology and vascular territory. The TOAST classification categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. The lesion in the semiovale likely represents small vessel or deep MCA branch occlusion. The stroke is part of the broader cerebrovascular disease family, which also includes transient ischemic attacks and hemorrhagic strokes. Classification systems have evolved to incorporate imaging and clinical data for precision medicine. Current consensus emphasizes integrating clinical, imaging, and laboratory data to tailor management and prognosis.",
        "classification_and_nosology": "Ischemic strokes are categorized according to their etiology (large vessel, small vessel, cardioembolic, etc.). In this case, the semiovale infarct could suggest a small vessel occlusion, but CTA is critical to rule out any large vessel pathology or tandem lesions.",
        "management_principles": "The tiered management approach in acute ischemic stroke involves initial noncontrast CT imaging followed by vascular imaging (CTA). First-line treatments include intravenous thrombolysis if within the therapeutic window and consideration of endovascular therapy if a large vessel occlusion is identified. In pregnant patients, radiation exposure from CT/CTA is minimized with abdominal shielding and risk\u2013benefit analysis given the time-sensitive nature of stroke interventions.",
        "option_analysis": "Option A (CTA) is correct because it is the suitable next step for evaluating the vessel status after the CT shows an infarct. Other options (if provided) may include MRI or CT perfusion but CTA remains the rapid and widely available choice in many stroke protocols.",
        "clinical_pearls": "1) 'Time is brain'\u2014rapid imaging and intervention in stroke are crucial for reducing morbidity. 2) CT followed by CTA is the standard protocol in acute ischemic stroke workup. 3) Even subtle hypodensities on CT should prompt vascular imaging to rule out treatable occlusions.",
        "current_evidence": "Recent AHA/ASA guidelines emphasize the importance of early vascular imaging to determine eligibility for endovascular reperfusion therapies. Recent studies have also validated the use of CTA in accurately assessing the vascular status in acute stroke settings, including in selected pregnant patients with appropriate protective measures."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993148",
    "fields": {
      "question_number": "266",
      "question_text": "Another question about Patient came with stroke CT showed watershed infarction, next?",
      "options": {
        "A": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Watershed infarctions occur in the border zones between cerebral artery territories and are typically a manifestation of hypoperfusion. In the context of stroke evaluation, identifying the vascular status is imperative to manage underlying causes of hypoperfusion such as severe stenosis or occlusion.",
        "pathophysiology": "Watershed infarcts result from decreased cerebral perfusion, most often due to systemic hypotension or significant stenosis/occlusion of major extracranial or intracranial vessels. The areas at the periphery of major vascular territories are especially vulnerable due to their marginal supply.",
        "clinical_correlation": "Clinically, patients may present with neurological deficits that correlate with the regions of border-zone ischemia. In this case, after the CT reveals a watershed infarction, the next step is to assess for an underlying vascular lesion that might be treatable, thereby reducing the risk of recurrent events.",
        "diagnostic_approach": "The recommended next step is performing a CT angiography (CTA) to evaluate the carotid arteries and intracranial vessels. Differential diagnoses include embolic stroke from an alternative source and small-vessel lacunar infarcts; however, the watershed pattern strongly supports a hemodynamic etiology that necessitates vascular imaging.",
        "classification_and_neurology": "Watershed infarctions are classified under ischemic strokes, specifically as hemodynamic strokes within the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system. TOAST categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Watershed infarctions are often linked to large artery atherosclerosis with hemodynamic compromise or systemic hypoperfusion. They are also recognized in the Oxfordshire Community Stroke Project (OCSP) classification as partial anterior circulation infarcts depending on the territory involved. The nosology has evolved to emphasize the pathophysiological mechanism (hypoperfusion vs embolic) rather than purely anatomical location. There is ongoing discussion about subclassifying watershed infarcts based on etiology to tailor management strategies.",
        "classification_and_nosology": "Watershed infarctions are subclassified under ischemic strokes and are differentiated from territorial infarcts by their location at the junction of major arterial territories. They are often associated with systemic or localized hypoperfusion.",
        "management_principles": "Immediate management is geared toward stabilizing hemodynamics and preventing further hypoperfusion. From a diagnostic perspective, CTA is essential to identify high-grade stenosis that may require revascularization therapies. In pregnancy, while the use of CT angiography is approached with caution due to radiation exposure, protective measures (like abdominal shielding) are implemented because the benefit of diagnosing a potentially life\u2010threatening condition outweighs the risk.",
        "option_analysis": "Option A (CTA) is correct because it provides critical information about the status of the cerebral and carotid vasculature, which is necessary for both acute management and long-term secondary prevention strategies. The selection is based on the need to exclude high-grade stenosis or occlusive disease that may require intervention.",
        "clinical_pearls": "1) Watershed infarctions are typically due to systemic hypoperfusion or severe arterial stenosis. 2) CTA is a rapid method to evaluate the cerebral vasculature in suspected stroke cases. 3) Identification of a watershed pattern should prompt consideration of both systemic and vascular causes of low perfusion.",
        "current_evidence": "Current stroke management guidelines continue to endorse CTA as a critical component of neurovascular imaging in acute ischemic stroke. Emerging research is also exploring advanced imaging techniques to better characterize the penumbra and guide revascularization, but CTA remains the cornerstone in the acute setting, including in special populations such as pregnant patients with meticulous risk mitigation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993149",
    "fields": {
      "question_number": "267",
      "question_text": "Stroke patient and he has fever, Cardiac consultation showed pan systolic murmur; what is the treatment:",
      "options": {
        "A": "antiplatelets",
        "B": "Antibiotics"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Infective endocarditis (IE) can lead to the formation of vegetations on heart valves. These vegetations may embolize, causing septic embolic strokes. The clinical picture of fever, a new murmur (in this case pansystolic which may indicate valve involvement like mitral regurgitation), and stroke is highly suggestive of IE.",
        "pathophysiology": "IE is characterized by microbial infection of the endocardial surface, which results in the formation of friable vegetations. These infected emboli can travel to the brain and occlude cerebral vessels, leading to ischemic or hemorrhagic stroke. The presence of fever indicates the systemic inflammatory and infectious process.",
        "clinical_correlation": "A stroke patient with fever and a newly detected pansystolic murmur should prompt suspicion for IE. The murmur may be due to valvular destruction or regurgitation from infection, and septic emboli from the vegetations can lead to multifocal cerebral infarctions. The clinical scenario fits the classic presentation of embolic stroke secondary to IE.",
        "diagnostic_approach": "The evaluation of suspected IE involves fulfilling the Modified Duke Criteria. This includes blood cultures, echocardiography (both transthoracic and potentially transesophageal), and careful clinical assessment. Differential diagnoses include non-infective thromboembolic stroke and primary cardiac conditions without infection; however, the combination of fever and murmur strongly supports IE.",
        "classification_and_neurology": "Stroke is classified etiologically into ischemic and hemorrhagic types. Ischemic stroke is further divided by the TOAST classification into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Infective endocarditis-related stroke falls under cardioembolic stroke of other determined etiology. Infective endocarditis itself is classified by causative organism, valve involvement (native vs prosthetic), and clinical course (acute vs subacute). The recognition of IE as a cause of stroke is essential for appropriate classification and management. The modified Duke criteria remain the gold standard for IE diagnosis, integrating clinical, microbiological, and echocardiographic findings.",
        "classification_and_nosology": "Infective endocarditis is classified based on the acuity (acute versus subacute), the type of valve involved (native versus prosthetic), and the causative organism. This case is typical of native valve endocarditis presenting with septic emboli.",
        "management_principles": "The mainstay of treatment for IE is prolonged, targeted intravenous antibiotic therapy based on culture and sensitivity results. According to current guidelines, treatment is individualized depending on the pathogen involved. For pregnant patients, antibiotics like penicillins and cephalosporins are typically preferred due to their safety profile in pregnancy, whereas gentamicin use may be limited due to potential fetal toxicity. In the context of a stroke, careful neurologic monitoring is required, and the use of antiplatelets or anticoagulants is generally avoided given the risk of hemorrhagic conversion.",
        "option_analysis": "Option B (Antibiotics) is correct because the treatment of infective endocarditis is centered on timely and appropriate antibiotic administration. Option A (Antiplatelets) is not suitable in this context as they do not address the underlying infectious process and may increase the risk of hemorrhagic complications in the brain.",
        "clinical_pearls": "1) Always suspect infective endocarditis in stroke patients who present with fever and a new or changing murmur. 2) Early identification and treatment with appropriate antibiotics can reduce both systemic and neurologic complications. 3) Echocardiography is key in diagnosing the source of emboli in these patients.",
        "current_evidence": "Recent guidelines from cardiology and infectious disease societies underscore the importance of early detection and targeted antibiotic therapy in IE. The emphasis is on using culture-directed therapy and, in some cases, early surgical intervention for complicated cases. For pregnant patients with IE, a multidisciplinary approach is adopted, carefully balancing maternal and fetal risks while ensuring adequate antimicrobial coverage."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993150",
    "fields": {
      "question_number": "268",
      "question_text": "Stroke patient has livedo reticularis what is the Dx?",
      "options": {
        "A": "Sneddon disease"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Sneddon syndrome is a rare non\u2010inflammatory arteriopathy that classically presents with the combination of cerebrovascular events (strokes or transient ischemic attacks) and a characteristic skin finding\u2014livedo reticularis (a netlike violaceous rash). The syndrome is an important diagnostic consideration when a stroke patient also exhibits these unique cutaneous findings.",
        "pathophysiology": "The underlying mechanism involves a thrombotic vasculopathy affecting small to medium-sized arteries. Although the precise etiology isn\u2019t fully understood, many patients have circulating antiphospholipid antibodies and there may be overlap with other autoimmune conditions (such as systemic lupus erythematosus). The vascular occlusion leads to chronic ischemia in the brain and skin, manifesting as strokes and livedo reticularis, respectively.",
        "clinical_correlation": "Patients typically present with neurologic deficits due to ischemic strokes and a persistent, often widespread, livedo reticularis rash. The concurrence of these findings should prompt the clinician to evaluate for Sneddon syndrome, especially in younger patients or those without typical stroke risk factors.",
        "diagnostic_approach": "Evaluation includes neuroimaging (MRI and CT) to document ischemic lesions, and careful dermatologic exam. Skin biopsy may show non-inflammatory occlusive changes. Laboratory work\u2010up for antiphospholipid antibodies and other autoimmune markers is also indicated in order to differentiate from primary vasculitides or other coagulopathies.",
        "classification_and_neurology": "Sneddon syndrome is classified as a rare non-inflammatory thrombotic vasculopathy affecting small and medium-sized arteries. It belongs to the broader category of non-atherosclerotic vasculopathies causing stroke, overlapping with antiphospholipid antibody syndrome (APS) when antibodies are present. Nosologically, it resides within the spectrum of primary vasculopathies distinct from classical vasculitis, as inflammation is minimal or absent. The syndrome is sometimes divided into idiopathic Sneddon syndrome and secondary forms associated with systemic lupus erythematosus or APS. Current consensus favors recognizing Sneddon syndrome as a distinct clinical entity characterized by livedo reticularis and stroke, with or without antiphospholipid antibodies. Some controversy exists regarding its overlap with APS, but the presence of livedo reticularis and characteristic arteriopathy remains a unifying feature.",
        "classification_and_nosology": "Sneddon syndrome is classified as a noninflammatory thrombotic vasculopathy. It can occur as a primary syndrome or secondary to connective tissue diseases (e.g., antiphospholipid syndrome, systemic lupus erythematosus).",
        "management_principles": "There is no standardized treatment, but management is generally aimed at stroke prevention. First-line therapies include antiplatelet agents (e.g., aspirin) or anticoagulation in patients with documented antiphospholipid antibodies. In cases associated with autoimmune disease, immunomodulatory therapies may be added. In pregnant patients, low-dose aspirin and careful monitoring are recommended because both thrombotic risks and bleeding complications have to be balanced during pregnancy and lactation.",
        "option_analysis": "Option A, Sneddon disease (another name for Sneddon syndrome), is correct. No other options were provided, but the distinctive association of livedo reticularis with stroke in this syndrome is the key diagnostic clue.",
        "clinical_pearls": "1. Always consider Sneddon syndrome in a stroke patient with livedo reticularis. 2. Testing for antiphospholipid antibodies can help differentiate it from other vasculopathies. 3. Management revolves around stroke prevention and may differ if associated with autoimmune conditions.",
        "current_evidence": "Recent studies have emphasized the role of comprehensive autoimmune work\u2010up in patients with unexplained strokes and skin findings. Current expert opinion supports early initiation of antiplatelet therapy and, when indicated, anticoagulation. Ongoing research is evaluating the efficacy of various immunomodulatory agents in patients with an underlying autoimmune component."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993151",
    "fields": {
      "question_number": "269",
      "question_text": "60 years old came to ER with left side weakness and left decrease propioception and right tongue weakness; what is the artery involved?",
      "options": {
        "A": "Rigth Vert",
        "B": "Left Vert",
        "C": "Basilar"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Sneddon syndrome is a rare non\u2010inflammatory arteriopathy that classically presents with the combination of cerebrovascular events (strokes or transient ischemic attacks) and a characteristic skin finding\u2014livedo reticularis (a netlike violaceous rash). The syndrome is an important diagnostic consideration when a stroke patient also exhibits these unique cutaneous findings.",
        "pathophysiology": "The underlying mechanism involves a thrombotic vasculopathy affecting small to medium-sized arteries. Although the precise etiology isn\u2019t fully understood, many patients have circulating antiphospholipid antibodies and there may be overlap with other autoimmune conditions (such as systemic lupus erythematosus). The vascular occlusion leads to chronic ischemia in the brain and skin, manifesting as strokes and livedo reticularis, respectively.",
        "clinical_correlation": "Patients typically present with neurologic deficits due to ischemic strokes and a persistent, often widespread, livedo reticularis rash. The concurrence of these findings should prompt the clinician to evaluate for Sneddon syndrome, especially in younger patients or those without typical stroke risk factors.",
        "diagnostic_approach": "Evaluation includes neuroimaging (MRI and CT) to document ischemic lesions, and careful dermatologic exam. Skin biopsy may show non-inflammatory occlusive changes. Laboratory work\u2010up for antiphospholipid antibodies and other autoimmune markers is also indicated in order to differentiate from primary vasculitides or other coagulopathies.",
        "classification_and_neurology": "Brainstem strokes are classified based on the vascular territory and anatomical location: medial medullary syndrome (anterior spinal artery or vertebral artery branches), lateral medullary syndrome (PICA or vertebral artery), pontine syndromes (paramedian or lateral pontine arteries from basilar artery), and midbrain syndromes (paramedian branches of basilar artery). This question pertains to medial medullary syndrome, a subtype of ischemic brainstem stroke. The classification aligns with the TOAST criteria for ischemic stroke subtypes, specifying large artery atherosclerosis or small vessel occlusion affecting vertebral artery branches. Over time, stroke classification has evolved from purely clinical syndromes to incorporate imaging and etiology, but the anatomical-vascular correlation remains essential for localization and management. There is consensus that vertebral artery involvement is key in medial medullary infarcts, as opposed to basilar artery occlusion which affects more rostral structures.",
        "classification_and_nosology": "Sneddon syndrome is classified as a noninflammatory thrombotic vasculopathy. It can occur as a primary syndrome or secondary to connective tissue diseases (e.g., antiphospholipid syndrome, systemic lupus erythematosus).",
        "management_principles": "There is no standardized treatment, but management is generally aimed at stroke prevention. First-line therapies include antiplatelet agents (e.g., aspirin) or anticoagulation in patients with documented antiphospholipid antibodies. In cases associated with autoimmune disease, immunomodulatory therapies may be added. In pregnant patients, low-dose aspirin and careful monitoring are recommended because both thrombotic risks and bleeding complications have to be balanced during pregnancy and lactation.",
        "option_analysis": "Option A, Sneddon disease (another name for Sneddon syndrome), is correct. No other options were provided, but the distinctive association of livedo reticularis with stroke in this syndrome is the key diagnostic clue.",
        "clinical_pearls": "1. Always consider Sneddon syndrome in a stroke patient with livedo reticularis. 2. Testing for antiphospholipid antibodies can help differentiate it from other vasculopathies. 3. Management revolves around stroke prevention and may differ if associated with autoimmune conditions.",
        "current_evidence": "Recent studies have emphasized the role of comprehensive autoimmune work\u2010up in patients with unexplained strokes and skin findings. Current expert opinion supports early initiation of antiplatelet therapy and, when indicated, anticoagulation. Ongoing research is evaluating the efficacy of various immunomodulatory agents in patients with an underlying autoimmune component."
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
