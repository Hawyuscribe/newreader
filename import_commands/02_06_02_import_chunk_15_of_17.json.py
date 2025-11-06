
# Import batch 2 of 3 from chunk_15_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993063",
    "fields": {
      "question_number": "103",
      "question_text": "70 years old male patient with PFO, has DM, HTN, had lacunar stroke in posterior limb of internal capsule, CTA showed extracranial atherosclerosis, what is the treatment:",
      "options": {
        "A": "closure PFO",
        "B": "Aspirin"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This patient presents with a lacunar stroke, most commonly a result of small vessel disease rather than a paradoxical embolism from a patent foramen ovale (PFO). In older patients with vascular risk factors (diabetes, hypertension) and imaging evidence of extracranial atherosclerosis, the stroke is best attributed to intrinsic vascular pathology. Therefore, management is focused on secondary prevention with medical therapy (i.e., antiplatelet agents such as aspirin) rather than interventional closure of a PFO.",
        "pathophysiology": "Lacunar strokes are small, deep infarcts in the brain due to lipohyalinosis or microatheroma of penetrating arteries. Although a PFO can serve as a conduit for paradoxical embolism, in older patients with significant vascular risk factors and extracranial atherosclerosis, the stroke mechanism is more likely due to small vessel disease. The management focus is on preventing further thrombotic events, controlling risk factors, and reducing atherosclerotic progression.",
        "clinical_correlation": "Patients with lacunar strokes may present with pure motor or sensorimotor deficits depending on the location, with the posterior limb of the internal capsule being a classic site. The presence of a PFO in this context is typically incidental, and the finding of significant atherosclerosis on CTA further supports a non-cardioembolic source.",
        "diagnostic_approach": "Imaging modalities such as MRI (to characterize lacunar infarcts) and CTA (to assess extracranial vessels) are used. Differential diagnoses include cardioembolic events (where PFO might be implicated) and large vessel strokes. The presence of atherosclerosis and risk factors helps differentiate a lacunar (small vessel) stroke from PFO-related events.",
        "classification_and_neurology": "The TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system categorizes ischemic strokes into: 1) large artery atherosclerosis, 2) cardioembolism, 3) small vessel occlusion (lacunar), 4) stroke of other determined etiology, and 5) stroke of undetermined etiology. This patient fits the small vessel occlusion category given lacunar infarct and vascular risk factors. PFO would be considered under cardioembolism but is less likely causative here. Extracranial atherosclerosis is a large artery disease but may be asymptomatic or non-significant. The classification guides treatment decisions, emphasizing antiplatelet therapy for small vessel disease and revascularization for symptomatic large artery stenosis. PFO closure is reserved for cryptogenic strokes with embolic features and no alternative cause, especially in younger patients. Current consensus supports individualized classification integrating clinical, imaging, and cardiac evaluation.",
        "classification_and_nosology": "This stroke is classified as an ischemic stroke, specifically a lacunar infarct, which is a subset of small vessel disease. It is distinct from strokes due to embolism from a patent foramen ovale (often seen in younger, cryptogenic strokes) or large artery atherosclerosis leading to territorial infarcts.",
        "management_principles": "Current guidelines recommend antiplatelet therapy (i.e., low-dose aspirin) as first-line secondary prevention in lacunar strokes. Risk factor modification (control of hypertension, diabetes, hyperlipidemia) and lifestyle changes are critical. For patients on antiplatelet therapy, low-dose aspirin is considered safe in pregnancy and lactation when needed for other indications, though its use in stroke prevention is primarily an adult/elderly concern. PFO closure is reserved for select younger patients with cryptogenic strokes in whom no other cause is identified.",
        "option_analysis": "Option A (PFO closure) is not indicated because, in this elderly patient with clear vascular risk factors and imaging evidence of extracranial atherosclerosis, the stroke is more likely due to small vessel disease rather than paradoxical embolism. Option B (Aspirin) is correct as it targets the pathophysiology of small vessel thromboembolism and forms the cornerstone of secondary prevention in lacunar strokes.",
        "clinical_pearls": "1. Lacunar strokes are most often due to small vessel disease related to chronic hypertension and diabetes. 2. PFO closure is generally indicated in younger patients with cryptogenic stroke after thorough evaluation. 3. Extracranial atherosclerosis on imaging reinforces the need for medical management rather than an interventional approach in older individuals.",
        "current_evidence": "Recent trials and stroke management guidelines continue to support the use of antiplatelet therapy for lacunar infarcts along with aggressive risk factor management. Further, evidence has not shown a benefit for PFO closure in older patients with lacunar strokes associated with significant atherosclerosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993064",
    "fields": {
      "question_number": "104",
      "question_text": "patient with asymptomatic extracranial ICA 60% stenosis what is the best treatment:",
      "options": {
        "A": "maximize medical therapy",
        "B": "carotid endarterectomy",
        "C": "carotid stenting."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Asymptomatic carotid stenosis is managed primarily with optimal medical therapy, especially when the degree of stenosis is moderate. A patient with a 60% stenosis, in the absence of symptoms, typically does not warrant surgical intervention because the perioperative risk may outweigh the benefits of carotid revascularization.",
        "pathophysiology": "Extracranial carotid stenosis is most often due to atherosclerotic plaque buildup. The ischemic risk in asymptomatic patients has been reduced substantially due to advancements in medical management, including statin therapy, antihypertensives, and antiplatelet agents.",
        "clinical_correlation": "In asymptomatic patients, the carotid stenosis is detected incidentally or through screening studies. The risk of stroke remains lower compared with symptomatic patients, and medical therapy aims at halting plaque progression and reducing cardiovascular risk.",
        "diagnostic_approach": "Diagnosis is commonly made using carotid duplex ultrasound with confirmation by CTA or MRA if needed. Differential diagnoses for carotid artery disease include dissection, fibromuscular dysplasia, and symptomatic carotid stenosis where associated neurological deficits are present. Distinction is made based on clinical presentation and imaging findings.",
        "classification_and_neurology": "Extracranial carotid artery stenosis is classified based on degree of luminal narrowing, symptom status, and plaque characteristics. The North American Symptomatic Carotid Endarterectomy Trial (NASCET) method is standard for quantifying stenosis percentage. Patients are categorized as asymptomatic or symptomatic based on history of ipsilateral ischemic events. This classification informs treatment guidelines. The disease belongs to the broader category of large artery atherosclerotic cerebrovascular disease under the TOAST classification system for ischemic stroke etiology. Over time, classification systems have evolved to incorporate imaging biomarkers of plaque vulnerability and hemodynamic assessments. Current consensus emphasizes degree of stenosis and symptomatology as primary classifiers, though emerging data on plaque instability may refine future nosology. Controversies remain regarding thresholds for intervention in asymptomatic disease and the role of advanced imaging in risk stratification.",
        "classification_and_nosology": "Carotid artery disease is classified based on the degree of stenosis (mild, moderate, severe) and whether the patient is symptomatic or asymptomatic. Asymptomatic patients with 60% stenosis fall into a moderate category where the risk-benefit ratio favors medical management.",
        "management_principles": "The first-line approach for asymptomatic moderate carotid stenosis is aggressive medical management which includes antiplatelet therapy (e.g., aspirin), statins, lifestyle modification, and meticulous control of hypertension and diabetes. Carotid endarterectomy or stenting is typically reserved for patients with high-grade stenosis (usually >70%) or in select high-risk plaques with additional risk factors. In pregnant or lactating patients, therapeutic decisions must consider the safety profile of medications (low-dose aspirin and statins are managed on a case-by-case basis with risk\u2013benefit discussions).",
        "option_analysis": "Option A (maximize medical therapy) is correct because it aligns with current recommendations for asymptomatic moderate carotid stenosis. Option B (carotid endarterectomy) and Option C (carotid stenting) are typically reserved for patients with symptomatic high-grade stenosis or select high-risk asymptomatic patients, not a 60% lesion.",
        "clinical_pearls": "1. Asymptomatic carotid stenosis up to 60\u201370% is primarily managed with medical therapy. 2. The risk of surgical intervention may not be justified in moderate lesions without symptoms. 3. Regular monitoring and risk factor management are key to preventing stroke in these patients.",
        "current_evidence": "Recent guidelines and research underscore the effectiveness of intensive medical therapy in asymptomatic carotid stenosis, with many studies showing that optimal medical management has improved outcomes and reduced the absolute risk of stroke compared to historical surgical series."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993065",
    "fields": {
      "question_number": "105",
      "question_text": "patient with medial medullary syndrome which artery is affected:",
      "options": {
        "A": "Posterior spinal Artery.",
        "B": "Anterior spinal Artery.",
        "C": "Basilar artery.",
        "D": "PICA"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Medial medullary syndrome, also known as Dejerine syndrome, is characterized by infarction of the medial aspect of the medulla oblongata. The primary vascular supply to this region is provided by the anterior spinal artery or its branches arising from the vertebral artery.",
        "pathophysiology": "Occlusion of the anterior spinal artery leads to ischemia of the medial medulla, affecting the corticospinal tract, medial lemniscus, and hypoglossal nerve nucleus/fibers. This results in a clinical syndrome of contralateral motor weakness and proprioceptive deficits with ipsilateral hypoglossal palsy.",
        "clinical_correlation": "Patients typically present with a combination of contralateral hemiparesis, contralateral loss of proprioception and fine touch, along with an ipsilateral tongue weakness (which may manifest as tongue deviation toward the affected side). Recognizing the vascular territory helps differentiate medial medullary syndrome from lateral medullary (Wallenberg) or other brainstem syndromes.",
        "diagnostic_approach": "Neuroimaging, particularly MRI, is essential to localize the infarct. Differential diagnoses include lateral medullary syndrome (typically due to PICA occlusion) and other brainstem infarcts. The pattern of deficits (especially the involvement of the hypoglossal nerve) helps pinpoint a medial medullary lesion.",
        "classification_and_neurology": "Medial medullary syndrome is classified under brainstem ischemic strokes within the broader category of cerebrovascular diseases. Specifically, it is a subtype of vertebrobasilar territory infarction affecting the medulla. The classification is based on:  - **Anatomical location**: Medulla oblongata - **Vascular territory**: Anterior spinal artery - **Clinical syndrome**: Motor and sensory deficits with cranial nerve involvement  Stroke classification systems such as the TOAST criteria categorize strokes by etiology (large artery atherosclerosis, cardioembolism, small vessel disease), but localization-based classifications are crucial for clinical diagnosis. The syndrome is part of the classic brainstem stroke syndromes, which include lateral medullary syndrome (PICA territory), medial pontine syndrome (paramedian branches of basilar artery), and others. While some controversy exists regarding the exact vascular territories due to anatomical variability, consensus supports ASA involvement in MMS.",
        "classification_and_nosology": "Medial medullary syndrome falls under the category of brainstem strokes and is specifically classified as a lacunar or small vessel stroke when due to occlusion of the paramedian branches of the anterior spinal artery.",
        "management_principles": "Acute management involves standard ischemic stroke protocols (e.g., evaluation for thrombolysis within the appropriate time window if applicable). Secondary prevention with antiplatelet agents and risk factor control (hypertension, diabetes, hyperlipidemia) is essential. In the setting of pregnancy or lactation, management is individualized, with careful consideration of the risks and benefits of thrombolytic therapy and other medications, often necessitating multidisciplinary consultation.",
        "option_analysis": "Option A (Posterior spinal artery) is incorrect because the posterior spinal artery does not primarily supply the medial medulla. Option B (Anterior spinal artery) is correct as it supplies the medial medullary territory. Option C (Basilar artery) typically produces more widespread brainstem symptoms when occluded, and Option D (PICA) is associated with lateral medullary syndrome (Wallenberg syndrome), not medial medullary syndrome.",
        "clinical_pearls": "1. Medial medullary syndrome (Dejerine syndrome) is characterized by contralateral hemiparesis with ipsilateral tongue weakness. 2. The anterior spinal artery is the key vascular supplier to the medial medulla. 3. Differentiating medial versus lateral medullary syndromes is crucial for accurate localization of the lesion.",
        "current_evidence": "Recent neuroimaging advancements have reinforced the understanding of brainstem vascular territories, and current stroke guidelines continue to recommend rapid imaging and supportive care as the cornerstones of management in brainstem strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993066",
    "fields": {
      "question_number": "106",
      "question_text": "patient with acute stroke on dabigatrin for AF, the patient underwent for thrombectomy, the patient developed hemorrhage over MCA territory, what to give:",
      "options": {
        "A": "Vit K.",
        "C": "Idarocizumab."
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Patients on dabigatran, a direct thrombin inhibitor, who develop serious bleeding complications such as intracranial hemorrhage require prompt reversal of its anticoagulant effects. Idarucizumab is a monoclonal antibody fragment that specifically binds dabigatran and reverses its effect rapidly.",
        "pathophysiology": "Dabigatran exerts its anticoagulant effect by directly inhibiting thrombin, thereby preventing fibrin clot formation. In the event of an acute bleeding complication, particularly in the context of an invasive procedure like thrombectomy, the anticoagulant effect can exacerbate hemorrhage. Idarucizumab binds dabigatran with high affinity, neutralizing its anticoagulant activity almost immediately.",
        "clinical_correlation": "In this clinical scenario, the patient developed a hemorrhage over the MCA territory after thrombectomy while on dabigatran for atrial fibrillation. Rapid reversal of dabigatran is critical to control the hemorrhage and prevent further neurological deterioration.",
        "diagnostic_approach": "Evaluating anticoagulant use and coagulation parameters is essential, especially in the setting of hemorrhagic transformation after a revascularization procedure. Differential considerations include bleeding due to procedural complications versus medication-induced coagulopathy. Laboratory tests measuring thrombin time and aPTT can provide additional information but are often not necessary when the clinical situation demands immediate reversal.",
        "classification_and_neurology": "Stroke classification systems such as TOAST categorize ischemic strokes by etiology, with cardioembolic stroke being common in AF. Hemorrhagic transformation is a complication classified radiographically (e.g., hemorrhagic infarction vs. parenchymal hematoma) and clinically (symptomatic vs. asymptomatic). Anticoagulant-related hemorrhages are a subset of intracerebral hemorrhages requiring specific management. Dabigatran belongs to the DOAC family, specifically direct thrombin inhibitors, distinct from vitamin K antagonists like warfarin. Reversal agents are classified by their target: vitamin K for warfarin, idarucizumab for dabigatran, and andexanet alfa for factor Xa inhibitors. Understanding these classifications informs targeted therapy. Contemporary guidelines recognize these distinctions and recommend agent-specific reversal strategies.",
        "classification_and_nosology": "This complication falls under anticoagulant-associated intracerebral hemorrhage. The reversal strategy depends on the specific anticoagulant agent being used. Dabigatran-related bleeding is distinct from warfarin-induced hemorrhage, which is managed with vitamin K and other agents.",
        "management_principles": "According to current guidelines, idarucizumab is the first-line reversal agent for dabigatran-induced bleeding. It is administered intravenously in a fixed dose and provides rapid reversal. Supportive measures, blood pressure control, and neurosurgical consultation may also be necessary. In pregnant or lactating patients, dabigatran is contraindicated; however, in an emergency situation with inadvertent exposure, the use of idarucizumab should be weighed against the potential risks and benefits in a multidisciplinary setting, although data in this population remain limited.",
        "option_analysis": "Option A (Vitamin K) is used for reversing warfarin but has no effect on dabigatran. Option C (Idarucizumab) is correct as it is the specific reversal agent indicated for dabigatran-associated bleeding. Options B and D are not provided or relevant in this scenario.",
        "clinical_pearls": "1. Always confirm the specific anticoagulant agent when managing a bleeding complication \u2013 dabigatran reversal is achieved with idarucizumab, not vitamin K. 2. Idarucizumab acts rapidly, which is critical in life-threatening hemorrhages such as intracerebral bleeding. 3. Knowing the reversal agents for different anticoagulants is essential in acute stroke management.",
        "current_evidence": "Recent studies and updated guidelines support the use of idarucizumab in dabigatran-associated bleeding. Its rapid action helps to minimize hemorrhagic progression and improve clinical outcomes. Ongoing research continues to monitor long-term outcomes in patients reversed with idarucizumab, especially regarding intracranial hemorrhages."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993067",
    "fields": {
      "question_number": "107",
      "question_text": "patient with perimesencephalic SAH, angiogram done 2 times was normal, what to do next:",
      "options": {
        "A": "send home",
        "B": "repeat digital subtraction angiogram"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Perimesencephalic subarachnoid hemorrhage (SAH) is a distinct, non-aneurysmal type of SAH characterized by bleeding localized around the midbrain. Its recognition is based on a characteristic CT appearance and the absence of aneurysms on angiography.",
        "pathophysiology": "The precise mechanism remains uncertain, but it is believed that a venous bleed from small perimesencephalic vessels is responsible. Unlike aneurysmal SAH, these hemorrhages rarely rebleed or lead to vasospasm, contributing to a more benign clinical course when high\u2010quality angiographic studies are negative.",
        "clinical_correlation": "Patients typically present with sudden onset headache, often described as severe and \u2018thunderclap\u2019 in nature, yet they tend to have a lower rate of complications compared to aneurysmal SAH. The negative repeated angiographic evaluations confirm the diagnosis and reassure both the clinician and the patient.",
        "diagnostic_approach": "After a CT scan demonstrates a hemorrhage confined to the perimesencephalic cisterns, the next step is vascular imaging. Both computed tomography angiography (CTA) and digital subtraction angiography (DSA) are used to exclude aneurysms. Differential diagnoses include aneurysmal SAH, traumatic SAH, and other causes of non-aneurysmal hemorrhage. The typical distribution on CT and the absence of aneurysms on two independent studies help differentiate perimesencephalic SAH from other types.",
        "classification_and_neurology": "PMSAH is classified under non-aneurysmal subarachnoid hemorrhages, a subset of spontaneous SAH. The broader classification of SAH distinguishes between traumatic and spontaneous causes, with spontaneous SAH further divided into aneurysmal and non-aneurysmal. Within non-aneurysmal SAH, PMSAH is differentiated by its characteristic hemorrhage pattern and angiographic negativity. The Fisher scale, which grades SAH based on CT blood amount and distribution, helps predict vasospasm risk but is less applicable to PMSAH due to its limited blood volume. The World Federation of Neurosurgical Societies (WFNS) grading system applies to clinical severity but again, PMSAH patients often present with low grades. Historically, PMSAH was recognized as a distinct entity in the 1980s, and consensus now supports conservative management due to its benign nature. Some debate exists about the need for repeated angiography, but current nosology emphasizes clinical and radiographic criteria for diagnosis.",
        "classification_and_nosology": "Subarachnoid hemorrhage can be classified into aneurysmal and non-aneurysmal types. Perimesencephalic SAH falls under the non-aneurysmal category, distinguished by its typical bleed pattern and benign prognosis.",
        "management_principles": "The management of perimesencephalic SAH is conservative and supportive. Guidelines recommend observation, control of pain, blood pressure monitoring, and management for any complications that may arise (such as hydrocephalus or rare vasospasm). Once two high\u2010quality angiograms are negative and the patient remains stable, no further invasive vascular studies are necessary. In terms of pregnancy and lactation, supportive treatments are used while avoiding medications that could adversely affect the fetus, with careful monitoring and observation being key.",
        "option_analysis": "Option A (send home) is correct provided that the patient has been adequately observed in the hospital, all imaging (including at least two angiograms) is negative, and the clinical course is stable. Option B (repeat digital subtraction angiogram) is not warranted due to the high level of confidence already established with the previous angiograms.",
        "clinical_pearls": "1. Perimesencephalic SAH is associated with a benign course and very low risk of rebleeding. 2. Two negative angiographic studies in the appropriate CT pattern generally obviate the need for further invasive testing.",
        "current_evidence": "Recent studies and guidelines support a conservative approach to perimesencephalic SAH. With advances in CT imaging and high-quality angiographic techniques, the benign nature of this hemorrhage is well recognized, leading to safe early discharge after a period of observation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993068",
    "fields": {
      "question_number": "108",
      "question_text": "female patient presented with hx of flashing in the right eye, then she had right homonymous hemianopia, then left side weakness over 45min, the patient during her way she had headache. CT brain, CTA including DWI all normal, improved after s:",
      "options": {
        "A": "hemiplegic migraine.",
        "B": "TIA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Hemiplegic migraine is a rare variant of migraine with aura that includes motor weakness alongside visual or sensory disturbances. It can mimic transient ischemic attacks (TIA) or strokes, making a detailed clinical history essential for correct diagnosis.",
        "pathophysiology": "The mechanism involves cortical spreading depression, which leads to transient neuronal hyperexcitability followed by inhibition. This phenomenon not only causes the typical visual and sensory auras but can also affect motor areas of the cortex, leading to transient hemiparesis. Genetic factors may also play a role in familial forms.",
        "clinical_correlation": "Patients with hemiplegic migraine often experience a progression of symptoms: visual aura (such as flashing lights), followed by sensory or motor deficits (like hemianopia or hemiparesis), and then headache. The gradual and spreading nature of the aura, along with the subsequent headache, distinguishes it from TIA, which usually presents more abruptly and often lacks a migrainous headache.",
        "diagnostic_approach": "The workup includes a detailed headache history, a neurological examination, and neuroimaging studies. In migraine aura, imaging studies such as CT, CTA, and DWI are typically normal, especially once the episode has resolved. Differential diagnoses include TIA/stroke, which tend to have more abrupt onset, risk factors like hypertension or atrial fibrillation, and may show DWI abnormalities if infarction occurs.",
        "classification_and_neurology": "Hemiplegic migraine is classified under migraine with aura in the International Classification of Headache Disorders (ICHD-3) with two subtypes: familial hemiplegic migraine (FHM) and sporadic hemiplegic migraine (SHM). It is a rare migraine variant characterized by motor aura. TIA is classified under cerebrovascular diseases by the American Heart Association/American Stroke Association (AHA/ASA) as a transient episode of neurological dysfunction caused by focal brain ischemia without acute infarction. The distinction between TIA and migraine aura is critical due to differing management. Over time, classification systems have evolved to incorporate imaging findings; for example, the tissue-based definition of TIA requires absence of infarction on MRI. Controversy exists in differentiating prolonged aura from stroke mimics, emphasizing clinical context and imaging.",
        "classification_and_nosology": "Hemiplegic migraine is classified under migraine with aura in the International Classification of Headache Disorders. It is divided into familial and sporadic forms, with the familial form having an autosomal dominant pattern in some cases.",
        "management_principles": "Acute management focuses on symptom relief and may include analgesics and antiemetics. Specific migraine abortive therapies that cause vasoconstriction, such as triptans and ergot derivatives, are contraindicated in hemiplegic migraine. Prophylactic treatments may be considered in frequent or severe cases. In pregnancy and lactation, treatment options are limited; typically, acetaminophen is preferred for pain control and non-pharmacologic measures are emphasized.",
        "option_analysis": "Option A (hemiplegic migraine) is the correct diagnosis because the patient\u2019s progression\u2014starting with visual phenomena (flashing lights), evolving into a homonymous hemianopia and motor weakness, and followed by headache\u2014fits the pattern of a migrainous aura rather than a vascular TIA. Option B (TIA) is less likely given the clear migrainous features and the normal imaging studies.",
        "clinical_pearls": "1. Hemiplegic migraine can closely mimic TIA; however, the gradual onset and evolution of symptoms with a subsequent headache are key distinguishing features. 2. Imaging studies (CT, CTA, DWI) are typically normal in migrainous phenomena once the event has resolved.",
        "current_evidence": "Contemporary guidelines stress the importance of distinguishing migraine aura from cerebrovascular events, as misdiagnosis can lead to inappropriate treatments. Advances in neuroimaging and a better understanding of migraine pathophysiology have helped clarify this differentiation, guiding clinicians towards safer, more appropriate management strategies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993069",
    "fields": {
      "question_number": "109",
      "question_text": "patient presented with acute stroke on warfarin CT showed ICH, INR=5, the patient received prothrombin complex, what to add for him:",
      "options": {
        "A": "Vit K",
        "B": "FFP."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Warfarin-induced hemorrhage, especially intracerebral hemorrhage (ICH), is a life-threatening complication that requires rapid reversal of anticoagulation to stop the bleeding and prevent further intracranial damage.",
        "pathophysiology": "Warfarin works by inhibiting vitamin K\u2013dependent clotting factors (II, VII, IX, and X). An elevated International Normalized Ratio (INR) indicates an increased bleeding risk. In cases of ICH, rapid reversal is achieved by replenishing these factors via prothrombin complex concentrate (PCC) and by providing vitamin K to allow for synthesis of new clotting factors.",
        "clinical_correlation": "The patient\u2019s presentation with ICH on a background of warfarin use and an elevated INR (5) is a classic scenario where reversal of coagulation is the priority. PCC works rapidly to replace clotting factors while vitamin K ensures a more sustained reversal effect, preventing re-accumulation of the anticoagulant effect.",
        "diagnostic_approach": "In a warfarin-associated ICH, history and laboratory studies (INR measurement) are crucial. CT imaging is used to identify and assess the extent of hemorrhage. Differential diagnoses include spontaneous ICH from hypertension and other coagulopathies, but the history of warfarin use and an elevated INR direct the diagnosis.",
        "classification_and_neurology": "Warfarin-associated ICH falls under the broader category of hemorrhagic stroke, specifically anticoagulant-associated intracerebral hemorrhage. Stroke classification systems, such as the TOAST classification, primarily address ischemic stroke subtypes but acknowledge hemorrhagic stroke as a distinct entity. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify anticoagulant-associated ICH as a high-risk hemorrhagic stroke requiring specialized management. This condition is further subclassified based on the causative anticoagulant (vitamin K antagonists, direct oral anticoagulants, etc.) and the severity of coagulopathy, guiding tailored reversal strategies. Understanding this classification aids in prognosis and therapeutic decisions.",
        "classification_and_nosology": "Warfarin-associated ICH is categorized as an anticoagulant-related hemorrhage, which is managed differently from non-anticoagulant hemorrhages due to the need for rapid reversal of the coagulopathy.",
        "management_principles": "The latest guidelines recommend the immediate reversal of warfarin in ICH patients using PCC combined with intravenous vitamin K (typically 5\u201310 mg IV slow push). PCC provides immediate replacement of clotting factors, while vitamin K allows the body to produce new factors over the ensuing hours. Fresh frozen plasma (FFP) may be considered only if PCC is not available because it has a slower preparation time and higher volume, which may be problematic. In pregnancy and lactation, vitamin K is safe and the reversal strategy remains similar, though clinicians must balance the risks and benefits carefully.",
        "option_analysis": "Option A (Vitamin K) is correct as an addition to PCC to ensure sustained correction of the warfarin-induced coagulopathy. Option B (FFP) is less ideal when PCC is already given because of its slower effect and risk profile, though it may be used when PCC is unavailable.",
        "clinical_pearls": "1. In warfarin-related ICH, rapid reversal of the coagulopathy is critical to reducing hematoma expansion. 2. Using PCC in conjunction with vitamin K is the recommended strategy for effective and sustained reversal.",
        "current_evidence": "Recent guidelines from agencies like the American Heart Association (AHA) and the Neurocritical Care Society endorse the combination of PCC and vitamin K for warfarin reversal. Emerging evidence has shown superior outcomes with PCC use compared to FFP, with faster correction of INR and reduced complications."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_7.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993070",
    "fields": {
      "question_number": "110",
      "question_text": "45 years old with hx of migraine 15 years ago, developed TIA, his father has stroke. MRI involving the anterior temporal lobe, what to do next:",
      "options": {
        "A": "NOTCH 3"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy (CADASIL) is a hereditary small vessel disease characterized by migraine (often with aura), recurrent TIAs or strokes, and personality changes. The anterior temporal lobe involvement on MRI is a classic radiographic clue.",
        "pathophysiology": "CADASIL results from mutations in the NOTCH3 gene, which encodes a receptor important for vascular smooth muscle function. Mutated proteins accumulate in the vessel walls, leading to degeneration of vascular smooth muscle cells and subsequent ischemic changes in the white matter.",
        "clinical_correlation": "The patient\u2019s history of migraine, a recent TIA, and a family history of stroke, along with MRI findings involving the anterior temporal lobe, are all highly suggestive of CADASIL. This condition often presents in mid-adulthood with transient ischemic events and subcortical white matter changes.",
        "diagnostic_approach": "Diagnosis is primarily based on clinical suspicion supported by MRI findings. The involvement of the anterior temporal lobes and external capsules are distinguishing radiologic features. Confirmation is achieved through genetic testing for NOTCH3 mutations. Differential diagnoses include other small vessel ischemic diseases and demyelinating conditions, but the unique MRI pattern and family history point towards CADASIL.",
        "classification_and_neurology": "CADASIL falls under the category of hereditary cerebral small vessel diseases (CSVD), which are a subset of cerebrovascular disorders. The current classification of CSVD includes: - Sporadic forms: primarily related to aging and vascular risk factors - Hereditary forms: monogenic disorders such as CADASIL (NOTCH3 mutation), CARASIL (HTRA1 mutation), COL4A1-related angiopathies, and others  CADASIL is classified as an autosomal dominant arteriopathy with subcortical infarcts and leukoencephalopathy. This classification is based on genetic etiology, clinical phenotype, and neuroimaging features. Over time, advances in genetics have refined nosology, distinguishing CADASIL from other hereditary and sporadic small vessel diseases. There is consensus that CADASIL is the prototypical hereditary CSVD, serving as a model for understanding pathophysiology and clinical management. Controversies remain regarding phenotypic variability and the role of modifying factors.",
        "classification_and_nosology": "CADASIL is classified as a hereditary cerebral small vessel disease. It is the most common form of hereditary stroke disorder and is inherited in an autosomal dominant pattern.",
        "management_principles": "There is no definitive cure for CADASIL; management is focused on controlling vascular risk factors, preventing stroke recurrence, and symptomatic treatment of migraines. Antiplatelet therapy is often used for secondary prevention in TIA/stroke, though evidence is limited. Genetic counseling is essential, especially when considering family planning. During pregnancy and lactation, treatment is largely supportive and focuses on minimizing stroke risk while avoiding medications that could adversely affect the fetus or infant.",
        "option_analysis": "Option A (NOTCH 3) is correct because the presence of anterior temporal lobe involvement on MRI in a patient with migraine and stroke, along with a family history, strongly points towards CADASIL, which is linked to NOTCH3 gene mutations. Other options (B, C, D) are not provided or relevant in this context.",
        "clinical_pearls": "1. Anterior temporal lobe hyperintensities on MRI are a hallmark of CADASIL. 2. A history of migraine with aura combined with a family history of stroke in a relatively young patient should prompt consideration of a genetic small vessel disease like CADASIL.",
        "current_evidence": "Recent research continues to refine our understanding of CADASIL\u2019s genetic underpinnings. Latest guidelines emphasize the importance of MRI patterns and genetic testing for early diagnosis. While no disease-modifying treatment exists, ongoing studies are exploring potential therapeutic targets aimed at mitigating vascular smooth muscle dysfunction."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993071",
    "fields": {
      "question_number": "111",
      "question_text": "female patient taking OCP, had CVT, thrombophilia work up was -ve, for how long to be on anticoagulation:",
      "options": {
        "A": "life long.",
        "B": "3-6 months"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral venous thrombosis (CVT) is a cerebrovascular disorder where thrombosis develops in the dural venous sinuses or cerebral veins. It can be provoked by transient factors such as oral contraceptive (OCP) use, pregnancy, or other reversible hypercoagulable states.",
        "pathophysiology": "OCPs increase the risk of thrombosis by inducing a hypercoagulable state, likely through estrogen\u2010mediated changes in coagulation factors. In a provoked CVT (with a negative thrombophilia workup) the underlying trigger is removable, leading to a lower recurrence risk once the agent is discontinued. The thrombus impedes venous outflow, increasing venous pressure, and causing edema and possibly hemorrhagic infarction.",
        "clinical_correlation": "Patients with CVT often present with headache, focal neurological deficits, seizures, and papilledema. When CVT is associated with a transient trigger \u2013 such as OCP use \u2013 the overall prognosis is favorable if the causal factor is eliminated.",
        "diagnostic_approach": "CVT is typically diagnosed via imaging such as CT venography or MR venography. Differential diagnoses include arterial stroke, intracranial hemorrhage, and idiopathic intracranial hypertension. Detailed history regarding risk factors (like OCP use) helps differentiate it from other causes of cerebrovascular events.",
        "classification_and_neurology": "CVT is classified under cerebrovascular diseases, specifically as a venous stroke subtype distinct from arterial ischemic stroke and hemorrhagic stroke. The International Classification of Headache Disorders (ICHD) also recognizes CVT-related headache as secondary headache attributed to intracranial vascular disorder. Regarding anticoagulation duration, guidelines classify CVT patients based on risk factors: (1) transient provoking factors (e.g., OCP use), (2) unprovoked CVT, and (3) CVT with persistent thrombophilia or recurrent events. This classification guides therapy duration. The current consensus from stroke societies such as the American Heart Association/American Stroke Association (AHA/ASA) reflects this stratification, emphasizing individualized management.",
        "classification_and_nosology": "CVT can be classified based on etiology into provoked (transient risk factor like OCP use) versus unprovoked (persistent thrombophilic states). This classification guides the duration of anticoagulation therapy.",
        "management_principles": "Current guidelines recommend initial treatment with heparin (often low molecular weight heparin) followed by oral anticoagulation for 3-6 months in cases of provoked CVT. In women with OCP-related CVT, discontinuation of the OCP is imperative. For pregnant patients, LMWH is preferred given warfarin\u2019s teratogenicity; in lactating patients, warfarin can be used safely as minimal amounts are excreted in breast milk. Lifelong anticoagulation is reserved for patients with recurrent events or proven thrombophilia.",
        "option_analysis": "Option A (lifelong) is not indicated because the CVT in this case is provoked by a reversible risk factor (OCP use) with a negative thrombophilia workup. Option B (3-6 months) is correct, as the standard duration for anticoagulation in a provoked CVT is typically 3-6 months.",
        "clinical_pearls": "1. Always consider OCP use as a reversible risk factor in CVT. 2. Provoked CVT usually requires a finite course of anticoagulation (3-6 months) rather than lifelong therapy.",
        "current_evidence": "Recent guidelines, including those from the AHA/ASA, support a 3-6 month duration of anticoagulation in cases of provoked CVT. Ongoing research continues to refine risk stratification and duration based on individual patient factors and imaging findings."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993072",
    "fields": {
      "question_number": "112",
      "question_text": "patient over 1 day he has symptoms of vertigo & ataxia, CT shown: there was left cerebellar hypodensity, midline shift & crowding of the posterior fossa, what to do next:",
      "options": {
        "A": "start Aspirin.",
        "B": "Give tPA",
        "C": "consult neurosurgery",
        "D": "admit ICU & monitor ICP"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Cerebellar infarcts, especially when extensive, can lead to mass effect in the confined space of the posterior fossa. The posterior fossa is a tight skull compartment containing the brainstem and cerebellum, making any swelling a potential neurosurgical emergency.",
        "pathophysiology": "Infarction of the cerebellum results in cerebral edema due to cytotoxic swelling. This edema can cause a mass effect with midline shift and crowding of the posterior fossa, which increases intracranial pressure and risks brainstem compression.",
        "clinical_correlation": "Patients with cerebellar infarcts may present with vertigo, ataxia, nausea, vomiting, and may deteriorate rapidly if brainstem compression ensues. The presence of midline shift and crowding indicates a higher risk of herniation.",
        "diagnostic_approach": "Noncontrast CT is typically used to diagnose a cerebellar infarct and assess for associated mass effect. Differential diagnoses include cerebellar hemorrhage, neoplasm, or abscess. Distinguishing features on imaging and the clinical setting help differentiate these conditions.",
        "classification_and_neurology": "Cerebellar strokes fall under the broader category of ischemic strokes affecting the posterior circulation territory. The TOAST classification system categorizes strokes by etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.), but management considerations also depend on anatomical factors such as infarct size and mass effect. Acute cerebellar infarcts are classified by infarct location (superior, anterior inferior, posterior inferior cerebellar arteries) and by presence or absence of complications like edema and hydrocephalus. Recognition of mass effect places the stroke in a high-risk subgroup necessitating neurosurgical evaluation.",
        "classification_and_nosology": "Cerebellar infarcts are categorized by the vascular territory involved. The severity is further classified by the extent of edema and mass effect, which guides management decisions.",
        "management_principles": "Given the mass effect, the immediate management of a cerebellar infarct with midline shift and posterior fossa crowding is neurosurgical evaluation. Surgical interventions, such as suboccipital decompressive craniectomy, may be needed. Medical management may include admission to the ICU for close neurological monitoring, but tPA is contraindicated in this setting, especially beyond the typical window and in the presence of mass effect. In pregnant patients, neurosurgical interventions require special anesthetic considerations, and imaging protocols may be adjusted to minimize fetal exposure; management remains urgent. Similar principles apply in lactation, with attention to medication safety.",
        "option_analysis": "Option A (start Aspirin) and Option B (Give tPA) are inappropriate given the patient's imaging findings and timing relative to symptom onset. Option D (admit ICU & monitor ICP) is supportive but insufficient as a standalone measure when significant mass effect is present. Option C (consult neurosurgery) is the correct and definitive step given the urgency of mass effect in the posterior fossa.",
        "clinical_pearls": "1. Significant cerebellar edema with midline shift mandates early neurosurgical consultation to prevent brainstem compromise. 2. Thrombolytic therapy (tPA) is contraindicated outside the treatment window and in patients with mass effect.",
        "current_evidence": "Recent stroke management guidelines emphasize the need for rapid neurosurgical assessment in patients with cerebellar infarctions showing signs of mass effect. Studies have shown that early decompressive surgery can be life-saving in select patients."
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
