
# Import batch 3 of 3 from chunk_14_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993287",
    "fields": {
      "question_number": "69",
      "question_text": "Patient presented with 6 hours right sided weakness including arm, leg and face with mild dysarthria. Brain CT showed acute left internal capsule infarction. What is the next step?",
      "options": {
        "A": "IV tpa",
        "B": "DAPT",
        "C": "Aspirin",
        "D": "?"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "In ischemic stroke management, timely initiation of antiplatelet therapy is crucial after the window for thrombolysis has passed. Aspirin is a cornerstone medication used to inhibit platelet aggregation and reduce the risk of further thrombotic events.",
        "pathophysiology": "Aspirin inhibits cyclooxygenase (COX-1), decreasing thromboxane A2 production, a potent aggregator of platelets. This reduces platelet activation and aggregation, thereby limiting the propagation of clot formation in cerebral vessels.",
        "clinical_correlation": "Patients presenting with stroke symptoms outside the window for thrombolytic therapy (typically 4.5 hours) are managed with antiplatelet therapy. Aspirin not only helps in preventing clot extension but also reduces the risk of early recurrent stroke.",
        "diagnostic_approach": "The diagnosis is primarily clinical corroborated by non-contrast CT to rule out hemorrhage. Differential considerations include hemorrhagic stroke (where aspirin is contraindicated) and stroke mimics like seizures or migraines.",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology and vascular territory. The TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology.  This patient's infarct in the internal capsule is consistent with a lacunar stroke subtype, typically caused by small vessel disease affecting penetrating arteries. However, management in the acute phase focuses on reperfusion rather than etiology.  The classification of stroke severity is often done using the NIH Stroke Scale (NIHSS), which helps guide treatment decisions and prognostication. This case exemplifies subcortical ischemic stroke within the broader cerebrovascular disease family.",
        "classification_and_nosology": "Ischemic strokes are classified by etiology (e.g., atherothrombotic, cardioembolic, lacunar). Aspirin is part of the standard management for non-cardioembolic strokes.",
        "management_principles": "First-line management for ischemic stroke within the therapeutic window is IV tPA; however, for patients presenting after the window, aspirin is initiated (usually a 160-325 mg loading dose). Dual antiplatelet therapy (DAPT) with aspirin and clopidogrel may be considered in minor strokes or high-risk transient ischemic attacks, particularly within the first 21 days. In pregnancy, low-dose aspirin is considered safe and is used for prevention and treatment in selected cases, with appropriate risk-benefit analysis.",
        "option_analysis": "Option A (IV tPA) is contraindicated beyond the typical window. Option B (DAPT) might be appropriate in minor stroke or TIA but is not the standard immediate management for a moderate to severe stroke in this scenario. Option C (Aspirin) is appropriate for a stroke presenting at 6 hours.",
        "clinical_pearls": "1. Aspirin should be initiated as soon as hemorrhage is excluded. 2. The therapeutic window for IV tPA is generally within 4.5 hours of symptom onset. 3. Early initiation of antiplatelet therapy improves outcomes in ischemic stroke.",
        "current_evidence": "Recent guidelines continue to support the use of aspirin for acute stroke management outside the IV tPA window. Studies have further refined the use of DAPT in select populations, particularly demonstrating benefits in minor strokes and TIAs."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993009",
    "fields": {
      "question_number": "141",
      "question_text": "Stroke patient presented within window brain Ct and CTA normal. NIHS 16 with BP200/140 what is next step.",
      "options": {
        "A": "Drop BP below 185/110 then give tPA",
        "B": "Cut perfusion"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke requiring thrombolytic therapy, it is critical to ensure blood pressure is within a safe range prior to administration to minimize the risk of hemorrhagic transformation.",
        "pathophysiology": "High blood pressure increases the risk of blood vessel rupture during thrombolysis, potentially leading to intracerebral hemorrhage. The standard is to control elevated blood pressure (target <185/110 mmHg) before administering IV tPA.",
        "clinical_correlation": "A patient presenting with a high NIHSS score and blood pressure above recommended thresholds must have their blood pressure lowered to mitigate the risk associated with thrombolytic therapy. Failure to control blood pressure can lead to catastrophic hemorrhagic complications.",
        "diagnostic_approach": "Diagnosis involves clinical evaluation and imaging confirmation of ischemic stroke. Differential diagnoses include hemorrhagic stroke (which would contraindicate tPA), subarachnoid hemorrhage, and stroke mimics. Continuous blood pressure monitoring is essential.",
        "classification_and_neurology": "Acute ischemic stroke is classified based on etiology (e.g., large artery atherosclerosis, cardioembolism, small vessel occlusion) and clinical severity (e.g., NIHSS score). The management falls under cerebrovascular disease classification per ICD-11 and AHA/ASA guidelines. Blood pressure management prior to thrombolysis is a critical component of acute stroke care protocols. The American Heart Association/American Stroke Association (AHA/ASA) guidelines provide consensus on BP thresholds for tPA eligibility. There is a well-established classification distinguishing ischemic stroke from hemorrhagic stroke, which influences treatment decisions such as thrombolysis eligibility.",
        "classification_and_nosology": "Acute ischemic strokes are categorized based on symptom severity and imaging findings. Management protocols such as the American Heart Association/American Stroke Association guidelines dictate blood pressure thresholds for safe tPA administration.",
        "management_principles": "First-line therapy for patients within the tPA window with ischemic stroke is IV tPA; however, only after blood pressure is lowered to below 185/110 mmHg using IV antihypertensives (e.g., labetalol, nicardipine). In patients with severe hypertension, blood pressure control is paramount. In pregnant patients, blood pressure management must be careful given fetal considerations, with medications such as labetalol being preferred due to safety profiles in pregnancy and lactation.",
        "option_analysis": "Option A (Drop BP below 185/110 then give tPA) is correct according to current guidelines. Option B (Cut perfusion) is nonspecific and not part of stroke management protocols.",
        "clinical_pearls": "1. Always check blood pressure before tPA administration; targets are <185/110 mmHg. 2. Rapid blood pressure control with appropriate IV medications is mandatory pre-thrombolysis. 3. Hypertensive emergency in stroke requires balancing cerebral perfusion and risk of hemorrhage.",
        "current_evidence": "Latest guidelines reinforce the necessity of strict blood pressure control before IV tPA administration in acute ischemic stroke. Ongoing studies address optimal management strategies for hypertensive emergencies in the context of stroke treatment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993010",
    "fields": {
      "question_number": "142",
      "question_text": "Elderly with quadriplegia, horizontal gaze palsy with spared vertical gaze, localization:",
      "options": {
        "A": "Pons",
        "B": "Thalamus"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Localization of brainstem lesions is based on the pattern of motor deficits and cranial nerve involvement. In this case, quadriplegia with horizontal gaze palsy and spared vertical gaze suggests a pontine involvement.",
        "pathophysiology": "The pons harbors important motor tracts and cranial nerve nuclei including the abducens nucleus and the paramedian pontine reticular formation (PPRF), which coordinate horizontal gaze. A lesion in the pons can disrupt these horizontal gaze centers while leaving the vertical gaze centers in the midbrain unaffected.",
        "clinical_correlation": "Clinically, patients with pontine lesions often present with locked-in syndrome or severe weakness in all four limbs (quadriplegia), along with specific deficits in horizontal eye movements while vertical movements remain intact. This constellation of findings strongly localizes the lesion to the pons.",
        "diagnostic_approach": "Localization is achieved through detailed neurological examination and supported by imaging studies such as MRI. Differential diagnoses include midbrain lesions (which typically affect vertical gaze) and thalamic lesions (which do not usually cause gaze palsies), helping narrow the diagnosis to a pontine lesion.",
        "classification_and_neurology": "Brainstem strokes are classified under ischemic stroke subtypes according to the TOAST criteria: large artery atherosclerosis, small vessel occlusion (lacunar), cardioembolism, etc. Pontine strokes specifically fall under brainstem infarcts and can be further subclassified by arterial territory\u2014paramedian, circumferential, or lacunar. Gaze palsies are classified by the affected gaze center: horizontal (pons) or vertical (midbrain). This case exemplifies a paramedian pontine infarct affecting the PPRF/abducens nucleus and corticospinal tracts. The nosology of gaze palsies also includes supranuclear versus nuclear/infranuclear lesions, with this being a nuclear/infranuclear lesion. Historically, brainstem stroke syndromes have been described by clinical signs (e.g., Millard-Gubler syndrome), reflecting advances in lesion localization.",
        "classification_and_nosology": "Brainstem strokes are classified based on the affected region (midbrain, pons, medulla) and the clinical syndromes they generate. Pontine strokes can lead to classic syndromes such as the 'locked-in' syndrome.",
        "management_principles": "Management of brainstem strokes involves supportive care, management of complications, and secondary prevention measures (like antiplatelet therapy, blood pressure control, and cholesterol management). In the acute setting, reperfusion therapy may be considered if the patient presents within the therapeutic window. For pregnant or lactating patients, treatment considerations include the safety profile of medications (e.g., low-dose aspirin) and supportive measures.",
        "option_analysis": "Option A (Pons) is correct because quadriplegia with isolated horizontal gaze palsy is consistent with a pontine lesion. Option B (Thalamus) does not explain the specific pattern of gaze abnormality or quadriplegia.",
        "clinical_pearls": "1. In pontine strokes, horizontal gaze palsy with spared vertical gaze is a key localizing sign. 2. Quadriplegia with these eye findings often indicates a lesion in the ventral pons. 3. Detailed neuro-ophthalmologic examination is essential for accurate localization.",
        "current_evidence": "Recent neuroimaging advances continue to improve localization of brainstem strokes. Current guidelines stress early recognition and supportive management while research into neuroprotective treatments and reperfusion strategies is ongoing."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993011",
    "fields": {
      "question_number": "143",
      "question_text": "Stroke patient presented within the window glucose 300 platelet 45000 BP 170/90 IV tPA not given, what the contraindication:",
      "options": {
        "A": "Glu",
        "B": "Platelet count",
        "C": "BP"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke, intravenous thrombolytic therapy (IV tPA) is administered within a narrow time window. However, strict inclusion/exclusion criteria must be met to minimize the risk of hemorrhagic complications. One key contraindication is a significantly low platelet count.",
        "pathophysiology": "Thrombolytic agents work by dissolving clots but they also carry the risk of causing bleeding. A sufficiently low platelet count (<100,000/\u00b5L) impairs clot formation and hemostasis, substantially increasing the risk of hemorrhage after tPA administration. Although elevated blood glucose or moderately high blood pressure can be concerning, they are not absolute contraindications as long as they are managed appropriately.",
        "clinical_correlation": "In the clinical scenario, the patient\u2019s blood pressure (170/90 mmHg) is below the critical threshold (usually 185/110 mmHg) for tPA use, and while a blood glucose of 300 mg/dL is high, hyperglycemia is not an absolute contraindication. The platelet count of 45,000/\u00b5L, however, is markedly low and represents an absolute contraindication because it significantly elevates the risk of bleeding complications.",
        "diagnostic_approach": "Before administering tPA in stroke patients, a rapid evaluation is needed\u2014this includes noncontrast CT brain imaging to rule out hemorrhage and laboratory tests (including platelet count, coagulation profile, and serum glucose). Differential considerations include ruling out hemorrhagic stroke, identifying metabolic abnormalities, and ensuring no contraindicating lab abnormalities are present.",
        "classification_and_neurology": "The use of IV tPA in acute ischemic stroke is classified under reperfusion therapies within cerebrovascular disease management guidelines. Contraindications are categorized as absolute or relative based on bleeding risk and outcome data. The American Heart Association/American Stroke Association (AHA/ASA) guidelines delineate these contraindications, which include severe hypertension, thrombocytopenia, recent surgery, and others. This classification aids clinicians in stratifying patients and making evidence-based decisions. Over time, classification systems have evolved with accumulating data, refining thresholds such as BP cutoffs and platelet counts to balance benefit and risk. Controversies persist regarding borderline values and individualized risk assessment, reflecting the dynamic nature of stroke management protocols.",
        "classification_and_nosology": "Acute ischemic stroke management is categorized by eligibility for reperfusion therapy. Contraindications to tPA (absolute vs relative) include factors such as low platelet count, extremely elevated blood pressure, recent surgery, and severe coagulopathy.",
        "management_principles": "According to the latest AHA/ASA guidelines, the presence of a platelet count less than 100,000/\u00b5L is an absolute contraindication to IV tPA. In a patient with low platelet count, tPA is withheld. Management then focuses on supportive care, possible alternative interventions, and addressing the cause of thrombocytopenia. In pregnant or lactating patients, similar contraindications apply, and alternative management strategies should be considered with multidisciplinary input.",
        "option_analysis": "Option A (Glucose) is not an absolute contraindication as high blood sugar is common in acute stroke but does not preclude tPA if managed. Option B indicating the low platelet count is the contraindication because a count of 45,000/\u00b5L is far below the safe threshold. Option C (BP) is acceptable since 170/90 mmHg is within limits. Option D is missing.",
        "clinical_pearls": "1. Always confirm laboratory values (especially platelet count) prior to thrombolysis in stroke. 2. A platelet count <100,000/\u00b5L is an absolute contraindication for tPA due to the high risk of hemorrhagic conversion. 3. Elevated blood pressure may be managed acutely, and hyperglycemia, while concerning, is not an exclusion if corrected.",
        "current_evidence": "Recent guidelines from the AHA/ASA continue to emphasize that a platelet count below 100,000/\u00b5L contraindicates tPA. Research and clinical audits have consistently demonstrated an increased hemorrhagic risk when tPA is administered in the context of thrombocytopenia."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993012",
    "fields": {
      "question_number": "144",
      "question_text": "One of the ICA branches:",
      "options": {
        "A": "SCA",
        "B": "Posterior Communicating",
        "C": "Ant com",
        "D": "AICA"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "A clear understanding of cerebrovascular anatomy is crucial in neurology. The internal carotid artery (ICA) is a major supplier of blood to the brain and gives off several branches that contribute to the Circle of Willis.",
        "pathophysiology": "ICA branches are responsible for distributing blood flow to key cerebral regions. The posterior communicating artery (PCOM) is one of these branches; it provides an important collateral pathway between the anterior and posterior circulations, potentially impacting stroke outcomes.",
        "clinical_correlation": "Knowledge of ICA branches is essential for evaluating vascular pathologies such as aneurysms and interpreting collateral circulation in stroke. Aneurysms frequently occur at branching points within the Circle of Willis, including the PCOM.",
        "diagnostic_approach": "When evaluating patients with suspected cerebrovascular disease, imaging modalities such as CT angiography or MR angiography are used to delineate vascular anatomy and identify anomalies. Differential considerations include differentiating between branches of the ICA versus those arising from the vertebrobasilar system.",
        "classification_and_neurology": "The cerebral arteries are classified based on their origin from the two primary arterial systems: the anterior circulation supplied by the internal carotid arteries and the posterior circulation supplied by the vertebrobasilar system. The ICA branches include the ophthalmic artery, posterior communicating artery, anterior choroidal artery, anterior cerebral artery, and middle cerebral artery. The posterior communicating artery is part of the Circle of Willis and acts as a crucial anastomotic vessel between anterior and posterior circulations. The superior cerebellar artery (SCA) and anterior inferior cerebellar artery (AICA) belong to the posterior circulation, arising from the basilar artery. The anterior communicating artery (ACom) is a midline vessel connecting the two anterior cerebral arteries and is not a branch of the ICA. Classification systems have evolved with advances in neuroimaging, allowing precise vascular mapping and improved understanding of stroke syndromes. Current consensus recognizes the functional significance of these arterial territories in clinical neurology and cerebrovascular pathology.",
        "classification_and_nosology": "The intracranial arterial system is classified into the anterior circulation (including the ICA and its branches) and the posterior circulation (involving the vertebrobasilar system). The posterior communicating artery belongs to the anterior circulation, while other arteries like the superior cerebellar artery (SCA) or anterior inferior cerebellar artery (AICA) belong to the posterior circulation.",
        "management_principles": "While this question focuses on anatomy rather than active management, it is important to recognize vascular branches when planning interventions, such as in the setting of aneurysmal clipping or endovascular therapy. In pregnant patients, radiation exposure during imaging is minimized through appropriate shielding and the use of MRI when feasible.",
        "option_analysis": "Option A (SCA) is incorrect because the superior cerebellar artery is typically a branch of the basilar artery. Option B (Posterior Communicating) is correct as it is a branch of the ICA. Option C (Anterior communicating) is not a branch of the ICA but connects the two anterior cerebral arteries. Option D (AICA) is incorrect because the anterior inferior cerebellar artery arises from the basilar artery.",
        "clinical_pearls": "1. The posterior communicating artery is a pivotal branch of the ICA, crucial for collateral blood flow within the Circle of Willis. 2. Misidentifying vascular branches can have implications during neurosurgical or endovascular procedures. 3. Always correlate anatomical knowledge with imaging findings.",
        "current_evidence": "Modern neuroradiologic studies and anatomical texts continue to validate the branch patterns of the ICA. These anatomical details are essential in the context of ischemic and hemorrhagic cerebrovascular pathology and guide current interventional and surgical therapies."
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
