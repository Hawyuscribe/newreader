
# Import batch 1 of 3 from chunk_10_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993310",
    "fields": {
      "question_number": "339",
      "question_text": "Site of lesion in weber syndrome",
      "options": {
        "A": "Base of midbrain",
        "B": "tegmentum",
        "C": "tectum"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Weber syndrome is a classical brainstem stroke syndrome characterized by ipsilateral oculomotor nerve dysfunction (manifesting as ptosis and ophthalmoplegia) and contralateral motor deficits. It results from a lesion in the midbrain.",
        "pathophysiology": "The syndrome is typically due to infarction or hemorrhage at the ventral (basal) portion of the midbrain affecting the exiting fibers of the oculomotor nerve and the corticospinal tracts that travel through the cerebral peduncles. The lesion is usually vascular in origin, commonly involving branches of the posterior cerebral artery.",
        "clinical_correlation": "Patients present with an ipsilateral third cranial nerve palsy (leading to diplopia and ptosis) along with contralateral hemiparesis, which reflects the involvement of adjacent motor pathways.",
        "diagnostic_approach": "Neuroimaging (MRI with diffusion-weighted imaging) is key in confirming the lesion in the ventral midbrain. Differential diagnoses include other midbrain syndromes such as Benedikt\u2019s syndrome, which additionally includes tremor and ataxia due to red nucleus involvement.",
        "classification_and_nosology": "Weber syndrome falls under the category of midbrain or brainstem strokes, specifically classified by vascular territory involvement of the paramedian branches of the posterior cerebral artery.",
        "management_principles": "Acute management follows standard stroke protocols including thrombolysis (if within window and no contraindications), blood pressure control, and supportive care. For patients who are pregnant or lactating, thrombolytic therapy and supportive measures are considered on a case-by-case basis following current AHA/ASA guidelines, with multidisciplinary consultation.",
        "option_analysis": "Option A (Base of midbrain) is correct because Weber syndrome classically involves the ventral midbrain (basis pedunculi), not the tegmentum (dorsal aspect) or the tectum (posterior aspect).",
        "clinical_pearls": "1. Weber syndrome is marked by the combination of oculomotor dysfunction and contralateral motor weakness. 2. Lesions are localized to the ventral midbrain. 3. Vascular supply from the posterior cerebral artery is typically implicated.",
        "current_evidence": "Recent imaging studies and guidelines continue to support the ventral midbrain localization in Weber syndrome. Management strategies align with broader ischemic stroke management protocols adapted to brainstem strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993311",
    "fields": {
      "question_number": "340",
      "question_text": "A man who has right side weakness and dysphasia, on stroke work up he was found to have left MCA severe stenosis what is the most appropriate management:",
      "options": {
        "A": "endarterectomy",
        "B": "stenting",
        "C": "Aspirin and plavix"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "A patient with right-sided weakness and dysphasia with left MCA stenosis is suffering an ischemic stroke related to intracranial atherosclerotic disease. The appropriate management of such a condition involves medical therapy rather than invasive procedures.",
        "pathophysiology": "Atherosclerotic disease of the left middle cerebral artery leads to luminal narrowing, reduced cerebral perfusion, and ultimately ischemia in the dependent brain territories. The resulting stroke produces contralateral motor and language deficits due to involvement of the dominant hemisphere.",
        "clinical_correlation": "The presentation of right-sided weakness and dysphasia reflects the involvement of the left MCA territory, which is responsible for motor control of the contralateral side of the body and language functions (in the dominant hemisphere).",
        "diagnostic_approach": "Diagnosis involves neuroimaging with CT/MRI to confirm infarct and vessel imaging (CTA/MRA) to assess the degree of stenosis. Differential considerations include embolic stroke from cardiac sources and lacunar strokes. Carotid duplex is more relevant for extracranial disease.",
        "classification_and_nosology": "This condition is classified as a form of ischemic stroke secondary to intracranial atherosclerosis. It falls under large-artery atherosclerotic strokes as categorized by the TOAST classification.",
        "management_principles": "First-line management is aggressive medical therapy with dual antiplatelet therapy (typically aspirin and clopidogrel) for a duration based on recent trials (e.g., 21-90 days, often 90 days in high-risk individuals). Second-line interventions, such as stenting or endarterectomy, are largely reserved for extracranial stenosis (e.g., carotid endarterectomy) and are not first-line for intracranial lesions. In pregnant or lactating patients with stroke, low-dose aspirin is generally considered safe, with careful multidisciplinary management tailoring the risk\u2013benefit ratio.",
        "option_analysis": "Option A (endarterectomy) is typically used for extracranial carotid stenosis and is not indicated for intracranial MCA stenosis. Option B (stenting) has been explored in clinical trials (e.g., SAMMPRIS) but has shown higher periprocedural risks compared to aggressive medical management. Option C (Aspirin and Plavix) is correct, representing the current standard of care for symptomatic intracranial atherosclerotic disease.",
        "clinical_pearls": "1. Intracranial atherosclerotic strokes are best managed medically with dual antiplatelet therapy. 2. Differentiation between intracranial and extracranial pathology is crucial when considering revascularization strategies. 3. SAMMPRIS trial data influenced the move toward medical management in these cases.",
        "current_evidence": "Recent trials, notably the SAMMPRIS study, have reinforced that aggressive medical management (including dual antiplatelet therapy and risk factor modification) provides superior outcomes compared to stenting for intracranial stenosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993312",
    "fields": {
      "question_number": "341",
      "question_text": "A patient who presented with inability to read his own hand writing, his comprehension for spoken language, fluency and repetition is normal (nothing was mentioned on his ability to write) what is the most common artery :",
      "options": {
        "A": "PCA",
        "B": "PICA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "The clinical presentation described is that of pure alexia (alexia without agraphia), a syndrome in which patients lose the ability to read despite preserved writing abilities and intact spoken language comprehension.",
        "pathophysiology": "This syndrome is most commonly encountered with infarcts in the territory of the left posterior cerebral artery (PCA), particularly affecting the left occipital lobe and often involving the splenium of the corpus callosum. The lesion disrupts visual processing and the transfer of visual information to language areas.",
        "clinical_correlation": "Patients with this syndrome can write and speak fluently, but when they attempt to read, whether it is their own writing or printed words, they are unable to decode the visual stimuli into meaningful language. This dissociation between reading and writing highlights the localization of the lesion.",
        "diagnostic_approach": "Neuroimaging (MRI) is essential for localizing the infarct, which typically involves the left occipital lobe. Differential diagnoses include other language disorders such as aphasia; however, in pure alexia, the preservation of spoken language distinguishes it from more global aphasic syndromes.",
        "classification_and_nosology": "Alexia without agraphia is categorized as a disconnection syndrome within the spectrum of stroke syndromes and is most commonly due to ischemic strokes within the posterior cerebral artery distribution.",
        "management_principles": "Acute management follows standard ischemic stroke protocols, including consideration for thrombolytic therapy if within the appropriate time window. Long-term management involves antiplatelet therapy, risk factor modification, and rehabilitation (including occupational and speech therapy). In pregnant or lactating patients, aspirin is typically acceptable with multidisciplinary review to balance risks and benefits, while thrombolytic therapy is used only under strict guidelines.",
        "option_analysis": "Option A (PCA) is correct because the syndrome of pure alexia is most commonly associated with infarcts in the left PCA territory. Option B (PICA) is incorrect as it typically supplies parts of the cerebellum and lateral brainstem rather than the occipital lobe.",
        "clinical_pearls": "1. Pure alexia (alexia without agraphia) is a disconnection syndrome resulting from left occipital infarct and splenial involvement. 2. The preservation of writing despite impaired reading is a key diagnostic feature. 3. The left PCA is the most often implicated vessel in this syndrome.",
        "current_evidence": "Recent research emphasizes the role of detailed neuroimaging in localizing lesions in stroke syndromes. Current stroke management guidelines continue to support prompt intervention in PCA strokes, with tailored approaches for special populations including pregnant and lactating patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993313",
    "fields": {
      "question_number": "342",
      "question_text": "Image of DWI showing watershed infarction in one side what to do :",
      "options": {
        "A": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Watershed infarctions occur at the border zones between major cerebral arteries. In cases where DWI imaging shows a unilateral watershed pattern, it raises concern for hemodynamic compromise, most commonly due to an upstream arterial stenosis (often in the internal carotid artery). The next logical step is to evaluate the vascular anatomy, which is best done with vascular imaging such as a CTA.",
        "pathophysiology": "Watershed zones are vulnerable to hypoperfusion. When there is significant stenosis or occlusion (commonly in the carotid circulation), these areas receive less than adequate blood flow, resulting in infarcts. CTA helps identify the site and severity of arterial narrowing, guiding further management.",
        "clinical_correlation": "Patients with watershed strokes can present with variable neurological deficits depending on the exact regions affected. The imaging pattern on DWI is distinct, and identifying the cause (such as carotid stenosis) is essential as it may alter future management, including possible revascularization procedures.",
        "diagnostic_approach": "Once DWI suggests a watershed infarct, vascular imaging (CTA in this case) is indicated. Differential diagnoses include embolic strokes and small vessel disease strokes; however, their imaging and clinical histories usually differ. CTA helps differentiate a hemodynamic mechanism from an embolic one by showing vascular narrowing or occlusion.",
        "classification_and_nosology": "Watershed infarcts are a subtype of ischemic strokes, often classified under large vessel atherosclerotic strokes. They are distinct from border-zone infarcts caused by embolism or lacunar infarcts from small vessel disease.",
        "management_principles": "After identifying a watershed infarct with CTA, management includes optimizing blood pressure, antiplatelet therapy, and addressing the underlying cause such as carotid atherosclerosis. For patients who are pregnant or lactating, CTA can be performed with proper shielding, and risk factor management (blood pressure, lipids) should follow guidelines that take maternal and fetal safety into account.",
        "option_analysis": "Option A (CTA) is correct because it provides crucial information on the vascular status (e.g., carotid/vertebral arteries) that likely contributed to the watershed infarct. The other options were either not provided or not appropriate for the next step in this scenario.",
        "clinical_pearls": "1) Unilateral watershed infarctions on DWI should prompt an evaluation for significant ipsilateral carotid stenosis. 2) Vascular imaging is a key next step in differentiating hemodynamic strokes from embolic phenomena.",
        "current_evidence": "Recent AHA/ASA guidelines emphasize early vessel imaging in acute ischemic stroke patients. Emerging research also supports the prompt use of CTA to lay the groundwork for possible interventions such as carotid revascularization if significant stenosis is identified."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993314",
    "fields": {
      "question_number": "343",
      "question_text": "Clear scenario of old man presented within the window of tpa about what to give:",
      "options": {
        "A": "Tpa"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Intravenous thrombolytic therapy (tPA) is the standard treatment for acute ischemic stroke if the patient is within the appropriate therapeutic window and meets eligibility criteria. The scenario describes an elderly man who is within this window.",
        "pathophysiology": "tPA works by catalyzing the conversion of plasminogen to plasmin, the enzyme responsible for breaking down fibrin clots. In the context of an ischemic stroke, the timely dissolution of the clot can restore blood flow, salvaging penumbral brain tissue.",
        "clinical_correlation": "Patients presenting with acute stroke symptoms require rapid evaluation including a non-contrast CT to exclude hemorrhage. If within 3-4.5 hours (and meeting other criteria) tPA is recommended. The older man in the scenario is an appropriate candidate assuming no contraindications are found on further workup.",
        "diagnostic_approach": "Initial assessment requires neuroimaging (usually a CT scan) to rule out hemorrhage. After confirming an ischemic event, the patient\u2019s history, time of symptom onset, and contraindications are reviewed. Differential diagnoses include stroke mimics like seizures or migraine, but the acute focal neurological deficits help distinguish true stroke.",
        "classification_and_nosology": "This management falls under the treatment of acute ischemic stroke. Guidelines separately classify acute stroke treatment strategies based on time windows \u2013 with tPA being the cornerstone for early management.",
        "management_principles": "The first-line management for eligible patients with acute ischemic stroke is IV tPA, ideally given within 3 to 4.5 hours of symptom onset. Subsequent treatments may include endovascular therapies if a large vessel occlusion is found. In pregnant or lactating women, tPA has been used with caution in select cases after weighing maternal and fetal risks, and consultation with specialists is advised.",
        "option_analysis": "Option A (tPA) is correct because the patient fits the criteria for thrombolysis. The other possible options (though not provided) would likely include alternatives not appropriate in the acute phase or less evidence-based interventions.",
        "clinical_pearls": "1) Time is brain \u2013 rapid recognition and treatment of acute ischemic stroke significantly improves outcomes. 2) Exclusion of hemorrhage via CT is essential before administering tPA.",
        "current_evidence": "The latest guidelines continue to support IV tPA in eligible acute ischemic stroke patients. Recent studies have also explored extended time windows and advanced imaging techniques, but standard practice remains to initiate tPA as early as possible within the defined window."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993315",
    "fields": {
      "question_number": "344",
      "question_text": "Patient with weakness hemianesthesia and tongue deviation (? medial medullary syndrome):",
      "options": {
        "A": "Vertebral artery",
        "B": "Anterior spinal artery (was not in options)"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Medial medullary syndrome, also known as Dejerine syndrome, is a brainstem stroke syndrome characterized by a triad of contralateral motor deficits, contralateral loss of proprioception/tactile sensation, and ipsilateral tongue deviation. The syndrome is most classically attributed to infarction in the territory supplied by the anterior spinal artery.",
        "pathophysiology": "The medial medulla is supplied primarily by the anterior spinal artery, a branch arising from the vertebral arteries. Occlusion of this vessel leads to infarction of structures in the medial medulla including the pyramids (causing weakness), medial lemniscus (affecting sensation), and the hypoglossal nerve nucleus (resulting in tongue deviation).",
        "clinical_correlation": "Clinically, patients typically present with contralateral hemiparesis and hemisensory loss along with tongue deviation toward the side of the lesion. This constellation of signs helps differentiate medial medullary syndrome from other brainstem strokes such as lateral medullary (Wallenberg) syndrome.",
        "diagnostic_approach": "Brain MRI with diffusion-weighted imaging is the modality of choice to identify medullary infarcts. To differentiate medial medullary syndrome from other brainstem strokes, vascular imaging (CTA or MRA) can be employed to assess the vertebral and anterior spinal arteries. Differential diagnoses include lateral medullary syndrome and pontine strokes, which have different clinical and imaging features.",
        "classification_and_nosology": "Medial medullary syndrome is classified as a brainstem stroke and is specifically due to infarction in the medial medulla. It is most frequently associated with occlusion of the anterior spinal artery, although sometimes the paramedian branches of the vertebral artery may be implicated.",
        "management_principles": "The management of medial medullary syndrome involves standard acute ischemic stroke protocols including potential thrombolysis, antiplatelet therapy thereafter, and aggressive risk factor management (e.g., controlling hypertension, dyslipidemia). In pregnant or lactating patients, treatment must be balanced with safety concerns, and nonpharmacologic measures or medications with established safety profiles in pregnancy should be considered.",
        "option_analysis": "Option B (Anterior spinal artery) is considered correct because infarction in medial medullary syndrome is most commonly due to occlusion of the anterior spinal artery. Option A (Vertebral artery) is less specific \u2013 although the vertebral artery gives rise to the anterior spinal artery, the classic lesion localizes to the territory of the anterior spinal artery rather than from a direct vertebral artery occlusion.",
        "clinical_pearls": "1) Medial medullary syndrome typically presents with contralateral hemiparesis and hemisensory loss with ipsilateral tongue weakness. 2) The anterior spinal artery, often a branch of the vertebral artery, is the vessel most commonly implicated in this syndrome.",
        "current_evidence": "Recent MRI-based studies and advanced vascular imaging have reinforced the role of the anterior spinal artery in medial medullary syndrome. Guidelines continue to advocate for rapid imaging and tailored management strategies in brainstem strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993316",
    "fields": {
      "question_number": "345",
      "question_text": "Long scenario for patient with obesity and HTN and high BMI asking about best way for stroke prevention, vital signs and labs provided showed high b/p and hba1c around 6.9. And he is taking ant HTN and statin but not any dm medication:",
      "options": {
        "A": "Perindopril",
        "B": "Metformin",
        "C": "Or weight reduction",
        "D": "Aspirin"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Stroke prevention in patients with multiple risk factors (such as obesity and hypertension) is most effectively achieved through a multifactorial approach that focuses on modifiable lifestyle factors. In a patient already on antihypertensive and statin medication with borderline glycemic control (HbA1c ~6.9), weight reduction can significantly reduce overall stroke risk.",
        "pathophysiology": "Obesity contributes to a pro-inflammatory state, insulin resistance, dyslipidemia, and increased blood pressure\u2014all of which favor atherosclerosis and increase the risk of stroke. Weight reduction has been shown to improve these metabolic parameters and reduce vascular inflammation.",
        "clinical_correlation": "Patients with obesity and hypertension are at an elevated risk for stroke due not only to high blood pressure but also because obesity worsens other metabolic risk factors. Weight reduction, therefore, becomes a central pillar of primary stroke prevention in such individuals.",
        "diagnostic_approach": "A thorough clinical assessment including vital signs, laboratory studies (such as HbA1c, fasting glucose, and lipid profile), and measurement of BMI is key for risk stratification. Differential diagnoses for stroke prevention strategies could include adjustments in antihypertensive regimes or initiation of diabetes medications, but lifestyle modification remains universally recommended as first-line.",
        "classification_and_nosology": "Primary prevention of stroke involves managing modifiable risk factors. This patient falls under the high-risk category due to obesity and hypertension, even though his glycemic control is only borderline abnormal.",
        "management_principles": "The first-line management for such a patient is lifestyle modification\u2014with weight reduction being paramount. This includes dietary changes, increased physical activity, and sometimes structured weight loss programs. While continuing antihypertensives and statins is essential, adding medications like metformin is reserved for established type 2 diabetes mellitus. Aspirin is not routinely recommended for primary prevention in all patients due to bleeding risks. In pregnancy and lactation, lifestyle modifications are especially prioritized to avoid medication side effects.",
        "option_analysis": "Option C (Weight reduction) is the best answer since it addresses the root modifiable risk factor. Option A (Perindopril) is already part of his antihypertensive regimen and further intensification would depend on blood pressure targets. Option B (Metformin) is not indicated unless he meets criteria for diabetes. Option D (Aspirin) has a limited role in primary prevention due to potential bleeding risks and is not the most effective choice here.",
        "clinical_pearls": "1) Lifestyle modification, especially weight reduction, is the cornerstone of primary stroke prevention in obese patients. 2) Optimizing modifiable risk factors (hypertension, hyperglycemia, dyslipidemia) can significantly reduce stroke risk.",
        "current_evidence": "Current guidelines emphasize the importance of a multifactorial approach to stroke prevention, with weight reduction being a key intervention. Recent studies have also highlighted the benefits of lifestyle modifications on cardiovascular outcomes, and these recommendations remain applicable in special populations (e.g., pregnant or lactating individuals) to minimize medication exposure when possible."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993317",
    "fields": {
      "question_number": "346",
      "question_text": "A woman presented with acute left sided weakness and dysarthria a right ICH was found on CT (image shown without mentioning the diagnosis) patient vital signs as follows BP 167 systolic, what is the most appropriate management:",
      "options": {
        "A": "labetalol",
        "B": "factor 7 infusion",
        "C": "referral for NS for (minimally invasive?) evacuation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Acute intracerebral hemorrhage (ICH) requires immediate management to prevent further bleeding and secondary brain injury. The core principle is to stabilize the patient by controlling blood pressure, which can reduce hematoma expansion and improve outcomes.",
        "pathophysiology": "In ICH, a ruptured cerebral vessel causes blood to accumulate within the brain parenchyma. Elevated blood pressure increases hydrostatic pressure on the vulnerable vessel walls, risking continued bleeding and hematoma enlargement. Controlling blood pressure minimizes further vessel disruption and secondary damage.",
        "clinical_correlation": "A patient presenting with acute left-sided weakness and dysarthria, in the context of a right-sided hemorrhage on CT, reflects the neurological deficits caused by mass effect and neuronal injury. The moderately elevated systolic pressure (167 mm Hg) is significant enough in this setting to justify immediate antihypertensive therapy.",
        "diagnostic_approach": "The gold standard in the acute setting is a non-contrast CT scan to identify ICH. Differential diagnoses include ischemic stroke (which typically shows no blood on the CT scan), subarachnoid hemorrhage (which has a different distribution on imaging), and stroke mimics such as tumors or seizures. Rapid imaging confirms the diagnosis, guiding early management.",
        "classification_and_nosology": "Intracerebral hemorrhage can be classified based on location (lobar, deep, cerebellar) and underlying cause (hypertensive, amyloid angiopathy, vascular malformations). This case is most consistent with a hypertensive hemorrhage, where blood pressure control is paramount.",
        "management_principles": "First-line management involves aggressive yet controlled blood pressure reduction using IV agents. Labetalol is a common first-line agent because of its rapid action and easy titration. Second-line approaches include using agents like nicardipine if labetalol is contraindicated. Neurosurgical intervention is reserved for cases with mass effect, imminent herniation, or specific locations (e.g., cerebellar hemorrhage). In pregnant and lactating patients, labetalol is also the antihypertensive of choice due to its well\u2010established safety profile in these populations.",
        "option_analysis": "Option A (labetalol) is correct because it is effective in controlling blood pressure in the acute ICH setting. Option B (factor 7 infusion) is not indicated; recombinant activated factor VII has been studied in hemorrhage but is associated with thrombotic risks and is not standard care in ICH. Option C (referral for neurosurgery for evacuation) is typically reserved for selected cases (e.g., cerebellar hemorrhages or those with significant mass effect) and is not the immediate priority in a patient with modest blood pressure elevation and a spontaneous ICH.",
        "clinical_pearls": "\u2022 Rapid blood pressure control is a cornerstone in preventing hematoma expansion in ICH.\n\u2022 Labetalol is safe and effective, including in pregnant and lactating patients.\n\u2022 Neurosurgical intervention is indicated only in select cases, not as the primary immediate treatment.",
        "current_evidence": "Recent trials such as INTERACT2 and ATACH-II support early and aggressive blood pressure lowering in ICH. The AHA/ASA guidelines recommend similar approaches, and labetalol remains a preferred agent due to its safety profile and efficacy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993318",
    "fields": {
      "question_number": "347",
      "question_text": "Scenario about TIA management:",
      "options": {
        "A": "Dual antiplatelet"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Transient ischemic attack (TIA) represents a temporary period of cerebral ischemia without permanent infarction. The primary goal is stroke prevention, and dual antiplatelet therapy (DAPT) has been shown to reduce early recurrent stroke risk in high-risk or minor TIA patients.",
        "pathophysiology": "TIAs typically result from transient thromboembolic events that temporarily interrupt cerebral blood flow. Platelet aggregation plays a crucial role in clot propagation, and using two antiplatelet agents can interrupt this process, reducing the risk of full-blown stroke.",
        "clinical_correlation": "Patients with TIA often have transient symptoms that resolve completely yet signal an increased risk for future stroke. Prompt initiation of therapy is thus essential to reduce this high early risk.",
        "diagnostic_approach": "Diagnosis involves a careful clinical history and supportive imaging (brain CT or MRI) to rule out acute infarction. Differential diagnoses include migraine with aura, seizures, and other non-vascular events. Risk stratification scores, such as the ABCD2 score, help assess the risk of stroke following a TIA.",
        "classification_and_nosology": "TIAs are classified as cerebrovascular events with clinical symptoms lasting less than 24 hours without acute infarction. They are considered a warning sign and an opportunity for early intervention to prevent stroke.",
        "management_principles": "First-line treatment for high-risk TIA typically involves dual antiplatelet therapy (e.g., aspirin plus clopidogrel) for a short course (typically 21\u201390 days) based on evidence from the CHANCE and POINT trials. Subsequent management includes long-term single antiplatelet therapy, risk factor modification (such as blood pressure and cholesterol control), and lifestyle changes. In pregnancy, low-dose aspirin is generally considered safe, but clopidogrel has less robust data; decisions should weigh risks versus benefits carefully. In lactating patients, aspirin at low doses is acceptable, though caution with clopidogrel is advised.",
        "option_analysis": "Option A (Dual antiplatelet therapy) is correct as studies have demonstrated its efficacy in reducing early recurrent stroke risk in TIA patients. Although other options exist (such as single antiplatelet therapy, anticoagulation, or immediate statin therapy), the evidence clearly supports short-term DAPT in patients with high-risk TIA.",
        "clinical_pearls": "\u2022 TIA is a critical warning sign for stroke; prompt DAPT can significantly reduce recurrence risk.\n\u2022 The CHANCE and POINT trials established the role of DAPT in the early management of TIA.\n\u2022 Risk factor modification remains an essential part of long-term stroke prevention.",
        "current_evidence": "Recent guidelines, supported by the CHANCE and POINT trials, advise the use of dual antiplatelet therapy for a limited period immediately following a high-risk TIA to reduce early recurrent stroke risk."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993319",
    "fields": {
      "question_number": "348",
      "question_text": "Scenario about a patient with A.COM aneurysm, which of the following factor is the most predictive of aneurysm rupture:",
      "options": {
        "A": "Size",
        "B": "Acom location less likely to rupture",
        "C": "Uncontrolled b/p"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Risk stratification in patients with intracranial aneurysms involves identifying features that most strongly predict rupture. Aneurysm size remains a critical factor in many validated scoring systems and risk models.",
        "pathophysiology": "The rupture of an aneurysm is primarily due to hemodynamic stress and wall weakening. Larger aneurysms have increased wall tension, making them more susceptible to rupture. Other factors, such as location and uncontrolled hypertension, also contribute, but size is often the primary measurable predictor.",
        "clinical_correlation": "Aneurysms located at the anterior communicating (ACOM) artery carry an inherently higher risk of rupture even when they are small. However, the overall risk of rupture increases in correlation with aneurysm size, which is used to guide the decision towards surgical or endovascular repair.",
        "diagnostic_approach": "Imaging tests, including CT angiography (CTA), MR angiography (MRA), or digital subtraction angiography (DSA), are used to evaluate aneurysm size, shape, and location. Differential diagnoses include pseudoaneurysms or vascular malformations. Detailed imaging is necessary to discern the rupture risk and plan management.",
        "classification_and_nosology": "Intracranial aneurysms are categorized by size (small, medium, large, giant), morphology (saccular, fusiform), and location (anterior vs. posterior circulation). Risk scoring systems like the PHASES score integrate aneurysm size as the dominant factor in predicting rupture risk.",
        "management_principles": "Management is tiered: small, low-risk aneurysms may be observed with serial imaging, while larger aneurysms (or those with concerning features) are managed with surgical clipping or endovascular coiling. Aggressive blood pressure control is important in all patients. In pregnant or lactating patients, treatment plans are individualized; non-ionizing imaging modalities and careful management of blood pressure and anesthesia risks are prioritized.",
        "option_analysis": "Option A (Size) is correct because numerous studies and risk scoring systems (like PHASES) underscore aneurysm size as the most predictive factor of rupture. Option B is incorrect because aneurysms in the anterior communicating artery are known to have a higher rupture risk rather than being 'less likely' to rupture. Option C (Uncontrolled blood pressure), while a modifiable risk factor for rupture, is less predictive than the inherent structural feature of aneurysm size.",
        "clinical_pearls": "\u2022 Aneurysm size is a key criterion in determining rupture risk; aneurysms above certain thresholds (e.g., >7 mm) are higher risk.\n\u2022 ACOM aneurysms are particularly dangerous and may rupture even at smaller sizes.\n\u2022 Integrating size with other factors (such as morphology and location) improves risk stratification.",
        "current_evidence": "Recent systematic reviews and updated scoring systems continue to emphasize the predictive value of aneurysm size. The PHASES score remains a widely used tool in clinical practice, alongside emerging research that refines risk prediction models."
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
