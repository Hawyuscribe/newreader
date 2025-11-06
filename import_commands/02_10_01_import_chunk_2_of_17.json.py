
# Import batch 1 of 3 from chunk_2_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99992997",
    "fields": {
      "question_number": "239",
      "question_text": "Based on the following brain CT, what is the most likely diagnosis?",
      "options": {
        "A": "Perimesencephalic hemorrhage SAH"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Subarachnoid hemorrhage (SAH) is a critical condition characterized by bleeding into the subarachnoid space. However, not all SAHs are due to aneurysm rupture. Perimesencephalic SAH, a subset of nonaneurysmal SAH, has a distinct CT appearance and a markedly better prognosis.",
        "pathophysiology": "Perimesencephalic SAH is thought to result from a venous or small arterial bleed in the area surrounding the midbrain (the perimesencephalic cisterns). Unlike aneurysmal SAH, it is not associated with ruptured aneurysms and tends to confine to the perimesencephalic cisterns, with no evidence of blood in the sylvian fissures or other cisterns.",
        "clinical_correlation": "Clinically, patients may present with a sudden severe headache, though the clinical course is typically benign compared to aneurysmal SAH. The typical CT finding is localized blood in the perimesencephalic region with no extension into other brain cisterns, which helps differentiate it from aneurysmal SAH.",
        "diagnostic_approach": "The initial diagnostic modality is a noncontrast head CT to detect subarachnoid blood. Once a perimesencephalic pattern is identified, it is standard to perform vascular imaging (CTA or digital subtraction angiography) to rule out an aneurysm. Differential diagnoses include aneurysmal SAH (which typically shows a more diffuse blood distribution) and other causes of intracranial hemorrhage.",
        "classification_and_neurology": "Subarachnoid hemorrhages are classified based on etiology and imaging characteristics. The primary division is between aneurysmal SAH and non-aneurysmal SAH. Non-aneurysmal SAH is further subclassified into perimesencephalic hemorrhage and other non-perimesencephalic types. Perimesencephalic SAH is recognized as a distinct clinical and radiological entity within the non-aneurysmal SAH group. The Fisher grading scale classifies SAH based on CT blood distribution and predicts vasospasm risk but does not specifically distinguish perimesencephalic SAH. The World Federation of Neurosurgical Societies (WFNS) scale grades clinical severity but likewise applies broadly. Current consensus recognizes perimesencephalic hemorrhage as a subtype with distinct prognosis and management implications, differentiating it from aneurysmal SAH which requires urgent neurosurgical intervention.",
        "classification_and_nosology": "SAH is broadly categorized into aneurysmal and nonaneurysmal. Perimesencephalic hemorrhage falls under the nonaneurysmal variant and is distinguished by its typical radiological pattern and benign clinical course.",
        "management_principles": "The management is largely supportive, including blood pressure control, pain management, and sometimes the use of nimodipine to help prevent vasospasm, though vasospasm is less common in perimesencephalic SAH. In pregnant or lactating women, supportive care is similarly applied, with careful selection of medications to minimize fetal or neonatal risk.",
        "option_analysis": "Option A ('Perimesencephalic hemorrhage SAH') is the correct answer when the CT scan shows a blood distribution centered around the midbrain with sparing of other cisterns. Other potential options (if provided) might have included aneurysmal SAH or other hemorrhagic patterns, which are excluded by the localized pattern seen here.",
        "clinical_pearls": "1. Perimesencephalic SAH carries a much lower risk of complications and rebleeding than aneurysmal SAH. 2. The typical CT distribution is key for an accurate diagnosis. 3. Confirmatory vascular imaging is still important to definitively exclude aneurysms.",
        "current_evidence": "Recent studies and guidelines support the conservative management of perimesencephalic SAH due to its benign natural history. The avoidance of aggressive interventions unless imaging reveals aneurysmal origins has been reinforced by current research."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_17.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992998",
    "fields": {
      "question_number": "240",
      "question_text": "Based on the following brain MRI, what is the most likely mechanism?",
      "options": {
        "A": "ICA stenosis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Brain MRI is an essential tool for evaluating the mechanism of ischemic events. One common mechanism depicted on MRI is cerebral ischemia due to hemodynamic compromise, often seen in watershed regions between major cerebral arteries. Severe internal carotid artery (ICA) stenosis is a well-known cause of such hemodynamic failure.",
        "pathophysiology": "ICA stenosis, usually from atherosclerotic disease, leads to reduced cerebral perfusion. This can result in watershed or borderzone infarcts\u2014ischemic lesions that occur between the territories of the major cerebral arteries. The MRI will typically show infarcts in these borderzone areas, supporting the mechanism of hypoperfusion rather than embolism or small vessel occlusion.",
        "clinical_correlation": "Patients with significant ICA stenosis may experience transient ischemic attacks or full-blown strokes, often with deficits corresponding to the affected vascular territories. The ischemic changes on MRI, particularly in watershed zones, are indicative of a hemodynamic mechanism linked to severe carotid narrowing.",
        "diagnostic_approach": "Diagnosis is confirmed through vascular imaging modalities like carotid Doppler ultrasound, CTA, or MRA, which assess the degree of ICA stenosis. Differential diagnoses include embolic stroke (from cardiac sources) or small vessel disease, but the watershed distribution and vascular studies help differentiate ICA stenosis-related ischemia from these conditions.",
        "classification_and_neurology": "ICA stenosis-related ischemic stroke falls under the TOAST classification system as a subtype of large-artery atherosclerosis. TOAST categorizes ischemic strokes into five major groups: (1) large-artery atherosclerosis, (2) cardioembolism, (3) small vessel occlusion (lacunar), (4) stroke of other determined etiology, and (5) stroke of undetermined etiology. Large-artery atherosclerosis includes stenosis or occlusion of major extracranial or intracranial arteries due to atherosclerosis. This classification aids in prognosis and guides treatment strategies. Over time, refinements in classification have integrated imaging and clinical data for precision. Other systems, such as CCS (Causative Classification of Stroke), also emphasize large vessel disease but differ in granularity. Despite minor differences, consensus supports ICA stenosis as a key large-vessel stroke mechanism with distinct management implications.",
        "classification_and_nosology": "Ischemic strokes are classified by their source; this case falls under the large vessel atherosclerotic category. Within this, borderzone infarcts are a classic imaging pattern seen in hemodynamic compromise from severe ICA stenosis.",
        "management_principles": "The first-line management of symptomatic ICA stenosis involves aggressive medical management\u2014including antiplatelet therapy, statins, and risk factor modification (control of hypertension, smoking cessation). In cases of severe stenosis in symptomatic patients, revascularization via carotid endarterectomy or stenting is recommended. In pregnant patients, the risks of interventional procedures must be balanced with medical therapy, using medications that are safe in pregnancy (e.g., certain antiplatelets and statins may be contraindicated, so tailored management is necessary). Lactating women are managed similarly, with careful consideration of drug safety.",
        "option_analysis": "Option A ('ICA stenosis') is correct if the MRI shows infarct patterns typical of a watershed distribution. Other mechanisms might include cardioembolism or small vessel disease, but these are less consistent with the described MRI pattern. Thus, ICA stenosis is the most plausible explanation given the information.",
        "clinical_pearls": "1. Watershed infarcts on MRI are a red flag for hemodynamic compromise due to carotid stenosis. 2. Vascular imaging is essential in determining the degree of stenosis. 3. Management is a combination of medical therapy and possible revascularization in symptomatic severe cases.",
        "current_evidence": "Recent trials continue to support the role of carotid revascularization in select symptomatic patients with high-grade stenosis, while emphasizing aggressive medical management in most cases. Guidelines stress individualized therapy based on imaging findings and clinical presentation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_15.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992999",
    "fields": {
      "question_number": "241",
      "question_text": "Patient developed ischemic stroke, his echo showed valvular hypokinesia lesion, how to treat this patient?",
      "options": {
        "A": "Warfarin",
        "B": "NOACs",
        "C": "Aspirin",
        "D": "Clopidogrel"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Cardioembolic strokes are a distinct subtype of ischemic stroke, where the source of embolization is cardiac in origin. In patients with cardiac wall motion abnormalities (often described as ventricular hypokinesia), blood stasis can lead to thrombus formation, which may subsequently embolize to cerebral arteries.",
        "pathophysiology": "Areas of ventricular hypokinesia, frequently due to previous myocardial infarction or cardiomyopathy, create conditions for blood stasis. This stasis predisposes to the formation of an intraventricular thrombus, which can dislodge and travel to the brain, causing an ischemic stroke. The management involves anticoagulation to prevent further thrombus formation and embolization.",
        "clinical_correlation": "Patients with a history of cardiac dysfunction and evidence of wall motion abnormalities (as seen on echocardiography) who develop an ischemic stroke are typically suspected of having a cardioembolic mechanism. This guides the clinician toward the use of anticoagulant therapy rather than solely antiplatelet agents.",
        "diagnostic_approach": "Echocardiography is the main diagnostic tool for identifying left ventricular thrombi and assessing wall motion. Differential diagnoses include atherosclerotic stroke or small vessel (lacunar) stroke, but the presence of an echocardiographic abnormality points to a cardioembolic source. Additional workup might include cardiac MRI or contrast studies for further delineation.",
        "classification_and_neurology": "Ischemic strokes are classified etiologically by the TOAST criteria into five major categories: large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. Cardioembolic stroke falls under the cardioembolism category, which includes sources such as atrial fibrillation, mechanical heart valves, valvular disease with hypokinesia, and intracardiac thrombus. This classification guides management decisions, particularly anticoagulation versus antiplatelet therapy. The presence of valvular hypokinesia places the patient in a high-risk cardioembolic category. Over time, refinements in stroke classification have emphasized imaging and cardiac evaluation to improve etiological precision and treatment tailoring.",
        "classification_and_nosology": "Strokes are classified based on etiology. Cardioembolic strokes (often due to conditions like atrial fibrillation or left ventricular thrombus formation following wall motion abnormalities) fall under the TOAST classification of ischemic strokes. This patient\u2019s echo finding directs the categorization in this subtype.",
        "management_principles": "The primary treatment for cardioembolic stroke due to a ventricular thrombus is systemic anticoagulation. Warfarin has been the traditional first-line therapy with a target INR typically between 2 and 3, and is supported by a body of evidence in preventing recurrent embolic events. Although non-vitamin K oral anticoagulants (NOACs) are preferred in non-valvular atrial fibrillation, their use in patients with left ventricular thrombus is off\u2013label and not yet supported by robust evidence. Antiplatelet therapies like aspirin or clopidogrel are not sufficient in this setting. In the context of pregnancy, warfarin is contraindicated due to its teratogenicity; low molecular weight heparin is the preferred anticoagulant. In lactating women, warfarin is generally safe, though careful monitoring is still warranted.",
        "option_analysis": "Option A ('Warfarin') is the correct treatment choice for a cardioembolic stroke in the setting of ventricular hypokinesia. NOACs (Option B) do not have established evidence in this specific scenario. Options C and D (aspirin and clopidogrel) are antiplatelet agents and do not provide adequate protection against thrombus formation from a low-flow cardiac source.",
        "clinical_pearls": "1. Cardioembolic strokes require anticoagulation rather than mere antiplatelet therapy. 2. Warfarin remains the gold standard for treating left ventricular thrombus despite emerging interest in NOACs. 3. In pregnant patients, warfarin is contraindicated\u2014LMWH should be used instead.",
        "current_evidence": "Recent guidelines reaffirm the role of warfarin for patients with left ventricular thrombus and cardioembolic stroke. While newer agents are under investigation, current large-scale studies and clinical practice continue to support warfarin as first\u2013line therapy in this setting, with adjustments made for special populations like pregnant women."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993000",
    "fields": {
      "question_number": "242",
      "question_text": "Typical scenario of CADASIL and the Q about the diagnosis",
      "options": {
        "B": "(genetic testing for NOTCH3 mutations) is correct because it is the definitive diagnostic modality. Option A (skin biopsy) is only supportive and is less sensitive and specific. Option C (MRI alone) reveals characteristic but nonspecific findings that overlap with other small vessel pathologies. Option D (CSF analysis) and Option E (routine blood tests) are non"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy) is a hereditary small vessel disease. The condition typically presents with migraine (often with aura), recurrent subcortical ischemic events, and progressive cognitive decline. The definitive diagnosis relies on identifying the pathogenic mutation in the NOTCH3 gene.",
        "pathophysiology": "Mutations in the NOTCH3 gene lead to abnormal protein accumulation in the smooth muscle cells of small arteries. This results in degeneration of the vascular smooth muscle with the accumulation of granular osmiophilic deposits (GOM) and subsequent compromise in blood flow. These changes produce the characteristic white matter lesions and lacunar infarcts seen on imaging.",
        "clinical_correlation": "Patients typically present with migraine with aura, mood disturbances, and eventual cognitive impairment. The cerebrovascular insufficiency due to microangiopathy manifests as lacunar strokes, which are central to the clinical presentation of CADASIL.",
        "diagnostic_approach": "The most specific diagnostic test is genetic testing for NOTCH3 mutations. Supportive findings include MRI features such as white matter hyperintensities (especially in the anterior temporal lobes), but these are not definitive. Skin biopsy can show GOM deposits but has less sensitivity and specificity, and is reserved for equivocal cases. Differential diagnoses include other causes of small vessel disease such as sporadic lacunar stroke, multiple sclerosis, and other hereditary leukoencephalopathies.",
        "classification_and_neurology": "CADASIL is classified under hereditary cerebral small vessel diseases (CSVD). It is an autosomal dominant arteriopathy caused by NOTCH3 mutations. Within the nosology of CSVD, CADASIL is the most common monogenic form.  Classification frameworks include: - **Hereditary vs. sporadic CSVD:** CADASIL is hereditary. - **Genetic subtype of CSVD:** NOTCH3 mutation-related. - **Pathological subtype:** Arteriopathy with VSMC degeneration and GOM deposits.  Other hereditary small vessel diseases include CARASIL (recessive, HTRA1 mutations), Fabry disease, and COL4A1-related angiopathy. The consensus classification emphasizes genetic and pathological distinctions, aiding diagnosis and management.  Controversies exist regarding overlap with sporadic CSVD and the phenotypic spectrum, but CADASIL remains a distinct clinical and genetic entity.",
        "classification_and_nosology": "CADASIL is classified as a hereditary arteriopathy affecting cerebral small vessels. It falls under the broader group of vascular cognitive impairment and hereditary stroke disorders.",
        "management_principles": "There is no cure for CADASIL; treatment is supportive and aims to manage symptoms and prevent complications. Migraine is managed symptomatically, while vascular risk factor modification (e.g., controlling blood pressure, avoiding smoking) is crucial. Genetic counseling is important for affected families. In pregnancy and lactation, careful coordination is necessary to manage migraines and vascular risk factors with medications that are safe for the fetus or infant.",
        "option_analysis": "Option B (genetic testing for NOTCH3 mutations) is correct because it is the definitive diagnostic modality. Option A (skin biopsy) is only supportive and is less sensitive and specific. Option C (MRI alone) reveals characteristic but nonspecific findings that overlap with other small vessel pathologies. Option D (CSF analysis) and Option E (routine blood tests) are non-diagnostic in CADASIL.",
        "clinical_pearls": "1. NOTCH3 gene mutation testing is the gold standard for diagnosing CADASIL. 2. MRI commonly shows white matter hyperintensities with a predilection for the anterior temporal lobes. 3. Skin biopsy can be used when genetic testing is inconclusive but is not first-line.",
        "current_evidence": "Recent guidelines reaffirm the importance of genetic testing for CADASIL given its specificity. Advances in imaging have helped in raising suspicion, but the definitive diagnosis continues to rely on molecular methods. Research continues into targeted therapies and better risk factor management although treatment remains largely supportive."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993001",
    "fields": {
      "question_number": "243",
      "question_text": "TIA with severe ICA stenosis (symptomatic side), what to do?",
      "options": {
        "A": "Angioplasty plus stenting",
        "B": "Male 50 shunting",
        "C": "Otherwise endarterectomy"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Acute neurologic events such as transient ischemic attacks (TIAs) in the context of severe internal carotid artery (ICA) stenosis require prompt evaluation to prevent a full-blown stroke. Symptomatic high-grade ICA stenosis has been shown to benefit significantly from surgical intervention.",
        "pathophysiology": "Atherosclerotic plaque buildup in the ICA can lead to severe stenosis, which predisposes to embolic events. In symptomatic patients, the unstable plaque can cause TIAs or strokes due to embolization or hemodynamic compromise.",
        "clinical_correlation": "Patients with severe, symptomatic ICA stenosis may have transient focal neurological deficits corresponding to the affected vascular territory. The presence of TIA in this setting is a warning sign for an impending stroke.",
        "diagnostic_approach": "Initial evaluation includes carotid duplex ultrasonography to determine the degree of stenosis, followed by confirmatory imaging such as CT angiography (CTA) or magnetic resonance angiography (MRA). Differential diagnoses include intracranial atherosclerosis, cardioembolic stroke, and small vessel disease, which can be differentiated based on imaging and clinical findings.",
        "classification_and_neurology": "Symptomatic carotid artery stenosis falls under the broader classification of large artery atherosclerotic cerebrovascular disease, a subtype of ischemic stroke etiologies per the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system. The degree of stenosis is commonly classified using the NASCET (North American Symptomatic Carotid Endarterectomy Trial) criteria, which quantifies percent luminal narrowing based on angiographic measurements. Severe stenosis is typically defined as \u226570% narrowing. The management classification distinguishes symptomatic from asymptomatic stenosis, with symptomatic status conferring higher stroke risk and influencing treatment decisions. Over time, classification systems have evolved to incorporate imaging modalities and clinical features to better stratify risk and guide therapy. Controversies remain regarding management thresholds for asymptomatic stenosis, but consensus strongly supports intervention in symptomatic severe stenosis.",
        "classification_and_nosology": "Carotid artery stenosis is categorized based on the percentage of luminal narrowing. Symptomatic stenosis, particularly when severe (>70%), is an indication for invasive intervention.",
        "management_principles": "For patients with symptomatic severe ICA stenosis, carotid endarterectomy (CEA) is the first-line treatment as recommended by current guidelines (e.g., American Heart Association/American Stroke Association). Carotid angioplasty plus stenting (CAS) is generally reserved for patients who are poor surgical candidates or have specific anatomical considerations. In pregnancy, intervention requires multidisciplinary coordination, as both surgery and stenting carry risks; management should minimize exposure to radiation and contrast, and timing of intervention may be modified until postpartum if feasible.",
        "option_analysis": "Option A (angioplasty plus stenting) is a less favored first-line therapy in typical cases unless the patient is a high surgical risk. Option B (male 50 shunting) appears to be irrelevant and not supported by guidelines. Option C (endarterectomy) is the guideline-supported intervention for symptomatic severe ICA stenosis and is therefore correct.",
        "clinical_pearls": "1. Carotid endarterectomy is the treatment of choice for patients with symptomatic carotid stenosis >70%. 2. Careful patient selection is essential when considering surgical versus endovascular approaches. 3. Noninvasive imaging (duplex ultrasound, CTA, MRA) plays a critical role in evaluation.",
        "current_evidence": "Recent updates in vascular stroke guidelines continue to support the use of CEA in symptomatic patients with high-grade stenosis. Endovascular approaches remain secondary options for those deemed high risk for surgery, and ongoing trials are comparing long-term outcomes between surgical and stenting approaches."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993002",
    "fields": {
      "question_number": "244",
      "question_text": "Case scenario about Weber's syndrome, where is the lesion?",
      "options": {
        "A": "Midbrain basis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Weber's syndrome is a classic brainstem stroke syndrome that involves the midbrain. It is characterized by an ipsilateral oculomotor nerve (CN III) palsy and contralateral hemiparesis, making localization of the lesion to the midbrain crucial.",
        "pathophysiology": "A lesion at the level of the midbrain basis (specifically in the cerebral peduncle region) can compromise both the oculomotor nerve fibers and the corticospinal tracts. Infarctions in this area typically result from occlusion of perforating branches of the posterior cerebral or superior cerebellar arteries.",
        "clinical_correlation": "Clinically, patients present with a combination of ipsilateral ptosis, pupil dilation, and eye movement deficits along with contralateral weakness/hemiparesis. This pattern allows for precise neuroanatomic localization, linking clinical findings to a lesion in the midbrain.",
        "diagnostic_approach": "Diagnosis is primarily based on clinical examination supported by neuroimaging (MRI) which can confirm an infarct in the midbrain. Differential diagnoses include other brainstem syndromes (e.g., Benedikt's syndrome, Claude's syndrome) which have differing clinical features depending on the exact anatomic involvement.",
        "classification_and_neurology": "Weber's syndrome is classified as one of the midbrain syndromes within the broader category of brainstem stroke syndromes. Brainstem strokes are subclassified based on anatomical location (midbrain, pons, medulla) and vascular territory (paramedian, circumferential, perforating arteries). Weber's syndrome specifically involves the ventral midbrain and is considered a paramedian midbrain syndrome. It belongs to the family of 'crossed hemiplegia' syndromes, where cranial nerve palsy is ipsilateral and motor weakness contralateral. Historically, midbrain syndromes include Weber's, Benedikt's, Claude's, and Nothnagel's syndromes, each with distinct lesion localization and clinical features. Contemporary classification emphasizes vascular territories and neuroimaging correlations, refining the nosology to guide diagnosis and management. There is consensus that Weber's syndrome represents a lesion in the midbrain basis affecting corticospinal tracts and the oculomotor nerve fascicles.",
        "classification_and_nosology": "Weber's syndrome falls under the group of midbrain stroke syndromes and is categorized based on its clinical manifestations (ipsilateral CN III palsy with contralateral motor deficits).",
        "management_principles": "Management is generally supportive and follows standard ischemic stroke protocols including antiplatelet therapy, management of risk factors, and rehabilitation. In the setting of acute stroke, thrombolytic therapy may be considered if the patient meets criteria. In pregnancy and lactation, the choice of thrombolytic agents and supportive medications should be made with fetal/infant safety in mind.",
        "option_analysis": "Option A (midbrain basis) is correct because Weber's syndrome is caused by infarction or a lesion in the ventral midbrain. Other choices, if provided, would likely refer to non-matching locations (e.g., pons, thalamus) and are therefore incorrect.",
        "clinical_pearls": "1. Weber's syndrome is a midbrain stroke characterized by ipsilateral third nerve palsy and contralateral hemiparesis. 2. The lesion is located in the ventral midbrain (basis pedunculi). 3. Differential diagnosis should include other midbrain syndromes which may have overlapping yet distinct features.",
        "current_evidence": "Current neuroimaging modalities, especially high-resolution MRI, continue to assist in the rapid localization and confirmation of brainstem strokes linked to syndromes like Weber's. Updated stroke guidelines underscore the importance of swift diagnosis and management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993003",
    "fields": {
      "question_number": "245",
      "question_text": "A case of acute ischemic stroke, BP is 193/103, what to do next?",
      "options": {
        "A": "IV labetalol",
        "B": "IV nitroprusside",
        "C": "Observation",
        "D": "Resume home medications"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "In the setting of acute ischemic stroke, elevated blood pressure is common and is part of the body\u2019s physiological response to maintain cerebral perfusion. Management of blood pressure is nuanced and depends on whether the patient is eligible for reperfusion therapies.",
        "pathophysiology": "After an ischemic stroke, autoregulation of cerebral blood flow is impaired, and permissive hypertension helps support penumbral tissue. Aggressive blood pressure reduction can potentially worsen ischemia in the affected areas.",
        "clinical_correlation": "A patient who presents with an acute ischemic stroke and a blood pressure of 193/103 mm Hg falls within the range tolerated in patients not eligible for thrombolytic therapy. If the patient is not undergoing reperfusion treatment, the elevated blood pressure is typically not immediately lowered unless it exceeds thresholds (commonly 220/120 mm Hg).",
        "diagnostic_approach": "Blood pressure management in stroke is guided by clinical criteria and imaging findings. Differential considerations include hemorrhagic stroke (where blood pressure control is more aggressive) versus ischemic stroke. In ischemic stroke, neuroimaging (CT/MRI) distinguishes between these conditions and directs management.",
        "classification_and_neurology": "Acute ischemic stroke is classified etiologically by systems such as the TOAST classification (Trial of Org 10172 in Acute Stroke Treatment), which categorizes strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and cryptogenic stroke. Blood pressure management in acute ischemic stroke is a component of acute stroke care protocols rather than a disease classification per se. The approach to BP management is integrated into stroke care guidelines by bodies such as the American Heart Association/American Stroke Association (AHA/ASA). These guidelines classify BP management strategies based on timing (acute vs subacute), stroke type (ischemic vs hemorrhagic), and treatment eligibility (e.g., thrombolysis).",
        "classification_and_nosology": "Acute ischemic stroke management is stratified by whether patients are candidates for thrombolytic therapy (IV tPA) or mechanical thrombectomy, each of which has specific blood pressure targets.",
        "management_principles": "For ischemic stroke patients not receiving thrombolytic therapy, current guidelines recommend tolerating higher blood pressures (up to 220/120 mm Hg)\u2014this is known as permissive hypertension. If the patient were eligible for IV tPA, blood pressure would need to be lowered to below 185/110 mm Hg using agents like IV labetalol before therapy. In pregnancy, blood pressure management must consider maternal and fetal safety, with agents like labetalol and hydralazine often preferred; however, if the stroke is not treated with thrombolysis, similar permissive limits may apply under close monitoring.",
        "option_analysis": "Option A (IV labetalol) would be indicated if the patient were a candidate for thrombolysis, as the blood pressure would need to be reduced to a safe level (<185/110 mm Hg). Option B (IV nitroprusside) is not typically used in acute ischemic stroke due to its potent and unpredictable effects on cerebral blood flow. Option C (Observation) is correct in a scenario where the patient is not receiving reperfusion therapy because the blood pressure is within the acceptable range for permissive hypertension. Option D (Resume home medications) is nonspecific and does not directly address the acute management of blood pressure in a stroke setting.",
        "clinical_pearls": "1. Permissive hypertension (up to 220/120 mm Hg) is generally allowed in acute ischemic stroke patients who are not candidates for reperfusion therapy. 2. For patients eligible for IV tPA, blood pressure must be carefully lowered to below 185/110 mm Hg before administration. 3. Monitoring and gradual reduction, when indicated, minimize the risk of compromising cerebral perfusion.",
        "current_evidence": "Recent guidelines continue to support a conservative approach to blood pressure management in acute ischemic stroke for non-thrombolysis candidates. There is ongoing research into optimal blood pressure targets during the hyperacute phase of stroke, balancing the risks of recurrent ischemia against the potential harms of aggressive blood pressure lowering."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993004",
    "fields": {
      "question_number": "246",
      "question_text": "Patient has recurrent headache and TIAs, he did cerebral angio which showed the following, what is the most likely diagnosis?",
      "options": {
        "B": "(assumed to be Moyamoya disease) is correct if the angiography reveals progressive stenosis of the terminal internal carotid arteries with prominent collateral vessels. Other options can be excluded as follows: \u2022 Atherosclerosis typically shows focal stenosis in older individuals. \u2022 Arterial dissection would present acutely with a tear, often along the cervical vessels. \u2022 Vasculitis tends to have systemic inflammatory markers and multifocal segmental narrowing. \u2022 Fibromuscular dysplasia classically displays a 'string\u2010of\u2010beads' pattern rather than the \u201cpuff\u2010of\u2010smoke\u201d appearance."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This question asks you to identify an arteriopathy on cerebral angiography in a patient with recurrent headaches and transient ischemic attacks (TIAs). In such cases, several vascular conditions (e.g., atherosclerosis, dissection, vasculitis, fibromuscular dysplasia, and Moyamoya disease) are considered; the key lies in recognizing characteristic imaging patterns.",
        "pathophysiology": "Moyamoya disease is characterized by progressive stenosis of the distal internal carotid arteries and their proximal branches. In response to the reduced blood flow, a network of transdural collateral vessels develops. On angiography, these collaterals appear as a hazy \u201cpuff\u2010of\u2010smoke\u201d pattern. This abnormal vasculature predisposes patients to recurrent TIAs and strokes, and headache is a common accompanying symptom.",
        "clinical_correlation": "Patients may present with recurrent transient neurological deficits (TIAs) and headaches. Although Moyamoya is classically described in children, it also occurs in young to middle\u2010aged adults and may have variable presentations including ischemic or hemorrhagic strokes.",
        "diagnostic_approach": "Cerebral angiography remains the gold standard. Differential diagnoses include: \u2022 Large artery atherosclerosis (typically seen in older patients with classic risk factors) \u2022 Arterial dissection (often with an intimal flap or double lumen appearance) \u2022 Vasculitis (with segmental narrowing and beading, often accompanied by systemic signs) \u2022 Fibromuscular dysplasia (showing a \u201cstring\u2010of\u2010beads\u201d pattern). The pattern of progressive stenosis with the development of a network of abnormal collateral vessels helps differentiate Moyamoya.",
        "classification_and_neurology": "Cerebrovascular diseases causing TIAs and headaches fall under the broader category of ischemic cerebrovascular disorders in the WHO classification. The TOAST classification further categorizes ischemic stroke/TIA etiologies into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Angiographic findings help classify patients into these subtypes. For example, focal stenosis suggests large artery atherosclerosis, while normal angiography with clinical TIAs may indicate small vessel or cardioembolic causes. The classification of vascular headaches includes migraine, cluster headache, and secondary headaches attributed to vascular disorders. Understanding these taxonomies helps tailor diagnosis and treatment. Emerging classifications incorporate vessel wall imaging and molecular markers to refine nosology.",
        "classification_and_nosology": "Moyamoya disease is considered an idiopathic, primary vasculopathy. When similar angiographic findings are seen in association with other systemic conditions (e.g., sickle cell disease, neurofibromatosis type I), the term Moyamoya syndrome is used.",
        "management_principles": "The first\u2010line management for symptomatic Moyamoya disease is surgical revascularization (either direct, such as superficial temporal artery to middle cerebral artery bypass, or indirect techniques). Medical management (including antiplatelet agents) is mainly supportive. In pregnant or lactating women, the decision for surgical intervention is individualized, with careful coordination between neurosurgery, obstetrics, and neurology to minimize fetal radiation exposure and optimize maternal outcomes.",
        "option_analysis": "Although the exact options are not provided, the differential includes several entities. Option B (assumed to be Moyamoya disease) is correct if the angiography reveals progressive stenosis of the terminal internal carotid arteries with prominent collateral vessels. Other options can be excluded as follows: \u2022 Atherosclerosis typically shows focal stenosis in older individuals. \u2022 Arterial dissection would present acutely with a tear, often along the cervical vessels. \u2022 Vasculitis tends to have systemic inflammatory markers and multifocal segmental narrowing. \u2022 Fibromuscular dysplasia classically displays a 'string\u2010of\u2010beads' pattern rather than the \u201cpuff\u2010of\u2010smoke\u201d appearance.",
        "clinical_pearls": "\u2022 Moyamoya means 'puff\u2010of\u2010smoke' in Japanese \u2013 a reference to its characteristic angiographic appearance. \u2022 Recurrent TIAs and headaches in a younger patient should prompt consideration of Moyamoya, especially when imaging shows extensive collateralization. \u2022 Differentiating Moyamoya from other arteriopathies is crucial since surgical revascularization can significantly improve outcomes.",
        "current_evidence": "Recent literature supports early surgical revascularization for symptomatic Moyamoya disease to reduce the risk of stroke. The updated guidelines emphasize the importance of high\u2010quality vascular imaging for diagnosis and advocate for a multidisciplinary approach to management, including considerations during pregnancy where imaging and surgical timing are carefully planned."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993005",
    "fields": {
      "question_number": "247",
      "question_text": "82-year-old woman came with acute ischemic stroke (2 hours onset) with partial improvement of her deficit?",
      "options": {
        "A": "Give IV tPA"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This question deals with the management of acute ischemic stroke in an elderly patient who shows partial improvement early in the time window. The decision to administer intravenous thrombolysis (IV tPA) depends on the severity and functional impact of the residual deficits.",
        "pathophysiology": "Acute ischemic stroke results from an occlusion of a cerebral vessel leading to ischemia of the brain tissue. In some patients, spontaneous recanalization or the natural evolution of the thrombus can result in partial clinical improvement. However, the risk of hemorrhagic transformation with thrombolytic therapy remains, and the net benefit must be weighed based on the disability of the remaining deficits.",
        "clinical_correlation": "An 82\u2010year-old patient may present with stroke symptoms that begin to improve spontaneously. The key consideration is whether the residual deficits are disabling. \u2018Rapid improvement\u2019 or minimal deficits might suggest that the risks of IV tPA (notably intracranial hemorrhage) may outweigh the benefits.",
        "diagnostic_approach": "A thorough neurological exam, often quantified by the NIH Stroke Scale (NIHSS), is used to determine the severity of stroke. Differential considerations include a transient ischemic attack (TIA) versus a minor stroke. Brain imaging (CT/MRI) is also used to rule out hemorrhage before considering IV tPA.",
        "classification_and_neurology": "Acute ischemic stroke is classified etiologically by the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. The current classification system incorporates clinical, imaging, and laboratory data to guide management. AIS belongs to the broader category of cerebrovascular diseases within neurology. The evolution of classification emphasizes precision medicine approaches, including molecular biomarkers and advanced imaging to tailor reperfusion strategies. Controversies exist regarding extended time windows and patient selection for thrombolysis and thrombectomy, leading to evolving guidelines.",
        "classification_and_nosology": "Strokes can be classified using the TOAST criteria, and minor stroke or rapidly improving symptoms represent a subgroup where treatment decisions with thrombolysis are more nuanced.",
        "management_principles": "For patients within 4.5 hours of onset with disabling deficits, IV tPA remains the first\u2010line treatment. However, in patients with mild or rapidly improving symptoms that are deemed non\u2010disabling, the benefit of IV tPA is less clear. In such cases, supportive care and observation may be preferred. In pregnant or lactating patients, the use of IV tPA is considered when the benefits significantly outweigh the risks, with careful monitoring and adjustments to minimize potential adverse effects.",
        "option_analysis": "\u2022 Option A (Give IV tPA) is the standard for acute ischemic strokes with significant, disabling deficits. However, in this scenario the patient shows partial improvement, suggesting that the deficit may now be minor or non\u2010disabling. \u2022 Option B (the marked answer) is assumed to represent conservative management (i.e., withholding IV tPA) when the residual deficit is not clinically disabling. Given the ambiguity in the clinical improvement, many clinicians choose not to expose patients to the risk of hemorrhage if the deficit is minimal. Thus, the marked answer is appropriate provided that the residual deficit is indeed non\u2010disabling.",
        "clinical_pearls": "\u2022 Always assess the degree of residual disability \u2013 even if a patient shows some improvement, a significant functional impairment warrants thrombolysis. \u2022 There is no strict age cutoff for IV tPA; decisions should be based on the balance of risks and benefits. \u2022 \u2018Rapid improvement\u2019 does not automatically preclude treatment, but if the symptoms are minor and not disabling, observation may be appropriate.",
        "current_evidence": "Recent studies have highlighted that patients with minor or rapidly improving symptoms often do well with conservative management, though it is recognized that a subset may deteriorate. Current guidelines recommend individualized assessment of disability rather than relying solely on the degree of improvement, with ongoing research into objective measures to guide thrombolytic use in this group."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993006",
    "fields": {
      "question_number": "248",
      "question_text": "Patient developed ischemic stroke, his echo showed intracardiac thrombus as part of stroke work up what is the best option for secondary prevention of stroke?",
      "options": {
        "A": "Warfarin",
        "B": "NOACs",
        "C": "Aspirin",
        "D": "Clopidogrel"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This question focuses on the secondary prevention of cardioembolic stroke in a patient whose workup (via echocardiography) revealed an intracardiac thrombus. The prevention strategy in such settings is aimed at reducing further embolic events.",
        "pathophysiology": "An intracardiac thrombus, often formed in areas of regional akinesis or dyskinesis (such as post-myocardial infarction), can dislodge and embolize to the cerebral circulation, causing ischemic stroke. Anticoagulants decrease thrombin production and clot propagation, thereby reducing embolic risk.",
        "clinical_correlation": "Patients with cardioembolic strokes typically present with sudden onset focal neurological deficits. Echocardiography is used to identify intracardiac sources of emboli. The discovery of a thrombus mandates anticoagulation to prevent recurrent embolization.",
        "diagnostic_approach": "Once a stroke is identified, workup includes brain imaging to identify the ischemic territory and cardiac imaging (transthoracic or transesophageal echo) to evaluate for intracardiac thrombi. Differential diagnoses include atherosclerotic stroke (where antiplatelet therapy is preferred) and paradoxical emboli (which may require further investigation for a patent foramen ovale).",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology using systems such as TOAST (Trial of Org 10172 in Acute Stroke Treatment). Cardioembolic stroke is a major subtype characterized by emboli originating from the heart. This subtype includes emboli from atrial fibrillation, valvular heart disease, intracardiac thrombi, and prosthetic valves. The presence of an intracardiac thrombus places the stroke firmly in the cardioembolic category, which guides management. The classification informs prognosis and treatment; cardioembolic strokes have higher recurrence risk and benefit from anticoagulation. Over time, classification systems have evolved to integrate imaging and cardiac findings, enhancing diagnostic accuracy. Controversies exist regarding anticoagulation in certain subgroups, but consensus supports anticoagulation in intracardiac thrombus-related strokes.",
        "classification_and_nosology": "Cardioembolic strokes are one of the subtypes in the TOAST classification. They are specifically linked to sources within the heart such as atrial fibrillation, left ventricular thrombus, or valvular disease.",
        "management_principles": "For secondary prevention in patients with a documented intracardiac thrombus, anticoagulation is the cornerstone. Warfarin (a vitamin K antagonist) has been the traditional first-line agent, given its proven efficacy in preventing systemic embolization. Novel oral anticoagulants (NOACs) are used in non-valvular atrial fibrillation, but their use in patients with intracardiac thrombus has less robust evidence. In pregnant patients, warfarin is contraindicated, particularly in the first trimester due to fetal teratogenicity; low molecular weight heparin is preferred during pregnancy and lactation.",
        "option_analysis": "\u2022 Option A (Warfarin) is correct because it effectively prevents thrombus propagation in patients with intracardiac thrombus. \u2022 Option B (NOACs) are currently less established for this specific indication despite their success in atrial fibrillation. \u2022 Options C (Aspirin) and D (Clopidogrel) are antiplatelet agents that do not adequately address the risk of thromboembolism from an intracardiac clot.",
        "clinical_pearls": "\u2022 Always evaluate for an intracardiac source in stroke patients when indicated, as management differs significantly from atherosclerotic stroke. \u2022 Warfarin remains the first-line anticoagulant for confirmed intracardiac thrombus unless contraindicated. \u2022 In women of childbearing age or those who are pregnant/lactating, consider alternative anticoagulation strategies.",
        "current_evidence": "Recent guidelines reaffirm the role of warfarin for patients with intracardiac thrombus. Although NOACs have become popular for non-valvular atrial fibrillation, their role in intracardiac thrombus is less clear, and ongoing trials seek to clarify their safety and efficacy in this indication."
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
