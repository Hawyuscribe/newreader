
# Import batch 1 of 3 from chunk_1_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99992972",
    "fields": {
      "question_number": "176",
      "question_text": "Patient with acute stroke brain MRI found dorsal cerebellar infarction (superior cerebellar artery) what will you find in exam:",
      "options": {
        "A": "Ipsilateral truncal Hyperalgesia",
        "B": "Ipsilateral Horner",
        "C": "Hearing loss"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Infarction in the superior cerebellar artery (SCA) territory typically affects the dorsal portion of the cerebellum \u2013 often the vermis and adjacent hemispheric regions \u2013 which are responsible for coordinating balance and gait. Classically, lesions in the midline (vermal) cerebellum produce ipsilateral deficits in truncal stability.",
        "pathophysiology": "The SCA supplies blood to the superior surface of the cerebellum. An infarct in this region disrupts the neural circuitry that modulates coordinated movement and balance. Although the clinical hallmark in a vermian stroke is truncal ataxia (impaired balance and unstable gait), the exam option is written as 'ipsilateral truncal hyperalgesia'. This appears to be a misnomer or typographical error because hyperalgesia (an increased pain response) is not a typical finding in cerebellar strokes. The expected finding is impaired coordination (eg, truncal ataxia) on the same side as the lesion.",
        "clinical_correlation": "Patients with dorsal (vermal) cerebellar infarctions usually present with imbalance and difficulty maintaining an erect posture. They may demonstrate a wide\u2010based, staggering gait and show dysmetria (misjudging distances) on finger\u2013nose testing on the same side as the infarct. These findings directly reflect the impaired processing in the cerebellum that is important for postural control.",
        "diagnostic_approach": "The diagnosis hinges on high\u2010resolution imaging, most commonly MRI with diffusion\u2010weighted imaging (DWI), which will reveal an infarct in the superior cerebellar artery territory. Differential diagnoses to consider include infarcts in other cerebellar vascular territories (eg, posterior inferior cerebellar artery [PICA] infarct causing lateral medullary syndrome, which may include additional brainstem findings) and lesions that affect sensory pathways. Careful comparison of clinical findings and imaging localization is essential.",
        "classification_and_neurology": "Superior cerebellar artery infarction is classified under ischemic strokes within the posterior circulation stroke subgroup. Posterior circulation strokes involve vertebrobasilar arterial territories, including the SCA, PICA, AICA, and basilar artery branches. The TOAST classification system categorizes ischemic strokes by etiology (e.g., large artery atherosclerosis, cardioembolism, small vessel disease), which guides management. SCA infarcts are typically embolic or atherothrombotic. This infarct is part of the broader family of cerebellar strokes, which differ in vascular supply and clinical presentation. While PICA infarcts often produce lateral medullary syndrome, and AICA infarcts cause hearing loss and facial weakness, SCA infarcts have a distinct pattern involving superior cerebellum and midbrain structures. Consensus on classification emphasizes vascular territory localization combined with etiological subtype.",
        "classification_and_nosology": "Cerebellar strokes are classified by the arterial territory involved \u2013 SCA, anterior inferior cerebellar artery (AICA), or PICA. An SCA infarct is part of the overall ischemic stroke subtypes and is characterized by ipsilateral cerebellar findings. When the vermis is involved, truncal instability is a classic sign.",
        "management_principles": "Acute management follows standard ischemic stroke protocols: rapid assessment for thrombolytic eligibility (if within the therapeutic time window), control of blood pressure and blood sugar, and antiplatelet therapy once appropriate. Rehabilitation focusing on balance and coordination is key. In cases where thrombolysis is indicated in a pregnant or lactating patient, a careful risk\u2010benefit analysis is essential; current guidelines support thrombolytic therapy if benefits outweigh risks, with appropriate monitoring and counseling.",
        "option_analysis": "Option A: Ipsilateral truncal hyperalgesia \u2013 Incorrect. Hyperalgesia (increased pain sensitivity) involving the trunk is characteristic of lesions affecting the spinothalamic tract in the lateral medulla, typically seen in PICA infarcts (Wallenberg syndrome). SCA territory infarcts spare these sensory pathways.  Option B: Ipsilateral Horner syndrome \u2013 Correct. The descending sympathetic fibers run through the lateral midbrain near the superior cerebellar peduncle. Infarction here disrupts these fibers, causing ipsilateral Horner syndrome (ptosis, miosis, anhidrosis). This is a hallmark sign supporting SCA territory involvement.  Option C: Hearing loss \u2013 Incorrect. Hearing loss results from infarction of the AICA territory, which supplies the internal auditory artery and cochlear nuclei. The SCA does not supply auditory pathways; thus, hearing loss is not expected in SCA infarcts.  Discriminating features: Horner syndrome localizes the lesion to the lateral brainstem, specifically implicating the SCA territory, whereas hearing loss points to AICA infarction, and truncal hyperalgesia suggests PICA involvement.",
        "clinical_pearls": "- **Remember the vascular territories:** AICA infarcts cause hearing loss, PICA infarcts cause lateral medullary syndrome (including sensory deficits), and SCA infarcts cause ipsilateral ataxia plus Horner syndrome. - **Horner syndrome in stroke localizes to lateral brainstem:** Disruption of descending sympathetic fibers in the lateral midbrain or pons. - **Cerebellar signs are ipsilateral due to double crossing:** Cerebellar output crosses twice, resulting in ipsilateral deficits. - **Early MRI with DWI is essential:** It detects acute posterior circulation infarcts better than CT. - **Monitor for cerebellar edema:** Large infarcts can cause mass effect and hydrocephalus. - Use the mnemonic \"H-A-H\" for SCA infarct features: **H**orner syndrome, **A**taxia, **H**emiparesis (if corticospinal tract involved).",
        "current_evidence": "The 2019 AHA/ASA Guidelines for the Early Management of Patients With Acute Ischemic Stroke state: \"Patients with posterior circulation stroke should be managed according to the same principles as anterior circulation stroke, including timely reperfusion therapy when indicated\" (Powers et al., 2019). However, they note that clinical diagnosis can be challenging due to varied presentations. Current evidence supports MRI-DWI as the diagnostic gold standard for posterior circulation strokes, including SCA infarcts. There remain knowledge gaps in optimal management of small vessel occlusions in the SCA territory and the role of thrombectomy in distal small vessels. Emerging research on advanced imaging and neuroprotective strategies continues to evolve. Controversies include the best approach to monitoring and surgical intervention for cerebellar infarcts with edema. Recent advances emphasize multidisciplinary stroke care and individualized rehabilitation to improve functional outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_6.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992973",
    "fields": {
      "question_number": "177",
      "question_text": "Patient with polycystic kidney disease with history suggestive of SAH:",
      "options": {
        "A": "AVM",
        "B": "Intracranial aneurysm"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Autosomal dominant polycystic kidney disease (ADPKD) is commonly associated with the development of berry (saccular) aneurysms. Patients with ADPKD are at an increased risk for intracranial aneurysms, which may rupture and cause subarachnoid hemorrhage (SAH). This fundamental linkage is critical in understanding the neurologic risk profile in ADPKD.",
        "pathophysiology": "ADPKD involves mutations that not only lead to renal cyst formation but also affect the integrity of vascular structures, particularly the walls of cerebral arteries. This predisposition results in the formation of saccular or berry aneurysms, which are prone to rupture due to their inherent structural weakness, leading to SAH.",
        "clinical_correlation": "When a patient with ADPKD presents with signs suggestive of SAH (e.g., sudden severe headache, neck stiffness, altered mental status), an intracranial aneurysm should be highly suspected. The clinical scenario ties the known association between ADPKD and berry aneurysms with the high clinical risk of SAH.",
        "diagnostic_approach": "Initial evaluation of suspected SAH often involves a non-contrast CT scan to identify bleeding. If SAH is detected, further evaluation with CT angiography or digital subtraction angiography is indicated to identify aneurysms. A detailed family history and screening in high-risk patients are also recommended.",
        "classification_and_neurology": "SAH is classified etiologically as traumatic or non-traumatic (spontaneous). Spontaneous SAH is further subclassified by cause: aneurysmal, perimesencephalic, AVM-related, or other rare causes. Intracranial aneurysms, particularly saccular (berry) aneurysms, belong to the category of cerebrovascular malformations and are the predominant cause of non-traumatic SAH. AVMs are congenital vascular malformations characterized by nidus formation and direct arteriovenous shunting. The International Classification of Diseases (ICD) and stroke classification systems (e.g., TOAST) categorize SAH under hemorrhagic strokes, with aneurysmal SAH as a distinct subtype. The relationship between ADPKD and aneurysmal SAH is well established, whereas AVMs are not typically linked to PKD. Nosological clarity assists in guiding diagnostic workup and management.",
        "classification_and_nosology": "Intracranial aneurysms, specifically berry aneurysms, are classified under vascular malformations that affect the intracranial circulation. They are distinct from arteriovenous malformations (AVMs), which have different etiologies and clinical presentations.",
        "management_principles": "The management of an intracranial aneurysm in the context of SAH includes urgent neurosurgical evaluation for either endovascular coiling or surgical clipping to prevent rebleeding. For pregnant or lactating women, management must be carefully tailored: non-contrast imaging modalities or low-dose radiation techniques are preferred, and multidisciplinary consultation is vital to balance maternal and fetal risks. Guidelines emphasize the importance of prompt intervention regardless of pregnancy status if SAH is suspected.",
        "option_analysis": "Option A (AVM) is not the typical association with ADPKD, as AVMs represent a different vascular pathology. With options C and D absent or unspecified, the complete clinical picture strongly favors option B (Intracranial aneurysm) due to its well-established association with polycystic kidney disease and SAH.",
        "clinical_pearls": "In patients with ADPKD, always consider a high index of suspicion for berry aneurysms, especially when presentation is consistent with SAH. Early neuroimaging, prompt diagnosis, and timely intervention can be lifesaving. Tailor management strategies in special populations, such as pregnant or lactating patients, to minimize risks.",
        "current_evidence": "Current research and clinical guidelines support regular screening for intracranial aneurysms in high-risk ADPKD patients. Recently updated clinical protocols advocate for early intervention when aneurysms are identified, emphasizing safety considerations in special populations such as pregnant and lactating women."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992974",
    "fields": {
      "question_number": "178",
      "question_text": "Patient with acute stroke in the left occipital lobe what will you see in his visual fields:",
      "options": {
        "A": "Congruent homonymous hemianopia with macular sparing",
        "B": "Incongruent homonymous hemianopia with macular sparing",
        "C": "Non-Macular sparing with congruent homonymous hemianopia",
        "D": "Non-Macular sparing with incongruent homonymous hemianopia"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "The visual pathways extend from the retina, through the optic nerves, chiasm, and tracts to the lateral geniculate nucleus, then via the optic radiations to the primary visual cortex in the occipital lobe. Lesions in the occipital cortex, particularly those affecting the primary visual area, typically produce a homonymous hemianopia that is highly congruous (i.e., similar defects in both eyes). Due to dual blood supply to the macular region (from both the posterior cerebral artery and middle cerebral artery), macular sparing is frequently seen in occipital lobe strokes.",
        "pathophysiology": "An infarct in the left occipital lobe (often due to occlusion of the posterior cerebral artery) leads to ischemia of the visual cortex. The central (macular) region often remains partially perfused by collateral vessels, resulting in preserved central vision despite a loss of peripheral vision in the corresponding contralateral visual field.",
        "clinical_correlation": "Patients with a left occipital lobe stroke typically present with a right homonymous hemianopia. The degree of congruity (i.e., how similar the visual field defects are between the two eyes) is high because the lesion is confined to the primary visual cortex, and the macular sparing occurs due to collateral vascular supply. This presentation helps differentiate occipital lobe lesions from those affecting the optic radiations, which may produce less congruent deficits.",
        "diagnostic_approach": "Evaluation begins with a meticulous visual field examination (such as confrontation testing followed by automated perimetry, e.g., Humphrey Visual Field testing) to characterize the type and extent of visual loss. Neuroimaging, particularly brain MRI with diffusion-weighted imaging, is crucial to localize the infarct in the occipital lobe. Differential diagnoses include lesions affecting the optic radiations (which might show less congruity) or optic nerve pathology (which would present with unilateral findings).",
        "classification_and_neurology": "Visual field defects are classified based on lesion location and characteristics. Homonymous hemianopias are subdivided into congruent and incongruent types. Occipital lobe strokes fall under ischemic cerebrovascular accidents affecting the posterior cerebral artery territory. The classification of visual field defects aligns with neuro-ophthalmological nosology, distinguishing lesions as pre-chiasmal, chiasmal, or post-chiasmal. Post-chiasmal lesions include optic tract, lateral geniculate nucleus, optic radiations, and occipital cortex lesions. The concept of macular sparing is a recognized clinical subtype within occipital lobe infarcts. Over time, classification has evolved with advances in imaging and understanding of vascular territories. Current consensus emphasizes lesion localization by combining clinical and imaging data, with macular sparing remaining a hallmark of occipital cortical involvement. Some controversy exists regarding the precise vascular anatomy underlying macular sparing, but the dual blood supply theory is widely accepted.",
        "classification_and_nosology": "Visual field defects are classified based on laterality (homonymous vs. heteronymous), congruity (how similar the defects are between the two eyes), and whether the macula is spared. Occipital lobe infarcts typically cause a congruent homonymous hemianopia with macular sparing, distinguishing them from lesions in the optic radiations or prechiasmal lesions.",
        "management_principles": "The management of an acute occipital stroke involves emergent evaluation for reperfusion therapies, such as intravenous thrombolytics (tPA) if within the appropriate time window and if there are no contraindications. Mechanical thrombectomy may be considered based on the vessel involved and extent of infarction. In pregnancy, recent guidelines support the cautious use of tPA when benefits outweigh the risks, with appropriate maternal and fetal monitoring. During lactation, tPA is considered safe due to minimal secretion into breast milk, but each case should be evaluated individually. Secondary stroke prevention (risk factor modification, antiplatelet therapy, and control of comorbid conditions) is also essential.",
        "option_analysis": "Option A (Congruent homonymous hemianopia with macular sparing) is the classic description seen in occipital lobe strokes. Option B (Incongruent homonymous hemianopia with macular sparing) is more consistent with lesions involving the optic radiations rather than the occipital cortex. Options C and D are incorrect as they state non-macular sparing, which does not align with the typical clinical presentation caused by the collateral vascular supply to the macula in occipital infarcts.",
        "clinical_pearls": "A stroke affecting the occipital lobe typically presents with a homonymous hemianopia that is congruous and spares the macula due to dual blood supply. Recognizing this pattern can help localize the lesion and prompt timely neuroimaging and initiation of reperfusion therapy, which is critical in acute stroke management. Special considerations should be given when managing stroke in pregnant or lactating patients.",
        "current_evidence": "Recent studies and clinical guidelines emphasize early neuroimaging (using MRI/CT) in suspected stroke cases to identify occipital cortex involvement. Updated protocols for reperfusion therapies, including the use of tPA and mechanical thrombectomy, underscore the importance of timely intervention. Current literature supports that the pattern of a congruent homonymous hemianopia with macular sparing is a reliable clinical indicator of a cortical visual field defect, particularly involving the occipital lobe."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992975",
    "fields": {
      "question_number": "179",
      "question_text": "case of subacute stroke CT brain attached, TTE: normal, 48 hours Holter normal what to do next:",
      "options": {
        "A": "Prolonged cardiac monitoring",
        "B": "Carotid US",
        "C": "Coagulation workup"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "In ischemic stroke workup, the identification of the embolic source is critical. When the initial cardiac evaluations (transthoracic echocardiogram [TTE] and a 48\u2010hour Holter monitor) are normal, clinicians must look for other common sources of emboli. Carotid atherosclerotic disease is one such common cause, especially for strokes involving anterior circulation.",
        "pathophysiology": "Carotid atherosclerosis involves the buildup of plaque within the carotid arteries. These plaques can narrow the vessel lumen or rupture, causing emboli to dislodge and travel to the brain, resulting in an ischemic event. Even if cardiac sources have been ruled out, significant carotid stenosis may be the culprit.",
        "clinical_correlation": "Patients with traditional vascular risk factors (e.g., hypertension, hyperlipidemia, smoking) are more susceptible to carotid artery disease. In a subacute stroke scenario where cardiac workup is negative, evaluating the carotid arteries helps determine if atherosclerotic disease is the cause.",
        "diagnostic_approach": "After a normal TTE and 48\u2010hour Holter monitoring, it is standard to proceed with imaging of the cervical vessels. Carotid ultrasound is a noninvasive, widely available, cost-effective method to assess for significant stenosis or plaque vulnerability that could be responsible for embolic strokes.",
        "classification_and_neurology": "Ischemic stroke classification commonly follows the TOAST criteria, which categorizes stroke into five subtypes: large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology (cryptogenic). This case fits into the cryptogenic stroke category pending further evaluation. The diagnosis of cardioembolic stroke requires evidence of a cardiac source of embolism. The classification system has evolved to emphasize the importance of extended cardiac monitoring in cryptogenic stroke. Alternative classification schemes, such as the CCS (Causative Classification System), similarly stress comprehensive evaluation. Controversy remains regarding the optimal duration and modality of cardiac monitoring, but consensus supports prolonged monitoring to improve detection of occult AF.",
        "classification_and_nosology": "Within the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system, strokes due to significant carotid atherosclerosis are categorized under large-artery atherosclerosis. This differentiates them from cardioembolic or small vessel (lacunar) strokes.",
        "management_principles": "Once carotid stenosis is identified, management may include medical therapy (such as antiplatelet agents, statins, and risk factor control) and, in cases of hemodynamically significant stenosis, revascularization procedures like carotid endarterectomy or stenting may be indicated. Importantly, in pregnant or lactating patients, carotid ultrasound is safe (as it involves no ionizing radiation), and any ensuing medical management (such as antiplatelets) should follow current safety guidelines relevant to pregnancy and lactation.",
        "option_analysis": "Option A, prolonged cardiac monitoring, is sometimes used to detect paroxysmal atrial fibrillation but is generally considered when there is a high index of suspicion or when the initial workup is inconclusive for a cardioembolic source. Option C, a coagulation workup, is more appropriate in younger patients or those without traditional risk factors where a hypercoagulable state is suspected. With the normal cardiac studies and a subacute presentation more suggestive of a large-artery source, Option B (Carotid US) is the appropriate next step. Option D is not provided.",
        "clinical_pearls": "Carotid ultrasound remains one of the first-line noninvasive approaches in the evaluation of stroke etiology when suspecting extracranial large-artery disease. Even when initial monitors for atrial fibrillation are negative, consider further evaluation with both prolonged cardiac monitoring (if clinical suspicion continues) and vascular imaging based on the patient\u2019s presentation.",
        "current_evidence": "Current AHA/ASA guidelines for stroke evaluation emphasize the importance of vascular imaging in acute ischemic stroke. There is strong evidence supporting the use of carotid ultrasound in detecting significant stenosis, which can guide further interventions and tailored secondary prevention strategies. In patients with negative cardiac evaluations, early carotid imaging is crucial in adapting the therapeutic approach."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992976",
    "fields": {
      "question_number": "180",
      "question_text": "Patient with history severe headache, right eye pupils 6mm and non-reactive, left is 3 mm and reactive, where is the lesion:",
      "options": {
        "A": "Anterior communicating",
        "B": "Posterior communicating",
        "C": "Anterior cerebral artery",
        "D": "Posterior cerebral artery"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "A posterior communicating artery aneurysm is classically associated with an isolated third nerve (oculomotor nerve) palsy. In this scenario, the patient\u2019s severe headache and unilateral dilated, non-reactive pupil (6 mm vs 3 mm) strongly suggest compressive involvement of the oculomotor nerve \u2013 a hallmark of a PCom aneurysm.",
        "pathophysiology": "The aneurysm arising from the posterior communicating artery can enlarge and compress the oculomotor nerve, particularly its superficial parasympathetic fibers responsible for pupillary constriction. Compression leads to pupillary dilation (mydriasis) and impaired reactivity. The severe headache may be due to local irritation from aneurysmal expansion or a sentinel bleed, even in the absence of full subarachnoid hemorrhage.",
        "clinical_correlation": "Clinically, a patient with a third nerve palsy from a PCom aneurysm typically presents with a dilated pupil that is non-reactive to light, ptosis, and a \u2018down and out\u2019 deviation of the eye. The headache accentuates the concern for an aneurysmal process, making this finding highly suggestive in the right clinical context.",
        "diagnostic_approach": "Initial workup includes neuroimaging \u2013 a noncontrast CT scan to rule out hemorrhage followed by CT angiography or MR angiography to evaluate for aneurysms. Differential diagnoses include aneurysms in other cerebral vessels and microvascular ischemic cranial nerve palsies; however, pupil involvement favors compressive etiologies over ischemic ones.",
        "classification_and_neurology": "Third cranial nerve palsies can be classified based on etiology into: - **Compressive lesions** (e.g., aneurysms, tumors, uncal herniation) - **Ischemic lesions** (microvascular cranial neuropathy, often diabetic) - **Inflammatory/infectious causes** - **Traumatic causes**  This question focuses on a vascular compressive third nerve palsy caused by an aneurysm, specifically a posterior communicating artery aneurysm.  From a cerebrovascular classification standpoint, the lesion falls under the category of **intracranial aneurysms**, which are saccular outpouchings of cerebral arteries, most commonly occurring at arterial bifurcations in the circle of Willis. The posterior communicating artery is a frequent site for aneurysm formation.  The nosology of cerebral aneurysms has evolved with advances in neuroimaging and endovascular techniques. Current consensus classifies aneurysms by size, location, and rupture status, guiding treatment decisions.  There is consensus that third nerve palsy with pupillary involvement in the setting of a PCOM aneurysm is a neurosurgical emergency due to high risk of rupture. Controversies remain in management timing and treatment modality (surgical clipping vs endovascular coiling), but diagnostic classification is well established.",
        "classification_and_nosology": "Aneurysms are classified by location and morphology. A posterior communicating artery aneurysm is a saccular (berry) aneurysm located at the junction of the internal carotid and the posterior communicating branch. It is a recognized cause of isolated third nerve palsies.",
        "management_principles": "Management involves urgent neurosurgical consultation. The treatment options include endovascular coiling or surgical clipping, depending on the aneurysm\u2019s size, morphology, and patient factors. Blood pressure control and avoidance of stressors are essential. In pregnant or lactating patients, imaging modalities without ionizing radiation (MR angiography) and careful multidisciplinary management are favored.",
        "option_analysis": "Option A (Anterior communicating) is more commonly involved in cognitive and personality changes rather than isolated third nerve involvement. Option C (Anterior cerebral artery) typically presents with lower limb motor/sensory deficits. Option D (Posterior cerebral artery) usually presents with visual field deficits. Option B (Posterior communicating) correctly correlates with the anatomical location affecting the oculomotor nerve.",
        "clinical_pearls": "1. A dilated, non-reactive pupil in the setting of headache is a red flag for an aneurysmal compression of the oculomotor nerve. 2. PCom aneurysms are the most common cause of compressive third nerve palsies with pupillary involvement.",
        "current_evidence": "Recent guidelines emphasize early identification of aneurysms with advanced imaging techniques (CTA/MRA) and prompt neurosurgical intervention to reduce the risk of rupture. Emerging data support individualized management based on aneurysm characteristics and patient comorbidities."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992977",
    "fields": {
      "question_number": "181",
      "question_text": "Case scenario of patient with left eye amaurosis fugax and transient dysarthria, what is your next step?",
      "options": {
        "A": "US carotid doppler"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Amaurosis fugax (transient monocular blindness) accompanied by transient dysarthria is highly suggestive of a transient ischemic attack (TIA) due to embolic phenomena from a carotid origin. Carotid artery evaluation is central to the workup of such presentations.",
        "pathophysiology": "Often, atherosclerotic plaque in the carotid artery can embolize, temporarily occluding blood flow to the retina (resulting in amaurosis fugax) and parts of the brain responsible for speech. The transient nature of these symptoms is characteristic of TIA, indicating reversible ischemia.",
        "clinical_correlation": "Patients with these transient neurologic symptoms should be assessed for carotid artery disease. The unilateral nature of amaurosis fugax often localizes the pathology to the ipsilateral carotid artery, while associated cerebral symptoms (like dysarthria) reflect embolic dissemination.",
        "diagnostic_approach": "The initial diagnostic approach should include a noninvasive carotid duplex ultrasound (Carotid Doppler) to assess for the degree of carotid stenosis or plaque burden. Differential diagnoses include retinal migraine, ocular conditions, and cardiac embolic sources\u2014hence additional workup with echocardiography and Holter monitoring is often performed.",
        "classification_and_neurology": "TIA is classified under cerebrovascular diseases according to the World Health Organization and American Heart Association/American Stroke Association (AHA/ASA) frameworks. It is distinguished from stroke by the absence of persistent neurological deficits or infarction on imaging.   TIAs are further subclassified by etiology using the TOAST criteria into large-artery atherosclerosis, cardioembolism, small-vessel occlusion, other determined, or undetermined causes. In this case, symptoms localize to large-artery atherosclerosis affecting the carotid artery.   Classification systems have evolved from purely time-based definitions (<24 hours) to tissue-based definitions incorporating MRI findings to improve diagnostic accuracy and guide management.",
        "classification_and_nosology": "TIAs are classified based on symptom duration (<1 hour) and are considered warning events for future strokes. Carotid artery disease due to atherosclerosis is one of the major causes, alongside cardioembolic and small vessel occlusive mechanisms.",
        "management_principles": "After confirming carotid disease, management includes antiplatelet therapy, statins, and risk factor modification. In high-grade stenosis, carotid endarterectomy or stenting may be considered. In pregnancy, non-ionizing imaging methods (such as carotid duplex ultrasound) are preferred. Lactating mothers can also safely undergo ultrasound evaluation.",
        "option_analysis": "Option A (US carotid Doppler) is the correct initial investigation for suspected carotid artery stenosis in TIA patients. Other tests (CT/MR angiography) may be used later for further delineation, but ultrasound is noninvasive, cost-effective, and free of radiation.",
        "clinical_pearls": "1. Amaurosis fugax is often a harbinger of carotid artery disease and future cerebrovascular events. 2. Early detection with a carotid Doppler can guide timely interventions to reduce stroke risk.",
        "current_evidence": "Current American Heart Association (AHA)/American Stroke Association (ASA) guidelines recommend prompt carotid imaging in patients with TIA symptoms to identify those who may benefit from revascularization procedures alongside aggressive medical management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992978",
    "fields": {
      "question_number": "182",
      "question_text": "70-year-old male came with acute stroke was given tPA in ER after 6 hours he was assessed nothing change vital signs showed BP 190/90, the patient looks anxious, what to do?",
      "options": {
        "A": "Amlodipine",
        "B": "Nicardipine",
        "C": "Observation",
        "D": "Diazepam."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Post-thrombolytic management in acute stroke involves careful blood pressure regulation. Elevated blood pressure following tPA administration increases the risk of hemorrhagic transformation.",
        "pathophysiology": "High blood pressure after tPA can lead to reperfusion injury and an increased risk of intracranial bleeding. The stress response and anxiety may further exacerbate hypertension. Tightly controlled BP management mitigates these risks.",
        "clinical_correlation": "In this case, after administration of tPA, the patient\u2019s blood pressure is 190/90 mm Hg, which exceeds the recommended threshold (generally <180/105 mm Hg post-tPA). The patient\u2019s anxiety could be a secondary response, and it further underscores the need for prompt BP control.",
        "diagnostic_approach": "Continuous monitoring of neurological status and blood pressure is essential following tPA. Differential considerations for elevated BP include uncontrolled baseline hypertension, pain, or stress responses. However, in the post-thrombolytic setting, rapid BP management is critical.",
        "classification_and_neurology": "Post-thrombolysis hypertension management falls under cerebrovascular disease management guidelines and acute stroke care protocols. The American Heart Association/American Stroke Association (AHA/ASA) classifies BP management after ischemic stroke into pre-thrombolysis, perithrombolysis, and post-thrombolysis phases, each with specific BP targets. This condition is part of the broader category of ischemic stroke complications and secondary prevention strategies. Classification systems have evolved to incorporate evidence-based BP thresholds tailored to thrombolytic therapy. Controversies remain regarding optimal BP targets in various stroke subtypes and patient populations, but consensus supports strict BP control post-tPA to reduce hemorrhagic risk.",
        "classification_and_nosology": "Hypertensive emergencies after thrombolytic therapy are a recognized complication and require immediate medical intervention. This scenario falls under the category of post-tPA blood pressure management.",
        "management_principles": "The first-line management for blood pressure management in the post-tPA period is intravenous antihypertensive therapy. Nicardipine is preferred due to its ease of titration and rapid onset of action. It is administered as an IV infusion to achieve a controlled reduction in blood pressure. For pregnant or lactating patients, nicardipine, though generally categorized as C, has been used with caution under close monitoring if necessary.",
        "option_analysis": "Option A (Amlodipine) is unsuitable as it is an oral agent with a slow onset and less titratability. Option C (Observation) is inappropriate given the risk of hemorrhage with elevated BP. Option D (Diazepam) may reduce anxiety but does not adequately address the urgent need for BP reduction. Option B (Nicardipine) is the correct choice, consistent with current guidelines.",
        "clinical_pearls": "1. Post-tPA blood pressure must be maintained below 180/105 mm Hg to minimize hemorrhagic complications. 2. IV nicardipine is a titratable and preferred agent in this setting.",
        "current_evidence": "The latest stroke management guidelines reaffirm the importance of immediate blood pressure control post-thrombolysis, with nicardipine being the agent of choice due to its rapid and easily adjustable effects."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992979",
    "fields": {
      "question_number": "183",
      "question_text": "Symptoms of TIA for 10 minutes Echocardiogram negative, Holter was negative what to do next:",
      "options": {
        "A": "Neck CTA",
        "B": "Brain MRI"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "In patients with transient ischemic attack (TIA) symptoms, a thorough evaluation of potential sources is paramount. With a negative cardiac workup (echo and Holter) in a patient with a brief TIA, investigation of the cervical vasculature is warranted as carotid artery atherosclerosis remains a common cause.",
        "pathophysiology": "Atherosclerotic plaques in the carotid arteries can lead to embolization and transient occlusion of cerebral vessels, resulting in TIA symptoms. A TIA lasting around 10 minutes is characteristic of embolic events from a carotid lesion rather than a cardioembolic source if the cardiac evaluation is negative.",
        "clinical_correlation": "The negative echocardiogram and Holter monitoring suggest that the source of embolism is less likely to be cardiac. Therefore, evaluation of the neck vessels, particularly the carotids, is critical. This helps in diagnosing significant stenosis or plaque that may necessitate intervention to prevent stroke.",
        "diagnostic_approach": "The diagnostic workup for TIA includes brain imaging and vascular imaging. While a carotid duplex ultrasound is often used as an initial noninvasive test, a Neck CTA provides a more detailed visualization of the carotid anatomy, making it a valuable next step if further clarification is needed. Differential diagnoses include vasculitis, dissection, and small vessel disease but these are less common when cardiac sources have been ruled out.",
        "classification_and_neurology": "TIA is classified under cerebrovascular diseases according to the World Health Organization and the American Heart Association/American Stroke Association (AHA/ASA). The 2014 AHA/ASA definition emphasizes the absence of infarction on imaging, distinguishing TIA from ischemic stroke. TIAs are subclassified etiologically by the Trial of Org 10172 in Acute Stroke Treatment (TOAST) criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, or undetermined etiology. This case fits the large artery atherosclerosis category given negative cardiac workup and symptomatology consistent with carotid territory ischemia. Classification systems have evolved from purely time-based definitions to tissue-based definitions incorporating neuroimaging. Controversies remain regarding optimal imaging modalities and thresholds for intervention, but consensus supports urgent vascular imaging after TIA.",
        "classification_and_nosology": "TIAs are transient events signaling a high risk for future strokes. They are categorized by the tissue and vascular imaging findings, and carotid artery disease is a well-established etiological category within TIA classifications.",
        "management_principles": "After identifying a carotid lesion, management involves medical therapy (antiplatelets, statins, and risk factor modification) and potential surgical intervention (carotid endarterectomy or stenting) for significant stenosis. In pregnant or lactating patients, a carotid duplex ultrasound is preferred due to the absence of ionizing radiation; however, if CTA is necessary, the risks and benefits must be weighed carefully.",
        "option_analysis": "Option A (Neck CTA) is an appropriate next step for detailed vascular imaging to evaluate the carotid arteries when cardiac sources have been excluded. Option B (Brain MRI) would be more useful for assessing parenchymal injury but does not directly identify the source of emboli. Given the clinical context, Option A is the more logical choice.",
        "clinical_pearls": "1. When cardiac evaluations are negative in TIA workup, the carotid arteries should be scrutinized for atherosclerotic disease. 2. Neck CTA offers high-resolution imaging and is particularly useful in assessing the extent of carotid pathology.",
        "current_evidence": "Recent guideline updates from stroke societies recommend a comprehensive vascular workup in TIA patients, highlighting the utility of advanced imaging (including CTA) to identify extracranial carotid stenosis and guide further intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992980",
    "fields": {
      "question_number": "184",
      "question_text": "70 something female with DM, HTN and fully independent came with 90 minutes onset of dense right hemiparesis and aphasia, 30 minutes after arrival CT brain done and showed (picture no hemorrhage), when she was on her way to ER her symptoms became slightly better what to do next:",
      "options": {
        "A": "IV tpa",
        "B": "CT angiogram"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This case involves an acute ischemic stroke within the thrombolysis time window. The core concept is rapid identification and treatment of ischemic strokes with IV tissue plasminogen activator (tPA) to salvage the ischemic penumbra, as long as hemorrhage is excluded on non\u2010contrast CT.",
        "pathophysiology": "Acute ischemic stroke is most often caused by thromboembolic occlusion of an artery supplying the brain. In this patient, risk factors (diabetes, hypertension) predispose to atherosclerosis. Although she showed some improvement (which may reflect partial spontaneous recanalization or penumbral recovery), the underlying clot still jeopardizes brain tissue. Early intervention with tPA can lyse the clot, restoring blood flow and improving outcomes.",
        "clinical_correlation": "The patient initially presented with dense right hemiparesis and aphasia\u2014classic signs of a left hemispheric stroke affecting both motor pathways and language centers. Slight improvement en route does not necessarily mean that she has fully recovered; persistent neurological deficits that are disabling warrant treatment with IV tPA.",
        "diagnostic_approach": "The initial diagnostic step is obtaining a non-contrast head CT to rule out hemorrhage. Differential diagnoses include hemorrhagic stroke, stroke mimics (seizure, migraine), and transient ischemic attacks. In some cases, further vascular imaging (CT angiogram) may be considered to identify large vessel occlusions, but here the absence of hemorrhage is the key criterion for proceeding with IV tPA.",
        "classification_and_neurology": "Ischemic stroke is classified under cerebrovascular diseases in the WHO ICD-11 and American Heart Association/American Stroke Association (AHA/ASA) stroke classifications. It is categorized by etiology into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), other determined etiologies, and cryptogenic stroke. This patient\u2019s risk factors suggest atherosclerotic or small vessel disease etiology. The classification guides management and secondary prevention. Thrombolytic therapy applies broadly to ischemic strokes without hemorrhage and within time windows rather than specific etiologies. Recent classifications emphasize imaging and clinical criteria for therapeutic decisions.",
        "classification_and_nosology": "Strokes are broadly classified into ischemic and hemorrhagic types. Ischemic strokes can further be categorized into thrombotic, embolic, or lacunar strokes. This case falls under the category of acute thrombolytic therapy for an ischemic stroke.",
        "management_principles": "According to the latest AHA/ASA guidelines, IV tPA is the first-line treatment for patients with acute ischemic stroke who present within 4.5 hours of symptom onset and meet inclusion criteria. Even with modest improvement, if the deficits remain functionally disabling (e.g., severe hemiparesis and aphasia), tPA is indicated. Pregnancy and lactation considerations are not applicable in this 70\u2010year-old patient.",
        "option_analysis": "Option A (IV tPA) is correct because the patient is within the time window and still has disabling symptoms despite slight improvement. Option B (CT angiogram) might be considered for evaluating large vessel occlusion when planning for endovascular therapy, but it is not the immediate next step after confirming the absence of hemorrhage when IV tPA is indicated. Options C and D are not provided and thus not relevant.",
        "clinical_pearls": "1. Time is brain\u2014prompt evaluation and treatment of acute ischemic stroke improves outcomes. 2. Even if there is slight improvement en route, residual disabling deficits warrant thrombolytic therapy. 3. A non\u2010contrast CT scan is essential to rule out hemorrhage before administering IV tPA.",
        "current_evidence": "Recent studies and updated guidelines continue to support the use of IV tPA in eligible patients within the recommended time window, even in cases where there is some clinical improvement, provided that disabling deficits remain. Advanced imaging is increasingly used to assess penumbral tissue but does not delay the initiation of tPA when criteria are met."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992981",
    "fields": {
      "question_number": "185",
      "question_text": "Female just had uneventful vaginal delivery one week ago, severe headache, vital signs within normal, afebrile, blood electrolytes and renal function normal. What will you do next:",
      "options": {
        "A": "Angiogram",
        "B": "CT venogram",
        "C": "Urine protein and liver function",
        "D": "LP"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses the evaluation of postpartum headache, emphasizing the importance of considering cerebral venous sinus thrombosis (CVST) in postpartum women.",
        "pathophysiology": "Postpartum women are in a hypercoagulable state, which increases the risk of thrombus formation in the cerebral venous sinuses. CVST leads to impaired venous drainage, increased intracranial pressure, and potentially venous cerebral infarction. The absence of fever and normal vital signs help rule out infectious etiologies.",
        "clinical_correlation": "A severe headache in a postpartum woman, particularly in the first few weeks after delivery, raises suspicion for CVST. Normal blood pressure, electrolytes, and renal function help differentiate it from conditions like postpartum preeclampsia. Despite an uneventful vaginal delivery, the hypercoagulable state of the postpartum period is a recognized risk factor.",
        "diagnostic_approach": "The gold standard imaging for suspected CVST is a CT venogram (or MR venography), which can visualize venous occlusions in the brain. Differential diagnoses include postpartum preeclampsia (which would show elevated blood pressure or abnormal labs), post-dural puncture headache (typically positional), and subarachnoid hemorrhage (usually with a different clinical profile).",
        "classification_and_neurology": "CVST is classified as a subtype of cerebrovascular disease under the broader category of venous strokes, distinct from arterial ischemic strokes. According to the International Classification of Diseases (ICD-11), CVST falls under cerebrovascular diseases with specific coding for venous thrombosis of cerebral vessels. It is further subclassified based on the location of the thrombus (e.g., superior sagittal sinus, transverse sinus) and etiology (e.g., pregnancy-related, infection-associated, idiopathic). The classification recognizes CVST as part of the spectrum of stroke syndromes but distinct in pathophysiology and management. Over time, classification systems have evolved to integrate imaging findings and etiological factors to guide prognosis and therapy. Controversies remain regarding the best criteria to classify atypical presentations and the role of genetic thrombophilias, but consensus supports recognizing CVST as a unique cerebrovascular entity requiring tailored diagnostic and therapeutic approaches.",
        "classification_and_nosology": "CVST is classified as a type of venous stroke distinct from arterial ischemic stroke. It falls under cerebrovascular disorders and is specifically more common in women, particularly during pregnancy and the postpartum period.",
        "management_principles": "The first-line management for CVST is anticoagulation, typically with low molecular weight heparin (LMWH), even in the postpartum period. This treatment is maintained for several months with a transition to oral anticoagulants if indicated. Pregnancy and lactation considerations: LMWH is considered safe during lactation. Further evaluation for underlying thrombophilic disorders may be warranted.",
        "option_analysis": "Option B (CT venogram) is correct because it is the appropriate imaging study to confirm a diagnosis of cerebral venous sinus thrombosis in a postpartum patient with a severe headache. Option A (Angiogram) is less commonly used and more invasive. Option C (Urine protein and liver function tests) is indicated for preeclampsia, which is unlikely given the normal vital signs and labs. Option D (Lumbar puncture) is not indicated in this clinical context due to the absence of signs of meningitis or subarachnoid hemorrhage.",
        "clinical_pearls": "1. The postpartum period is a high-risk period for CVST due to hypercoagulability. 2. CT venogram is the imaging modality of choice when CVST is suspected. 3. Normal vital signs and laboratory values help distinguish CVST from postpartum preeclampsia.",
        "current_evidence": "Current guidelines and recent research underscore the importance of early diagnosis and treatment of CVST in postpartum women. Anticoagulation with LMWH remains the first-line treatment, and imaging with CT venogram (or MRV) is recommended for accurate diagnosis."
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
