
# Import batch 1 of 3 from chunk_16_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993155",
    "fields": {
      "question_number": "92",
      "question_text": "Elderly had embolic stroke, what to do next:",
      "options": {
        "A": "is correct because initiating anticoagulation directly addresses the thromboembolic source, significantly reducing the risk of recurrent strokes. Options that suggest antiplatelet therapy alone or no treatment are inadequate in preventing further embolic events, as antiplatelets do not provide sufficient protection in cardioembolic stroke."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Embolic strokes, especially in the elderly, often arise from a cardioembolic source such as atrial fibrillation. Recognizing the stroke mechanism is crucial, as management strategies differ substantially from those for atherothrombotic strokes.",
        "pathophysiology": "In embolic strokes, a clot (often formed in the heart due to conditions like atrial fibrillation or from a cardiac thrombus) dislodges and travels to the cerebral circulation, causing sudden arterial occlusion and ischemia. This process typically leads to infarction in a vascular territory distant from the primary lesion.",
        "clinical_correlation": "Patients with cardioembolic strokes usually present with sudden-onset neurological deficits (e.g., hemiparesis, aphasia) that can be more severe compared to lacunar strokes. Identifying the embolic source is important, as recurrent embolic events are common without appropriate intervention.",
        "diagnostic_approach": "Workup includes brain imaging (CT or MRI), cardiac evaluation (ECG, Holter monitoring, echocardiography), and assessment of stroke risk factors. Differential diagnoses include atherothrombotic stroke, lacunar infarcts from small vessel disease, and hemorrhagic stroke. Cardiac investigations help confirm the embolic source.",
        "classification_and_neurology": "Embolic strokes are classified under ischemic strokes, specifically as cardioembolic or artery-to-artery embolic strokes. The TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system is widely used, categorizing ischemic stroke into large-artery atherosclerosis, cardioembolism, small-vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Cardioembolic strokes arise from cardiac sources such as atrial fibrillation, valvular disease, or intracardiac thrombi. Artery-to-artery embolism involves emboli from atherosclerotic plaques in large arteries like the carotid. The classification aids in tailoring secondary prevention strategies. Current consensus emphasizes thorough cardiac and vascular evaluation to accurately classify stroke subtype, as management differs significantly. Some controversy exists regarding optimal duration of cardiac monitoring for occult atrial fibrillation detection.",
        "classification_and_nosology": "Embolic strokes fall under the category of cardioembolic strokes, which is a distinct subtype of ischemic strokes. They are typically managed with anticoagulants rather than antiplatelet therapy.",
        "management_principles": "For secondary prevention of cardioembolic stroke, anticoagulation is the cornerstone of therapy. Options include warfarin and direct oral anticoagulants (DOACs), with DOACs increasingly preferred in non-valvular atrial fibrillation due to better safety profiles. In pregnancy, warfarin is contraindicated and low molecular weight heparin is preferred. For lactating mothers, warfarin is generally considered safe, but each case should be evaluated individually. The decision to start anticoagulation should follow confirmation of the embolic source to reduce recurrent stroke risk.",
        "option_analysis": "Option A is correct because initiating anticoagulation directly addresses the thromboembolic source, significantly reducing the risk of recurrent strokes. Options that suggest antiplatelet therapy alone or no treatment are inadequate in preventing further embolic events, as antiplatelets do not provide sufficient protection in cardioembolic stroke.",
        "clinical_pearls": "\u2022 Always evaluate for atrial fibrillation in patients with embolic stroke as it is a common and treatable source. \u2022 Anticoagulation reduces the risk of stroke recurrence by approximately 60-70% in cardioembolic stroke. \u2022 DOACs have largely supplanted warfarin in nonvalvular atrial fibrillation due to their favorable safety profile.",
        "current_evidence": "Recent guidelines from the American Heart Association and European Stroke Organization support the use of anticoagulation for secondary prevention in cardioembolic strokes, with a growing body of evidence favoring DOACs over warfarin in appropriate patients. Ongoing research continues to optimize treatment strategies in various patient populations, including considerations for pregnancy and lactation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993156",
    "fields": {
      "question_number": "93",
      "question_text": "Cadasil scenario of pt tried stroke dementia migraine what to giv pat foe prophlaxis ??",
      "options": {
        "A": "smoking cessation",
        "B": "anti-goagulant (warfarin)",
        "C": "!ASA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy) is a hereditary small vessel disease of the brain characterized by migraine (often with aura), recurrent subcortical strokes, and progressive cognitive decline leading to dementia. Its management is predominantly supportive, with emphasis on controlling modifiable vascular risk factors.",
        "pathophysiology": "Mutations in the NOTCH3 gene impair the function of vascular smooth muscle cells, leading to degeneration and thickening of the vessel wall. This results in chronic ischemia, white matter changes, lacunar infarcts, and ultimately, the clinical manifestations of migraine, strokes, and dementia. There is no disease\u2010modifying therapy currently available.",
        "clinical_correlation": "Patients typically present with migraine (often with aura), followed by recurrent ischemic strokes and a progressive decline in cognitive function. The history of migraine, stroke, and subsequent vascular dementia in a relatively young patient may suggest CADASIL.",
        "diagnostic_approach": "Initial evaluation includes a detailed clinical history and brain MRI (which typically shows confluent white matter hyperintensities especially in the anterior temporal lobes). Confirmation is achieved via genetic testing for NOTCH3 mutations. Differential diagnoses include other causes of vascular dementia, multiple sclerosis, and other hereditary leukoencephalopathies.",
        "classification_and_neurology": "CADASIL is classified as a hereditary cerebral small vessel disease (CSVD), specifically an autosomal dominant arteriopathy due to NOTCH3 mutations. It belongs to the broader family of genetic vasculopathies causing stroke and dementia. The classification of CSVD includes sporadic forms related to hypertension and aging, and hereditary forms like CADASIL, CARASIL, and others. CADASIL is the most common monogenic cause of CSVD and is distinct in its genetic etiology and clinical features. Nosologically, it is categorized under hereditary small vessel diseases causing ischemic strokes and leukoencephalopathy. The classification has evolved with advances in molecular genetics, enabling precise diagnosis and differentiation from sporadic CSVD and other inherited leukoencephalopathies. Current consensus recognizes CADASIL as a prototype of genetic CSVD with well-defined clinical and radiological criteria.",
        "classification_and_nosology": "CADASIL is classified as a hereditary cerebral small vessel disease. It belongs to the group of arteriopathies affecting small vessels and is an important cause of subcortical ischemic events in younger individuals with a family history of similar events.",
        "management_principles": "There is no curative treatment for CADASIL. Management is centered on controlling modifiable vascular risk factors. First\u2010line recommendations include lifestyle modifications (most importantly, smoking cessation) and blood pressure control. Antiplatelet agents (such as ASA) are sometimes used for secondary stroke prevention, but the evidence in CADASIL is not robust. Anticoagulation is generally avoided due to a higher risk of hemorrhage. In pregnant or lactating patients, careful risk\u2013benefit evaluation of any pharmacotherapy is mandatory, with an emphasis on non\u2010pharmacological risk factor modification.",
        "option_analysis": "Option A (smoking cessation) is correct because eliminating a modifiable risk factor is paramount in slowing the progression of vascular damage in CADASIL. Option B (anticoagulant/warfarin) is contraindicated as it increases hemorrhagic risks in small vessel arteriopathy. Option C (ASA) is not the first choice given the lack of proven benefit in CADASIL prophylaxis and potential bleeding risks, thus making risk factor modification (i.e. smoking cessation) the preferred approach.",
        "clinical_pearls": "1. CADASIL is a genetic small vessel disease with no specific disease\u2010modifying treatment \u2013 management relies on controlling risk factors. 2. Smoking cessation is critical as smoking exacerbates vascular injury. 3. MRI with anterior temporal lobe involvement is a key radiologic clue to CADASIL.",
        "current_evidence": "Recent reviews and consensus guidelines emphasize that in genetically mediated small vessel diseases like CADASIL, the most effective strategy is strict risk factor modification rather than relying on antithrombotic therapy. Ongoing research continues to explore potential targeted therapies, but none are currently validated for routine clinical practice."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993157",
    "fields": {
      "question_number": "94",
      "question_text": "Same above Q what Rx:",
      "options": {
        "A": "Anticoaglation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question revisits the management approach in CADASIL, where the clinical picture includes migraine, stroke, and cognitive decline. With CADASIL being a non-inflammatory, non-atherosclerotic arteriopathy, the management goal is to reduce additional vascular injury.",
        "pathophysiology": "The underlying NOTCH3 mutation leads to vascular smooth muscle dysfunction which causes progressive damage to the small cerebral vessels. This structural abnormality predisposes patients to ischemic events and white matter lesions.",
        "clinical_correlation": "Due to the recurring strokes and associated migraine attacks, patients with CADASIL are prone to worsening disability. Prevention of further vascular damage through modification of risk factors is essential since no disease-specific pharmacological treatment exists.",
        "diagnostic_approach": "Diagnosis is based on clinical findings (migraine with aura, subcortical strokes, and early dementia) along with radiologic evidence on MRI and confirmed by genetic testing. Differential diagnoses include sporadic ischemic stroke and other hereditary leukoencephalopathies.",
        "classification_and_neurology": "Ischemic strokes are classified etiologically using systems like TOAST, which categorizes strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunes), other determined etiology, and undetermined etiology. Anticoagulation is primarily indicated in cardioembolic strokes and certain hypercoagulable states. This classification guides management strategies, as antiplatelet agents are preferred in large artery atherosclerosis without cardioembolism, whereas anticoagulants are first-line in cardioembolic sources. The classification has evolved to incorporate imaging and cardiac evaluation findings, refining therapeutic decisions.",
        "classification_and_nosology": "CADASIL is categorized under hereditary cerebral small vessel diseases. It is an autosomal dominant disorder that primarily affects the brain's microvasculature.",
        "management_principles": "Since there is no curative treatment, the first-line management involves rigorous modification of vascular risk factors. The cornerstone of treatment is lifestyle modification, with smoking cessation being the most critical. Although antiplatelets like ASA are sometimes used, their role is not clearly established in CADASIL, and anticoagulation is generally contraindicated. Management in pregnancy and lactation similarly emphasizes non-pharmacologic interventions to avoid harm to the fetus or neonate.",
        "option_analysis": "Option A (smoking cessation) is the correct answer as it directly addresses modifiable risk factors to slow disease progression. Option A is consistent with the principles of CADASIL management. The marked answer was C, but given the context from the previous similar question, risk factor modification (specifically smoking cessation) remains the best intervention. The other options (if contemplating anticoagulation or other pharmacologic interventions) do not have evidence to support their use in the prophylaxis of further vascular events in CADASIL.",
        "clinical_pearls": "1. Risk factor modification is the only proven strategy to potentially slow the progression of CADASIL-related vascular damage. 2. Smoking is particularly detrimental in CADASIL. 3. Traditional thrombolytic or anticoagulant therapies have not proven beneficial in this disorder.",
        "current_evidence": "The latest research continues to support that in CADASIL, aggressive control of modifiable risk factors \u2013 particularly smoking cessation \u2013 is central to management. No randomized clinical trials favor pharmacologic prophylaxis like anticoagulation in this setting, and current guidelines reflect an emphasis on lifestyle management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993158",
    "fields": {
      "question_number": "95",
      "question_text": "Scenario about old age man around 80 y.o k/c of DM, HTN, stroke 2 months back Came with stroke in windo .. (Ct attached showed good aspect and old cortical insult) what TO DO NEXT ?",
      "options": {
        "A": "IV tpA",
        "B": "IV tpA followed by thrombectomy"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke management, the decision to administer reperfusion therapies such as intravenous tissue plasminogen activator (IV tPA) is based on strict eligibility criteria. A history of a recent stroke is a well-recognized contraindication to thrombolysis.",
        "pathophysiology": "IV tPA works by dissolving clots; however, in brain tissue that has already sustained recent ischemic injury, the blood\u2013brain barrier is compromised. Administering tPA under these circumstances significantly increases the risk of hemorrhagic transformation, where damaged vessels are prone to bleeding.",
        "clinical_correlation": "In the case presented, an 80-year-old man with a stroke history 2 months prior is now having a new stroke within the therapeutic window. Despite a CT scan showing no acute hemorrhage and evidence of an old cortical insult, the recent stroke is a major red flag, making reperfusion therapy (tPA or tPA plus thrombectomy) a dangerous option.",
        "diagnostic_approach": "Evaluation includes confirming the stroke timing, reviewing the patient\u2019s history for contraindications (like stroke within the past 3 months), and neuroimaging (CT, MRI) to assess for hemorrhage or infarct evolution. Differential diagnoses such as transient ischemic attack (TIA) and hemorrhagic stroke must be considered and appropriately excluded.",
        "classification_and_neurology": "AIS is classified under cerebrovascular diseases per the WHO and AHA/ASA stroke classification systems. Subtypes include large artery atherosclerosis, cardioembolism, small vessel occlusion, and others. The current clinical classification relevant here is based on time from symptom onset (acute window), imaging features, and eligibility for reperfusion therapies. The concept of 'time windows' for intravenous thrombolysis (generally up to 4.5 hours) and mechanical thrombectomy (up to 24 hours in select cases) is central. The presence of a recent stroke (within 3 months) is considered a relative or absolute contraindication to thrombolysis in many guidelines, reflecting the increased hemorrhagic risk. Nosological evolution has shifted from purely time-based to tissue-based approaches using advanced imaging, but recent stroke remains a key exclusion criterion in most protocols.",
        "classification_and_nosology": "This scenario falls under acute ischemic stroke management. There are important subcategories: patients eligible for IV thrombolysis/transcatheter thrombectomy and those who are not, based on contraindications including recent stroke.",
        "management_principles": "First-line treatment for eligible acute ischemic stroke patients is IV tPA administered within the appropriate window, potentially followed by thrombectomy if large vessel occlusion is identified. However, in patients with a recent stroke (within the last 3 months), reperfusion therapies are contraindicated due to the heightened risk of bleeding. In such situations, management shifts to supportive care and secondary prevention strategies. In pregnant or lactating patients, the use of tPA involves careful consideration of maternal and fetal risks, with current guidelines generally advising against thrombolysis if contraindications are present.",
        "option_analysis": "Option A (IV tPA) and Option B (IV tPA followed by thrombectomy) are incorrect because recent stroke (< 3 months) is a contraindication to tPA administration. The marked answer, Option C, though not textually described, is interpreted to mean that thrombolytic therapy should be withheld in this situation, making it the correct choice.",
        "clinical_pearls": "1. A stroke within the past 3 months is a contraindication to tPA due to increased hemorrhagic risk. 2. Always review the patient's recent medical history before considering reperfusion therapies. 3. Advanced age alone is not a contraindication, but accompanying recent stroke is critical.",
        "current_evidence": "Recent guidelines and updated stroke management protocols underscore that a recent stroke (typically within 3 months) is a contraindication for IV tPA due to the risk of hemorrhagic transformation. Ongoing studies and clinical audits consistently support excluding patients with recent strokes from reperfusion therapies, even if they present within the otherwise acceptable time window."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993159",
    "fields": {
      "question_number": "96",
      "question_text": "Why tpa contraindicated in previous Q",
      "options": {
        "A": "stroke less than 3mo (Relative contraindication)",
        "B": "Or The presence of exclusion criteria",
        "C": "pt can be benefit of thrombectomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Thrombolytic therapy with tPA is indicated in acute ischemic stroke provided that patients meet strict eligibility criteria. One key contraindication is a recent ischemic event, as the risk of hemorrhagic conversion is significantly increased in recently infarcted brain tissue.",
        "pathophysiology": "After an ischemic stroke, the blood\u2013brain barrier is disrupted. Administering tPA in this vulnerable period (usually within 3 months of a previous stroke) can precipitate bleeding into the damaged brain tissue, leading to hemorrhagic transformation and worse clinical outcomes.",
        "clinical_correlation": "In the scenario, the patient had a stroke just 2 months ago and is now presenting with a new ischemic event. This recent history significantly raises the risk of hemorrhagic complications if tPA is administered. Recognizing and adhering to this contraindication is crucial for patient safety.",
        "diagnostic_approach": "A thorough history is vital to determine the timing of previous strokes. Neuroimaging (CT/MRI) is used to rule out current hemorrhage and to assess brain tissue status. The differential diagnosis may include a new ischemic event versus a hemorrhagic transformation of the previous stroke, making accurate history-taking essential.",
        "classification_and_neurology": "Intravenous thrombolytic therapy falls under acute ischemic stroke management in cerebrovascular disease classification. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify contraindications into absolute and relative categories based on risk-benefit analyses. Recent stroke within 3 months is a classic relative contraindication, reflecting a nuanced understanding of hemorrhagic risk. This classification system has evolved with accumulating evidence, balancing the urgency of reperfusion against safety concerns. Alternative reperfusion strategies such as mechanical thrombectomy represent adjunct or alternative treatments, especially in large vessel occlusions.",
        "classification_and_nosology": "This contraindication is categorized under tPA eligibility criteria in acute ischemic stroke protocols. Patients are routinely evaluated based on time since last stroke, current neurological status, and imaging findings.",
        "management_principles": "The standard management principles dictate that in patients with a stroke within the past 3 months, tPA should be withheld. Management then focuses on secondary prevention of stroke, optimization of vascular risk factors, and supportive care. In pregnant or lactating patients, the risk\u2013benefit analysis is even more complex, and conservative management is favored in the presence of contraindications.",
        "option_analysis": "Option A states that a stroke less than 3 months ago is a (relative) contraindication for tPA, which is correct. Option B is vague with reference to exclusion criteria, and Option C (suggesting thrombectomy benefit) is misleading because the contraindication applies primarily to tPA usage. Therefore, Option A is the best answer.",
        "clinical_pearls": "1. Always confirm the time interval since the last stroke; a stroke within 3 months significantly increases tPA-associated hemorrhagic risk. 2. A thorough medical history is paramount in acute stroke management. 3. Thrombolytic therapy contraindications are strictly adhered to in order to minimize risks.",
        "current_evidence": "The most recent stroke management guidelines (including those from the American Heart Association/American Stroke Association) explicitly list recent stroke (within 3 months) as a contraindication for IV tPA. Recent literature continues to validate this exclusion due to the elevated risk of bleeding, and research is ongoing to better stratify risk in these patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993160",
    "fields": {
      "question_number": "97",
      "question_text": "Pt 64 dm came with weakness lasted 25 min then resolved (tia case); asked about meds to start?",
      "options": {
        "A": "Loading plavix+ then regular ASA + Plavix",
        "B": "ASA only, ..."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "A transient ischemic attack (TIA) is defined as a brief episode of neurological dysfunction caused by focal brain, spinal cord, or retinal ischemia without acute infarction. It is a warning sign for an impending stroke and requires prompt evaluation and secondary prevention.",
        "pathophysiology": "TIA is most commonly due to embolic or thrombotic events in a cerebral artery that transiently compromise cerebral blood flow. In patients with diabetes mellitus and other vascular risk factors, small vessel atherosclerosis and embolic phenomena often play a role. The transient occlusion leads to reversible neurological deficits when reperfusion occurs.",
        "clinical_correlation": "In this case, a 64\u2010year\u2010old diabetic patient experienced weakness lasting 25 minutes. This classic presentation of a TIA indicates a temporary reduction in blood flow. Recognizing TIA is crucial because of the high subsequent stroke risk.",
        "diagnostic_approach": "Diagnosis is primarily clinical with supportive imaging. A non-contrast CT scan is used to rule out hemorrhage or completed infarction, while MRI (especially with diffusion-weighted imaging) is more sensitive in detecting acute ischemia. Differential diagnoses include seizure with postictal paresis, migraine aura, or hypoglycemic events.",
        "classification_and_neurology": "TIA is classified under cerebrovascular diseases in the ICD-11 and the American Heart Association/American Stroke Association (AHA/ASA) stroke classification. It is differentiated from ischemic stroke by the absence of infarction on imaging and symptom duration less than 24 hours, though recent definitions emphasize tissue-based criteria over time-based. TIAs are further categorized by etiology according to the TOAST classification (Trial of Org 10172 in Acute Stroke Treatment), including large artery atherosclerosis, cardioembolism, small vessel disease, other determined etiology, and undetermined etiology. This nosology informs prognosis and management. The evolving consensus now prioritizes MRI confirmation and stratification by risk scores such as ABCD2 to guide therapy intensity.",
        "classification_and_nosology": "TIAs are classified as non-disabling ischemic events and risk stratification is often performed using scoring systems such as ABCD2. A high score indicates an increased 90-day risk of stroke.",
        "management_principles": "According to current guidelines, for patients with a TIA who are at high risk for stroke (often with an ABCD2 score \u22654), dual antiplatelet therapy (DAPT) using aspirin plus clopidogrel is recommended for the short term (typically 21\u201390 days) to reduce recurrent stroke risk. After this period, therapy is usually de-escalated to single antiplatelet therapy. In pregnant or lactating women (if encountered), low-dose aspirin is generally considered acceptable, although clopidogrel is used with caution and only if the benefits outweigh potential risks.",
        "option_analysis": "Option A (loading with clopidogrel followed by regular aspirin plus clopidogrel) is correct because numerous studies (such as the CHANCE and POINT trials) have shown that early initiation of DAPT in high-risk TIA/minor stroke patients reduces the risk of subsequent stroke. Options that suggest only aspirin monotherapy or no antiplatelet treatment would not address the high risk of recurrence adequately.",
        "clinical_pearls": "1. TIA is a crucial warning sign for stroke, and early intervention can significantly reduce the risk of stroke. 2. In high-risk TIA patients, DAPT should be initiated within 24 hours. 3. Always address modifiable vascular risk factors alongside antiplatelet therapy.",
        "current_evidence": "Recent trials (CHANCE, POINT) support the use of DAPT in reducing the risk of stroke after a TIA, particularly in the first 21 to 90 days. Guidelines stress the importance of rapid intervention and risk factor modification."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993161",
    "fields": {
      "question_number": "98",
      "question_text": "around 65 y.o male DM, HTN Bp=150/70 present to ER with hx of left side weakness last for 18 mints then improved .. ? 90 day risk of stroke",
      "options": {
        "A": "Low",
        "B": "modrate",
        "C": "High"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Risk stratification after a TIA is commonly done using the ABCD2 score, which estimates the risk of subsequent stroke within 90 days based on factors such as Age, Blood pressure, Clinical features, Duration of symptoms, and Diabetes.",
        "pathophysiology": "The underlying mechanism involves temporary blockage of a cerebral artery leading to transient symptoms. In patients with multiple risk factors (such as diabetes, hypertension, and significant symptomatology like unilateral weakness), the likelihood of an unstable vascular pathology and subsequent stroke is high.",
        "clinical_correlation": "A 65-year-old male with diabetes and hypertension who experienced 18 minutes of left-side weakness would accumulate a high ABCD2 score (Age \u226560 = 1, blood pressure \u2265140 systolic = 1, unilateral weakness = 2, duration >10 minutes = 1, plus diabetes = 1; total = 6). A score of 6 correlates with a high risk of stroke in the next 90 days.",
        "diagnostic_approach": "Risk assessment in TIA patients involves a detailed history and physical examination combined with imaging studies (CT/MRI) to rule out infarction. Differential diagnoses include transient seizures or syncope. The scoring system (ABCD2) helps differentiate patients at low versus high risk.",
        "classification_and_neurology": "TIA falls within the spectrum of ischemic cerebrovascular diseases and is classified as a transient episode of neurological dysfunction without infarction. The traditional time-based definition (<24 hours) has been supplanted by tissue-based definitions emphasizing the absence of infarction on diffusion-weighted MRI. Stroke classification systems such as the TOAST criteria categorize ischemic strokes by etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. TIAs are considered prodromal events in this framework. Risk stratification tools like the ABCD2 score classify TIA patients into low, moderate, or high risk for stroke based on Age, Blood pressure, Clinical features, Duration of symptoms, and Diabetes presence. This question relates directly to such classification systems guiding prognosis and management. There is consensus that TIAs require urgent evaluation due to their high risk of progression to stroke, especially in patients with vascular risk factors.",
        "classification_and_nosology": "TIAs are categorized based on risk into low, moderate, or high, using scoring systems such as ABCD2. A score of 4 or more is generally considered high risk.",
        "management_principles": "High-risk TIA patients should be managed urgently with dual antiplatelet therapy along with aggressive control of vascular risk factors. Hospitalization for further work-up, including vascular imaging, may be indicated. While not directly affecting this older male patient, in pregnant or lactating patients, low-dose aspirin is acceptable and other agents are used with caution.",
        "option_analysis": "Option C, which labels the 90-day stroke risk as 'High', is correct given the patient's risk factors and ABCD2 score of 6. Options indicating low or moderate risk would underestimate the potential for recurrent stroke.",
        "clinical_pearls": "1. An ABCD2 score of 4 or greater indicates high risk for a subsequent stroke. 2. Unilateral weakness gives 2 points and is a strong predictor of stroke risk. 3. Early intervention in high-risk TIA patients is critical to prevent a full-blown stroke.",
        "current_evidence": "Guidelines consistently recommend rapid evaluation and initiation of DAPT in high-risk TIA patients to reduce the chance of subsequent stroke. Recent studies validate the use of ABCD2 in prognostication."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993162",
    "fields": {
      "question_number": "99",
      "question_text": "young Male patient with 3rd nerve palsy pic attached of Pcom aneurism :",
      "options": {},
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Third nerve (oculomotor nerve) palsy can be caused by various etiologies. A key clinical differentiation is whether the pupil is involved because compressive lesions (like aneurysms) typically affect the pupillary fibers.",
        "pathophysiology": "The oculomotor nerve has superficially located parasympathetic fibers that control pupillary constriction. A posterior communicating (PCom) artery aneurysm can compress these fibers, leading to pupil dilation and dysfunction, distinguishing it from ischemic (microvascular) causes that usually spare the pupil.",
        "clinical_correlation": "In a young patient presenting with a third nerve palsy that includes pupil involvement, the clinical suspicion for a PCom aneurysm is high, making it a neurosurgical emergency due to the risk of rupture and subarachnoid hemorrhage.",
        "diagnostic_approach": "Diagnosis involves neuroimaging with CT angiography or MR angiography to identify the aneurysm. Differential diagnoses include diabetic microvascular third nerve palsy (which typically spares the pupil), midbrain infarct, cavernous sinus syndrome, and myasthenia gravis.",
        "classification_and_neurology": "Third nerve palsies are classified based on etiology (vascular, compressive, traumatic, inflammatory), pupil involvement (pupil-sparing vs. pupil-involving), and anatomical location (nuclear, fascicular, subarachnoid, cavernous sinus, orbital). Pcom aneurysm-induced third nerve palsy falls under compressive vascular cranial neuropathies. The International Classification of Headache Disorders and neuro-ophthalmological taxonomies emphasize the importance of pupil involvement in classification. This classification aids in differentiating aneurysmal compression from microvascular ischemic palsies, which is crucial for management decisions.",
        "classification_and_nosology": "Third nerve palsy is classified based on the etiology: compressive (aneurysmal, neoplastic) versus ischemic (microvascular). PCom aneurysm falls into the compressive category.",
        "management_principles": "Immediate neurosurgical referral is required. Management options include endovascular coiling or surgical clipping of the aneurysm. In pregnancy, management becomes more complex, necessitating a balance between maternal and fetal risks, and generally requires a multidisciplinary team including neurosurgery, obstetrics, and anesthesia.",
        "option_analysis": "Although the options are not explicitly listed, the key concept is that in the setting of a pupil-involving third nerve palsy, a PCom aneurysm is the most likely and critical diagnosis. Alternative choices such as diabetic neuropathy (which spares the pupil), midbrain infarct (which has additional signs), cavernous sinus syndrome, or myasthenia gravis would be incorrect.",
        "clinical_pearls": "1. Pupil involvement in third nerve palsy points to a compressive etiology. 2. A PCom aneurysm is a neurosurgical emergency. 3. Diabetic third nerve palsy rarely involves the pupil.",
        "current_evidence": "Recent neuroimaging advances have improved early detection of aneurysms. Updated guidelines stress the urgency of neurosurgical evaluation for pupil-involving third nerve palsies to prevent catastrophic hemorrhage."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_4.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993216",
    "fields": {
      "question_number": "194",
      "question_text": "Elderly female patient wakes up with abnormal left arm and leg involuntary movements, before she slept she had no complains, presented to the ER, CT brain was normal, MRI stroke protocol done, later the involuntary movement improved. Where do you expect to the abnormality in the MRI?",
      "options": {
        "A": "Midbrain",
        "B": "Sub-thalamic",
        "C": "Pons",
        "D": "Medulla"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Hemiballismus is a rare movement disorder characterized by violent, involuntary flinging movements of the limbs, typically due to a lesion in the subthalamic nucleus.",
        "pathophysiology": "The subthalamic nucleus plays a key role in modulating motor activity through the basal ganglia circuit. Lesions, most commonly lacunar infarcts due to small vessel disease, disrupt this modulation, resulting in disinhibited, excessive motor output on the contralateral side.",
        "clinical_correlation": "An elderly female presenting with sudden abnormal, involuntary movements in the left arm and leg is highly suggestive of a lacunar stroke affecting the right subthalamic nucleus, which produces contralateral hemiballismus. The normal CT initially followed by an abnormal MRI stroke protocol is typical, as small deep infarcts may not be evident on CT.",
        "diagnostic_approach": "Diagnosis relies on clinical findings of hemiballismus combined with imaging. MRI is more sensitive than CT for detecting small lacunar infarcts. Differential diagnoses include other movement disorders such as chorea (often seen in metabolic or neurodegenerative conditions) or seizures.",
        "classification_and_neurology": "Hemichorea and hemiballismus are classified as hyperkinetic movement disorders within the broader category of basal ganglia syndromes. Stroke-induced hemichorea is categorized under vascular movement disorders, a subset of secondary movement disorders caused by cerebrovascular insults. The classification aligns with the Movement Disorder Society's nosology, which distinguishes primary (idiopathic/genetic) from secondary (structural/metabolic/toxic) chorea. Vascular hemichorea often arises from lacunar infarcts affecting subcortical motor pathways, particularly the STN. This contrasts with other hyperkinetic disorders such as Huntington's disease, which involve diffuse basal ganglia degeneration. The classification has evolved with improved imaging and understanding of basal ganglia circuits, emphasizing lesion localization and etiology.",
        "classification_and_nosology": "Hemiballismus is classified as a hyperkinetic movement disorder, usually arising from vascular lesions in the subthalamic nucleus. It is a subtype of basal ganglia stroke syndromes.",
        "management_principles": "Management focuses on addressing the underlying stroke with antithrombotic therapy and aggressive control of vascular risk factors. Symptomatic treatment for hemiballismus may involve dopamine-depleting agents or neuroleptics if the movements are severe. In patients who are pregnant or lactating, careful selection of medications is essential; many antipsychotics require risk\u2013benefit analysis and close monitoring.",
        "option_analysis": "Option B (Sub-thalamic) is correct. Lesions in other locations \u2013 midbrain, pons, and medulla \u2013 are not typically associated with hemiballismus. The subthalamic nucleus is the classic site for lacunar infarcts causing this condition.",
        "clinical_pearls": "1. Lacunar infarcts in the subthalamic nucleus can cause contralateral hemiballismus. 2. CT scans may be normal early in the stroke, making MRI the investigation of choice. 3. Rapid recognition is important to initiate appropriate vascular risk management.",
        "current_evidence": "Recent advances in MRI technology have improved the detection of small, deep infarcts. Current guidelines emphasize aggressive vascular risk factor management and appropriate antithrombotic therapy in patients with lacunar strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993217",
    "fields": {
      "question_number": "195",
      "question_text": "What is the diagnosis:\n- Cerebral vasculitis\n- CVT",
      "options": {
        "A": "Cerebral vasculitis",
        "B": "CVT"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Cerebral Venous Thrombosis (CVT) is a condition where a clot forms in the brain\u2019s venous sinuses, leading to impaired venous drainage. This contrasts with cerebral vasculitis, which involves an inflammatory destruction of the vessel wall primarily affecting smaller arteries. The clinical distinction is crucial because the management, prognosis, and underlying risk factors differ between these two entities.",
        "pathophysiology": "In CVT, thrombus formation within the cerebral veins or dural sinuses causes increased venous pressure, resulting in cerebral edema, venous infarction, and potentially hemorrhagic transformation due to disruption of the blood\u2013brain barrier. In contrast, cerebral vasculitis involves immune-mediated inflammatory damage to blood vessel walls, which can lead to multiple areas of infarction. CVT is often associated with conditions that promote a hypercoagulable state such as pregnancy, oral contraceptive use, infection, or inherited thrombophilia.",
        "clinical_correlation": "Patients with CVT typically present with headache (often the most common symptom), seizures, focal neurological deficits, and signs of increased intracranial pressure (e.g., papilledema). A presentation with acute neurological deficits in a setting that suggests a clotting disorder is more consistent with CVT rather than an insidious inflammatory process as seen in cerebral vasculitis.",
        "diagnostic_approach": "The gold standard for diagnosing CVT is magnetic resonance imaging (MRI) combined with magnetic resonance venography (MRV) or computed tomography venography (CTV). These imaging modalities can reveal the absence of flow in the affected venous sinuses. In contrast, diagnosing cerebral vasculitis may require vessel wall imaging, laboratory markers of inflammation, and sometimes brain biopsy. Differential diagnoses include intracranial hemorrhage, arterial ischemic stroke, and other causes of headache and focal deficits.",
        "classification_and_neurology": "Cerebral vasculitis falls under the broader category of central nervous system vasculitides, which can be primary (PACNS) or secondary to systemic inflammatory diseases. The Chapel Hill Consensus Conference (2012) provides widely accepted definitions of vasculitis types, emphasizing vessel size and etiology. PACNS is classified as a small- to medium-vessel vasculitis confined to the CNS.  CVT is classified within cerebrovascular diseases, specifically under venous stroke syndromes. The International Classification of Headache Disorders (ICHD-3) also recognizes CVT-related headache as a secondary headache disorder.  While both conditions involve cerebral vessels, cerebral vasculitis primarily affects arteries and arterioles through inflammatory mechanisms, whereas CVT involves thrombosis of venous structures. This fundamental difference guides classification and management. There is consensus on these distinctions, although diagnostic overlap can occur, especially when vasculitis leads to secondary thrombosis.",
        "classification_and_nosology": "CVT is broadly classified based on the anatomical location of the thrombosis (e.g., superior sagittal sinus, transverse sinus) and whether the risk factor is acquired (e.g., pregnancy, infection) or inherited (e.g., factor V Leiden mutation). Cerebral vasculitis can be primary (confined to the CNS) or secondary to systemic autoimmune disorders.",
        "management_principles": "The first-line treatment for CVT is immediate anticoagulation, typically with low molecular weight heparin (LMWH) or unfractionated heparin, even in the presence of small hemorrhagic infarcts. This is followed by a transition to oral anticoagulants for several months based on individual risk. For pregnant patients, LMWH is preferred due to its safety profile. Second-line treatments may include endovascular thrombolysis in refractory cases. In contrast, management of cerebral vasculitis involves high-dose corticosteroids and often immunosuppressive agents.",
        "option_analysis": "Option A (Cerebral vasculitis) is incorrect because the clinical and imaging features (as implied in the context) lean more towards a thrombotic process than an inflammatory one. Option B (CVT) is the correct diagnosis given the typical presentation and factors associated with venous thrombosis.",
        "clinical_pearls": "1. CVT often presents with a new-onset headache and neurological deficits in a patient with a hypercoagulable state. 2. MRI with MR venography is the diagnostic study of choice. 3. Early anticoagulation is critical, even if there is evidence of hemorrhagic conversion.",
        "current_evidence": "Recent guidelines from organizations such as the American Heart Association endorse early anticoagulation for CVT and suggest that newer direct oral anticoagulants may have a role in long-term management, though more research is ongoing. The emphasis remains on rapid diagnosis with advanced imaging techniques."
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
