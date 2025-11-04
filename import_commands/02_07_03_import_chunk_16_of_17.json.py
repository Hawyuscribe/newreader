
# Import batch 3 of 3 from chunk_16_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993258",
    "fields": {
      "question_number": "17",
      "question_text": "Around 70 yo female patient with history of DM, HTN, previous stroke 2 months ago, presented with 3.5 hours of right side weakness, facial weakness, dysarthria, NIHSS 8. Presented to the ER, CT & CTA brain done. BP 172/60, afebrile. CBC normal, INR 1.3 plt 160. What is the management:",
      "options": {
        "A": "IV thrombolytic thereby is absolute contraindication - Mechanical thrombectomy",
        "B": "IV thrombolysis",
        "C": "IV thrombolysis and mechanical thrombectomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "This question examines the management of acute ischemic stroke (AIS) in a patient with significant contraindications to IV thrombolysis. The scenario highlights how recent medical history, such as a previous stroke, influences treatment decisions.",
        "pathophysiology": "IV thrombolysis (tPA) carries a risk for hemorrhagic transformation of ischemic brain tissue. In patients with a recent stroke\u2014especially within the past three months\u2014the brain may be more vulnerable, increasing the risk of hemorrhage when tPA is administered. This necessitates careful patient selection and strict adherence to guidelines.",
        "clinical_correlation": "The patient, a 70-year-old female with a history of diabetes, hypertension, and a prior stroke 2 months ago, presents with moderate neurological deficits (NIHSS 8). Although she is within the window for reperfusion (3.5 hours), the recent stroke represents a critical contraindication to tPA use, heightening the risk of intracranial hemorrhage. CT and CTA have been appropriately performed to evaluate for large vessel occlusion.",
        "diagnostic_approach": "In AIS workup, after confirming no hemorrhage on CT and evaluating for large vessel occlusion on CTA, clinicians must review contraindications to tPA. A history of stroke within the last 3 months is a recognized contraindication. Differential considerations might include evaluating whether the previous stroke is old and stable versus recent and unstable, as the risk profiles differ.",
        "classification_and_neurology": "Stroke is classified broadly into ischemic and hemorrhagic types. Ischemic strokes are further subclassified by etiology using systems like TOAST (Trial of Org 10172 in Acute Stroke Treatment), which includes large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. This patient likely has a large artery atherosclerotic or embolic stroke given her risk factors and presentation. The management of AIS falls under cerebrovascular disease within neurology, with acute management protocols guided by time-based and imaging-based criteria. The American Heart Association/American Stroke Association (AHA/ASA) guidelines provide standardized criteria for thrombolysis and thrombectomy eligibility. Nosological evolution includes expanding indications for mechanical thrombectomy beyond the initial 6-hour window based on advanced imaging (DAWN and DEFUSE 3 trials). Contraindications to thrombolysis have been refined to balance hemorrhagic risk and benefit.",
        "classification_and_nosology": "This patient falls under the AIS category with contraindications for standard IV thrombolysis. The management algorithm for AIS distinguishes between patients eligible for IV tPA and those who require alternative therapies, such as mechanical thrombectomy.",
        "management_principles": "According to current AHA/ASA guidelines, a previous stroke within the past 3 months is considered an absolute contraindication to IV tPA due to the high risk of hemorrhagic complications. For patients with large vessel occlusion and contraindications to tPA, mechanical thrombectomy is recommended. In settings such as pregnancy or lactation, mechanical thrombectomy remains a therapeutic option when tPA is contraindicated, with appropriate multidisciplinary consultation.",
        "option_analysis": "Option A is correct because it identifies that IV thrombolysis is contraindicated in this patient (due to the stroke 2 months ago) and that mechanical thrombectomy should be considered as the next line of intervention. Option B (IV thrombolysis alone) and Option C (combination of IV thrombolysis and mechanical thrombectomy) are incorrect due to the contraindication imposed by the recent stroke.",
        "clinical_pearls": "1. A history of stroke within the past 3 months is a key contraindication to administering IV tPA due to an elevated risk of hemorrhage. 2. Mechanical thrombectomy is the preferred intervention in patients with large vessel occlusion who are ineligible for IV thrombolysis.",
        "current_evidence": "Recent trials and updated guidelines continue to support mechanical thrombectomy for AIS patients with large vessel occlusion, especially when thrombolytics are contraindicated. Emerging research is focused on expanding treatment windows and refining selection criteria, but the contraindications for IV tPA, such as recent stroke, remain firmly established."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993259",
    "fields": {
      "question_number": "18",
      "question_text": "Same scenario but image was CTA not attached they asked about max same CT brain NIHSS 12",
      "options": {
        "A": "DUAP",
        "B": "Aspirin and plaxix",
        "C": "Tpa",
        "D": "IV tpa",
        "E": "IV heparin",
        "F": "Aspirin and plavix"
      },
      "correct_answer": "Aspirin monotherapy",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke is a medical emergency in which immediate reperfusion therapy can markedly improve outcomes. The cornerstone for eligible patients presenting within 4.5 hours is intravenous thrombolysis with tissue plasminogen activator (IV tPA), particularly when the stroke severity (e.g., an NIHSS score of 12 indicating moderate deficits) supports active intervention.",
        "pathophysiology": "In ischemic stroke, an artery is occluded by a thrombus or embolus, leading to reduced blood flow, energy failure, and infarction of brain tissue. IV tPA works by dissolving fibrin clots, thereby re-establishing blood flow to preserve the ischemic penumbra. This mechanism is most effective when administered early, before irreversible injury occurs.",
        "clinical_correlation": "A patient presenting with a CT brain (to exclude hemorrhage), a moderate NIHSS of 12, and within the therapeutic time window is an ideal candidate for IV tPA. Skipping tPA (for example, by using aspirin monotherapy) would deprive the patient of a time\u2010sensitive benefit that can improve long\u2010term neurologic function.",
        "diagnostic_approach": "The diagnosis is made by first excluding hemorrhage with a noncontrast CT. Advanced imaging (like CTA) is used to confirm vessel occlusion and assess for large vessel occlusion. Differential diagnoses include intracerebral hemorrhage, stroke mimics such as seizures or hypoglycemia, and transient neurological events. The rapid imaging assessment helps in selecting the appropriate therapy.",
        "classification_and_neurology": "Acute ischemic strokes are classified etiologically by the Trial of Org 10172 in Acute Stroke Treatment (TOAST) criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. LVO strokes fall under large artery atherosclerosis or cardioembolism categories. The NIHSS provides a quantitative clinical classification of stroke severity. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify stroke management into hyperacute (within 4.5 hours for IV tPA, up to 24 hours for MT in selected cases), acute, subacute, and chronic phases. Endovascular therapy has been integrated into the classification of reperfusion strategies alongside intravenous thrombolysis. This dual approach reflects evolving consensus from landmark trials such as MR CLEAN, ESCAPE, and DAWN. Controversies remain regarding optimal patient selection criteria, time windows, and adjunctive therapies, but current nosology emphasizes a combined pharmacologic and mechanical reperfusion paradigm for LVO strokes.",
        "classification_and_nosology": "This situation falls under the category of acute ischemic stroke. Stroke classification systems differentiate between small vessel (lacunar), large vessel, and cardioembolic causes. In this case, with moderate deficits and a CT demonstrating no hemorrhage, reperfusion therapy with IV tPA is the first-line intervention.",
        "management_principles": "According to current AHA/ASA guidelines, the first-line management for patients with acute ischemic stroke within 4.5 hours and without contraindications is IV tPA. In patients with large vessel occlusion, mechanical thrombectomy (MT) may be added. In pregnancy, tPA may be used if the benefits outweigh the risks, and it is considered relatively safe with proper multidisciplinary management. Lactating women can also receive tPA with careful observation.",
        "option_analysis": "Option A (DUAP) likely refers to dual antiplatelet therapy, which is not standard in acute moderate stroke when reperfusion is possible. Option B (Aspirin and Plavix) represents dual antiplatelet therapy, recommended in certain TIA or minor stroke scenarios but not as a substitute for reperfusion therapy in a moderate stroke. Option C (tPA) is ambiguous regarding the route; the approved treatment is IV tPA. Option D (IV tPA) is the correct, guideline-supported choice. Option E (IV heparin) is contraindicated in acute ischemic stroke due to the risk of hemorrhagic transformation. The marked answer, \u201cAspirin monotherapy,\u201d does not meet the current standards for acute management in this scenario.",
        "clinical_pearls": "1. Time is brain: every minute delay in reperfusion therapy leads to a greater infarct size. 2. Always perform a noncontrast CT to rule out hemorrhage before administering tPA. 3. Dual antiplatelet therapy is not a substitute for tPA in patients who are eligible for thrombolysis.",
        "current_evidence": "Recent guidelines continue to support the use of IV tPA in eligible acute stroke patients. Studies and systematic reviews have consistently shown improved functional outcomes with timely IV tPA administration, and ongoing research is refining patient selection criteria, including assessments using advanced neuroimaging."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993260",
    "fields": {
      "question_number": "19",
      "question_text": "Around 62 yo male patient with history of DM 12 years ago, presented to the ER with history of left side weakness lasted for 10 min then resolved, HTN 150/60 What is the risk of stroke in 90 days?",
      "options": {
        "A": "Low risk 3%",
        "B": "High 18 %",
        "C": "Moderate risk",
        "E": "(IV heparin) is contraindicated in acute ischemic stroke due to the risk of hemorrhagic transformation. The marked answer, \u201cAspirin monotherapy,\u201d does not meet the current standards for acute management in this scenario."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke is a medical emergency in which immediate reperfusion therapy can markedly improve outcomes. The cornerstone for eligible patients presenting within 4.5 hours is intravenous thrombolysis with tissue plasminogen activator (IV tPA), particularly when the stroke severity (e.g., an NIHSS score of 12 indicating moderate deficits) supports active intervention.",
        "pathophysiology": "In ischemic stroke, an artery is occluded by a thrombus or embolus, leading to reduced blood flow, energy failure, and infarction of brain tissue. IV tPA works by dissolving fibrin clots, thereby re-establishing blood flow to preserve the ischemic penumbra. This mechanism is most effective when administered early, before irreversible injury occurs.",
        "clinical_correlation": "A patient presenting with a CT brain (to exclude hemorrhage), a moderate NIHSS of 12, and within the therapeutic time window is an ideal candidate for IV tPA. Skipping tPA (for example, by using aspirin monotherapy) would deprive the patient of a time\u2010sensitive benefit that can improve long\u2010term neurologic function.",
        "diagnostic_approach": "The diagnosis is made by first excluding hemorrhage with a noncontrast CT. Advanced imaging (like CTA) is used to confirm vessel occlusion and assess for large vessel occlusion. Differential diagnoses include intracerebral hemorrhage, stroke mimics such as seizures or hypoglycemia, and transient neurological events. The rapid imaging assessment helps in selecting the appropriate therapy.",
        "classification_and_neurology": "TIA is classified within the spectrum of cerebrovascular diseases, specifically under ischemic cerebrovascular events. The traditional time-based definition classified TIA as neurological symptoms lasting less than 24 hours; however, modern imaging-based definitions emphasize the absence of infarction on diffusion-weighted MRI. The ABCD2 scoring system is the most widely accepted risk stratification tool, categorizing patients into low (score 0\u20133), moderate (4\u20135), and high risk (6\u20137) groups for stroke within 90 days. This patient\u2019s profile (age >60, hypertension, diabetes, clinical features) likely places him in the high-risk category. The classification also distinguishes TIA from minor stroke, with the latter showing evidence of infarction. Nosologically, TIA is part of the transient ischemic cerebrovascular syndromes and is related to large artery atherosclerosis, cardioembolism, and small vessel disease subtypes.",
        "classification_and_nosology": "This situation falls under the category of acute ischemic stroke. Stroke classification systems differentiate between small vessel (lacunar), large vessel, and cardioembolic causes. In this case, with moderate deficits and a CT demonstrating no hemorrhage, reperfusion therapy with IV tPA is the first-line intervention.",
        "management_principles": "According to current AHA/ASA guidelines, the first-line management for patients with acute ischemic stroke within 4.5 hours and without contraindications is IV tPA. In patients with large vessel occlusion, mechanical thrombectomy (MT) may be added. In pregnancy, tPA may be used if the benefits outweigh the risks, and it is considered relatively safe with proper multidisciplinary management. Lactating women can also receive tPA with careful observation.",
        "option_analysis": "Option A (DUAP) likely refers to dual antiplatelet therapy, which is not standard in acute moderate stroke when reperfusion is possible. Option B (Aspirin and Plavix) represents dual antiplatelet therapy, recommended in certain TIA or minor stroke scenarios but not as a substitute for reperfusion therapy in a moderate stroke. Option C (tPA) is ambiguous regarding the route; the approved treatment is IV tPA. Option D (IV tPA) is the correct, guideline-supported choice. Option E (IV heparin) is contraindicated in acute ischemic stroke due to the risk of hemorrhagic transformation. The marked answer, \u201cAspirin monotherapy,\u201d does not meet the current standards for acute management in this scenario.",
        "clinical_pearls": "1. Time is brain: every minute delay in reperfusion therapy leads to a greater infarct size. 2. Always perform a noncontrast CT to rule out hemorrhage before administering tPA. 3. Dual antiplatelet therapy is not a substitute for tPA in patients who are eligible for thrombolysis.",
        "current_evidence": "Recent guidelines continue to support the use of IV tPA in eligible acute stroke patients. Studies and systematic reviews have consistently shown improved functional outcomes with timely IV tPA administration, and ongoing research is refining patient selection criteria, including assessments using advanced neuroimaging."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993261",
    "fields": {
      "question_number": "20",
      "question_text": "Left MCA occlusion within 3.5hr from sx onset. Had hx of ischemic stroke 2 months ago. NIHSS 8. What to do?",
      "options": {
        "A": "IV tPA",
        "B": "IV tPA + MT",
        "C": "DAPT",
        "D": "IV heparin"
      },
      "correct_answer": "Mechanical thrombectomy alone",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "This patient presents with an acute left middle cerebral artery (MCA) occlusion within 3.5 hours of symptom onset \u2013 a scenario typically managed with reperfusion therapy. In most eligible patients, the standard treatment would be intravenous (IV) tissue plasminogen activator (tPA) within 4.5 hours, ideally combined with mechanical thrombectomy (MT) for large vessel occlusions (LVO). However, a history of an ischemic stroke only 2 months ago contraindicates the use of IV tPA due to increased hemorrhagic risk. Thus, the core principle is to offer mechanical thrombectomy alone to safely revascularize the occluded territory while avoiding the risks posed by thrombolytics in this setting.",
        "pathophysiology": "In acute ischemic stroke from a large vessel occlusion like the MCA, a thrombus obstructs arterial blood flow resulting in ischemia and infarction of the brain tissue supplied by that vessel. There is an ischemic core of irreversibly damaged tissue surrounded by a penumbra of potentially salvageable brain tissue. Mechanical thrombectomy directly removes the occlusive clot, restoring blood flow and minimizing the extent of infarction.",
        "clinical_correlation": "Despite an NIH Stroke Scale (NIHSS) score of 8, a left MCA occlusion\u2014even with moderate deficits\u2014can result in significant functional impairment, such as language deficits if the dominant hemisphere is involved or motor deficits affecting daily activities. The recent stroke history further limits the safe use of IV tPA, making mechanical thrombectomy the primary intervention.",
        "diagnostic_approach": "The diagnostic process for acute stroke typically involves obtaining a noncontrast head CT to rule out hemorrhage and a CT angiogram to identify the occlusion. In this case, the left MCA occlusion is confirmed on vascular imaging. Differential diagnoses include intracerebral hemorrhage and stroke mimics, but imaging is decisive in confirming an LVO. The recent stroke history is also ascertained from the patient\u2019s clinical history.",
        "classification_and_neurology": "Acute ischemic stroke is classified within cerebrovascular diseases (ICD-10 I63). The TOAST classification categorizes ischemic strokes etiologically (large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined, and undetermined causes). MCA occlusion typically falls under large artery atherosclerosis or cardioembolism. Stroke severity is classified by NIHSS scores (mild <5, moderate 5-15, severe >15). Treatment classification distinguishes between reperfusion therapies (IV thrombolysis, mechanical thrombectomy) and secondary prevention (antiplatelets, anticoagulants). The current consensus, as per AHA/ASA guidelines, supports IV tPA within 4.5 hours for eligible patients and mechanical thrombectomy up to 24 hours in select cases with large vessel occlusion and salvageable brain tissue. Controversies persist regarding thrombolysis in recent stroke and optimal management of moderate strokes with large vessel occlusion.",
        "classification_and_nosology": "This case is classified as an acute ischemic stroke due to large vessel occlusion (LVO). Within stroke subtypes, LVO strokes have specific treatment pathways that include mechanical thrombectomy. Patients with LVO and contraindications for thrombolysis (such as recent stroke) fall into a distinct management category.",
        "management_principles": "Current American Heart Association/American Stroke Association guidelines recommend that for patients with acute ischemic stroke due to LVO who are within the treatment window, IV tPA should be administered if no contraindications exist. However, a recent ischemic stroke (within 3 months) is a relative contraindication to IV tPA because of the increased risk of hemorrhagic transformation. Therefore, in this patient, mechanical thrombectomy alone is indicated. For pregnant or lactating patients, while IV tPA has been used in selected cases with caution, thrombectomy is generally favored when there is a contraindication to tPA, as it minimizes systemic drug exposure and potential risks.",
        "option_analysis": "Option A (IV tPA) is contraindicated because of the recent stroke. Option B (IV tPA + MT) similarly exposes the patient to the thrombolytic risk, which is unacceptable in this context. Options C (Dual Antiplatelet Therapy) and D (IV Heparin) are not appropriate for acute revascularization in LVO strokes. The marked answer of 'Mechanical thrombectomy alone' is the only treatment that aligns with guideline-based management for a patient with a recent stroke and confirmatory imaging of a left MCA occlusion.",
        "clinical_pearls": "1. A history of ischemic stroke within the last 3 months is a contraindication to IV tPA because of hemorrhagic risk. 2. Mechanical thrombectomy is effective in removing thrombi in large vessel occlusions, even in patients with moderate NIHSS scores, if the deficits are disabling. 3. In patients with contraindications to thrombolysis, especially in those with recent strokes or other contraindications, MT alone is the preferred method of reperfusion.",
        "current_evidence": "Landmark trials such as MR CLEAN, ESCAPE, and REVASCAT have demonstrated that mechanical thrombectomy significantly improves outcomes in patients with LVO. Current guidelines endorse MT either in addition to tPA or, in cases where tPA is contraindicated (such as a recent stroke within 3 months), as the sole reperfusion therapy. This evidence supports the marked answer of using mechanical thrombectomy alone in this patient."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993262",
    "fields": {
      "question_number": "21",
      "question_text": "Young male with ICA occlusion in vessel image post MVA with ischemic infarctions. What is the diagnosis?",
      "options": {
        "A": "Dissection",
        "B": "Thromboembolism",
        "C": "Atherosclerosis",
        "D": "Vasculitis",
        "E": "Other"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Carotid dissection involves a tear in the intimal layer of the internal carotid artery, allowing blood to enter the vessel wall, forming a hematoma that narrows or occludes the lumen. In a young male following an MVA with imaging evidence of ICA occlusion and ischemic infarctions, dissection is the most consistent diagnosis.",
        "pathophysiology": "Traumatic forces during an MVA can cause a tear in the arterial wall (intima) of the ICA. Blood entering the subintimal space creates an intramural hematoma, leading to vessel stenosis or complete occlusion, which in turn causes reduced cerebral perfusion and ischemia.",
        "clinical_correlation": "Patients with traumatic dissection generally present with signs of stroke such as focal neurological deficits, headache, or neck pain. In young patients without significant atherosclerotic risk factors, and particularly following trauma, dissection should be high on the differential diagnosis.",
        "diagnostic_approach": "Key imaging modalities include CT angiography or MR angiography, which can reveal features such as a double lumen, intimal flap, or tapered occlusion. Differential diagnoses include thromboembolism, atherosclerosis, and vasculitis; however, these are less likely in a young post-traumatic scenario.",
        "classification_and_neurology": "ICA dissection falls under the category of cervicocephalic arterial dissections, a subset of ischemic stroke etiologies classified within the TOAST (Trial of Org 10172 in Acute Stroke Treatment) criteria as 'other determined etiology' or sometimes under 'arterial dissection.' Dissections are further classified by location (extracranial vs intracranial), etiology (traumatic vs spontaneous), and vessel involved (carotid vs vertebral). This classification is important for prognosis and management. The classification of ischemic strokes has evolved to incorporate vessel wall imaging findings and genetic predispositions. Controversies remain regarding optimal classification when multiple etiologies coexist or when dissections are spontaneous without clear trauma.",
        "classification_and_nosology": "Carotid dissection is classified under arterial dissections, a subgroup of vascular injuries that can lead to ischemic stroke. In young patients, it is one of the leading causes of stroke related to trauma.",
        "management_principles": "Management typically includes antithrombotic therapy, with either antiplatelet agents or anticoagulants used to prevent thromboembolic complications. Current guidelines recommend careful patient selection. In pregnant or lactating women, low dose aspirin is generally considered safe, while warfarin is contraindicated and low molecular weight heparin can be used with appropriate caution. Endovascular interventions are reserved for cases that do not respond to medical management or where there is clinical deterioration.",
        "option_analysis": "Option A (Dissection) is the most accurate answer given the clinical scenario. Thromboembolism, while a potential result of dissection, is not the primary diagnosis in this traumatic context; atherosclerosis is unlikely in a young individual, and vasculitis typically presents with systemic findings, making them less appropriate choices.",
        "clinical_pearls": "In any young patient presenting with stroke after trauma, carotid dissection should be strongly considered. Rapid imaging is critical for diagnosis, as early initiation of antithrombotic therapy can significantly affect outcomes. Special considerations should be taken in pregnant or lactating patients to ensure both maternal and fetal safety.",
        "current_evidence": "Recent guidelines from the American Heart Association and American Stroke Association support the use of either antiplatelet or anticoagulant therapy in managing carotid dissection. Emerging research also emphasizes individualized management approaches based on the patient's clinical condition and comorbid status, with a focus on safe therapies during pregnancy and lactation."
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
