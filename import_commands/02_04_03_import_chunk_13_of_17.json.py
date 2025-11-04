
# Import batch 3 of 3 from chunk_13_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993249",
    "fields": {
      "question_number": "33",
      "question_text": "Two weeks Postpartum with headache, presented with left side weakness. MRI picture with right cortical ICH with surrounding edema",
      "options": {
        "A": "aneurysm rupture",
        "B": "CVT"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Postpartum women are in a hypercoagulable state due to physiological changes of pregnancy and the postpartum period. This increases their risk for venous thromboembolic events, including cerebral venous thrombosis (CVT), which can present with headache and focal neurologic deficits.",
        "pathophysiology": "CVT occurs when thrombi form in the cerebral venous sinuses or cortical veins. In the postpartum period, elevated coagulation factors and reduced fibrinolysis predispose to clot formation. Thrombotic occlusion leads to increased venous pressure, disruption of the blood\u2013brain barrier, vasogenic edema, and sometimes hemorrhagic venous infarction manifesting as a cortical intracerebral hemorrhage with surrounding edema.",
        "clinical_correlation": "A postpartum woman presenting two weeks after delivery with headache and left-sided weakness fits the clinical picture for CVT. The imaging finding of a right cortical intracerebral hemorrhage with surrounding edema is consistent with a hemorrhagic venous infarction secondary to venous sinus thrombosis rather than a typical hypertensive or aneurysmal bleed.",
        "diagnostic_approach": "The diagnosis typically involves neuroimaging. An MRI combined with MR venography is the modality of choice to detect venous occlusions. Differential diagnoses include aneurysm rupture (which usually causes subarachnoid hemorrhage rather than a cortical hemorrhage) and primary intracerebral hemorrhage from hypertension. The patient\u2019s postpartum status and imaging findings should raise suspicion for CVT.",
        "classification_and_neurology": "Postpartum intracerebral hemorrhage falls under the broader category of stroke, specifically hemorrhagic stroke. CVT is classified within cerebrovascular disorders affecting cerebral venous outflow, distinct from arterial ischemic stroke and aneurysmal subarachnoid hemorrhage. According to the International Classification of Diseases (ICD-11), CVT is coded under venous thrombosis of the intracranial veins and sinuses, while aneurysmal rupture is classified under non-traumatic intracerebral hemorrhage or subarachnoid hemorrhage depending on bleeding location. The nosology has evolved with improved imaging, recognizing CVT as a distinct entity with unique pathophysiology and management. Controversies remain in classification when hemorrhagic transformation occurs, but consensus supports categorizing based on the primary vascular pathology. Understanding these classifications aids in epidemiological tracking, research, and tailored therapeutic strategies.",
        "classification_and_nosology": "CVT is classified as a form of stroke and falls under cerebrovascular disorders. It can be further subclassified by the site of venous occlusion (e.g., superior sagittal sinus, lateral sinus, cortical veins) and by its clinical presentation (isolated intracranial hypertension, focal deficits, or seizures).",
        "management_principles": "According to current guidelines, the mainstay of CVT treatment is early anticoagulation \u2013 typically low-molecular-weight heparin (LMWH) even when intracerebral hemorrhage is present. In the postpartum period, LMWH is preferred due to its safety profile in lactating women and its predictable pharmacokinetics. Second-line treatments might include unfractionated heparin in cases where rapid reversal might be necessary. Follow\u2010up imaging and long\u2010term anticoagulation duration are individualized based on risk factors.",
        "option_analysis": "Option A (aneurysm rupture) is unlikely because aneurysmal subarachnoid hemorrhage typically presents with a sudden severe headache and subarachnoid blood on imaging, not a cortical ICH with surrounding edema. Marked Answer B (CVT) is correct given the patient\u2019s postpartum hypercoagulable state and the imaging findings. Options C and D were not provided.",
        "clinical_pearls": "1. The postpartum period is a high-risk time for venous thromboembolic events, including CVT. 2. CVT can cause hemorrhagic venous infarctions, so a hemorrhage on imaging does not preclude the diagnosis. 3. Anticoagulation is indicated for CVT even in the presence of hemorrhage.",
        "current_evidence": "Recent research and guideline updates (including AHA/ASA recommendations) emphasize early diagnosis and initiation of anticoagulation therapy in CVT. Studies have supported the safety and efficacy of LMWH in postpartum patients, reinforcing its role even when hemorrhagic infarction is present."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993250",
    "fields": {
      "question_number": "34",
      "question_text": "75 years old female, DM, HTN who came with acute right side weakness. CTA angiography showed left ICA at 60% and right is 65% what to do",
      "options": {
        "A": "Maximize medical management",
        "B": "Carotid endarterectomy",
        "C": "Elective carotid stenting",
        "D": "Stenting within 1 week"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Management of carotid artery disease in the context of stroke is largely driven by the degree of stenosis and symptoms. Surgical interventions like carotid endarterectomy (CEA) are typically reserved for high-grade stenoses in symptomatic individuals.",
        "pathophysiology": "Atherosclerotic plaque formation in the carotid arteries can lead to luminal narrowing. In this patient, the moderate stenosis (60-65%) suggests atherosclerotic disease that has not reached thresholds (generally \u226570% in symptomatic patients) where surgical intervention confers a significant benefit over medical therapy.",
        "clinical_correlation": "The elderly patient with vascular risk factors (DM and HTN) presenting with acute right-sided weakness is suggestive for an ischemic stroke. CTA findings showing moderate carotid stenosis indicate that the stroke is more likely due to small vessel or other embolic mechanisms rather than significant carotid artery obstruction warranting surgical revascularization.",
        "diagnostic_approach": "The diagnostic workup in stroke includes vascular imaging (like CTA or carotid Duplex ultrasound) to assess carotid stenosis. Differential diagnoses include cardioembolic stroke, intracranial atherosclerotic disease, and lacunar strokes. The decision between medical versus surgical management hinges on the degree of stenosis and whether the patient is symptomatic.",
        "classification_and_neurology": "Carotid artery stenosis is classified based on the degree of luminal narrowing, commonly using the NASCET (North American Symptomatic Carotid Endarterectomy Trial) criteria: mild (<50%), moderate (50-69%), and severe (\u226570%). Symptomatic stenosis refers to patients with recent ischemic symptoms in the territory of the stenosed artery, while asymptomatic stenosis lacks recent symptoms. This classification informs treatment decisions. Stroke subtypes are also classified (e.g., TOAST criteria) to identify large artery atherosclerosis as a cause. Management guidelines evolve based on evidence from landmark trials such as NASCET and CREST, which established the benefit of CEA in symptomatic severe stenosis. Controversies remain regarding timing and modality of intervention in the acute stroke phase.",
        "classification_and_nosology": "Carotid atherosclerotic disease is categorized by the degree of luminal narrowing: mild (<50%), moderate (50-69%), and severe (\u226570%). In symptomatic individuals, CEA is typically recommended for severe stenosis, while moderate stenosis is usually managed medically.",
        "management_principles": "Current guidelines recommend intensive medical management (antiplatelet therapy, statins, blood pressure control, and lifestyle modifications) as the first-line approach for moderate carotid stenosis. Carotid revascularization (CEA or stenting) is indicated primarily in symptomatic patients with at least 70% stenosis. For a 75-year-old with moderate stenosis and significant comorbidities, maximizing medical therapy is most appropriate. In terms of pregnancy and lactation, this scenario does not apply; however, emphasis on medical management is similarly preferred when surgical risks outweigh benefits.",
        "option_analysis": "Option A (Maximize medical management) is correct because the stenosis levels (60% and 65%) do not meet the threshold for surgical intervention. Option B (Carotid endarterectomy) and Option C (Elective carotid stenting) are typically reserved for higher-grade stenosis. Option D (Stenting within 1 week) is not appropriate given the degree and the acute setting without severe stenoses.",
        "clinical_pearls": "1. In symptomatic patients, carotid revascularization is generally considered when stenosis is 70% or greater. 2. Intensive medical management is the cornerstone for moderate carotid stenosis. 3. Risk factor modification is critical in stroke prevention.",
        "current_evidence": "Recent trials and guideline updates (including those from the AHA/ASA and the European Society for Vascular Surgery) support optimal medical therapy for moderate carotid stenosis, highlighting that surgical benefits are most pronounced in patients with high-grade (>70%) stenosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993251",
    "fields": {
      "question_number": "35",
      "question_text": "Pregnant female patient with positive antiphospholipid who had a stroke was found to have small PFO, and prior history of DVT, what is the next best step",
      "options": {
        "A": "Aspirin",
        "B": "Close the PFO",
        "C": "Heparin",
        "D": "Warfarin"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Antiphospholipid syndrome (APS) is an acquired thrombophilia that predisposes patients to both arterial and venous thrombosis. In pregnant patients, APS poses a significant risk for stroke and recurrent venous thromboembolic events, making anticoagulation the cornerstone of management.",
        "pathophysiology": "APS involves the production of antiphospholipid antibodies (eg, anticardiolipin, lupus anticoagulant) that interfere with normal coagulation. These antibodies lead to endothelial dysfunction and activation of the coagulation cascade, resulting in both arterial (stroke) and venous (DVT) thrombosis. The presence of a small patent foramen ovale (PFO) is incidental in this context and does not drive the treatment strategy.",
        "clinical_correlation": "A pregnant woman with a history of DVT and a positive APS screen who also presents with a stroke strongly suggests that her event is due to hypercoagulability associated with APS. In pregnancy, warfarin is contraindicated owing to its teratogenicity, and PFO closure is not indicated for APS-related strokes.",
        "diagnostic_approach": "The diagnosis of APS is based on clinical criteria (history of thrombosis or pregnancy morbidity) plus laboratory confirmation (presence of antiphospholipid antibodies on two occasions at least 12 weeks apart). Differential considerations include cardioembolic strokes from PFO-related paradoxical embolism; however, the history of DVT and APS positivity points toward a thrombophilic process.",
        "classification_and_neurology": "Antiphospholipid syndrome is classified as a systemic autoimmune thrombophilia under the category of acquired thrombophilic disorders. The revised Sapporo criteria (2006) define APS based on clinical events (vascular thrombosis or pregnancy morbidity) plus laboratory evidence of persistent antiphospholipid antibodies.  Stroke in APS is considered a form of arterial thrombosis within this syndrome. PFO is a congenital cardiac anomaly classified among interatrial communications. Paradoxical embolism is a clinical syndrome bridging cardiology and neurology.  Stroke classification systems such as TOAST include cardioembolic stroke, under which paradoxical embolism via PFO can be categorized. The management of APS-related stroke requires integrating autoimmune disease classification, thrombophilia taxonomy, and stroke etiological frameworks.  There is ongoing debate regarding the role of PFO closure in patients with APS due to the autoimmune thrombophilia component.",
        "classification_and_nosology": "APS can be classified as primary (in the absence of another autoimmune disorder) or secondary (associated with conditions like systemic lupus erythematosus). It is considered an important cause of hypercoagulability in young to middle-aged individuals, particularly women.",
        "management_principles": "For pregnant patients with APS, the current guideline-recommended first-line treatment is the use of heparin \u2013 typically low molecular weight heparin (LMWH) \u2013 often in combination with low-dose aspirin. This regimen is safe during pregnancy and lactation. Warfarin is contraindicated in pregnancy due to teratogenic effects, and PFO closure is not recommended given that the underlying issue is hypercoagulability rather than an anatomic shunt.",
        "option_analysis": "Option A (Aspirin) alone is insufficient for a high-risk APS patient with a history of DVT and stroke. Option B (Close the PFO) addresses a potential embolic source but is not indicated when APS is the underlying cause. Option D (Warfarin) is contraindicated in pregnancy. Option C (Heparin) is the correct choice as it effectively anticoagulates the patient while being safe in pregnancy.",
        "clinical_pearls": "1. In pregnant patients with APS, LMWH plus low-dose aspirin is the standard treatment to prevent recurrent thrombosis. 2. A small PFO in an APS patient is likely incidental; focus should be on managing the hypercoagulable state. 3. Warfarin is prohibited during pregnancy due to its known teratogenic risks.",
        "current_evidence": "Recent studies and updated guidelines (including those from the American College of Rheumatology and obstetrical societies) consistently support the combined use of LMWH and aspirin in pregnant patients with APS to reduce the risk of thrombotic complications."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993252",
    "fields": {
      "question_number": "36",
      "question_text": "Stroke within window what should be done before IV tPA.",
      "options": {
        "A": "Coagulation",
        "B": "Glucose Level",
        "C": "ECG"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Before administration of IV tPA for acute ischemic stroke, it is crucial to rule out mimics and contraindications. One of the rapid, bedside tests is the measurement of blood glucose, as hypoglycemia can produce stroke-like symptoms.",
        "pathophysiology": "Hypoglycemia can lead to focal neurological deficits that closely mimic a stroke. Because tPA is a potent thrombolytic agent with significant hemorrhagic risks, it is imperative to ensure that the patient\u2019s symptoms are due to true ischemic stroke rather than a metabolic disturbance.",
        "clinical_correlation": "In an acute stroke setting, rapid evaluation is paramount. A fingerstick blood glucose test is easily performed, and abnormal values (too low or too high) must be corrected before considering thrombolytic therapy. This helps prevent unnecessary administration of tPA to patients with stroke mimics.",
        "diagnostic_approach": "Prior to IV tPA administration, the standard workup includes a non-contrast CT scan to exclude hemorrhage, a rapid fingerstick blood glucose measurement, and assessment of coagulation parameters if indicated (especially in patients on anticoagulants). Differential considerations include hypoglycemia, which can both mimic and worsen neurological deficits.",
        "classification_and_neurology": "Acute ischemic stroke is classified etiologically by systems such as the TOAST classification, which categorizes strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. The management of acute ischemic stroke falls under cerebrovascular disorders. The classification of stroke by time window (hyperacute within 4.5 hours, acute, subacute, chronic) guides therapeutic decisions including thrombolysis eligibility. Pre-thrombolysis evaluation is a key step in the acute stroke management protocol endorsed by guidelines such as those from the American Heart Association/American Stroke Association (AHA/ASA). These guidelines emphasize rapid but thorough assessment to optimize patient selection for IV tPA and minimize complications.",
        "classification_and_nosology": "Acute ischemic stroke evaluation includes a battery of tests aimed at confirming the diagnosis and excluding contraindications to thrombolytic therapy. Glucose level measurement is a key component of this protocol.",
        "management_principles": "Current guidelines (AHA/ASA) mandate that a bedside blood glucose test be performed in all suspected stroke patients before tPA administration to rule out hypoglycemia. Although coagulation studies and ECG are also important components of the overall stroke workup, the glucose test is rapid and critical in the immediate decision-making process. In pregnancy or lactation, similar protocols are used; however, additional considerations (like radiation exposure from CT) are managed with protective measures. tPA itself is contraindicated in certain pregnancy settings but may be considered in life-threatening strokes with informed risk-benefit discussions.",
        "option_analysis": "Option A (Coagulation) is important if there is suspicion of a coagulopathy or if the patient is on anticoagulants, but it is not as immediately critical as checking blood glucose. Option C (ECG) is useful for detecting arrhythmias (such as atrial fibrillation) that might suggest a cardioembolic source but is not a prerequisite for tPA administration. Marked Answer B (Glucose Level) is correct because verifying a normal blood glucose level is a rapid and necessary step to avoid treating a stroke mimic.",
        "clinical_pearls": "1. Always perform a rapid fingerstick blood glucose test in suspected stroke cases before administering tPA. 2. Hypoglycemia can mimic stroke, so its prompt correction is essential. 3. Although additional tests (coagulation studies, ECG) are important, they are secondary to the immediate check of blood glucose in the acute setting.",
        "current_evidence": "Recent AHA/ASA guidelines reiterate the necessity of checking blood glucose immediately in the acute stroke setting to ensure that the clinical picture is indeed due to ischemia and not a hypoglycemic event. This practice remains a cornerstone in the door-to-needle protocols for IV thrombolysis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993253",
    "fields": {
      "question_number": "37",
      "question_text": "Same picture of Moyamoya in Q12 with right side weakness and CTA showing severe stenosis in the left MCA, what to do next",
      "options": {
        "A": "Exchange Transfusion",
        "B": "Aspirin and Plavix",
        "C": "Labetalol"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Moyamoya syndrome is characterized by progressive steno\u2010occlusive changes in the terminal portions of the internal carotid arteries and their proximal branches. In patients with sickle cell disease (SCD), a moyamoya pattern may develop as a complication of chronic vaso-occlusive injury. In the acute setting of a stroke with evidence of severe MCA stenosis in an SCD patient, rapid reduction of sickled hemoglobin (HbS) is critical.",
        "pathophysiology": "In SCD, abnormal hemoglobin S leads to red cell sickling under stress conditions. These sickled cells trigger endothelial injury, promoting intimal proliferation and eventual vascular stenosis and occlusion. The moyamoya\u2010like vascular changes, with the formation of fragile collateral vessels, predispose the patient to ischemic events. Urgent reduction of circulating HbS via exchange transfusion improves blood rheology and oxygen delivery, helping to limit infarct size.",
        "clinical_correlation": "The patient\u2019s right-sided weakness correlates with left MCA territory ischemia. In the context of a sickle cell patient showing imaging features of moyamoya, the clinical picture is that of an acute ischemic stroke precipitated by vaso-occlusion. Rapid intervention is essential to mitigate further neurologic damage.",
        "diagnostic_approach": "Diagnosis is typically made with non-invasive imaging such as CTA or MRA to document the stenotic changes. Differential diagnoses include atherosclerotic stroke, vasculitis, or reversible cerebral vasoconstriction syndrome (RCVS), but in a young patient with SCD and moyamoya findings, vaso-occlusion is the underlying mechanism. Confirmation of sickle cell status and hemoglobin electrophoresis support the diagnosis.",
        "classification_and_neurology": "Moyamoya disease is classified as a chronic, idiopathic cerebrovascular occlusive disease. It is part of the broader category of intracranial arterial steno-occlusive disorders. The disease can be classified into:  - **Primary Moyamoya disease**: idiopathic, bilateral involvement without associated conditions. - **Secondary Moyamoya syndrome**: similar vascular changes associated with other conditions such as Down syndrome, neurofibromatosis, sickle cell disease, or radiation therapy.  The classification is important because secondary Moyamoya requires addressing the underlying cause.  The disease is also categorized by angiographic staging (Suzuki stages I-VI) based on severity of arterial occlusion and collateral formation.  Controversies exist regarding the nomenclature and whether unilateral cases represent early Moyamoya or distinct entities. Current consensus favors the term 'Moyamoya syndrome' for secondary causes and 'Moyamoya disease' for idiopathic cases.",
        "classification_and_nosology": "Moyamoya can be idiopathic (Moyamoya disease) or secondary (Moyamoya syndrome) when associated with conditions like SCD. In sickle cell patients, the syndrome is recognized as a complication stemming from chronic hemolytic and vaso-occlusive phenomena.",
        "management_principles": "For an acute ischemic stroke in a sickle cell patient with moyamoya-like features, the first-line treatment is urgent exchange transfusion to reduce circulating HbS levels (aiming for <30%). This intervention is critical to arrest further sickling and ischemic injury. Long-term management may include possible revascularization surgery after stabilization and rigorous secondary stroke prevention measures. In pregnant or lactating patients with SCD, exchange transfusion is considered safe with appropriate hematologic consultation and monitoring, as the benefits in reducing ischemic brain injury outweigh potential risks.",
        "option_analysis": "Option A (Exchange Transfusion) is correct because it directly addresses the acute pathophysiology of sickle cell\u2013related stroke by reducing HbS and improving cerebral perfusion. Option B (Aspirin and Plavix) is more appropriate for atherosclerotic or non\u2013sickle cell embolic strokes and does not address the unique pathophysiology of SCD. Option C (Labetalol) is aimed at blood pressure control and is not the primary acute treatment for sickle cell stroke.",
        "clinical_pearls": "\u2022 In SCD patients with stroke, early exchange transfusion can limit infarct expansion.  \u2022 Moyamoya syndrome in SCD warrants careful neuroimaging evaluation.  \u2022 Time is brain \u2013 rapid intervention is essential in vaso-occlusive stroke.",
        "current_evidence": "Recent guidelines from hematology and stroke societies support early exchange transfusion in SCD patients presenting with acute ischemic stroke. Studies have demonstrated that prompt reduction of HbS levels significantly reduces the progression of cerebral infarction, and this approach is endorsed in current SCD management protocols."
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
