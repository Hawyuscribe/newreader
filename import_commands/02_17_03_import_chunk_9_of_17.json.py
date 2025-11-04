
# Import batch 3 of 3 from chunk_9_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993305",
    "fields": {
      "question_number": "334",
      "question_text": "A patient in the clinic he has continuous facial jerk and hand jerk (partials continua) how to treat:",
      "options": {
        "A": "iv valproic acid",
        "B": "iv diazepam",
        "C": "iv phenytoin",
        "D": "iv \u2026\u2026"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses a type of focal status epilepticus \u2013 continuous partial motor seizures (epilepsia partialis continua) \u2013 where abnormal electrical activity leads to repetitive jerking in specific muscle groups (e.g., face and hand). The immediate goal in management is to terminate the seizure activity, and benzodiazepines are the first\u2010line agents for status epilepticus.",
        "pathophysiology": "In status epilepticus, there is prolonged, unremitting neuronal firing. This occurs because inhibitory GABAergic mechanisms become impaired and excitatory activity becomes dominant. IV benzodiazepines (such as diazepam) enhance GABA-A receptor activity, helping to restore inhibitory tone and rapidly abort seizure activity. With continued seizures, receptor trafficking may render the seizures more refractory, which underpins the urgency of early intervention.",
        "clinical_correlation": "A patient with continuous facial and hand jerks is manifesting focal seizure activity. This focal status\u2014despite being limited to specific regions\u2014can evolve and cause structural injury if not controlled promptly. Recognizing the pattern and rapidly instituting therapy is key to preventing worsening neuronal injury.",
        "diagnostic_approach": "Diagnosis is primarily clinical though EEG confirmation is important if the diagnosis is in doubt. Differential diagnoses include epilepsia partialis continua secondary to structural lesions (e.g., stroke, tumor or infection) and non-epileptic movement disorders. Imaging (CT/MRI) helps evaluate for structural causes, while EEG confirms ongoing epileptiform activity.",
        "classification_and_nosology": "Epilepsia partialis continua is classified as a form of focal status epilepticus. It falls under the larger umbrella of status epilepticus, which is divided into convulsive and non-convulsive types, with focal or generalized onset.",
        "management_principles": "The latest guidelines (e.g., from the Neurocritical Care Society and ILAE) recommend immediate treatment of status epilepticus. First\u2010line management is IV benzodiazepines (diazepam, lorazepam) due to their rapid onset. If seizures persist, second\u2010line agents such as fosphenytoin, valproic acid, or levetiracetam are considered. In special populations such as pregnant or lactating women, the risks of fetal exposure to benzodiazepines (potential for fetal sedation, withdrawal) are weighed against the emergent need to control seizures, and therapy is individualized.",
        "option_analysis": "Option A (IV valproic acid) is recognized as a second-line option once benzodiazepines have been tried. Option B (IV diazepam) fits the first-line recommendation for acute seizure termination. Option C (IV phenytoin) is also generally used as a second-line agent. Option D is incomplete. Therefore, Option B is the correct initial treatment.",
        "clinical_pearls": "\u2022 In status epilepticus, prompt administration of benzodiazepines is critical, as delays increase morbidity and mortality.  \u2022 Recognize that focal status epilepticus may be due to an underlying lesion; work-up should include neuroimaging.",
        "current_evidence": "Recent evidence continues to support benzodiazepines as the first-line treatment in all forms of status epilepticus, with multiple guidelines emphasizing rapid administration to improve outcomes. Research is also ongoing concerning the optimal sequencing and combination of second-line agents."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993306",
    "fields": {
      "question_number": "335",
      "question_text": "Patient with large left ICA territory infarction with image of CT shown (massive acute infarction), was found to have AFIB what is the appropriate treatment next to start:",
      "options": {
        "A": "Aspirin",
        "B": "DAPT",
        "C": "dabigatran",
        "D": "warfarin"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question involves the acute management of a patient with a large left internal carotid territory infarction in the setting of atrial fibrillation (AF). AF is a common cause of cardioembolic stroke. However, in the setting of a massive infarct, the risk of hemorrhagic transformation must be carefully balanced against the benefits of anticoagulation.",
        "pathophysiology": "In patients with AF, emboli originating from the left atrium can lodge in the cerebral circulation (typically the ICA territory), leading to large infarctions. A massive infarct increases the risk of blood\u2013brain barrier disruption and hemorrhagic conversion, which can be exacerbated by early full-dose anticoagulation.",
        "clinical_correlation": "The CT showing a massive infarction indicates extensive brain tissue damage. Although AF typically mandates long-term anticoagulation for secondary stroke prevention, immediate initiation post-large infarct could precipitate hemorrhagic transformation. Thus, initial management with an antiplatelet agent is often preferred until the infarct stabilizes.",
        "diagnostic_approach": "Management begins with neuroimaging (CT/MRI) to assess infarct size and exclude hemorrhage, followed by cardiac evaluation (ECG, echocardiogram) for AF. Differential diagnoses include large artery atherosclerosis and lacunar strokes; however, the presence of AF shifts the etiology toward a cardioembolic source.",
        "classification_and_nosology": "Ischemic strokes are classified by etiology (cardioembolic, atherothrombotic, lacunar). In this scenario, the stroke is cardioembolic, associated with AF.",
        "management_principles": "For massive infarctions in patients with AF, current guidelines (AHA/ASA) recommend delaying full-dose anticoagulation by 1\u20132 weeks to reduce the risk of hemorrhagic transformation. In the acute phase, low-dose aspirin is used for antithrombotic therapy. When transitioning to long-term stroke prevention, direct oral anticoagulants (DOACs; e.g., dabigatran) or warfarin are considered, with DOACs often preferred in non-pregnant adults. For pregnant patients, warfarin is contraindicated, and low-molecular-weight heparin is often chosen, whereas lactating patients may use warfarin safely with monitoring.",
        "option_analysis": "Option A (Aspirin) is correct as the immediate treatment to bridge the patient while delaying anticoagulation. Option B (Dual antiplatelet therapy) is generally not indicated for cardioembolic strokes. Options C (dabigatran) and D (warfarin) represent long-term anticoagulation strategies but are not initiated immediately in the context of a massive infarct due to the heightened hemorrhagic risk.",
        "clinical_pearls": "\u2022 In cardioembolic strokes due to AF, full anticoagulation is essential for secondary prevention but must be timed appropriately after a large infarct.  \u2022 Massive infarcts require cautious initiation of any antithrombotic therapy to prevent hemorrhagic transformation.",
        "current_evidence": "Current research and recent guideline updates recommend a delayed approach to anticoagulation in large infarcts, highlighting the safety benefit of initial antiplatelet therapy (aspirin) before transitioning to full anticoagulation. Ongoing studies continue to refine the optimum timing balance between reducing recurrence and avoiding hemorrhage."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993307",
    "fields": {
      "question_number": "336",
      "question_text": "SCA artery infarction scenario what you will find also:",
      "options": {
        "A": "Rt. ptosis Ipsilateral"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question pertains to identifying additional clinical findings associated with a Superior Cerebellar Artery (SCA) infarction. SCA strokes typically affect structures of the cerebellum, leading to deficits in coordination and balance.",
        "pathophysiology": "The superior cerebellar artery supplies the superior aspect of the cerebellum, including regions responsible for coordinating limb movements and maintaining balance. Infarction in this territory can cause degeneration or dysfunction of the cerebellar cortex and deep nuclei, leading to ipsilateral cerebellar deficits.",
        "clinical_correlation": "Patients with SCA infarction may present with ipsilateral limb dysmetria, ataxia, dysdiadochokinesia (impaired ability to perform rapid alternating movements), and sometimes vertigo or nausea. These symptoms help differentiate the infarct from involvement of other cerebellar territories.",
        "diagnostic_approach": "Diagnosis is made via neuroimaging (MRI is more sensitive than CT for posterior fossa strokes) and clinical examination. Differentiation from infarctions in other cerebellar arterial territories, like the Anterior Inferior Cerebellar Artery (AICA) or Posterior Inferior Cerebellar Artery (PICA), rests on subtle differences in the clinical presentation \u2013 for example, AICA infarcts may also involve facial nerve findings, while PICA infarcts are associated with lateral medullary (Wallenberg) syndrome.",
        "classification_and_nosology": "Cerebellar strokes are categorized based on the vascular territory involved: SCA, AICA, or PICA infarctions. The SCA infarct is characterized by involvement of the superior cerebellum leading to distinct ipsilateral cerebellar signs.",
        "management_principles": "Management of an SCA stroke follows guidelines for acute ischemic stroke, including potential thrombolysis if within the therapeutic window, supportive care, and monitoring for complications such as cerebellar edema that could cause brainstem compression. In pregnant women, thrombolysis can be used if indicated after careful risk\u2013benefit analysis, and similar principles apply during lactation with attention to medication safety profiles.",
        "option_analysis": "Although the option texts are incomplete in this question, Option A mentions \u201cRt. ptosis Ipsilateral\u201d which is more suggestive of an oculomotor or midbrain involvement rather than a cerebellar syndrome. Option B is the marked answer and, based on classical SCA infarct presentations, likely represents clinical signs such as ipsilateral cerebellar ataxia and dysmetria. Without the full list, we assume Option B correctly identifies the typical cerebellar findings seen in SCA infarction.",
        "clinical_pearls": "\u2022 SCA infarctions classically produce ipsilateral cerebellar deficits rather than cranial nerve III findings (such as ptosis).  \u2022 A careful clinical examination paired with posterior fossa imaging is crucial in localizing cerebellar strokes.",
        "current_evidence": "The latest imaging techniques (especially diffusion-weighted MRI) have improved the detection of cerebellar infarcts. Recent stroke guidelines also emphasize a tailored approach to managing posterior circulation strokes, including vigilant monitoring for complications like brainstem compression in cerebellar infarctions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993308",
    "fields": {
      "question_number": "337",
      "question_text": "30 y/o male found unconscious at street What you expect as the mechanism of injury for attached CT (looked like coup countercoup bleed \"repeated question from previous exam\")",
      "options": {
        "A": "Aneurysmal",
        "B": "Trauma",
        "C": "HTN"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question highlights a scenario with a 30\u2010year\u2010old male found unconscious and a CT scan showing a lesion that resembles a coup\u2013countercoup injury. Coup\u2013countercoup injuries are a type of traumatic brain injury (TBI) resulting from blunt force trauma.",
        "pathophysiology": "In coup\u2013countercoup injuries, the brain is injured at the site of impact (coup) and on the opposite side (countercoup) due to the brain's movement within the skull. The rapid deceleration forces generate contusions and bruising, which can lead to intracranial hemorrhage and edema.",
        "clinical_correlation": "The patient\u2019s presentation (unconsciousness) combined with CT findings consistent with a coup\u2013countercoup injury points to a trauma-related mechanism. This distinguishes it from aneurysmal bleeds (which usually present with subarachnoid hemorrhage) or hypertensive hemorrhages (which typically affect deep brain structures in older individuals).",
        "diagnostic_approach": "Diagnosis is established with neuroimaging (CT scan being the first-line modality in acute trauma). Differential diagnoses include aneurysmal subarachnoid hemorrhage and hypertensive intracerebral hemorrhage; however, the imaging pattern and patient profile (young age, history of trauma) point toward a traumatic cause.",
        "classification_and_nosology": "Traumatic brain injuries are classified based on the mechanism (blunt vs. penetrating) and imaging findings (contusion, hemorrhage, diffuse axonal injury). Coup\u2013countercoup injuries are a specific subset of blunt brain injuries.",
        "management_principles": "Management of traumatic brain injury includes stabilization of airway, breathing, and circulation (the ABCs), followed by neuroimaging and neurosurgical evaluation. Intracranial pressure monitoring and supportive care are key components. For pregnant patients, while imaging with CT is generally avoided when possible due to radiation concerns, if necessary, appropriate shielding is used. The same management principles apply with heightened caution.",
        "option_analysis": "Option A (Aneurysmal) is incorrect as aneurysmal bleeds produce a different pattern (typically subarachnoid hemorrhage) and are less common in a young trauma patient. Option B (Trauma) is the correct answer, accurately reflecting the coup\u2013countercoup injury mechanism. Option C (Hypertension) is unlikely in a 30-year-old with traumatic findings and would more typically produce deep hemorrhages in older patients.",
        "clinical_pearls": "\u2022 Coup\u2013countercoup injuries result from inertial forces that damage both the site of impact and the opposite side; always consider trauma in young patients with such CT findings.  \u2022 Rapid identification and management of TBI are critical to prevent secondary brain injury.",
        "current_evidence": "Recent guidelines on traumatic brain injury emphasize early recognition, stabilization, and neuroimaging. Advances in CT technology have improved the early detection of coup\u2013countercoup lesions, and current management protocols stress the importance of monitoring intracranial pressure and using neuroprotective strategies where appropriate."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993309",
    "fields": {
      "question_number": "338",
      "question_text": "A female who develops transverse sinus thrombosis what is the most accurate statement to describe this patient",
      "options": {
        "A": "female sex is a major risk",
        "B": "seizure is the most common presenting symptoms",
        "C": "transverse sinus is the most commonly affected sinus in CVT"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral venous thrombosis (CVT) is a condition characterized by clot formation in the dural venous sinuses. It disproportionately affects women, largely due to risk factors such as oral contraceptive use, pregnancy, and the postpartum period.",
        "pathophysiology": "In CVT, thrombosis occurs in one or more of the dural venous sinuses resulting in impaired venous drainage, increased intracranial pressure, and possibly venous infarctions or hemorrhages. Hypercoagulable states, frequently encountered in females (e.g., due to estrogen exposure), play a central role.",
        "clinical_correlation": "Patients often present with headache (the most common symptom), focal neurological deficits, seizures, and signs of raised intracranial pressure. Although seizures may occur, they are not the predominant presenting feature. The strong female preponderance is a critical clue in the clinical scenario.",
        "diagnostic_approach": "Diagnosis is made with neuroimaging studies such as magnetic resonance imaging (MRI) combined with magnetic resonance venography (MRV). Differentials include migraines, meningitis, intracerebral hemorrhage, and subarachnoid hemorrhage, but the clinical context along with imaging aids in differentiation.",
        "classification_and_nosology": "CVT is classified under cerebrovascular diseases. It is categorized based on the location of the thrombus (e.g., involvement of the transverse sinus, superior sagittal sinus, etc.) and the underlying risk factors (prothrombotic conditions, infections, etc.).",
        "management_principles": "First-line management involves anticoagulation with low molecular weight heparin (LMWH) even in cases with hemorrhagic transformation. In pregnancy and lactation, LMWH is preferred due to its safety profile. Subsequent management includes transitioning to oral anticoagulants with appropriate monitoring and risk factor modification.",
        "option_analysis": "Option A (female sex is a major risk) is correct, as women are indeed at higher risk due to hormonal factors and related hypercoagulable states. Option B is incorrect because, although seizures can occur, headache remains the most common presenting symptom. Option C, while noting that the transverse sinus is a common site, is less accurate as literature variably points to both the superior sagittal and transverse sinuses; moreover, the emphasis on female risk makes option A more specific in this context.",
        "clinical_pearls": "1. Always assess for prothrombotic risk factors in women with CVT. 2. Headache is the most common presenting symptom in CVT. 3. Early anticoagulation is key to reducing morbidity.",
        "current_evidence": "Recent guidelines and research from the American Heart Association (AHA) endorse prompt anticoagulation in CVT. Studies continue to clarify which sinus is most commonly involved, yet the strong female predisposition remains universally acknowledged."
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
