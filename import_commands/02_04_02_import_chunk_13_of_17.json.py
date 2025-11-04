
# Import batch 2 of 3 from chunk_13_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993514",
    "fields": {
      "question_number": "37",
      "question_text": "Clear scenario of anterior choroidal artery infarction, they brought VF suggestive of it",
      "options": {
        "A": "anterior choroidal artery infarction"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Anterior choroidal artery infarction is a specific type of ischemic stroke involving the small artery that supplies portions of the internal capsule, optic tract, lateral geniculate body, and other deep brain structures. Clinically, it is characterized by a triad including contralateral hemiparesis, hemisensory loss, and a visual field defect (often a homonymous hemianopia), making the diagnosis suggestion clear when these features are present.",
        "pathophysiology": "Occlusion of the anterior choroidal artery leads to ischemic damage in its vascular territory. The infarct typically affects the posterior limb of the internal capsule (resulting in motor and sensory deficits) and the optic radiations/tract (leading to visual field deficits). This infarction is often thromboembolic in nature, related either to atherosclerotic disease or cardioembolic events.",
        "clinical_correlation": "Patients with anterior choroidal artery stroke often present acutely with neurological deficits that include weakness and numbness on the contralateral side as well as a visual field defect corresponding to the loss of visual information processing in the affected optical pathway. The presence of visual field findings in tandem with motor/sensory deficits strongly supports the diagnosis.",
        "diagnostic_approach": "Diagnosis is based on a combined assessment of clinical presentation and neuroimaging (CT, MRI, and angiography). Differential diagnoses include other vascular territories such as middle cerebral artery or posterior cerebral artery infarctions, as well as lacunar strokes; however, the classic combination seen in anterior choroidal strokes helps in distinguishing it. A focused neurological exam assessing motor strength, sensory function, and visual fields is critical in directing imaging studies for confirmation.",
        "classification_and_neurology": "Anterior choroidal artery infarction is classified under ischemic strokes within the cerebrovascular disease taxonomy. According to the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification, it is categorized as a large artery atherosclerosis or cardioembolism subtype depending on etiology. The AChA infarction is a subtype of lacunar or subcortical infarcts but differs from classic small vessel lacunes due to its vascular territory and clinical presentation. The classification of stroke by vascular territory is essential for clinical localization and management. Over time, neuroimaging advances have refined the understanding of AChA infarction as a distinct clinical and radiological entity. There is some debate about the overlap between AChA and MCA or PCA infarcts, but consensus supports recognizing AChA territory infarcts based on clinical and imaging criteria. This classification aids in prognosis and therapeutic decision-making.",
        "classification_and_nosology": "Anterior choroidal artery infarction is classified under ischemic strokes and is considered a lacunar-type or small-vessel stroke in terms of size, though its clinical presentation is distinct. It is important to recognize this entity as a separate vascular syndrome due to its characteristic distribution and clinical features.",
        "management_principles": "Acute management involves assessing eligibility for reperfusion therapies such as intravenous thrombolysis or endovascular treatment if within the therapeutic window. Subsequent management includes antiplatelet therapy and secondary prevention strategies (including risk factor management such as hypertension, diabetes, and dyslipidemia control). For pregnant or lactating patients, treatment choices require special considerations: low-dose aspirin is generally acceptable during pregnancy, and thrombolytic therapy may be considered when potential benefits outweigh risks after consultation with multidisciplinary teams. Individualized risk\u2013benefit analysis is crucial in these populations.",
        "option_analysis": "In the presented MCQ, Option A ('anterior choroidal artery infarction') is the appropriate answer because the clinical scenario, which includes a visual field defect along with associated neurological deficits, matches the typical presentation of an infarction in the anterior choroidal artery territory. Although the other options are not listed, the information given solidly supports Option A.",
        "clinical_pearls": "Recognize the classic triad of deficits (motor, sensory, and visual) in anterior choroidal strokes. Immediate neuroimaging is essential to confirm the diagnosis, and early reperfusion can significantly improve outcomes. In special populations such as pregnant or lactating patients, adapt standard stroke management protocols with extra care regarding medication safety.",
        "current_evidence": "Recent guidelines and studies continue to support the early use of reperfusion therapy in acute ischemic stroke, including those with anterior choroidal involvement. Updated protocols emphasize rapid diagnosis and tailored management, especially for vulnerable groups such as pregnant women, where low-dose aspirin and careful consideration of thrombolytic therapy are supported by current evidence."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993419",
    "fields": {
      "question_number": "4",
      "question_text": "pt suddenly explaned to his wife seeing animals and fade after while pt loss consciousness / EMd arrived. Take him to the hospital intubation done. Attache Ct scan. New left occipital stroke. What you will do? Pt presneted with window not mention bt writeen sudden and within 1 hr",
      "options": {
        "A": "cta",
        "B": "EEG",
        "C": "tpa"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case describes an acute ischemic stroke evidenced by a new left occipital lesion on CT scan, with a presentation that is sudden and within the thrombolytic time window (approximately 1 hour). The rationale for administering IV tPA is based on the principle that early reperfusion therapy can salvage ischemic but still viable brain tissue, thereby improving outcomes.",
        "pathophysiology": "Acute ischemic stroke is caused by occlusion of a cerebral artery\u2014in this scenario, likely a branch supplying the occipital lobe. This occlusion leads to a cessation of blood flow, resulting in energy failure, neuronal injury, and infarction in the affected area. tPA (tissue plasminogen activator) works by enzymatically breaking down the fibrin clot, restoring perfusion to the penumbral area surrounding the infarct core.",
        "clinical_correlation": "Visual hallucinations (e.g., seeing animals) can occur with occipital lobe involvement. The subsequent loss of consciousness could be related to the evolution of the stroke or secondary complications. Since the patient is intubated, airway protection has been addressed, enabling the safe administration of thrombolytic therapy.",
        "diagnostic_approach": "Initial evaluation with a non-contrast CT scan is critical to exclude hemorrhage in patients suspected of having a stroke. Once an acute ischemic stroke is confirmed and no contraindications are present, especially within the therapeutic window, IV tPA is indicated. Advanced imaging such as CTA is reserved for cases where vascular occlusion details are required, often in the context of considering mechanical thrombectomy.",
        "classification_and_neurology": "Ischemic strokes are classified by etiology using systems like the TOAST criteria, which include large-artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. This patient\u2019s stroke likely falls under large-artery or cardioembolic ischemic stroke depending on further workup. The classification aids in secondary prevention but does not delay acute management. The acute ischemic stroke diagnosis is based on clinical presentation and imaging, distinguishing it from hemorrhagic stroke and stroke mimics. The classification of stroke management follows guidelines that stratify patients based on time from symptom onset and imaging findings.",
        "classification_and_nosology": "This entity falls under the classification of acute ischemic stroke. Within this, strokes can be stratified by the underlying pathogenesis (e.g., thrombotic vs. embolic). In this case, the occlusion of a branch of the posterior cerebral circulation (affecting the occipital region) is most likely thrombotic.",
        "management_principles": "According to current guidelines (AHA/ASA), IV tPA is recommended for patients with acute ischemic stroke who present within 3 to 4.5 hours of symptom onset, provided there are no contraindications. Since the patient presented within 1 hour and imaging confirmed an ischemic stroke with no evidence of hemorrhage, IV tPA is indicated. In pregnant or lactating patients, tPA is not contraindicated when the benefits outweigh the potential risks; multidisciplinary consultation is advised to guide therapy.",
        "option_analysis": "Option A (CTA) is used for vascular imaging but is not mandatory when the diagnosis of ischemia is already established and the patient is within the therapeutic window. Option B (EEG) would only be relevant if a seizure were the primary concern. Option C (TPA) is the appropriate intervention given the acute ischemic findings within the necessary time frame. Option D is absent and does not contribute to management decision-making in this scenario.",
        "clinical_pearls": "\u2022 Rapid assessment and imaging are crucial in stroke management \u2013 'time is brain.'\n\u2022 A non-contrast CT scan is the first-line investigation to rule out hemorrhage before thrombolysis.\n\u2022 IV tPA should be administered as soon as possible in eligible patients to optimize neurological outcomes.\n\u2022 In special populations such as pregnant or lactating patients, tPA can be considered after balancing potential risks and benefits.",
        "current_evidence": "Recent clinical trials and guidelines from the AHA/ASA have reinforced that the benefits of timely IV tPA in acute ischemic stroke extend even more when administered early. Consensus supports its use in patients with confirmed ischemic stroke within the therapeutic window. Although data on tPA use in pregnancy is limited, case reports and expert recommendations suggest that it can be safely administered when clearly indicated, with appropriate monitoring and multidisciplinary management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993430",
    "fields": {
      "question_number": "5",
      "question_text": "Male 56 years old male pt found in teh house with decreas level of consuos Last tome seen normal 1 day back Brain ct scan showed:",
      "options": {
        "A": "tpa",
        "B": "admission to stroke unite"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Stroke management is highly time\u2010sensitive. For acute ischemic stroke, the decision to administer treatments like tPA depends on the time since onset, with a narrow window (typically within 3-4.5 hours). In patients presenting outside this window, as in this case (last seen normal one day ago), the best management is supportive care in a stroke unit.",
        "pathophysiology": "Acute ischemic stroke results from arterial occlusion leading to brain tissue ischemia and infarction. The cascade of excitotoxicity, inflammation, and eventual cell death occurs over hours. When the patient is found with decreased consciousness long after the onset, the infarct may be well established and not amenable to reperfusion therapies.",
        "clinical_correlation": "A 56-year-old with decreased level of consciousness and a delayed presentation is unlikely to benefit from thrombolytics since the window for maximum efficacy has closed. Admission to a stroke unit allows for monitoring of complications such as edema, hemorrhagic transformation, and management of secondary stroke prevention.",
        "diagnostic_approach": "Imaging studies (typically a non-contrast CT scan) are used to differentiate hemorrhagic from ischemic stroke. Differential diagnoses include intracerebral hemorrhage, stroke mimics (e.g., seizure postictal state, hypoglycemia), and other causes of altered mental status. The timing (last known well time) is crucial in guiding the therapeutic approach.",
        "classification_and_neurology": "Ischemic stroke is classified within the broader cerebrovascular disease category. The TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system categorizes ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This classification guides diagnostic evaluation and secondary prevention strategies. The diagnosis of acute ischemic stroke is clinical, supported by neuroimaging to differentiate from hemorrhagic stroke and stroke mimics. The concept of stroke mimics (e.g., seizures, hypoglycemia) is important in acute management decisions. Over time, classification systems have evolved to incorporate advanced imaging and biomarkers, but the TOAST system remains widely used in clinical practice and research.",
        "classification_and_nosology": "Ischemic strokes are categorized by mechanisms such as thrombotic, embolic, or small vessel (lacunar) strokes using systems like the TOAST classification. In this patient, the risk factors and presentation favor an ischemic event.",
        "management_principles": "Since the patient is outside the thrombolytic window, first-line management involves supportive care: admission to a specialized stroke unit where multidisciplinary care improves outcomes. Secondary prevention with antiplatelet agents, statins, and risk factor modification is initiated. In pregnancy and lactation, while tPA may be used in selected cases within the window, in patients beyond the window, supportive care in a stroke unit remains standard and is safe.",
        "option_analysis": "Option A (tPA) is incorrect because the therapeutic window has elapsed. Option B (admission to a stroke unit) is the correct answer as it aligns with current guidelines in managing patients with established stroke outside the tPA window. Options C and D are not provided or applicable.",
        "clinical_pearls": "1. Always ascertain the 'last known well' time to determine eligibility for thrombolysis. 2. Stroke units have been shown to significantly improve functional outcomes in stroke patients.",
        "current_evidence": "Recent AHA/ASA guidelines reinforce the importance of dedicated stroke unit care for all patients with acute ischemic stroke, particularly when reperfusion therapy is not an option. Studies continue to validate improved outcomes with organized multidisciplinary care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_9.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993409",
    "fields": {
      "question_number": "6",
      "question_text": "What you can see with RCVS",
      "options": {
        "A": "Low glucose"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Reversible Cerebral Vasoconstriction Syndrome (RCVS) is characterized by sudden, severe ('thunderclap') headaches and reversible narrowing of cerebral arteries. The syndrome is often triggered by vasoactive substances or physical stressors.",
        "pathophysiology": "RCVS involves transient dysregulation of cerebral arterial tone, leading to multifocal, segmental vasoconstriction. The exact mechanism is not fully understood, but sympathetic overactivity, endothelial dysfunction, and hormonal influences (especially postpartum) are implicated.",
        "clinical_correlation": "Patients with RCVS typically present with thunderclap headaches, which can recur over days to weeks. Neurological deficits may occur if the vasoconstriction leads to ischemia. Unlike other vasculopathies, RCVS is self-limited and reversible over time.",
        "diagnostic_approach": "Diagnosis is primarily radiological. CTA, MRA, or digital subtraction angiography may reveal a 'string-of-beads' appearance of alternating constricted and dilated segments. Differential diagnoses include primary angiitis of the central nervous system (PACNS), subarachnoid hemorrhage, and migraine variants; PACNS tends to have a more insidious onset and is not self-limited.",
        "classification_and_neurology": "RCVS is classified under non-inflammatory cerebral vasculopathies and is part of the broader group of transient vasospastic disorders. It is distinct from primary angiitis of the central nervous system (PACNS), which is an inflammatory vasculitis.  The diagnosis is based on clinical and radiographic criteria, such as the RCVS2 score, which integrates clinical features and angiographic findings to differentiate RCVS from CNS vasculitis.  Historically, RCVS was often confused with PACNS, leading to inappropriate immunosuppressive treatment. Advances in imaging and clinical characterization have led to consensus criteria distinguishing these entities. The International Classification of Headache Disorders (ICHD-3) recognizes thunderclap headache attributed to RCVS as a distinct headache disorder.  Controversies remain regarding overlap syndromes and the relationship between RCVS and PRES, as well as their shared pathophysiological mechanisms.",
        "classification_and_nosology": "RCVS is classified as a non-inflammatory vasculopathy distinct from primary CNS angiitis. It is usually categorized within reversible conditions of cerebral arterial dysregulation.",
        "management_principles": "First-line management includes supportive care and calcium channel blockers (e.g., nimodipine) to alleviate vasospasm. Avoiding triggers and symptomatic management are important. In pregnancy and lactation, management is similar; calcium channel blockers can be used with careful monitoring, and supportive measures remain the mainstay.",
        "option_analysis": "Although the provided options are incomplete, Option A (Low glucose) is not a recognized feature of RCVS. Marked Answer B is presumed to describe the classic angiographic finding (multifocal segmental vasoconstriction or 'string-of-beads' appearance), which is correct. Other unlisted options likely do not match the hallmark features of RCVS.",
        "clinical_pearls": "1. RCVS is a reversible condition and often self-limited over weeks. 2. Thunderclap headache is the hallmark, and angiographic studies reveal multi-segmental vasoconstriction.",
        "current_evidence": "Recent studies underscore the utility of calcium channel blockers in RCVS management and stress the importance of differentiating RCVS from conditions like PACNS. Guidelines advocate for a conservative, supportive approach as the vasoconstriction is typically transient."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993492",
    "fields": {
      "question_number": "",
      "question_text": "SCA came with ??",
      "options": {
        "A": "(Ipsilateral Horner's syndrome) is correct as it reflects the involvement of the descending sympathetic fibers in the lateral midbrain due to SCA infarct. Option B (4th cranial nerve palsy) is incorrect as the trochlear nerve is usually spared in SCA territory strokes, making it an uncommon presentation."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "The Superior Cerebellar Artery (SCA) supplies parts of the lateral midbrain and cerebellum. Lesions in this territory can affect adjacent neural structures, including the descending sympathetic fibers responsible for ocular sympathetic innervation.",
        "pathophysiology": "An infarct in the SCA territory may extend into the lateral midbrain where sympathetic fibers run. Interruption of these fibers can produce ipsilateral Horner's syndrome, characterized by ptosis, miosis, and anhidrosis.",
        "clinical_correlation": "Patients with SCA strokes may present with a constellation of symptoms including ataxia, vertigo, and sometimes cranial nerve deficits. The presence of ipsilateral Horner's syndrome is an important clue localizing the lesion to regions where the sympathetic pathway is affected.",
        "diagnostic_approach": "Diagnosis is achieved via neuroimaging (CT or MRI) showing infarction in the SCA territory. Differential diagnoses include lateral medullary (Wallenberg) syndrome and other brainstem strokes. The demonstration of ipsilateral Horner's syndrome, without involvement of the trochlear nerve (as seen in 4th nerve palsy), helps solidify the diagnosis.",
        "classification_and_neurology": "SCA stroke is classified under ischemic strokes of the posterior circulation according to the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system. It falls within the category of large artery atherosclerosis or cardioembolism depending on etiology. The posterior circulation strokes encompass infarctions in territories supplied by the vertebral, basilar, posterior cerebral, and cerebellar arteries (including SCA, anterior inferior cerebellar artery, and posterior inferior cerebellar artery). The classification has evolved to emphasize vascular territory localization, facilitating tailored diagnostic and therapeutic approaches. While some frameworks separate brainstem and cerebellar strokes, the SCA stroke straddles both, highlighting the importance of integrated neurovascular understanding. There is consensus that clinical syndromes correspond closely to vascular territories, but overlap and variability exist.",
        "classification_and_nosology": "SCA infarcts are a type of posterior circulation ischemic stroke. They are categorized based on vascular territories and are often managed within the larger context of stroke care.",
        "management_principles": "Management follows standard ischemic stroke protocols. First-line treatment includes supportive care in a stroke unit, antiplatelet therapy, and risk factor modification. In selected cases within the appropriate time window, reperfusion therapy may be considered. In pregnancy and lactation, treatment modalities including antiplatelet therapy are used with appropriate risk-benefit discussions. Secondary prevention is emphasized.",
        "option_analysis": "Option A (Ipsilateral Horner's syndrome) is correct as it reflects the involvement of the descending sympathetic fibers in the lateral midbrain due to SCA infarct. Option B (4th cranial nerve palsy) is incorrect as the trochlear nerve is usually spared in SCA territory strokes, making it an uncommon presentation.",
        "clinical_pearls": "1. Ipsilateral Horner's syndrome is a key localizing sign in lateral midbrain and SCA infarcts. 2. Careful neurological examination can differentiate between various brainstem syndromes based on specific deficits.",
        "current_evidence": "Recent research emphasizes the importance of recognizing subtle signs such as Horner's syndrome in posterior circulation strokes. Guidelines continue to support optimized stroke unit care and secondary prevention measures as key to reducing morbidity."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993244",
    "fields": {
      "question_number": "28",
      "question_text": "Patient with right side weakness, non-fluent speech, impaired repetition and naming but intact comprehension but Broca aphasia localization",
      "options": {
        "A": "Supramarginal Gyrus",
        "B": "Frontal Perisylvian",
        "C": "Temporal posterior, superior"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Broca's aphasia is characterized by non-fluent, effortful speech with impaired repetition and naming but relatively preserved comprehension. The lesions are typically localized to the left inferior frontal gyrus in the dominant hemisphere, an area within the frontal perisylvian region.",
        "pathophysiology": "An ischemic stroke affecting Broca\u2019s area results in disruption of the neural circuits involved in speech production. Despite the damage, receptive language areas (such as Wernicke's area) remain intact, preserving comprehension.",
        "clinical_correlation": "Patients present with right-sided weakness (often due to proximity of motor fibers in the dominant hemisphere) and expressive language deficits. The specific pattern of impaired fluency, repetition, and naming in the setting of intact comprehension makes the diagnosis of Broca's aphasia clear.",
        "diagnostic_approach": "Clinical bedside language assessments coupled with neuroimaging (MRI/CT) help confirm the localization. Differential diagnoses include conduction aphasia (characterized by impaired repetition but with relatively fluent speech) and global aphasia (which has both expressive and receptive deficits).",
        "classification_and_neurology": "Broca aphasia is classified as a type of non-fluent aphasia within the Western aphasia classification system, which divides aphasias into fluent and non-fluent types based on speech output and comprehension. It belongs to the broader category of cortical aphasias affecting language production. The classification includes: - Broca aphasia (non-fluent, expressive) - Wernicke aphasia (fluent, receptive) - Conduction aphasia - Global aphasia - Transcortical motor and sensory aphasias Modern nosology integrates neuroimaging and lesion localization to refine classifications, emphasizing perisylvian cortical involvement. Contemporary consensus supports localization of Broca aphasia to the frontal perisylvian area, distinct from temporal lobe lesions causing Wernicke aphasia. The classification has evolved with advances in neuroanatomy and imaging, but the clinical syndromic approach remains foundational in stroke neurology.",
        "classification_and_nosology": "Aphasias are categorized based on the location of the lesion in the language-dominant hemisphere. Broca\u2019s aphasia falls under non-fluent aphasias and is part of the overall classification of cortical aphasias.",
        "management_principles": "Acute management involves standard stroke care with possible reperfusion therapy if within the time window. Long-term management centers on early speech and language therapy. For pregnant or lactating patients, standard stroke management and rehabilitation measures are used, with particular care to avoid teratogenic medications.",
        "option_analysis": "Option A (Supramarginal Gyrus) is typically associated with conduction aphasia and is less likely to cause the non-fluent speech seen in Broca\u2019s aphasia. Option B (Frontal Perisylvian) is correct as it encompasses Broca\u2019s area. Option C (Temporal posterior, superior) is aligned with Wernicke's area, which would not produce the non-fluent speech and preserved comprehension seen in this case.",
        "clinical_pearls": "1. Broca's aphasia is characterized by non-fluent speech with relatively preserved comprehension. 2. Lesions in the frontal perisylvian region, particularly the left inferior frontal gyrus, are classically responsible for Broca\u2019s aphasia.",
        "current_evidence": "Recent guideline updates and rehabilitation research emphasize early intervention with speech therapy to improve outcomes in Broca\u2019s aphasia. Advanced neuroimaging continues to refine our understanding of the neural networks involved in language processing."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993245",
    "fields": {
      "question_number": "29",
      "question_text": "Patient with visual defect, what is the artery",
      "options": {
        "A": "SCA",
        "B": "Basilar artery"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "The visual cortex in the occipital lobe receives its blood supply primarily from the posterior cerebral artery (PCA). In patients presenting with visual field defects\u2014such as contralateral homonymous hemianopia with potential macular sparing\u2014the involvement of the PCA is highly suspect. Although the options list includes arteries like the superior cerebellar artery (SCA) and the basilar artery, the artery directly linked to primary visual processing is the PCA.",
        "pathophysiology": "Occlusion of the PCA, whether due to embolism, thrombosis, or other cerebrovascular events, leads to ischemia in the occipital cortex. This ischemia disrupts the function of the primary visual cortex, resulting in characteristic visual deficits. Recent evidence emphasizes that timely identification and reperfusion (when indicated) can limit the extent of neural damage.",
        "clinical_correlation": "Clinically, a stroke in the PCA territory typically presents with contralateral visual field deficits (e.g., homonymous hemianopia with macular sparing). Patients may or may not have additional symptoms depending on the involvement of adjacent structures, but the hallmark is the visual defect.",
        "diagnostic_approach": "Imaging studies such as CT scans (initially) followed by MRI (to better delineate the affected area) are crucial. CT angiography or MR angiography can help identify an occlusion in the PCA. Differential diagnoses include occipital lobe lesions from other causes (hemorrhage, tumor) but the vascular pattern in stroke remains distinct.",
        "classification_and_neurology": "Vascular lesions causing visual field deficits are classified under ischemic strokes affecting posterior circulation territories. According to the TOAST classification, strokes are categorized by etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.), with posterior circulation strokes involving the vertebrobasilar system. The basilar artery, a major posterior circulation vessel, supplies the PCA and thus the visual cortex. The SCA is a branch of the basilar artery but is classified as a cerebellar artery, not a posterior cerebral artery. This distinction is crucial in nosology and clinical classification. Contemporary stroke classifications emphasize vascular territory localization for prognosis and management. Debates exist regarding optimal subclassifications for posterior circulation strokes due to their heterogeneity, but consensus supports territory-based approaches.",
        "classification_and_nosology": "Cerebrovascular accidents (strokes) are categorized broadly into ischemic and hemorrhagic types. A PCA infarct falls under the ischemic stroke category and is classified based on its vascular territory.",
        "management_principles": "The management of an acute PCA stroke involves rapid evaluation for thrombolytic therapy (if within the therapeutic window), supportive care, and secondary prevention with antiplatelets and control of risk factors. In pregnant or lactating patients, the use of thrombolytics is carefully considered following current guidelines, weighing maternal benefit against potential fetal risk. Blood pressure and glucose control, as well as early rehabilitation, form integral parts of management.",
        "option_analysis": "Option A (SCA) primarily supplies portions of the cerebellum and midbrain; Option B (Basilar artery) mainly supplies the brainstem and parts of the cerebellum; Option C is presumed to represent the Posterior Cerebral Artery (PCA) and is correct; Option D is blank. Thus, the marked answer (C) is correct.",
        "clinical_pearls": "1. PCA strokes classically cause contralateral homonymous hemianopia with possible macular sparing. 2. Rapid recognition and imaging are critical in stroke management. 3. Timely intervention with thrombolytic therapy (when indicated) can improve outcomes.",
        "current_evidence": "Recent AHA/ASA guidelines stress the importance of rapid imaging and intervention in acute ischemic strokes. Studies continue to support the role of MRI and vascular imaging in confirming PCA occlusion, thereby guiding timely thrombolysis or endovascular therapy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993246",
    "fields": {
      "question_number": "30",
      "question_text": "Hypertension & diabetic who bone fracture went for surgery then developed stroke what is the mechanism in sickle cell anemia patient with 2 attacks of weakness 1 year apart. What is the most common provocative factor",
      "options": {
        "A": "Physical stress",
        "B": "Emotional Stress",
        "C": "Hypertension",
        "D": "Hyperventilation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Sickle cell anemia is characterized by the abnormal deformation of red blood cells under stress. This predisposes patients to vaso-occlusive crises, which can manifest in various organs, including the brain. In the context of stroke, various triggers can provoke sickling and endothelial injury leading to vaso-occlusion.",
        "pathophysiology": "In sickle cell disease, under conditions of physical stress (including surgical stress, trauma, or strenuous activity), hypoxia and acidosis can promote the polymerization of hemoglobin S. This results in the sickling of red blood cells, microvascular occlusion, and ultimately ischemic injury to brain tissue, which may manifest as transient neurological deficits or stroke.",
        "clinical_correlation": "Patients with sickle cell disease may present with recurrent neurological deficits or stroke-like episodes. In this scenario, the patient\u2019s history of surgery following a bone fracture (a significant physical stressor) is a common trigger for a vaso-occlusive crisis leading to stroke.",
        "diagnostic_approach": "Diagnosis is based on clinical history (repeated episodes of weakness), neuroimaging (MRI can show ischemic lesions), and transcranial Doppler (TCD) ultrasound to assess cerebral blood flow velocities. Differential diagnoses include embolic strokes from other causes, hemorrhagic stroke, or transient ischemic attacks related to other vasculopathies.",
        "classification_and_neurology": "Stroke in sickle cell anemia is classified under cerebrovascular diseases, specifically ischemic stroke due to sickle cell vasculopathy. The World Health Organization (WHO) and American Heart Association (AHA) classify strokes in SCA as ischemic strokes secondary to hematologic disorders.  - **Taxonomy:** It falls within the category of stroke due to sickle cell disease, distinct from atherosclerotic or cardioembolic strokes. - **Subtypes:** Large vessel occlusive stroke and small vessel (lacunar) infarcts are recognized. - **Evolution of classification:** Earlier views considered strokes in SCA as purely vaso-occlusive; now, the role of large vessel vasculopathy and endothelial dysfunction is acknowledged. - **Controversies:** The relative contribution of hypercoagulability versus vaso-occlusion remains debated, but current consensus emphasizes multifactorial mechanisms.",
        "classification_and_nosology": "Strokes in sickle cell disease are typically categorized as ischemic strokes resulting from vaso-occlusion. They are further classified based on the underlying precipitating factor\u2014here, physical stress serves as the provocative trigger.",
        "management_principles": "The primary management strategy includes avoiding or mitigating provoked crises by managing triggers (such as dehydration, hypoxia, and stress). Acute stroke management in sickle cell patients may include exchange transfusions to reduce the percentage of sickled cells. Long-term management includes hydroxyurea and regular blood transfusions to reduce stroke risk. In pregnancy and lactation, these therapies are used with caution, and multidisciplinary approaches are recommended to balance maternal health with fetal safety.",
        "option_analysis": "Option A (Physical stress) is the recognized trigger in many vaso-occlusive episodes leading to stroke in sickle cell patients, making it correct. Option B (Emotional stress) can contribute but is less commonly the direct precipitant. Option C (Hypertension) is a risk factor for stroke in general but is not the predominant trigger in sickle cell crises. Option D (Hyperventilation) is not typically associated with inducing sickling events.",
        "clinical_pearls": "1. Sickle cell crises are often precipitated by physical stress, such as surgery or trauma. 2. Recurrent neurological deficits in sickle cell patients warrant evaluation for stroke. 3. Preventative strategies, including blood transfusions and hydroxyurea, can reduce recurrence.",
        "current_evidence": "Recent research supports the role of physical stress in precipitating vaso-occlusive crises that lead to stroke in sickle cell patients. Current guidelines emphasize early intervention with exchange transfusions and novel disease-modifying agents to limit recurrence, with adjustments in management protocols during pregnancy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993247",
    "fields": {
      "question_number": "31",
      "question_text": "ICH 2 days later with BP 170/90 with long list of labs all within normal but marginal low 145 platelet count what is next",
      "options": {
        "A": "Labetalol",
        "B": "Amlodipine",
        "C": "Platelet transfusion"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Intracerebral hemorrhage (ICH) requires prompt management to prevent hematoma expansion and secondary brain injury. Blood pressure control is a vital component of the acute management strategy. In this clinical scenario, even though the blood pressure is moderately elevated (170/90 mmHg), immediate pharmacologic intervention is warranted.",
        "pathophysiology": "In ICH, elevated blood pressure can lead to further bleeding by increasing the hydrostatic pressure within compromised vessels. Tight blood pressure control using intravenous agents helps to mitigate hematoma expansion. The choice of agent is also guided by its rapid onset and ease of titration.",
        "clinical_correlation": "A patient two days post-ICH with a blood pressure of 170/90 mmHg might be at risk for further hemorrhagic extension. The laboratory data being within normal limits (aside from a marginally low platelet count of 145, which remains within acceptable ranges for most interventions) support the decision to manage blood pressure rather than pursue transfusion.",
        "diagnostic_approach": "Diagnosis is confirmed by CT imaging showing an intracerebral hemorrhage. Differential considerations include hemorrhagic transformation of an ischemic stroke, coagulopathy-related bleeding, or vascular malformations. Laboratory evaluation, including platelet counts and coagulation profiles, helps rule out bleeding diatheses.",
        "classification_and_neurology": "ICH is classified under hemorrhagic stroke within cerebrovascular diseases. The American Heart Association/American Stroke Association (AHA/ASA) stroke classification system categorizes ICH by location (lobar, deep, brainstem, cerebellar), etiology (hypertensive, amyloid angiopathy, coagulopathy), and clinical severity. Thrombocytopenia is classified by platelet count thresholds: mild (100,000-150,000/\u00b5L), moderate (50,000-100,000/\u00b5L), and severe (<50,000/\u00b5L). Management guidelines align with this classification, emphasizing BP control and correction of significant hemostatic abnormalities. The classification system has evolved to integrate imaging markers (e.g., spot sign) predicting hematoma expansion and to refine treatment thresholds based on risk stratification.",
        "classification_and_nosology": "Intracerebral hemorrhage is classified among hemorrhagic strokes. The categorization is based on the etiology (primary vs. secondary), the location within the brain, and associated risk factors such as hypertension and coagulopathies.",
        "management_principles": "The first-line management in ICH with moderately elevated blood pressure involves the use of intravenous antihypertensives such as labetalol, which is preferred for its quick onset and ease of titration. Second-line agents include nicardipine. Oral agents like amlodipine are avoided in the hyperacute setting due to their slower onset. Platelet transfusion is only indicated if the platelet count is significantly low (usually <50 x 10\u2079/L) or in patients on antiplatelet agents. In pregnancy, labetalol is widely accepted as a first-line antihypertensive, and its use remains appropriate during lactation.",
        "option_analysis": "Option A (Labetalol) is the most appropriate choice for rapid blood pressure control in acute ICH. Option B (Amlodipine) is not ideal for acute management because it is typically administered orally and does not allow rapid titration. Option C (Platelet transfusion) is not indicated since the platelet count, although marginally low, remains near normal levels. Option D is blank.",
        "clinical_pearls": "1. Rapid blood pressure control in ICH is crucial to prevent hemorrhage expansion. 2. IV labetalol is a first-line agent in both general and obstetric populations. 3. Platelet transfusions are reserved for significant thrombocytopenia or antiplatelet agent use.",
        "current_evidence": "The latest AHA/ASA guidelines for the management of intracerebral hemorrhage continue to endorse the use of IV labetalol (or nicardipine) for emergent blood pressure management. Recent studies have underscored the importance of moderate blood pressure reduction to balance the risks of hematoma expansion with the risks of cerebral hypoperfusion."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993248",
    "fields": {
      "question_number": "32",
      "question_text": "After 5 hours of labour, with depression on SSRI, ?? CT picture & angiography",
      "options": {
        "A": "PRES",
        "B": "??"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Postpartum neurological emergencies include a variety of conditions such as Posterior Reversible Encephalopathy Syndrome (PRES) and Reversible Cerebral Vasoconstriction Syndrome (RCVS). Both conditions can occur in the postpartum setting and may share overlapping clinical features, but specific imaging findings help to differentiate them.",
        "pathophysiology": "RCVS is characterized by transient, multifocal narrowing of the cerebral arteries due to dysregulation of cerebral vascular tone. It is commonly triggered by the postpartum state, and factors such as the use of serotonergic medications (like SSRIs) can contribute. In contrast, PRES involves vasogenic edema secondary to blood\u2013brain barrier disruption, often in the context of severe hypertension. The presence of angiographic changes (e.g., a 'string of beads' appearance) is more consistent with RCVS.",
        "clinical_correlation": "In a postpartum patient with a history of SSRI use, the development of neurological symptoms along with imaging findings on CT and abnormal angiographic features strongly points to RCVS. Patients typically present with thunderclap headaches and may have transient neurological deficits. Although PRES is also seen postpartum, its hallmark is symmetrical vasogenic edema predominantly in the posterior regions of the cerebral hemispheres, without the characteristic segmental arterial constriction seen in RCVS.",
        "diagnostic_approach": "The diagnostic approach involves neuroimaging. MRI is optimal for detecting the vasogenic edema of PRES, while CT angiography or digital subtraction angiography can reveal the multifocal segmental narrowing typical of RCVS. Differential diagnoses include cerebral vasculitis, which tends to have a more chronic course, and aneurysmal subarachnoid hemorrhage, which is excluded by the imaging pattern.",
        "classification_and_neurology": "PRES is classified as a reversible encephalopathy syndrome within the broader category of cerebrovascular disorders and neurotoxic syndromes. It overlaps clinically and radiologically with hypertensive encephalopathy, eclampsia-associated neurological complications, and certain drug-induced encephalopathies. The nosology has evolved from being considered a rare syndrome to a recognized clinical-radiological entity with diverse etiologies including hypertensive crises, cytotoxic drugs, autoimmune diseases, and pregnancy-related conditions. Current consensus places PRES under reversible cerebral edema syndromes with a distinct pathophysiological basis of autoregulatory failure and endothelial dysfunction. Controversies remain regarding the exact pathogenesis\u2014whether vasospasm or hyperperfusion predominates\u2014and the role of SSRIs and other medications as precipitating factors.",
        "classification_and_nosology": "RCVS is classified among the reversible cerebral vasoconstriction syndromes, a group characterized by reversible segmental constriction of cerebral arteries. PRES is categorized as a neurotoxic state associated with endothelial dysfunction leading to vasogenic edema. Both entities are distinct but can occasionally coexist.",
        "management_principles": "Management of RCVS is primarily supportive. Calcium channel blockers (such as nimodipine) are commonly employed to alleviate vasospasm, and pain management is crucial. Blood pressure is typically not as dramatically elevated as in PRES, so aggressive antihypertensive therapy is less central. In postpartum patients, including those who are breastfeeding, medications like nimodipine are considered relatively safe, but individualized risk\u2010benefit analysis is still essential. For PRES, management focuses on blood pressure control and withdrawal of the inciting agent. The distinction between the two is important for guiding therapy.",
        "option_analysis": "Option A (PRES) represents one of the differential diagnoses; however, the inclusion of angiographic findings (typically not a feature of PRES) suggests that the diagnosis is more in line with RCVS. Option B (presumed here to be RCVS) is the better match given the patient\u2019s postpartum status, the SSRI association, and the angiographic findings. Options C and D are not provided. Thus, the marked answer B is correct.",
        "clinical_pearls": "1. RCVS often presents in postpartum women with severe, thunderclap headaches and reversible arterial narrowing on angiography. 2. SSRIs and the postpartum state are recognized triggers for RCVS. 3. Differentiation between RCVS and PRES is critical, as management strategies differ.",
        "current_evidence": "Recent literature has further delineated the diagnostic criteria for RCVS, emphasizing the role of vascular imaging to identify reversible vasoconstriction. Current guidelines advocate for supportive care with calcium channel blockers, and emerging research continues to refine the management protocols for postpartum patients presenting with these syndromes."
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
