
# Import batch 2 of 3 from chunk_1_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99992982",
    "fields": {
      "question_number": "186",
      "question_text": "Patient 50 male, has DM, HTN, smoker, 3 days he has acute stroke at home, what is the artery involved?",
      "options": {
        "A": "ICA stenosis",
        "B": "Aortic atheroma",
        "C": "Hypercoagulable state",
        "D": "Lenticulostriate arteries"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This question focuses on identifying the most common arterial territory involved in lacunar strokes, which are a type of small vessel disease commonly seen in patients with vascular risk factors such as diabetes, hypertension, and smoking.",
        "pathophysiology": "Lacunar strokes result from lipohyalinosis and microatheroma formation in the small penetrating arteries, particularly the lenticulostriate arteries, which supply the deep structures of the brain (e.g., basal ganglia and internal capsule). These occlusions lead to small, deep infarcts.",
        "clinical_correlation": "In a 50\u2010year\u2010old male with diabetes, hypertension, and a smoking history, lacunar strokes are common. Symptoms typically involve pure motor or sensory deficits, depending on the location of the infarct. The lenticulostriate arteries are most commonly implicated in such cases.",
        "diagnostic_approach": "Diagnosis is primarily clinical, supported by neuroimaging. CT or MRI may show small, deep infarcts in the territory of the lenticulostriate arteries. Differential diagnoses include embolic strokes from larger vessels (e.g., due to ICA stenosis) or cardioembolic sources, which usually affect cortical regions.",
        "classification_and_neurology": "Ischemic strokes are classified by the TOAST criteria into five subtypes: large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This patient\u2019s presentation fits the small vessel occlusion subtype, caused by occlusion of small penetrating arteries like the lenticulostriate arteries. Small vessel disease is a distinct pathological entity characterized by lacunar infarcts and white matter changes. Large artery atherosclerosis includes ICA stenosis and MCA disease. Embolic strokes arise from cardiac or aortic sources. The classification helps guide prognosis and management. Over time, imaging advances have refined the nosology by correlating lesion size and location with etiologies. Some debate persists regarding overlap between small vessel disease and embolic mechanisms, but clinical and imaging features aid distinction.",
        "classification_and_nosology": "Lacunar strokes are classified under ischemic strokes and represent a subgroup of small vessel disease. They are distinct from large vessel and embolic strokes based on their pathologic mechanism and vascular territory.",
        "management_principles": "Management focuses on secondary prevention: aggressive control of hypertension, diabetes, and cessation of smoking, along with antiplatelet therapy. There is no role for thrombolysis beyond the acute period if the patient presents late. Pregnancy and lactation considerations are not typically relevant in this demographic.",
        "option_analysis": "Option D (Lenticulostriate arteries) is correct because these small penetrating vessels are the most frequently affected in lacunar strokes. Option A (ICA stenosis) and Option B (Aortic atheroma) are more commonly associated with embolic or large vessel strokes, while Option C (Hypercoagulable state) is not the typical cause in a patient with conventional vascular risk factors.",
        "clinical_pearls": "1. Lacunar strokes are the result of small vessel disease and typically occur in patients with hypertension and diabetes. 2. The lenticulostriate arteries are the classic site of involvement. 3. Management is centered on risk factor modification and secondary prevention.",
        "current_evidence": "Recent research reaffirms the crucial role of intensive risk factor management in reducing the recurrence of lacunar strokes. Current guidelines continue to advocate for stringent blood pressure, glycemic, and lipid management in these patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992983",
    "fields": {
      "question_number": "187",
      "question_text": "Case of acute stroke patient has left gaze preference when he tries to look to the right cannot cross, what other finding in exam:",
      "options": {
        "A": "Right upper motor neuron facial palsy",
        "B": "Right lower motor neuron facial palsy",
        "C": "Left upper motor neuron facial palsy",
        "D": "Oculomotor nerve"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the understanding of neurologic exam findings in stroke patients, especially the implications of gaze preference and associated cranial nerve deficits.",
        "pathophysiology": "In a cortical stroke involving the frontal eye field, there is a loss of the voluntary contralateral gaze. The patient\u2019s eyes deviate towards the side of the lesion (due to unopposed action of the intact contralateral eye field). In a left hemisphere stroke, this results in a left gaze preference, accompanied by right-sided motor deficits, including a contralateral upper motor neuron facial palsy.",
        "clinical_correlation": "A patient with an acute stroke and left gaze preference is likely to have a left hemispheric lesion. Consequently, the motor pathways, including fibers controlling the lower face, are affected, leading to a right upper motor neuron (UMN) facial palsy. UMN lesions typically spare the forehead due to bilateral cortical innervation.",
        "diagnostic_approach": "The diagnosis is based on focal neurological deficits on examination and confirmed by neuroimaging (CT or MRI) to localize the lesion. Differential diagnoses might include brainstem strokes (which may involve cranial nerve findings) and other causes of gaze palsies. However, the presence of an UMN facial palsy and gaze preference points to a cortical process.",
        "classification_and_neurology": "This clinical presentation falls under the classification of ischemic stroke within the cerebrovascular disease spectrum. The lesion is localized to the anterior circulation, specifically the territory of the left MCA, affecting cortical and subcortical motor pathways. Stroke classification systems such as the TOAST criteria categorize strokes by etiology (large artery atherosclerosis, cardioembolism, small vessel disease, etc.), while the OCSP classification (Oxford Community Stroke Project) categorizes strokes by clinical syndromes (e.g., partial anterior circulation infarct). This case fits a partial anterior circulation infarct with cortical signs (gaze preference, facial palsy) and motor deficits. Understanding these classifications aids in prognosis and management planning.",
        "classification_and_nosology": "Stroke is categorized based on its vascular territory. Cortical strokes, which affect the frontal eye field and corticobulbar tracts, present with features such as gaze deviation and contralateral UMN facial weakness.",
        "management_principles": "Management is tailored to the underlying stroke etiology. Acute ischemic strokes are managed with reperfusion therapy (IV tPA within the therapeutic window) and supportive care. In this exam finding, the focus is on clinical localization rather than immediate management changes. Pregnancy and lactation considerations are not typically relevant in this scenario.",
        "option_analysis": "Option A (Right upper motor neuron facial palsy) is correct because a left hemispheric lesion causes contralateral facial weakness in an UMN pattern. Option B (Right lower motor neuron facial palsy) is incorrect since LMN lesions would have a different distribution and etiology. Option C (Left upper motor neuron facial palsy) would be ipsilateral to the gaze preference and does not fit with the contralateral deficit expected. Option D (Oculomotor nerve involvement) would present with additional findings (such as ptosis and pupillary abnormalities) that are not described in this case.",
        "clinical_pearls": "1. In cortical strokes, gaze preference is typically toward the side of the lesion. 2. An upper motor neuron facial palsy will present contralaterally to a hemispheric lesion. 3. The frontal eye field plays a critical role in directing voluntary gaze, and its impairment leads to characteristic exam findings.",
        "current_evidence": "Recent studies have reinforced the value of a detailed neurologic exam in localizing stroke lesions. Current guidelines emphasize a rapid clinical assessment to guide urgent imaging and treatment decisions in acute stroke management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992984",
    "fields": {
      "question_number": "188",
      "question_text": "Patient with history of acute SAH, (no mention of hydrocephalus) CT angiography showed posterior communicating aneurysm what to do next:",
      "options": {
        "A": "Craniotomy with clipping",
        "B": "Endovascular coiling",
        "C": "Observation"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Aneurysmal subarachnoid hemorrhage (SAH) is a neurosurgical emergency in which the ruptured aneurysm must be secured promptly to prevent rebleeding. Two primary methods to secure the aneurysm are surgical clipping (via craniotomy) and endovascular coiling. The choice depends on the aneurysm\u2019s morphology, location, and patient factors.",
        "pathophysiology": "After rupture, the aneurysm can rebleed due to high intraluminal pressures. Endovascular coiling involves advancing microcatheters into the aneurysm and depositing coils made of platinum to cause thrombosis within the sac, thereby excluding it from the circulation. This minimally invasive technique reduces the risk of rebleeding while avoiding a craniotomy in selected patients.",
        "clinical_correlation": "Patients with SAH often present with a sudden, severe headache (often described as \u2018the worst headache of my life\u2019), vomiting, and sometimes loss of consciousness. Once SAH is diagnosed (typically with a non\u2010contrast head CT), CT angiography is used to identify the aneurysm. In patients with a ruptured posterior communicating artery aneurysm, securing the aneurysm is urgent to prevent rebleeding and secondary complications such as vasospasm.",
        "diagnostic_approach": "The initial diagnostic evaluation starts with a non\u2010contrast CT scan which is highly sensitive for SAH in the first 24 hours. CT angiography helps localize and characterize the aneurysm. Differential diagnoses include perimesencephalic nonaneurysmal hemorrhage and traumatic SAH. The presence of an aneurysm on imaging directs the management toward definitive aneurysm repair.",
        "classification_and_neurology": "Aneurysmal SAH is classified within the broader category of hemorrhagic stroke. It is distinguished from non-aneurysmal (perimesencephalic) SAH by etiology and prognosis. The International Subarachnoid Aneurysm Trial (ISAT) classification and other systems categorize aneurysms by size, location, and morphology to guide treatment. PCOM aneurysms are part of anterior circulation aneurysms, which are more common than posterior circulation aneurysms. The nosology includes differentiating ruptured versus unruptured aneurysms, with ruptured requiring immediate management. The classification systems have evolved with advances in imaging and endovascular techniques, shifting management paradigms from surgical clipping dominance to increased use of coiling. Controversies remain regarding optimal treatment for certain aneurysm types and patient subgroups.",
        "classification_and_nosology": "Cerebral aneurysms can be classified by their location (e.g., anterior communicating, posterior communicating, etc.), morphology, and rupture status. A ruptured posterior communicating artery aneurysm falls within the spectrum of saccular (berry) aneurysms, which are responsible for most cases of non\u2010traumatic SAH.",
        "management_principles": "First-line management is to secure the aneurysm as soon as possible. Endovascular coiling is recommended for many aneurysms, particularly those in locations like the posterior communicating artery if the anatomical configuration is favorable. Surgical clipping remains an option, especially in younger patients or those whose lesions are not amenable to a safe endovascular approach. In pregnant patients, minimizing radiation exposure is critical; clipping may be considered if endovascular procedures are deemed to have higher fetal risk, though protective shielding and dose minimization strategies can allow endovascular therapy if indicated.",
        "option_analysis": "Option A (Craniotomy with clipping) is a standard, valid treatment but may involve a more invasive approach with longer recovery in selected cases. Option B (Endovascular coiling) is the marked answer and is widely accepted for appropriate aneurysm morphology, offering a less invasive treatment with decreased perioperative morbidity. Option C (Observation) is not acceptable in the setting of a ruptured aneurysm due to the high risk of rebleeding.",
        "clinical_pearls": "\u2022 Securing the aneurysm early after SAH is critical to reduce rebleeding risk. \u2022 Endovascular coiling, supported by trials such as ISAT, has become a mainstay for many aneurysms. \u2022 The choice between clipping and coiling is individualized based on aneurysm anatomy and patient factors.",
        "current_evidence": "Current guidelines and studies, particularly the International Subarachnoid Aneurysm Trial (ISAT), support endovascular coiling in appropriately selected patients due to its less invasive nature and favorable outcomes. Ongoing research continues to refine patient selection criteria and procedural techniques."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992985",
    "fields": {
      "question_number": "189",
      "question_text": "ICH case in basal ganglia regarding target blood pressure:",
      "options": {
        "A": "160/100",
        "B": "140/90"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Aneurysmal subarachnoid hemorrhage (SAH) is a neurosurgical emergency in which the ruptured aneurysm must be secured promptly to prevent rebleeding. Two primary methods to secure the aneurysm are surgical clipping (via craniotomy) and endovascular coiling. The choice depends on the aneurysm\u2019s morphology, location, and patient factors.",
        "pathophysiology": "After rupture, the aneurysm can rebleed due to high intraluminal pressures. Endovascular coiling involves advancing microcatheters into the aneurysm and depositing coils made of platinum to cause thrombosis within the sac, thereby excluding it from the circulation. This minimally invasive technique reduces the risk of rebleeding while avoiding a craniotomy in selected patients.",
        "clinical_correlation": "Patients with SAH often present with a sudden, severe headache (often described as \u2018the worst headache of my life\u2019), vomiting, and sometimes loss of consciousness. Once SAH is diagnosed (typically with a non\u2010contrast head CT), CT angiography is used to identify the aneurysm. In patients with a ruptured posterior communicating artery aneurysm, securing the aneurysm is urgent to prevent rebleeding and secondary complications such as vasospasm.",
        "diagnostic_approach": "The initial diagnostic evaluation starts with a non\u2010contrast CT scan which is highly sensitive for SAH in the first 24 hours. CT angiography helps localize and characterize the aneurysm. Differential diagnoses include perimesencephalic nonaneurysmal hemorrhage and traumatic SAH. The presence of an aneurysm on imaging directs the management toward definitive aneurysm repair.",
        "classification_and_neurology": "Intracerebral hemorrhage is classified under hemorrhagic strokes within the cerebrovascular disease taxonomy. The basal ganglia hemorrhage subtype is categorized based on anatomical location: deep (basal ganglia, thalamus), lobar, brainstem, or cerebellar. Hypertensive ICH is the most common etiology for deep hemorrhages, differentiating it from lobar hemorrhages often caused by cerebral amyloid angiopathy. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify ICH severity and management strategies based on volume, location, and clinical status. BP management recommendations have evolved with emerging evidence, reflecting a shift from permissive hypertension to more controlled lowering within safe limits. Controversies remain regarding optimal BP targets, but consensus supports individualized approaches based on hemorrhage characteristics and patient factors.",
        "classification_and_nosology": "Cerebral aneurysms can be classified by their location (e.g., anterior communicating, posterior communicating, etc.), morphology, and rupture status. A ruptured posterior communicating artery aneurysm falls within the spectrum of saccular (berry) aneurysms, which are responsible for most cases of non\u2010traumatic SAH.",
        "management_principles": "First-line management is to secure the aneurysm as soon as possible. Endovascular coiling is recommended for many aneurysms, particularly those in locations like the posterior communicating artery if the anatomical configuration is favorable. Surgical clipping remains an option, especially in younger patients or those whose lesions are not amenable to a safe endovascular approach. In pregnant patients, minimizing radiation exposure is critical; clipping may be considered if endovascular procedures are deemed to have higher fetal risk, though protective shielding and dose minimization strategies can allow endovascular therapy if indicated.",
        "option_analysis": "Option A (Craniotomy with clipping) is a standard, valid treatment but may involve a more invasive approach with longer recovery in selected cases. Option B (Endovascular coiling) is the marked answer and is widely accepted for appropriate aneurysm morphology, offering a less invasive treatment with decreased perioperative morbidity. Option C (Observation) is not acceptable in the setting of a ruptured aneurysm due to the high risk of rebleeding.",
        "clinical_pearls": "\u2022 Securing the aneurysm early after SAH is critical to reduce rebleeding risk. \u2022 Endovascular coiling, supported by trials such as ISAT, has become a mainstay for many aneurysms. \u2022 The choice between clipping and coiling is individualized based on aneurysm anatomy and patient factors.",
        "current_evidence": "Current guidelines and studies, particularly the International Subarachnoid Aneurysm Trial (ISAT), support endovascular coiling in appropriately selected patients due to its less invasive nature and favorable outcomes. Ongoing research continues to refine patient selection criteria and procedural techniques."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992986",
    "fields": {
      "question_number": "190",
      "question_text": "Female Patient with left side weakness, diagnose by carotid doppler, With right carotid stenosis 50% and the left 80%, management:",
      "options": {
        "A": "Medical therapy",
        "B": "Left carotid stent",
        "C": "Left endarterectomy",
        "D": "Right carotid stent"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Aneurysmal subarachnoid hemorrhage (SAH) is a neurosurgical emergency in which the ruptured aneurysm must be secured promptly to prevent rebleeding. Two primary methods to secure the aneurysm are surgical clipping (via craniotomy) and endovascular coiling. The choice depends on the aneurysm\u2019s morphology, location, and patient factors.",
        "pathophysiology": "After rupture, the aneurysm can rebleed due to high intraluminal pressures. Endovascular coiling involves advancing microcatheters into the aneurysm and depositing coils made of platinum to cause thrombosis within the sac, thereby excluding it from the circulation. This minimally invasive technique reduces the risk of rebleeding while avoiding a craniotomy in selected patients.",
        "clinical_correlation": "Patients with SAH often present with a sudden, severe headache (often described as \u2018the worst headache of my life\u2019), vomiting, and sometimes loss of consciousness. Once SAH is diagnosed (typically with a non\u2010contrast head CT), CT angiography is used to identify the aneurysm. In patients with a ruptured posterior communicating artery aneurysm, securing the aneurysm is urgent to prevent rebleeding and secondary complications such as vasospasm.",
        "diagnostic_approach": "The initial diagnostic evaluation starts with a non\u2010contrast CT scan which is highly sensitive for SAH in the first 24 hours. CT angiography helps localize and characterize the aneurysm. Differential diagnoses include perimesencephalic nonaneurysmal hemorrhage and traumatic SAH. The presence of an aneurysm on imaging directs the management toward definitive aneurysm repair.",
        "classification_and_neurology": "Carotid artery stenosis is classified based on the degree of luminal narrowing and symptomatology. The North American Symptomatic Carotid Endarterectomy Trial (NASCET) criteria are the standard for measuring stenosis percentage. Stenoses are categorized as mild (<50%), moderate (50-69%), or severe (\u226570%). The condition falls under the broader category of large artery atherosclerosis causing ischemic stroke, per the TOAST classification system. Symptomatic carotid stenosis refers to patients who have experienced ischemic events attributable to the stenotic artery, whereas asymptomatic stenosis is identified incidentally without clinical symptoms. Management guidelines and clinical trials focus primarily on symptomatic high-grade stenosis due to the elevated stroke risk. The classification has evolved to incorporate imaging modalities and clinical presentation to guide therapeutic decisions. Controversies remain regarding treatment thresholds in asymptomatic patients and the choice between endarterectomy and stenting.",
        "classification_and_nosology": "Cerebral aneurysms can be classified by their location (e.g., anterior communicating, posterior communicating, etc.), morphology, and rupture status. A ruptured posterior communicating artery aneurysm falls within the spectrum of saccular (berry) aneurysms, which are responsible for most cases of non\u2010traumatic SAH.",
        "management_principles": "First-line management is to secure the aneurysm as soon as possible. Endovascular coiling is recommended for many aneurysms, particularly those in locations like the posterior communicating artery if the anatomical configuration is favorable. Surgical clipping remains an option, especially in younger patients or those whose lesions are not amenable to a safe endovascular approach. In pregnant patients, minimizing radiation exposure is critical; clipping may be considered if endovascular procedures are deemed to have higher fetal risk, though protective shielding and dose minimization strategies can allow endovascular therapy if indicated.",
        "option_analysis": "Option A (Craniotomy with clipping) is a standard, valid treatment but may involve a more invasive approach with longer recovery in selected cases. Option B (Endovascular coiling) is the marked answer and is widely accepted for appropriate aneurysm morphology, offering a less invasive treatment with decreased perioperative morbidity. Option C (Observation) is not acceptable in the setting of a ruptured aneurysm due to the high risk of rebleeding.",
        "clinical_pearls": "\u2022 Securing the aneurysm early after SAH is critical to reduce rebleeding risk. \u2022 Endovascular coiling, supported by trials such as ISAT, has become a mainstay for many aneurysms. \u2022 The choice between clipping and coiling is individualized based on aneurysm anatomy and patient factors.",
        "current_evidence": "Current guidelines and studies, particularly the International Subarachnoid Aneurysm Trial (ISAT), support endovascular coiling in appropriately selected patients due to its less invasive nature and favorable outcomes. Ongoing research continues to refine patient selection criteria and procedural techniques."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992987",
    "fields": {
      "question_number": "191",
      "question_text": "42 y/o female founded unconscious? CT attached:",
      "options": {
        "A": "Amyloid angiopathy.",
        "B": "Aneurysmal hemorrhage.",
        "C": "Hypertensive hemorrhage.",
        "D": "Traumatic hemorrhage."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "This case involves the evaluation of an intracranial hemorrhage in a middle\u2010aged woman. When a patient is found unconscious and a CT scan reveals blood, distinguishing between different hemorrhage etiologies (such as aneurysmal rupture, hypertensive bleed, amyloid angiopathy, or traumatic injury) is essential. Aneurysmal hemorrhage is the classic cause of spontaneous subarachnoid hemorrhage, particularly seen in middle\u2010aged adults.",
        "pathophysiology": "Aneurysmal hemorrhage typically occurs when a saccular (\u2018berry\u2019) aneurysm, often located in the circle of Willis, ruptures. The rupture leads to bleeding into the subarachnoid space, causing a sudden increase in intracranial pressure. This can result in loss of consciousness, severe headache (often described as a 'thunderclap headache'), and, if extensive, may also lead to intraparenchymal extension.",
        "clinical_correlation": "Patients with aneurysmal subarachnoid hemorrhage often present with sudden onset of a severe headache, altered mental status or loss of consciousness, and sometimes focal neurological deficits. In this 42-year-old patient, the presentation of being found unconscious along with CT findings consistent with blood in the subarachnoid space (as suggested by the question context) points toward an aneurysmal origin.",
        "diagnostic_approach": "The initial investigation for suspected intracranial hemorrhage is a non-contrast CT scan, which can reliably detect acute blood. If a subarachnoid hemorrhage is identified, the next steps include CT angiography (CTA) or digital subtraction angiography (DSA) to locate and characterize the aneurysm. Differential diagnoses include hypertensive hemorrhage (typically causing deep or basal ganglia bleeds), amyloid angiopathy (more common in elderly patients with lobar bleeds), and trauma (which would often show extra-axial bleeds such as epidural or subdural hematomas).",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on etiology, location, and clinical context. The major nosological categories include: - **Primary ICH**: spontaneous hemorrhage without underlying vascular malformation or trauma, subdivided into hypertensive hemorrhage and cerebral amyloid angiopathy-related hemorrhage. - **Secondary ICH**: hemorrhage due to identifiable causes such as aneurysmal rupture, vascular malformations, neoplasms, coagulopathies, or trauma. The World Health Organization and American Heart Association/American Stroke Association (AHA/ASA) guidelines classify stroke subtypes, including hemorrhagic stroke, by etiology to guide management. The classification system emphasizes anatomical location (lobar vs. deep), patient age, and risk factors (hypertension, amyloid angiopathy, trauma). There remains some debate about overlap syndromes and the role of genetic factors in hemorrhage risk, but consensus favors a structured approach integrating clinical and imaging data.",
        "classification_and_nosology": "Intracranial hemorrhages are classified based on their location and etiology. Aneurysmal hemorrhage most commonly causes subarachnoid hemorrhage, although secondary intraparenchymal bleeding can occur. In contrast, hypertensive hemorrhage is generally intraparenchymal and involves deep structures like the basal ganglia, thalamus, pons, and cerebellum. Amyloid angiopathy causes lobar hemorrhages typically in older patients, while traumatic hemorrhages have distinct clinical and radiological features related to injury.",
        "management_principles": "Once an aneurysmal subarachnoid hemorrhage is diagnosed, urgent management is critical. The main goals include securing the aneurysm through neurosurgical clipping or endovascular coiling to prevent rebleeding, and the prevention of vasospasm, commonly managed with nimodipine. In acute settings, supportive care to manage intracranial pressure, blood pressure, and electrolyte imbalances is essential. In pregnant or lactating patients, additional care must be taken: imaging studies should minimize fetal radiation exposure (using MRI or shielding techniques when possible), and treatment modalities should be selected to limit risks to the fetus, with multidisciplinary consultation (neurology, neurosurgery, obstetrics) being imperative.",
        "option_analysis": "Option A (Amyloid angiopathy) is more typical in elderly patients and causes lobar hemorrhages. Option C (Hypertensive hemorrhage) usually presents with bleeding in deep brain structures in individuals with longstanding hypertension \u2013 less likely in a 42-year-old female without that history. Option D (Traumatic hemorrhage) would usually be associated with a history of head injury and produce extra-axial hemorrhage patterns (epidural or subdural). Option B (Aneurysmal hemorrhage) aligns best with the patient demographics, clinical presentation, and presumed CT findings showing subarachnoid blood.",
        "clinical_pearls": "Immediate recognition of a subarachnoid hemorrhage is vital, as time-sensitive interventions (securing the aneurysm and preventing vasospasm) are necessary to reduce morbidity and mortality. In any patient presenting with a sudden severe headache or with loss of consciousness and corresponding CT findings, an aneurysmal rupture should be high on the differential. Special considerations must be taken in pregnant or lactating women to balance diagnostic and therapeutic risks.",
        "current_evidence": "Current guidelines, such as those from the American Heart Association/American Stroke Association, emphasize early aneurysm repair (via endovascular or surgical methods) to prevent rebleeding and the use of nimodipine to reduce the incidence of vasospasm. There is ongoing research into optimal management strategies, but early diagnosis and intervention remain the cornerstone of improving outcomes. In pregnant patients, recent recommendations stress minimizing fetal exposure to ionizing radiation and tailoring neurosurgical interventions to ensure maternal and fetal safety."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992988",
    "fields": {
      "question_number": "192",
      "question_text": "Wernicke Aphasia where is the lesion:",
      "options": {
        "A": "Posteroinferior perisylvian.",
        "B": "Posterior perisylvian.",
        "C": "Frontoparietal Operculum"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Wernicke's aphasia is characterized by fluent, yet often nonsensical or jargon-filled speech with impaired comprehension. The core concept involves a lesion in the posterior language area, typically in the dominant (usually left) hemisphere within the perisylvian region.",
        "pathophysiology": "The syndrome is most commonly due to an infarct or lesion affecting the posterior superior temporal gyrus and adjacent areas. This region, in the posterior perisylvian cortex, is responsible for processing and understanding spoken language. Disruption here leads to fluent speech that lacks meaningful content and poor auditory comprehension.",
        "clinical_correlation": "Patients with Wernicke's aphasia produce well-articulated but meaningless speech, have impaired comprehension, and often show difficulty in naming objects or understanding complex language. Recognition of these features, along with neuroimaging that shows damage in the left temporoparietal region, aids in diagnosis.",
        "diagnostic_approach": "Diagnosis is clinical \u2013 through detailed language and neuropsychological assessments \u2013 and is supported by imaging modalities like MRI or CT to localize the lesion. Differential diagnoses include Broca\u2019s aphasia (characterized by nonfluent speech with relatively preserved comprehension) and conduction aphasia (where repetition is particularly impaired).",
        "classification_and_neurology": "Wernicke aphasia belongs to the classical classification of aphasias based on lesion localization within the perisylvian language network. The traditional taxonomy includes Broca's aphasia (anterior perisylvian lesion), Wernicke's aphasia (posterior perisylvian lesion), conduction aphasia (arcuate fasciculus lesion), global aphasia (extensive perisylvian damage), and transcortical aphasias (lesions sparing core language areas but affecting connections). This classification is rooted in the work of Carl Wernicke and later refined by Lichtheim and Geschwind. Modern neuroimaging has nuanced this framework by showing overlapping and distributed networks, but the classical localization remains clinically relevant. The posterior perisylvian cortex specifically refers to the posterior superior temporal gyrus and adjacent regions, differentiating it from the posteroinferior perisylvian cortex (which can involve parts of the inferior parietal lobule) and the frontoparietal operculum (associated with Broca's area). Thus, Wernicke aphasia is taxonomically defined by lesion location in the posterior perisylvian area, consistent with its clinical syndrome.",
        "classification_and_nosology": "Wernicke\u2019s aphasia falls under the umbrella of fluent aphasias. It is typically classified based on the location of the lesion within the language network and is contrasted with nonfluent types such as Broca\u2019s aphasia.",
        "management_principles": "Management involves treating the underlying cause (for example, stroke, tumor, or trauma) and instituting early rehabilitation with speech therapy to maximize recovery. For pregnant or lactating patients, neuroimaging (preferably MRI without contrast when possible) and speech therapy remain the cornerstone, with considerations to minimize any fetal exposure to potentially harmful agents.",
        "option_analysis": "Option A (Posteroinferior perisylvian) misleads by suggesting a designation that is not typically used to define Wernicke\u2019s area. Option B (Posterior perisylvian) correctly captures the location of the lesion, while Option C (Frontoparietal Operculum) more closely corresponds to Broca\u2019s area, which is involved in language production rather than comprehension.",
        "clinical_pearls": "\u2022 Wernicke\u2019s aphasia is recognized by fluent but meaningless speech and poor language comprehension.  \u2022 The lesion is classically in the posterior superior temporal gyrus near the Sylvian fissure in the left hemisphere.",
        "current_evidence": "Recent neuroimaging studies have helped refine our understanding of language networks. Current stroke and aphasia rehabilitation guidelines emphasize early, targeted speech therapy to harness neuroplasticity, even in pregnant or lactating patients where benefits outweigh minimal risks from imaging protocols."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992989",
    "fields": {
      "question_number": "193",
      "question_text": "Patient with stroke for physiotherapy and speech therapy what is the type of prevention:",
      "options": {
        "A": "Primary",
        "B": "Secondary",
        "C": "Tertiary"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Prevention strategies in medicine are classified as primary, secondary, or tertiary. Tertiary prevention involves measures to reduce the impact of an ongoing illness or injury that has lasting effects\u2014in this case, rehabilitation after a stroke.",
        "pathophysiology": "Following an ischemic stroke, brain tissue injury leads to deficits in motor, language, and cognitive functions. Rehabilitation through physiotherapy and speech therapy aims to maximize neuroplasticity and functional recovery, thus reducing disability.",
        "clinical_correlation": "Patients recovering from stroke often face challenges such as motor weakness, language dysfunction, and impaired activities of daily living. Therapies like physiotherapy and speech therapy help improve these deficits and lessen long\u2010term disability, representing tertiary prevention.",
        "diagnostic_approach": "The evaluation involves clinical scales (e.g., the NIH Stroke Scale) and functional assessments that guide early rehabilitation strategies. Differential considerations include secondary prevention measures such as antiplatelet therapy and risk factor modification, which are distinct from rehabilitative interventions.",
        "classification_and_neurology": "The classification of stroke prevention is well established:  - **Primary prevention:** Interventions before any cerebrovascular event, targeting modifiable risk factors such as hypertension, diabetes, smoking, and atrial fibrillation. - **Secondary prevention:** Measures after a first stroke or TIA to prevent recurrence, including antiplatelet or anticoagulant therapy, lipid lowering, and lifestyle modifications. - **Tertiary prevention:** Rehabilitation and supportive care post-stroke to reduce disability and improve quality of life.  This tripartite classification is endorsed by major guidelines such as those from the American Heart Association/American Stroke Association (AHA/ASA). No competing classification systems exist that redefine these prevention stages, making this a cornerstone concept in cerebrovascular disease management.",
        "classification_and_nosology": "Within public health, primary prevention aims to prevent the disease, secondary prevention seeks early detection and management, and tertiary prevention focuses on reducing complications and improving quality of life after the onset of disease.",
        "management_principles": "Current guidelines (like those by the AHA/ASA) strongly recommend timely initiation of rehabilitation therapies post-stroke to improve outcomes. For pregnant or lactating patients, physiotherapy and speech therapy are safe interventions and are adapted as needed based on the patient\u2019s overall clinical status.",
        "option_analysis": "Option A (Primary prevention) is incorrect because these measures are meant to prevent the onset of disease, not manage its sequelae; Option B (Secondary prevention) targets early disease detection and immediate management; Option C (Tertiary prevention) is correct as it pertains to rehabilitation after the disease has occurred.",
        "clinical_pearls": "\u2022 Rehabilitation (through physiotherapy and speech therapy) is a classic example of tertiary prevention.  \u2022 Early, multidisciplinary intervention improves functional outcomes in stroke patients.",
        "current_evidence": "Recent guidelines underscore early, intensive rehabilitation to enhance long-term functional recovery. Studies continue to show that tailored post-stroke therapy regimens, even in special populations such as pregnant and lactating patients, lead to improved disability outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992990",
    "fields": {
      "question_number": "232",
      "question_text": "Patient has right pontine stroke, his NIHSS was 8 and he was on aspirin prior to stroke onset, what is the best option to prevent recurrence of stroke?",
      "options": {
        "A": "Add clopidogrel to aspirin",
        "B": "Keep on aspirin",
        "C": "Change aspirin to clopidogrel",
        "D": "Start anticoagulation"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Secondary prevention of stroke focuses on preventing recurrence after an initial event. When a patient experiences a stroke while already on aspirin, it raises the possibility of aspirin resistance or treatment failure, necessitating a re-evaluation of the antiplatelet regimen.",
        "pathophysiology": "Aspirin works by irreversibly inhibiting cyclooxygenase-1 (COX-1) and reducing thromboxane A2 production, which decreases platelet aggregation. However, in some individuals, this mechanism may not provide adequate protection (so\u2010called aspirin failure), and alternate pathways of platelet aggregation may persist. Clopidogrel, which inhibits the P2Y12 receptor on platelets, offers a different mechanism of action and can be effective in patients who experience ischemic events despite aspirin therapy.",
        "clinical_correlation": "This patient, who sustained a right pontine stroke with an NIHSS of 8 while on aspirin, demonstrates a scenario where the current antiplatelet regimen may be insufficient. A review of his medication adherence, dosing, and potential resistance is warranted. Switching to clopidogrel as monotherapy is supported by evidence in patients with non-cardioembolic stroke who have had an event on aspirin.",
        "diagnostic_approach": "Before altering therapy, it is important to review patient compliance, assess for other stroke risk factors, and consider imaging and laboratory tests if necessary. Differential considerations include the need for dual antiplatelet therapy or even evaluation for cardioembolic sources if suspected, though the clinical scenario here suggests a non-cardioembolic mechanism.",
        "classification_and_neurology": "Ischemic strokes are classified according to the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. Pontine strokes frequently fall under small vessel occlusion or branch atheromatous disease but may also be due to large artery disease. Secondary prevention strategies are classified based on stroke subtype and risk factors. Antiplatelet therapies are standard for non-cardioembolic ischemic strokes, while anticoagulation is reserved for cardioembolic strokes. The concept of dual antiplatelet therapy has evolved from trials demonstrating benefit in selected patients with minor stroke or high-risk transient ischemic attack (TIA), particularly in the early post-event period.",
        "classification_and_nosology": "This falls under secondary prevention for non-cardioembolic ischemic stroke. Antiplatelet agents are routinely used in this setting. Aspirin failure may prompt a change of agent or addition of a second antiplatelet in selected cases (with careful consideration of bleeding risks).",
        "management_principles": "According to current guidelines, if a patient experiences a stroke while on aspirin, switching to an alternative antiplatelet agent like clopidogrel is a reasonable approach. Dual antiplatelet therapy (aspirin plus clopidogrel) is typically reserved for a short duration in minor strokes (often defined by a lower NIHSS score) due to increased bleeding risk when used long term. In patients with moderate stroke severity (as in this case), monotherapy with clopidogrel is preferred. When considering pregnant or lactating patients, the use of antiplatelet agents is a careful balance; aspirin is generally preferred in pregnancy, but when there is clear aspirin failure, clopidogrel may be used if the benefits clearly outweigh the risks, following a thorough risk\u2013benefit analysis in consultation with obstetrics.",
        "option_analysis": "Option A (Add clopidogrel to aspirin) suggests dual therapy, which is typically indicated only for a short period in minor stroke/TIA and is not generally recommended long term in moderate strokes due to bleeding risk. Option B (Keep on aspirin) does not address the apparent treatment failure. Option C (Change aspirin to clopidogrel) is correct as it addresses the therapeutic failure by switching mechanisms of action. Option D (Start anticoagulation) is inappropriate here because there is no evidence of a cardioembolic source.",
        "clinical_pearls": "\u2022 Stroke recurrence on aspirin may suggest aspirin resistance, warranting a switch to an alternative agent.  \u2022 Long-term dual antiplatelet therapy is generally avoided due to increased bleeding risk unless specifically indicated for a short term.",
        "current_evidence": "Recent studies and guidelines, including updates from the AHA/ASA and findings from trials such as CAPRIE, support the use of clopidogrel in patients who experience an ischemic event on aspirin. This evidence reinforces a switch of antiplatelet strategy rather than the prolonged use of dual therapy, especially in strokes with moderate severity."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992991",
    "fields": {
      "question_number": "233",
      "question_text": "Scenario about AICA syndrome, which artery involved?",
      "options": {
        "A": "AICA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "AICA syndrome, or lateral pontine syndrome caused by occlusion of the anterior inferior cerebellar artery, is defined by deficits that involve both cerebellar and inner ear structures. The concept here is the direct relationship between the vascular territory and the clinical features observed.",
        "pathophysiology": "The anterior inferior cerebellar artery (AICA) supplies blood to portions of the lateral pons, the cerebellum, and the inner ear. Occlusion of AICA leads to ischemia in these areas, resulting in signs such as facial weakness, hearing loss, vertigo, and ataxia.",
        "clinical_correlation": "Clinically, AICA infarction may present with a constellation of symptoms including peripheral facial paralysis, vestibulocochlear deficits (such as hearing loss and vertigo), and ataxia. These findings help differentiate it from other brainstem syndromes, such as those involving the posterior inferior cerebellar artery.",
        "diagnostic_approach": "Diagnosis is usually made on clinical grounds supported by magnetic resonance imaging (MRI) that confirms infarction in the AICA territory. The differential includes lateral medullary (Wallenberg) syndrome from PICA occlusion and other brainstem infarcts, each with its own distinct set of neurological deficits.",
        "classification_and_neurology": "AICA syndrome is classified under brainstem ischemic strokes, specifically within the category of posterior circulation strokes. The posterior circulation includes the vertebral arteries, basilar artery, and their branches (AICA, PICA, SCA).   Nosologically, it is part of the lateral pontine syndromes, which are subtypes of brainstem strokes distinguished by vascular territory and clinical features. The widely accepted classification systems for stroke, such as the TOAST (Trial of Org 10172 in Acute Stroke Treatment) criteria, categorize strokes by etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.), but localization remains critical for clinical diagnosis and management.  While some controversy exists regarding the overlap between lateral pontine syndromes caused by AICA versus SCA infarctions, current consensus emphasizes vascular territory-based classification supported by imaging. This approach aligns with neuroanatomical and clinical correlation principles.",
        "classification_and_nosology": "AICA syndrome is categorized as a brainstem stroke, specifically a type of lateral pontine syndrome. In vascular nosology, strokes are grouped based on their arterial territories, which aids in guiding both diagnosis and management.",
        "management_principles": "Acute management includes standard stroke care protocols, often involving antiplatelet therapy and risk factor modification. Rehabilitation for balance and facial function might be necessary. In pregnant or lactating patients, management follows the same principles with careful assessment of risks versus benefits for any pharmacological intervention and ensuring safety with neuroimaging.",
        "option_analysis": "Option A (AICA) is the only provided option and correctly identifies the artery involved in this syndrome. The absence of other options reinforces that the question is testing recognition of the vascular supply related to the clinical syndrome.",
        "clinical_pearls": "\u2022 AICA infarcts typically present with audiovestibular symptoms in addition to signs of lateral pontine involvement.  \u2022 Differentiation from PICA (Wallenberg syndrome) is key, as the latter does not typically produce hearing deficits.",
        "current_evidence": "Recent advances in neuroimaging have improved the localization of brainstem strokes. Current stroke guidelines continue to support tailored antiplatelet and rehabilitative strategies based on specific vascular territories, with appropriate adjustments for vulnerable populations including pregnant and lactating women."
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
