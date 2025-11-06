
# Import batch 3 of 3 from chunk_8_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993240",
    "fields": {
      "question_number": "13",
      "question_text": "Female patient came with ischemic stroke, history of previous 2 abortions, elevated prothrombin time. What is the most helpful investigation in her case?",
      "options": {
        "A": "Anti phospholipid syndrome",
        "B": "Prothrombin Gene Mutation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Antiphospholipid syndrome (APS) is an autoimmune thrombophilic disorder that manifests with both arterial and venous thromboses and recurrent pregnancy losses. It represents one of the key causes of ischemic stroke in young to middle-aged women, especially when accompanied by a history of miscarriages.",
        "pathophysiology": "APS is characterized by the presence of antiphospholipid antibodies (such as anticardiolipin antibodies, lupus anticoagulant, and anti-\u03b22 glycoprotein I) which lead to a hypercoagulable state. These antibodies disrupt normal coagulation processes, paradoxically prolonging clotting times in laboratory assays while predisposing patients to thrombosis. This explains the association with both elevated clotting times and thrombotic events.",
        "clinical_correlation": "A female patient with an ischemic stroke, a history of recurrent miscarriages, and abnormal coagulation tests is highly suggestive of APS. The clinical picture differentiates APS from other thrombophilias, such as prothrombin gene mutation, which does not commonly present with recurrent abortions.",
        "diagnostic_approach": "The diagnostic workup for APS involves laboratory testing for lupus anticoagulant, anticardiolipin antibodies, and anti-\u03b22 glycoprotein I. For a definitive diagnosis, these tests need to be positive on two separate occasions at least 12 weeks apart. Differential diagnoses include other inherited thrombophilias (such as factor V Leiden or prothrombin gene mutation), but the obstetric history specifically points toward APS.",
        "classification_and_neurology": "Antiphospholipid syndrome is classified as an acquired autoimmune thrombophilia and is part of the broader group of systemic autoimmune diseases. It can be categorized as: - **Primary APS**: occurring in isolation without other autoimmune diseases. - **Secondary APS**: associated with systemic lupus erythematosus or other autoimmune disorders.  The classification criteria for APS (Sydney criteria, 2006) require at least one clinical event (vascular thrombosis or pregnancy morbidity) and laboratory confirmation of antiphospholipid antibodies on two occasions 12 weeks apart.   Prothrombin gene mutation is classified as an inherited thrombophilia, specifically a genetic risk factor for venous thromboembolism. It belongs to a family of inherited coagulation disorders including Factor V Leiden mutation and deficiencies of antithrombin, protein C, and protein S.   The classification of stroke etiologies incorporates these hypercoagulable states under 'stroke of other determined etiology' in systems such as the TOAST classification. The evolving understanding of thrombophilias has refined stroke workup protocols, especially in young stroke patients.",
        "classification_and_nosology": "APS is classified as either primary (occurring in isolation) or secondary (associated with systemic lupus erythematosus or other autoimmune diseases). It is defined by the revised Sapporo criteria which combine clinical events and laboratory findings.",
        "management_principles": "In patients diagnosed with APS, long-term anticoagulation (typically with warfarin aiming for an INR of 2.0-3.0) is recommended for secondary stroke prevention. During pregnancy, warfarin is contraindicated due to teratogenic effects; instead, a regimen of low molecular weight heparin and low-dose aspirin is used. These management strategies are supported even in lactating patients, with special considerations given to the safety profiles of the medications.",
        "option_analysis": "Option A (Anti phospholipid syndrome testing) is correct because it directly addresses the suspected diagnosis given the patient\u2019s history of recurrent abortions and ischemic stroke. Option B (Prothrombin Gene Mutation) is less appropriate for this clinical picture, as this mutation is not typically associated with recurrent pregnancy losses.",
        "clinical_pearls": "1. APS should be considered in any young woman with thrombotic events and a history of miscarriages. 2. Laboratory testing for APS requires confirmation on two occasions to fulfill diagnostic criteria.",
        "current_evidence": "Recent guidelines stress the importance of early APS detection through standardized antibody testing, and they advocate for aggressive, individualized anticoagulation management to reduce the risk of recurrent thrombotic events."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993241",
    "fields": {
      "question_number": "14",
      "question_text": "A 30-year-old healthy women presented with 10 days history of severe headache, blurred vision and new onset symptomatic seizure. Neurological examination was unremarkable. Vitaly stable.\n\nCT brain done (image attached).\n\nWhich of the following is the best diagnostic test?",
      "options": {
        "A": "MRI brain",
        "B": "CT angiogram.",
        "C": "CT venogram",
        "D": "Lumbar puncture"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "This question concerns a young woman with a subacute presentation of headache, blurred vision, and new\u2010onset seizure \u2013 a constellation that should raise suspicion for cerebral venous sinus thrombosis (CVT). The core concept is that CVT often presents with signs of raised intracranial pressure and seizures in a young patient (often women, sometimes with risk factors like OCP use or pregnancy), and the imaging choice should best visualize the venous system.",
        "pathophysiology": "CVT occurs when a thrombus occludes one or more of the cerebral venous sinuses. This results in impaired venous drainage, increased intracranial pressure, and potentially venous infarction or hemorrhagic conversion. The disruption of venous flow leads to leakage, edema, and sometimes localized seizures. Up\u2010to\u2010date research emphasizes early detection as prompt anticoagulation can minimize permanent damage.",
        "clinical_correlation": "The patient\u2019s headache, blurred vision (often a sign of papilledema secondary to raised ICP), and seizure are typical clinical manifestations of CVT. Despite a normal neurological exam, the subacute nature of symptoms in a young woman without classic risk factors for arterial stroke shifts concern to a venous process.",
        "diagnostic_approach": "Common differentials include subarachnoid hemorrhage, idiopathic intracranial hypertension, and even demyelinating lesions. However, CVT should be differentiated by using imaging modalities that visualize the venous sinuses. Although MRI brain (sometimes with MR venography) is highly sensitive, in acute settings CT venography is both rapid and effective. CT angiogram focuses on arteries and lumbar puncture can be contraindicated in patients with increased intracranial pressure.",
        "classification_and_neurology": "CVST is classified within cerebrovascular diseases as a venous stroke subtype, distinct from arterial ischemic stroke. The International Classification of Diseases (ICD-11) and the American Stroke Association recognize CVST as a unique entity under venous thromboembolism affecting the central nervous system. Classification can be further refined by location (e.g., superior sagittal sinus thrombosis, transverse sinus thrombosis) and etiology (e.g., idiopathic, infection-associated, prothrombotic states). The condition belongs to the broader category of cerebrovascular disorders but differs mechanistically and therapeutically from arterial strokes. Advances in neuroimaging have refined diagnostic criteria and classification, emphasizing the importance of venous imaging modalities. Some controversy remains regarding optimal diagnostic algorithms and the role of emerging imaging techniques, but consensus guidelines emphasize the importance of venous sinus imaging for definitive diagnosis.",
        "classification_and_nosology": "CVT is categorized as a form of stroke caused by thrombosis of the cerebral venous system. It is classified based on which sinus is involved (e.g., superior sagittal sinus, transverse sinus) and may be further sub\u2010categorized by underlying risk factors (e.g., prothrombotic states, pregnancy, OCP use).",
        "management_principles": "Immediate management involves anticoagulation (typically with low molecular weight heparin), even in the presence of small hemorrhagic infarcts. According to current guidelines, supportive measures to reduce intracranial pressure and seizure control are also important. In pregnant or lactating patients, unfractionated heparin or LMWH remains the treatment of choice as they do not cross the placenta and are compatible with breastfeeding.",
        "option_analysis": "Option A (MRI brain) is useful but may not adequately evaluate the venous system without specialized sequences (i.e., MR venography). Option B (CT angiogram) focuses on arterial rather than venous circulation. Option D (Lumbar puncture) can be dangerous in suspected increased ICP and does not diagnose CVT. Option C (CT venogram) is the best study to visualize the cerebral venous sinuses in an acute setting.",
        "clinical_pearls": "1. CVT should be suspected in young women with headaches, seizures, and visual changes even if the neurological exam is unremarkable. 2. CT venogram is a rapid, sensitive imaging modality for assessing the cerebral venous sinuses. 3. Early anticoagulation is critical even in the presence of hemorrhagic lesions.",
        "current_evidence": "Recent studies and guidelines continue to support the use of CT venography as a first\u2010line diagnostic tool in suspected CVT. There is also an emphasis on early diagnosis and treatment with heparin anticoagulation, with adaptations made for special populations like pregnant and lactating women."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993242",
    "fields": {
      "question_number": "15",
      "question_text": "Patient presented with acute limb weakness and dysarthria. CT brain done and was normal. He was within the window and IV t-PA started. 20 minutes later the primary nurse called the physician as the patient has abnormal swelling around the mouth (imaged attached). Blood pressure was normal.\n\nWhich of the following is the most likely associated risk factor for this condition?",
      "options": {
        "A": "Frontal lobe stroke",
        "B": "ACE inhibitor"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses a known adverse effect of intravenous thrombolysis (t-PA) used for acute ischemic stroke \u2013 specifically, orolingual angioedema. The core concept is recognizing that t-PA can trigger angioedema, especially in patients taking ACE inhibitors.",
        "pathophysiology": "t-PA facilitates the conversion of plasminogen to plasmin, which can lead to the activation of the kallikrein-kinin system and subsequent release of bradykinin. Bradykinin accumulation increases vascular permeability. In patients on ACE inhibitors, the degradation of bradykinin is reduced, further enhancing the risk of angioedema.",
        "clinical_correlation": "The appearance of abnormal swelling around the mouth 20 minutes after initiation of IV t-PA in a patient with normal blood pressure is characteristic of orolingual angioedema. This reaction is often localized to the lips, tongue, or oropharyngeal tissues and can progress to airway compromise if not recognized and managed promptly.",
        "diagnostic_approach": "The diagnosis is clinical; one differentiates this condition from other allergic reactions by its rapid onset following t-PA administration and its predilection for the orolingual region. The history of ACE inhibitor use is a critical associated risk factor distinguishing it from other causes of allergic or angioedematous reactions.",
        "classification_and_neurology": "Angioedema secondary to t-PA is classified as a drug-induced, bradykinin-mediated angioedema within the broader family of hypersensitivity reactions. It differs mechanistically from histamine-mediated allergic angioedema and from hereditary angioedema caused by C1 esterase inhibitor deficiency. Within stroke management complications, it is a recognized but uncommon adverse effect of thrombolytic therapy. The classification of stroke-related complications includes hemorrhagic transformation, reperfusion injury, and allergic or inflammatory reactions such as angioedema. Current stroke guidelines categorize t-PA associated angioedema as a rare but potentially life-threatening adverse event requiring immediate attention.",
        "classification_and_nosology": "This reaction is classified as a drug-induced angioedema, specifically iatrogenic and associated with thrombolytic therapy. It falls under the category of adverse drug reactions mediated by bradykinin rather than histamine.",
        "management_principles": "Immediate management involves addressing airway concerns followed by pharmacologic therapy. Guidelines suggest administering antihistamines (e.g., diphenhydramine) and steroids, and if necessary, epinephrine. In patients with mild symptoms and stable airway, conservative management with antihistamines is indicated. It is also important to note that ACE inhibitors are contraindicated during pregnancy due to teratogenicity, and this adverse effect is an additional reason to avoid them in pregnant women.",
        "option_analysis": "Option A (Frontal lobe stroke) is unrelated to the development of angioedema. The marked answer, Option B (ACE inhibitor), is correct because the use of ACE inhibitors predisposes patients to t-PA induced orolingual angioedema by impairing bradykinin breakdown. Other unspecified options do not pertain to the risk factors for this reaction.",
        "clinical_pearls": "1. t-PA-associated angioedema typically occurs within an hour of administration. 2. Concomitant use of ACE inhibitors significantly increases the risk of developing this adverse reaction. 3. Recognizing this complication early is essential to prevent airway compromise.",
        "current_evidence": "Newer studies reinforce the association between ACE inhibitors and increased risk of orolingual angioedema with t-PA. Protocols now emphasize early identification and rapid management of this complication, especially in patients known to be taking ACE inhibitors."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993243",
    "fields": {
      "question_number": "16",
      "question_text": "Patient presented with acute limb weakness and dysarthria. CT brain done and was normal. He was within the window and IV t-PA started. 20 minutes later the primary nurse called the physician as the patient has abnormal swelling around the mouth (imaged attached). Blood pressure was normal.\n\nWhich of the following is the appropriate next step?",
      "options": {
        "A": "Stop t-PA",
        "B": "Diphenhydramine",
        "C": "Immediate intubation",
        "D": "CT brain"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "In this scenario, the patient receiving IV t-PA for acute ischemic stroke develops orolingual angioedema shortly thereafter. The key concept is recognizing the complication and instituting appropriate management without unnecessarily interrupting stroke treatment unless airway compromise is imminent.",
        "pathophysiology": "IV t-PA can trigger the release of bradykinin through the activation of the kallikrein-kinin pathway. Elevated bradykinin levels increase vascular permeability, leading to angioedema. This is particularly common in patients on ACE inhibitors, where bradykinin degradation is impaired.",
        "clinical_correlation": "The patient\u2019s development of swelling around the mouth\u2014an area highly susceptible to bradykinin effects\u2014despite normal blood pressure, points toward an angioedema reaction rather than a hypertensive bleed or other complication. The clinical picture is consistent with a localized, non-life-threatening adverse reaction that, if not progressing to airway compromise, can be managed medically.",
        "diagnostic_approach": "The diagnosis is clinical, based on the temporal relationship with t-PA infusion and examination of the orofacial region. Differential diagnoses include anaphylaxis from other agents; however, the presence of orolingual swelling without hypotension or diffuse skin involvement supports a localized reaction.",
        "classification_and_neurology": "t-PA induced angioedema falls under the category of drug-induced angioedema, specifically bradykinin-mediated angioedema. Angioedema broadly classifies into histamine-mediated (allergic) and bradykinin-mediated types. The latter includes hereditary angioedema, ACEI-induced angioedema, and t-PA induced angioedema. This entity is recognized in stroke management guidelines as a rare but important adverse effect of thrombolytic therapy. It is distinct from systemic hypersensitivity reactions and classified under adverse drug reactions in the cerebrovascular treatment framework. Current nosology emphasizes the mechanistic distinction to guide management, as antihistamines and corticosteroids are often ineffective in bradykinin-mediated forms, though diphenhydramine is still used as adjunctive therapy.",
        "classification_and_nosology": "This adverse event is categorized as t-PA induced orolingual angioedema \u2013 a bradykinin-mediated drug reaction distinct from classic histamine-mediated allergic reactions.",
        "management_principles": "The first step in management for patients with mild to moderate orolingual angioedema is to administer antihistamines such as diphenhydramine. Corticosteroids may also be used. Airway monitoring is essential, and while discontinuing t-PA may be considered in severe cases or if the airway is compromised, mild reactions can often be managed without stopping thrombolytic therapy. In cases of progression to airway compromise, immediate airway protection measures, including intubation, should be instituted. In pregnant or lactating women, diphenhydramine remains the first-line agent as it is considered relatively safe.",
        "option_analysis": "Option A (Stop t-PA) might be considered if the angioedema were severe or causing airway compromise; however, in a stable patient with localized swelling, stopping t-PA is not immediately necessary. Option C (Immediate intubation) is reserved for patients with overt airway compromise. Option D (CT brain) is not indicated in this scenario. The marked answer, Option B (Diphenhydramine), is correct as it targets the allergic reaction and is the appropriate immediate management step for mild to moderate symptoms.",
        "clinical_pearls": "1. Orolingual angioedema following t-PA does not automatically warrant cessation of thrombolytic therapy if the airway remains secure. 2. Early intervention with antihistamines can arrest the progression of swelling. 3. Always monitor the airway closely, as angioedema can progress rapidly.",
        "current_evidence": "Recent guidelines advocate for rapid assessment of airway compromise in t-PA-induced angioedema and recommend medical management with antihistamines and steroids before considering more invasive measures. Studies support that early intervention with agents like diphenhydramine can be effective in controlling mild reactions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993229",
    "fields": {
      "question_number": "2",
      "question_text": "Patient presented to the ER with vertigo and vomiting, What is the feature that can differentiate peripheral from central cause of vertigo?",
      "options": {
        "A": "Severe nausea and vomiting",
        "B": "Reproducible vertigo"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "The question differentiates the etiologies of vertigo by asking which feature helps distinguish a peripheral from a central cause. The core concept is that peripheral vertigo, often stemming from inner ear disorders such as benign paroxysmal positional vertigo (BPPV) or vestibular neuritis, tends to be elicited by specific head movements or positions.",
        "pathophysiology": "Peripheral vertigo arises from pathology in the vestibular apparatus of the inner ear. In conditions like BPPV, displaced otoliths trigger vertigo when the head is moved into certain positions. Conversely, central vertigo is due to lesions in the brainstem or cerebellum (often vascular or demyelinating), where symptoms are less typically tied to positional changes.",
        "clinical_correlation": "Patients with peripheral vertigo often experience episodic vertigo that is reproducible with positional maneuvers (e.g., Dix-Hallpike test), and may also have associated tinnitus or hearing loss. In contrast, central vertigo may present with additional neurological signs (e.g., diplopia, dysarthria) and is less reliably elicited by maneuvers.",
        "diagnostic_approach": "When evaluating vertigo, differential diagnoses include peripheral causes such as BPPV, M\u00e9ni\u00e8re\u2019s disease, and vestibular neuritis, versus central causes such as cerebellar infarction, multiple sclerosis, or brainstem tumors. A detailed history and physical exam (including the head impulse test, positional testing, and evaluation for neurological deficits) help differentiate these conditions.",
        "classification_and_neurology": "Vertigo is classified broadly into peripheral and central types based on lesion location. The International Classification of Vestibular Disorders (ICVD) provides a framework to categorize vestibular syndromes. Peripheral vestibular disorders include BPPV, vestibular neuritis, M\u00e9ni\u00e8re\u2019s disease, and labyrinthitis. Central vestibular disorders encompass brainstem or cerebellar infarctions, demyelinating diseases, tumors, and migraine-associated vertigo. This classification aids in diagnostic approach and management. The distinction is critical as peripheral vertigo generally has a benign course and favorable prognosis, whereas central vertigo may indicate life-threatening pathology requiring urgent intervention. Some overlap exists, and mixed presentations can occur, but reproducibility of vertigo on positional testing remains a cornerstone in classification.",
        "classification_and_nosology": "Vertigo is broadly classified as either peripheral (originating in the vestibular apparatus) or central (originating from central nervous system lesions). This classification guides both diagnostic evaluation and management.",
        "management_principles": "Management of peripheral vertigo involves maneuvers such as the Epley or Semont maneuvers for BPPV, vestibular rehabilitation for other vestibular disorders, and symptomatic control with vestibular suppressants. In central vertigo, management is directed at the underlying cause (e.g., stroke management protocols). In pregnant or lactating patients, nonpharmacologic measures and repositioning maneuvers are preferred due to medication safety profiles.",
        "option_analysis": "Option A (Severe nausea and vomiting) can occur in both peripheral and central vertigo and is not sufficiently discriminatory. The marked answer, Option B (Reproducible vertigo), is correct because in peripheral causes, vertigo can typically be reproduced with specific maneuvers (e.g., Dix-Hallpike), whereas central vertigo is less likely to be triggered reliably by positional changes. The other options were not provided, but among the choices given, reproducibility points toward a peripheral origin.",
        "clinical_pearls": "1. In peripheral vertigo, symptoms are often positional and can be reproduced with maneuvers, whereas central vertigo may present with additional focal neurological deficits. 2. The presence of auditory symptoms (tinnitus, hearing loss) alongside vertigo supports a peripheral cause. 3. A normal head impulse test favors a central etiology.",
        "current_evidence": "Recent research reinforces that reproducible vertigo with positional changes is a hallmark of peripheral vestibular disorders. Moreover, guideline updates stress the importance of a focused neurological exam (including the HINTS exam) to rule out central causes, especially when the clinical picture is ambiguous."
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
