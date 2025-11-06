
# Import batch 1 of 1 from chunk_17_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993263",
    "fields": {
      "question_number": "22",
      "question_text": "Which one is correct about anti thrombotic?",
      "options": {
        "A": "apixaban + rivaroxaban Ar direct thrombin inhibitor",
        "B": "aspirin is adenosine diposphate inhibitor",
        "C": "Ticagrelol is p2 y12 inhibitors",
        "D": "Clopidogrel is working on factor 1-2-5-7"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Antithrombotic agents are divided into two main categories: antiplatelet drugs (which prevent platelet aggregation) and anticoagulants (which interfere with the coagulation cascade). Each subgroup works via a distinct mechanism. For example, drugs like ticagrelor specifically target the P2Y12 receptor on platelets, whereas other agents such as apixaban or rivaroxaban target factor Xa in the coagulation cascade.",
        "pathophysiology": "Platelet activation and aggregation are key processes in thrombosis. Ticagrelor binds reversibly to the P2Y12 ADP receptor on platelets, thereby reducing ADP-mediated platelet activation, a crucial step in clot formation. In contrast, apixaban and rivaroxaban work by inhibiting factor Xa (not thrombin), aspirin works by irreversibly inhibiting cyclooxygenase-1 (COX-1) leading to reduced thromboxane A2 production, and clopidogrel also targets P2Y12 receptors rather than clotting factors.",
        "clinical_correlation": "The correct classification of these medications is critical when treating or preventing thrombotic events such as myocardial infarction, stroke, or deep venous thrombosis. Misattributing their mechanisms can lead to inappropriate management choices, affecting patient safety especially in settings requiring precise antithrombotic therapy.",
        "diagnostic_approach": "No laboratory diagnostic test is needed to choose the appropriate antithrombotic; however, clinicians should consider patient-specific factors (renal function, bleeding risk, etc.) when deciding among these medications. Platelet function tests or coagulation panels may be used in select situations to monitor therapy.",
        "classification_and_neurology": "Antithrombotic agents are classified broadly into antiplatelet drugs and anticoagulants. Antiplatelet drugs include COX inhibitors (aspirin), ADP receptor antagonists (clopidogrel, ticagrelor, prasugrel), and glycoprotein IIb/IIIa inhibitors. Anticoagulants include vitamin K antagonists (warfarin), direct thrombin inhibitors (dabigatran), and direct factor Xa inhibitors (apixaban, rivaroxaban, edoxaban). This classification is based on their molecular targets and mechanisms. The American Heart Association/American Stroke Association (AHA/ASA) guidelines categorize stroke prevention therapies accordingly. Over time, DOACs have largely supplanted warfarin due to better safety and ease of use. Controversies remain regarding optimal antithrombotic regimens in certain stroke subtypes and dual antiplatelet therapy duration.",
        "classification_and_nosology": "Antithrombotic medications are broadly classified as antiplatelet agents (aspirin, ticagrelor, clopidogrel) and anticoagulants (e.g., direct factor Xa inhibitors like apixaban and rivaroxaban, versus direct thrombin inhibitors such as dabigatran).",
        "management_principles": "Management with these agents should be individualized and guided by current guidelines such as those from the ACC/AHA or the European Society of Cardiology. In pregnant or lactating women, low molecular weight heparin is preferred over agents with potential fetal risks. Selection should be based on the clinical scenario\u2014acute coronary syndrome, stroke prevention, or venous thromboembolism prevention.",
        "option_analysis": "Option A is incorrect because apixaban and rivaroxaban are direct factor Xa inhibitors, not direct thrombin inhibitors. Option B is incorrect as aspirin works by blocking cyclooxygenase-1, not by inhibiting adenosine diphosphate. Option C is correct because ticagrelor acts as a P2Y12 inhibitor. Option D is incorrect since clopidogrel works as a P2Y12 receptor inhibitor after its hepatic activation and does not act on clotting factors 1, 2, 5, or 7.",
        "clinical_pearls": "1. Ticagrelor is distinguished from other P2Y12 inhibitors by its reversible binding and lack of requirement for metabolic activation. 2. Direct factor Xa inhibitors are fundamental in the management of various thrombotic conditions, in contrast to direct thrombin inhibitors. 3. Aspirin\u2019s antiplatelet effect is achieved through COX-1 inhibition, ultimately reducing thromboxane A2 production.",
        "current_evidence": "Recent updates in cardiology and thrombosis guidelines emphasize precise mechanism-based therapy. Studies continue to refine the relative advantages of each antithrombotic agent, supporting the use of ticagrelor in certain acute coronary syndromes and underscoring the need for individualized patient risk stratification."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993264",
    "fields": {
      "question_number": "23",
      "question_text": "26 Young lady with SLE complained of seizures and confusion this time. SLE nephritis on dialysis. What is your diagnosis? MRV was venous thrombosis in transverse CVT",
      "options": {
        "A": "CVT"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral venous thrombosis (CVT) is a subtype of stroke caused by thrombosis in the cerebral veins or dural sinuses. Its presentation can include seizures, headache, altered mental status, and other neurological deficits, particularly in patients with prothrombotic conditions such as systemic lupus erythematosus (SLE).",
        "pathophysiology": "In SLE, especially when associated with antiphospholipid syndrome, patients are predisposed to a hypercoagulable state. Thrombosis within the cerebral venous system, particularly in the transverse sinus as seen on MRV, can lead to venous congestion and increased intracranial pressure, which manifests as neurological symptoms including seizures and confusion.",
        "clinical_correlation": "A young SLE patient with seizures and confusion, along with a history of lupus nephritis on dialysis, is at increased risk for thrombotic events. The MRV finding of venous thrombosis in the transverse sinus supports the diagnosis of CVT, aligning well with her clinical presentation.",
        "diagnostic_approach": "Diagnosis is primarily confirmed with MR venography (MRV), which clearly visualizes thrombosis in the venous sinuses. Differential diagnoses include arterial stroke, infectious processes like encephalitis, or metabolic encephalopathies; however, clinical context combined with MRV findings differentiates CVT.",
        "classification_and_neurology": "CVT is classified under cerebrovascular diseases, specifically venous strokes, distinct from arterial ischemic strokes or hemorrhagic strokes. The International Classification of Headache Disorders (ICHD) and the American Heart Association/American Stroke Association (AHA/ASA) classify CVT as a subtype of stroke due to venous occlusion. Within CVT, classification can be based on the involved venous structures (e.g., superior sagittal sinus, transverse sinus, deep cerebral veins), etiology (e.g., prothrombotic states, infections, malignancy), and clinical presentation. SLE-associated CVT falls under secondary CVT due to systemic autoimmune disease and hypercoagulability, often linked to antiphospholipid syndrome (APS) overlap. Over time, classification systems have evolved to emphasize etiological factors and imaging findings, improving diagnostic accuracy and guiding management. Controversies remain regarding the optimal classification of autoimmune-related CVT, especially in patients with overlapping syndromes or concurrent dialysis-related coagulopathies.",
        "classification_and_nosology": "CVT is classified under cerebrovascular disorders and is distinct from arterial ischemic stroke due to its venous origin. It is an important diagnostic consideration in young patients, especially women with underlying risk factors such as SLE.",
        "management_principles": "Management of CVT involves prompt anticoagulation, typically beginning with low molecular weight heparin even in cases where there is associated hemorrhagic transformation. Subsequent transition to oral anticoagulants is common. In pregnant patients, LMWH is the treatment of choice due to its favorable safety profile. Dialysis patients require careful management due to altered pharmacokinetics and bleeding risk.",
        "option_analysis": "Option A is correct because the clinical picture and MRV findings clearly point to a diagnosis of CVT. The other options, though not provided, would likely be irrelevant or not fit the clinical scenario described.",
        "clinical_pearls": "1. SLE patients, particularly those with antiphospholipid antibodies, are at high risk for venous thrombosis including CVT. 2. MRV is the gold standard imaging modality for diagnosing CVT. 3. Anticoagulation remains the cornerstone of treatment, even in the setting of intracranial hemorrhage associated with CVT.",
        "current_evidence": "The latest guidelines from the American Heart Association and the European Stroke Organization support early initiation of anticoagulation in CVT, highlighting improved outcomes with timely intervention. Ongoing research emphasizes individualized therapy durations and monitoring in patients with underlying autoimmune conditions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993265",
    "fields": {
      "question_number": "24",
      "question_text": "Which of the following is the correct mechanism of action of these medications:\n- Aspirin inhibits adenosine deaminase\n- Ticagrelor inhibits P2Y12\n- Apixaban and rivaroxaban are direct thrombin inhibitors\n- Clopidogrel inhibits factor 7, 10, 11, 12",
      "options": {
        "A": "Aspirin inhibits adenosine deaminase",
        "B": "Ticagrelor inhibits P2Y12",
        "C": "Apixaban and rivaroxaban are direct thrombin inhibitors",
        "D": "Clopidogrel inhibits factor 7, 10, 11, 12"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "A solid grasp of the mechanisms of antithrombotic medications is crucial for their correct use in clinical practice. Each medication class has a defined target which guides its use in preventing thrombosis.",
        "pathophysiology": "Aspirin exerts its effect by irreversibly inhibiting cyclooxygenase-1 (COX-1), thereby reducing thromboxane A2 synthesis; it does not inhibit adenosine deaminase. Ticagrelor selectively and reversibly inhibits the P2Y12 receptor on platelets, blocking ADP-induced platelet activation. Apixaban and rivaroxaban inhibit factor Xa, not thrombin. Clopidogrel, after metabolic activation, also blocks the P2Y12 receptor rather than affecting multiple clotting factors.",
        "clinical_correlation": "Accurate identification of these mechanisms is essential when selecting treatment for preventing arterial and venous thrombotic events. The choice and dosing of these agents are guided by factors such as the patient\u2019s risk profile, co-morbid conditions, and specific cardiovascular or cerebrovascular event risk.",
        "diagnostic_approach": "While direct laboratory tests for these mechanisms are not usually necessary, clinicians use a patient\u2019s history, risk factors, and sometimes specialized assays (like platelet function tests) to guide therapy in complex cases.",
        "classification_and_neurology": "Antithrombotic agents are classified broadly into antiplatelet drugs and anticoagulants. Antiplatelet agents include COX inhibitors (aspirin), P2Y12 receptor antagonists (clopidogrel, ticagrelor, prasugrel), and glycoprotein IIb/IIIa inhibitors. Anticoagulants include vitamin K antagonists (warfarin), direct oral anticoagulants (DOACs) subdivided into direct thrombin inhibitors (dabigatran) and factor Xa inhibitors (apixaban, rivaroxaban, edoxaban). This classification is based on their molecular targets within the hemostatic system. Nosologically, these drugs belong to the pharmacological family of antithrombotic agents, essential in cerebrovascular disease management. Over time, the classification has evolved with the development of DOACs that offer targeted inhibition with improved safety profiles compared to older agents. Controversies remain regarding optimal combinations and durations of therapy, especially in complex cerebrovascular disease and concomitant cardiac conditions.",
        "classification_and_nosology": "These medications fit into two primary groups: antiplatelet agents (aspirin, ticagrelor, clopidogrel) and anticoagulants (apixaban, rivaroxaban). Each group is defined by its target within the clotting process.",
        "management_principles": "Management should follow evidence-based guidelines. For instance, ticagrelor is preferred in certain acute coronary syndromes. In pregnant and lactating patients, clinicians must balance efficacy with safety; LMWH is often preferred over direct oral anticoagulants due to limited safety data in these populations.",
        "option_analysis": "Option A is incorrect; aspirin does not inhibit adenosine deaminase but rather COX enzymes. Option B is correct, as ticagrelor indeed works by inhibiting the P2Y12 receptor. Option C is incorrect because apixaban and rivaroxaban are factor Xa inhibitors, not direct thrombin inhibitors. Option D is incorrect as clopidogrel inhibits the P2Y12 receptor instead of multiple clotting factors (7, 10, 11, and 12).",
        "clinical_pearls": "1. Ticagrelor\u2019s reversible P2Y12 inhibition sets it apart from clopidogrel\u2019s irreversible mechanism, which is clinically significant in situations requiring rapid platelet function recovery. 2. Direct factor Xa inhibitors are distinct in their function from direct thrombin inhibitors like dabigatran. 3. Aspirin\u2019s benefit in preventing thrombotic events is due to its inhibition of thromboxane A2 synthesis.",
        "current_evidence": "Recent updates in cardiovascular guidelines reinforce the specific roles of antithrombotic agents based on their mechanisms. Ongoing studies continue to assess safety profiles and optimal usage strategies, particularly in special populations such as the elderly or those with renal impairment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993266",
    "fields": {
      "question_number": "25",
      "question_text": "Patient had cerebellar ICH near 4th ventricle with dilated lateral ventricles and 3rd ventricle. Which of the following is next:",
      "options": {
        "A": "Insert EVD and release high ICP",
        "B": "Do CT angio to look for posterior criculation aneurysm",
        "C": "Other choices I forgot which were irrelevant"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Cerebellar hemorrhage, particularly near the fourth ventricle, raises concern for obstructive hydrocephalus. When blood obstructs CSF pathways, increased intracranial pressure (ICP) can occur, necessitating prompt intervention.",
        "pathophysiology": "A hemorrhage in the cerebellum adjacent to the fourth ventricle can mechanically block the flow of cerebrospinal fluid (CSF), leading to dilation of the lateral and third ventricles. This obstructive hydrocephalus results in elevated ICP, which may cause neurological deterioration if not relieved.",
        "clinical_correlation": "Patients with cerebellar hemorrhage may present with signs of raised ICP such as headache, nausea, altered mental status, and brainstem compression symptoms. The noted dilation of the lateral and third ventricles confirms hydrocephalus secondary to obstruction at the fourth ventricle.",
        "diagnostic_approach": "A non-contrast head CT is typically used to identify a cerebellar hemorrhage and the presence of ventricular enlargement. Differential diagnoses include primary intraventricular hemorrhage or brainstem stroke, but the location of the bleed and ventricular dilation help to pinpoint the cause as obstructive hydrocephalus secondary to cerebellar ICH.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on location (lobar, deep, cerebellar, brainstem), etiology (hypertensive, amyloid angiopathy, vascular malformations), and clinical severity. Cerebellar hemorrhages are a subset of posterior fossa hemorrhages and are distinct due to their anatomical constraints.  Hydrocephalus is classified as communicating or non-communicating (obstructive). In this case, the hydrocephalus is obstructive due to blockage at the fourth ventricle level.  The American Heart Association/American Stroke Association (AHA/ASA) guidelines on spontaneous ICH recognize cerebellar hemorrhages with hydrocephalus as a neurosurgical emergency. The classification of hemorrhage size (>3 cm in cerebellum) and presence of hydrocephalus guide management decisions.  No major controversies exist regarding the classification of cerebellar ICH with obstructive hydrocephalus; however, debates continue regarding timing and extent of surgical intervention in certain cases.",
        "classification_and_nosology": "Cerebellar hemorrhages are a subset of intracerebral hemorrhages. They are particularly dangerous due to the limited space within the posterior fossa and the potential for rapid deterioration from brainstem compression and obstructive hydrocephalus.",
        "management_principles": "Immediate management focuses on lowering the ICP. The first-line intervention in the setting of obstructive hydrocephalus due to cerebellar hemorrhage is the insertion of an external ventricular drain (EVD) to relieve high ICP. In some cases, additional neurosurgical procedures like suboccipital decompression may be required. In pregnant patients, CT imaging remains justified in emergencies and neurosurgical interventions are performed with appropriate obstetrical support and monitoring, ensuring both maternal and fetal safety.",
        "option_analysis": "Option A is correct because inserting an EVD addresses the raised ICP by draining the CSF and reducing ventricular pressure. Option B is less appropriate as CT angiography to evaluate for a posterior circulation aneurysm is not the immediate concern in a scenario where hydrocephalus is causing the patient\u2019s symptoms. Option C (and any irrelevant choices) do not address the urgent life-threatening increase in ICP.",
        "clinical_pearls": "1. Obstructive hydrocephalus secondary to cerebellar hemorrhage is a neurosurgical emergency. 2. EVD placement is crucial to managing elevated ICP in the setting of ventricular dilation. 3. Rapid intervention can prevent further brainstem compromise and improve outcomes.",
        "current_evidence": "Current neurosurgical guidelines support early EVD placement for patients with obstructive hydrocephalus due to cerebellar hemorrhage. Recent research emphasizes the importance of rapid ICP management and has refined criteria for when to escalate to additional surgical decompression."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993267",
    "fields": {
      "question_number": "26",
      "question_text": "male elderly with left side weakness dysarthria on dabigatran underwent thrombectomy only no tpa given later has ct of bleeding what you will give that was the cause of increase bleeding",
      "options": {
        "A": "Osmotic therapy",
        "B": "Idrucizumab",
        "C": "Vit k"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "This case involves an elderly male on dabigatran, a direct thrombin inhibitor, who developed intracranial hemorrhage after thrombectomy. The key concept is managing life\u2010threatening bleeding by reversing the anticoagulant effect. Idarucizumab is the specific reversal agent approved for dabigatran-induced bleeding.",
        "pathophysiology": "Dabigatran directly inhibits thrombin, preventing the conversion of fibrinogen to fibrin and impairing clot formation, which may precipitate bleeding. Idarucizumab, a monoclonal antibody fragment, binds dabigatran with high affinity, neutralizing its activity rapidly and restoring normal coagulation. Its use is supported by clinical trials showing prompt reversal of anticoagulation in emergency bleeding events.",
        "clinical_correlation": "In this patient, the CT scan revealed intracranial hemorrhage following thrombectomy. The presence of dabigatran poses an increased risk of hemorrhagic complications. Administering idarucizumab is critical to stabilize the patient by counteracting the drug's anticoagulant effects, thereby reducing the progression of bleeding.",
        "diagnostic_approach": "The diagnosis is supported by neuroimaging (CT) demonstrating intracranial bleeding in the setting of dabigatran therapy. Differential diagnoses include hemorrhagic transformation of ischemic stroke, hypertensive intracerebral hemorrhage, or hemorrhage due to other coagulopathies. Assessing coagulation parameters and medication history is central to refining the diagnosis.",
        "classification_and_neurology": "This clinical scenario falls under the classification of ischemic stroke complicated by anticoagulant-associated intracerebral hemorrhage. Stroke classification systems such as the TOAST criteria categorize ischemic strokes by etiology, while hemorrhagic transformation is considered a complication rather than a separate disease entity. Anticoagulant-associated ICH is a recognized subtype of hemorrhagic stroke, distinct from primary spontaneous ICH. The management aligns with guidelines for anticoagulant-related bleeding events, which classify reversal agents based on the type of anticoagulant (e.g., vitamin K antagonists vs. direct oral anticoagulants). This case highlights the importance of classification in guiding targeted reversal therapy.",
        "classification_and_nosology": "Bleeding complications associated with direct oral anticoagulants (DOACs) fall under DOAC-related hemorrhage. Specifically, dabigatran-induced bleeding is managed differently from warfarin-related bleeding, with the latter reversed by vitamin K. This scenario is classified as a major hemorrhagic event in patients taking dabigatran.",
        "management_principles": "First-line management of dabigatran-associated bleeding involves prompt reversal with idarucizumab (a typical dose of 5 g IV, administered as two 2.5 g infusions). Supportive care, including blood pressure control and intracranial pressure management, may be necessary. Second-line measures, if bleeding persists, include additional supportive interventions. In pregnant or lactating patients, the use of idarucizumab should be considered only if the benefits outweigh potential risks, as data in this population are limited.",
        "option_analysis": "Option A (Osmotic therapy) is used for reducing intracranial pressure but does not reverse the coagulation defect. Option B (Idarucizumab) is the approved and specific reversal agent for dabigatran, making it correct. Option C (Vitamin K) reverses warfarin effects, not dabigatran. Option D is not provided, hence only option B is appropriate.",
        "clinical_pearls": "\u2022 Idarucizumab efficiently reverses dabigatran effects within minutes, crucial for life-threatening bleeds. \u2022 Always verify a patient\u2019s anticoagulant regimen when managing intracranial hemorrhage. \u2022 Differentiation of DOAC reversal agents from those used for warfarin is essential for proper management.",
        "current_evidence": "Recent guidelines from bodies such as the American Heart Association and evidence from clinical trials support the use of idarucizumab for dabigatran reversal in bleeding emergencies. Ongoing research continues to affirm its efficacy and safety profile in managing DOAC-associated hemorrhage."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993268",
    "fields": {
      "question_number": "27",
      "question_text": "A patient had a head trauma, after 10 days developed spontaneous perimesencephalic SAH. Done 2 digital subtraction imaging 2 weeks apart which was unremarkable, which of the following is the appropriate management:",
      "options": {
        "A": "Send him home with F/U in the clinic",
        "B": "Repeat digital subtraction imaging",
        "C": "MR angiography",
        "D": "CT angiography"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses the management of a patient with a perimesencephalic subarachnoid hemorrhage (SAH) following head trauma. The key concept is recognizing that a non-aneurysmal perimesencephalic SAH, confirmed by two negative digital subtraction angiographies (DSAs), typically has a benign clinical course and warrants conservative management.",
        "pathophysiology": "Perimesencephalic SAH is often venous in origin and is characterized by a limited distribution of blood around the midbrain. Unlike aneurysmal SAH, it does not involve a ruptured cerebral aneurysm and is associated with minimal risk of rebleeding. The absence of vascular abnormalities on repeated DSAs further supports a benign etiology.",
        "clinical_correlation": "Patients with perimesencephalic SAH usually present with a sudden headache and may have mild neurological complaints but tend to have a favorable prognosis. The negative imaging studies reduce worry about a missed aneurysm, thereby supporting outpatient management with appropriate follow-up rather than further invasive testing.",
        "diagnostic_approach": "The diagnosis is established by neuroimaging, starting with CT which shows the characteristic pattern of hemorrhage around the midbrain. Digital subtraction angiography is the gold standard to rule out an aneurysm. Differential diagnoses include aneurysmal SAH, traumatic SAH from high-impact injury, and other vascular malformations. Serial imaging and clinical observation help differentiate these conditions.",
        "classification_and_neurology": "PM-SAH is classified as a subtype of non-aneurysmal spontaneous subarachnoid hemorrhage. The broader classification of SAH includes traumatic vs spontaneous, with spontaneous further subdivided into aneurysmal and non-aneurysmal. Non-aneurysmal SAH can be perimesencephalic or non-perimesencephalic based on bleeding pattern. The Fisher grading scale for SAH on CT helps predict vasospasm risk but is less applicable in PM-SAH due to limited blood volume. The World Federation of Neurosurgical Societies (WFNS) grading system applies to clinical severity but PM-SAH patients usually present with low grades. The current nosological consensus recognizes PM-SAH as a distinct clinical and radiological entity with a benign prognosis, separate from aneurysmal SAH which carries significant morbidity and mortality. Some controversy exists regarding the need for repeated angiography, but consensus favors limited imaging once aneurysms are excluded.",
        "classification_and_nosology": "Perimesencephalic SAH is a subtype of non-aneurysmal subarachnoid hemorrhage. It is classified separately from aneurysmal SAH due to its benign nature, distinct bleeding pattern, and low risk of complications. This nosological distinction guides both prognosis and management.",
        "management_principles": "First-line management of non-aneurysmal perimesencephalic SAH is conservative. This includes observation, adequate analgesia, and sometimes short hospital admission for monitoring of potential complications (e.g., vasospasm). When two DSAs are negative, further invasive imaging is not needed, and the patient can be safely discharged with close outpatient follow-up. In pregnant or lactating patients, minimizing unnecessary radiation exposure is important; thus, when vascular imaging is not indicated, conservative management is particularly preferred.",
        "option_analysis": "Option A (Send him home with follow-up in the clinic) is appropriate given the benign nature of perimesencephalic SAH and two repeatedly negative DSAs. Option B (Repeat digital subtraction imaging) is unnecessary after two high-quality negative studies. Option C (MR angiography) and Option D (CT angiography) are not warranted when DSAs have definitively ruled out aneurysmal pathology and would expose the patient to additional, often unnecessary, investigations.",
        "clinical_pearls": "\u2022 Non-aneurysmal perimesencephalic SAH generally has an excellent prognosis with low rebleeding risk. \u2022 Two consecutive negative DSAs reliably exclude an aneurysmal source, making further invasive studies redundant. \u2022 Conservative management with outpatient follow-up is the standard approach once serious vascular abnormalities are ruled out.",
        "current_evidence": "Recent studies and updated AHA/ASA guidelines support the conservative management of non-aneurysmal perimesencephalic SAH. The evidence indicates that after two negative DSAs, further invasive testing does not improve outcomes and may unnecessarily expose patients to procedure-related risks."
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
