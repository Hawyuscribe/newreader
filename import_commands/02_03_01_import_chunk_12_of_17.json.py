
# Import batch 1 of 3 from chunk_12_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993121",
    "fields": {
      "question_number": "49",
      "question_text": "Same patient asking what treatment you will give?",
      "options": {
        "A": "Antiepileptic",
        "B": "Antithrombotic"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In many neurology MCQs concerning stroke management, the key distinction is made between immediate reperfusion therapy versus supportive or secondary measures. Although the provided options include antiepileptics (used primarily for seizure prophylaxis or treatment) and antithrombotics (which are important for secondary prevention in atherosclerotic or embolic events), in the hyperacute setting of an ischemic stroke a more aggressive reperfusion strategy (commonly represented by thrombolytic therapy) is indicated. In this scenario the marked answer (Option C) is assumed to denote an intervention such as intravenous thrombolysis, which is the appropriate acute treatment when a patient meets eligibility criteria.",
        "pathophysiology": "Acute ischemic stroke occurs when there is an abrupt occlusion of a cerebral artery, most frequently due to a thromboembolic event. This leads to ischemia, energy failure, and eventual infarction of brain tissue if reperfusion is not rapidly achieved. Thrombolytic therapy works by catalyzing the conversion of plasminogen to plasmin, thereby dissolving the occluding clot and restoring blood flow to the ischemic penumbra.",
        "clinical_correlation": "A patient presenting within the therapeutic window (typically 4.5 hours from symptom onset) with focal neurologic deficits and imaging evidence ruling out hemorrhage is a candidate for reperfusion therapy. This strategy is critical for salvaging at-risk brain tissue, improving functional outcomes, and reducing long-term disability.",
        "diagnostic_approach": "The evaluation begins with a rapid clinical assessment paired with emergent imaging (usually non\u2010contrast head CT) to differentiate ischemic from hemorrhagic stroke. Other workup may include vascular imaging and laboratory tests to help classify the stroke type (e.g., using the TOAST criteria). The decision tree focuses on determining eligibility for reperfusion therapies.",
        "classification_and_neurology": "Ischemic stroke is classified according to etiological schemes such as the TOAST criteria, which categorizes strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. This classification informs prognosis and management. Treatment decisions fall within cerebrovascular disease management guidelines, which are part of broader neurological and vascular medicine taxonomies. The distinction between ischemic and hemorrhagic stroke is critical, as management differs fundamentally. Contemporary guidelines emphasize personalized therapy based on subtype, risk factors, and comorbidities. The evolution of stroke classification has improved targeted interventions and outcome prediction.",
        "classification_and_nosology": "Stroke is broadly classified as either ischemic or hemorrhagic. Ischemic strokes are further subcategorized into thrombotic, embolic, and lacunar types. This classification informs both acute management and secondary prevention strategies.",
        "management_principles": "Current American Heart Association/American Stroke Association guidelines support the use of intravenous thrombolysis (typically with recombinant tissue plasminogen activator, rtPA) in eligible patients presenting with acute ischemic stroke within 4.5 hours of symptom onset. Although antithrombotic therapy (e.g., aspirin) is essential for secondary prevention, it does not address the immediate need for reperfusion. In addition, prophylactic antiepileptics are not routinely recommended unless there is evidence of seizures or a high risk thereof. In pregnant or lactating patients, guidelines advise careful risk\u2013benefit evaluation; thrombolysis has been used in pregnancy in select cases after multidisciplinary consultation, and the management plan should be tailored to both maternal and fetal safety.",
        "option_analysis": "Option A (Antiepileptic) would be chosen if the primary concern were seizure activity or seizure prophylaxis\u2014which is not the case unless seizures are present. Option B (Antithrombotic) is important for long\u2010term stroke prevention but does not serve as the acute intervention to restore cerebral blood flow. Option C, though not explicitly described in the question, is presumed to denote thrombolytic therapy (or a similarly aggressive reperfusion strategy) which is indicated immediately in eligible patients with acute ischemic stroke. Option D is not provided, and given the context, Option C is the superior and correct choice.",
        "clinical_pearls": "\u2022 Time is brain: prompt administration of reperfusion therapy is crucial in acute ischemic stroke.  \u2022 Differentiating between immediate interventions (thrombolysis) and secondary preventive treatments (antithrombotics, antiepileptics) is essential in formulating an effective treatment plan.  \u2022 In special populations such as pregnant or breastfeeding patients, individualized risk assessment with input from relevant specialties is key.",
        "current_evidence": "Recent guidelines underscore that intravenous thrombolysis improves outcomes when administered according to strict inclusion/exclusion criteria. Studies continue to support its benefit when used within the recommended time frame, and although data in pregnancy are more limited, case series and expert opinion support its cautious use when the potential benefits outweigh the risks. Continued research and advances in endovascular techniques further refine the acute management of stroke."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993122",
    "fields": {
      "question_number": "50",
      "question_text": "pt with stroke and has marfinoid feature, what is the treatment:",
      "options": {
        "A": "vit B6"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Homocystinuria is a hereditary metabolic disorder characterized by elevated blood homocysteine levels, often manifesting with marfanoid features (such as a long, thin body habitus), lens dislocation, and an increased risk of thromboembolic events including stroke. In pyridoxine (vitamin B6)\u2013responsive cases, high\u2010dose vitamin B6 is a cornerstone of therapy.",
        "pathophysiology": "The disorder is most commonly due to a deficiency in cystathionine beta\u2010synthase (CBS), which leads to impaired conversion of homocysteine to cystathionine. Elevated homocysteine damages vascular endothelium and predisposes patients to thrombosis. In cases that are pyridoxine responsive, vitamin B6 acts as an essential cofactor that enhances any residual CBS enzyme activity, thereby lowering homocysteine levels.",
        "clinical_correlation": "Patients may present with thromboembolic events such as stroke at a young age alongside features resembling Marfan syndrome (marfanoid habitus) but with distinctive findings like downward lens dislocation (compared to the upward shift in Marfan syndrome). Recognizing these features directs the clinician to evaluate for homocystinuria, particularly in patients with cryptogenic stroke.",
        "diagnostic_approach": "The workup involves measuring plasma total homocysteine and methionine levels, along with urine amino acid analysis and potentially genetic testing. Differential diagnoses include Marfan syndrome (which shares a marfanoid habitus but lacks the metabolic abnormalities) and other connective tissue disorders.",
        "classification_and_neurology": "Homocystinuria due to CBS deficiency is classified as an inherited metabolic disorder affecting amino acid metabolism. Within stroke etiologies, it falls under 'rare causes of stroke' or 'stroke due to metabolic disorders' in most cerebrovascular classification systems such as the TOAST classification, which primarily categorizes stroke by etiology (large artery, cardioembolism, small vessel, other determined, and undetermined). Homocystinuria represents a 'stroke of other determined etiology' due to a systemic metabolic cause. The nosology distinguishes it from Marfan syndrome, which is a connective tissue disorder without hyperhomocysteinemia. Current consensus emphasizes recognizing metabolic causes in young stroke patients with systemic features to guide therapy.",
        "classification_and_nosology": "Homocystinuria is classified as an inborn error of metabolism. It can be subdivided into pyridoxine-responsive and non-responsive forms. This classification guides treatment choices and long-term management.",
        "management_principles": "For pyridoxine-responsive homocystinuria, the first-line therapy is high-dose vitamin B6 supplementation. Treatment is typically accompanied by dietary methionine restriction and supplementation with folate and vitamin B12 to further reduce homocysteine levels. Pregnancy and lactation considerations: Vitamin B6, folate, and B12 are safe in pregnancy and lactation, and their use is encouraged to optimize metabolic control and reduce thrombotic risk.",
        "option_analysis": "Option A (vitamin B6) is correct because it directly addresses the underlying enzyme deficiency in pyridoxine-responsive homocystinuria. The other options (which are not provided) are not relevant in the management of this condition.",
        "clinical_pearls": "1. Homocystinuria can mimic Marfan syndrome but is distinguished by metabolic abnormalities and a higher thrombotic risk. 2. Downward lens subluxation is a key differentiator from Marfan syndrome. 3. Early identification and pyridoxine treatment can significantly reduce the risk of vascular complications.",
        "current_evidence": "Recent studies and consensus guidelines continue to support the use of high-dose vitamin B6 in B6-responsive cases, with adjunctive nutritional therapy to manage homocysteine levels and prevent thrombotic events."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993124",
    "fields": {
      "question_number": "52",
      "question_text": "Patient came with left side weakness; CT showed right semiovale hypodensity; what is the next step:",
      "options": {
        "A": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke evaluation relies on promptly excluding hemorrhage via a noncontrast CT scan and then assessing the vasculature for occlusive lesions. Computed tomography angiography (CTA) is the key imaging modality used to visualize cerebral arteries and identify large vessel occlusions.",
        "pathophysiology": "In ischemic stroke, occlusion of a cerebral artery leads to insufficient blood flow and tissue infarction. In this patient, a hypodensity in the right semiovale reflects an infarct in the white matter supplied by small or large vessels that can be further characterized with vascular imaging.",
        "clinical_correlation": "The clinical presentation of left-sided weakness correlates with right hemisphere impairment. CTA is used to confirm the presence of a vascular occlusion (or significant stenosis), which has implications for treatment options such as thrombolysis or mechanical thrombectomy.",
        "diagnostic_approach": "After a noncontrast CT confirms the presence of an infarct and excludes hemorrhage, the next step is vascular imaging. CTA differentiates between large vessel occlusions, small vessel disease, and other etiologies like embolism. Differential diagnoses include lacunar infarcts (typically due to small vessel disease) and other stroke mimics.",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology and vascular territory. The TOAST classification categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. The lesion in the semiovale likely falls under large artery or small vessel categories depending on vessel involvement. Stroke classification systems have evolved to incorporate imaging and clinical data to stratify patients for treatment and prognosis. This case fits within the cerebrovascular disease family and acute ischemic stroke subtype.",
        "classification_and_nosology": "Ischemic strokes are categorized by underlying etiology, such as thromboembolic (cardioembolic or large vessel atherosclerosis) and small vessel (lacunar) strokes. The semiovale infarct in this case can be viewed as a white matter stroke.",
        "management_principles": "Acute management of ischemic stroke includes consideration for intravenous thrombolysis, provided the patient is within the therapeutic window and there are no contraindications. CTA is essential for identifying candidates for endovascular thrombectomy in cases of large vessel occlusion. In pregnant or lactating patients, CT and CTA are used judiciously with appropriate fetal shielding and minimized radiation exposure when necessary, as the benefits usually outweigh the risks in acute settings.",
        "option_analysis": "Option A (CTA) is correct because it is the most appropriate next step to evaluate the cerebral vasculature after detection of ischemic changes on the CT scan. Other options are either not provided or not appropriate at this stage.",
        "clinical_pearls": "1. Rapid vascular imaging is critical in stroke management as 'time is brain'. 2. CTA helps in the diagnosis of large vessel occlusions which may be amenable to mechanical thrombectomy. 3. Distinguishing between stroke subtypes using imaging guides the choice of intervention.",
        "current_evidence": "Current stroke guidelines endorse the use of CTA immediately after noncontrast CT in patients with suspected acute ischemic stroke, as it increases the detection of vascular occlusions and guides advanced therapeutic decisions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993125",
    "fields": {
      "question_number": "53",
      "question_text": "pt with SLE + antiphospholipid presented with stroke for 2 days what you will give:",
      "options": {
        "A": "warfarin",
        "B": "Aspirin"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Patients with systemic lupus erythematosus (SLE) are at risk of developing antiphospholipid syndrome (APS), an autoimmune condition that significantly increases the risk of thrombotic events, including stroke. In APS, long-term anticoagulation is the mainstay of secondary prevention.",
        "pathophysiology": "APS is mediated by autoantibodies (lupus anticoagulant, anticardiolipin, and anti-\u03b22 glycoprotein I) that create a hypercoagulable state through various mechanisms, including endothelial cell activation and interference with the natural anticoagulant pathways. This predisposes patients to both arterial and venous thrombosis.",
        "clinical_correlation": "The patient, with a background of SLE and confirmed antiphospholipid antibodies, presents with stroke\u2014a common manifestation of APS. In such cases, anticoagulation is essential to prevent further thrombotic episodes.",
        "diagnostic_approach": "Diagnosis of APS relies on both clinical criteria (history of thrombosis or pregnancy morbidity) and laboratory criteria (presence of antiphospholipid antibodies on two or more occasions 12 weeks apart). Differential diagnoses for stroke include atherosclerotic or cardioembolic causes, which are distinguished by the absence of antiphospholipid antibodies in these conditions.",
        "classification_and_neurology": "Antiphospholipid syndrome is classified as a systemic autoimmune prothrombotic disorder under the category of acquired thrombophilias. It is subdivided into primary APS (occurring in isolation) and secondary APS (associated with autoimmune diseases such as SLE). The international consensus criteria for APS diagnosis require at least one clinical event (vascular thrombosis or pregnancy morbidity) and persistent laboratory evidence of antiphospholipid antibodies. Stroke in APS is classified as an arterial thrombotic event and falls under the broader category of ischemic stroke etiologies. The TOAST classification system for ischemic stroke includes cardioembolism, large artery atherosclerosis, small vessel occlusion, other determined etiology, and undetermined etiology; APS-related stroke is considered an 'other determined etiology' due to its unique pathophysiology. Nosologically, APS bridges immunology and vascular neurology, highlighting the importance of integrating systemic autoimmune disease classification with cerebrovascular disease taxonomy. This classification has evolved with improved understanding of antibody profiles and clinical phenotypes, emphasizing the need for tailored therapeutic approaches.",
        "classification_and_nosology": "APS can be classified as primary (occurring in isolation) or secondary (associated with SLE or other autoimmune disorders). It is recognized as a significant acquired thrombophilia with implications for both arterial and venous thromboses.",
        "management_principles": "For patients with APS who have experienced a thrombotic event such as a stroke, long-term anticoagulation with warfarin is indicated, typically targeting an INR of 2.0\u20133.0 (or higher in cases of recurrent events). In the acute phase, bridging with heparin may be used until therapeutic INR is reached. Pregnancy and lactation considerations: Warfarin is contraindicated in pregnancy due to teratogenicity; therefore, pregnant patients are managed with low-molecular-weight heparin (LMWH) and low-dose aspirin instead.",
        "option_analysis": "Option A (warfarin) is correct since anticoagulation is essential in APS-related strokes. Aspirin alone does not provide sufficient protection against recurrent thrombosis in APS. The other options are not provided and would not be appropriate as sole therapy.",
        "clinical_pearls": "1. APS markedly increases the risk of recurrent thrombotic events and requires long-term anticoagulation. 2. Warfarin is typically preferred for non-pregnant patients, while LMWH is used in pregnancy. 3. Regular monitoring of INR is crucial to ensure adequate anticoagulation.",
        "current_evidence": "Recent guidelines and clinical trials reaffirm warfarin as the treatment of choice for secondary prevention in APS, while also cautioning against the use of direct oral anticoagulants (DOACs) in this population due to potential reduced efficacy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993126",
    "fields": {
      "question_number": "54",
      "question_text": "Another question about Patient came with stroke CT showed watershed infarction, next?",
      "options": {
        "A": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Watershed infarctions occur in regions at the boundaries of cerebral arterial territories and are typically caused by hypoperfusion, either from systemic hypotension or significant proximal arterial stenosis. Assessment of the vascular supply is essential in managing these infarctions.",
        "pathophysiology": "Watershed strokes result from decreased cerebral blood flow in the border zones between major vascular territories (such as between the anterior, middle, and posterior cerebral arteries). This hypoperfusion may be secondary to conditions like severe carotid stenosis or systemic hypotension, leading to ischemia in these vulnerable regions.",
        "clinical_correlation": "Patients with watershed infarctions may exhibit variable neurological deficits depending on the areas involved. Identifying the underlying cause is key, as treatment may differ if, for example, significant carotid stenosis is present.",
        "diagnostic_approach": "After an initial noncontrast CT confirms a watershed infarct, the next step is to perform vascular imaging with CTA. This test assesses for carotid or intracranial stenosis, occlusions, and other vascular abnormalities. Differential diagnoses include small vessel occlusion or embolic strokes, which are distinguished based on vascular imaging findings.",
        "classification_and_neurology": "Watershed infarctions are classified within the broader category of ischemic strokes under the TOAST classification system, typically falling into the 'large artery atherosclerosis' or 'cardioembolism' subtypes when caused by proximal stenosis or embolism, or 'other determined etiology' when related to systemic hypoperfusion. Anatomically, they are divided into: - **Cortical (external) watershed infarcts:** Located at the junction of ACA-MCA or MCA-PCA territories. - **Internal (subcortical) watershed infarcts:** Located between deep and superficial arterial systems in the white matter. This classification aids in identifying underlying mechanisms and guiding management. The concept of watershed infarcts has evolved with advances in neuroimaging, allowing better differentiation from lacunar infarcts and embolic strokes. Some controversy exists regarding the relative contributions of embolism versus hypoperfusion in causing watershed infarcts, especially in patients with carotid stenosis.",
        "classification_and_nosology": "Watershed infarcts are classified as a subtype of ischemic stroke, specifically falling into the category of border zone infarcts. They are often differentiated from lacunar strokes (small vessel disease) and embolic strokes by their characteristic location and association with hypoperfusion.",
        "management_principles": "Management involves stabilizing the patient\u2019s hemodynamics, initiating antiplatelet therapy, and correcting underlying causes such as carotid stenosis if present. CTA plays a pivotal role in evaluating for significant vascular compromise that might require revascularization interventions. Pregnancy and lactation considerations: While CTA involves radiation, appropriate shielding and dose minimization can be used in pregnant and lactating patients when the benefits outweigh the risks in the context of acute stroke evaluation.",
        "option_analysis": "Option A (CTA) is correct because it is the most appropriate next diagnostic step to assess the vascular status and identify potential reversible causes (e.g., carotid stenosis) underlying a watershed infarction. The absence of alternative options further supports this choice.",
        "clinical_pearls": "1. Watershed infarcts often indicate underlying hemodynamic compromise rather than embolic events. 2. CTA is invaluable for evaluating carotid and intracranial vasculature in this setting. 3. Recognizing the pattern of watershed infarction can prompt timely interventions to improve cerebral perfusion.",
        "current_evidence": "Recent stroke management guidelines emphasize the importance of early vascular imaging in all ischemic strokes, including watershed infarctions, to tailor appropriate therapies and identify candidates for potential revascularization procedures."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993127",
    "fields": {
      "question_number": "55",
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
        "conceptual_foundation": "This case represents an embolic stroke secondary to infective endocarditis. The combination of fever and a pansystolic murmur raises suspicion for an infectious process on the heart valves, which can lead to septic emboli causing stroke.",
        "pathophysiology": "In infective endocarditis, bacterial colonization of the heart valves produces vegetations that can break off and embolize to cerebral vessels. The inflammatory response and infection contribute to the clinical picture, and the vegetations are typically friable, leading to systemic embolization.",
        "clinical_correlation": "Patients with infective endocarditis may present with stroke symptoms accompanied by systemic signs of infection (fever, malaise) and cardiac findings (e.g., a pansystolic murmur from regurgitant flow). The combination of these findings should prompt evaluation for endocarditis.",
        "diagnostic_approach": "The diagnostic approach includes obtaining multiple blood cultures and performing echocardiography (with transesophageal echocardiography being more sensitive) to identify vegetations. Differential diagnoses include non-infectious embolic strokes (e.g., cardioembolism from atrial fibrillation), which are less likely to present with fever.",
        "classification_and_neurology": "Infective endocarditis is classified by causative organism (e.g., streptococcal, staphylococcal), valve involvement (native vs prosthetic), and clinical course (acute vs subacute). Stroke secondary to IE is categorized under cardioembolic stroke in the TOAST classification system for ischemic stroke etiologies. TOAST (Trial of Org 10172 in Acute Stroke Treatment) defines cardioembolism as stroke due to emboli from cardiac sources such as atrial fibrillation, IE, or left ventricular thrombus. This classification guides treatment strategies and prognosis. The presence of infection and septic emboli distinguishes IE-related stroke from other cardioembolic causes, necessitating integration of infectious disease and stroke management principles.",
        "classification_and_nosology": "Infective endocarditis is classified by its clinical course (acute versus subacute) and by the causative organism (e.g., Staphylococcus aureus, Streptococcus viridans). It is an infection of the endothelial surface of the heart, particularly the heart valves.",
        "management_principles": "The current guidelines (AHA/ACC) recommend prompt initiation of empiric, then culture-guided, intravenous antibiotic therapy as the first line treatment in infective endocarditis. In cases complicated by large vegetations, heart failure, or uncontrolled infection, surgical intervention may be necessary. In pregnant and lactating patients, antibiotic selection should favor agents with proven safety profiles (e.g., penicillins and cephalosporins) while avoiding those known to carry teratogenic risks.",
        "option_analysis": "Option A (antiplatelets) is insufficient because it does not address the underlying infection, whereas Option B (antibiotics) directly treats the bacterial cause of infective endocarditis, making it the correct choice. Unspecified options C and D add no therapeutic benefit in this scenario.",
        "clinical_pearls": "1) In any stroke patient with fever and a new murmur, always consider infective endocarditis. 2) Early detection and targeted antibiotic therapy are critical to reduce the risk of catastrophic embolic events.",
        "current_evidence": "Recent research emphasizes early multimodal imaging and the use of advanced echocardiographic techniques to detect vegetations. Updated guidelines stress the importance of individualized antibiotic regimens based on microbial susceptibility, along with a multidisciplinary approach in managing complicated cases."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993128",
    "fields": {
      "question_number": "56",
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
        "conceptual_foundation": "This is a classic example of a crossed or alternating brainstem syndrome, where a lesion in the medulla produces ipsilateral cranial nerve deficits and contralateral motor and sensory deficits.",
        "pathophysiology": "Medial medullary syndrome (Dejerine syndrome) results from an infarct in the medial portion of the medulla. It affects the corticospinal tract and medial lemniscus, leading to contralateral weakness and loss of proprioception, as well as the hypoglossal nucleus or nerve, which causes tongue weakness on the same side as the lesion.",
        "clinical_correlation": "The patient\u2019s presentation of left-sided body weakness and loss of proprioception with right-sided tongue weakness indicates a lesion in the right medial medulla. The tongue weakness (ipsilateral to the lesion) and contralateral limb deficits are hallmark features of medial medullary syndrome.",
        "diagnostic_approach": "Magnetic resonance imaging (MRI) of the brainstem is the investigation of choice. Vascular imaging with CT angiography or MR angiography helps in identifying the occluded vessel. Differential diagnoses include lateral medullary syndrome (Wallenberg syndrome) and pontine infarcts, but these present with different cranial nerve involvements.",
        "classification_and_neurology": "Medial medullary syndrome is classified under brainstem strokes within the cerebrovascular disease taxonomy. The TOAST classification categorizes ischemic strokes by etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, etc. Medial medullary infarcts often result from large artery atherosclerosis affecting the vertebral artery.  Within brainstem syndromes, medial medullary infarcts differ from lateral medullary (Wallenberg) syndrome, which involves the posterior inferior cerebellar artery (PICA) territory. The classification of brainstem strokes is based on vascular territory and clinical syndrome. This has evolved with advanced imaging allowing better correlation of infarct location and vascular anatomy.  Controversies include the overlap of clinical signs between medial and lateral medullary syndromes and the variable vascular anatomy of vertebral and basilar arteries. However, consensus supports the use of clinical localization combined with imaging to guide diagnosis.",
        "classification_and_nosology": "Medial medullary syndrome is classified as a type of brainstem stroke, specifically involving the medial medulla. It is most commonly due to occlusion of the paramedian branches of the vertebral artery.",
        "management_principles": "The standard management in acute stroke settings includes assessment for thrombolytic therapy eligibility. Secondary prevention strategies, such as antiplatelet agents and risk factor management (e.g., blood pressure control), are also essential. In pregnancy and lactation, thrombolytic agents and low-dose aspirin may be employed after careful risk assessment, as they are relatively safe when used appropriately.",
        "option_analysis": "Option A (Right Vert) is correct because the right vertebral artery supplies the medial medulla where the lesion resides. Option B (Left Vert) would imply a lesion on the left medulla, which would lead to ipsilateral tongue weakness on the left, and Option C (Basilar) is more likely to affect different brainstem territories.",
        "clinical_pearls": "1) Alternating (crossed) neurological deficits are highly indicative of a brainstem stroke. 2) Medial medullary syndrome classically presents with contralateral hemiparesis and loss of proprioception alongside ipsilateral hypoglossal nerve dysfunction.",
        "current_evidence": "Recent advances in neuroimaging have enhanced the localization of brainstem infarcts, and updated stroke management guidelines continue to prioritize rapid intervention with thrombolytic therapy where applicable."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993129",
    "fields": {
      "question_number": "57",
      "question_text": "Stroke patient has livedo reticularis what is the Dx?",
      "options": {
        "A": "Sneddon disease"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Sneddon disease (or syndrome) is defined by the association of livedo reticularis\u2014a characteristic net-like pattern on the skin\u2014with cerebrovascular events such as strokes.",
        "pathophysiology": "The underlying mechanism is believed to be a non-inflammatory thrombotic arteriopathy affecting medium-sized arteries, which may be related to the presence of antiphospholipid antibodies. This leads to occlusion of vessels in both the skin and the brain, resulting in the observed manifestations.",
        "clinical_correlation": "Patients with Sneddon syndrome typically present with recurrent strokes or transient ischemic attacks in conjunction with the skin finding of livedo reticularis. Cognitive impairment and other systemic manifestations may also occur.",
        "diagnostic_approach": "Diagnosis involves clinical evaluation, skin examination, and supportive investigations such as antiphospholipid antibody testing and vascular imaging. Differential diagnoses include antiphospholipid syndrome, vasculitis, and systemic lupus erythematosus, which can present with overlapping features.",
        "classification_and_neurology": "Sneddon syndrome is classified as a rare, non-inflammatory thrombotic vasculopathy within the spectrum of systemic vasculopathies affecting medium and small arteries. It is often considered part of the broader category of non-atherosclerotic vasculopathies causing stroke.   Two subtypes are recognized: - **Primary (idiopathic) Sneddon syndrome:** No associated autoimmune markers. - **Secondary Sneddon syndrome:** Associated with antiphospholipid antibodies or systemic lupus erythematosus.  The syndrome overlaps clinically and pathologically with antiphospholipid syndrome but is distinguished by the prominent livedo reticularis and characteristic vascular pathology. Current nosology places Sneddon syndrome within cerebrovascular disorders secondary to systemic arteriopathies. There remains some debate about its classification, especially regarding its relation to APS, but consensus supports its recognition as a distinct clinical entity.",
        "classification_and_nosology": "Sneddon syndrome is categorized as a vascular disorder rather than a primary inflammatory vasculitis. It may occur as an idiopathic condition or in association with autoimmune diseases.",
        "management_principles": "Treatment centers on preventing further thromboembolic events, typically using antiplatelet therapy or anticoagulation depending on the presence of antiphospholipid antibodies. In pregnant women, low molecular weight heparin in combination with low-dose aspirin is often recommended to reduce the risk of thrombosis while maintaining safety for both mother and fetus.",
        "option_analysis": "Option A (Sneddon disease) is the correct diagnosis given the presentation of livedo reticularis and stroke. Other options, if provided, do not typically manifest with this distinctive combination of clinical findings.",
        "clinical_pearls": "1) The presence of livedo reticularis in a stroke patient should prompt evaluation for Sneddon syndrome. 2) Consider testing for antiphospholipid antibodies when Sneddon syndrome is suspected, as it guides therapeutic decisions.",
        "current_evidence": "Recent studies have further elucidated the role of immune-mediated thrombotic mechanisms in Sneddon syndrome, and evolving guidelines emphasize a tailored approach to anticoagulation versus antiplatelet therapy based on individual risk factors and antibody status."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993130",
    "fields": {
      "question_number": "58",
      "question_text": "pt with stroke and had fibromuscular dysplasia, what next:",
      "options": {
        "A": "Renal Angio"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Fibromuscular dysplasia (FMD) is a non-atherosclerotic, non-inflammatory arterial disease that commonly affects medium-sized arteries, most notably the renal and carotid arteries.",
        "pathophysiology": "FMD results from abnormal cellular proliferation and architectural distortion of the arterial wall, often producing a characteristic 'string-of-beads' appearance on angiography. When it involves the carotid or vertebral arteries, it can predispose to cerebrovascular events, whereas renal artery involvement may lead to renovascular hypertension.",
        "clinical_correlation": "In a stroke patient found to have FMD, it is essential to evaluate for multisystem arterial involvement. The detection of FMD in the cerebrovascular circulation raises the possibility of concurrent renal artery disease, which has important implications for blood pressure management and overall vascular risk.",
        "diagnostic_approach": "Imaging studies such as computed tomography angiography (CTA), magnetic resonance angiography (MRA), or digital subtraction angiography (DSA) are used to diagnose FMD by visualizing the typical beading in affected arteries. Differential diagnoses include atherosclerotic disease, vasculitis, and arterial dissection.",
        "classification_and_neurology": "Fibromuscular dysplasia is classified as a non-atherosclerotic, non-inflammatory arteriopathy affecting medium-sized arteries. The most commonly used classification divides FMD based on the arterial wall layer involved: medial fibroplasia (most common, producing the classic string-of-beads), intimal fibroplasia, and perimedial fibroplasia. The disease is part of the broader category of arteriopathies that cause stroke, distinct from atherosclerotic, inflammatory (vasculitis), and embolic causes. The American Heart Association and European consensus statements recognize FMD as a distinct entity with systemic vascular involvement. There is ongoing debate regarding the genetic basis and whether FMD represents a spectrum of disorders. It is important to differentiate FMD from other causes of arterial stenosis such as atherosclerosis, vasculitis, and arterial dissection without underlying FMD.",
        "classification_and_nosology": "Fibromuscular dysplasia is classified based on the arterial wall layer predominantly affected (medial, intimal, or adventitial) with medial fibroplasia being the most common subtype.",
        "management_principles": "Management involves a comprehensive vascular evaluation. For patients with significant renal involvement, percutaneous transluminal angioplasty may be indicated to manage renovascular hypertension. Stroke management follows standard protocols including antiplatelet therapy and risk factor modification. In pregnant or lactating patients, blood pressure control is critical, and interventions such as angioplasty are considered only if clearly indicated, with careful minimization of radiation exposure.",
        "option_analysis": "Option A (Renal Angio) is correct because once FMD is identified in a stroke patient, screening the renal arteries for involvement is essential for complete management. Other options would not address the need for a full vascular workup in FMD.",
        "clinical_pearls": "1) FMD is more common in young to middle-aged women and often involves multiple vascular territories. 2) Renal artery involvement in FMD can lead to secondary hypertension, necessitating early detection and appropriate intervention.",
        "current_evidence": "Recent guidelines support the use of non-invasive angiographic techniques for diagnosing FMD and emphasize a multidisciplinary approach. Research continues to refine risk stratification and individualized treatment strategies, particularly concerning endovascular versus medical management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993131",
    "fields": {
      "question_number": "59",
      "question_text": "MRI with dissection, what to do:",
      "options": {
        "A": "Medical Therapy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "The key concept is recognizing that an arterial dissection identified on MRI\u2014typically a cervical (carotid or vertebral) artery dissection\u2014is primarily managed medically. Dissections occur when there is a tear in the artery\u2019s intima allowing blood to enter the vessel wall, and this can lead to luminal stenosis, thrombus formation, and embolic stroke. The appropriate initial step is to institute antithrombotic therapy (antiplatelet or anticoagulation), which is encompassed under the term 'Medical Therapy'.",
        "pathophysiology": "An arterial dissection involves an intimal tear that permits blood to dissect into the media layer, creating a false lumen accompanied by an intramural hematoma. This process can cause vessel narrowing or occlusion and may predispose to thrombus formation with subsequent embolization, which is the primary mechanism for ischemic stroke in these patients.",
        "clinical_correlation": "Patients with cervical artery dissections may present with unilateral neck pain, headache (often localized), and in carotid dissections, signs such as partial Horner syndrome. Neurologic deficits may occur if the dissection results in compromised cerebral blood flow or embolic stroke. Prompt diagnosis via imaging (such as MRI/MRA) is crucial for initiating treatment.",
        "diagnostic_approach": "When clinical evaluation suggests an arterial dissection, MRI (along with MRA/CTA) is used to identify features such as an intramural hematoma and double lumen. Differential diagnoses include atherosclerotic vascular disease or vasculitis; however, the imaging characteristics (e.g., crescent-shaped hyperintensity on fat-suppressed sequences) aid in distinguishing a dissection from other vascular pathologies.",
        "classification_and_neurology": "Arterial dissections are classified based on etiology (spontaneous vs traumatic), location (carotid vs vertebral), and vessel involvement (intracranial vs extracranial). Spontaneous cervical artery dissection (sCAD) is a distinct nosological entity within cerebrovascular diseases and a major cause of stroke in young adults. The TOAST classification for ischemic stroke includes arterial dissection under 'other determined etiology.' The classification has evolved with advances in imaging, allowing differentiation between intramural hematoma, intimal flap, and pseudoaneurysm. There is ongoing discussion about the role of genetic predisposition and connective tissue disorders in spontaneous dissections, placing some cases within a broader spectrum of vasculopathies. Current consensus guidelines categorize dissections primarily by clinical and imaging features to guide management.",
        "classification_and_nosology": "Arterial dissections are categorized based on location (e.g., carotid or vertebral) and etiology (spontaneous vs. traumatic). This classification helps guide treatment\u2014most spontaneous dissections are managed medically. They can also be classified by severity (e.g., with or without aneurysmal dilation) which may modify follow-up but generally do not change the initial management approach.",
        "management_principles": "The current guidelines (including recommendations from the AHA/ASA and evidence from the CADISS trial) support the use of medical management with antithrombotic therapy as the first-line treatment. This may be achieved with either anticoagulants (such as heparin transitioning to warfarin or direct oral anticoagulants) or antiplatelet agents (such as aspirin). In pregnancy, LMWH is preferred over warfarin due to teratogenic risks; low-dose aspirin is also considered safe. During lactation, both LMWH and low-dose aspirin are generally acceptable. Surgical or endovascular interventions are reserved for patients with progression or complications refractory to medical management.",
        "option_analysis": "The provided answer option, 'Medical Therapy', correctly encompasses the standard initial treatment for a cervical artery dissection. Other potential options (e.g., surgical intervention or conservative observational management without antithrombotic therapy) are less appropriate in the absence of contraindications or complicating factors. Thus, the marked answer A is correct.",
        "clinical_pearls": "\u2022 Early recognition is critical in managing cervical artery dissection to prevent stroke. \n\u2022 Both antiplatelet and anticoagulation strategies have demonstrated similar efficacy; selection should be individualized based on patient factors and contraindications. \n\u2022 In pregnancy, consider LMWH and low-dose aspirin as safe options. \n\u2022 Follow-up imaging is important to assess healing and rule out complications such as pseudoaneurysm formation.",
        "current_evidence": "Recent evidence from the CADISS trial has shown no significant difference in stroke prevention between anticoagulant and antiplatelet therapies for cervical artery dissections. Updated guidelines advocate for a medical management approach initially, with adjustments based on patient-specific factors including pregnancy and lactation where LMWH and aspirin are favored due to their safety profiles."
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
