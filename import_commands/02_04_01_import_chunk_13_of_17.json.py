
# Import batch 1 of 3 from chunk_13_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993468",
    "fields": {
      "question_number": "23",
      "question_text": "Intracranial MCA severe stenosis what next",
      "options": {
        "A": "(DAPT) is correct because it directly targets the pathophysiology of platelet activation and subsequent thrombus formation in severe stenosis. Alternative options such as single antiplatelet therapy, anticoagulation, or immediate endovascular intervention are less suitable based on current evidence, which emphasizes the efficacy of DAPT. The marked answer (B) is incorrect because the evidence supports DAPT as the initial management strategy."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Intracranial stenosis of the MCA refers to a significant narrowing usually caused by atherosclerotic plaque, which predisposes patients to ischemic strokes. The core concept involves reducing the risk of thromboembolic events by stabilizing the atherosclerotic plaque and preventing platelet aggregation.",
        "pathophysiology": "Severe intracranial stenosis leads to turbulent blood flow and endothelial injury, which can trigger platelet activation and thrombus formation. The SAMMPRIS trial provided evidence that dual antiplatelet therapy (DAPT) with aspirin and clopidogrel reduces recurrent stroke risk by inhibiting platelet aggregation in these patients.",
        "clinical_correlation": "Patients with severe MCA stenosis may present with transient ischemic attacks or stroke symptoms corresponding to the MCA territory (e.g., contralateral weakness, speech disturbances). The risk of recurrent events is high unless effective antithrombotic strategies are implemented.",
        "diagnostic_approach": "Diagnosis typically involves non-invasive imaging such as CT/MRI to exclude infarcted tissue or hemorrhage, followed by vascular studies (MRA, CTA, or digital subtraction angiography) to assess the severity of stenosis. Differential diagnoses include dissection, vasculitis, and moyamoya disease, which are differentiated based on clinical history, imaging characteristics, and additional laboratory tests.",
        "classification_and_neurology": "Intracranial arterial stenosis is classified within the broader category of large artery atherosclerotic cerebrovascular disease, as per the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system. This system categorizes ischemic strokes based on etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. Intracranial MCA stenosis falls under large artery atherosclerosis. Further subclassification can be based on the degree of stenosis (mild <50%, moderate 50-69%, severe \u226570%), and the presence of symptoms (symptomatic vs. asymptomatic). The WASID (Warfarin-Aspirin Symptomatic Intracranial Disease) trial criteria are often used to define severity. There has been debate regarding optimal classification, but consensus supports using vascular imaging and clinical correlation to guide management. Understanding this nosology aids in prognosis and therapeutic decision-making.",
        "classification_and_nosology": "This condition falls under the umbrella of intracranial atherosclerotic disease, a known cause of ischemic stroke. It is also categorized based on the degree of stenosis (mild, moderate, severe) and whether it is symptomatic or asymptomatic.",
        "management_principles": "Current guidelines based on the SAMMPRIS trial recommend initiating DAPT (aspirin plus clopidogrel) for 90 days in patients with symptomatic severe intracranial stenosis. Risk factor modification, statin therapy, and lifestyle changes are also integral. For pregnant women, low-dose aspirin is typically considered safe, and while data on clopidogrel is limited, it may be used if the benefits outweigh the risks. Endovascular interventions remain a secondary option reserved for patients who fail medical therapy.",
        "option_analysis": "Option A (DAPT) is correct because it directly targets the pathophysiology of platelet activation and subsequent thrombus formation in severe stenosis. Alternative options such as single antiplatelet therapy, anticoagulation, or immediate endovascular intervention are less suitable based on current evidence, which emphasizes the efficacy of DAPT. The marked answer (B) is incorrect because the evidence supports DAPT as the initial management strategy.",
        "clinical_pearls": "1. DAPT with aspirin and clopidogrel is supported by evidence for reducing recurrent stroke in severe intracranial stenosis. 2. Early intensive medical management is often more beneficial than immediate invasive procedures. 3. Always assess and modify vascular risk factors concurrently.",
        "current_evidence": "The SAMMPRIS trial remains a cornerstone in the management of intracranial atherosclerotic disease, demonstrating that aggressive medical management with DAPT is superior to stenting in preventing recurrent strokes. Recent updates continue to support this approach, emphasizing individualized risk factor management and the potential role of newer antiplatelet agents."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993475",
    "fields": {
      "question_number": "24",
      "question_text": "Minor stroke NIHSS 3 (left side decrease sensation, mild facial weakness) within the window what\u2019s next",
      "options": {
        "A": "(DAPT) is not the appropriate acute treatment because it does not address the clot directly as required in reperfusion strategies. Option B (tPA) is correct because it actively dissolves the clot and has been shown to improve outcomes in acute ischemic stroke. Option C (Aspirin alone) only serves a role in secondary prevention and lacks the efficacy in restoring perfusion during the acute phase."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In patients with a minor stroke (NIHSS 3) who are within the thrombolytic window, the primary goal is to rapidly restore cerebral perfusion. Although the symptoms might be mild, if they are potentially disabling, acute reperfusion therapy is warranted.",
        "pathophysiology": "Ischemic stroke results from an occlusive thrombus that obstructs blood flow. Intravenous tPA facilitates clot dissolution (thrombolysis), thereby restoring blood flow and reducing the infarct size. Even minor strokes, if affecting eloquent areas, can have a significant impact on quality of life.",
        "clinical_correlation": "A patient presenting with decreased sensation and mild facial weakness, even with a low NIHSS score, may have deficits that are considered disabling if they impair daily activities. The timely administration of tPA can improve functional outcomes if given within the 4.5-hour therapeutic window.",
        "diagnostic_approach": "Evaluation begins with a non-contrast head CT to exclude hemorrhage, followed by assessment of eligibility for thrombolytic therapy. Stroke mimics (migraine, seizure, hypoglycemia) should be considered but can typically be excluded based on clinical evaluation and imaging.",
        "classification_and_neurology": "Ischemic stroke is classified etiologically by systems such as the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), other determined, and undetermined causes. Minor stroke is a clinical severity classification rather than a distinct subtype. The NIHSS provides a standardized measure of severity, guiding therapeutic decisions. Acute ischemic stroke management protocols stratify patients based on time from onset and stroke severity. The classification of stroke severity (minor, moderate, severe) influences eligibility for reperfusion therapies. Current consensus supports thrombolysis for eligible patients regardless of minor deficits, given evidence of benefit. Controversies exist about treating very mild or rapidly improving symptoms, but guidelines emphasize individualized assessment.",
        "classification_and_nosology": "Minor stroke is often defined as an NIHSS score less than or equal to 5, but the presence of disabling symptoms (even with a low score) may necessitate treatment with tPA. Stroke is classified as ischemic or hemorrhagic; in this case, it is an acute ischemic event.",
        "management_principles": "First-line management for eligible patients within the 4.5-hour window is intravenous thrombolysis (tPA). DAPT (aspirin plus clopidogrel) is recommended for secondary prevention but does not provide acute reperfusion. In pregnant patients, the use of tPA requires careful evaluation of risks versus benefits, though current literature suggests that, when indicated, tPA may be used in pregnancy on a case-by-case basis. In lactating women, tPA is generally considered safe because minimal transfer occurs into breast milk.",
        "option_analysis": "Option A (DAPT) is not the appropriate acute treatment because it does not address the clot directly as required in reperfusion strategies. Option B (tPA) is correct because it actively dissolves the clot and has been shown to improve outcomes in acute ischemic stroke. Option C (Aspirin alone) only serves a role in secondary prevention and lacks the efficacy in restoring perfusion during the acute phase.",
        "clinical_pearls": "1. Even minor strokes with disabling features warrant consideration for tPA if within the treatment window. 2. Quick imaging to differentiate ischemic from hemorrhagic events is critical before initiating thrombolysis. 3. Time is brain \u2013 the earlier the treatment, the better the potential outcome.",
        "current_evidence": "Recent guidelines and trials, including those reflected in the American Heart Association/American Stroke Association recommendations, support the use of tPA for mild but disabling stroke symptoms in eligible patients. Ongoing research continues to refine patient selection for thrombolytic therapy, especially in cases presenting with low NIHSS scores."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993480",
    "fields": {
      "question_number": "25",
      "question_text": "TIA found to have atrial flutter echo normal",
      "options": {
        "A": "(Factor Xa inhibitor) is correct because these agents have been shown to be effective in reducing the risk of embolic events in patients with atrial flutter. Other options such as antiplatelet therapy or rate control alone do not adequately reduce the thromboembolic risk associated with this arrhythmia."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Atrial flutter, similar to atrial fibrillation, predisposes patients to thrombus formation in the atria, which can embolize and cause transient ischemic attacks (TIAs) or strokes. The use of Factor Xa inhibitors is aimed at reducing this embolic risk.",
        "pathophysiology": "In atrial flutter, the organized but rapid atrial contractions lead to stasis in the atria, especially in the left atrial appendage. This stasis promotes clot formation. Factor Xa inhibitors, such as apixaban or rivaroxaban, block a key step in the coagulation cascade (the conversion of prothrombin to thrombin), thereby reducing clot formation and subsequent embolic events.",
        "clinical_correlation": "Patients with atrial flutter can present with TIAs or embolic strokes even when structural heart evaluations (like an echocardiogram) are normal. This underscores the need for appropriate anticoagulation rather than just symptomatic management.",
        "diagnostic_approach": "Diagnosis involves ECG to document atrial flutter, and often an echocardiogram to assess cardiac structure and function. Differential diagnoses include atrial fibrillation and other causes of cardioembolic stroke, such as valvular heart disease, which are differentiated based on the rhythm and imaging findings.",
        "classification_and_neurology": "TIA is classified under cerebrovascular diseases, specifically ischemic cerebrovascular events. According to the American Heart Association/American Stroke Association (AHA/ASA) guidelines, TIA is defined clinically by transient neurological symptoms without infarction on imaging. Atrial flutter is classified as a supraventricular tachyarrhythmia within cardiac arrhythmias. In the context of stroke classification, the TOAST (Trial of Org 10172 in Acute Stroke Treatment) criteria categorize strokes and TIAs by etiology; atrial flutter-associated TIA falls under cardioembolic stroke/TIA subtype. This classification guides management decisions, particularly anticoagulation. The nosology has evolved with improved imaging and understanding of arrhythmia-related embolism, emphasizing the need for rhythm monitoring and anticoagulation in non-valvular atrial arrhythmias. Controversies exist regarding the relative embolic risk of atrial flutter versus atrial fibrillation, but current consensus treats them similarly for stroke prevention.",
        "classification_and_nosology": "This condition is classified as a cardioembolic syndrome. Stroke prevention in patients with atrial flutter falls under the broader category of stroke prevention in atrial arrhythmias.",
        "management_principles": "Current guidelines recommend the use of direct oral anticoagulants (DOACs), including Factor Xa inhibitors, for stroke prevention in patients with non-valvular atrial flutter or atrial fibrillation. In pregnancy, however, the use of Factor Xa inhibitors is generally avoided due to limited safety data; low-molecular-weight heparin is preferred. In lactating women, caution is advised, but many DOACs may be considered if the benefits outweigh the risks.",
        "option_analysis": "Option A (Factor Xa inhibitor) is correct because these agents have been shown to be effective in reducing the risk of embolic events in patients with atrial flutter. Other options such as antiplatelet therapy or rate control alone do not adequately reduce the thromboembolic risk associated with this arrhythmia.",
        "clinical_pearls": "1. Always consider the cardioembolic source in TIA when atrial flutter is present. 2. DOACs are preferred over vitamin K antagonists for non-valvular atrial arrhythmias in most patients due to their improved safety profile and ease of management. 3. Tailor anticoagulation strategies in pregnant or lactating patients carefully.",
        "current_evidence": "Recent trials and updated guidelines continue to support the use of DOACs, including Factor Xa inhibitors, for stroke prevention in patients with atrial flutter/fibrillation. Ongoing studies are refining their risk-benefit profiles in special populations, including the elderly and those with co-morbid conditions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993476",
    "fields": {
      "question_number": "27",
      "question_text": "82 female with stroke NIHSS 20, BP 180/100, 3 hrs from symptoms onset, brain CT pic look okay no clear hypodensity but showed subtle early ischemic changes in BG, insular ribbon what to do next",
      "options": {
        "A": "(Labetalol) is incorrect because the patient\u2019s BP is below the threshold that necessitates acute lowering prior to thrombolysis; unnecessary BP reduction may compromise cerebral perfusion. Option B (Thrombolysis) is correct as the patient is within the 4.5",
        "C": "(Thrombectomy) is not immediately indicated without further vascular imaging confirming a large vessel occlusion."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke management, timely reperfusion therapy is critical. Intravenous thrombolysis (tPA) is indicated for patients presenting within 4.5 hours from symptom onset, provided there are no contraindications. Blood pressure management is an important precursor, but aggressive lowering is only necessary if the BP exceeds treatment thresholds.",
        "pathophysiology": "Acute stroke results from an occlusive thrombus leading to cerebral ischemia. tPA works by enzymatically breaking down the clot and restoring blood flow. Elevated blood pressure is a common physiologic response in acute ischemia, and excessive lowering may compromise perfusion in the penumbra.",
        "clinical_correlation": "An 82-year-old female with an NIHSS of 20 and blood pressure of 180/100 mmHg is a candidate for tPA as her blood pressure is below the critical threshold of 185/110 mmHg. The CT scan, though showing subtle early ischemic changes, is not contraindicating thrombolysis. The primary goal is rapid reperfusion to salvage viable brain tissue.",
        "diagnostic_approach": "The diagnostic process involves CT imaging to exclude hemorrhage and confirm early ischemic changes, and vascular studies if large vessel occlusion is suspected. Differential diagnoses include hemorrhagic stroke and stroke mimics, but the clinical scenario and imaging findings support ischemic stroke.",
        "classification_and_neurology": "Acute ischemic stroke is classified etiologically using systems such as the TOAST classification, which categorizes stroke into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and cryptogenic. This patient's presentation and imaging suggest a large vessel territory infarct, likely MCA distribution. Stroke severity is classified by NIHSS score, with 20 indicating severe stroke. The management of acute ischemic stroke falls under cerebrovascular disease classification within neurology. The therapeutic approach aligns with guidelines from the American Heart Association/American Stroke Association (AHA/ASA) for acute ischemic stroke. There is ongoing debate about extending thrombolysis windows and the role of advanced imaging to guide therapy, but current consensus supports intravenous thrombolysis within 4.5 hours of onset in eligible patients.",
        "classification_and_nosology": "This is an acute ischemic stroke with a significant burden as indicated by an NIHSS of 20. Stroke is categorized by etiology (ischemic vs hemorrhagic) and severity, with acute management strategies tailored accordingly.",
        "management_principles": "First-line management for eligible acute ischemic stroke patients is intravenous thrombolysis with tPA. Blood pressure should be managed only if it exceeds 185/110 mmHg. In this case, since the BP is 180/100 mmHg, withholding BP lowering medications (like labetalol) is crucial to maintain cerebral perfusion. Mechanical thrombectomy is reserved for patients with confirmed large vessel occlusion. In pregnancy, tPA may be administered when the benefit outweighs potential risks, while in lactation, tPA is generally considered safe with minimal excretion in breast milk.",
        "option_analysis": "Option A (Labetalol) is incorrect because the patient\u2019s BP is below the threshold that necessitates acute lowering prior to thrombolysis; unnecessary BP reduction may compromise cerebral perfusion. Option B (Thrombolysis) is correct as the patient is within the 4.5-hour window, with BP acceptable for tPA administration and imaging consistent with ischemia. Option C (Thrombectomy) is not immediately indicated without further vascular imaging confirming a large vessel occlusion.",
        "clinical_pearls": "1. Do not lower blood pressure aggressively in acute ischemic stroke if it is below 185/110 mmHg prior to tPA. 2. tPA administration within the therapeutic window significantly improves outcomes even in elderly patients. 3. Early imaging and rapid clinical assessment are key to determining eligibility for reperfusion therapy.",
        "current_evidence": "Current guidelines from the American Heart Association/American Stroke Association emphasize that patients with BP below 185/110 mmHg and within the 4.5-hour window should receive tPA. Recent studies continue to validate the safety and efficacy of thrombolysis in carefully selected elderly patients, reaffirming its role as the first-line therapy in acute ischemic stroke."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_23.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993485",
    "fields": {
      "question_number": "28",
      "question_text": "Case of malignant MCA with mass effect and decreased level of consciousness found unresponsive, what will change outcomes",
      "options": {
        "A": "(Decompressive hemicraniectomy) is correct because it directly addresses the mass effect and intracranial hypertension, altering the course of the disease. Option B (Stroke admission) is vital for supportive care but does not reverse the mass effect. Option C (Hyperventilation) only provides transient reduction of ICP and may risk ischemia without improving long\u2010term outcomes."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Malignant MCA infarction refers to a massive cerebral infarct in the middle cerebral artery territory that leads to severe cerebral edema and raised intracranial pressure. The central concept is that timely reduction of intracranial pressure through surgical means, specifically decompressive hemicraniectomy, can improve survival and functional outcomes.",
        "pathophysiology": "An occlusion of the MCA results in a large territory of brain tissue dying. This necrosis triggers both cytotoxic and vasogenic edema, which leads to a rapid rise in intracranial pressure and risk of herniation. Decompressive hemicraniectomy removes a part of the skull, allowing the swollen brain to expand and thus reducing the pressure on critical structures.",
        "clinical_correlation": "Clinically, these patients may present with decreased consciousness, signs of increased intracranial pressure (such as pupillary changes), and a risk for imminent brain herniation. Without intervention, the natural history is poor, with high mortality and morbidity.",
        "diagnostic_approach": "Diagnosis is confirmed with neuroimaging (CT/MRI), which will demonstrate a large infarct with significant edema and mass effect. Differential diagnoses include hemorrhagic stroke, large territorial infarction with hemorrhagic transformation, and brain abscess. However, the imaging and clinical context of an acute malignant stroke help differentiate these conditions.",
        "classification_and_neurology": "Malignant MCA infarction is classified as a subtype of large vessel ischemic stroke within the cerebrovascular disease spectrum. According to the TOAST classification, it falls under cardioembolic or large artery atherosclerosis strokes depending on etiology but is defined clinically and radiographically by its large infarct volume and malignant course. It is often differentiated from smaller MCA strokes by its rapid progression and life-threatening mass effect. The term \u201cmalignant\u201d reflects the high mortality and morbidity associated with the edema and herniation. Classification schemes have evolved to incorporate imaging criteria (e.g., infarct size >145 cm\u00b3 on diffusion-weighted MRI) that predict malignant edema. Current consensus guidelines recognize malignant MCA infarction as an indication for decompressive hemicraniectomy. Controversies in classification relate to timing and criteria for surgical intervention and the role of advanced imaging biomarkers. Overall, malignant MCA infarction is a severe clinical phenotype within the ischemic stroke family with distinct management implications.",
        "classification_and_nosology": "Malignant MCA infarction is classified as a severe form of ischemic stroke characterized by rapid development of life\u2010threatening cerebral edema. It is a specific subtype within ischemic strokes that carries a distinct management and prognosis profile.",
        "management_principles": "First-line management for patients with malignant MCA infarction in eligible populations (typically younger than 60 but individualized) is decompressive hemicraniectomy, optimally performed within 48 hours of stroke onset. Supportive treatment includes intensive care monitoring, osmotherapy, and maintaining adequate cerebral perfusion. In pregnant patients, surgical interventions are approached with careful multidisciplinary planning to balance maternal benefits with fetal safety. Non-surgical interventions like hyperventilation are only temporizing measures and insufficient as definitive management.",
        "option_analysis": "Option A (Decompressive hemicraniectomy) is correct because it directly addresses the mass effect and intracranial hypertension, altering the course of the disease. Option B (Stroke admission) is vital for supportive care but does not reverse the mass effect. Option C (Hyperventilation) only provides transient reduction of ICP and may risk ischemia without improving long\u2010term outcomes.",
        "clinical_pearls": "1. Early surgical intervention (within 48 hours) is crucial in malignant MCA infarction. 2. Non-surgical measures are supportive but do not change the natural history. 3. Decompressive hemicraniectomy has been shown in trials (e.g., DESTINY, HAMLET) to improve survival.",
        "current_evidence": "Recent randomized controlled trials, including DESTINY and HAMLET, support the use of decompressive hemicraniectomy in appropriately selected patients with malignant MCA infarction, and current guidelines recommend timely surgical evaluation to improve survival and functional outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993479",
    "fields": {
      "question_number": "29",
      "question_text": "Acute stroke treated with tPA pic showing tongue angio edema, patient stable but severely dysarthric, what to do",
      "options": {
        "A": "(Intubation) is incorrect in this context because the patient does not demonstrate active airway compromise. Option B (Steroid with antihistamine) is the appropriate first",
        "C": "(ACE inhibitor with diuretics) is contraindicated because ACE inhibitors can exacerbate angioedema."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "tPA-induced angioedema is a known complication of thrombolytic therapy in acute ischemic stroke. It typically manifests as localized swelling, most often involving the tongue or oropharyngeal structures, due to a bradykinin-mediated reaction.",
        "pathophysiology": "tPA catalyzes the conversion of plasminogen to plasmin, which, besides breaking down clots, can increase bradykinin levels. Elevated bradykinin increases vascular permeability leading to angioedema. This reaction is usually localized and can be particularly concerning if it progresses to airway compromise.",
        "clinical_correlation": "In this scenario, the patient exhibits tongue angioedema with dysarthria but remains stable, with no signs of respiratory distress or imminent airway obstruction. Recognizing the early signs of angioedema is important to prevent potential progression to life-threatening airway compromise.",
        "diagnostic_approach": "The diagnosis is predominantly clinical, based on the temporal association with tPA administration and the appearance of tongue swelling. Differential diagnoses include ACE inhibitor-induced angioedema and allergic reactions to other medications. Airway assessment is paramount, with tools such as fiberoptic laryngoscopy used if needed.",
        "classification_and_neurology": "tPA-induced angioedema is classified as a drug-induced, bradykinin-mediated angioedema distinct from histamine-mediated allergic angioedema. Within the broader category of angioedema, etiologies include hereditary (C1 esterase inhibitor deficiency), acquired, allergic (IgE-mediated), and drug-induced forms. The nosology recognizes tPA-induced angioedema as a unique iatrogenic complication related to fibrinolytic therapy, often overlapping with ACEi-associated angioedema due to shared bradykinin pathways. Stroke management guidelines categorize this complication under adverse drug reactions requiring emergent intervention. Understanding this classification aids in targeted management, differentiating it from anaphylaxis or other causes of airway swelling.",
        "classification_and_nosology": "Angioedema is categorized by etiology (allergic/histamine-mediated vs. bradykinin-mediated). tPA-induced angioedema is classified as bradykinin-mediated, which distinguishes it from other forms of drug-induced allergic reactions.",
        "management_principles": "First-line treatment for tPA-induced angioedema in a stable patient is the prompt administration of steroids combined with antihistamines. These agents work to reduce inflammation and limit the further progression of edema. Intubation is reserved for cases with clear evidence of airway compromise. For pregnant or lactating patients, low-dose steroids and certain antihistamines (those with a good safety profile) can be utilized, prioritizing airway security as the paramount concern.",
        "option_analysis": "Option A (Intubation) is incorrect in this context because the patient does not demonstrate active airway compromise. Option B (Steroid with antihistamine) is the appropriate first-line treatment to address the inflammatory and bradykinin-mediated components. Option C (ACE inhibitor with diuretics) is contraindicated because ACE inhibitors can exacerbate angioedema.",
        "clinical_pearls": "1. tPA-induced angioedema is often self-limited but requires close monitoring due to the risk of airway compromise. 2. Early administration of steroids and antihistamines can prevent further progression. 3. Airway management should be escalated only if there is evidence of respiratory distress.",
        "current_evidence": "Recent studies and updated guidelines emphasize vigilant monitoring following tPA administration. Although the precise protocols may vary, the combination of steroids and antihistamines remains the cornerstone of management for tPA-induced angioedema in non-compromised patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993424",
    "fields": {
      "question_number": "3",
      "question_text": "Long senario pt came with anyrism rupture of PcOm what you will do?",
      "options": {
        "A": "Cliping",
        "B": "Coiling",
        "C": "Decompressivw craniotomy",
        "D": "Amdission to stroke unit"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "A ruptured aneurysm, specifically in the posterior communicating artery (PcOM), is a neurosurgical emergency that typically presents as a subarachnoid hemorrhage. The key management goal is to secure the aneurysm promptly to prevent rebleeding.",
        "pathophysiology": "The rupture of an aneurysm leads to bleeding into the subarachnoid space, resulting in a sudden increase in intracranial pressure, irritation of the meninges, and potential vasospasm. Failure to secure the aneurysm places the patient at high risk for rebleeding, one of the main causes of morbidity and mortality.",
        "clinical_correlation": "Patients with aneurysmal rupture often present with a sudden, severe headache (sometimes described as 'thunderclap headache'), neck stiffness, and altered mental status. Early intervention is crucial to stabilize the patient and prevent complications.",
        "diagnostic_approach": "Diagnosis is typically made with a non-contrast head CT followed by CT angiography or digital subtraction angiography (DSA) to localize and characterize the aneurysm. Differential diagnoses include traumatic subarachnoid hemorrhage and perimesencephalic hemorrhage, which are differentiated based on imaging appearance and clinical history.",
        "classification_and_neurology": "Intracranial aneurysms are classified primarily by morphology (saccular, fusiform, dissecting), location (anterior vs. posterior circulation), and rupture status (ruptured vs. unruptured). PCOM aneurysms are saccular (berry) aneurysms located at the junction of the internal carotid artery and PCOM artery, part of the anterior circulation. The World Federation of Neurosurgical Societies (WFNS) grading and Hunt and Hess scale classify SAH severity based on clinical presentation, guiding prognosis and treatment urgency. The Fisher scale classifies SAH based on CT blood amount, predicting vasospasm risk. These classification systems help stratify patients and guide management. Current consensus favors early intervention for ruptured aneurysms regardless of grade to prevent rebleeding.",
        "classification_and_nosology": "Intracranial aneurysms are classified by location (e.g., anterior vs. posterior circulation), morphology (saccular, fusiform), and risk of rupture. PcOM aneurysms fall into the category of anterior circulation aneurysms and are among the more common sites for aneurysm formation.",
        "management_principles": "Endovascular coiling is generally preferred in many centers for treating ruptured aneurysms due to its less invasive nature and lower perioperative morbidity, provided the aneurysm\u2019s morphology is favorable. Microsurgical clipping remains an option when coiling is not feasible. In pregnant patients, endovascular procedures are performed with enhanced precautions to minimize fetal radiation exposure (using shielding and limiting contrast volume). Options like decompressive craniotomy or simple stroke unit admission are not definitive treatments for aneurysm rupture.",
        "option_analysis": "Option A (Clipping) is a viable alternative but is more invasive compared to coiling. Option B (Coiling) is correct as it represents the preferred endovascular method in many cases for securing the aneurysm. Option C (Decompressive craniotomy) does not address the source of bleeding. Option D (Admission to a stroke unit) is supportive care but not a definitive treatment.",
        "clinical_pearls": "1. Securing the aneurysm\u2014either via coiling or clipping\u2014is essential to prevent rebleeding. 2. Endovascular coiling is often preferred in anatomically favorable aneurysms. 3. Rapid identification and management are key to improving outcomes in subarachnoid hemorrhage.",
        "current_evidence": "Data from studies such as the International Subarachnoid Aneurysm Trial (ISAT) have demonstrated favorable outcomes with endovascular coiling compared to clipping in suitable patients. Current neurosurgical guidelines increasingly favor coiling as the first-line treatment in many cases of aneurysmal rupture."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993410",
    "fields": {
      "question_number": "3",
      "question_text": "60 years old male pt DM/ HTN/ came with history of TiA for 10 min numbness and dysarthtia. NiHSs is 3. We have to calculate ABCD2 score. On examination ot still have numbness what you will give",
      "options": {
        "A": "aspirin",
        "B": "plavix",
        "C": "dual"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Transient ischemic attacks (TIAs) are brief episodes of neurologic dysfunction caused by temporary cerebral ischemia. Risk stratification using tools like the ABCD2 score is essential to identify patients at higher risk for subsequent strokes and to guide antiplatelet therapy.",
        "pathophysiology": "TIAs occur when there is a temporary interruption of blood flow to the brain, leading to transient neurological deficits without infarction on imaging. Patients with vascular risk factors\u2014such as diabetes, hypertension, and older age\u2014are at increased risk of repeated events due to underlying atherosclerotic disease.",
        "clinical_correlation": "This 60-year-old male with diabetes and hypertension has experienced a TIA characterized by brief episodes of numbness and dysarthria. The presence of residual symptoms (persistent numbness) alongside a moderate NIHSS score (3) suggests an elevated risk for recurrent stroke, necessitating aggressive secondary prevention.",
        "diagnostic_approach": "Evaluation involves a thorough neurological exam supplemented by neuroimaging (CT/MRI) to rule out established infarction, as well as vascular imaging (carotid ultrasound, CT or MR angiography) to assess for significant stenosis. Differential diagnoses include seizure-related deficits, hypoglycemia, and migraine with aura.",
        "classification_and_neurology": "TIA is classified within the cerebrovascular disease spectrum under ischemic cerebrovascular events. The traditional definition required symptom resolution within 24 hours without infarction. The tissue-based definition, endorsed by the American Heart Association/American Stroke Association (AHA/ASA), defines TIA as transient neurological dysfunction without acute infarction on imaging. This shift recognizes that some transient symptoms may have infarcts visible on diffusion-weighted MRI, reclassifying them as minor strokes. The ABCD2 score is part of risk stratification classification systems for TIA, guiding prognosis and management. TIAs fall under the broader category of transient focal neurological episodes and are distinguished from stroke mimics and minor strokes. Nosologically, TIAs are grouped by etiology (large artery atherosclerosis, cardioembolism, small vessel disease, other determined or undetermined causes) using TOAST criteria. Current consensus emphasizes rapid assessment and treatment to prevent progression to ischemic stroke.",
        "classification_and_nosology": "TIAs are often classified based on the ABCD2 score\u2014a composite of Age, Blood Pressure, Clinical features, Duration of symptoms, and Diabetes. Patients with a higher score are considered high-risk for stroke.",
        "management_principles": "Current guidelines recommend dual antiplatelet therapy (DAPT), typically with aspirin plus clopidogrel, for high-risk TIA patients or those with minor strokes (usually for 21-90 days) to reduce the risk of subsequent stroke. After this short-term period, patients are generally transitioned to single antiplatelet therapy. In pregnant or lactating patients, low-dose aspirin is generally considered safe, but clopidogrel requires careful risk-benefit analysis due to limited data.",
        "option_analysis": "Option A (Aspirin alone) may offer some protection but is less effective than dual therapy in high-risk individuals. Option B (Clopidogrel alone) is not favored as monotherapy compared to the synergistic effect of dual therapy. Option C (Dual antiplatelet therapy) is correct as it has been shown to reduce early recurrent cerebrovascular events in patients with high-risk TIA, as supported by the CHANCE and POINT trials.",
        "clinical_pearls": "1. A high ABCD2 score in TIA patients indicates a significantly increased risk of stroke. 2. Dual antiplatelet therapy is recommended for a limited duration in high-risk TIA patients to reduce recurrence. 3. Early identification and intervention in TIA can significantly alter stroke outcomes.",
        "current_evidence": "Recent clinical trials (CHANCE, POINT) have demonstrated that short-term dual antiplatelet therapy significantly reduces the risk of recurrent stroke in patients with high-risk TIA or minor stroke. Current guidelines advocate using DAPT for a short duration (21-90 days) before transitioning to monotherapy to balance efficacy with bleeding risks."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993503",
    "fields": {
      "question_number": "33",
      "question_text": "45 YO female came with SAH and found to have P-chom aneurysm what's next",
      "options": {
        "A": "Endovascular coiling",
        "B": "Surgical clipping",
        "C": "Observation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Subarachnoid hemorrhage (SAH) secondary to a ruptured aneurysm is a neurological emergency. In this case, the aneurysm is located at the posterior communicating (P-com) segment, which is one of the common sites for berry aneurysms. The main management goal is to secure the aneurysm to prevent rebleeding.",
        "pathophysiology": "A saccular (berry) aneurysm develops at a weak point in the arterial wall. Its rupture releases blood into the subarachnoid space, triggering a cascade of events including raised intracranial pressure, vasospasm, and hydrocephalus. Evidence from trials such as ISAT (International Subarachnoid Aneurysm Trial) has helped shape management choices between endovascular and surgical approaches.",
        "clinical_correlation": "Patients typically present with a sudden 'thunderclap headache', loss of consciousness, or neurological deficits. A P-com aneurysm may also present with cranial nerve III palsy (ptosis and a 'down and out' eye) if it compresses the oculomotor nerve.",
        "diagnostic_approach": "Initial evaluation includes a non\u2010contrast CT scan to identify SAH. If the CT is equivocal, a lumbar puncture is indicated. Digital subtraction angiography (DSA) or CT angiography (CTA) is used to localize and characterize the aneurysm. Differential diagnoses include traumatic SAH, perimesencephalic hemorrhage, and non-aneurysmal causes of SAH.",
        "classification_and_neurology": "Ruptured intracranial aneurysms causing SAH fall under the broader category of cerebrovascular disorders and neurovascular emergencies. They are classified by location (anterior vs posterior circulation), morphology (saccular, fusiform), and rupture status (ruptured vs unruptured). The International Subarachnoid Aneurysm Trial (ISAT) and other consensus guidelines have helped refine classification and management approaches. The World Federation of Neurosurgical Societies (WFNS) grading system and Hunt and Hess scale classify SAH severity based on clinical presentation. This nosology aids in prognostication and treatment planning. Controversies remain regarding the best approach for certain aneurysm types and patient subgroups, but consensus favors early aneurysm securing in ruptured cases.",
        "classification_and_nosology": "Aneurysms are classified by location (anterior vs. posterior circulation), morphology (saccular, fusiform), and rupture status. P-com aneurysms belong to the anterior circulation and are one of the most frequent sites of aneurysmal SAH.",
        "management_principles": "According to current guidelines, once an aneurysm is identified in a ruptured SAH, it must be secured emergently. Endovascular coiling is often first line if the aneurysm\u2019s size and morphology are favorable. If endovascular treatment is unsuitable due to anatomical constraints or if there are other complicating factors, surgical clipping is considered. In pregnancy or lactation, the decision must weigh the risks of radiation (for coiling) against surgical risks. Multidisciplinary discussions involving neurosurgery, neurointerventionalists, and obstetrics are essential to customize management.",
        "option_analysis": "Option A (Endovascular coiling) is the correct next step because it is minimally invasive and supported by trials (ISAT) in appropriately selected patients. Option B (Surgical clipping) is an alternative when coiling is not feasible. Option C (Observation) is not acceptable given the high risk of rebleeding with unsecured aneurysms.",
        "clinical_pearls": "\u2022 Timely securing of a ruptured aneurysm greatly reduces the risk of fatal rebleeding. \u2022 Endovascular coiling is preferred in many centers for aneurysms with favorable anatomy. \u2022 Always assess for potential vasospasm in the days following SAH.",
        "current_evidence": "Recent updates and long\u2010term follow\u2010up from the ISAT study and other trials continue to support the use of endovascular coiling for aneurysms that are anatomically amenable, with a trend toward lower morbidity compared to clipping. Newer devices and techniques further expand the indications for endovascular treatment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993498",
    "fields": {
      "question_number": "36",
      "question_text": "What to expect from O.A. infarction",
      "options": {
        "A": "Ipsilateral Horner",
        "B": "Ipsilateral hearing loss"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Subarachnoid hemorrhage (SAH) secondary to a ruptured aneurysm is a neurological emergency. In this case, the aneurysm is located at the posterior communicating (P-com) segment, which is one of the common sites for berry aneurysms. The main management goal is to secure the aneurysm to prevent rebleeding.",
        "pathophysiology": "A saccular (berry) aneurysm develops at a weak point in the arterial wall. Its rupture releases blood into the subarachnoid space, triggering a cascade of events including raised intracranial pressure, vasospasm, and hydrocephalus. Evidence from trials such as ISAT (International Subarachnoid Aneurysm Trial) has helped shape management choices between endovascular and surgical approaches.",
        "clinical_correlation": "Patients typically present with a sudden 'thunderclap headache', loss of consciousness, or neurological deficits. A P-com aneurysm may also present with cranial nerve III palsy (ptosis and a 'down and out' eye) if it compresses the oculomotor nerve.",
        "diagnostic_approach": "Initial evaluation includes a non\u2010contrast CT scan to identify SAH. If the CT is equivocal, a lumbar puncture is indicated. Digital subtraction angiography (DSA) or CT angiography (CTA) is used to localize and characterize the aneurysm. Differential diagnoses include traumatic SAH, perimesencephalic hemorrhage, and non-aneurysmal causes of SAH.",
        "classification_and_neurology": "Ophthalmic artery infarction is classified under ischemic cerebrovascular diseases, specifically as part of anterior circulation strokes involving the internal carotid artery and its branches. It falls within the broader category of ocular ischemic syndromes and retinal artery occlusions. The American Heart Association/American Stroke Association (AHA/ASA) stroke classification systems categorize this as a large artery atherosclerosis or embolic stroke depending on etiology. The condition is distinct from posterior circulation strokes, which affect the brainstem and cerebellum, and from other ocular pathologies such as optic neuritis or glaucoma. Contemporary nosology emphasizes vascular territory-based classification to guide diagnosis and management. There is consensus on the importance of differentiating ophthalmic artery infarction from other causes of monocular vision loss due to its vascular implications and stroke risk.",
        "classification_and_nosology": "Aneurysms are classified by location (anterior vs. posterior circulation), morphology (saccular, fusiform), and rupture status. P-com aneurysms belong to the anterior circulation and are one of the most frequent sites of aneurysmal SAH.",
        "management_principles": "According to current guidelines, once an aneurysm is identified in a ruptured SAH, it must be secured emergently. Endovascular coiling is often first line if the aneurysm\u2019s size and morphology are favorable. If endovascular treatment is unsuitable due to anatomical constraints or if there are other complicating factors, surgical clipping is considered. In pregnancy or lactation, the decision must weigh the risks of radiation (for coiling) against surgical risks. Multidisciplinary discussions involving neurosurgery, neurointerventionalists, and obstetrics are essential to customize management.",
        "option_analysis": "Option A (Endovascular coiling) is the correct next step because it is minimally invasive and supported by trials (ISAT) in appropriately selected patients. Option B (Surgical clipping) is an alternative when coiling is not feasible. Option C (Observation) is not acceptable given the high risk of rebleeding with unsecured aneurysms.",
        "clinical_pearls": "\u2022 Timely securing of a ruptured aneurysm greatly reduces the risk of fatal rebleeding. \u2022 Endovascular coiling is preferred in many centers for aneurysms with favorable anatomy. \u2022 Always assess for potential vasospasm in the days following SAH.",
        "current_evidence": "Recent updates and long\u2010term follow\u2010up from the ISAT study and other trials continue to support the use of endovascular coiling for aneurysms that are anatomically amenable, with a trend toward lower morbidity compared to clipping. Newer devices and techniques further expand the indications for endovascular treatment."
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
