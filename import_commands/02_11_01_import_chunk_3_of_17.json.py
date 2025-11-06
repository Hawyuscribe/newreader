
# Import batch 1 of 3 from chunk_3_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993027",
    "fields": {
      "question_number": "120",
      "question_text": "Patient with history of mild head trauma pic showing (left Horner\u2019s and tongue deviation to the left) what is the involved artery",
      "options": {
        "A": "Internal carotid",
        "B": "Vertebral artery",
        "C": "PICA",
        "D": "Basilar"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the recognition of signs indicative of cervical arterial dissection following mild head trauma. The combination of Horner\u2019s syndrome and tongue deviation strongly implicates involvement of structures near the internal carotid artery.",
        "pathophysiology": "A dissection of the internal carotid artery can occur after even minor trauma, resulting in a tear in the arterial wall. This allows blood to dissect into the vessel wall, which may compromise the adjacent sympathetic plexus (producing Horner's syndrome) and affect the nearby hypoglossal nerve (resulting in ipsilateral tongue deviation).",
        "clinical_correlation": "Patients with internal carotid dissection often present with neck pain, headache, and signs of cranial nerve dysfunction. The presence of a unilateral Horner's syndrome (ptosis, miosis, anhidrosis) coupled with tongue deviation to the same side is almost pathognomonic for carotid dissection, making the recognition of these signs critical.",
        "diagnostic_approach": "Noninvasive imaging modalities such as CT angiography or MR angiography are used to diagnose carotid dissection. Differential diagnoses include vertebral artery dissection (which may not produce Horner\u2019s syndrome) and brainstem stroke (which would present with additional brainstem signs). Ultrasound is less sensitive for dissections in the high cervical region.",
        "classification_and_neurology": "This clinical scenario falls under the classification of brainstem strokes, specifically lateral medullary syndrome (Wallenberg syndrome), caused by ischemia in the vertebrobasilar arterial territory. The vertebral artery is a major branch of the subclavian artery, supplying the medulla, cerebellum, and posterior circulation. The nosology includes ischemic strokes classified by vascular territory (anterior vs posterior circulation), with brainstem strokes further subclassified by anatomical location (medulla, pons, midbrain). The lateral medullary infarct is a classic subtype of posterior circulation stroke. This classification aligns with the TOAST criteria for ischemic stroke etiologies and the vascular territory-based approach used in clinical neurology. Controversies exist regarding the overlap of symptoms in brainstem stroke syndromes and the variability of arterial supply due to anatomical variants.",
        "classification_and_nosology": "Carotid dissections are a subtype of cervical artery dissections classified under non-traumatic or spontaneous dissections when there is no clear mechanical trigger, though trauma is a common precipitating factor. They are an important cause of stroke in young and middle-aged adults.",
        "management_principles": "The standard management of internal carotid dissection involves antithrombotic therapy, which may be antiplatelet agents or anticoagulation, based on the individual patient\u2019s risk factors and contraindications. In pregnancy and lactation, low molecular weight heparin is preferred due to its safety profile.",
        "option_analysis": "Option A (Internal carotid) is correct because dissection in this artery accounts for the presence of ipsilateral Horner\u2019s syndrome and involvement of the hypoglossal nerve, which leads to tongue deviation. Option B (Vertebral artery) is less likely to cause these specific cranial nerve findings. Options C (PICA) and D (Basilar) are not associated with the described constellation of symptoms.",
        "clinical_pearls": "1. Horner's syndrome in a post-trauma setting should prompt evaluation for carotid dissection. 2. Tongue deviation toward the side of the lesion implicates lower cranial nerve involvement near the carotid artery. 3. Early vascular imaging is critical in patients with suspected dissection to prevent ischemic complications.",
        "current_evidence": "Recent studies emphasize the role of early MRI/MRA in diagnosing cervical artery dissections, with guidelines recommending prompt initiation of antithrombotic therapy to reduce the risk of stroke. In pregnant patients, the use of LMWH remains the mainstay due to its established safety profile over warfarin or DOACs."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993028",
    "fields": {
      "question_number": "121",
      "question_text": "Case of presentation typical to Fabry with pic of angiokeratoma and 2 strokes and",
      "options": {},
      "correct_answer": "Fabry",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This case describes a clinical presentation typical of Fabry disease, a multisystem X-linked lysosomal storage disorder. The hallmark cutaneous manifestation is angiokeratomas, which when combined with a history of strokes in a relatively young patient, strongly suggests Fabry disease.",
        "pathophysiology": "Fabry disease is caused by a deficiency in the enzyme alpha-galactosidase A, leading to the accumulation of globotriaosylceramide (Gb3) in various tissues including vascular endothelium, kidneys, heart, and the nervous system. This accumulation results in progressive organ damage, vascular dysfunction, and an increased risk of cerebrovascular events.",
        "clinical_correlation": "Patients with Fabry disease often present with angiokeratomas, acroparesthesias, and frequently experience strokes or transient ischemic attacks at a young age. Other features may include corneal verticillata, renal insufficiency, and cardiac issues. The combination of cutaneous findings and recurrent strokes is highly distinctive for Fabry disease.",
        "diagnostic_approach": "The diagnosis is typically confirmed by measuring alpha-galactosidase A enzyme activity in blood or leukocytes, followed by genetic testing. Differential diagnoses include Moyamoya disease (which has a characteristic angiographic pattern without skin lesions), CADASIL (a hereditary small vessel disease with white matter changes and no angiokeratomas), homocystinuria (which typically presents with lens dislocation and marfanoid habitus), and sickle cell disease (associated with hemolytic anemia).",
        "classification_and_neurology": "Fabry disease belongs to the family of lysosomal storage disorders (LSDs), specifically classified as a sphingolipidosis due to the accumulation of glycosphingolipids. It is an X-linked inherited metabolic disorder, with males typically more severely affected, though heterozygous females can also manifest symptoms due to X-inactivation. The disease is classified under genetic cerebrovascular disorders when considering its neurological complications, particularly stroke. Historically, LSDs were grouped by accumulated substrate, but current nosology integrates genetic, enzymatic, and clinical phenotypes. Fabry disease\u2019s classification as a cause of stroke has gained recognition in stroke genetics and metabolic stroke categories, emphasizing its importance in early-onset stroke differential diagnosis. Controversies include phenotypic variability and the role of variant forms with residual enzyme activity, which may present later or with milder symptoms, complicating classification and management decisions.",
        "classification_and_nosology": "Fabry disease is classified as a lysosomal storage disorder and is X-linked. It is typically divided into the classical type, which presents in childhood with systemic manifestations, and a later-onset variant with predominantly cardiac or renal involvement.",
        "management_principles": "Treatment of Fabry disease primarily involves enzyme replacement therapy (ERT) with agalsidase beta or agalsidase alfa, which helps reduce the accumulation of Gb3. Supportive therapies may include pain management and addressing organ-specific complications. In pregnant patients, the decision to continue ERT is made on a case-by-case basis after weighing potential risks and benefits, though many experts favor continuation if maternal benefit is significant. Lactating mothers should be counseled, and therapy adjusted as needed given the limited data.",
        "option_analysis": "The correct answer is Fabry disease. Hypothetical alternatives such as Moyamoya disease, CADASIL, and homocystinuria do not have the pathognomonic presence of angiokeratomas and have other distinguishing clinical features that do not match this case.",
        "clinical_pearls": "1. Angiokeratomas are a classic dermatologic hallmark of Fabry disease. 2. Early stroke in a young patient, when combined with multisystem involvement, should raise suspicion for a lysosomal storage disorder. 3. Enzyme replacement therapy is the cornerstone of management and may help prevent progression of organ damage.",
        "current_evidence": "Recent research supports early initiation of enzyme replacement therapy to delay the progression of Fabry-related complications. Updated guidelines emphasize periodic monitoring of cardiac, renal, and neurologic function. There is also ongoing research into alternative therapies, including oral chaperone molecules, which may complement or offer alternatives to ERT in the future."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993029",
    "fields": {
      "question_number": "122",
      "question_text": "Scenario showing an MRI (flare) with unilateral deep watershed infarction what is the diagnosis",
      "options": {
        "A": "ICA stenosis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Watershed infarcts occur in border zones between major cerebral arterial territories. In this case, a unilateral deep watershed infarction seen on an MRI flare image indicates a region particularly vulnerable to hypoperfusion. Typically, when such an infarct is unilateral, it points to a focal hemodynamic compromise rather than a global hypotensive event.",
        "pathophysiology": "In patients with significant internal carotid artery (ICA) stenosis, the distal perfusion pressure drops enough to compromise blood flow in the terminal distributions (the watershed zones). The reduced flow fails to fully oxygenate tissues in these territories, leading to ischemic injury. The 'flare' signal on MRI corresponds to the acute/subacute phase of ischemia in these deep white matter areas.",
        "clinical_correlation": "Patients with unilateral watershed infarctions usually exhibit milder, sometimes fluctuating, neurological deficits attributable to the compromised blood supply on one side. Associated clinical findings, such as the presence of a carotid bruit and vascular risk factors (e.g., hypertension, atherosclerosis), further support the diagnosis of ICA stenosis as the underlying cause.",
        "diagnostic_approach": "Initial evaluation with neuroimaging, like MRI and CT, identifies the location and pattern of ischemia. Carotid Doppler ultrasonography, CT angiography or MR angiography can help assess the degree of ICA stenosis. Differential diagnoses include global hypoperfusion states, embolic events from other sources, or small vessel disease, which can be differentiated based on clinical history and imaging characteristics.",
        "classification_and_neurology": "Watershed infarctions are classified based on location: cortical (external) watershed infarcts occur at the junctions between cortical territories of major cerebral arteries, while deep (internal) watershed infarcts occur in the white matter between deep penetrating arteries. The TOAST classification system for ischemic stroke etiologies includes large artery atherosclerosis, which encompasses ICA stenosis as a cause of hemodynamic infarcts. Watershed infarcts due to ICA stenosis fall under large artery atherosclerosis with hemodynamic compromise. Over time, classification systems have evolved to emphasize the mechanism (hemodynamic vs embolic) and location of infarcts to better tailor treatment. Some controversy exists in distinguishing pure hemodynamic infarcts from embolic watershed strokes; however, unilateral deep watershed infarcts ipsilateral to ICA stenosis strongly suggest hemodynamic etiology.",
        "classification_and_nosology": "Watershed infarctions are categorized under border zone strokes. They are further divided into cortical (between territories of MCA/ACA or MCA/PCA) and deep (internal border zone between deep and superficial perforators) infarcts. ICA stenosis is a well\u2010recognized cause of such infarcts.",
        "management_principles": "For patients with ICA stenosis leading to watershed infarction, first-line management includes antiplatelet therapy (aspirin, possibly combined with clopidogrel in select cases), high-intensity statin therapy, and aggressive risk factor modification (hypertension, diabetes, smoking cessation). If the stenosis is high-grade and symptomatic, revascularization options like carotid endarterectomy or carotid stenting are considered. In pregnancy or lactation, risk factor management employs agents with established safety profiles (e.g., low-dose aspirin) and decisions regarding surgical intervention are highly individualized after multidisciplinary consultation.",
        "option_analysis": "Option A (ICA stenosis) is correct because unilateral deep watershed infarction is typically due to a focal reduction in blood flow from ipsilateral carotid stenosis. Other options are not provided, but none would better explain the unilateral deep border zone pattern seen on MRI.",
        "clinical_pearls": "1. Unilateral watershed infarcts are a strong clue for ipsilateral carotid disease. 2. Always evaluate for carotid stenosis in patients with focal ischemic strokes in border zones. 3. Early revascularization in selected patients can prevent recurrent events.",
        "current_evidence": "Recent studies emphasize the importance of identifying carotid stenosis in patients with border zone infarcts. Guidelines support aggressive medical management with antithrombotic therapy and risk factor modification, and in selected cases, carotid revascularization has been shown to reduce stroke recurrence rates."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993030",
    "fields": {
      "question_number": "123",
      "question_text": "Patient with hemorrhagic stroke what bp target",
      "options": {
        "A": "160/100",
        "B": "140/90"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "In hemorrhagic stroke, the primary goal is to prevent hematoma expansion and secondary brain injury by tightly controlling blood pressure. The optimal blood pressure target is essential to balance the risk of rebleeding against the need to preserve adequate cerebral perfusion.",
        "pathophysiology": "Elevated BP raises the transmural pressure across cerebral vessels, which can worsen bleeding and expand the hemorrhage. By reducing blood pressure, the stress on vessel walls diminishes, potentially limiting the expansion of the hemorrhage and reducing subsequent edema and intracranial pressure.",
        "clinical_correlation": "Patients with intracerebral hemorrhage (ICH) often present with sudden-onset headaches, vomiting, altered mental status, and focal neurologic deficits. Aggressive BP management has been shown to limit hematoma growth in this subgroup.",
        "diagnostic_approach": "Initial noncontrast CT scan differentiates hemorrhagic from ischemic stroke. In the setting of ICH, BP measurement is critical. Differential diagnosis includes ischemic stroke with hemorrhagic transformation and subarachnoid hemorrhage, but imaging readily distinguishes these entities.",
        "classification_and_neurology": "Intracerebral hemorrhage belongs to the broader category of hemorrhagic stroke, distinct from ischemic stroke by pathogenesis and management. Hemorrhagic strokes are classified by location (lobar, deep, brainstem, cerebellar) and etiology (hypertensive arteriopathy, cerebral amyloid angiopathy, vascular malformations, coagulopathy). The classification systems used include the SMASH-U criteria for ICH etiology and the NIH Stroke Scale for severity assessment. Blood pressure management guidelines are incorporated within stroke management protocols from organizations such as the American Heart Association/American Stroke Association (AHA/ASA). Over time, consensus has shifted from permissive hypertension toward controlled lowering based on trial evidence, reflecting evolving understanding of the balance between perfusion and hemorrhage control.",
        "classification_and_nosology": "Hemorrhagic strokes are primarily classified as intracerebral hemorrhage (ICH) or subarachnoid hemorrhage (SAH). The management and prognosis vary significantly between these types, with ICH being directly linked to hypertension-related vessel rupture.",
        "management_principles": "Current AHA/ASA guidelines recommend lowering the systolic blood pressure to around 140 mm Hg in patients presenting with ICH if the initial systolic BP is between 150 and 220 mm Hg. First-line agents include intravenous short-acting antihypertensives such as nicardipine or labetalol. In pregnant or lactating patients, labetalol is often preferred due to its safety profile, and nicardipine may also be considered with appropriate maternal-fetal monitoring.",
        "option_analysis": "Option A (160/100) represents a less aggressive BP target and does not align with the current evidence-based recommendations, making Option B (140/90) the correct target for BP management in hemorrhagic stroke.",
        "clinical_pearls": "1. Rapid BP reduction in ICH helps minimize hematoma expansion. 2. Intravenous nicardipine and labetalol are commonly used agents in acute stroke settings. 3. Always consider the safety profile of antihypertensive agents in pregnancy and lactation.",
        "current_evidence": "Interventional trials such as INTERACT2 have demonstrated that rapid BP lowering to a systolic target of 140 mm Hg is safe and may improve functional outcomes in patients with ICH, leading to its endorsement in current guidelines."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993031",
    "fields": {
      "question_number": "124",
      "question_text": "Patient with recent history of car accident has PCA infarction",
      "options": {
        "A": "Artery to artery",
        "B": "Cryptogenic",
        "C": "Cardioembolic",
        "D": "Hypoperfusion"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Posterior cerebral artery (PCA) infarctions can result from various stroke mechanisms. In the setting of trauma, such as a car accident, vascular injury\u2014particularly cervical artery dissection\u2014is a well-documented cause. This dissection can lead to artery-to-artery embolism causing infarction in the PCA territory.",
        "pathophysiology": "Blunt trauma from a car accident can injure the cervical arteries (especially the vertebral arteries), leading to dissection. The tear in the vessel wall creates an intramural hematoma that can either cause local luminal narrowing or serve as a source for thrombus formation. Embolic fragments from this thrombus can then travel distally to occlude branches such as the PCA.",
        "clinical_correlation": "Clinically, a PCA infarction may present with visual field deficits, such as homonymous hemianopia, along with other signs that reflect the affected posterior circulation territory. In patients with a recent history of trauma, a cervical artery dissection must be actively considered.",
        "diagnostic_approach": "A high index of suspicion should prompt vascular imaging (e.g., CT angiography or MR angiography of the neck) to evaluate for dissection. Differential diagnoses include cardioembolic stroke (common in atrial fibrillation), cryptogenic stroke, or hypoperfusion states\u2014all of which are less likely in the context of a trauma history.",
        "classification_and_neurology": "Ischemic stroke etiologies are classified according to the TOAST criteria into five major categories: (1) large artery atherosclerosis (artery-to-artery embolism), (2) cardioembolism, (3) small vessel occlusion (lacunar), (4) stroke of other determined etiology, and (5) stroke of undetermined etiology (cryptogenic). Cardioembolic strokes account for approximately 20-30% of ischemic strokes and are characterized by emboli arising from cardiac sources. Artery-to-artery embolism is a subtype of large artery atherosclerosis. Hypoperfusion is not a primary TOAST category but is recognized as a mechanism in watershed infarcts. The classification system helps guide management and secondary prevention strategies. The evolving concept of embolic stroke of undetermined source (ESUS) reflects advances in diagnostics and highlights gaps in identifying embolic sources.",
        "classification_and_nosology": "Cervical artery dissections are classified as a subtype of stroke under the umbrella of 'arterial dissection.' Strokes related to dissection are considered a mechanism of 'artery-to-artery embolism,' which differentiates them from cardioembolic sources.",
        "management_principles": "Management of cervical artery dissection typically includes antithrombotic therapy\u2014either antiplatelets or anticoagulation\u2014as first-line treatment. The choice between them is patient-specific, with recent studies (such as the CADISS trial) showing similar outcomes. In pregnant or lactating patients, antiplatelet therapy (e.g., low-dose aspirin) or low molecular weight heparin (which has an excellent safety profile) can be used, avoiding warfarin due to teratogenic risks.",
        "option_analysis": "Option A (Artery to artery) is correct as it best describes the mechanism of stroke in a patient with recent trauma. The likely scenario is a cervical artery dissection leading to thrombus formation and subsequent embolization to the PCA territory. Options such as cardioembolic or cryptogenic are less supported by the history of a car accident, and hypoperfusion is not typical for an isolated PCA infarction.",
        "clinical_pearls": "1. Always consider cervical artery dissection as a cause of stroke in patients with a recent history of neck trauma. 2. Vertebral artery dissection is a common mechanism resulting in posterior circulation strokes. 3. Early vascular imaging is crucial to confirm the diagnosis.",
        "current_evidence": "Recent guidelines and studies, including those emerging from the CADISS trial, advocate for early diagnosis of cervical artery dissection and support antithrombotic management. Both antiplatelet and anticoagulation therapies have shown comparable efficacy in preventing stroke recurrence in this population."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993032",
    "fields": {
      "question_number": "125",
      "question_text": "Case of TGA (4 hours, confused, repeating questions, preserved identity, knows the family) Next step:",
      "options": {
        "A": "EEG",
        "B": "Brain CT & CTA",
        "C": "Lumbar puncture",
        "D": "???"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Transient Global Amnesia (TGA) is a benign, self-limited syndrome characterized by sudden onset of anterograde amnesia along with repetitive questioning, lasting up to 24 hours. Importantly, the patient\u2019s personal identity remains intact and there are no other focal neurological deficits.",
        "pathophysiology": "The exact cause of TGA remains unclear, though hypotheses include transient ischemia, migraine-related phenomena, or venous congestion. Despite various theories, TGA is recognized as a distinct clinical syndrome with excellent prognosis and no lasting neurological impairment.",
        "clinical_correlation": "Clinically, TGA presents with confusion and repetitive questioning for a few hours while preserving awareness of personal identity and recognition of familiar people. The hallmark is the abrupt loss of the ability to form new memories, with resolution typically within 24 hours.",
        "diagnostic_approach": "Diagnosis of TGA is primarily clinical. While neuroimaging (MRI, particularly with diffusion-weighted imaging) may be obtained in atypical cases to exclude alternative diagnoses such as stroke, seizure, or encephalitis, extensive workup (EEG, lumbar puncture) is generally unnecessary if the presentation is classic. Differential diagnoses include transient ischemic attack, complex partial seizures, and psychogenic amnesia, all of which are distinguished based on the detailed history, duration, and associated neurological signs.",
        "classification_and_neurology": "TGA is classified as a transient amnestic syndrome under the broader category of transient neurological disorders. According to the International Classification of Headache Disorders (ICHD-3) and neurological consensus, TGA is a distinct clinical entity separate from transient ischemic attacks and epileptic events. It is considered a benign, self-limited syndrome of unknown etiology but with suspected vascular and migrainous components. Nosologically, TGA belongs to the family of memory disorders and transient focal neurological syndromes. The classification has evolved from purely clinical descriptions to incorporating neuroimaging and electrophysiological data to differentiate it from mimics like TIA or transient epileptic amnesia. Current consensus emphasizes the importance of excluding acute cerebrovascular events given overlapping presentations, especially in older adults with vascular risk factors.",
        "classification_and_nosology": "TGA is classified as a transient amnestic syndrome and is distinct from other amnestic states such as transient ischemic attacks or epileptic events. It is also categorized as a self-limiting, non-recurring condition in the majority of cases.",
        "management_principles": "The mainstay of TGA management is reassurance and observation, as the condition is benign and resolves spontaneously. There is no need for acute aggressive intervention. However, if there is any atypical feature or if the history raises suspicion for other conditions, further evaluation (e.g., brain MRI) may be warranted. In pregnancy or lactation, the same approach applies since the condition is benign; unnecessary invasive testing is avoided to protect both the mother and the fetus.",
        "option_analysis": "Option D (which implies no further invasive workup and instead recommends reassurance/observation) is correct. Options A (EEG), B (Brain CT & CTA), and C (Lumbar puncture) are not routinely indicated in classic TGA because the syndrome is self-limited and additional testing may lead to unnecessary interventions and anxiety.",
        "clinical_pearls": "1. TGA is self-limiting and generally resolves within 24 hours with complete recovery of memory functions. 2. Routine neuroimaging or invasive testing is not necessary in classic presentations of TGA. 3. A thorough history and clinical examination are paramount to distinguish TGA from stroke, seizure, or infection.",
        "current_evidence": "Current literature supports the diagnosis of TGA based on clinical criteria. Recent studies emphasize the high diagnostic yield of a detailed history and recommend reserved use of neuroimaging only in atypical cases. Guidelines underscore that reassurance and observation remain the primary approach for classic TGA presentations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993033",
    "fields": {
      "question_number": "126",
      "question_text": "Patient has stroke with slurred speech you referred him to speech therapist and rehab service, this is considered as:",
      "options": {
        "A": "Primary prevention",
        "B": "Secondary prevention",
        "C": "Tertiary prevention"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Prevention in medicine is classified into primary (preventing onset), secondary (early detection and treatment), and tertiary (reducing disability and improving quality of life after disease onset). In stroke management, referral to a speech therapist and rehab service to address slurred speech is a classic example of tertiary prevention, as it aims to restore function and minimize long\u2010term deficits.",
        "pathophysiology": "Stroke results in neuronal injury and loss of function depending on the area of the brain affected. In cases where speech production is impaired due to cortical or subcortical damage, neuroplasticity and rehabilitation work to reorganize and strengthen alternative neural pathways. This process underpins the rationale for involving speech therapy and other rehabilitative services after the acute incident.",
        "clinical_correlation": "A patient presenting with post-stroke slurred speech benefits from a multidisciplinary rehabilitation program. Speech therapy helps improve communication skills while overall rehabilitation addresses other potential deficits, thereby improving daily functioning and overall quality of life.",
        "diagnostic_approach": "Diagnosis of stroke relies on neuroimaging (CT or MRI) to define the lesion. Differential considerations include transient ischemic attacks and hemorrhagic strokes. The need for rehabilitation confirms the persistence of deficits that require long-term management.",
        "classification_and_neurology": "Stroke prevention falls under the broader classification of **preventive neurology** and cerebrovascular disease management.  - The three-tiered prevention model (primary, secondary, tertiary) is a widely accepted framework endorsed by organizations such as the American Heart Association (AHA) and World Health Organization (WHO). - Primary prevention: No prior event; focus on risk factor control. - Secondary prevention: Post-event; focus on preventing recurrence. - Tertiary prevention: Post-event; focus on reducing disability and improving function.  This classification aids clinical decision-making and resource allocation.  Controversies sometimes arise regarding the overlap between secondary and tertiary prevention, especially in chronic stroke management, but rehabilitation is clearly categorized as tertiary prevention.",
        "classification_and_nosology": "Tertiary prevention is part of the preventive medicine classification system. It is distinct from primary prevention (risk factor modification) and secondary prevention (early detection and immediate post-event management to prevent recurrence).",
        "management_principles": "Rehabilitation is a key component of post-stroke care. Current guidelines recommend early initiation of speech, physical, and occupational therapy to enhance recovery. Special populations, such as pregnant or lactating patients, should receive individualized therapy plans that consider both maternal benefits and fetal safety. Medications or interventions used in the acute phase (e.g., thrombolytics) have their own separate guidelines, while rehabilitation remains a supportive, non-pharmacologic strategy.",
        "option_analysis": "Option A (Primary prevention) addresses measures to prevent the initial occurrence and is not applicable here. Option B (Secondary prevention) refers to immediate interventions after the stroke to prevent recurrence (e.g., antiplatelets, statins). Option C (Tertiary prevention) is correct because it includes rehabilitative interventions that aim to reduce long-term disability.",
        "clinical_pearls": "1. Early rehabilitation post-stroke is associated with improved neurological recovery. 2. Distinguishing between types of prevention is essential for understanding different stages of patient care.",
        "current_evidence": "Recent American Heart Association guidelines emphasize the importance of early, multidisciplinary rehabilitation post-stroke in order to maximize neuroplasticity and functional recovery, reinforcing the role of tertiary prevention in modern stroke management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993034",
    "fields": {
      "question_number": "206",
      "question_text": "RCVS ttt",
      "options": {
        "A": "(IV hydration) is supportive but insufficient as definitive therapy. Option B (Steroids) are contraindicated because RCVS is non",
        "C": "(Nimodipine) is correct as it directly addresses the pathophysiologic mechanism of vasospasm. Option D (ASA) is not indicated since antiplatelet therapy does not target the dysregulated vascular tone and could potentially raise hemorrhagic risks."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Reversible Cerebral Vasoconstriction Syndrome (RCVS) is a condition characterized by transient constriction of cerebral blood vessels that can lead to severe headaches and sometimes neurologic deficits. The goal of treatment is to relieve vasospasm and support cerebral blood flow.",
        "pathophysiology": "RCVS involves a dysregulation of cerebrovascular tone, leading to segmental vasoconstriction. The condition is largely non-inflammatory. Calcium channel blockers like nimodipine work by inhibiting calcium influx into vascular smooth muscle cells, promoting vasodilation, and reducing the severity of vasospasm.",
        "clinical_correlation": "Clinically, RCVS often presents with recurrent thunderclap headaches. While supportive care measures like IV hydration are important, they do not directly reverse the vasoconstriction. Nimodipine alleviates the vascular spasm and improves symptoms, making it the treatment of choice.",
        "diagnostic_approach": "Diagnosis is typically established via imaging studies such as CTA, MRA, or conventional angiography, which show segmental narrowing of the cerebral arteries. Differential diagnoses include aneurysmal subarachnoid hemorrhage, primary angiitis of the CNS, and migrainous syndromes.",
        "classification_and_neurology": "RCVS is classified under non-inflammatory cerebral vasculopathies. It is distinct from primary angiitis of the central nervous system (PACNS), which is an inflammatory vasculitis. RCVS belongs to a group of disorders characterized by transient cerebral artery narrowing without vessel wall inflammation. The International Classification of Headache Disorders (ICHD-3) recognizes RCVS as a cause of thunderclap headache. Nosologically, RCVS is considered a syndrome rather than a single disease entity, as it can be idiopathic or secondary to various triggers. The evolving consensus emphasizes its reversible nature and absence of inflammatory markers, differentiating it from vasculitides. Controversies remain regarding overlap with conditions like posterior reversible encephalopathy syndrome (PRES), which can co-occur or mimic RCVS.",
        "classification_and_nosology": "RCVS is categorized among cerebrovascular disorders, specifically those characterized by transient and reversible vasospastic phenomena. It should not be confused with inflammatory vasculitides or thrombotic events.",
        "management_principles": "First-line management for RCVS is the administration of nimodipine, a calcium channel blocker that targets the underlying mechanism of vasospasm. Supportive care such as analgesia and careful blood pressure management are essential adjuncts. In pregnant or lactating patients, the use of nimodipine requires careful assessment; while data are limited, its benefits in reversibility of vasospasm often outweigh potential risks when managed under specialist guidance.",
        "option_analysis": "Option A (IV hydration) is supportive but insufficient as definitive therapy. Option B (Steroids) are contraindicated because RCVS is non-inflammatory and steroids may worsen vasoconstriction. Option C (Nimodipine) is correct as it directly addresses the pathophysiologic mechanism of vasospasm. Option D (ASA) is not indicated since antiplatelet therapy does not target the dysregulated vascular tone and could potentially raise hemorrhagic risks.",
        "clinical_pearls": "1. RCVS should be suspected in patients with sudden, severe (thunderclap) headaches. 2. Nimodipine remains the mainstay of therapy for alleviating vasospasm in RCVS.",
        "current_evidence": "Recent studies and clinical practice guidelines consistently support nimodipine as the first-line treatment for RCVS. Ongoing research focuses on optimizing dosing and managing the syndrome in special populations, including postpartum women."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993035",
    "fields": {
      "question_number": "207",
      "question_text": "A patient with 3rd nerve palsy, with contralateral weakness, localization:",
      "options": {
        "A": "(Pons) and Option B (Medulla) are incorrect because the oculomotor nerve originates in the midbrain. Option C (Bases of midbrain) is correct, as it accounts for the simultaneous involvement of CN III and the corticospinal tract."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Brainstem syndromes often exhibit 'crossed findings'\u2014ipsilateral cranial nerve deficits with contralateral motor or sensory deficits. Recognizing this pattern helps in localizing the lesion within the brainstem.",
        "pathophysiology": "The midbrain contains both the oculomotor nerve (CN III) nuclei/fascicles and the corticospinal tract. An infarct affecting the bases of the midbrain can damage these adjacent structures simultaneously, producing ipsilateral CN III palsy and contralateral hemiparesis\u2014classically seen in Weber syndrome.",
        "clinical_correlation": "A patient presenting with oculomotor nerve palsy (leading to diplopia, ptosis, and possibly pupillary involvement) alongside contralateral motor weakness should raise suspicion for a midbrain lesion. This clinical constellation is pathognomonic.",
        "diagnostic_approach": "Neuroimaging, preferably MRI, is used to confirm the lesion's location. The differential diagnosis must consider pontine or medullary lesions; however, such regions don't harbor the oculomotor nerve, thereby narrowing the probable site to the midbrain.",
        "classification_and_neurology": "This lesion is classified under brainstem stroke syndromes, specifically midbrain infarcts. The classification of brainstem strokes is based on anatomical location (midbrain, pons, medulla) and vascular territory (paramedian, lateral, dorsal). Weber syndrome falls under the paramedian midbrain infarcts affecting the basis pedunculi and oculomotor nerve fascicles.  The broader nosology includes: - Midbrain syndromes: Weber, Benedikt, Claude - Pontine syndromes: Millard-Gubler, Foville - Medullary syndromes: Medial medullary (Dejerine), lateral medullary (Wallenberg)  Modern stroke classification systems like the TOAST criteria help categorize ischemic strokes by etiology, but clinical syndromes remain essential for localization. Some controversy exists in overlapping syndromes due to variable lesion sizes, but the anatomical-clinical correlation remains robust.",
        "classification_and_nosology": "Weber syndrome is one of several midbrain syndromes in the classification of brainstem strokes. It is defined by the peculiar combination of an ipsilateral oculomotor nerve palsy with contralateral hemiparesis.",
        "management_principles": "Management adheres to standard stroke protocols, including acute reperfusion strategies when eligible and subsequent rehabilitation to address motor and cranial deficits. In pregnant or lactating patients, treatment selection (including thrombolysis) must be individualized to balance maternal benefits with fetal safety.",
        "option_analysis": "Option A (Pons) and Option B (Medulla) are incorrect because the oculomotor nerve originates in the midbrain. Option C (Bases of midbrain) is correct, as it accounts for the simultaneous involvement of CN III and the corticospinal tract.",
        "clinical_pearls": "1. The combination of ipsilateral third nerve palsy with contralateral hemiparesis strongly localizes to the midbrain. 2. Weber syndrome is the quintessential example of a brainstem 'crossed syndrome.'",
        "current_evidence": "Advancements in neuroimaging and refinements in stroke management guidelines continue to support early detection and localization of brainstem strokes, which is critical for prompt and effective therapeutic intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993036",
    "fields": {
      "question_number": "208",
      "question_text": "III nerve palsy with ipsilateral ataxia",
      "options": {
        "A": "(Claude syndrome) is correct because it exactly matches the clinical picture of CN III palsy with ipsilateral ataxia. Option B (Weber syndrome) is incorrect since it presents with contralateral hemiparesis. Option C (Benedikt syndrome) is associated with contralateral involuntary movements, and Option D (Nothnagel syndrome) is less commonly used and does not fully capture the classic presentation described."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "When a patient presents with a cranial nerve III palsy combined with ipsilateral ataxia, the clinical syndrome most consistent with this presentation is Claude syndrome. It highlights a specific midbrain involvement where both oculomotor function and cerebellar coordination are affected.",
        "pathophysiology": "Claude syndrome results from a lesion in the midbrain that interrupts the oculomotor nerve fibers as well as adjacent structures involved in cerebellar coordination (such as the red nucleus or superior cerebellar peduncle). This leads to the combination of ocular motor deficits and cerebellar ataxia on the same side.",
        "clinical_correlation": "Patients with Claude syndrome typically display signs of CN III dysfunction (ptosis, diplopia, and potential pupillary involvement) along with ipsilateral ataxia. This contrasts with other midbrain syndromes where additional contralateral motor deficits or involuntary movements may be evident.",
        "diagnostic_approach": "Differential diagnosis includes other midbrain syndromes: Weber syndrome (characterized by contralateral hemiparesis), Benedikt syndrome (which involves contralateral involuntary movements), and Nothnagel syndrome (a less common entity with overlapping features). MRI is pivotal for accurate localization of the lesion.",
        "classification_and_neurology": "These syndromes belong to the category of midbrain (mesencephalic) brainstem stroke syndromes, classically described in neuroanatomical localization frameworks. They are part of the broader family of crossed brainstem syndromes characterized by ipsilateral cranial nerve deficits and contralateral motor or sensory findings. Claude, Weber, Benedikt, and Nothnagel syndromes are distinguished by the combination of affected structures within the midbrain tegmentum and basis. Historically, these eponymous syndromes have helped refine clinical localization in neurology and neuroanatomy. Contemporary nosology integrates these syndromes within vascular brainstem infarction classifications, often described by lesion topography on imaging rather than eponyms alone. Some debate exists regarding overlap and distinctions among these syndromes, but they remain valuable teaching tools for clinical localization.",
        "classification_and_nosology": "Claude syndrome is classified under midbrain vascular syndromes and is distinguished by the unique combination of ipsilateral oculomotor palsy and ipsilateral cerebellar ataxia. This precise localization sets it apart from similar syndromes of the midbrain.",
        "management_principles": "Management of Claude syndrome follows acute stroke management protocols, including potential thrombolysis if within the therapeutic window and supportive care thereafter. Subsequent rehabilitation focusing on ocular motor control and coordination is essential. In pregnant or lactating patients, care should be taken to use agents with proven safety profiles while ensuring prompt treatment to minimize long-term disability.",
        "option_analysis": "Option A (Claude syndrome) is correct because it exactly matches the clinical picture of CN III palsy with ipsilateral ataxia. Option B (Weber syndrome) is incorrect since it presents with contralateral hemiparesis. Option C (Benedikt syndrome) is associated with contralateral involuntary movements, and Option D (Nothnagel syndrome) is less commonly used and does not fully capture the classic presentation described.",
        "clinical_pearls": "1. Claude syndrome is characterized by ipsilateral oculomotor nerve palsy and ataxia due to a midbrain lesion. 2. Accurate anatomical localization is critical for differentiating between various midbrain syndromes.",
        "current_evidence": "The traditional descriptions of midbrain syndromes, including Claude syndrome, remain valid. Recent literature supports the use of advanced neuroimaging techniques to confirm diagnosis and guide management, with current stroke management guidelines emphasizing early rehabilitation even in atypical presentations."
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
