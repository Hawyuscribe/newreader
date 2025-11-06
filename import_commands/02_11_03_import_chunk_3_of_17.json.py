
# Import batch 3 of 3 from chunk_3_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993047",
    "fields": {
      "question_number": "219",
      "question_text": "30 y.o male found unconscious at street. What you expect as the mechanism of injury for attached CT",
      "options": {
        "A": "(Aneurysmal) is incorrect because aneurysmal ruptures typically produce subarachnoid hemorrhage in a non",
        "B": "(Trauma) is correct as the patient\u2019s history and clinical situation strongly indicate a traumatic injury. Option C (Hypertension) is incorrect because hypertensive hemorrhages generally occur in older individuals with a history of poorly controlled blood pressure and typically involve deep brain regions."
      },
      "correct_answer": "b",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This case involves a young male found unconscious outdoors, which strongly suggests a traumatic mechanism. In trauma cases, the evaluation focuses on identifying intracranial injuries such as hematomas, contusions, or diffuse axonal injury.",
        "pathophysiology": "Traumatic brain injuries (TBIs) result from external mechanical forces that disrupt normal cerebral function. Vessel rupture due to blunt force trauma can lead to various hemorrhages (e.g., epidural, subdural) and parenchymal contusions.",
        "clinical_correlation": "A 30-year-old male found unconscious is more likely to have suffered head trauma rather than a spontaneous hemorrhage from hypertension or an aneurysmal rupture. The CT appearance in traumatic injury typically includes localized hemorrhages or contusions, often with a pattern distinct from spontaneous bleeds seen in hypertensive or aneurysmal events.",
        "diagnostic_approach": "Immediate non-contrast CT imaging is used to identify intracranial hemorrhages and traumatic injuries. Differential diagnoses include aneurysmal subarachnoid hemorrhage (which usually presents with a severe headache and a different bleeding pattern on CT) and hypertensive hemorrhage (characteristically seen in older patients with chronic hypertension involving deep brain structures).",
        "classification_and_neurology": "Intracranial hemorrhages are classified based on location and etiology. The major categories include:  - Traumatic hemorrhages: epidural hematoma, subdural hematoma, traumatic intracerebral hemorrhage, subarachnoid hemorrhage from trauma. - Non-traumatic spontaneous hemorrhages: hypertensive hemorrhage, aneurysmal subarachnoid hemorrhage, hemorrhagic transformation of ischemic stroke, cerebral amyloid angiopathy-related hemorrhage.  The International Classification of Diseases (ICD) and the American Heart Association/American Stroke Association (AHA/ASA) stroke classifications incorporate these distinctions.   This classification aids in prognosis and management decisions. The evolution of classification systems has emphasized imaging characteristics and clinical context. Some controversy exists in differentiating traumatic from spontaneous hemorrhages in patients with unclear history, but imaging patterns and clinical correlation help resolve this.",
        "classification_and_nosology": "Traumatic brain injury is classified based on the mechanism (blunt versus penetrating) and the type of intracranial injury (e.g., epidural hematoma, subdural hematoma, contusion). This case falls under blunt force trauma.",
        "management_principles": "Management of TBI includes rapid neurosurgical evaluation, maintenance of airway, breathing, and circulation, and intracranial pressure monitoring when indicated. Surgical intervention may be necessary if there is significant hematoma with mass effect. In pregnant patients, imaging protocols are adjusted to minimize fetal exposure while ensuring maternal safety, and similar principles apply for lactating patients with careful counseling regarding radiation exposure.",
        "option_analysis": "Option A (Aneurysmal) is incorrect because aneurysmal ruptures typically produce subarachnoid hemorrhage in a non-traumatic context with a characteristic severe headache. Option B (Trauma) is correct as the patient\u2019s history and clinical situation strongly indicate a traumatic injury. Option C (Hypertension) is incorrect because hypertensive hemorrhages generally occur in older individuals with a history of poorly controlled blood pressure and typically involve deep brain regions.",
        "clinical_pearls": "1. In young patients found unconscious, always consider trauma as the primary cause of intracranial injury. 2. CT imaging is crucial to distinguishing between traumatic and spontaneous intracranial hemorrhages. 3. Traumatic hemorrhages have characteristic CT patterns that differ from hypertensive or aneurysmal bleeds.",
        "current_evidence": "Recent trauma guidelines stress the importance of rapid CT imaging for TBI evaluation and emphasize early neurosurgical consultation. Ongoing research is focused on minimizing radiation exposure in vulnerable populations, such as pregnant women, while ensuring accurate diagnosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993048",
    "fields": {
      "question_number": "220",
      "question_text": "Global aphasia after one month (? asking about prognosis)",
      "options": {
        "A": "(Broca\u2019s aphasia) is incorrect because it represents a less severe, non",
        "B": "(Global aphasia) is correct, reflecting the patient\u2019s persistent and extensive language deficits. Option C (Anomia) is incorrect as it refers only to word",
        "D": "(Wernicke\u2019s aphasia) is incorrect because it does not match the global nature of the deficits observed."
      },
      "correct_answer": "b",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Aphasia is a language disorder caused by damage to specific regions of the brain. Global aphasia involves severe impairment in both expressive and receptive language functions. Persistence of global aphasia after one month indicates extensive cortical damage, generally implying a poorer prognosis.",
        "pathophysiology": "Global aphasia results from large lesions that affect essential language centers, typically involving both Broca\u2019s (expressive) and Wernicke\u2019s (receptive) areas, often due to a large middle cerebral artery (MCA) infarct. The extensive damage disrupts communication networks in the brain, leading to profound language deficits.",
        "clinical_correlation": "A patient with persistent global aphasia at one month post-stroke is unlikely to have transitioned to a less severe form such as Broca\u2019s or Wernicke\u2019s aphasia. This sustained deficit reflects a large area of infarction with limited potential for rapid recovery.",
        "diagnostic_approach": "Evaluation includes detailed language assessments performed by a speech-language pathologist and correlating neuroimaging studies (CT/MRI) to determine the extent of cortical damage. Differential diagnoses in aphasia include Broca\u2019s aphasia (non-fluent, relatively preserved comprehension), Wernicke\u2019s aphasia (fluent but with impaired comprehension), and anomic aphasia (word-finding difficulties with milder deficits).",
        "classification_and_neurology": "Aphasia classification traditionally follows the Boston Diagnostic Aphasia Examination framework, dividing aphasia into fluent and non-fluent types based on speech output, comprehension, repetition, and naming abilities. Global aphasia is classified as a non-fluent aphasia subtype with severe deficits in all language modalities. It belongs to the cerebrovascular aphasia subtype family caused by ischemic or hemorrhagic stroke affecting the MCA territory. Other systems, such as the Western Aphasia Battery, similarly categorize aphasias based on linguistic profiles. Over time, classification has evolved to incorporate neuroimaging and lesion localization, with some controversies regarding overlapping features and mixed aphasias. Current consensus emphasizes a multidimensional approach integrating clinical, neuroanatomical, and functional data for precise nosology.",
        "classification_and_nosology": "Aphasias are categorized based on fluency and the affected language domains. Global aphasia is the most severe form, involving deficits in both production and comprehension, and is usually indicative of widespread damage in the left hemisphere.",
        "management_principles": "The mainstay of management for aphasia is intensive, early speech and language therapy. While prognosis in global aphasia is guarded, early rehabilitation, multidisciplinary care, and patient-specific interventions can optimize functional recovery. For pregnant and lactating patients, non-invasive treatments such as speech therapy are safe and remain the standard of care.",
        "option_analysis": "Option A (Broca\u2019s aphasia) is incorrect because it represents a less severe, non-fluent aphasia with relatively preserved comprehension. Option B (Global aphasia) is correct, reflecting the patient\u2019s persistent and extensive language deficits. Option C (Anomia) is incorrect as it refers only to word-finding difficulties, and Option D (Wernicke\u2019s aphasia) is incorrect because it does not match the global nature of the deficits observed.",
        "clinical_pearls": "1. Persistent global aphasia after one month typically indicates a large infarct with a poorer prognosis. 2. Early, aggressive speech and language therapy is crucial, though recovery may be limited. 3. Detailed language assessments help to monitor recovery and tailor rehabilitative efforts.",
        "current_evidence": "Recent research emphasizes the role of neuroplasticity and early intervention in post-stroke aphasia. Although recovery in global aphasia remains challenging, emerging therapies and advanced neurorehabilitation techniques continue to evolve, with ongoing studies investigating adjuvant therapies to improve outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993049",
    "fields": {
      "question_number": "221",
      "question_text": "Small PFO & AF in young female who developed stroke, ttt",
      "options": {
        "A": "(Closure): Incorrect because closing a small PFO does not address the embolic risk from AF. Option b (Warfarin): While anticoagulation is indicated in many AF cases, warfarin is not preferred given the availability of DOACs and may be overtreatment in a low AF burden scenario. Option c (ASA): Correct in this context where the clinical scenario implies low AF burden or diagnostic uncertainty, making antiplatelet therapy a conservative and appropriate choice."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This question concerns the management of stroke in a young female with a small patent foramen ovale (PFO) and atrial fibrillation (AF). The key concept is discerning the stroke source. In patients with cryptogenic stroke and a small PFO, closure is typically reserved when no other embolic source exists. However, when AF is present\u2014even if paroxysmal or of low burden\u2014it can be considered a source of cardioembolism. In selected cases, especially when the AF burden isn\u2019t definitively high or when its role is ambiguous, a conservative approach with antiplatelet therapy may be chosen.",
        "pathophysiology": "A small PFO permits the possibility of paradoxical embolism, but its risk is generally lower compared to a significant shunt. In atrial fibrillation, stasis in the left atrium promotes thrombus formation that may embolize to the brain. When both conditions coexist, the underlying pathophysiological concern is determining which source is dominant. Current evidence suggests that in patients with low-risk AF or uncertainty about stroke mechanism, aggressive anticoagulation may not provide additional benefit compared to antiplatelet therapy, particularly if the PFO is small.",
        "clinical_correlation": "Clinically, a young stroke patient might present with focal neurologic deficits and workup may reveal a small PFO on echocardiography and episodes of paroxysmal AF on prolonged monitoring. The decision for treatment is influenced by the frequency and burden of AF as well as the anatomical significance of the PFO. The clinical challenge lies in attributing the stroke to either a paradoxical embolism via PFO or an embolism from AF.",
        "diagnostic_approach": "Evaluation includes brain imaging (MRI/CT) to confirm infarction, transthoracic or transesophageal echocardiography to assess for PFO, and cardiac monitoring (e.g., Holter) for detecting paroxysmal AF. Differential diagnoses include other causes of cryptogenic stroke such as hypercoagulable states, arterial dissection, and vasculitis. Differentiation relies on combining imaging studies with clinical risk factor assessments.",
        "classification_and_neurology": "Ischemic stroke in young adults is classified under cerebrovascular diseases, with subtypes including cardioembolic stroke, large artery atherosclerosis, small vessel disease, and stroke of other determined or undetermined etiology. The TOAST classification is commonly used to categorize ischemic strokes based on etiology. PFO-related strokes fall under 'stroke of undetermined etiology' or 'paradoxical embolism' if a venous source is identified. AF is classified as a major cardioembolic source. The coexistence of PFO and AF complicates classification, requiring careful etiological attribution. Recent consensus emphasizes comprehensive evaluation to distinguish between PFO-related paradoxical embolism and AF-related cardioembolism, as management differs substantially. The classification has evolved with increased recognition of PFO as a risk factor in cryptogenic stroke and the advent of prolonged cardiac monitoring improving AF detection.",
        "classification_and_nosology": "This scenario falls under the cryptogenic stroke category (sometimes classified as embolic stroke of undetermined source, ESUS) when no clear source is identified. The presence of a small PFO and AF blur the typical categorization, necessitating a tailored approach based on the relative risk of each source.",
        "management_principles": "Latest guidelines recommend antiplatelet therapy (aspirin) for secondary prevention in patients with low-risk or uncertain sources where the burden of AF is minimal. First-line treatment is usually aspirin, particularly in younger patients or those in whom the risk\u2013benefit profile for full anticoagulation is unclear. In contrast, patients with definite, sustained AF typically require anticoagulation with direct oral anticoagulants (DOACs), which are preferred over warfarin for their predictable effect and safety profile. In pregnancy and lactation, low-dose aspirin is generally considered safe, although the decision must account for individual patient risk factors and breastfeeding status.",
        "option_analysis": "Option a (Closure): Incorrect because closing a small PFO does not address the embolic risk from AF. Option b (Warfarin): While anticoagulation is indicated in many AF cases, warfarin is not preferred given the availability of DOACs and may be overtreatment in a low AF burden scenario. Option c (ASA): Correct in this context where the clinical scenario implies low AF burden or diagnostic uncertainty, making antiplatelet therapy a conservative and appropriate choice.",
        "clinical_pearls": "1. In patients with cryptogenic stroke, discerning the stroke source (PFO vs. AF) is essential to guide management. 2. PFO closure is generally reserved for patients without another clear embolic source. 3. Low-dose aspirin is relatively safe in young patients and during pregnancy/lactation when full anticoagulation is not clearly indicated.",
        "current_evidence": "Recent studies and guidelines continue to stress the need for individualized therapy in stroke management. The data support the use of DOACs in definitive AF cases, whereas in cryptogenic stroke with a small PFO and minimal AF burden, aspirin remains a viable first-line option. Ongoing research is further refining criteria to differentiate stroke sources."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993050",
    "fields": {
      "question_number": "222",
      "question_text": "Lobar hemorrhage with high INR, ttt:",
      "options": {
        "A": "(PCC): Correct",
        "B": "(FFP): Incorrect",
        "C": "(Vitamin K alone): Incorrect",
        "D": "(Protamine): Incorrect"
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This question deals with the acute management of warfarin-associated intracerebral hemorrhage (ICH) in a patient with a lobar hemorrhage and an elevated International Normalized Ratio (INR). The primary goal is rapid reversal of the coagulopathy to prevent hematoma expansion and further neurological injury.",
        "pathophysiology": "Warfarin interferes with the synthesis of vitamin K\u2013dependent clotting factors (II, VII, IX, and X). In the setting of an intracranial hemorrhage, the lack of these factors prolongs bleeding. Prothrombin complex concentrates (PCC) provide concentrated clotting factors, rapidly normalizing the INR and thereby limiting further bleeding.",
        "clinical_correlation": "Patients on warfarin presenting with lobar hemorrhage require urgent correction of their coagulopathy. A high INR correlates with an increased risk of bleeding expansion. Timely reversal can mitigate hematoma growth and improve clinical outcomes.",
        "diagnostic_approach": "Initial workup includes a non-contrast head CT confirming hemorrhage, laboratory testing to determine INR and coagulation status, and a careful review of the medication history. Differential diagnoses include hemorrhagic transformation of an ischemic stroke and other coagulopathies.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified by location (lobar, deep, cerebellar, brainstem) and etiology (hypertensive, amyloid angiopathy, anticoagulation-related, vascular malformations). Anticoagulant-related ICH falls under secondary hemorrhages due to coagulopathy. The classification system most relevant here is the hemorrhagic stroke classification within cerebrovascular diseases, as per the American Heart Association/American Stroke Association (AHA/ASA) guidelines.  This hemorrhage is specifically a lobar ICH with anticoagulation-associated coagulopathy. The nosology distinguishes primary spontaneous ICH from secondary causes like anticoagulant use. Understanding this classification aids in tailoring management strategies and prognostication.  Controversies exist regarding the best method for anticoagulation reversal, but consensus favors rapid correction of coagulopathy to limit hematoma expansion in anticoagulant-associated ICH.",
        "classification_and_nosology": "This scenario is categorized as drug-induced coagulopathy leading to acute intracerebral hemorrhage. It is managed under the umbrella of anticoagulant-related bleeding emergencies.",
        "management_principles": "Current guidelines recommend using PCC as first-line therapy because of its rapid action in reversing warfarin-induced coagulopathy. Vitamin K should be administered concurrently to achieve sustained reversal, although its onset is delayed (6\u201324 hours). Fresh frozen plasma (FFP) is a secondary option if PCC is unavailable due to its slower action and larger volume requirements. Protamine sulfate is reserved for the reversal of heparin and has no effect on warfarin reversal. In pregnancy and lactation, rapid reversal remains critical; PCC along with vitamin K is used despite warfarin\u2019s contraindication in pregnancy, as the acute situation mandates reversal of coagulopathy.",
        "option_analysis": "Option a (PCC): Correct \u2013 Provides rapid reversal of warfarin\u2019s effects by delivering clotting factors. Option b (FFP): Incorrect \u2013 Although it provides clotting factors, its slower action and higher volume load make it less desirable in an acute setting. Option c (Vitamin K alone): Incorrect \u2013 While necessary for sustained reversal, its delayed onset precludes its use as the sole agent in acute hemorrhage management. Option d (Protamine): Incorrect \u2013 Protamine reverses heparin, not warfarin.",
        "clinical_pearls": "1. PCC is the fastest means to reverse warfarin-induced coagulopathy in acute ICH. 2. Always use vitamin K alongside PCC for prolonged reversal. 3. Distinguish between warfarin reversal agents and those used for heparin.",
        "current_evidence": "Recent guidelines from the American Heart Association emphasize that PCC is preferred over FFP for reversing warfarin-associated ICH due to its rapid efficacy and lower complication profile. Studies have reinforced its use in improving clinical outcomes by rapidly restoring coagulation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993051",
    "fields": {
      "question_number": "223",
      "question_text": "Severe MCA stenosis in elderly with stroke, ttt",
      "options": {
        "A": "(ASA): Correct",
        "B": "(Angio & stenting): Incorrect",
        "C": "(ASA & Warfarin): Incorrect"
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This question focuses on the management of severe middle cerebral artery (MCA) stenosis in an elderly patient with stroke. The central principle is that medical management, primarily with antiplatelet therapy, is the mainstay of treatment for intracranial atherosclerotic disease.",
        "pathophysiology": "Severe MCA stenosis is usually the result of atherosclerotic plaque buildup, which may lead to turbulent flow and a propensity for thrombosis. This mechanism increases the risk of ischemic stroke by limiting cerebral perfusion and facilitating embolism from unstable plaques.",
        "clinical_correlation": "Patients typically present with symptoms of ischemic stroke such as hemiparesis, aphasia, or sensory deficits. Imaging (CT/MRI angiography) identifies the degree of stenosis. Recognizing the underlying pathology directs the treatment toward limiting further ischemic events while managing vascular risk factors.",
        "diagnostic_approach": "The diagnostic workup involves brain imaging to document the stroke and vascular studies (MRA, CTA, or catheter angiography) to assess the severity of intracranial stenosis. Differential diagnoses include embolic stroke from cardiac sources and small vessel lacunar infarcts. Risk factor evaluation (hypertension, diabetes, hyperlipidemia) is essential.",
        "classification_and_neurology": "MCA stenosis is classified under large artery atherosclerosis in the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification of ischemic stroke subtypes. It falls within the broader category of intracranial atherosclerotic disease (ICAD). The degree of stenosis is often graded by percentage luminal narrowing using imaging criteria: mild (<50%), moderate (50-69%), and severe (\u226570%). This classification informs prognosis and treatment strategies. Alternative classification schemes include the WASID (Warfarin-Aspirin Symptomatic Intracranial Disease) criteria, which have been pivotal in guiding clinical trials. The consensus favors aggressive medical management for symptomatic severe ICAD, although endovascular approaches are evolving.",
        "classification_and_nosology": "This condition is classified under intracranial atherosclerotic disease (ICAS) and is a well-recognized cause of ischemic stroke in the elderly. It is managed medically unless specific criteria for intervention are met.",
        "management_principles": "First-line management is aggressive medical therapy, which includes antiplatelet agents (aspirin as the cornerstone), risk factor modification (blood pressure, lipid control), and lifestyle changes. Second-line therapies (such as angioplasty and stenting) are generally reserved for patients who fail optimal medical therapy and are approached with caution due to periprocedural risks. In pregnancy and lactation, aspirin (in low-dose form) is typically considered safe for stroke prevention, whereas invasive procedures are usually deferred unless absolutely necessary.",
        "option_analysis": "Option a (ASA): Correct \u2013 Aspirin is the recommended first-line antiplatelet therapy supported by evidence from trials like SAMMPRIS and WASID. Option b (Angio & stenting): Incorrect \u2013 Invasive procedures carry a high risk and are not first-line due to increased periprocedural complications. Option c (ASA & Warfarin): Incorrect \u2013 Combining anticoagulation with antiplatelet therapy has not been shown to be superior to antiplatelet monotherapy and increases the risk of hemorrhage.",
        "clinical_pearls": "1. Aspirin remains the cornerstone in the management of intracranial atherosclerotic disease. 2. Invasive procedures should be reserved for refractory cases, given the high associated risks. 3. Optimal management includes aggressive control of vascular risk factors.",
        "current_evidence": "Recent clinical trials such as SAMMPRIS and WASID reinforce that aggressive medical management, particularly with antiplatelet therapy, is superior to invasive interventions in patients with severe MCA stenosis. Current guidelines continue to endorse aspirin as the primary antiplatelet agent in this setting."
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
