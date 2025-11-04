
# Import batch 3 of 3 from chunk_5_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993099",
    "fields": {
      "question_number": "74",
      "question_text": "50-year-old patient, heavy smoker, hypertensive on medication, came with history of left eye visual changes & dysarthria for 10 min then resolved, asked about next?",
      "options": {
        "A": "MRI brain",
        "B": "CTA neck"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This case describes a classic transient ischemic attack (TIA): a self\u2010limiting episode of neurological dysfunction caused by transient cerebral ischemia. Given the patient\u2019s vascular risk factors (hypertension and heavy smoking) and the nature of his symptoms (transient visual changes and dysarthria), the next step is to evaluate the potential vascular source of embolism.",
        "pathophysiology": "TIAs are typically due to temporary occlusion of a cerebral artery often from an embolus or in situ thrombosis over an atherosclerotic plaque. In patients with risk factors like atherosclerosis, an unstable plaque in the carotid artery may intermittently shed emboli leading to transient neurological deficits.",
        "clinical_correlation": "The patient\u2019s symptoms\u2014transient visual changes (which may represent amaurosis fugax) and dysarthria\u2014are indicative of ischemia in areas supplied by the carotid circulation. The presence of such symptoms in a high-risk patient mandates urgent evaluation to stratify risk and prevent subsequent stroke.",
        "diagnostic_approach": "Initial evaluation of suspected TIA typically includes neuroimaging (CT or MRI) to rule out acute infarction, followed by vascular imaging. Differential diagnoses include migraine with aura, seizure-related transient deficits, and ocular causes. However, in a patient with vascular risk factors, evaluation of the carotids is paramount. Carotid imaging via CT angiography (CTA neck) or duplex ultrasound is used to identify significant stenosis.",
        "classification_and_neurology": "TIA is classified under cerebrovascular diseases per the World Health Organization and American Heart Association/American Stroke Association (AHA/ASA) frameworks. Traditionally defined by symptom duration (<24 hours), newer definitions incorporate tissue-based criteria using MRI diffusion-weighted imaging (DWI) to exclude infarction, refining diagnosis to transient symptoms without imaging evidence of infarction. TIAs are further subclassified by etiology using the TOAST classification into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. This patient likely falls into the large artery atherosclerosis category due to risk factors and symptom pattern. Contemporary nosology emphasizes urgent evaluation and secondary prevention to mitigate stroke risk. Controversies remain regarding the optimal imaging protocol and criteria for TIA diagnosis, but consensus supports a tissue-based approach.",
        "classification_and_nosology": "TIAs are considered part of the ischemic cerebrovascular events spectrum. With advances in imaging, many now define TIA by the absence of permanent tissue infarction. TIA workups are categorized under stroke prevention protocols.",
        "management_principles": "Management involves both diagnostic evaluation and secondary prevention. First-line evaluation includes brain imaging to exclude stroke and vascular imaging (CTA neck, carotid duplex) to evaluate for carotid stenosis. In addition, antiplatelet therapy (e.g., aspirin) and aggressive risk factor modification (smoking cessation, control of hypertension, statin therapy) are essential. In pregnant or lactating patients, alternative imaging modalities (like carotid duplex ultrasound) may be preferred to minimize radiation exposure, though CTA can be performed with proper shielding if necessary.",
        "option_analysis": "Option A (MRI brain) is useful for detecting small infarcts but does not evaluate the carotid vasculature directly. Option B (CTA neck) is the most appropriate next step as it assesses the extracranial carotid arteries for atherosclerotic disease or dissection, which is critical in TIA workup. The other options are not provided and therefore are not considered.",
        "clinical_pearls": "1. TIA is a warning sign of potential future strokes\u2014prompt evaluation is crucial. 2. Vascular imaging (such as CTA neck) is indispensable to identify a treatable source of embolism. 3. Risk factor modification is a cornerstone of secondary prevention.",
        "current_evidence": "Recent guidelines from the American Heart Association emphasize rapid vascular imaging in TIA patients to identify high-risk lesions and guide early intervention. Studies continue to support early carotid imaging as part of a comprehensive stroke prevention strategy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993100",
    "fields": {
      "question_number": "75",
      "question_text": "Case scenario of a patient with high NIHSS then dropped down to 6 but still has dysarthria and weakness what do next?",
      "options": {
        "A": "Give t-PA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question concerns the management decision in acute ischemic stroke when there is dramatic early improvement but residual deficits persist. The key concept is that even if a patient\u2019s NIH Stroke Scale (NIHSS) improves, if disabling deficits remain, treatment with IV t-PA is still indicated.",
        "pathophysiology": "Acute ischemic stroke results from an arterial occlusion leading to brain tissue ischemia. Early reperfusion therapy (with t-PA) helps to salvage at-risk brain tissue. In some cases, spontaneous partial recanalization may occur, leading to improvement, but residual deficits (such as dysarthria and weakness) may still be significant and disabling.",
        "clinical_correlation": "Despite an initial high NIHSS, the patient\u2019s improvement to an NIHSS of 6 does not eliminate the possibility of a clinically significant and disabling stroke. Dysarthria and weakness can significantly impair daily functioning. The risk of deterioration or incomplete recovery supports proceeding with reperfusion therapy in eligible patients.",
        "diagnostic_approach": "The diagnostic workup includes a non-contrast CT scan (to rule out hemorrhage) and clinical scoring using the NIHSS. Differential considerations include transient ischemic attack (if deficits resolve completely) versus an evolving stroke. In this case, the persistent deficits indicate a stroke that may benefit from thrombolytic therapy.",
        "classification_and_neurology": "Acute ischemic stroke is classified within cerebrovascular diseases, specifically under ischemic strokes. The TOAST classification categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. The decision to administer thrombolysis is based on clinical presentation and timing rather than stroke subtype. The NIHSS provides a standardized measure of stroke severity and is integral to clinical trials and guidelines. This classification framework helps tailor secondary prevention but does not preclude acute reperfusion therapy when indicated.",
        "classification_and_nosology": "Ischemic stroke is classified based on clinical presentation and imaging findings. The patient\u2019s presentation falls under the category of an acute ischemic stroke with residual deficits despite some spontaneous improvement.",
        "management_principles": "According to current guidelines, IV t-PA is indicated for acute ischemic stroke within the 4.5-hour window unless contraindicated. First-line management is rapid thrombolysis with t-PA. For patients with residual disabling deficits, even after some improvement, reperfusion therapy is recommended. In pregnant patients, the use of t-PA is controversial but may be justified if benefits outweigh risks, and similarly in lactating patients, t-PA is considered relatively safe.",
        "option_analysis": "Option A (Give t-PA) is correct because the presence of residual disabling deficits (even with an improved NIHSS of 6) qualifies the patient for thrombolytic therapy provided he is within the window and no contraindications exist. The other options (B, C, D) were not provided, making t-PA the best and only provided management option.",
        "clinical_pearls": "1. Improvement in NIHSS does not automatically preclude the use of t-PA if deficits remain disabling. 2. Even an NIHSS of 6 can represent a stroke that significantly impairs function. 3. \u2018Rapidly improving\u2019 is a relative contraindication only if the deficits are non-disabling.",
        "current_evidence": "Recent stroke guidelines underscore that patients with \u2018rapid improvement\u2019 but residual disabling symptoms should not be excluded from thrombolysis. Updated research reinforces the benefit of t-PA in salvaging brain tissue in eligible patients, with several studies addressing the management of these borderline cases."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993101",
    "fields": {
      "question_number": "76",
      "question_text": "Case scenario of a patient with stroke syndrome findings suggestive of lateral pons (patient has hearing problem)?",
      "options": {
        "A": "AICA",
        "B": "PICA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This case centers on lateral pontine syndrome. The involvement of auditory pathways in the lateral pons is most characteristically associated with infarction of the territory supplied by the anterior inferior cerebellar artery (AICA).",
        "pathophysiology": "An infarct in the AICA territory affects the lateral pons where important structures including the cochlear nuclei are located, leading to symptoms such as hearing loss. Damage to the adjacent neural structures may also produce deficits like facial paralysis and ataxia.",
        "clinical_correlation": "In patients presenting with stroke symptoms localized to the lateral pons, the presence of hearing impairment strongly points toward an AICA infarct. This helps differentiate it from other brainstem syndromes (e.g., lateral medullary syndrome from PICA infarction) which rarely present with hearing loss.",
        "diagnostic_approach": "Diagnosis is supported by clinical exam and confirmed with neuroimaging (CT or MRI). Differential diagnoses include lateral medullary syndrome (PICA infarct) and other brainstem pathologies; however, the notable finding of hearing loss is more specific for AICA involvement.",
        "classification_and_neurology": "Brainstem strokes are classified based on the vascular territory involved: - **AICA syndrome:** lateral pontine infarction - **PICA syndrome:** lateral medullary infarction - **Basilar artery syndrome:** affecting midline pontine structures  This classification is part of the broader cerebrovascular disease taxonomy per the TOAST criteria and other stroke classification systems. The differentiation between AICA and PICA infarcts is crucial because they belong to distinct vascular territories with different clinical and therapeutic implications. Although both are posterior circulation strokes, their symptomatology and prognosis differ. Current consensus favors vascular territory-based classification to guide diagnosis and management, though overlap syndromes and anatomical variations can complicate classification.",
        "classification_and_nosology": "Brainstem strokes are classified by the vascular territory involved. An AICA stroke, which presents as lateral pontine syndrome, is distinct from PICA infarcts (lateral medullary syndrome) based on the structures involved and clinical findings.",
        "management_principles": "Acute management aligns with stroke protocols \u2013 rapid evaluation, consideration of thrombolytic therapy if within the window, and supportive care. Secondary prevention includes antiplatelets, statins, and risk factor management. In pregnancy or lactation, similar stroke guidelines apply; thrombolysis can be considered if benefits outweigh risks, with careful monitoring and multidisciplinary management.",
        "option_analysis": "Option A (AICA) is correct because hearing loss is a hallmark of lateral pontine syndrome due to AICA infarction. Option B (PICA) is incorrect because lateral medullary syndrome from PICA infarct typically spares hearing. Options C and D were not provided.",
        "clinical_pearls": "1. AICA infarcts classically present with ipsilateral hearing loss, vertigo, and facial weakness. 2. Differentiation from lateral medullary syndrome relies heavily on the presence of auditory symptoms. 3. Accurate localization aids in optimizing management strategies.",
        "current_evidence": "Recent neuroimaging advances have improved the diagnostic accuracy of brainstem strokes. Current guidelines continue to recommend prompt reperfusion therapy for eligible patients with posterior circulation strokes, with careful attention to clinical localization."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993102",
    "fields": {
      "question_number": "77",
      "question_text": "Attached picture of a patient with Horner\u2019s (ptosis, miosis) came with thunderclap HA, ct brain and LP done within 4 hr, was normal!!",
      "options": {
        "A": "Pcom aneurysm rupture",
        "B": "RCVS",
        "C": "ICA dissection"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This clinical scenario describes a patient who presents with thunderclap headache and signs of Horner\u2019s syndrome (ptosis and miosis). These features are highly suggestive of an internal carotid artery (ICA) dissection, a known cause of such presentations.",
        "pathophysiology": "ICA dissection occurs when a tear in the arterial wall allows blood to enter and split the layers of the vessel wall, often compromising the sympathetic plexus that runs along the artery. This results in Horner\u2019s syndrome. The sudden, severe headache (\u201cthunderclap headache\u201d) is a common presenting feature.",
        "clinical_correlation": "Patients with ICA dissection frequently present with a unilateral headache, neck pain, and ipsilateral Horner\u2019s syndrome. The normal CT scan and lumbar puncture (LP) help rule out subarachnoid hemorrhage, making ICA dissection the most likely diagnosis in this setting.",
        "diagnostic_approach": "Although the initial CT brain and LP are normal, further evaluation with CT angiography (or MR angiography) of the neck is essential to identify the dissection. Differentials include ruptured aneurysm (e.g., Pcom aneurysm rupture which typically shows hemorrhage on CT) and reversible cerebral vasoconstriction syndrome (RCVS, which usually lacks Horner\u2019s syndrome).",
        "classification_and_neurology": "ICA dissection is classified under extracranial arterial dissections within the broader category of cervicocranial arterial dissections, a subset of ischemic stroke etiologies. It is distinguished from intracranial dissections and other causes of thunderclap headache such as subarachnoid hemorrhage and RCVS. The nosology has evolved to recognize dissections as a distinct vascular pathology with unique clinical and imaging features. The International Classification of Headache Disorders (ICHD-3) includes headache attributed to arterial dissection as a secondary headache disorder, emphasizing the importance of identifying underlying vascular causes. Competing classifications sometimes group dissections with other vasculopathies, but current consensus supports their distinct categorization due to their specific pathophysiology and management.",
        "classification_and_nosology": "ICA dissection falls under the category of arterial dissection and is a specific subtype of ischemic stroke etiology. It is distinct from aneurysmal subarachnoid hemorrhage and RCVS based on clinical and imaging findings.",
        "management_principles": "Management of ICA dissection involves antithrombotic therapy (either antiplatelet agents or anticoagulation) to prevent thromboembolic complications. This is typically the first-line treatment. In cases where symptoms deteriorate or if there is evidence of compromised cerebral blood flow, endovascular repair may be considered. For pregnant or lactating patients, antithrombotic therapies (especially low-dose aspirin) are used with caution, considering the safety profiles and risk\u2013benefit assessments in these populations.",
        "option_analysis": "Option A (Pcom aneurysm rupture) would generally produce subarachnoid hemorrhage with positive CT/LP findings. Option B (RCVS) usually causes thunderclap headache without the classic finding of Horner\u2019s syndrome. Option C (ICA dissection) is correct because it best explains the combination of thunderclap headache and Horner\u2019s syndrome in the context of normal CT/LP findings.",
        "clinical_pearls": "1. Horner\u2019s syndrome in the setting of a thunderclap headache is a red flag for carotid dissection. 2. Normal CT and LP do not rule out ICA dissection; vascular imaging is required. 3. Early diagnosis and treatment with antithrombotic therapy can reduce the risk of subsequent stroke.",
        "current_evidence": "Current guidelines and recent studies continue to support the use of antithrombotic therapy as first-line management for cervical artery dissection. Advances in vascular imaging have significantly improved early detection, and updated consensus statements provide guidance on management in special populations such as pregnant and lactating patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993103",
    "fields": {
      "question_number": "78",
      "question_text": "SAH female young patient with symptomatic PComm aneurysm next?",
      "options": {
        "A": "Clipping",
        "B": "Coiling",
        "C": "Discharge",
        "D": "Medical treatment"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Aneurysmal subarachnoid hemorrhage (SAH) most often results from rupture of a cerebral aneurysm. In this case, a young female with a symptomatic posterior communicating artery (PComm) aneurysm presents a scenario where the key step is to secure the aneurysm to prevent rebleeding. Two primary methods are available: surgical clipping and endovascular coiling.",
        "pathophysiology": "The rupture of an aneurysm leads to blood extravasation into the subarachnoid space, provoking a cascade of events including increased intracranial pressure, inflammation, and vasospasm due to breakdown products of blood. The PComm aneurysm\u2019s location often makes it amenable to endovascular intervention because modern coiling techniques can effectively isolate the aneurysm from the circulation with lower invasiveness.",
        "clinical_correlation": "Patients with SAH typically present with a sudden, severe headache ('thunderclap headache'), along with signs of meningeal irritation and possible focal deficits depending on the hemorrhage location. Securing the aneurysm rapidly is critical to reduce the high risk of rebleeding in the acute phase.",
        "diagnostic_approach": "Initial diagnosis is made with a non-contrast CT scan of the head to identify hemorrhage. Following this, CT angiography or digital subtraction angiography is employed to localize and characterize the aneurysm, distinguishing it from other vascular lesions and guiding the treatment plan.",
        "classification_and_neurology": "Intracranial aneurysms are classified based on morphology (saccular/fusiform), size (small <7mm, large 7-12mm, giant >25mm), location (anterior vs. posterior circulation), and rupture status (ruptured vs. unruptured). The PComm aneurysm is a subtype of anterior circulation saccular aneurysm. SAH is classified by etiology (aneurysmal, traumatic, perimesencephalic) and severity (Hunt and Hess, Fisher scales). The management of aneurysmal SAH is guided by international consensus, including the American Heart Association/American Stroke Association (AHA/ASA) guidelines, which stratify treatment based on rupture status, aneurysm characteristics, and patient factors. Controversies exist regarding the best treatment modality for specific aneurysm types, but the consensus supports early aneurysm securing either by microsurgical clipping or endovascular coiling.",
        "classification_and_nosology": "Aneurysmal SAH is classified by the location and morphology of the aneurysm. PComm aneurysms are a subtype based on their anatomical location. The management approach falls under neurovascular interventions, where decisions between surgical clipping and endovascular coiling are made based on aneurysm characteristics, patient factors, and local expertise.",
        "management_principles": "Current guidelines (supported by studies such as ISAT) favor endovascular coiling for many aneurysms due to its less invasive nature and lower immediate morbidity compared to clipping. First-line treatment in a suitable aneurysm is coiling, provided the aneurysm morphology supports it. In women of child\u2010bearing age, careful attention is needed with radiation exposure and contrast use; multidisciplinary input ensures that pregnancy (or potential pregnancy) is managed appropriately. Second-line or alternative treatment is surgical clipping, which may be considered based on aneurysm anatomy or if endovascular expertise is unavailable.",
        "option_analysis": "Option A (Clipping) is a valid treatment modality but is more invasive; Option B (Coiling) is the chosen and correct option as it is typically preferred when the aneurysm\u2019s morphology is favorable; Option C (Discharge) is inappropriate given the life\u2010threatening nature of aneurysmal SAH; Option D (Medical treatment) is inadequate since active intervention is required to prevent rebleeding.",
        "clinical_pearls": "1) Nimodipine is used in SAH for vasospasm prophylaxis. 2) Endovascular coiling is less invasive and, in suitable aneurysms, has been shown to yield better short\u2010term outcomes. 3) Multidisciplinary evaluation is essential in determining the best approach for aneurysm management.",
        "current_evidence": "Recent updates and evidence from the International Subarachnoid Aneurysm Trial (ISAT) and subsequent studies support the use of endovascular coiling in anatomically favorable aneurysms. Advancements in endovascular technology continue to refine patient selection and improve outcomes."
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
