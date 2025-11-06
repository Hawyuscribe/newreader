
# Import batch 2 of 3 from chunk_3_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993037",
    "fields": {
      "question_number": "209",
      "question_text": "Young female with stroke & recurrent abortion",
      "options": {
        "A": "(Protein C deficiency) and option b (Antithrombin III deficiency) predispose mainly to venous thrombosis and do not explain recurrent abortions. Option d (Anti",
        "C": ", Antiphospholipid syndrome, best fits the clinical scenario with its dual presentation of arterial stroke and recurrent pregnancy loss."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Antiphospholipid syndrome (APS) is an autoimmune disorder marked by the presence of antiphospholipid antibodies (such as lupus anticoagulant, anticardiolipin, and anti-\u03b22 glycoprotein I) that predispose patients to thrombosis. The syndrome uniquely presents with both arterial events (e.g., stroke) and obstetric complications (e.g., recurrent early pregnancy loss).",
        "pathophysiology": "In APS, antibodies target plasma proteins bound to phospholipids, leading to endothelial cell activation, platelet aggregation, and a prothrombotic state. Vascular occlusion in cerebral arteries can lead to stroke, while placental thrombosis causes recurrent miscarriages. Recent studies have further clarified the role of these antibodies in disrupting annexin V shields and promoting coagulation.",
        "clinical_correlation": "Young females presenting with neurological deficits such as stroke in combination with a history of recurrent abortions should raise suspicion for APS. The clinical picture is distinct because most inherited thrombophilias, like Protein C or antithrombin III deficiencies, predominantly predispose to venous thrombosis without the obstetric complications seen in APS.",
        "diagnostic_approach": "The workup involves laboratory testing for lupus anticoagulant, anticardiolipin antibodies, and anti-\u03b22 glycoprotein I on two separate occasions (at least 12 weeks apart). Differential diagnoses include inherited thrombophilias (e.g., Protein C deficiency, antithrombin deficiency) and other autoimmune disorders (secondary APS associated with SLE), but the combined arterial thrombosis and miscarriage history is highly characteristic of APS.",
        "classification_and_neurology": "Antiphospholipid syndrome is classified as an acquired autoimmune thrombophilia within the spectrum of systemic autoimmune disorders. The 2006 revised Sapporo classification criteria (Sydney criteria) define APS by the presence of at least one clinical criterion (vascular thrombosis or pregnancy morbidity) and one laboratory criterion (presence of lupus anticoagulant, anticardiolipin, or anti-beta-2 glycoprotein I antibodies). APS can be primary (isolated) or secondary, most commonly associated with systemic lupus erythematosus. It fits within the broader category of hypercoagulable states alongside inherited thrombophilias such as Protein C deficiency, Protein S deficiency, and antithrombin III deficiency. Unlike inherited deficiencies, APS is autoimmune-mediated and often requires immunologic testing. The classification has evolved to improve specificity and reproducibility of diagnosis, with ongoing research into non-criteria manifestations and antibody profiles.",
        "classification_and_nosology": "APS can be classified as primary (occurring in the absence of any other autoimmune disease) or secondary (associated with conditions like systemic lupus erythematosus). It falls in the nosological category of acquired hypercoagulable states with autoimmune etiology.",
        "management_principles": "First-line management for APS with a history of thrombotic events includes long-term anticoagulation, typically with warfarin (with a target INR of 2-3). In pregnant women, warfarin is contraindicated due to teratogenicity; therefore, treatment involves low molecular weight heparin (LMWH) combined with low-dose aspirin. In non-pregnant patients, direct oral anticoagulants (DOACs) are under investigation, but warfarin remains the standard in high-risk APS.",
        "option_analysis": "Option a (Protein C deficiency) and option b (Antithrombin III deficiency) predispose mainly to venous thrombosis and do not explain recurrent abortions. Option d (Anti-factor VII antibodies) is not recognized as a cause of hypercoagulability; factor VII deficiency usually leads to bleeding. Option c, Antiphospholipid syndrome, best fits the clinical scenario with its dual presentation of arterial stroke and recurrent pregnancy loss.",
        "clinical_pearls": "1) Always suspect APS in young females with stroke and a history of miscarriage. 2) Confirmatory testing requires repeat antibody assays at least 12 weeks apart. 3) Anticoagulation regimens differ in pregnant patients (LMWH + aspirin) compared to non-pregnant patients (warfarin).",
        "current_evidence": "Recent guidelines and consensus statements from rheumatology and hematology societies emphasize the importance of early diagnosis and appropriate anticoagulation in APS. While DOACs are emerging, warfarin remains the first-line treatment in high-risk APS patients, and management in pregnancy continues to favor LMWH with low-dose aspirin based on current research."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993038",
    "fields": {
      "question_number": "210",
      "question_text": "Middle age male Rt hemiplegia , found to have AF with attached CT brain, ttt",
      "options": {
        "A": "(ASA) and option b (dual antiplatelet therapy with ASA & Plavix) have been shown to be inferior to anticoagulation in AF",
        "C": ", warfarin, effectively reduces the risk of cardioembolic events and is considered an evidence",
        "D": "(LMWH) is not used for long"
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Atrial fibrillation (AF) is a common cardiac arrhythmia that predisposes patients to thrombus formation in the atria, which can embolize to the brain causing ischemic stroke. Effective stroke prevention in AF is achieved by systemic anticoagulation.",
        "pathophysiology": "In AF, the irregular and often rapid atrial contractions lead to stasis of blood, especially in the left atrial appendage, promoting clot formation. These clots can then dislodge and travel to cerebral arteries causing embolic strokes. Anticoagulation with warfarin inhibits the vitamin K-dependent synthesis of clotting factors II, VII, IX, and X, thereby reducing the risk of thrombosis.",
        "clinical_correlation": "A middle-aged male presenting with right hemiplegia and a new stroke on CT in the setting of AF fits the classic picture of a cardioembolic stroke. Prevention of future embolic events is critical in such patients.",
        "diagnostic_approach": "After initial brain imaging (CT scan) confirms ischemic stroke, further cardiac evaluation with echocardiography is standard. When echocardiography is normal and AF is present, the focus shifts to long-term anticoagulation. Differential diagnoses include other causes of stroke such as carotid artery disease or intracranial hemorrhage, but the presence of AF strongly points toward a cardioembolic source.",
        "classification_and_neurology": "Ischemic strokes are classified etiologically by systems such as TOAST (Trial of Org 10172 in Acute Stroke Treatment), which categorizes stroke into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Cardioembolic stroke due to AF falls under the cardioembolism category, which is important because it dictates specific management. This classification has evolved to incorporate imaging and cardiac monitoring advances. The nosology emphasizes the need to identify the stroke subtype to optimize therapy. AF-related strokes are a major subset of cardioembolic strokes and carry distinct prognostic and therapeutic implications.",
        "classification_and_nosology": "Stroke related to AF is classified as a cardioembolic stroke. AF itself can be paroxysmal, persistent, or permanent, and is a leading cause of cardioembolic events.",
        "management_principles": "First-line management for stroke prevention in AF typically involves anticoagulation. While direct oral anticoagulants (DOACs) have largely supplanted warfarin in many settings due to ease of use and lower bleeding risks, warfarin remains a standard option particularly when DOACs are contraindicated or unavailable. In pregnant women, warfarin is contraindicated due to teratogenic risks, and LMWH is preferred. In lactating women, warfarin is considered safe but DOACs are generally not recommended.",
        "option_analysis": "Option a (ASA) and option b (dual antiplatelet therapy with ASA & Plavix) have been shown to be inferior to anticoagulation in AF-related stroke prevention. Option d (LMWH) is not used for long-term outpatient management of AF. Option c, warfarin, effectively reduces the risk of cardioembolic events and is considered an evidence-based choice in appropriate clinical contexts.",
        "clinical_pearls": "1) AF is a high-risk arrhythmia for cardioembolic stroke, necessitating effective anticoagulation therapy. 2) DOACs are increasingly used; however, warfarin remains an acceptable option in many situations. 3) Special considerations are needed for anticoagulation therapy in pregnancy and lactation.",
        "current_evidence": "While recent guidelines increasingly favor DOACs for non-valvular AF, warfarin remains a cornerstone in stroke prevention for certain patient groups and settings. Clinical trials have demonstrated a significant reduction in stroke risk with proper anticoagulation compared to antiplatelet therapy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993039",
    "fields": {
      "question_number": "211",
      "question_text": "Patient with 3 mm Hemorrhage in putamen, stable hemorrhage but had increased oedema & decrease LOC, ttt",
      "options": {
        "A": "(Triple H therapy) is inappropriate as it is used in managing vasospasm in subarachnoid hemorrhage. Option b (Osmotic treatment) may transiently reduce ICP but does not address ongoing mass effect in a deteriorating patient. Option c (Dexamethasone) has been proven ineffective and is potentially harmful in ICH. Option d (Surgical evacuation) is correct as it directly alleviates the mass effect and reduces the risk of further neurological deterioration."
      },
      "correct_answer": "d",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Intracerebral hemorrhage (ICH) in the putamen is typically related to hypertensive hemorrhage. Even a small hematoma (e.g., 3 mm) can be surrounded by significant edema, leading to increased intracranial pressure (ICP) and neurological deterioration such as decreased level of consciousness.",
        "pathophysiology": "Following hemorrhage, blood products and clot retraction trigger an inflammatory cascade resulting in vasogenic edema. The expanding edema may cause a mass effect that further compromises adjacent brain structures. Although the hematoma itself is small, the associated swelling can lead to significant clinical deterioration.",
        "clinical_correlation": "In this case, despite a stable hemorrhage size, the patient\u2019s declining level of consciousness is clinically significant and suggests worsening mass effect from cerebral edema. This scenario necessitates prompt intervention to reduce ICP and prevent herniation.",
        "diagnostic_approach": "Serial brain imaging (primarily CT scans) is used to monitor the size of the hemorrhage and associated edema. Differential diagnoses for acute neurological decline in ICH include hematoma expansion, hydrocephalus, or re-bleeding. In this context, the stable hematoma but increased edema indicates that mass effect is the culprit.",
        "classification_and_neurology": "Intracerebral hemorrhage is classified under hemorrhagic strokes, distinct from ischemic strokes. The classification can be further refined by etiology (hypertensive, amyloid angiopathy, vascular malformations, coagulopathy), location (lobar, deep structures such as putamen, thalamus, brainstem, cerebellum), and size. The putaminal hemorrhage is a subtype of deep hypertensive hemorrhage. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify ICH severity based on volume, location, and clinical status, which directly informs management strategies. Surgical indications vary depending on these factors, with deep hemorrhages traditionally considered less surgically accessible, but worsening edema and deterioration may mandate surgical evacuation.",
        "classification_and_nosology": "ICH is typically classified by location (lobar, deep, cerebellar, brainstem) and etiology (hypertensive, amyloid angiopathy, vascular malformation). A putaminal hemorrhage is a classic example of a hypertensive deep hemorrhage.",
        "management_principles": "Initial management includes blood pressure control, reversal of any coagulopathy, and measures to reduce ICP (e.g., osmotic agents like mannitol or hypertonic saline). However, when neurological deterioration occurs due to significant mass effect from edema, surgical evacuation is recommended. Current guidelines advise considering surgical intervention for patients who deteriorate neurologically despite medical management. In a pregnant patient, special consideration would be given to the timing and type of surgery and the anesthetic management, balancing maternal and fetal risks.",
        "option_analysis": "Option a (Triple H therapy) is inappropriate as it is used in managing vasospasm in subarachnoid hemorrhage. Option b (Osmotic treatment) may transiently reduce ICP but does not address ongoing mass effect in a deteriorating patient. Option c (Dexamethasone) has been proven ineffective and is potentially harmful in ICH. Option d (Surgical evacuation) is correct as it directly alleviates the mass effect and reduces the risk of further neurological deterioration.",
        "clinical_pearls": "1) In ICH, clinical deterioration may result from progressive edema even if the hematoma is small. 2) Surgical intervention is reserved for cases where medical management fails and neurological status worsens. 3) Triple H therapy is specific to cerebral vasospasm in subarachnoid hemorrhage and not applicable in ICH.",
        "current_evidence": "Recent trials and meta-analyses have shown that while medical management is first-line in many ICH cases, selected patients with deep hemorrhages and evidence of mass effect with clinical decline may benefit from surgical evacuation. Steroid use (such as dexamethasone) has been expressly discouraged based on high-quality evidence demonstrating no benefit and possible harm."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993040",
    "fields": {
      "question_number": "212",
      "question_text": "MRI (DWI) multiple infarctions in one side, NL ECHO- Next step",
      "options": {
        "A": "(CTA) is correct because it provides detailed imaging of both extracranial and intracranial arteries and is rapid and widely available. Option b (Doppler ultrasound) is limited by operator dependency and inability to fully image intracranial vessels. Option c (MRA) is less sensitive for detecting calcific plaques and may not be as readily available in acute settings. Thus, CTA stands out as the most appropriate next diagnostic step."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Multiple acute infarctions on diffusion-weighted imaging (DWI) confined to one side of the brain suggest an embolic phenomenon likely arising from an arterial source rather than a cardiac source, especially when the echocardiogram is normal.",
        "pathophysiology": "The presence of multiple infarcts often implies an artery-to-artery embolism, possibly due to atherosclerotic plaque rupture or dissection. Computed tomography angiography (CTA) provides detailed images of both extracranial and intracranial vessels, identifying stenosis, occlusions, or unstable plaques that may shed microemboli.",
        "clinical_correlation": "In a patient with acute ischemic stroke and multiple infarctions on the same side, a normal echocardiogram decreases the likelihood of cardioembolism. Thus, evaluating the arterial system, especially the carotid and vertebral arteries, is crucial to determine the source of emboli.",
        "diagnostic_approach": "After a normal echocardiogram, the next step is vascular imaging. Differential diagnoses include carotid artery stenosis, arterial dissection, and intracranial atherosclerotic disease. While Doppler ultrasound is useful as a screening tool, it is operator dependent and less sensitive for intracranial pathology. Magnetic resonance angiography (MRA) is an alternative but may not detect calcified plaques as reliably as CTA.",
        "classification_and_neurology": "This clinical scenario falls under the broad category of ischemic stroke, specifically the subtype of embolic stroke of undetermined source (ESUS) if no cardiac or arterial source is identified, or artery-to-artery embolism if a proximal vascular lesion is found. The TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Here, with normal cardiac evaluation and multiple infarcts, the classification leans toward large artery atherosclerosis or ESUS pending further vascular imaging. Evolving classifications emphasize the importance of detailed vascular and cardiac workup to accurately subtype stroke etiology, which guides management. Controversies remain regarding the best imaging modality for arterial evaluation and the threshold for invasive testing.",
        "classification_and_nosology": "Strokes are classified by etiology \u2013 cardioembolic, large-artery atherosclerosis, small vessel disease, etc. This case fits the profile of large-artery atherosclerotic stroke as the pattern of infarcts points to an embolic source from an arterial plaque.",
        "management_principles": "The current guidelines recommend CTA as the next diagnostic step for rapid and comprehensive evaluation of the cerebrovascular tree. Following identification of the underlying pathology, management may include antiplatelet therapy, statins, and risk factor modification. In pregnant patients, radiation exposure from CTA is a concern; in such cases, magnetic resonance angiography (MRA) may be considered as an alternative. During lactation, the risk is much lower, and CTA can generally be performed with proper safety measures.",
        "option_analysis": "Option a (CTA) is correct because it provides detailed imaging of both extracranial and intracranial arteries and is rapid and widely available. Option b (Doppler ultrasound) is limited by operator dependency and inability to fully image intracranial vessels. Option c (MRA) is less sensitive for detecting calcific plaques and may not be as readily available in acute settings. Thus, CTA stands out as the most appropriate next diagnostic step.",
        "clinical_pearls": "1) In stroke workup with multiple infarcts and a normal echocardiogram, always consider an arterial source such as carotid stenosis or plaque rupture. 2) CTA is the gold standard for quick and comprehensive vascular assessment in these cases. 3) In pregnant patients, balancing imaging modality risks is crucial, with MRA serving as an alternative when necessary.",
        "current_evidence": "Recent studies and stroke guidelines emphasize the role of CTA in acute stroke settings due to its superior resolution and rapid acquisition time. Although DOACs and other preventive measures have evolved for stroke management, detailed vascular imaging remains essential for guiding appropriate secondary prevention strategies and interventions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993041",
    "fields": {
      "question_number": "213",
      "question_text": "Decrease risk of stroke in patient with homocysteinemia",
      "options": {
        "A": "(Vitamin B1) supports carbohydrate metabolism rather than homocysteine clearance. Option b (Coenzyme Q10) plays a role in mitochondrial function and antioxidant defense but does not lower homocysteine levels. Option d (Carnitine) is involved in fatty acid transport and energy metabolism without an impact on homocysteine metabolism. Only option c (Vitamin B6) directly aids the enzyme"
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Hyperhomocysteinemia is associated with an increased risk of stroke because elevated homocysteine levels can damage blood vessels and promote thrombosis. Vitamin B6 (pyridoxine) is a critical cofactor in the transsulfuration pathway, converting homocysteine into cystathionine, thereby reducing plasma homocysteine levels.",
        "pathophysiology": "The accumulation of homocysteine leads to endothelial dysfunction, proinflammatory changes, and a propensity for thrombus formation. Vitamin B6 facilitates the activity of cystathionine \u03b2-synthase, which metabolizes homocysteine into cystathionine. This metabolic conversion is vital for maintaining lower levels of homocysteine and decreasing the vascular injury that predisposes patients to stroke.",
        "clinical_correlation": "Patients with elevated homocysteine levels are at higher risk for stroke and other cardiovascular events. Supplementation with vitamin B6 can help lower homocysteine levels, reducing stroke risk. This approach is part of a broader strategy that may also include folate and vitamin B12 supplementation, along with lifestyle and dietary modifications.",
        "diagnostic_approach": "Diagnosing hyperhomocysteinemia involves plasma homocysteine measurement and identifying underlying causes such as nutritional deficiencies, genetic mutations (e.g., MTHFR), or renal insufficiency. Differential diagnoses include other metabolic causes of vascular disease. Laboratory evaluation is key to tailoring therapy.",
        "classification_and_neurology": "Hyperhomocysteinemia is classified biochemically based on plasma homocysteine levels: normal (<15 \u03bcmol/L), moderate (15\u201330 \u03bcmol/L), intermediate (30\u2013100 \u03bcmol/L), and severe (>100 \u03bcmol/L). It is further categorized etiologically into: - **Genetic:** e.g., CBS deficiency, MTHFR mutations - **Nutritional:** deficiencies of folate, vitamin B12, vitamin B6 - **Secondary causes:** renal failure, hypothyroidism, certain medications  From a cerebrovascular disease perspective, hyperhomocysteinemia is a modifiable risk factor for ischemic stroke, classified under metabolic and biochemical risk factors. Contemporary stroke classification systems like TOAST recognize metabolic contributors but focus primarily on clinical and imaging criteria; however, biochemical risk factor modification is integral to secondary prevention.",
        "classification_and_nosology": "Hyperhomocysteinemia can be categorized as primary (genetic) or secondary (due to vitamin deficiencies, renal disease, or medication effects). It is recognized as a modifiable risk factor for stroke and cardiovascular disease.",
        "management_principles": "Management begins with vitamin supplementation: first-line therapy typically includes vitamin B6 (along with folate and vitamin B12 when indicated) to correct the metabolic defect. In addition, controlling other stroke risk factors through lifestyle changes and medications is essential. In pregnancy, folate supplementation is critical to prevent neural tube defects, and vitamin B6 is generally considered safe though should be dosed appropriately. During lactation, supplementation is usually well tolerated but must be monitored according to clinical guidelines.",
        "option_analysis": "Option a (Vitamin B1) supports carbohydrate metabolism rather than homocysteine clearance. Option b (Coenzyme Q10) plays a role in mitochondrial function and antioxidant defense but does not lower homocysteine levels. Option d (Carnitine) is involved in fatty acid transport and energy metabolism without an impact on homocysteine metabolism. Only option c (Vitamin B6) directly aids the enzyme-mediated clearance of homocysteine, making it the correct choice.",
        "clinical_pearls": "1. Elevated homocysteine is an independent risk factor for stroke. 2. Vitamin B6 is crucial in lowering homocysteine via the transsulfuration pathway. 3. A comprehensive approach often includes folate and B12 alongside B6.",
        "current_evidence": "Recent studies have underscored the biological rationale for lowering homocysteine with B vitamin supplementation, although clinical trials have shown mixed results regarding direct stroke prevention. Current guidelines still support correcting vitamin deficiencies in patients with hyperhomocysteinemia as part of an overall cardiovascular risk reduction strategy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993042",
    "fields": {
      "question_number": "214",
      "question_text": "Patient was not able to read his handwriting",
      "options": {
        "A": "(ACA) would more likely cause contralateral leg weakness and cognitive changes rather than isolated visual processing deficits. Option b (MCA) is associated with hemiparesis and language deficits. Option c (ICA) would result in broader deficits by affecting multiple cerebral territories. Option d (PCA) directly supplies the occipital lobe, clarifying the visual disturbance observed."
      },
      "correct_answer": "d",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "The posterior cerebral artery (PCA) supplies the occipital lobe and visual association areas. Damage to these regions typically results in visual processing deficits rather than classical language deficits.",
        "pathophysiology": "An ischemic event in the PCA territory affects the occipital cortex, including regions essential for visual recognition and processing. This can produce specific syndromes such as alexia (inability to read) without agraphia, where reading is impaired while writing remains intact.",
        "clinical_correlation": "A patient presenting with an inability to read his own handwriting suggests a deficit in visual processing rather than motor or language dysfunction. This localization is more consistent with a lesion in the visual cortex supplied by the PCA.",
        "diagnostic_approach": "Neuroimaging, especially MRI, is paramount for identifying infarcts in the occipital lobes. Differential diagnoses include strokes in the MCA territory (which more commonly cause aphasia and hemiparesis) or ACA territory (which more often lead to leg weakness and frontal lobe changes). Detailed clinical assessment combined with imaging helps to localize the lesion accurately.",
        "classification_and_neurology": "Ischemic strokes are classified by vascular territory and underlying etiology. The TOAST classification categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined causes, and undetermined causes. PCA infarcts are a subset of large artery strokes affecting the posterior circulation. The PCA arises from the vertebrobasilar system and supplies the occipital lobes and inferomedial temporal lobes. Understanding the vascular territories is critical for the anatomical classification of stroke syndromes. Over time, advances in neuroimaging have refined these classifications by allowing precise localization and etiological diagnosis, improving prognostication and management.",
        "classification_and_nosology": "PCA strokes are categorized under posterior circulation strokes. They are distinct from anterior circulation strokes in their clinical presentation and in the vascular territories involved, often presenting with isolated visual deficits.",
        "management_principles": "Acute management involves standard stroke protocols, including the potential use of thrombolytic therapy if within the appropriate window. Secondary prevention includes the use of antiplatelet agents, statin therapy, and control of vascular risk factors. In pregnant or lactating patients, careful selection of medications is required; low-dose aspirin is typically acceptable, and adjustments may be made based on individual risk profiles.",
        "option_analysis": "Option a (ACA) would more likely cause contralateral leg weakness and cognitive changes rather than isolated visual processing deficits. Option b (MCA) is associated with hemiparesis and language deficits. Option c (ICA) would result in broader deficits by affecting multiple cerebral territories. Option d (PCA) directly supplies the occipital lobe, clarifying the visual disturbance observed.",
        "clinical_pearls": "1. PCA infarcts are commonly linked with visual field deficits and reading impairments. 2. Alexia without agraphia is a hallmark of occipital lobe involvement. 3. Differentiating stroke territories is critical for accurate diagnosis and management.",
        "current_evidence": "Advances in imaging have improved localization of infarcts, and current guidelines emphasize the tailored management of posterior circulation strokes. Recent research continues to refine the indications for thrombolytic therapy and secondary prevention strategies in these patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993043",
    "fields": {
      "question_number": "215",
      "question_text": "Post of aortic surgery awake with flaccid paraparesis & sensory level",
      "options": {
        "B": "(T8) is correct because of the typical anatomical origin of the artery of Adamkiewicz in this region. Option a (T4) would suggest a higher level infarct, which is less common in this scenario; option c (L4) is below the termination of the spinal cord; and option d (C2) is inconsistent with the clinical presentation focused on lower extremity involvement."
      },
      "correct_answer": "b",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Spinal cord ischemia is a known complication after aortic surgery, primarily due to compromised blood flow through the artery of Adamkiewicz, which is the major arterial supply to the anterior spinal cord.",
        "pathophysiology": "The artery of Adamkiewicz most commonly originates between T8 and L1. Its disruption during aortic surgery can lead to anterior spinal artery syndrome, resulting in flaccid paraparesis and a clear sensory level at the corresponding spinal segment due to ischemia of the anterior two-thirds of the spinal cord.",
        "clinical_correlation": "Postoperative patients presenting with flaccid paraparesis and a defined sensory level have classic findings for spinal cord ischemia. The level of sensory loss typically correlates with the location of the compromised arterial blood supply.",
        "diagnostic_approach": "Diagnosis is based on clinical examination and is confirmed with MRI of the spine. Differential diagnoses include spinal epidural hematoma, transverse myelitis, or mechanical compression, but the temporal relationship to aortic surgery and the level-specific deficit point toward ischemia.",
        "classification_and_neurology": "Spinal cord ischemia is classified under vascular myelopathies, which include ischemic, hemorrhagic, and compressive etiologies. Anterior spinal artery syndrome is a subtype characterized by ischemia of the anterior two-thirds of the spinal cord. This condition is part of the broader category of spinal cord infarction, which can be spontaneous or iatrogenic (e.g., post-aortic surgery). Nosologically, it is distinct from demyelinating myelopathies and compressive lesions. Classification systems emphasize the vascular territory involved (anterior vs. posterior spinal arteries) and the clinical syndrome produced. Current consensus recognizes spinal cord ischemia as a rare but devastating complication of aortic interventions.",
        "classification_and_nosology": "Spinal cord ischemia is classified as a vascular myelopathy and specifically as anterior spinal artery syndrome when the anterior two-thirds of the cord are affected. The level of the lesion is critical for both diagnosis and prognosis.",
        "management_principles": "Management is primarily supportive and aimed at optimizing perfusion pressure, including strategies such as blood pressure augmentation and, in some cases, cerebrospinal fluid drainage. In high-risk patients, careful intraoperative monitoring and protective strategies are used. In pregnant patients, maintaining spinal cord perfusion through judicious hemodynamic management is essential, while similar principles apply in lactating patients with attention to supportive care.",
        "option_analysis": "Option b (T8) is correct because of the typical anatomical origin of the artery of Adamkiewicz in this region. Option a (T4) would suggest a higher level infarct, which is less common in this scenario; option c (L4) is below the termination of the spinal cord; and option d (C2) is inconsistent with the clinical presentation focused on lower extremity involvement.",
        "clinical_pearls": "1. The artery of Adamkiewicz generally arises between T8 and L1, making these levels most vulnerable post-aortic surgery. 2. A clear sensory level is indicative of a localized cord lesion. 3. Early recognition of spinal cord ischemia is critical for improving outcomes.",
        "current_evidence": "Recent improvements in aortic surgical techniques and intraoperative monitoring have emphasized the need to protect spinal cord perfusion. Updated guidelines recommend measures like cerebrospinal fluid drainage and blood pressure optimization to reduce the incidence of postoperative spinal cord ischemia."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993044",
    "fields": {
      "question_number": "216",
      "question_text": "75 year old female, DM and HTN, came with Rt sided weakness since one week, MRI: Lt internal capsule lacunar infarction, vascular workup: Rt ICA 55 % stenosis & Lt ICA of 65 % stenosis. What to do for her regarding stroke prevention",
      "options": {
        "A": "(Right ICA stenting) and option b (Left ICA stenting) are not indicated because both stenoses are moderate and asymptomatic relative to the lacunar stroke pathophysiology. Option c (Maximize medical treatment) is appropriate, as current guidelines support intensive medical management for lacunar strokes."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Lacunar strokes are a type of small vessel cerebrovascular disease and are often the result of chronic conditions such as hypertension and diabetes. They differ from large vessel strokes caused by significant atherosclerotic disease.",
        "pathophysiology": "Lacunar infarcts occur due to occlusion of small penetrating arteries that supply deep brain structures such as the internal capsule. The moderate carotid stenoses in this patient (55% and 65%) are typically insufficient to cause embolic strokes, particularly when the clinical picture is that of a lacunar infarct.",
        "clinical_correlation": "In elderly patients with risk factors like diabetes and hypertension, lacunar strokes are common. The presentation with an internal capsule lacunar infarction and moderate carotid stenosis supports the diagnosis of a small vessel stroke rather than an embolic event from significant carotid atherosclerosis.",
        "diagnostic_approach": "Diagnosis is made based on clinical findings and imaging studies (MRI) that reveal small, deep infarcts. Differential diagnoses include embolic strokes from significant carotid stenosis or cortical infarcts, but the absence of high-grade stenosis or cortical involvement makes a lacunar stroke more likely.",
        "classification_and_neurology": "The patient's stroke falls under the category of lacunar infarcts, a subtype of ischemic stroke classified in the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system as 'small vessel occlusion.' This classification distinguishes lacunar strokes from large artery atherosclerosis and cardioembolism. Carotid artery stenosis is classified under large artery atherosclerosis. The degree of stenosis is graded by NASCET (North American Symptomatic Carotid Endarterectomy Trial) criteria, with intervention typically recommended for symptomatic stenosis >70%. Asymptomatic carotid stenosis management is more conservative. The current consensus supports medical therapy for moderate or asymptomatic stenosis, especially when the stroke subtype is lacunar. This nuanced classification guides therapeutic decisions.",
        "classification_and_nosology": "Lacunar strokes are classified under small vessel disease. They are distinct from large vessel strokes, which are caused by significant carotid or cardioembolic sources.",
        "management_principles": "The first-line treatment is aggressive medical management. This includes antiplatelet therapy (aspirin and/or clopidogrel), high-intensity statin therapy, optimal control of blood pressure and blood sugar, and lifestyle modifications. Carotid stenting or endarterectomy is generally reserved for symptomatic high-grade stenosis (typically >70%). In pregnant or lactating patients, medical management is adjusted with agents proven safe in these groups; low-dose aspirin is often acceptable with careful monitoring.",
        "option_analysis": "Option a (Right ICA stenting) and option b (Left ICA stenting) are not indicated because both stenoses are moderate and asymptomatic relative to the lacunar stroke pathophysiology. Option c (Maximize medical treatment) is appropriate, as current guidelines support intensive medical management for lacunar strokes.",
        "clinical_pearls": "1. Lacunar strokes result from small vessel disease, not embolism from carotid stenosis. 2. Moderate carotid stenosis does not typically warrant revascularization in the context of lacunar infarction. 3. Risk factor modification is key to preventing recurrent stroke.",
        "current_evidence": "Recent trials and guidelines emphasize that aggressive medical management is superior to invasive interventions in the setting of lacunar strokes. Ongoing research supports the role of strict blood pressure, glycemic, and lipid control in reducing the risk of future cerebrovascular events."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993045",
    "fields": {
      "question_number": "217",
      "question_text": "82-year-old, medically free, came with acute right-side weakness and global aphasia for 3 hours, BP 180/100mmHg, his CT scan is shown (no hemorrhage, with good ASPECT scores). What is your next step in his management?",
      "options": {
        "A": "(reduce BP) is incorrect because although the patient is hypertensive, his blood pressure is still below the critical threshold that mandates immediate lowering prior to tPA. Option B (IV thrombolytic) is the correct and time",
        "C": "(CTA) is valuable in later planning for endovascular therapy but should not delay the administration of thrombolysis in eligible patients."
      },
      "correct_answer": "b",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke management relies on rapid identification and revascularization to salvage the ischemic penumbra. The patient, presenting within 3 hours of symptom onset with CT imaging that excludes hemorrhage and shows a high ASPECTS score, meets the criteria for thrombolytic therapy.",
        "pathophysiology": "Ischemic strokes occur when an occlusive thrombus or embolus disrupts cerebral blood flow, leading to a core of irreversibly injured tissue surrounded by a penumbra that is at risk yet salvageable. Intravenous thrombolytics (tPA) catalyze the conversion of plasminogen to plasmin, lysing the clot and restoring perfusion. Inappropriately lowering blood pressure can reduce perfusion in the penumbra and worsen injury.",
        "clinical_correlation": "The patient\u2019s global aphasia and right-sided weakness suggest a dominant hemisphere (likely left MCA territory) infarct. His blood pressure of 180/100 mmHg, although high, is below the threshold of 185/110 mmHg that necessitates urgent control before thrombolytic administration. His CT findings (absence of hemorrhage, good ASPECTS) further affirm that thrombolysis is appropriate.",
        "diagnostic_approach": "The immediate use of non-contrast head CT is critical to exclude hemorrhage. Differential diagnoses include hemorrhagic stroke (ruled out by CT), stroke mimics (e.g., seizures, migraine), and other intracranial emergencies. Advanced imaging like CTA may be used subsequently to assess large vessel occlusion but should not delay thrombolysis.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases per the ICD-10 and the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system, which categorizes stroke subtypes based on etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. This patient likely falls under large artery or cardioembolic stroke pending further vascular imaging. The ASPECTS scoring system is a validated tool to quantify early ischemic changes on CT in the MCA territory and guides eligibility for reperfusion therapies. The classification of stroke has evolved to integrate clinical, radiologic, and etiologic data to optimize management strategies.",
        "classification_and_nosology": "This is a case of acute ischemic stroke, which is categorized by etiology (thrombotic, embolic) and anatomical distribution, with this scenario most consistent with a large vessel occlusion in the MCA territory.",
        "management_principles": "First-line management is intravenous thrombolysis (tPA) if administered within the therapeutic window (currently recommended within 4.5 hours, with greatest benefit within 3 hours) after excluding contraindications such as intracranial hemorrhage. Blood pressure should be maintained below 185/110 mmHg prior to tPA. Endovascular intervention is reserved for patients with large vessel occlusion who may benefit from thrombectomy. In pregnant patients, tPA has been used cautiously when benefits outweigh risks, and in lactating patients tPA is also considered acceptable with appropriate counseling.",
        "option_analysis": "Option A (reduce BP) is incorrect because although the patient is hypertensive, his blood pressure is still below the critical threshold that mandates immediate lowering prior to tPA. Option B (IV thrombolytic) is the correct and time-sensitive treatment. Option C (CTA) is valuable in later planning for endovascular therapy but should not delay the administration of thrombolysis in eligible patients.",
        "clinical_pearls": "1. The therapeutic window for IV tPA is narrow; prompt imaging and treatment initiation are essential. 2. A good ASPECTS score indicates a smaller infarct core, suggesting a greater benefit from reperfusion therapies. 3. Blood pressure management is crucial: avoid unnecessary lowering if BP is below 185/110 mmHg prior to tPA.",
        "current_evidence": "Recent AHA/ASA guidelines continue to support the use of IV thrombolytics in eligible patients within the specified time window, emphasizing rapid treatment to reduce long-term disability. Ongoing research into extended windows for mechanical thrombectomy complements these guidelines without altering the need for immediate tPA in eligible patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993046",
    "fields": {
      "question_number": "218",
      "question_text": "50-year-old transient Rt side weakness, Dx: TIA, Rt ICA 60%, Lt 65% stenosis",
      "options": {
        "A": "(Aspirin alone) is correct because it is the cornerstone of medical management in patients with moderate symptomatic carotid stenosis. Option B (Angioplasty alone) is not standard due to high rates of restenosis and embolic risks. Option C (Dual antiplatelet therapy) is not required for long",
        "D": "(Angioplasty with stenting) is generally reserved for high"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Transient ischemic attacks (TIAs) serve as a warning sign for future stroke and are most often due to emboli from atherosclerotic plaques. In patients with moderate carotid stenosis (60-65%), the focus is on medical management to stabilize the plaque and prevent embolization.",
        "pathophysiology": "TIAs result from transient reductions in cerebral blood flow, often due to emboli from unstable atherosclerotic plaques in the carotid arteries. Platelet aggregation plays a crucial role in the formation and propagation of these emboli.",
        "clinical_correlation": "A 50-year-old patient with a TIA and moderate carotid stenosis typically presents with transient neurological deficits. Since the degree of stenosis is not high-grade (70% or more), the risk of recurrent stroke can be minimized through conservative, medical management.",
        "diagnostic_approach": "Diagnosis includes neurological evaluation, brain imaging (CT or MRI) to exclude infarction, and carotid duplex ultrasonography to quantify the degree of stenosis. Differential diagnoses include small vessel (lacunar) disease and cardioembolic sources, which can be differentiated by additional imaging and cardiac workup.",
        "classification_and_neurology": "Carotid artery disease is classified based on the degree of luminal stenosis and symptomatology. The North American Symptomatic Carotid Endarterectomy Trial (NASCET) method defines percentage stenosis by comparing the narrowest lumen to the distal normal ICA lumen. Patients are categorized as asymptomatic or symptomatic (TIA or stroke ipsilateral to stenosis). Symptomatic carotid stenosis is further stratified into mild (<50%), moderate (50-69%), and severe (\u226570%) stenosis. This classification informs treatment decisions. The disease belongs to the broader category of large artery atherosclerotic cerebrovascular disease within the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification of ischemic stroke subtypes. Classification systems have evolved to incorporate imaging modalities and clinical risk stratification, with ongoing debate regarding optimal cutoffs for intervention. Current consensus supports invasive intervention primarily for symptomatic stenosis \u226570%, with individualized consideration for 50-69%. This patient\u2019s bilateral moderate symptomatic stenosis places him in a nuanced category requiring careful management decisions.",
        "classification_and_nosology": "This condition is classified as a cerebrovascular ischemic event with underlying large vessel atherosclerotic disease. TIAs, by definition, resolve within 24 hours without permanent deficit.",
        "management_principles": "First-line management includes initiating antiplatelet therapy with aspirin to reduce platelet aggregation and the risk of future strokes. Aggressive risk factor modification (control of hypertension, diabetes, dyslipidemia, and smoking cessation) is also essential. Dual antiplatelet therapy may be considered short-term in specific acute cases but is not indicated for long-term management of moderate stenosis. Invasive procedures like carotid stenting or endarterectomy are reserved for high-grade stenosis (\u226570%) or when patients have recurrent symptoms despite optimal medical therapy. For pregnant or lactating women, low-dose aspirin is generally recommended when the benefits outweigh the risks, although the risk\u2013benefit profile must be carefully assessed.",
        "option_analysis": "Option A (Aspirin alone) is correct because it is the cornerstone of medical management in patients with moderate symptomatic carotid stenosis. Option B (Angioplasty alone) is not standard due to high rates of restenosis and embolic risks. Option C (Dual antiplatelet therapy) is not required for long-term management in this scenario because it increases bleeding risk without clear benefit over aspirin monotherapy. Option D (Angioplasty with stenting) is generally reserved for high-grade stenosis (\u226570%) or patients who are poor surgical candidates.",
        "clinical_pearls": "1. Aspirin is the first-line therapy in most TIAs to reduce the risk of stroke. 2. Moderate carotid stenosis (less than 70%) is best managed medically rather than invasively. 3. Aggressive management of vascular risk factors is essential to prevent future cerebrovascular events.",
        "current_evidence": "Current guidelines from the American Stroke Association recommend aspirin monotherapy for patients with symptomatic carotid artery stenosis below 70%. Recent studies continue to validate the safety and efficacy of medical management in these patients while reserving endarterectomy or stenting for those with severe stenosis."
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
