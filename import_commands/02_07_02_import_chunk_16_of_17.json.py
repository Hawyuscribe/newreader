
# Import batch 2 of 3 from chunk_16_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993218",
    "fields": {
      "question_number": "196",
      "question_text": "What to order next:",
      "options": {
        "A": "Beta 2 glycoprotein antibody",
        "B": "Cholesterol, triglycerides, LDL",
        "C": "NOTCH 3"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses the selection of the appropriate next laboratory investigation in a patient presumably being evaluated for stroke or transient ischemic attack (TIA). The options include tests for dyslipidemia, antiphospholipid syndrome, and CADASIL, each of which is relevant to different underlying etiologies of cerebrovascular disease.",
        "pathophysiology": "Elevated levels of cholesterol, triglycerides, and low-density lipoprotein (LDL) are well-established contributors to atherosclerotic plaque formation, leading to an increased risk for ischemic events. Beta 2 glycoprotein antibodies are associated with an autoimmune-induced hypercoagulable state in antiphospholipid syndrome, while mutations in NOTCH3 are linked with CADASIL, a hereditary arteriopathy affecting small vessels.",
        "clinical_correlation": "In the evaluation of a patient with suspected ischemic stroke or TIA, assessing traditional cardiovascular risk factors is vital. A lipid panel (cholesterol, triglycerides, LDL) is routinely ordered to evaluate atherosclerotic risk. The patient\u2019s clinical context, which likely includes other vascular risk factors, makes option B the most appropriate next step.",
        "diagnostic_approach": "The workup for ischemic cerebrovascular events includes neuroimaging along with laboratory tests to determine risk factors. While Beta 2 glycoprotein antibody tests and genetic screening for NOTCH3 are important in select cases (such as when clinical suspicion for antiphospholipid syndrome or CADASIL is high), the lipid panel is generally the first step given its broad applicability and ease of testing.",
        "classification_and_neurology": "Stroke etiologies are classified under the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. APS falls under 'stroke of other determined etiology' as an acquired hypercoagulable state. Dyslipidemia contributes to large artery atherosclerosis. CADASIL is categorized as a hereditary small vessel disease. The classification emphasizes identifying specific mechanisms to tailor management. Over time, the integration of genetic and immunologic markers has refined nosology, with APS recognized as a systemic autoimmune thrombophilia and CADASIL as a NOTCH3 mutation-driven arteriopathy. Controversies remain regarding the role of screening for antiphospholipid antibodies in all stroke patients, but consensus supports testing in younger patients or those with recurrent unexplained strokes.",
        "classification_and_nosology": "Dyslipidemia is categorized as a modifiable risk factor in both ischemic stroke and cardiovascular disease. CADASIL is a genetic disorder, while antiphospholipid syndrome is an immune-mediated hypercoagulable state.",
        "management_principles": "Based on the results of the lipid panel, lifestyle modifications and pharmacologic treatments (e.g., statins) are initiated as first-line therapy in ischemic stroke risk reduction. In pregnant or lactating patients, the use of statins is contraindicated due to teratogenicity, so alternative therapies and close monitoring are advised.",
        "option_analysis": "Option A (Beta 2 glycoprotein antibody) is specifically used when antiphospholipid syndrome is suspected, and Option C (NOTCH 3) is reserved for cases with a strong family history or clinical suspicion of CADASIL. Option B, the cholesterol panel, is the most appropriate initial test in the absence of specific indicators toward autoimmune or genetic causes.",
        "clinical_pearls": "1. A lipid panel is a cost-effective and essential screening tool in the evaluation of stroke risk factors. 2. Differentiating between atherosclerotic and non-atherosclerotic causes of stroke is key to targeted therapy. 3. Always consider the patient\u2019s overall clinical picture before ordering specialized tests.",
        "current_evidence": "Recent stroke prevention guidelines continue to emphasize aggressive management of dyslipidemia as a cornerstone of ischemic stroke prevention. The utility of a lipid profile in guiding therapy is well supported by current evidence."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993219",
    "fields": {
      "question_number": "197",
      "question_text": "Around 62 yo male patient with history of DM 12 years ago, presented to the ER with history of left side weakness lasted for 10 min then resolved, HTN 150/60. What is the risk of stroke in 90 days?",
      "options": {
        "A": "Low risk 3%",
        "B": "High 18 %",
        "C": "Moderate risk"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question revolves around risk stratification in patients with a transient ischemic attack (TIA). The widely used ABCD2 score includes Age, Blood pressure, Clinical features, Duration of TIA, and Diabetes to predict the short-term risk of stroke following a TIA.",
        "pathophysiology": "A TIA results from transient cerebral ischemia without causing permanent infarction. Factors such as older age, hypertension, diabetes, and clinical features like unilateral weakness contribute to an increased risk of subsequent stroke.",
        "clinical_correlation": "In this 62-year-old male with a 12-year history of diabetes, hypertension, and an episode of left-sided weakness lasting 10 minutes, the ABCD2 score is likely high. Studies have shown that patients with high scores can have a 90-day stroke risk of approximately 18%.",
        "diagnostic_approach": "Assessment involves careful history taking, neurological examination, and calculating the ABCD2 score. Neuroimaging (MRI with diffusion-weighted imaging) is used to rule out infarction. Differential diagnoses include seizure, hypoglycemia, and migraine aura, which are ruled out based on clinical context and imaging findings.",
        "classification_and_neurology": "TIA is classified within the spectrum of ischemic cerebrovascular events, distinct from completed ischemic stroke by the absence of infarction on imaging and transient symptom duration. The traditional time-based definition (<24 hours) has evolved with tissue-based definitions incorporating MRI diffusion-weighted imaging to identify infarction. The ABCD2 score is a widely accepted clinical tool for risk stratification post-TIA, classifying patients into low (0-3), moderate (4-5), and high risk (6-7) categories based on clinical and demographic parameters. This classification helps prioritize urgent diagnostic and therapeutic interventions. The nosology of cerebrovascular disease also includes lacunar strokes, large vessel strokes, and cardioembolic strokes, with TIA often representing a transient manifestation of these underlying pathologies.",
        "classification_and_nosology": "TIAs are classified as transient episodes of neurological dysfunction caused by focal brain ischemia without acute infarction. The ABCD2 score stratifies patients into low, moderate, and high risk for future stroke.",
        "management_principles": "Immediate management includes starting antiplatelet therapy (typically aspirin) and instituting risk factor modification such as blood pressure control, glycemic management, and lipid lowering. Patients with high ABCD2 scores should be admitted for urgent evaluation. In pregnant or lactating patients, low-dose aspirin may be considered if the benefits outweigh the risks, but careful monitoring is needed.",
        "option_analysis": "Option A (Low risk 3%) underestimates the risk given the patient\u2019s multiple risk factors. Option B (High risk 18%) aligns with data from studies correlating a high ABCD2 score with a near 18% risk of stroke within 90 days. Option C (Moderate risk) is too vague and lacks the quantitative specificity provided by current evidence.",
        "clinical_pearls": "1. The ABCD2 score is a quick and useful tool to predict stroke risk after a TIA. 2. Diabetes and hypertension significantly elevate the risk of subsequent stroke. 3. Prompt assessment and intervention can drastically reduce subsequent stroke risk.",
        "current_evidence": "Recent validation studies of the ABCD2 score support its use in clinical practice to identify patients at high risk for stroke. Updated guidelines emphasize rapid secondary prevention measures in patients with high ABCD2 scores to reduce the incidence of early stroke."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993220",
    "fields": {
      "question_number": "198",
      "question_text": "Around 60s yo male patient with 3.5 hr history of sudden left side flaccid weakness, severe dysarthria, facial weakness BP 176/60, afebrile, Plt 45000, BG 300. Presented to the ER, CT brain done was normal. IV TPA given, later the patient develops intracranial hemorrhage. In this case What is the protocol Violations in Community-Based rTPA Stroke Treatment:",
      "options": {
        "A": "Low deficit",
        "B": "Out of TPA window",
        "C": "Plt 45000",
        "D": "??"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests knowledge of the contraindications for administering intravenous tissue plasminogen activator (rTPA) in acute ischemic stroke. The protocol mandates careful patient selection to avoid complications such as hemorrhage.",
        "pathophysiology": "IV tPA facilitates clot dissolution by activating plasminogen to plasmin. However, in patients with significant thrombocytopenia (a low platelet count), the risk of bleeding, particularly intracranial hemorrhage, increases because platelets are essential for clot formation and hemostasis. A platelet count below 100,000/\u00b5L is generally considered an absolute contraindication.",
        "clinical_correlation": "In this case, the patient presented with acute ischemic stroke symptoms within the therapeutic window (3.5 hours). However, his platelet count was only 45,000/\u00b5L\u2014a clear violation of the protocol. Despite the acceptable time frame, the administration of tPA in the context of severe thrombocytopenia predisposed him to intracranial hemorrhage.",
        "diagnostic_approach": "Prior to administration of rTPA, a complete blood count (CBC) is mandatory to screen for contraindications such as coagulopathies and thrombocytopenia. Differential considerations for hemorrhagic complications post-tPA include uncontrolled hypertension and underlying coagulopathies, but in this instance, the low platelet count is the primary red flag.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases (ICD-10 I63) and further subclassified based on etiology (e.g., large artery atherosclerosis, cardioembolism, small vessel occlusion) and clinical syndromes (e.g., lacunar, cortical). The management of ischemic stroke includes reperfusion therapies such as intravenous thrombolysis and endovascular thrombectomy. Protocol violations in thrombolytic therapy relate to deviations from established guidelines that define contraindications and exclusion criteria to minimize adverse events. The American Heart Association/American Stroke Association (AHA/ASA) guidelines provide a standardized framework for thrombolysis eligibility, including platelet count thresholds, blood pressure limits, and time windows. This case exemplifies a protocol violation within the thrombolysis classification, specifically concerning contraindications. Over time, classification systems have evolved to incorporate imaging-based criteria (e.g., perfusion imaging) and expanded time windows under specific conditions, but laboratory contraindications like thrombocytopenia remain consistent. Debates exist regarding the safety of thrombolysis in mild stroke or extended windows, but thrombocytopenia is universally accepted as a contraindication.",
        "classification_and_nosology": "Thrombolytic therapy contraindications are well enumerated in stroke treatment guidelines, with thrombocytopenia being an absolute contraindication. This clearly categorizes the protocol violation for this case.",
        "management_principles": "According to current guidelines, IV tPA should not be administered in the presence of a platelet count less than 100,000/\u00b5L. The first step in managing acute ischemic stroke is a thorough laboratory evaluation. In cases where contraindications are present, alternative management strategies and supportive care should be pursued. For pregnant patients, while rTPA can be considered if absolutely necessary, the same laboratory contraindications apply, underscoring the universal need for caution.",
        "option_analysis": "Option A (Low deficit) is not a contraindication to tPA. Option B (Out of TPA window) is incorrect because the patient presented within the accepted time frame. Option C (Platelet count of 45,000) accurately identifies an absolute contraindication to tPA administration according to established protocols.",
        "clinical_pearls": "1. Always verify laboratory values, especially platelet count, before proceeding with rTPA. 2. Thrombocytopenia is an absolute contraindication to thrombolytic therapy. 3. Strict adherence to stroke treatment protocols is essential to minimize the risk of hemorrhagic complications.",
        "current_evidence": "Updated guidelines from the American Heart Association and American Stroke Association reinforce that a platelet count below 100,000/\u00b5L is a contraindication to tPA therapy. Ongoing research continues to explore optimal patient selection and novel management strategies for hyperacute stroke care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993221",
    "fields": {
      "question_number": "199",
      "question_text": "What is the management:\n-IV thrombolytic thereby is absolute contraindication\n-Mechanical thrombectomy\n-IV thrombolysis\n-IV thrombolysis and mechanical thrombectomy",
      "options": {
        "A": "IV thrombolytic thereby is absolute contraindication",
        "B": "Mechanical thrombectomy",
        "C": "IV thrombolysis",
        "D": "IV thrombolysis and mechanical thrombectomy"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke treatment centers on rapid reperfusion of the affected brain region. The two main modalities are IV thrombolysis and mechanical thrombectomy. When contraindications to IV thrombolysis exist (for example, due to high bleeding risk or recent surgery), mechanical thrombectomy becomes the preferred modality\u2014especially in patients with large vessel occlusion.",
        "pathophysiology": "In ischemic stroke, an occlusive thrombus blocks cerebral blood flow leading to ischemia and potential infarction. IV thrombolytic agents (e.g., alteplase) dissolve clots through enzymatic degradation. However, when there is an absolute contraindication to thrombolysis, mechanical thrombectomy uses endovascular devices (like stent retrievers or aspiration catheters) to physically remove the clot, restoring blood flow to salvageable brain tissue.",
        "clinical_correlation": "Patients with large vessel occlusions often present with sudden focal deficits. Rapid imaging (noncontrast CT followed by CT angiography) is used to rule out hemorrhage and to locate the occlusion. When IV thrombolysis is contraindicated, timely decision\u2010making to perform mechanical thrombectomy is crucial to improve outcomes.",
        "diagnostic_approach": "Initial evaluation includes a noncontrast CT scan to exclude hemorrhage and MRI/CT angiography to assess the location and extent of occlusion. Differential diagnoses include hemorrhagic stroke, stroke mimics (e.g., seizure, migraine), and other ischemic etiologies. Identifying a large vessel occlusion with salvageable penumbra is key to opting for thrombectomy.",
        "classification_and_neurology": "AIS is classified based on etiology (TOAST classification: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined, and undetermined causes) and anatomical location (anterior vs posterior circulation). Treatment classification distinguishes pharmacological reperfusion (IV thrombolysis) from mechanical reperfusion (endovascular thrombectomy). The evolution of stroke classification has integrated imaging and clinical criteria to optimize patient selection for reperfusion therapies. Current nosology emphasizes the importance of LVO identification, as these strokes benefit most from thrombectomy. Controversies remain regarding treatment of distal occlusions and timing beyond traditional windows, but consensus supports thrombectomy for proximal LVOs.",
        "classification_and_nosology": "Acute ischemic strokes are classified based on the underlying etiology (e.g., thrombotic, embolic) and vessel involvement. Large vessel occlusion strokes, which are amenable to mechanical thrombectomy, represent a distinct subgroup within ischemic strokes.",
        "management_principles": "According to the latest AHA/ASA guidelines, eligible acute ischemic stroke patients should receive IV thrombolysis within 4.5 hours if no contraindications exist. In patients with large vessel occlusion or those contraindicated for IV thrombolysis, mechanical thrombectomy is recommended, with trials (e.g., DAWN and DEFUSE-3) extending the treatment window up to 24 hours in selected cases. In pregnant or lactating patients, treatment must be individualized\u2014the risks of systemic thrombolysis are weighed against potential benefits, and thrombectomy may be preferred given lower systemic drug exposure.",
        "option_analysis": "Option A is a statement declaring IV thrombolytics as absolutely contraindicated, which does not represent an active management strategy. Option B (mechanical thrombectomy) is correct because it represents the appropriate management option in a scenario where IV thrombolysis is contraindicated. Option C (IV thrombolysis) would be contraindicated in this context, and Option D (combination therapy) is not applicable since thrombolysis cannot be used.",
        "clinical_pearls": "1. Mechanical thrombectomy has been shown to improve outcomes in patients with large vessel occlusion strokes and contraindications to IV thrombolysis. 2. Rapid imaging and door-to-treatment time are critical for successful reperfusion. 3. In pregnancy, multidisciplinary risk-benefit analysis is essential when considering reperfusion therapy.",
        "current_evidence": "Recent landmark trials such as DAWN and DEFUSE-3 have expanded the window for mechanical thrombectomy and solidified its role in acute stroke management, particularly in patients with large vessel occlusion. Current guidelines recommend thrombectomy in patients who cannot receive IV thrombolysis due to contraindications."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993222",
    "fields": {
      "question_number": "200",
      "question_text": "Around 40 yo male patient presented with history of left side weakness, numbnesses, dysarthria. He found to have stroke. He reported history of migraine headache and cognitive decline. His father died at young age. What will you order in this case?",
      "options": {},
      "correct_answer": "NOTCH",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy) is a hereditary small vessel disease that presents with recurrent strokes, migraine with aura, and cognitive decline. The condition has a strong familial pattern and is confirmed by identifying mutations in the NOTCH3 gene.",
        "pathophysiology": "Mutations in the NOTCH3 gene lead to degeneration and dysfunction of vascular smooth muscle cells, resulting in thickened, fibrotic small arteries. This compromises cerebral blood flow, particularly in the subcortical regions, leading to ischemic injury and the characteristic white matter changes seen on MRI.",
        "clinical_correlation": "Affected individuals typically present in mid-adulthood with a history of migraine (often with aura), subcortical ischemic strokes, and progressively worsening cognitive impairment. A positive family history (e.g., a parent dying young) heightens suspicion for a genetic etiology like CADASIL.",
        "diagnostic_approach": "The diagnostic workup includes brain MRI, which commonly shows white matter hyperintensities in the anterior temporal poles and external capsules. However, definitive diagnosis is achieved via genetic testing for NOTCH3 mutations. Differential diagnoses include other causes of small vessel disease, demyelinating disorders, and mitochondrial cytopathies.",
        "classification_and_neurology": "CADASIL belongs to the group of hereditary cerebral small vessel diseases. It is classified under monogenic stroke syndromes with autosomal dominant inheritance. The broader nosological framework of stroke includes: - Large artery atherosclerosis - Cardioembolic stroke - Small vessel occlusion (including sporadic and hereditary forms) - Other determined etiologies (e.g., vasculitis, dissection) - Undetermined etiology  Hereditary small vessel diseases like CADASIL are distinguished by genetic testing and characteristic clinical/imaging features. The classification has evolved with advances in molecular genetics, allowing for more precise diagnosis. Other hereditary small vessel diseases include CARASIL (recessive NOTCH3 mutations), COL4A1-related disorders, and Fabry disease, each with distinct genetic and clinical profiles.  Controversies exist regarding the spectrum of NOTCH3 mutations and phenotypic variability, but CADASIL remains the prototypical hereditary small vessel disease.",
        "classification_and_nosology": "CADASIL is classified as a hereditary cerebral small vessel disease with autosomal dominant inheritance. It is the most common monogenic form of stroke and vascular dementia.",
        "management_principles": "There is no curative treatment for CADASIL; management focuses on controlling vascular risk factors, symptomatic treatment, and secondary stroke prevention. Antiplatelet agents and blood pressure management are often employed. Genetic counseling is recommended. In pregnant or lactating patients, careful blood pressure management is essential and medications should be chosen with safety profiles in mind.",
        "option_analysis": "The correct answer is genetic testing for the NOTCH3 mutation, as it directly confirms the diagnosis of CADASIL. Echocardiography is more useful when an embolic source is suspected, and testing for antiphospholipid antibodies is pertinent in acquired hypercoagulable states, neither of which aligns with the classic clinical picture of CADASIL.",
        "clinical_pearls": "1. CADASIL should be suspected in young to middle-aged patients with a combination of strokes, migraine with aura, and a positive family history. 2. The anterior temporal lobe white matter lesions on MRI are a helpful radiological clue. 3. There is currently no disease-modifying treatment for CADASIL; management is supportive.",
        "current_evidence": "Contemporary research continues to focus on elucidating the molecular mechanisms in CADASIL with the aim of developing targeted therapies. Meanwhile, management remains symptomatic and preventive, with genetic testing serving as the gold standard for diagnosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993223",
    "fields": {
      "question_number": "201",
      "question_text": "This is 24 yo female patient with k/c of aneurysm with history right side headache and right pupil dilatation. On exam right pupil dilated, with impaired right eye adduction, CT brain showed ruptured aneurysm. Where is the location of aneurysm?",
      "options": {
        "A": "Right PCOM",
        "B": "Right ICR",
        "C": "Right ACOM",
        "D": "Right MCA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Intracranial aneurysms are dilations or outpouchings of arterial walls, often occurring at branch points. Aneurysms in the posterior communicating (PCOM) segment are notorious for causing oculomotor nerve (CN III) palsies due to their anatomical proximity.",
        "pathophysiology": "A PCOM aneurysm can enlarge and compress the adjacent oculomotor nerve, which carries parasympathetic fibers responsible for pupil constriction and motor fibers that mediate most extraocular movements. Compression leads to a dilated pupil (mydriasis), ptosis, and impaired ocular movements\u2014especially affecting the medial rectus, which is responsible for adduction.",
        "clinical_correlation": "Clinically, patients with a ruptured PCOM aneurysm may present with sudden headache, signs of subarachnoid hemorrhage, and a CN III palsy. The presence of a dilated pupil and impaired adduction in the same eye strongly suggests compression by a nearby aneurysm.",
        "diagnostic_approach": "Initial evaluation typically includes a noncontrast CT scan to identify hemorrhage and a CT angiogram (or digital subtraction angiography) to localize the aneurysm. Differential diagnoses include other aneurysm locations (such as anterior communicating or middle cerebral arteries), which less commonly produce isolated CN III dysfunction.",
        "classification_and_neurology": "Intracranial aneurysms are classified based on location, morphology, and etiology. The most common classification system is by arterial territory: anterior circulation (including ACOM, PCOM, MCA, ICA) and posterior circulation aneurysms. PCOM aneurysms belong to the anterior circulation group, specifically at the junction of the internal carotid artery and posterior communicating artery. Morphologically, aneurysms can be saccular (berry), fusiform, or dissecting, with saccular being most common in PCOM. Etiologically, aneurysms are classified as congenital, degenerative, traumatic, or mycotic; congenital and degenerative are most common. The International Study of Unruptured Intracranial Aneurysms (ISUIA) and the Hunt and Hess grading system guide prognosis and management. No major controversies exist regarding the classification of PCOM aneurysms; however, some debate persists about the best treatment modality depending on size and rupture status.",
        "classification_and_nosology": "Intracranial aneurysms are classified by their location (e.g., PCOM, ACOM, MCA) and morphology (saccular vs. fusiform). PCOM aneurysms are a common subtype and have specific clinical implications due to their propensity to compress the oculomotor nerve.",
        "management_principles": "Management of a ruptured aneurysm generally involves securing the aneurysm via surgical clipping or endovascular coiling to prevent rebleeding. The choice of procedure depends on aneurysm size, neck morphology, and patient-specific factors. In pregnant patients, endovascular coiling is often favored to minimize surgical risks and anesthesia exposure, though the risks of radiation must be addressed through shielding and minimizing exposure.",
        "option_analysis": "Option A (Right PCOM) is correct, as a PCOM aneurysm is classically associated with CN III palsy, manifesting with a dilated pupil and impaired adduction on the same side. Options B, C, and D refer to aneurysm locations that are less likely to cause the specific pattern of oculomotor dysfunction seen in this patient.",
        "clinical_pearls": "1. A \u2018blown pupil\u2019 (dilated and unresponsive) in the setting of subarachnoid hemorrhage is highly suggestive of a PCOM aneurysm. 2. Immediate neuroimaging and vascular studies are critical in the management of suspected aneurysmal rupture. 3. Endovascular services have increasingly become the mainstay in managing many cerebral aneurysms.",
        "current_evidence": "Recent trials and meta-analyses continue to support the efficacy and safety of endovascular coiling for PCOM aneurysms. Updated guidelines advocate for early intervention in ruptured aneurysms to reduce the risk of rebleeding and improve outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993224",
    "fields": {
      "question_number": "202",
      "question_text": "Which of the following arteries arise from the internal carotid artery?",
      "options": {
        "A": "(AICA), Option B (PICA), and Option D (SCA) originate from the basilar or vertebral arteries. Option C (PCA) is correct because, in the setting of a fetal"
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "The cerebral arterial circulation is divided into the anterior and posterior systems. Although the posterior cerebral artery (PCA) normally arises from the basilar artery, a common anatomical variant known as the fetal-type PCA arises directly from the internal carotid artery (ICA). This variant essentially links the PCA directly to the ICA.",
        "pathophysiology": "During fetal development, the PCA originates from the ICA. In many adults, the PCA subsequently shifts its origin to the basilar artery; however, in a significant proportion of individuals, the fetal configuration persists. This means that the PCA\u2014at least in its proximal segment\u2014arises from the ICA, influencing cerebral hemodynamics and collateral circulation patterns.",
        "clinical_correlation": "Recognizing vascular variants is important when evaluating stroke patients or planning neurosurgical/endovascular procedures. A fetal origin of the PCA can alter perfusion dynamics, and in cases of ICA occlusion, the ipsilateral PCA may be more directly affected.",
        "diagnostic_approach": "A detailed vascular imaging study (CT angiography or MR angiography) is used to delineate the circle of Willis architecture and identify variants such as a fetal-type PCA. Differential diagnosis in this context involves verifying the origins of other cerebellar arteries, which typically arise from the vertebrobasilar system.",
        "classification_and_neurology": "The cerebral arteries are classified based on their origin into the anterior and posterior circulations. The anterior circulation arises from the internal carotid arteries and includes the ACA, MCA, anterior choroidal artery, and PCoA. The posterior circulation arises from the vertebral arteries, which merge to form the basilar artery, giving rise to the AICA, SCA, and PCA. The Circle of Willis is the anastomotic ring connecting these circulations. This classification is essential in cerebrovascular disease taxonomy and stroke syndromes. Current consensus classifies strokes as anterior or posterior circulation strokes, guiding diagnostic and therapeutic approaches. There is broad agreement on this classification, with minor variations in nomenclature related to anatomical variants.",
        "classification_and_nosology": "Cerebral arteries are grouped by their typical origins\u2014ICA derivatives (such as the MCA, ACA, and in cases of fetal-type PCA) versus vertebrobasilar derivatives (like AICA, PICA, and SCA). The fetal PCA variant is an example of intraspecies anatomical variation.",
        "management_principles": "While this anatomical variant does not typically alter immediate management in ischemic stroke beyond diagnostic awareness, it is critical for surgical planning. In pregnant or lactating patients, any imaging that involves radiation must be carefully managed; non-ionizing modalities (like MR angiography) might be preferred when safe and available.",
        "option_analysis": "Option A (AICA), Option B (PICA), and Option D (SCA) originate from the basilar or vertebral arteries. Option C (PCA) is correct because, in the setting of a fetal-type PCA, it arises from the ICA. Even though the PCA classically comes from the basilar artery in adults, the fetal variant is common and functionally connects the PCA to the ICA.",
        "clinical_pearls": "1. The fetal-type PCA is present in roughly 10%-30% of people and is important in cerebral hemodynamics. 2. Recognizing this variant can help explain unusual stroke patterns in the posterior circulation. 3. Always review the circle of Willis anatomy in advanced neuroimaging assessments.",
        "current_evidence": "Recent vascular imaging studies continue to highlight the prevalence and clinical significance of the fetal PCA variant. This anatomical insight is increasingly important in planning interventions for stroke patients and in understanding collateral circulation dynamics."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993225",
    "fields": {
      "question_number": "203",
      "question_text": "Elderly patient presented to the ER with a history of visual disturbances. On the exam she has right homonymous hemianopia. She can write but not be able to read. CT brain done. What is the location of infarction?",
      "options": {
        "A": "(Splenium of the corpus callosum) is correct because the lesion disrupts the transfer of visual information between hemispheres, producing alexia without agraphia. Option b (Right occipital lobe) is incorrect because a right occipital infarct would cause a left",
        "C": "(Left occipital lobe) would typically result in an inability to read and write (due to more extensive involvement of language and visual areas) rather than the selective loss of reading."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the recognition of the classic disconnection syndrome known as alexia without agraphia. In this syndrome, the patient loses the ability to read while retaining the ability to write because of a disruption in the transfer of visual information from one hemisphere (typically the intact right occipital cortex) to the language centers in the dominant left hemisphere. The splenium of the corpus callosum is the key conduit for this interhemispheric transfer.",
        "pathophysiology": "Infarction in the region of the splenium (typically in the territory of the posterior cerebral artery) prevents visual information captured by the right occipital lobe from reaching the dominant (usually left) language areas. Although the classic lesion often involves the left occipital lobe plus the splenium, isolated splenial involvement can produce a similar syndrome by disconnecting the intact visual field input from language processing centers. The resulting right homonymous hemianopia reflects involvement of the left visual pathway.",
        "clinical_correlation": "The patient\u2019s symptom of right homonymous hemianopia indicates a lesion affecting the left visual pathway, while the preserved ability to write despite the inability to read is a hallmark of alexia without agraphia. The syndrome is attributed to a disconnection between the visual recognition centers in the right occipital region and the left-sided language areas.",
        "diagnostic_approach": "Neuroimaging is essential. A CT scan can identify infarcts in the posterior circulation territory. Follow\u2010up MRI (especially diffusion\u2010weighted imaging) helps delineate the exact location and extent of the infarction. Differential diagnoses to consider include isolated occipital lobe infarcts (which may impair both reading and writing) and other disconnection syndromes from lesions in the dominant hemisphere.",
        "classification_and_neurology": "This clinical syndrome falls under the category of cerebrovascular accidents (ischemic strokes) affecting the posterior circulation territory. The infarct location is within the territory of the posterior cerebral artery (PCA), specifically involving the splenium of the corpus callosum. The syndrome of alexia without agraphia is a classic disconnection syndrome, categorized under higher cortical dysfunctions (agnosias and aphasias) secondary to stroke. The classification of stroke by vascular territory (anterior vs. posterior circulation) and by clinical syndromes (visual field defects, language disturbances) applies here. While classic stroke classifications focus on cortical vs. subcortical infarcts, this syndrome highlights the importance of white matter tract involvement (splenium) leading to disconnection phenomena. There is consensus that alexia without agraphia results from splenial lesions disrupting interhemispheric visual-linguistic transfer.",
        "classification_and_nosology": "This syndrome falls under stroke syndromes in the posterior cerebral artery distribution. It is often classified as a disconnection syndrome (sometimes referred to as Dejerine syndrome) because it reflects a disruption in the interhemispheric communication necessary for integrated function.",
        "management_principles": "Acute management follows ischemic stroke protocols, including assessment for reperfusion therapies within the therapeutic window (IV thrombolysis, endovascular thrombectomy if indicated by large vessel occlusion). Secondary prevention (antiplatelet therapy, statins, risk factor management) is key. In special populations such as pregnancy or lactation, the decision to use tPA is carefully balanced against risks, but the principles of rapid neuroimaging and reperfusion remain similar when criteria are met.",
        "option_analysis": "Option a (Splenium of the corpus callosum) is correct because the lesion disrupts the transfer of visual information between hemispheres, producing alexia without agraphia. Option b (Right occipital lobe) is incorrect because a right occipital infarct would cause a left-sided visual deficit. Option c (Left occipital lobe) would typically result in an inability to read and write (due to more extensive involvement of language and visual areas) rather than the selective loss of reading.",
        "clinical_pearls": "1. Alexia without agraphia is a rare disconnection syndrome most often seen with a left occipital and splenial infarct. 2. Preservation of writing despite loss of reading should prompt evaluation for a splenium lesion.",
        "current_evidence": "Recent stroke guidelines emphasize the importance of rapid imaging (CT/MRI) to localize infarcts and guide reperfusion therapy. Although the classical description involves both the left occipital lobe and splenium, advanced imaging has shown that isolated splenial involvement can suffice to produce the syndrome."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993226",
    "fields": {
      "question_number": "204",
      "question_text": "AIS patient within the window with platelet count of 45, he was given tPA which resulted in intracranial hemorrhage? What violation to the AIS treatment protocol was done?",
      "options": {
        "A": "(Out of the tPA window) is incorrect because the patient was within the therapeutic time frame. Option b (Platelet count 45,000) is correct as administering tPA in the presence of significant thrombocytopenia is an established contraindication and likely led to the intracranial hemorrhage."
      },
      "correct_answer": "b",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question focuses on the proper application of thrombolytic therapy in acute ischemic stroke (AIS) and the importance of adhering to contraindications. A thorough understanding of tPA contraindications is crucial to prevent serious complications such as intracranial hemorrhage.",
        "pathophysiology": "tPA works by promoting fibrinolysis. However, in patients with thrombocytopenia (e.g., a platelet count of 45,000/mm\u00b3), the risk of bleeding is augmented due to impaired hemostasis. This predisposes them to hemorrhagic conversion, including intracranial hemorrhage.",
        "clinical_correlation": "In the acute management of AIS, an inappropriately low platelet count (below the recommended threshold of 100,000/mm\u00b3) is an absolute contraindication to tPA administration because it increases hemorrhagic risk. Recognizing and correcting laboratory abnormalities before thrombolysis is essential in clinical practice.",
        "diagnostic_approach": "Before administering tPA, a careful review of laboratory values including complete blood count (CBC), coagulation profile, and imaging to rule out hemorrhage is mandatory. Differentials for bleeding risk include coagulopathies from anticoagulant use or liver dysfunction, which must be ruled out before proceeding with thrombolysis.",
        "classification_and_neurology": "AIS is classified within the cerebrovascular disease spectrum and further subclassified by etiology using systems such as TOAST (Trial of Org 10172 in Acute Stroke Treatment), which categorizes strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. Treatment protocols for AIS, including thrombolytic therapy, are governed by guidelines from professional bodies such as the American Heart Association/American Stroke Association (AHA/ASA). These guidelines define absolute and relative contraindications for intravenous thrombolysis to standardize care and minimize harm. Thrombocytopenia is an absolute contraindication due to the risk of hemorrhage. The classification of treatment violations includes administration outside the therapeutic window, presence of contraindications like low platelet count, recent surgery, or bleeding disorders.",
        "classification_and_nosology": "Contraindications to IV tPA are categorized as absolute or relative. Thrombocytopenia (platelet count <100,000/mm\u00b3) falls under the absolute contraindications per current guidelines.",
        "management_principles": "The first step in the management of AIS is to ascertain eligibility for IV tPA by confirming that all contraindications (including a platelet count <100,000/mm\u00b3) are absent. When contraindications are identified, alternative management strategies such as antiplatelet therapy and supportive care are pursued. In special populations such as pregnant or lactating women, the same lab criteria apply with careful consideration given to the risks and benefits of tPA use.",
        "option_analysis": "Option a (Out of the tPA window) is incorrect because the patient was within the therapeutic time frame. Option b (Platelet count 45,000) is correct as administering tPA in the presence of significant thrombocytopenia is an established contraindication and likely led to the intracranial hemorrhage.",
        "clinical_pearls": "1. Always review the lab values, especially platelet count, before initiating thrombolytic therapy in AIS. 2. A platelet count below 100,000/mm\u00b3 is an absolute contraindication for tPA, significantly increasing the risk of hemorrhage.",
        "current_evidence": "The latest American Heart Association/American Stroke Association (AHA/ASA) guidelines underscore the importance of adhering to strict laboratory thresholds to minimize hemorrhagic complications associated with tPA. Ongoing studies continue to evaluate the balance between risk and benefit in borderline cases, but current recommendations remain clear."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993227",
    "fields": {
      "question_number": "205",
      "question_text": "Patient had mild trauma as he can not see the left side of the road. Presented with visual deficit and reported a similar headache at age 15 years occurring for about 24 hours?",
      "options": {
        "A": "(PRES) is incorrect because PRES is typically associated with severe hypertension, seizures, and encephalopathy rather than isolated visual deficits following mild trauma. Option b (RCVS) is less likely given its hallmark presentation with thunderclap headaches and diffuse vasospasm, not isolated visual symptoms. Option c (Vertebral artery dissection) is correct as it best explains the temporal relationship with trauma and the neurological presentation."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses the diagnosis of vertebral artery dissection, a vascular injury that can occur even after minor trauma. Recognizing the clinical cues such as focal neurological deficits in the context of trauma is essential to prompt diagnosis and management.",
        "pathophysiology": "Vertebral artery dissection involves an intimal tear that can lead to the formation of a thrombus, subsequent embolization, or local ischemia in the posterior circulation. Mild trauma, particularly involving the neck, can trigger this process. The resultant ischemia can produce focal deficits such as visual disturbances if the occipital lobe or associated structures are affected.",
        "clinical_correlation": "The patient\u2019s complaint of not being able to see the left side of the road, along with a history of a similar prolonged headache (which may hint at a predisposition to vascular issues), is consistent with vertebral artery dissection. The relatively minor trauma described aligns with the known risk factors for this condition.",
        "diagnostic_approach": "Imaging studies, particularly CT angiography (CTA) or MR angiography, are critical for diagnosing vertebral artery dissection. Differential diagnoses include Posterior Reversible Encephalopathy Syndrome (PRES), typically associated with acute hypertension and seizures, and Reversible Cerebral Vasoconstriction Syndrome (RCVS), which presents with thunderclap headaches and multifocal arterial narrowing on angiography.",
        "classification_and_neurology": "Vertebral artery dissection is classified under cervicocephalic arterial dissections, a subset of arterial dissections affecting the carotid and vertebral arteries. It falls within the broader category of ischemic stroke etiologies, specifically under arterial dissection-related strokes. Nosologically, it is a vascular disorder characterized by traumatic or spontaneous intimal injury leading to intramural hematoma and ischemia. The classification systems (such as TOAST for stroke subtypes) categorize arterial dissection as a distinct cause of stroke. Over time, improved imaging techniques have refined the diagnosis and classification of dissections. Controversies remain regarding the optimal classification of spontaneous versus traumatic dissections and their risk stratification.",
        "classification_and_nosology": "Vertebral artery dissection is a type of cervicocephalic arterial dissection. It is categorized based on etiology (traumatic vs. spontaneous) and the vascular territory involved.",
        "management_principles": "The mainstay of treatment for vertebral artery dissection involves antithrombotic therapy (either antiplatelet agents or anticoagulation) to prevent thromboembolic events. Endovascular intervention is reserved for cases where medical management fails or there is significant ongoing ischemia. In pregnant or lactating patients, low molecular weight heparin is generally preferred due to its safety profile.",
        "option_analysis": "Option a (PRES) is incorrect because PRES is typically associated with severe hypertension, seizures, and encephalopathy rather than isolated visual deficits following mild trauma. Option b (RCVS) is less likely given its hallmark presentation with thunderclap headaches and diffuse vasospasm, not isolated visual symptoms. Option c (Vertebral artery dissection) is correct as it best explains the temporal relationship with trauma and the neurological presentation.",
        "clinical_pearls": "1. Vertebral artery dissection should be considered in patients presenting with posterior circulation symptoms following even minor cervical trauma. 2. CTA is the imaging modality of choice for early detection of arterial dissections.",
        "current_evidence": "Recent literature and guidelines emphasize prompt recognition of vertebral artery dissection, as early antithrombotic therapy has been shown to reduce the risk of stroke. Advances in imaging techniques continue to improve diagnostic accuracy, shaping current management practices."
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
