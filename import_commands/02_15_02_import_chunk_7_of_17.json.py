
# Import batch 2 of 3 from chunk_7_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993189",
    "fields": {
      "question_number": "272",
      "question_text": "60 years old male pt DM/ HTN/ came with history of TiA for 10 min numbness and dysarthtia. NiHSs is 3. We have to calculate ABCD2 score. On examination ot still have numbness what you will give",
      "options": {
        "A": "aspirin",
        "B": "plavix",
        "C": "dual"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "The ABCD2 score is a clinical tool for risk-stratifying patients after a transient ischemic attack (TIA) to predict the short-term risk of stroke. It incorporates Age, Blood pressure, Clinical features, Duration of symptoms, and Diabetes.",
        "pathophysiology": "TIAs result from transient cerebral ischemia, often due to embolism or small vessel occlusion in the setting of underlying atherosclerosis. The score reflects the cumulative risk imposed by these factors.",
        "clinical_correlation": "In a 60\u2010year\u2010old male with traditional vascular risk factors and a transient episode of neurological deficits, a high ABCD2 score indicates a substantial risk for future stroke. Persistent neurologic deficits (such as ongoing numbness) further raise concern and influence treatment intensity.",
        "diagnostic_approach": "Differentiation involves excluding mimics like migraine, seizure-related symptoms, or hypoglycemia. Neuroimaging (CT/MRI) is needed to rule out acute infarction and to evaluate for underlying vascular pathology.",
        "classification_and_neurology": "TIA is classified within the cerebrovascular disease spectrum under ischemic cerebrovascular events. The traditional definition required symptom resolution within 24 hours without infarction. The tissue-based definition, endorsed by the American Heart Association/American Stroke Association (AHA/ASA), defines TIA as transient neurological dysfunction without acute infarction on imaging. This shift recognizes that some transient symptoms may have infarcts visible on diffusion-weighted MRI, reclassifying them as minor strokes. The ABCD2 score is part of risk stratification classification systems for TIA, guiding prognosis and management. TIAs fall under the broader category of transient focal neurological episodes and are distinguished from stroke mimics and minor strokes. Nosologically, TIAs are grouped by etiology (large artery atherosclerosis, cardioembolism, small vessel disease, other determined or undetermined causes) using TOAST criteria. Current consensus emphasizes rapid assessment and treatment to prevent progression to ischemic stroke.",
        "classification_and_nosology": "TIA is classified based on duration (typically less than 24 hours) and severity. High-risk TIAs, commonly defined by an ABCD2 score of 4 or greater, warrant aggressive early intervention.",
        "management_principles": "Current guidelines, informed by trials such as CHANCE and POINT, support the initiation of dual antiplatelet therapy (aspirin plus clopidogrel) within 24 hours of a high-risk TIA or minor stroke and continuing it for 21\u201390 days before transitioning to monotherapy. Although this patient is a 60-year-old male, these principles are standard; in pregnant or lactating patients, low-dose aspirin is often acceptable, but clopidogrel has a less established safety profile and is generally used with caution.",
        "option_analysis": "Option A (aspirin alone) and Option B (clopidogrel alone) may be considered in lower-risk settings, but for high-risk TIA, dual therapy (Option C) has been proven superior in reducing early recurrent stroke risk. Option D was not provided.",
        "clinical_pearls": "1. Dual antiplatelet therapy is beneficial when initiated early in high-risk TIA or minor stroke patients to reduce recurrent stroke risk. 2. The ABCD2 score is an essential clinical tool for determining the intensity of secondary prevention strategies.",
        "current_evidence": "Large-scale trials, including CHANCE and POINT, have firmly established the benefit of dual antiplatelet therapy in reducing stroke recurrence in patients with high ABCD2 scores, thereby shaping current guideline recommendations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993190",
    "fields": {
      "question_number": "273",
      "question_text": "What you will do:",
      "options": {
        "A": "(angioplasty alone) is not recommended because it can lead to vessel recoil and restenosis. Option B (stenting) is typically reserved for patients who cannot undergo surgery, while Option C (endarterectomy) is an option for selected high",
        "D": "(medical therapy) is the most appropriate initial approach in a broad range of patients with large vessel stenosis."
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Management of symptomatic large vessel cerebrovascular stenosis requires an evaluation of both the severity of the stenosis and the symptoms. The initial treatment approach generally prioritizes optimized medical management over immediate invasive procedures.",
        "pathophysiology": "Atherosclerotic disease in large vessels, such as the carotid arteries, leads to narrowing and turbulent flow that predisposes to thromboembolic events and hypoperfusion. The chronic inflammatory process leads to plaque formation and progression of stenosis.",
        "clinical_correlation": "Patients with symptomatic stenosis presenting with TIA or minor stroke symptoms are at risk for further ischemic events. While invasive procedures like endarterectomy or stenting can reduce stroke risk in selected patients, many individuals initially benefit from aggressive medical therapy that addresses risk factors and stabilizes plaque.",
        "diagnostic_approach": "Diagnosis is typically confirmed by noninvasive imaging modalities such as carotid duplex ultrasonography, CTA, or MRA. Differential diagnoses include intracranial atherosclerosis, vasculitis, and cardioembolic sources; the degree of stenosis guides the treatment plan.",
        "classification_and_neurology": "Large vessel cerebrovascular disease falls under the broader category of ischemic stroke etiologies, specifically classified within the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system as 'large artery atherosclerosis.' This category includes atherosclerotic stenosis or occlusion of major extracranial or intracranial arteries. The disease family encompasses carotid artery disease, intracranial atherosclerosis, and other large vessel pathologies. Over time, classification systems have evolved to incorporate imaging findings and genetic markers, but TOAST remains widely used in clinical practice and research. Some controversies exist regarding the classification of intracranial versus extracranial disease and the role of embolic versus hemodynamic mechanisms, but large artery atherosclerosis is a well-established nosological entity.",
        "classification_and_nosology": "Carotid artery disease is classified based on the percentage of stenosis (mild, moderate, severe) and whether the patient is symptomatic or asymptomatic. The decision for surgical versus medical management hinges on both these factors.",
        "management_principles": "Current guidelines emphasize that the first-line management for most patients with large vessel stenosis is optimized medical therapy. This includes antiplatelet agents (often aspirin \u00b1 clopidogrel), high-intensity statin therapy, strict blood pressure control, and lifestyle modification. In patients with high-grade (typically >70%) symptomatic stenosis, carotid endarterectomy (CEA) may be indicated if the patient is an appropriate surgical candidate. Carotid stenting is reserved for patients with contraindications to surgery. In pregnant and lactating patients, medications must be selected for safety; for example, low-dose aspirin is generally acceptable in pregnancy, whereas many statins and interventional procedures are contraindicated or require special consideration.",
        "option_analysis": "Option A (angioplasty alone) is not recommended because it can lead to vessel recoil and restenosis. Option B (stenting) is typically reserved for patients who cannot undergo surgery, while Option C (endarterectomy) is an option for selected high-grade stenosis cases but is not universally required. Option D (medical therapy) is the most appropriate initial approach in a broad range of patients with large vessel stenosis.",
        "clinical_pearls": "1. Optimal medical management, including risk factor modification, is the cornerstone of treatment for cerebrovascular stenosis. 2. Invasive interventions should be reserved for carefully selected patients after a thorough evaluation of stenosis severity.",
        "current_evidence": "Recent trials such as SAMMPRIS and CREST have underscored the efficacy of aggressive medical therapy in reducing recurrent stroke risk and have helped refine the indications for interventional procedures in patients with large vessel cerebrovascular disease."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993191",
    "fields": {
      "question_number": "274",
      "question_text": "sickler pt come with stroke work up done and found to have multiple stenosis in AcA and McA. Ehat is the method of prevention?",
      "options": {
        "A": "aspirin",
        "B": "plavix",
        "C": "chronic transfusion",
        "D": "dual antiplate"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In patients with sickle cell disease (SCD), the abnormal hemoglobin leads to red blood cell sickling, which can cause vaso-occlusion and vascular injury, notably in cerebral vessels. This predisposes them to stroke and progressive vasculopathy.",
        "pathophysiology": "The sickling of red blood cells in SCD results in chronic hemolysis and microvascular occlusions. Repeated vaso-occlusive events damage the endothelium, leading to intimal hyperplasia and progressive arterial stenosis, particularly affecting major intracranial arteries such as the anterior (AcA) and middle cerebral arteries (McA).",
        "clinical_correlation": "SCD patients are at high risk for both overt and silent strokes, often presenting with transient ischemic attacks or neurological deficits. The identification of multiple intracranial stenoses on stroke workup is a common finding in this population.",
        "diagnostic_approach": "The evaluation involves neuroimaging studies, including MRA or CTA, to assess vessel patency and differentiate SCD vasculopathy from other conditions such as atherosclerotic disease or inflammatory vasculitis. Differential diagnoses include moyamoya syndrome and other forms of vasculitis.",
        "classification_and_neurology": "Stroke in sickle cell disease is classified as a secondary ischemic stroke due to a hematologic disorder causing vasculopathy. According to the TOAST classification, it falls under stroke subtype 5: stroke of other determined etiology. The vascular pathology in SCD represents a unique cerebrovascular disease entity characterized by large-vessel stenosis and small-vessel disease. The classification of SCD-related cerebrovascular disease has evolved to emphasize the role of transcranial Doppler velocities and MRI/MRA findings in stratifying stroke risk. Current nosology integrates clinical, radiographic, and hematologic criteria to guide prevention and treatment. This condition is part of the broader family of hematologic stroke syndromes, distinct from atherosclerotic or cardioembolic strokes.",
        "classification_and_nosology": "SCD-associated vasculopathy is a secondary stroke syndrome. It is typically categorized separately from atherosclerotic cerebrovascular disease because its pathogenesis stems from red cell sickling rather than lipid-driven inflammation.",
        "management_principles": "Chronic blood transfusion therapy is the cornerstone of both primary and secondary stroke prevention in SCD. Regular transfusions work by reducing the proportion of hemoglobin S below 30%, thereby minimizing sickling events and reducing stroke risk. Hydroxyurea may be considered as an adjunct therapy in some cases. In pregnant or lactating patients with SCD, transfusion protocols must be carefully managed by a multidisciplinary team, balancing maternal and fetal risks while ensuring optimal reduction in stroke risk.",
        "option_analysis": "Option A (aspirin) and Option B (clopidogrel) are antiplatelet regimens typically used in atherosclerotic stroke prevention and do not address the underlying pathophysiology of SCD. Option D (dual antiplatelet therapy) similarly fails to alter the sickling process. Option C (chronic transfusion) is the established and effective method for stroke prevention in SCD by reducing the hemoglobin S load.",
        "clinical_pearls": "1. Chronic transfusion therapy remains the standard of care for stroke prevention in SCD, targeting a reduction in hemoglobin S levels. 2. SCD vasculopathy involves unique mechanisms distinct from atherosclerotic disease, thus requiring different treatment strategies.",
        "current_evidence": "Recent studies continue to support the efficacy of chronic transfusion protocols in reducing stroke incidence in SCD patients. Ongoing research into adjunctive therapies, including hydroxyurea and gene therapy, aims to further improve outcomes in this high-risk population."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993193",
    "fields": {
      "question_number": "276",
      "question_text": "82 years old male pt came within 3 hrs and have no contraindication for tpa and ct attached with early signe of stroke but infarction not established what you will give",
      "options": {
        "A": "aspirin",
        "B": "plavix",
        "C": "tpa"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses the acute management of ischemic stroke in the hyperacute phase. The mainstay treatment for eligible patients is thrombolysis with tissue plasminogen activator (tPA).",
        "pathophysiology": "In ischemic stroke, clot formation leads to occlusion of cerebral blood vessels, resulting in neuronal ischemia and infarction. Early restoration of blood flow with tPA can dissolve the thrombus, limiting tissue damage and improving outcomes.",
        "clinical_correlation": "The patient, an 82\u2010year\u2010old male, presented within 3 hours of symptom onset with early signs on CT but without established infarction. The absence of contraindications combined with the timely presentation makes him a good candidate for tPA despite advanced age.",
        "diagnostic_approach": "Initial evaluation includes a noncontrast head CT to rule out hemorrhage, assessment of stroke symptoms, and careful review of contraindications. Differential diagnoses include stroke mimics such as seizures or hypoglycemia. However, early ischemic changes assessed on CT support the diagnosis of acute ischemic stroke.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases within the International Classification of Diseases (ICD-10: I63). It is further categorized by etiology using the TOAST classification:  - Large artery atherosclerosis - Cardioembolism - Small vessel occlusion (lacunar) - Stroke of other determined etiology - Stroke of undetermined etiology  This classification aids in understanding stroke mechanisms and tailoring secondary prevention. The management of acute ischemic stroke falls under emergency neurology and stroke medicine, with treatment protocols standardized by guidelines such as those from the American Heart Association/American Stroke Association (AHA/ASA). The evolution of classification systems has improved diagnostic precision and therapeutic strategies.",
        "classification_and_nosology": "Ischemic strokes are classified by etiology into categories such as cardioembolic, large artery atherosclerosis, small vessel occlusion, and others. The patient\u2019s presentation fits into the general management approach for acute ischemic stroke.",
        "management_principles": "The current guidelines recommend intravenous tPA as a first-line treatment for eligible patients presenting within 3 hours (and in select cases up to 4.5 hours) of stroke onset. In elderly patients, tPA is not contraindicated; careful evaluation of bleeding risk is crucial. In pregnancy and lactation, tPA can be used if benefits outweigh risks, though data in these populations are limited and management should be individualized.",
        "option_analysis": "Option A (Aspirin) and Option B (Plavix) are antiplatelet agents generally used for secondary prevention, not for acute reperfusion. Option C (tPA) is the correct choice as it is the established treatment in the hyperacute period when no contraindications exist. Option D is not provided.",
        "clinical_pearls": "1. Time is brain: early administration of tPA is critical. 2. Advanced age alone is not a contraindication for tPA. 3. CT imaging is essential to rule out hemorrhage before initiating therapy.",
        "current_evidence": "Recent AHA/ASA updates affirm the benefit of tPA in eligible patients within the 3-hour window, with growing evidence supporting its use in patients over 80 years old, provided contraindications are absent. Ongoing research continues to refine selection criteria, including the use of advanced imaging techniques."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993194",
    "fields": {
      "question_number": "277",
      "question_text": "pt suddenly explaned to his wife seeing animals and fade after while pt loss consciousness / EMd arrived. Take him to the hospital intubation done. Attache Ct scan. New left occipital stroke. What you will do? Pt presneted with window not mention bt writeen sudden and within 1 hr",
      "options": {
        "A": "cta",
        "B": "EEG",
        "C": "tpa"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question involves the acute management of an ischemic stroke presenting with occipital lobe involvement, where symptoms may include visual disturbances such as seeing animals (visual hallucinations).",
        "pathophysiology": "An infarct in the occipital lobe affects the visual processing center of the brain, leading to phenomena such as visual hallucinations or altered vision. This ischemic process results from an arterial occlusion that, if treated promptly, can be salvaged using reperfusion therapy.",
        "clinical_correlation": "The case describes a patient with a new left occipital stroke who presented acutely (within 1 hour), making him an ideal candidate for thrombolytic therapy. Despite being intubated, if there are no contraindications and the patient is within the therapeutic window, tPA can significantly improve outcomes.",
        "diagnostic_approach": "A noncontrast CT scan is performed first to exclude hemorrhage, supported by clinical history. Although additional studies like CT angiogram (CTA) can help visualize vessel occlusion, the immediate determination of eligibility for tPA is paramount. Differential diagnosis would include seizure activity or other visual disturbances, but imaging confirming a new infarct solidifies the diagnosis.",
        "classification_and_neurology": "Ischemic strokes are classified by etiology using systems like the TOAST criteria, which include large-artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. This patient\u2019s stroke likely falls under large-artery or cardioembolic ischemic stroke depending on further workup. The classification aids in secondary prevention but does not delay acute management. The acute ischemic stroke diagnosis is based on clinical presentation and imaging, distinguishing it from hemorrhagic stroke and stroke mimics. The classification of stroke management follows guidelines that stratify patients based on time from symptom onset and imaging findings.",
        "classification_and_nosology": "This is classified as an acute ischemic stroke of the posterior circulation (occipital lobe involvement). Stroke subtypes are often categorized based on the vascular territory involved.",
        "management_principles": "For eligible patients presenting within the approved time window (up to 4.5 hours, with the greatest benefit seen earlier), IV tPA is recommended as first-line therapy. The decision remains similar even in patients who have been intubated, provided airway management and supportive care are ensured. In pregnancy and lactation, treatment with tPA is considered on a case-by-case basis, weighing risks and benefits, though available data remain limited.",
        "option_analysis": "Option A (CTA) is an imaging modality that can further evaluate vessel occlusion but is not a treatment. Option B (EEG) is unrelated and used to assess for seizures. Option C (tPA) is the appropriate therapeutic intervention to achieve reperfusion in an acute ischemic stroke. Option D is not provided.",
        "clinical_pearls": "1. Occipital strokes may present with visual hallucinations or disturbances. 2. Rapid identification and treatment with tPA are critical within the treatment window. 3. Intubation should not automatically preclude the use of tPA if other criteria are met.",
        "current_evidence": "Current guidelines from the AHA/ASA strongly support the use of tPA in patients with acute ischemic stroke presenting within the therapeutic window. Research continues into optimizing patient selection using advanced imaging techniques to extend reperfusion therapy to more patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993195",
    "fields": {
      "question_number": "278",
      "question_text": "What yoi will do?",
      "options": {
        "A": "Shunt",
        "B": "anticoagulant",
        "C": "give",
        "D": "give LMWH"
      },
      "correct_answer": "Insufficient information to determine the correct management option",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question appears to ask for the next step in management, but the lack of clinical context (such as the underlying diagnosis or situation) makes it ambiguous. The provided options range from a surgical intervention (shunt), general anticoagulation, an unspecified 'give', or the use of low molecular weight heparin (LMWH).",
        "pathophysiology": "Without a clear clinical scenario, it is not possible to ascertain the underlying pathophysiological process. For instance, a shunt would be used for managing hydrocephalus, whereas LMWH is typically used for thromboembolic prophylaxis or treatment, and the generic term 'anticoagulant' could apply to multiple vascular conditions.",
        "clinical_correlation": "The options suggest two distinct clinical pathways: one related to neurosurgical management (shunt placement for hydrocephalus) and the other related to medical management (anticoagulation or LMWH for thromboembolism or stroke prophylaxis). Without additional patient history, imaging details, or a specific diagnosis, correlating these options to a clinical presentation is not feasible.",
        "diagnostic_approach": "A proper diagnostic workup would require detailed history, physical examination, and appropriate imaging studies to differentiate between conditions such as normal-pressure hydrocephalus, cerebral venous thrombosis, or post-stroke deep venous thrombosis prophylaxis. Differential diagnoses might include hydrocephalus, acute ischemic stroke with subsequent thrombosis risk, or another cerebrovascular abnormality.",
        "classification_and_neurology": "Cerebrovascular diseases are classified broadly into ischemic strokes, hemorrhagic strokes, and venous strokes (CVT). The International Classification of Diseases (ICD-11) and the TOAST criteria focus on arterial ischemic stroke subtypes. CVT is classified under venous strokes, a distinct nosological entity due to its unique pathophysiology and treatment. This classification influences management algorithms. Over time, recognition of CVT as a separate category has improved diagnosis and targeted therapy. Controversies exist regarding anticoagulation in hemorrhagic CVT, but consensus supports its use. The differentiation between arterial and venous strokes is critical for appropriate therapy.",
        "classification_and_nosology": "The term 'shunt' typically applies to conditions involving abnormal cerebrospinal fluid (CSF) dynamics (e.g., hydrocephalus), whereas 'anticoagulant' or 'LMWH' would be classified under the treatment of thromboembolic disorders. The lack of a specific diagnostic label prevents proper categorization.",
        "management_principles": "Management should be tailored based on the definitive diagnosis. If the issue were hydrocephalus, a shunt procedure (typically a ventriculoperitoneal shunt) would be indicated. Conversely, if the patient has a thromboembolic disorder (such as cerebral venous thrombosis or requires DVT prophylaxis post-stroke), the use of anticoagulants like LMWH is appropriate. In pregnancy and lactation, LMWH is preferred over other anticoagulants because it does not cross the placenta and has a favorable safety profile during breastfeeding.",
        "option_analysis": "Option A (Shunt) is correct if the underlying problem is hydrocephalus but irrelevant if the condition is thromboembolic in nature. Option B (anticoagulant) is a broad term and might be applicable in multiple scenarios but is non-specific. Option C (give) is incomplete and provides no actionable information. Option D (give LMWH) is appropriate for thromboembolic conditions (e.g., for prophylaxis in immobilized patients or in the treatment of cerebral venous thrombosis) as well as for VTE prevention in high-risk patients, including those who are pregnant or lactating. However, without further context, it is impossible to choose definitively among these.",
        "clinical_pearls": "1. Always ensure that a question provides adequate clinical context before selecting a management option. 2. In cases of cerebrospinal fluid buildup (hydrocephalus), a shunt is indicated, while in thromboembolic conditions, anticoagulation (preferably LMWH in pregnancy/lactation) is preferred.",
        "current_evidence": "Recent guidelines underscore the importance of tailoring stroke and hydrocephalus management to the individual patient based on imaging and clinical presentation. In conditions requiring anticoagulation, LMWH remains the agent of choice in pregnant and lactating women due to its safety profile. However, current evidence also highlights the necessity of a precise diagnosis before initiating treatment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993196",
    "fields": {
      "question_number": "279",
      "question_text": "Long senario pt came with anyrism rupture of PcOm what you will do?",
      "options": {
        "A": "Cliping",
        "B": "Coiling",
        "C": "Decompressivw craniotomy",
        "D": "Amdission to stroke unit"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Ruptured cerebral aneurysms, particularly those in the region of the posterior communicating artery (PCOM), lead to subarachnoid hemorrhage. The core concept is that rapid hemorrhage into the subarachnoid space may cause sudden, severe headache (often described as thunderclap headache) and neurological deficits, necessitating prompt intervention to secure the aneurysm and prevent re-bleeding.",
        "pathophysiology": "Aneurysms form due to the weakening of the arterial wall and, when ruptured, cause bleeding into the subarachnoid space. This generates a rise in intracranial pressure, risk of cerebral vasospasm, and ischemic injury to surrounding brain tissue. PCOM aneurysms are common and sometimes manifest with third nerve palsy due to proximity to the oculomotor nerve.",
        "clinical_correlation": "Patients commonly present with a sudden, severe headache, nausea, vomiting, and sometimes loss of consciousness. Specific to PCOM aneurysms, unilateral oculomotor nerve palsy with ptosis and a dilated pupil may be observed due to the compressive effects of an enlarging aneurysm or hemorrhage.",
        "diagnostic_approach": "The initial diagnosis is typically made using a noncontrast CT scan to detect subarachnoid blood. This is followed by CT-angiography or digital subtraction angiography (DSA) to localize the aneurysm. Differential diagnoses include perimesencephalic subarachnoid hemorrhage and hypertensive hemorrhage, which can be differentiated by the bleeding pattern and location.",
        "classification_and_neurology": "Intracranial aneurysms are classified primarily by morphology (saccular, fusiform, dissecting), location (anterior vs. posterior circulation), and rupture status (ruptured vs. unruptured). PCOM aneurysms are saccular (berry) aneurysms located at the junction of the internal carotid artery and PCOM artery, part of the anterior circulation. The World Federation of Neurosurgical Societies (WFNS) grading and Hunt and Hess scale classify SAH severity based on clinical presentation, guiding prognosis and treatment urgency. The Fisher scale classifies SAH based on CT blood amount, predicting vasospasm risk. These classification systems help stratify patients and guide management. Current consensus favors early intervention for ruptured aneurysms regardless of grade to prevent rebleeding.",
        "classification_and_nosology": "Intracranial aneurysms are classified by location (anterior vs. posterior circulation), morphology (saccular, fusiform), and risk of rupture. PCOM aneurysms belong to the anterior circulation group despite being adjacent to the posterior communicating artery.",
        "management_principles": "Early securing of the aneurysm is the priority. Current guidelines suggest that endovascular coiling is preferred in many cases due to less invasiveness and favorable outcomes (as shown by the ISAT trial) if the aneurysm\u2019s anatomy is amenable. Surgical clipping remains an alternative if endovascular coiling is not feasible. Post-procedure, patients require management of vasospasm (typically with nimodipine), control of intracranial pressure, and supportive care. In pregnant patients, special considerations include minimizing radiation exposure (with appropriate shielding) and careful monitoring of fetal status during any interventional procedure, whereas during lactation, most contrast agents and anesthesia drugs are considered relatively safe with proper guidance.",
        "option_analysis": "Option A (Clipping) is an acceptable treatment alternative but is generally reserved for aneurysms with unfavorable coiling anatomy. Option B (Coiling), the marked answer, is preferred in many centers for PCOM aneurysms due to lower procedural morbidity. Option C (Decompressive craniotomy) is not a direct treatment for an aneurysm rupture but may be used later in cases with malignant edema. Option D (Admission to stroke unit) is inadequate as definitive management and does not secure the aneurysm.",
        "clinical_pearls": "1. PCOM aneurysms can present with cranial nerve III palsy. 2. Early intervention is crucial to prevent re-bleeding and vasospasm. 3. Endovascular coiling offers a less invasive option with favorable outcomes in selected patients.",
        "current_evidence": "Recent guidelines and trials (such as ISAT) support the use of endovascular coiling in appropriate aneurysms due to reduced morbidity and similar long-term outcomes to clipping. Ongoing research is focused on further refining patient selection and improving endovascular techniques."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993197",
    "fields": {
      "question_number": "280",
      "question_text": "Male 56 years old male pt found in teh house with decreas level of consuos Last tome seen normal 1 day back Brain ct scan showed:",
      "options": {
        "A": "tpa",
        "B": "admission to stroke unite"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "The management of stroke patients depends critically on the timing from symptom onset. In this scenario, a 56\u2010year\u2010old man was found with decreased consciousness and a known last normal time of 24 hours ago, which is well beyond the therapeutic window for thrombolytic therapy.",
        "pathophysiology": "Ischemic strokes are caused by occlusion of cerebral arteries leading to ischemia and infarction of brain tissue. The prolonged occlusion results in neuronal death and can cause significant deficits. The diminished level of consciousness could be from a large stroke or associated edema.",
        "clinical_correlation": "Patients with ischemic stroke may present with various focal neurological deficits. A decreased level of consciousness in an elderly patient along with imaging findings on CT (even if not detailed here) necessitates prompt evaluation, though reperfusion therapies are time-sensitive.",
        "diagnostic_approach": "A noncontrast CT scan is generally performed to rule out hemorrhage. In patients presenting beyond the thrombolytic window, advanced imaging modalities like CT perfusion or MRI may be used in select cases to assess salvageable brain tissue. Differentials include hemorrhagic stroke, hypoglycemia, and seizure post-ictal states.",
        "classification_and_neurology": "Ischemic stroke is classified within the broader cerebrovascular disease category. The TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This classification guides diagnostic evaluation and secondary prevention strategies. The diagnosis of acute ischemic stroke is clinical, supported by neuroimaging to differentiate from hemorrhagic stroke and stroke mimics. The concept of stroke mimics (e.g., seizures, hypoglycemia) is important in acute management decisions. Over time, classification systems have evolved to incorporate advanced imaging and biomarkers, but the TOAST system remains widely used in clinical practice and research.",
        "classification_and_nosology": "Stroke is broadly classified into ischemic and hemorrhagic. Within ischemic strokes, further categorization is by etiology (thrombotic, embolic, lacunar, etc.).",
        "management_principles": "Given that the patient is outside the therapeutic window for tPA (typically within 3-4.5 hours from onset), the current evidence supports admission to a dedicated stroke unit where specialized care, supportive management, and secondary prevention strategies are initiated. For pregnant patients with stroke, management must balance maternal benefits against fetal safety, with careful use of imaging and medications. For lactating mothers, medication choices are adjusted based on excretion in breast milk.",
        "option_analysis": "Option A (tPA) is contraindicated due to the elapsed time since last known well. Option B (Admission to stroke unit) is appropriate and correct as specialized stroke care can improve outcomes. Options C and D are not provided or applicable in this context.",
        "clinical_pearls": "1. 'Time is brain' \u2013 rapid recognition and treatment are essential in stroke. 2. Patients discovered beyond the tPA window should be managed in a stroke unit to optimize supportive care and secondary prevention. 3. Advanced imaging may extend treatment windows in select patients but 24 hours is generally too long for standard tPA protocols.",
        "current_evidence": "Recent studies confirm that dedicated stroke unit care consistently improves survival and functional outcomes. Although advanced imaging techniques have allowed for extended therapy windows in some cases (e.g., DAWN and DEFUSE 3 trials), these are typically limited to carefully selected patients within 24 hours and not applicable in a general scenario as described here."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_9.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993198",
    "fields": {
      "question_number": "281",
      "question_text": "What is the artey?",
      "options": {
        "A": "mca",
        "B": "pca",
        "C": "ant choroidal artery"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question focuses on identifying the cerebral artery involved based on a presumed clinical or radiological scenario. The Middle Cerebral Artery (MCA) is the most commonly affected artery in ischemic strokes due to its direct flow from the internal carotid artery and its large territory of perfusion.",
        "pathophysiology": "Occlusion of the MCA typically leads to infarction in the regions of the brain it supplies. This results from thromboembolism or atherosclerotic narrowing. The large territory of the MCA means that occlusions often produce significant neurological deficits.",
        "clinical_correlation": "Clinically, an MCA stroke often manifests with contralateral weakness (especially affecting the face and arm), sensory deficits, and if the dominant hemisphere is involved, aphasia. Visual field deficits may also occur if the inferior division is involved.",
        "diagnostic_approach": "Initial imaging with a noncontrast CT scan is used to exclude hemorrhage. MRI with diffusion-weighted imaging and CT angiography are instrumental in confirming an MCA occlusion and assessing the extent of core infarction versus salvageable penumbra. Differentials would include PCA infarction (which typically affects the occipital lobe and causes visual deficits) and anterior choroidal artery infarction (which often produces lacunar syndromes).",
        "classification_and_neurology": "The **anterior choroidal artery syndrome** is classified among lacunar or small vessel infarcts due to the artery\u2019s small caliber and deep perforating branches. However, it can also result from large artery atherosclerosis or embolism involving the internal carotid artery.  In the TOAST classification of ischemic stroke etiology, AChA strokes may fall into the categories of large artery atherosclerosis or cardioembolism depending on the underlying cause.  From a vascular anatomy standpoint, the AChA is considered a branch of the internal carotid artery, distinct from the MCA and PCA, which arise from the internal carotid and basilar arteries respectively. This anatomical classification is critical for understanding stroke syndromes and potential collateral pathways.  Controversies exist regarding the variability of the AChA territory and its collateral supply, which may influence clinical presentations.",
        "classification_and_nosology": "In ischemic stroke nosology, infarctions are often categorized by the arterial territory involved. MCA strokes constitute the bulk of large vessel occlusions and are a subset of ischemic strokes.",
        "management_principles": "If within the window, management of an MCA occlusion may include intravenous thrombolysis and/or mechanical thrombectomy for large vessel occlusions. Guidelines emphasize rapid reperfusion therapy and supportive care. For pregnant patients, thrombolysis may be considered on a case-by-case basis with proper precautions. In lactation, most agents used in stroke care have been evaluated for safety, though individual risk assessments are needed.",
        "option_analysis": "Option A (MCA) is the correct answer, as it is the most common site for ischemic strokes and fits the described scenario. Option B (PCA) supplies the occipital lobe and is less commonly involved in the typical clinical presentation presented. Option C (Anterior choroidal artery) supplies deep brain structures and would usually produce a more restricted clinical syndrome. Option D is not provided.",
        "clinical_pearls": "1. The middle cerebral artery is the most commonly occluded vessel in ischemic stroke. 2. MCA territory infarcts are typically characterized by contralateral hemiparesis and aphasia if the dominant hemisphere is affected. 3. Quick identification and treatment are essential to improve outcomes.",
        "current_evidence": "Recent guidelines emphasize the role of endovascular thrombectomy in MCA occlusions, particularly in large vessel occlusions, with multiple randomized controlled trials confirming its efficacy in improving functional outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993199",
    "fields": {
      "question_number": "282",
      "question_text": "What is the mechanism?",
      "options": {
        "A": "tramatic haemorrage",
        "B": "ICh",
        "C": "lobar haemorrage",
        "D": "is not provided."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question evaluates the understanding of the underlying mechanisms leading to intracranial bleeding. The differentiation between traumatic and spontaneous hemorrhages is critical in neurology. Here, the focus is on spontaneous intracerebral hemorrhage (ICH).",
        "pathophysiology": "Intracerebral hemorrhage typically occurs due to rupture of small penetrating arteries, most commonly as a consequence of chronic hypertension. Long-standing high blood pressure leads to changes in the vessel wall (e.g., formation of Charcot-Bouchard microaneurysms) which predispose them to rupture. Lobar hemorrhages, while a subset of ICH, are often associated with cerebral amyloid angiopathy, particularly in older patients.",
        "clinical_correlation": "ICH presents with the sudden onset of headache, vomiting, a decline in levels of consciousness, and focal neurological deficits. The location of the hemorrhage (deep vs. lobar) can provide clues to its etiology; hypertensive ICH frequently occurs in deep structures such as the basal ganglia or thalamus.",
        "diagnostic_approach": "A noncontrast CT scan is the diagnostic modality of choice for ICH, as it quickly differentiates hemorrhagic from ischemic strokes. MRI can be used in subacute settings for further characterization. Differential diagnoses include traumatic brain hemorrhage, subarachnoid hemorrhage, and lobar hemorrhage due to different etiologies such as amyloid angiopathy.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified primarily by location and etiology. The major categories include: 1) Hypertensive deep hemorrhages affecting basal ganglia, thalamus, pons, and cerebellum; 2) Lobar hemorrhages, often related to cerebral amyloid angiopathy; 3) Traumatic hemorrhages, including contusions and diffuse axonal injury; and 4) Secondary hemorrhages due to vascular malformations, tumors, or coagulopathy. The classification is reflected in systems such as the SMASH-U classification (Structural lesion, Medication, Amyloid angiopathy, Systemic/Hypertensive, Hypertensive, Undetermined) which aids in etiologic diagnosis. This nosology has evolved to emphasize etiology for guiding management and prognosis. There is consensus that distinguishing spontaneous ICH (e.g., hypertensive, amyloid) from traumatic hemorrhage is critical, as mechanisms and treatments differ substantially.",
        "classification_and_nosology": "Intracerebral hemorrhages are classified based on location (deep vs. lobar, cerebellar, brainstem) and etiology. Hypertensive hemorrhages are typically located in deep brain structures, whereas lobar hemorrhages are more often linked with cerebral amyloid angiopathy.",
        "management_principles": "Management of ICH includes rapid blood pressure control, reversal of any coagulopathy, and supportive care. Patients may require neurosurgical evaluation for hematoma evacuation if there is significant mass effect or deterioration in the neurological exam. In pregnant patients, blood pressure control must consider both maternal and fetal safety, with agents chosen that have established safety profiles. In lactating mothers, medication choices are similarly guided by safety data for breastfeeding.",
        "option_analysis": "Option A (Traumatic hemorrhage) is incorrect in the absence of a history of trauma. Option B (ICH) is the correct answer, representing a spontaneous intracerebral hemorrhage, likely hypertensive in origin. Option C (Lobar hemorrhage) is a subtype of ICH but typically relates to cerebral amyloid angiopathy in the elderly and is less likely in a 56-year-old man; thus, it is less appropriate without specific supporting details. Option D is not provided.",
        "clinical_pearls": "1. Hypertension is the most common risk factor for spontaneous ICH. 2. Blood pressure management is crucial in the acute phase to prevent hemorrhage expansion. 3. Differentiating the hemorrhage location (deep vs. lobar) assists in identifying the underlying etiology.",
        "current_evidence": "Emerging research focuses on optimal blood pressure targets and minimally invasive surgical techniques for ICH evacuation. Current guidelines recommend early aggressive management of blood pressure and individualized decisions regarding surgical intervention, with ongoing studies further refining best practices."
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
