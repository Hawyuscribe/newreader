
# Import batch 1 of 3 from chunk_6_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993104",
    "fields": {
      "question_number": "79",
      "question_text": "ICH case, target bp?",
      "options": {
        "A": "140/90",
        "B": "160/90"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In intracerebral hemorrhage (ICH), blood pressure management is critical since elevated blood pressure can contribute to hematoma expansion. The goal is to safely reduce blood pressure to minimize further bleeding while maintaining adequate cerebral perfusion.",
        "pathophysiology": "High blood pressure exerts force on the already compromised vessel walls in ICH, potentially worsening the hemorrhage. Controlling the blood pressure reduces the transmural pressure gradient across the vessel wall, thereby limiting hematoma growth.",
        "clinical_correlation": "Patients with ICH often present acutely with focal neurological deficits and altered consciousness. Elevated blood pressure in these patients is common as a physiologic response, but unchecked it may lead to worsening outcomes due to hematoma expansion.",
        "diagnostic_approach": "CT scanning is the gold standard for identifying and characterizing ICH. Additional vascular imaging may be done to rule out underlying vascular anomalies. Differential diagnoses include ischemic stroke with hemorrhagic transformation and other mimics such as tumors or cerebral amyloid angiopathy.",
        "classification_and_neurology": "ICH is classified under hemorrhagic stroke within the broader cerebrovascular disease category. The American Heart Association/American Stroke Association (AHA/ASA) classifies ICH based on location (lobar, deep, brainstem, cerebellar), etiology (hypertensive, amyloid angiopathy, anticoagulant-related), and volume. BP management in ICH falls under acute stroke care protocols. The classification of BP management strategies has evolved with accumulating evidence from randomized controlled trials, leading to consensus guidelines that define specific BP thresholds for intervention. Controversies have existed regarding how aggressively to lower BP, but current nosology emphasizes individualized targets within recommended ranges to balance risks and benefits.",
        "classification_and_nosology": "ICH is classified by location (lobar, deep, cerebellar, brainstem) and etiology (hypertensive, amyloid, arteriovenous malformations, etc.). Management strategies are guided by the size, location, and patient\u2019s clinical status.",
        "management_principles": "According to current guidelines (e.g., AHA/ASA), in patients with ICH who present with systolic blood pressures between 150-220 mm Hg, it is recommended to lower the systolic blood pressure to around 140 mm Hg. This approach minimizes hematoma expansion while avoiding the risk of cerebral hypoperfusion. In pregnant or lactating patients, careful selection of antihypertensive medications (such as labetalol or hydralazine) with proven safety profiles is important.",
        "option_analysis": "Option A (140/90) corresponds to the common target of reducing the systolic pressure to about 140 mm Hg, which is in line with guideline recommendations. Option B (160/90) would be considered less aggressive and may not optimally prevent hematoma expansion. The other options are either missing or not applicable.",
        "clinical_pearls": "1) The INTERACT2 trial supports lowering systolic blood pressure to 140 mm Hg in ICH. 2) Avoid overly aggressive lowering to prevent cerebral hypoperfusion. 3) Early blood pressure management is crucial to limit hematoma growth.",
        "current_evidence": "Recent trials such as INTERACT2 and ATACH-II have provided substantial evidence supporting the safe reduction of systolic BP to 140 mm Hg in ICH patients, and these findings are reflected in the most recent AHA/ASA guidelines."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993105",
    "fields": {
      "question_number": "80",
      "question_text": "Case scenario of a patient who came with 1 day history of ischemic stroke, high bp SBP 190, CT brain reported established stroke next?",
      "options": {
        "A": "Keep bp the same"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In the management of acute ischemic stroke, permissive hypertension is generally allowed in order to maintain cerebral perfusion in the ischemic penumbra. This is especially true when the patient is outside the thrombolytic window, as is the case here with an established infarct on CT.",
        "pathophysiology": "In acute ischemic stroke, the body often compensates with elevated blood pressure to improve perfusion to the ischemic brain areas. Premature reduction in blood pressure may compromise blood flow to the penumbral region, potentially enlarging the infarct size.",
        "clinical_correlation": "Patients who present with ischemic stroke within the first 24 hours often have elevated BP as a compensatory mechanism. The CT scan findings of an established stroke indicate that the infarct is complete and that aggressive lowering of blood pressure might risk further hypoperfusion of regions that are still at risk.",
        "diagnostic_approach": "Imaging with CT is key to differentiating between ischemic stroke and hemorrhage and to identify whether the infarct is established. Clinical assessment and BP monitoring play a critical role in determining management.",
        "classification_and_neurology": "Blood pressure management in acute ischemic stroke falls under the broader classification of cerebrovascular disease management within the stroke subspecialty. The American Heart Association/American Stroke Association (AHA/ASA) guidelines classify stroke into ischemic and hemorrhagic types, with further subclassifications based on etiology (e.g., large artery atherosclerosis, cardioembolism). BP management strategies are stratified according to stroke phase (acute, subacute, chronic) and treatment eligibility (e.g., thrombolysis).   The current consensus, as per AHA/ASA, delineates BP targets for patients not receiving reperfusion therapy versus those eligible for thrombolysis or thrombectomy. This classification system has evolved from earlier uniform BP lowering approaches to more nuanced, individualized strategies reflecting advances in stroke pathophysiology and treatment modalities. Controversies remain regarding optimal BP thresholds in various clinical scenarios, but guidelines provide evidence-based frameworks to guide practice.",
        "classification_and_nosology": "Ischemic strokes are categorized based on etiology (for example, large artery atherosclerosis, cardioembolism, lacunar infarcts) as per the TOAST classification. This case fits into the scenario of an established infarct, where aggressive BP lowering is contraindicated.",
        "management_principles": "Current guidelines recommend not lowering blood pressure immediately in acute ischemic stroke patients who are not candidates for reperfusion therapy. Unless the blood pressure is extremely high (typically above 220/120 mm Hg), a permissive approach is advised. In patients receiving thrombolysis, a target of <185/110 mm Hg is recommended. In pregnant or lactating patients, careful blood pressure control with medication that is safe in these populations (e.g., labetalol) is advised, but the general principle of avoiding unnecessary BP reduction remains.",
        "option_analysis": "Option A ('Keep bp the same') is correct because, in the setting of an established ischemic stroke without a thrombolytic indication, maintaining a higher blood pressure can help preserve perfusion to the penumbra. Other options that advocate for lowering BP could risk reducing cerebral blood flow and worsening ischemia.",
        "clinical_pearls": "1) Permissive hypertension is standard in acute ischemic stroke when not undergoing thrombolysis. 2) Avoid lowering BP in the first 24 hours unless extremely high. 3) The target for thrombolytic candidates is <185/110 mm Hg, but this does not apply here.",
        "current_evidence": "Several studies have shown that early aggressive blood pressure lowering in acute ischemic stroke without thrombolysis does not improve outcomes and may be harmful. These findings have solidified the practice of permissive hypertension in these patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993106",
    "fields": {
      "question_number": "81",
      "question_text": "Case scenario of a patient k/c DM, cardiac risk factors on ASA came with right hemiplegia, has left MCA stenosis what is your next step?",
      "options": {
        "A": "Medical",
        "B": "endarterectomy",
        "C": "stenting",
        "D": "is not provided."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "The patient described has significant vascular risk factors and presents with right hemiplegia, correlating with left middle cerebral artery (MCA) stenosis. The management of intracranial stenosis, especially in the MCA, is predominantly medical since the lesions are less amenable to surgical intervention.",
        "pathophysiology": "Atherosclerotic narrowing in the MCA reduces the blood flow to the corresponding cerebral territory, predisposing to ischemia. In patients with diabetes and cardiac risk factors, atherosclerosis is progressive, making optimal medical management crucial.",
        "clinical_correlation": "Right hemiplegia points to ischemia in the left MCA territory. Neuroimaging (CT/MRI and vessel imaging) confirms the presence of focal stenosis, which correlates with the patient\u2019s risk factors and clinical presentation.",
        "diagnostic_approach": "Diagnosis involves non-invasive imaging modalities like CT angiography or MR angiography to evaluate the degree and location of stenosis. Differential diagnoses include embolic occlusion and other causes of large-vessel ischemic stroke. Detailed vascular imaging helps differentiate intracranial stenosis from extracranial carotid disease.",
        "classification_and_neurology": "Symptomatic MCA stenosis falls under the category of intracranial large artery atherosclerosis, a subtype of ischemic stroke classified by the Trial of ORG 10172 in Acute Stroke Treatment (TOAST) criteria. The TOAST classification identifies large artery atherosclerosis as a major ischemic stroke subtype, further subdivided by lesion location (intracranial vs extracranial). Intracranial arterial stenosis is part of the broader cerebrovascular disease family, which includes small vessel disease and cardioembolic sources. Classification systems have evolved to emphasize imaging-defined etiologies, with intracranial stenosis recognized as a distinct entity with unique epidemiology and management considerations compared to extracranial carotid stenosis. Controversies remain regarding optimal intervention strategies, especially for intracranial lesions.",
        "classification_and_nosology": "This condition is classified under intracranial atherosclerotic disease, which is a subset of stroke due to large artery atherosclerosis (as defined by the TOAST criteria). Left MCA stenosis is specifically an intracranial lesion and is managed differently compared to extracranial carotid stenosis.",
        "management_principles": "According to the latest guidelines and evidence (e.g., SAMMPRIS trial), aggressive medical management is the first-line treatment for intracranial atherosclerotic disease. This includes dual antiplatelet therapy (often aspirin plus clopidogrel in the acute/subacute phase), statin therapy, and strict control of risk factors such as hypertension, diabetes, and hyperlipidemia. In patients with this profile, endarterectomy is not performed on intracranial vessels, and stenting has been associated with higher complication rates. For pregnant or lactating women, antiplatelet and statin use require careful consideration, with medications chosen based on their safety profiles in these populations.",
        "option_analysis": "Option A (Medical) is correct because medical management is the mainstay of treatment for intracranial MCA stenosis. Option B (Endarterectomy) is typically reserved for extracranial carotid stenosis and is not feasible for the MCA. Option C (Stenting) has been evaluated in trials like SAMMPRIS and found to carry a higher peri-procedural risk compared with aggressive medical therapy. Option D is not provided.",
        "clinical_pearls": "1) Intracranial atherosclerotic disease is best managed with aggressive medical therapy rather than surgical intervention. 2) The SAMMPRIS trial has significantly influenced management by favoring medical management over stenting. 3) Optimal control of vascular risk factors is essential to prevent recurrent events.",
        "current_evidence": "Recent randomized control trials, notably SAMMPRIS, have reinforced that aggressive medical management (dual antiplatelet therapy, statins, and risk factor control) is superior to interventional strategies in reducing the risk of recurrent stroke in patients with intracranial stenosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993107",
    "fields": {
      "question_number": "82",
      "question_text": "Case scenario of acute ischemic stroke patient\u2026 contraindication for tpa?",
      "options": {
        "A": "Bp>200",
        "B": "rapid improvement",
        "C": "PLT <150"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke management with IV tPA, several contraindications must be considered. One of the classical exclusions listed in many exam settings is that patients whose neurological deficits are rapidly improving (\u201crapid improvement\u201d) are often not given tPA, since many of these patients may continue to improve without intervention.",
        "pathophysiology": "tPA works by catalyzing the conversion of plasminogen to plasmin, thereby dissolving thrombi. However, the risk-benefit ratio is optimized when deficits are significant and persistent. Rapid improvement may indicate spontaneous recanalization or minor deficits, reducing the expected benefit of thrombolysis while still exposing patients to hemorrhagic risk. Although other factors such as severe uncontrolled hypertension (e.g., systolic >185 mm Hg) are absolute contraindications unless controlled, many clinical protocols have historically listed rapid improvement as an exclusion criterion.",
        "clinical_correlation": "Patients presenting with acute ischemic stroke are evaluated for eligibility for tPA. A patient whose neurological deficits improve rapidly may be observed rather than treated because the potential risks (such as hemorrhagic transformation) may outweigh the marginal benefit if the deficit is already resolving.",
        "diagnostic_approach": "Prior to tPA administration, a full workup including noncontrast head CT (to exclude hemorrhage), blood pressure measurement, coagulation profile, and complete blood count (platelet count should be \u2265100,000/\u03bcL) is performed. The differential includes uncontrolled hypertension, bleeding diatheses, and mild strokes; each is evaluated for appropriateness for tPA use.",
        "classification_and_neurology": "Acute ischemic stroke is classified based on etiology (TOAST criteria) into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. The management of ischemic stroke falls under cerebrovascular disease classifications in neurology. Thrombolytic therapy indications and contraindications are codified in guidelines such as those from the American Heart Association/American Stroke Association (AHA/ASA). Contraindications are divided into absolute and relative categories based on hemorrhagic risk and patient safety. The concept of rapid neurological improvement as a contraindication reflects the dynamic nature of ischemic injury and the risk-benefit assessment in thrombolysis. Over time, classification systems have evolved to incorporate imaging findings and molecular markers, but clinical criteria remain central to acute management decisions.",
        "classification_and_nosology": "Contraindications to tPA are divided into absolute (e.g., evidence of intracranial hemorrhage, extremely elevated blood pressure that cannot be lowered promptly, recent major surgery) and relative (e.g., minor or rapidly improving neurological deficits). The item \u201crapid improvement\u201d fits under relative contraindications in many protocols, though there is evolving perspective on its application.",
        "management_principles": "Current guidelines recommend tPA only if the benefits exceed the risks. The earliest step is to control blood pressure if it is elevated (using IV antihypertensives to bring it below 185/110 mm Hg). In cases of rapidly improving symptoms, many centers opt for observation rather than administering tPA. Note that if the patient\u2019s residual deficits are still disabling despite some improvement, many now consider tPA administration even in the setting of improvement. In pregnant or lactating patients, extra caution is taken to balance risks, and blood pressure management is critical before any intervention.",
        "option_analysis": "Option A (BP >200): Although high blood pressure is a contraindication if not promptly controlled (with the standard threshold being >185/110 mm Hg), such elevations are frequently managed prior to tPA administration. Option B (Rapid improvement): Traditionally a contraindication since patients with rapidly improving symptoms (often non\u2010disabling) were excluded in major tPA trials. Option C (Platelets <150): The accepted threshold for platelets is <100,000/\u03bcL; values between 100,000 and 150,000 are not considered an absolute contraindication. Thus, option B is the intended answer in many board-style questions.",
        "clinical_pearls": "\u2022 Rapid improvement does not always guarantee full recovery; however, if deficits become minimal and non-disabling, tPA may be withheld.  \u2022 Blood pressure must be below 185/110 mm Hg prior to tPA, but elevations can be pharmacologically controlled before treatment.",
        "current_evidence": "Recent research indicates that the decision to exclude patients based solely on rapid improvement should be individualized since some patients with transient improvement may worsen. Nonetheless, many exam guidelines still list rapid improvement as an exclusion criterion for tPA eligibility."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993108",
    "fields": {
      "question_number": "83",
      "question_text": "Case scenario of a patient with lower extremity weakness worse upon coughing or Valsalva. MRI spine attached. What is your diagnosis?",
      "options": {
        "A": "Dural AVF"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke management with IV tPA, several contraindications must be considered. One of the classical exclusions listed in many exam settings is that patients whose neurological deficits are rapidly improving (\u201crapid improvement\u201d) are often not given tPA, since many of these patients may continue to improve without intervention.",
        "pathophysiology": "tPA works by catalyzing the conversion of plasminogen to plasmin, thereby dissolving thrombi. However, the risk-benefit ratio is optimized when deficits are significant and persistent. Rapid improvement may indicate spontaneous recanalization or minor deficits, reducing the expected benefit of thrombolysis while still exposing patients to hemorrhagic risk. Although other factors such as severe uncontrolled hypertension (e.g., systolic >185 mm Hg) are absolute contraindications unless controlled, many clinical protocols have historically listed rapid improvement as an exclusion criterion.",
        "clinical_correlation": "Patients presenting with acute ischemic stroke are evaluated for eligibility for tPA. A patient whose neurological deficits improve rapidly may be observed rather than treated because the potential risks (such as hemorrhagic transformation) may outweigh the marginal benefit if the deficit is already resolving.",
        "diagnostic_approach": "Prior to tPA administration, a full workup including noncontrast head CT (to exclude hemorrhage), blood pressure measurement, coagulation profile, and complete blood count (platelet count should be \u2265100,000/\u03bcL) is performed. The differential includes uncontrolled hypertension, bleeding diatheses, and mild strokes; each is evaluated for appropriateness for tPA use.",
        "classification_and_neurology": "Spinal vascular malformations are classified into four main types: Type I (dural AVF), Type II (glomus AVM), Type III (juvenile AVM), and Type IV (intradural perimedullary AVF). Spinal dural AVFs (Type I) are the most common and typically present in middle-aged to elderly males. They are characterized by a single fistulous connection between a dural branch of a radicular artery and a medullary vein. This classification system, first proposed by Anson and Spetzler and refined over time, helps guide diagnosis and management. The nosology distinguishes dAVFs from intramedullary AVMs and perimedullary AVFs based on angioarchitecture, clinical presentation, and treatment approach. Current consensus favors this classification due to its clinical utility and correlation with outcomes, though some debate remains about overlapping features in complex cases.",
        "classification_and_nosology": "Contraindications to tPA are divided into absolute (e.g., evidence of intracranial hemorrhage, extremely elevated blood pressure that cannot be lowered promptly, recent major surgery) and relative (e.g., minor or rapidly improving neurological deficits). The item \u201crapid improvement\u201d fits under relative contraindications in many protocols, though there is evolving perspective on its application.",
        "management_principles": "Current guidelines recommend tPA only if the benefits exceed the risks. The earliest step is to control blood pressure if it is elevated (using IV antihypertensives to bring it below 185/110 mm Hg). In cases of rapidly improving symptoms, many centers opt for observation rather than administering tPA. Note that if the patient\u2019s residual deficits are still disabling despite some improvement, many now consider tPA administration even in the setting of improvement. In pregnant or lactating patients, extra caution is taken to balance risks, and blood pressure management is critical before any intervention.",
        "option_analysis": "Option A (BP >200): Although high blood pressure is a contraindication if not promptly controlled (with the standard threshold being >185/110 mm Hg), such elevations are frequently managed prior to tPA administration. Option B (Rapid improvement): Traditionally a contraindication since patients with rapidly improving symptoms (often non\u2010disabling) were excluded in major tPA trials. Option C (Platelets <150): The accepted threshold for platelets is <100,000/\u03bcL; values between 100,000 and 150,000 are not considered an absolute contraindication. Thus, option B is the intended answer in many board-style questions.",
        "clinical_pearls": "\u2022 Rapid improvement does not always guarantee full recovery; however, if deficits become minimal and non-disabling, tPA may be withheld.  \u2022 Blood pressure must be below 185/110 mm Hg prior to tPA, but elevations can be pharmacologically controlled before treatment.",
        "current_evidence": "Recent research indicates that the decision to exclude patients based solely on rapid improvement should be individualized since some patients with transient improvement may worsen. Nonetheless, many exam guidelines still list rapid improvement as an exclusion criterion for tPA eligibility."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993109",
    "fields": {
      "question_number": "84",
      "question_text": "Case scenario of 1 day history of a patient with malignant MCA stroke next step (CT brain attached? 2/3 hypodensity without midline shift or hydrocephalus)",
      "options": {
        "A": "Hemicaniectomy",
        "B": "Osmotic therapy",
        "C": "ASA",
        "D": "Aspirin",
        "E": "Indications for hemicraniotomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke management with IV tPA, several contraindications must be considered. One of the classical exclusions listed in many exam settings is that patients whose neurological deficits are rapidly improving (\u201crapid improvement\u201d) are often not given tPA, since many of these patients may continue to improve without intervention.",
        "pathophysiology": "tPA works by catalyzing the conversion of plasminogen to plasmin, thereby dissolving thrombi. However, the risk-benefit ratio is optimized when deficits are significant and persistent. Rapid improvement may indicate spontaneous recanalization or minor deficits, reducing the expected benefit of thrombolysis while still exposing patients to hemorrhagic risk. Although other factors such as severe uncontrolled hypertension (e.g., systolic >185 mm Hg) are absolute contraindications unless controlled, many clinical protocols have historically listed rapid improvement as an exclusion criterion.",
        "clinical_correlation": "Patients presenting with acute ischemic stroke are evaluated for eligibility for tPA. A patient whose neurological deficits improve rapidly may be observed rather than treated because the potential risks (such as hemorrhagic transformation) may outweigh the marginal benefit if the deficit is already resolving.",
        "diagnostic_approach": "Prior to tPA administration, a full workup including noncontrast head CT (to exclude hemorrhage), blood pressure measurement, coagulation profile, and complete blood count (platelet count should be \u2265100,000/\u03bcL) is performed. The differential includes uncontrolled hypertension, bleeding diatheses, and mild strokes; each is evaluated for appropriateness for tPA use.",
        "classification_and_neurology": "Malignant MCA infarction is classified as a subset of large territory ischemic strokes with a high risk of life-threatening cerebral edema. Stroke classification systems such as the TOAST criteria categorize ischemic stroke by etiology (large artery atherosclerosis, cardioembolism, etc.), but malignant MCA infarction is defined by clinical and radiological severity rather than etiology alone. It belongs to the family of large vessel occlusion strokes with secondary malignant edema. The term 'malignant' reflects the natural history and poor prognosis without intervention. Current consensus emphasizes the distinction between large MCA strokes with and without malignant edema due to implications for management. There is some debate about timing and selection criteria for decompressive surgery, but consensus guidelines have standardized indications based on infarct size and clinical deterioration.",
        "classification_and_nosology": "Contraindications to tPA are divided into absolute (e.g., evidence of intracranial hemorrhage, extremely elevated blood pressure that cannot be lowered promptly, recent major surgery) and relative (e.g., minor or rapidly improving neurological deficits). The item \u201crapid improvement\u201d fits under relative contraindications in many protocols, though there is evolving perspective on its application.",
        "management_principles": "Current guidelines recommend tPA only if the benefits exceed the risks. The earliest step is to control blood pressure if it is elevated (using IV antihypertensives to bring it below 185/110 mm Hg). In cases of rapidly improving symptoms, many centers opt for observation rather than administering tPA. Note that if the patient\u2019s residual deficits are still disabling despite some improvement, many now consider tPA administration even in the setting of improvement. In pregnant or lactating patients, extra caution is taken to balance risks, and blood pressure management is critical before any intervention.",
        "option_analysis": "Option A (BP >200): Although high blood pressure is a contraindication if not promptly controlled (with the standard threshold being >185/110 mm Hg), such elevations are frequently managed prior to tPA administration. Option B (Rapid improvement): Traditionally a contraindication since patients with rapidly improving symptoms (often non\u2010disabling) were excluded in major tPA trials. Option C (Platelets <150): The accepted threshold for platelets is <100,000/\u03bcL; values between 100,000 and 150,000 are not considered an absolute contraindication. Thus, option B is the intended answer in many board-style questions.",
        "clinical_pearls": "\u2022 Rapid improvement does not always guarantee full recovery; however, if deficits become minimal and non-disabling, tPA may be withheld.  \u2022 Blood pressure must be below 185/110 mm Hg prior to tPA, but elevations can be pharmacologically controlled before treatment.",
        "current_evidence": "Recent research indicates that the decision to exclude patients based solely on rapid improvement should be individualized since some patients with transient improvement may worsen. Nonetheless, many exam guidelines still list rapid improvement as an exclusion criterion for tPA eligibility."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993110",
    "fields": {
      "question_number": "85",
      "question_text": "Case scenario of a patient with acute onset weakness and pain & temperature loss, sparing vibration? Dx?",
      "options": {
        "A": "Spinal cord infarction"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "The central concept here is recognition of an acute spinal cord lesion that produces a dissociated sensory loss\u2014specifically, loss of pain and temperature sensation due to involvement of the spinothalamic tracts, while sparing the dorsal columns which mediate vibration and proprioception. This pattern is classic for anterior spinal artery syndrome, a form of spinal cord infarction.",
        "pathophysiology": "Spinal cord infarction typically results from occlusion of the anterior spinal artery, which supplies the anterior two-thirds of the spinal cord. This region includes not only the motor pathways but also the spinothalamic tracts, responsible for pain and temperature sensation. In contrast, the dorsal columns receive blood from the posterior spinal arteries, preserving vibratory and proprioceptive sensations.",
        "clinical_correlation": "Patients often present acutely with weakness and a distinct pattern of sensory loss\u2014loss of pain and temperature with preserved vibration and proprioception below the level of the lesion. This presentation helps differentiate anterior spinal artery syndrome from other myelopathies, where both sensory modalities might be impaired.",
        "diagnostic_approach": "Key differential diagnoses include anterior spinal artery syndrome (spinal cord infarction) versus conditions such as transverse myelitis, compressive myelopathy, or a syrinx (syringomyelia); however, the acute onset favors an ischemic etiology. MRI of the spine is the investigation of choice to confirm infarction in the anterior spinal cord and to rule out other compressive or inflammatory causes.",
        "classification_and_neurology": "Spinal cord infarction is classified under **vascular myelopathies**, a subset of spinal cord disorders caused by ischemia or hemorrhage.   It belongs to the broader category of **acute spinal cord syndromes** and specifically to the anterior spinal artery syndrome subgroup.   The classification of spinal cord infarction is based on: - Vascular territory involved (anterior vs posterior spinal artery) - Clinical syndrome (anterior spinal artery syndrome, posterior spinal artery syndrome, central cord syndrome)  Historically, the classification has evolved from purely clinical syndromes to incorporate imaging and etiological data. Current consensus emphasizes the vascular territory and clinical features for diagnosis.   Controversies remain regarding the best classification when overlapping syndromes or mixed vascular territories are involved, but anterior spinal artery syndrome remains a well-defined clinical entity.",
        "classification_and_nosology": "Spinal cord infarction is classified among vascular myelopathies and is typically described as anterior spinal artery syndrome when the infarct involves the anterior two-thirds of the cord. It is distinct from inflammatory, compressive, and demyelinating myelopathies in both its etiology and clinical features.",
        "management_principles": "Management of spinal cord infarction is largely supportive. This includes maintaining adequate blood pressure and oxygenation to optimize spinal cord perfusion. There is no definitive acute therapy; thrombolytic therapy is not standard in this context. In pregnant and lactating patients, careful attention must be paid to the safety of hemodynamic support medications and imaging techniques (preferably MRI without contrast when possible). Rehabilitation plays a crucial role in long-term recovery.",
        "option_analysis": "The presentation of acute onset weakness accompanied by loss of pain and temperature sensation with intact vibration points directly to an anterior cord lesion due to spinal cord infarction. Alternative possibilities like syringomyelia typically have a more insidious course and a 'cape-like' distribution of sensory loss, while inflammatory causes would not present as acutely.",
        "clinical_pearls": "Acute onset dissociated sensory loss, where pain and temperature are impaired with intact proprioception and vibration, is a hallmark of anterior spinal artery syndrome. Prompt imaging is key to confirming the diagnosis and ruling out other causes. In all patients, including special populations such as pregnant or lactating individuals, a supportive management strategy is essential.",
        "current_evidence": "Current guidelines emphasize early recognition and supportive care for spinal cord infarction. While ongoing research into neuroprotective strategies continues, treatment remains supportive and focused on rehabilitation. In managing pregnant or breastfeeding patients, clinicians should tailor supportive measures and imaging protocols to minimize fetal or neonatal risk."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993111",
    "fields": {
      "question_number": "86",
      "question_text": "Women after successful vaginal delivery complained of severe Headache, hemiparesis and her exam showed papilledema, what to do",
      "options": {
        "A": "CTV"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In postpartum women, especially after a vaginal delivery, the hypercoagulable state increases the risk for cerebral venous sinus thrombosis (CVT). CVT typically presents with severe headache, focal neurological deficits (such as hemiparesis), and signs of increased intracranial pressure (e.g., papilledema).",
        "pathophysiology": "During the postpartum period, hormonal changes and a hypercoagulable state predispose women to thrombosis. In CVT, thrombus formation in the dural venous sinuses impairs venous drainage, resulting in increased venous pressure, cerebral edema, and potential hemorrhagic venous infarcts. Recent evidence emphasizes early diagnosis to mitigate brain injury.",
        "clinical_correlation": "The presentation of severe headache, hemiparesis, and papilledema in this patient is highly suspicious for CVT. Papilledema indicates raised intracranial pressure, while focal deficits (hemiparesis) suggest the presence of localized brain injury or infarction secondary to venous occlusion.",
        "diagnostic_approach": "The gold standard diagnostic tools include MR Venography and CT Venography (CTV). The latter is often more readily available and can quickly detect venous sinus occlusion. Differential diagnoses include intracranial hemorrhage, arterial stroke, post-dural puncture headache with neurological sequelae, and even eclampsia, which must be differentiated based on imaging and clinical history.",
        "classification_and_neurology": "CVT is classified under cerebrovascular diseases, specifically within the category of venous strokes. According to the International Classification of Diseases (ICD-11) and the American Heart Association/American Stroke Association (AHA/ASA) stroke classification, CVT is a distinct entity from arterial ischemic stroke and intracerebral hemorrhage.  CVT can be subclassified based on site of thrombosis (e.g., superior sagittal sinus, transverse sinus, deep cerebral veins), etiology (e.g., puerperium, thrombophilia, infection), and clinical presentation (acute, subacute, chronic). The classification has evolved with advances in neuroimaging allowing precise localization of thrombi. Current consensus emphasizes the importance of recognizing CVT as a cause of stroke-like symptoms in young adults and peripartum women, differentiating it from other stroke subtypes due to differing management and prognosis.  Controversies exist regarding the classification of isolated cortical vein thrombosis and the role of genetic thrombophilias in CVT risk stratification.",
        "classification_and_nosology": "CVT is classified as a form of stroke that affects the venous rather than the arterial vasculature. It falls under the broader category of cerebrovascular disorders and is distinct from arterial ischemic or hemorrhagic strokes.",
        "management_principles": "First-line management for CVT is anticoagulation, typically with low molecular weight heparin even in the presence of small hemorrhagic infarcts. Subsequent therapies include transitioning to oral anticoagulants for long-term management. In pregnancy or lactation, LMWH is preferred due to its safety profile for both the mother and the infant. Supportive care, management of intracranial pressure, and monitoring for neurological deterioration are essential.",
        "option_analysis": "Option A (CTV) is appropriate because CT Venography is a rapid, accessible imaging modality to evaluate the cerebral venous system. While MR Venography is also highly sensitive, CTV is a correct choice, especially in an acute setting. The other options (B, C, D) were not provided, but they likely represent less optimal or unrelated imaging techniques.",
        "clinical_pearls": "1) Always suspect CVT in postpartum women presenting with headache and neurological deficits. 2) Papilledema is a key indicator of increased intracranial pressure and should prompt urgent imaging. 3) Early diagnosis with CTV or MRV improves outcomes by enabling prompt anticoagulation.",
        "current_evidence": "Recent guidelines from neurology and stroke associations underscore the importance of early imaging with CT or MR Venography for suspected CVT. Studies continue to support the safety and efficacy of early anticoagulation even in the presence of minor hemorrhagic changes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993112",
    "fields": {
      "question_number": "87",
      "question_text": "Patient came with a CT brain attached unilateral occipital stroke, asked about which artery? (According to picture)",
      "options": {
        "A": "PCA",
        "B": "SCA",
        "C": "PICA",
        "D": "MCA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "The occipital lobe is primarily supplied by the posterior cerebral artery (PCA). Infarctions in this region most commonly result from occlusion of the PCA, leading to visual deficits.",
        "pathophysiology": "An occlusion in the PCA causes ischemia in the occipital cortex. The resulting infarction typically affects the primary visual processing areas, leading to characteristic visual field deficits such as contralateral homonymous hemianopia with possible macular sparing. Current research supports the role of rapid reperfusion therapies in minimizing infarct size.",
        "clinical_correlation": "Patients with a PCA stroke usually present with visual disturbances \u2013 most notably, a loss of the contralateral visual field. The CT image showing a unilateral occipital stroke is consistent with PCA territory involvement. This distinguishes it from other strokes that affect motor or sensory cortices.",
        "diagnostic_approach": "Imaging via CT and magnetic resonance imaging (MRI) can help identify the infarct location. Differential diagnoses include strokes in the middle cerebral artery (MCA) territory (which typically present with motor and sensory deficits), and those in the cerebellar regions (supplied by the SCA or PICA), which present with coordination issues.",
        "classification_and_neurology": "Ischemic strokes are classified by vascular territory and underlying etiology. The **TOAST classification** categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. PCA strokes fall under large artery atherosclerosis or cardioembolism when involving the posterior circulation. The PCA is part of the **posterior circulation**, which includes vertebral, basilar, and PCA arteries, distinct from the anterior circulation supplied by the internal carotid system. Stroke classification systems have evolved to integrate imaging and clinical data for better prognostication. There remains debate on the best approach to classify posterior circulation strokes due to overlapping symptoms and less frequent occurrence compared to anterior circulation strokes.",
        "classification_and_nosology": "PCA strokes are classified under ischemic cerebrovascular accidents. They are categorized based on the affected arterial territory. The infarct localization helps determine both prognosis and therapeutic approach.",
        "management_principles": "The management of an acute PCA stroke includes intravenous thrombolysis if the patient presents within the therapeutic window, followed by antiplatelet agents. Mechanical thrombectomy is considered in select cases based on the size and occlusion site. In pregnant or lactating women, thrombolysis may still be considered after careful risk\u2010benefit assessment, while antiplatelet management should consider safety for the fetus or neonate.",
        "option_analysis": "Option A (PCA) is correct because the occipital lobe is vascularized by the posterior cerebral artery. Option B (SCA) and Option C (PICA) supply cerebellar regions, and Option D (MCA) supplies the lateral aspects of the cerebral hemispheres, which typically do not include the occipital lobe.",
        "clinical_pearls": "1) Occipital strokes most commonly result in visual field deficits like homonymous hemianopia. 2) Macular sparing is a classic finding in PCA strokes due to collateral blood supply. 3) Timely reperfusion therapy is pivotal in preserving visual function.",
        "current_evidence": "Recent updates in stroke guidelines emphasize the window for thrombolysis and detail criteria for mechanical thrombectomy. Advanced imaging techniques are increasingly used to guide individualized management plans."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_39.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993113",
    "fields": {
      "question_number": "88",
      "question_text": "Patient post carotid stent or endarterectomy (not sure) Came with altered level of conscious, CT attached (small Right frontal cortical hemorrhage)",
      "options": {
        "A": "hyperperfusion syndrome"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Hyperperfusion syndrome is a known complication following carotid revascularization procedures such as stenting or endarterectomy. It occurs due to impaired cerebral autoregulation in chronically hypoperfused brain regions.",
        "pathophysiology": "After carotid revascularization, the sudden restoration of blood flow can overwhelm the distal vasculature that has adapted to a lower perfusion state. The loss of autoregulation leads to excessive cerebral blood flow, which in turn can cause blood\u2013brain barrier disruption, vasogenic edema, and even small hemorrhages, as seen in the CT image (small right frontal cortical hemorrhage).",
        "clinical_correlation": "Patients typically present within days following the procedure with symptoms ranging from headache and altered mental status to seizures. In this case, the altered level of consciousness and CT findings are consistent with hyperperfusion syndrome.",
        "diagnostic_approach": "Diagnosis is primarily clinical, supported by imaging findings. Differential diagnoses include embolic stroke, reperfusion injury, and hemorrhagic transformation of an ischemic infarct. A detailed review of the procedural history and blood pressure control is essential.",
        "classification_and_neurology": "Hyperperfusion syndrome is classified under cerebrovascular complications of carotid revascularization procedures. It belongs to the family of reperfusion injuries, distinct from ischemic stroke syndromes caused by embolism or thrombosis. Within stroke classifications, it is considered a hemorrhagic complication secondary to intervention rather than a primary ischemic event. Nosologically, it is recognized as a post-procedural syndrome characterized by dysregulated cerebral blood flow leading to neurological deficits. The syndrome is differentiated from cerebral hyperperfusion syndrome without hemorrhage (which may present with only headache and seizures) and from reperfusion hemorrhagic transformation seen after ischemic stroke thrombolysis. Current consensus classifies HPS as a rare but serious complication of CEA and CAS with specific diagnostic criteria focusing on clinical presentation, imaging findings, and temporal relation to intervention. Some controversy exists regarding optimal diagnostic thresholds for cerebral blood flow increases defining hyperperfusion, but clinical and radiological criteria remain the cornerstone.",
        "classification_and_nosology": "Hyperperfusion syndrome is categorized as a reperfusion injury that occurs post-carotid intervention. It is considered an iatrogenic complication related to the restoration of blood flow and disruption of normal cerebral autoregulation.",
        "management_principles": "The cornerstone of management is strict blood pressure control using IV antihypertensives (e.g., labetalol, nicardipine). In addition, supportive care and neurological monitoring are key. For patients who are pregnant or lactating, antihypertensive choices should be guided by safety profiles (e.g., labetalol is generally considered safe during pregnancy). Early recognition and aggressive blood pressure management are critical to prevent further neurological deterioration.",
        "option_analysis": "Option A (hyperperfusion syndrome) is correct given the clinical context of recent carotid intervention, altered mental status, and the imaging findings of a small cortical hemorrhage. Other options, which were not provided, likely pertain to alternative causes of post-procedural complications but do not fit the described presentation.",
        "clinical_pearls": "1) Post-carotid revascularization, any sudden neurological deterioration should raise suspicion for hyperperfusion syndrome. 2) Strict blood pressure control is essential in the immediate postoperative period to minimize the risk of reperfusion injury. 3) Early imaging is key to differentiating between hyperperfusion syndrome and embolic events.",
        "current_evidence": "Recent studies highlight the importance of individualized blood pressure targets post-revascularization and reinforce early detection protocols for hyperperfusion syndrome. Updated guidelines recommend the use of IV antihypertensive agents with a favorable safety profile in sensitive populations including pregnant women."
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
