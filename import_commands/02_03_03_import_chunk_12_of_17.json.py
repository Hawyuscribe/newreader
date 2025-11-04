
# Import batch 3 of 3 from chunk_12_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993415",
    "fields": {
      "question_number": "2",
      "question_text": "What is the mechanism?",
      "options": {
        "A": "(Aneurysm rupture) is incorrect because the hemorrhage pattern in premesencephalic hemorrhage does not support an aneurysmal source. Option B (Atherosclerosis) is incorrect as it is associated with ischemic strokes rather than subarachnoid hemorrhage. Option C (Premesencephalic hemorrhage) is correct because it accurately describes the mechanism for this subtype of SAH. The previously marked answer (D) does not correspond to any of the relevant options provided."
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Subarachnoid hemorrhage (SAH) can occur due to a variety of mechanisms. Premesencephalic (or perimesencephalic) hemorrhage is a subtype of non-aneurysmal SAH characterized by bleeding in the cisternal spaces around the midbrain with a relatively benign clinical course.",
        "pathophysiology": "Unlike aneurysmal SAH, which is typically due to aneurysm rupture and is associated with a high risk of rebleeding and vasospasm, premesencephalic hemorrhage is believed to result from venous or small arterial bleeding in the premesencephalic cisterns. It usually does not involve an aneurysm, and patients often experience a smoother recovery with fewer complications.",
        "clinical_correlation": "Patients with premesencephalic hemorrhage tend to present with a sudden-onset headache that may be less severe than that associated with aneurysmal SAH. Neurological deficits are often minimal, and the clinical course is more benign. The limited blood spread on imaging distinguishes it from aneurysmal SAH.",
        "diagnostic_approach": "Initial evaluation with non-contrast CT typically shows blood localized around the midbrain without the extensive subarachnoid spread seen in aneurysm rupture. Vascular imaging (CTA, MRA, or digital subtraction angiography) is undertaken to rule out aneurysms. Differential diagnoses include aneurysmal SAH and other non-aneurysmal causes of SAH, which are differentiated based on the distribution of blood on imaging and clinical severity.",
        "classification_and_neurology": "Subarachnoid hemorrhages can be classified based on etiology into aneurysmal, traumatic, perimesencephalic (also called premesencephalic), and other less common causes such as arteriovenous malformations or coagulopathies. The Fisher scale classifies SAH based on CT appearance to predict vasospasm risk but does not differentiate etiology. The World Federation of Neurosurgical Societies (WFNS) grading scale assesses clinical severity. Premesencephalic hemorrhage is considered a nonaneurysmal SAH subtype with distinct clinical and radiographic features. Historically, nonaneurysmal SAH was often lumped together, but current consensus recognizes perimesencephalic hemorrhage as a unique entity with a different pathophysiology and prognosis. This classification impacts management decisions, particularly regarding the need for invasive angiography and surgical intervention.",
        "classification_and_nosology": "Premesencephalic hemorrhage is classified as a non-aneurysmal subarachnoid hemorrhage. This entity is distinct from aneurysmal SAH both in terms of etiology and prognosis, and it is generally associated with lower morbidity and mortality.",
        "management_principles": "Management is generally conservative, including bed rest, analgesia, and close neurological monitoring. Nimodipine is less frequently used because the risk of vasospasm is much lower compared to aneurysmal SAH. In pregnant or lactating women, conservative management is especially preferred unless there is evidence of complications, with decisions being made in consultation with neurology and maternal-fetal medicine specialists.",
        "option_analysis": "Option A (Aneurysm rupture) is incorrect because the hemorrhage pattern in premesencephalic hemorrhage does not support an aneurysmal source. Option B (Atherosclerosis) is incorrect as it is associated with ischemic strokes rather than subarachnoid hemorrhage. Option C (Premesencephalic hemorrhage) is correct because it accurately describes the mechanism for this subtype of SAH. The previously marked answer (D) does not correspond to any of the relevant options provided.",
        "clinical_pearls": "1. Premesencephalic hemorrhage has a benign course compared to aneurysmal SAH, with lower rates of vasospasm and rebleeding. 2. The localization of bleeding on CT is a critical clue in differentiating premesencephalic hemorrhage from aneurysmal SAH. 3. Vascular imaging must be performed to exclude the presence of an aneurysm, even when a premesencephalic pattern is suspected.",
        "current_evidence": "Recent studies have confirmed that patients with premesencephalic hemorrhage generally have excellent outcomes and benefit from conservative management. Updated guidelines recommend distinguishing this entity from aneurysmal SAH to ensure appropriate, less invasive management strategies are applied."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993413",
    "fields": {
      "question_number": "2",
      "question_text": "sickler pt come with stroke work up done and found to have multiple stenosis in AcA and McA. Ehat is the method of prevention?",
      "options": {
        "A": "aspirin",
        "B": "plavix",
        "C": "chronic transfusion",
        "D": "dual antiplate"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Sickle cell disease (SCD) predisposes patients to cerebrovascular complications because of the abnormal hemoglobin (HbS) that can polymerize under low oxygen conditions. This leads to recurrent vaso\u2010occlusion and chronic vascular injury. In the context of stroke prevention, reducing the proportion of sickled cells is paramount.",
        "pathophysiology": "In SCD, red blood cells containing HbS undergo polymerization during deoxygenation, leading to deformation and aggregation. The recurring infarctions and subsequent vessel wall injury result in stenosis in critical cerebral arteries such as the anterior cerebral (AcA) and middle cerebral (McA) arteries. Chronic transfusion therapy works by diluting the concentration of HbS, thus lowering the risk of further vaso\u2010occlusive events and progression of vasculopathy.",
        "clinical_correlation": "Patients with SCD frequently develop cerebrovascular disease, which may manifest as stroke or transient ischemic attacks, particularly when arterial stenosis is present. A history of abnormal transcranial Doppler studies or a prior stroke indicates the need for aggressive measures to prevent recurrence.",
        "diagnostic_approach": "The workup includes transcranial Doppler ultrasound (especially in the pediatric population) to screen for increased velocities, brain MRI to delineate infarcted areas, and vascular imaging (CTA/MRA) to assess the degree and location of arterial stenoses. Differential diagnoses include other causes of stroke such as cardioembolic events or conventional atherosclerosis, but the presence of SCD directs the etiology to vaso\u2010occlusion mechanisms.",
        "classification_and_neurology": "Stroke in sickle cell disease is classified as a secondary ischemic stroke due to a hematologic disorder causing vasculopathy. According to the TOAST classification, it falls under stroke subtype 5: stroke of other determined etiology. The vascular pathology in SCD represents a unique cerebrovascular disease entity characterized by large-vessel stenosis and small-vessel disease. The classification of SCD-related cerebrovascular disease has evolved to emphasize the role of transcranial Doppler velocities and MRI/MRA findings in stratifying stroke risk. Current nosology integrates clinical, radiographic, and hematologic criteria to guide prevention and treatment. This condition is part of the broader family of hematologic stroke syndromes, distinct from atherosclerotic or cardioembolic strokes.",
        "classification_and_nosology": "Strokes in the setting of SCD are classified as ischemic strokes resulting from large vessel vasculopathy. They are distinct from atherosclerotic strokes seen in the general population and are managed accordingly.",
        "management_principles": "First\u2010line prevention for recurrent strokes in SCD is chronic transfusion therapy aimed at maintaining the percentage of HbS below a target threshold (often <30%). In addition, hydroxyurea is sometimes used in select patients to reduce vaso\u2010occlusive crises. For pregnant or lactating patients with SCD, transfusion protocols are modified with close monitoring to avoid iron overload and alloimmunization, while hydroxyurea is generally avoided during pregnancy.",
        "option_analysis": "\u2022 Option A (aspirin): Although antiplatelet agents are standard in general stroke prevention, they do not address the underlying sickling process in SCD. \n\u2022 Option B (plavix): Similarly, clopidogrel is not indicated as a primary preventive measure in SCD-related strokes. \n\u2022 Option C (chronic transfusion): This is the evidence-based approach for secondary prevention in SCD patients with stroke, addressing the fundamental abnormality by reducing HbS levels. \n\u2022 Option D (dual antiplatelet): Dual antiplatelet therapy is used in atherosclerotic disease but is not the standard measure for stroke prevention in SCD.",
        "clinical_pearls": "\u2022 Chronic transfusion therapy has been shown to reduce recurrent stroke risk in patients with SCD by decreasing the proportion of HbS. \n\u2022 Regular transcranial Doppler screening is a key preventive strategy in pediatric SCD populations.",
        "current_evidence": "Recent trials and guidelines (for example, those emerging from the STOP and TWiTCH studies) have reinforced the use of chronic transfusion therapy as the cornerstone for preventing recurrent stroke events in patients with SCD."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993411",
    "fields": {
      "question_number": "2",
      "question_text": "What you will do:",
      "options": {},
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Large vessel atherosclerotic disease that leads to stroke is initially managed with optimized medical therapy rather than immediate intervention. The focus is on reducing the risk factors that contribute to plaque formation and thrombosis.",
        "pathophysiology": "Atherosclerotic plaques develop in the carotid or other large cerebral vessels, which can lead to significant stenosis and increased risk of thromboembolic events. The systemic inflammatory process and endothelial dysfunction promote plaque instability. Medical therapy aims to stabilize plaques, control dyslipidemia, and reduce platelet aggregation.",
        "clinical_correlation": "In patients with symptomatic or high-grade carotid stenosis, the choice between medical management, endarterectomy, or stenting depends on the degree of stenosis, symptom status, and individual patient risk factors. Often, patients present with minor strokes or transient ischemic attacks and require risk factor modification as a first-line approach.",
        "diagnostic_approach": "Diagnosis is supported by duplex ultrasound, CTA, or MRA to quantify the degree of stenosis. Differential diagnoses include cardioembolism and small vessel disease, which are managed differently.",
        "classification_and_neurology": "Large vessel cerebrovascular disease falls under the broader category of ischemic stroke etiologies, specifically classified within the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system as 'large artery atherosclerosis.' This category includes atherosclerotic stenosis or occlusion of major extracranial or intracranial arteries. The disease family encompasses carotid artery disease, intracranial atherosclerosis, and other large vessel pathologies. Over time, classification systems have evolved to incorporate imaging findings and genetic markers, but TOAST remains widely used in clinical practice and research. Some controversies exist regarding the classification of intracranial versus extracranial disease and the role of embolic versus hemodynamic mechanisms, but large artery atherosclerosis is a well-established nosological entity.",
        "classification_and_nosology": "Carotid artery disease is typically classified based on the degree of stenosis (mild, moderate, or severe) and whether the patient is symptomatic versus asymptomatic. Current guidelines stratify treatment choices according to these classifications.",
        "management_principles": "\u2022 First-line management is optimized medical therapy, including antiplatelet agents (like aspirin), high-intensity statin therapy, and strict control of blood pressure and diabetes. \n\u2022 Carotid endarterectomy is reserved for symptomatic patients with high-grade stenosis (commonly >70%). \n\u2022 Carotid stenting is considered in patients who are not candidates for surgery. \nPregnancy and lactation: In pregnant patients, medication choices must consider fetal safety; low-dose aspirin may be continued, but statins are contraindicated. A tailored therapeutic plan is necessary.",
        "option_analysis": "\u2022 Option 1 (Angioplasty alone): Not adequate as a sole therapy because angioplasty without stenting can lead to vessel recoil and restenosis. \n\u2022 Option 2 (Stent): Carotid stenting has a higher periprocedural stroke risk and is generally reserved for patients with contraindications to surgery. \n\u2022 Option 3 (Endarterectomy): While effective, it is not universally applied and is appropriate mainly in selected high-grade stenosed, symptomatic patients. \n\u2022 Option 4 (Medical therapy): This is the appropriate first-line intervention, focusing on aggressive risk factor modification and pharmacologic therapy.",
        "clinical_pearls": "\u2022 Optimized medical therapy remains the cornerstone for initial management of most patients with large vessel cerebrovascular stenosis. \n\u2022 Revascularization techniques are specifically reserved for cases where the benefit outweighs the risks based on the degree of stenosis and symptomatology.",
        "current_evidence": "Recent studies, including the CREST trial and evolving AHA/ASA guidelines, underscore the importance of initiating intensive medical therapy as the primary approach for stroke prevention in patients with carotid stenosis, with revascularization considered only in select high-risk patient populations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993563",
    "fields": {
      "question_number": "20",
      "question_text": "Stroke all stroke workups mentioned except CTA asked what to do next",
      "options": {
        "A": "(CTA): Correct because it provides rapid, comprehensive vascular imaging necessary for acute stroke management. \n\u2022 Option B: Does not offer the comprehensive vascular assessment needed for immediate management decisions. Other non"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In the workup of acute stroke, after initial non-contrast imaging to rule out hemorrhage, rapid vascular imaging is critical to identify occlusions or stenoses that can guide acute therapeutic interventions.",
        "pathophysiology": "Cerebrovascular occlusions, particularly in large vessel strokes, require quick identification to determine candidacy for reperfusion therapies. Computed tomography angiography (CTA) provides detailed images of the cerebral vasculature, allowing for identification of vessel occlusions and stenosis patterns.",
        "clinical_correlation": "In an acute stroke setting, time is brain \u2013 rapid identification of a large vessel occlusion can lead to timely decisions regarding thrombolysis or thrombectomy, which are essential for improving outcomes.",
        "diagnostic_approach": "The usual diagnostic workflow in suspected acute ischemic stroke includes an initial non-contrast CT (NCCT) to exclude hemorrhage, followed by CTA to evaluate the arterial system. Differential diagnoses might include plain CT (which cannot assess vessel patency adequately), MRI/MRA (which is accurate but may not be as rapidly accessible), or carotid Doppler (limited to extracranial evaluation).",
        "classification_and_neurology": "Stroke classification systems, such as the TOAST criteria, categorize ischemic strokes based on etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. Vascular imaging including CTA is instrumental in classifying strokes as large artery atherosclerosis or dissection by revealing arterial pathology. The American Heart Association/American Stroke Association (AHA/ASA) guidelines emphasize vascular imaging as part of the comprehensive stroke evaluation. The classification informs secondary prevention strategies and prognosis. Over time, stroke classification has evolved to integrate advanced imaging findings, recognizing the heterogeneity of stroke mechanisms and facilitating personalized management.",
        "classification_and_nosology": "Acute stroke imaging is categorized into basic imaging (NCCT) for hemorrhage exclusion and advanced imaging (CTA, MRA) for vascular delineation. CTA is the most commonly used modality in acute settings due to its speed, accessibility, and high-resolution detail.",
        "management_principles": "Current guidelines (such as those from the AHA/ASA) recommend that after an NCCT, CTA should be performed immediately to assess for large vessel occlusion, facilitating decision making regarding thrombolytic therapy or endovascular intervention. In pregnancy, non-contrast imaging is preferred initially to reduce radiation, but if CTA is necessary, precautions (such as abdominal shielding) should be taken. In lactating patients, CTA can be performed as the risk is minimal.",
        "option_analysis": "\u2022 Option A (CTA): Correct because it provides rapid, comprehensive vascular imaging necessary for acute stroke management. \n\u2022 Option B: Does not offer the comprehensive vascular assessment needed for immediate management decisions. Other non-contrast studies or limited vascular studies are insufficient when CTA data is critical for reperfusion decision-making.",
        "clinical_pearls": "\u2022 CTA is the modality of choice to rapidly evaluate the cerebral vasculature after initial stroke imaging. \n\u2022 Quick delineation of vascular status is essential for determining eligibility for advanced reperfusion therapies.",
        "current_evidence": "Recent evidence and updated AHA/ASA guidelines continue to support the role of CTA as a critical next step in the imaging algorithm for acute ischemic stroke, affirming its place in current stroke protocols."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993473",
    "fields": {
      "question_number": "21",
      "question_text": "Patient with ESRD Scenario with pic showing rt superficial borderzone infarction at MCA/ACA territory asking about next investigation",
      "options": {
        "A": "(Brain CT angiography alone): Although it provides good intracranial detail, it is incomplete without neck imaging to evaluate the carotid arteries. \n\u2022 Option B (Conventional angiography): While being the gold standard, it is invasive and carries higher risks, especially in ESRD patients. \n\u2022 Option C: Implied to represent a comprehensive CTA (including both brain and neck vessels), which is the most appropriate next investigation given its noninvasive nature and ability to assess the entire cerebrovascular system."
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Watershed (borderzone) infarctions typically occur in areas between major cerebral arterial territories and are often due to hemodynamic compromise rather than embolic occlusion. In patients with conditions such as ESRD, who have a higher burden of atherosclerosis, the evaluation of both intracranial and extracranial vessels is crucial.",
        "pathophysiology": "Borderzone infarcts result from hypoperfusion, where the distal territories of the cerebral arteries (such as the MCA and ACA territories) are inadequately supplied. This commonly occurs in the presence of significant arterial stenosis, especially at the carotid bifurcation, leading to a reduced perfusion pressure in these watershed regions.",
        "clinical_correlation": "In patients with ESRD, the risk of atherosclerotic disease is heightened. A superficial borderzone infarct as seen on imaging should prompt consideration of a hemodynamic mechanism, and a comprehensive vascular evaluation is necessary to determine the extent and location of any stenotic lesions.",
        "diagnostic_approach": "The optimal evaluation includes a CT angiography (CTA) that encompasses both the intracranial vessels and the cervical (extracranial) carotid arteries. Differential diagnoses include relying solely on brain CTA (which may miss extracranial pathology) or invasive conventional angiography, which carries unnecessary risk as a first-line investigation.",
        "classification_and_neurology": "Borderzone infarctions are classified under ischemic stroke subtypes in the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification as 'large artery atherosclerosis' or 'hemodynamic stroke' depending on the etiology. Watershed infarcts can be cortical (between MCA and ACA or MCA and PCA territories) or internal (between deep and superficial MCA territories). This classification system emphasizes the importance of vascular imaging and clinical context to differentiate stroke mechanisms. Alternative classification systems like CCS (Causative Classification of Stroke System) also incorporate imaging and clinical features. Understanding these classifications helps tailor investigations and treatment strategies. The consensus is that borderzone infarcts often indicate hemodynamic compromise, necessitating vascular imaging focused on extracranial and intracranial arteries.",
        "classification_and_nosology": "Watershed infarcts are classified as either cortical (superficial) or subcortical (deep) and are typically related to systemic hypoperfusion or significant upstream arterial stenosis. They are distinct from embolic or lacunar strokes.",
        "management_principles": "For patients with suspected hemodynamic compromise from carotid stenosis, a comprehensive, noninvasive vascular imaging study (CTA of both brain and neck) is the first investigation of choice. In patients with ESRD, while the use of contrast is a consideration, the patient\u2019s renal status (often already on dialysis) modifies the risk-benefit ratio. In pregnant or lactating patients, contrast studies are approached cautiously with appropriate shielding and timing, though ESRD typically precludes pregnancy.",
        "option_analysis": "\u2022 Option A (Brain CT angiography alone): Although it provides good intracranial detail, it is incomplete without neck imaging to evaluate the carotid arteries. \n\u2022 Option B (Conventional angiography): While being the gold standard, it is invasive and carries higher risks, especially in ESRD patients. \n\u2022 Option C: Implied to represent a comprehensive CTA (including both brain and neck vessels), which is the most appropriate next investigation given its noninvasive nature and ability to assess the entire cerebrovascular system.",
        "clinical_pearls": "\u2022 In borderzone infarctions, always ensure that the vascular imaging covers both intracranial and extracranial territories. \n\u2022 ESRD patients are at increased risk for significant atherosclerotic disease and warrant comprehensive evaluation despite concerns regarding contrast media.",
        "current_evidence": "The latest stroke imaging protocols and guidelines emphasize the value of a comprehensive CTA that includes neck imaging to assess for extracranial carotid disease, particularly in cases of watershed infarcts. This approach minimizes risk while providing detailed vascular mapping to guide further management."
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
