
# Import batch 3 of 3 from chunk_1_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99992992",
    "fields": {
      "question_number": "234",
      "question_text": "Based on the following imaging, which territory involved?",
      "options": {
        "A": "Posterior cerebral artery",
        "B": "PICA",
        "C": "Superior cerebellar artery SCA",
        "D": "AICA"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "The Superior Cerebellar Artery (SCA) supplies the superior portion of the cerebellum, including parts of the cerebellar hemispheres and vermis. In vascular neuroimaging, identifying which arterial territory is involved is based on the location of the infarct or lesion seen on imaging.",
        "pathophysiology": "An infarct in the SCA territory typically results from thromboembolism or atherosclerotic occlusion. The resulting ischemia affects the regions of the cerebellum responsible for coordination, balance, and fine motor control. Recent studies and imaging techniques (such as high-resolution MRI) have improved our ability to differentiate between infarcts in different cerebellar vascular territories.",
        "clinical_correlation": "Patients with an SCA infarct may present with ataxia, dysmetria, and difficulty with coordinated movements due to involvement of the superior cerebellum. These symptoms help differentiate an SCA stroke from other posterior circulation strokes (e.g., PICA infarcts may involve lateral medullary signs, whereas AICA strokes often involve hearing loss and facial paralysis).",
        "diagnostic_approach": "Once clinical signs suggest a cerebellar involvement, neuroimaging is essential. Differential diagnoses include infarcts in the PICA (lateral medullary syndrome), AICA (lateral pontine syndrome), and even occipital infarcts (PCA territory). MRI with diffusion-weighted imaging (DWI) is highly sensitive, and CT scans may initially be used to rule out hemorrhage.",
        "classification_and_neurology": "Cerebellar strokes are classified based on the arterial territory involved: PICA, AICA, and SCA infarcts each define a distinct clinical syndrome within the broader category of posterior circulation strokes. The TOAST classification system categorizes ischemic strokes by etiology (large artery atherosclerosis, cardioembolism, small vessel disease, etc.), but anatomical localization remains essential for clinical management. The posterior circulation stroke syndromes have been further refined by clinical-radiological correlation studies that define typical infarct patterns for each cerebellar artery. There is consensus that SCA infarcts constitute a distinct nosological entity within cerebellar strokes due to their unique vascular supply and clinical presentation. Controversies exist in overlapping infarcts and watershed areas, but imaging advances have improved classification accuracy.",
        "classification_and_nosology": "Cerebellar strokes are categorized under posterior circulation strokes. The SCA, PICA, and AICA infarcts are further sub-classified based on the vascular territory involved within the cerebellum.",
        "management_principles": "Acute management involves rapid stroke evaluation and consideration for thrombolysis if within the treatment window, along with supportive and rehabilitative care. First-line therapy is usually IV thrombolysis (if eligible) and sometimes endovascular therapy. In pregnant or lactating women, CT and MRI protocols are adjusted to minimize radiation exposure; IV thrombolysis has been used with caution when benefits outweigh risks.",
        "option_analysis": "Option A (Posterior cerebral artery) involves the occipital lobe, not the cerebellum; Option B (PICA) supplies the inferior cerebellum and lateral medullary region; Option D (AICA) affects parts of the lateral pons and inner ear structures. Thus, Option C correctly matches the infarct location seen in the imaging.",
        "clinical_pearls": "1) Localization of stroke based on vascular territories is critical for proper diagnosis. 2) SCA strokes typically present with gait ataxia and dysmetria. 3) Differentiating cerebellar vascular territories helps tailor management and anticipate complications.",
        "current_evidence": "Recent advances underscore the importance of rapid imaging with MRI/DWI in diagnosing posterior circulation strokes. Updated stroke guidelines emphasize the timely use of thrombolysis and endovascular therapy, even in posterior circulation strokes, with careful adjustments in special populations such as pregnant or lactating women."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992993",
    "fields": {
      "question_number": "235",
      "question_text": "Young female developed severe headache and photophobia post-partum, what to do?",
      "options": {
        "A": "Brain CT venography"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Postpartum women are at increased risk for hypercoagulable states, and cerebral venous sinus thrombosis (CVST) is a key consideration when a young female presents with severe headache and photophobia. The use of appropriate venographic imaging helps confirm the diagnosis.",
        "pathophysiology": "CVST involves thrombosis in the cerebral venous system, leading to impaired venous drainage, raised intracranial pressure, and resultant neurological symptoms. The postpartum period is particularly risky due to physiological changes and a hypercoagulable state. Recent studies emphasize early detection and prompt anticoagulation therapy to improve outcomes.",
        "clinical_correlation": "Severe headache, often accompanied by photophobia, nausea, and sometimes focal neurological deficits, are hallmark signs of CVST. In the postpartum period, these symptoms should raise significant concern for this diagnosis.",
        "diagnostic_approach": "The differential diagnosis includes pre-eclampsia/eclampsia, migraines, subarachnoid hemorrhage, and meningitis. Brain CT venography is a rapid and accessible imaging modality that is highly useful for diagnosing CVST. Alternatively, MR venography can be used when available, especially when radiation avoidance is a priority.",
        "classification_and_neurology": "CVST is classified under cerebrovascular disorders, specifically venous strokes, distinct from arterial ischemic strokes. The International Classification of Headache Disorders (ICHD-3) recognizes headache attributed to intracranial venous thrombosis as a secondary headache disorder. CVST is part of the broader category of cerebral venous and sinus thrombosis disorders, which include thrombosis of cortical veins and deep cerebral veins. Etiologically, CVST is grouped under prothrombotic conditions, with pregnancy and puerperium as recognized transient risk factors. Classification systems have evolved with advances in neuroimaging, allowing better identification of venous infarcts and thrombosis. Some debate exists regarding the optimal subtyping based on location (superior sagittal sinus vs. transverse sinus) and clinical severity, but consensus supports early recognition based on clinical and imaging criteria.",
        "classification_and_nosology": "CVST is classified under cerebrovascular disorders involving venous systems as opposed to arterial strokes. Its etiology is often linked to hypercoagulable states, including the postpartum period.",
        "management_principles": "First-line management involves anticoagulation therapy (typically low molecular weight heparin) even in the presence of hemorrhagic transformation. In pregnant or lactating women, LMWH is considered safe and is the treatment of choice. Subsequent management includes supportive care and addressing potential complications such as raised intracranial pressure.",
        "option_analysis": "Option A (Brain CT venography) is the appropriate imaging study to confirm CVST and is rapidly available in emergency settings. The other options are either not provided or not relevant to the investigation of CVST.",
        "clinical_pearls": "1) Always consider a hypercoagulable work-up in postpartum women with headaches. 2) CT venography is a preferred initial study for CVST due to its rapid availability. 3) Anticoagulation is the cornerstone of CVST management even if hemorrhage is present.",
        "current_evidence": "Recent guidelines support early diagnosis of CVST with CT or MR venography and the initiation of anticoagulation therapy. There is also increasing emphasis on the safety profile of LMWH in pregnancy and lactation, with robust evidence favoring its use in these populations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992994",
    "fields": {
      "question_number": "236",
      "question_text": "Based on the following visual field defect in picture B, which artery involved?",
      "options": {
        "A": "Anterior choroidal artery",
        "B": "Posterior choroidal artery",
        "C": "Ophthalmic artery",
        "D": "Posterior cerebral artery"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "The visual field defect described in picture B is consistent with a lesion in the occipital lobe. The Posterior Cerebral Artery (PCA) supplies this region, and occlusion typically leads to contralateral homonymous hemianopia with potential macular sparing.",
        "pathophysiology": "Occlusion of the PCA leads to an ischemic stroke in the occipital lobe. This region of the brain is responsible for processing visual information. The phenomenon of macular sparing occurs because the macular region often receives collateral blood flow from the middle cerebral artery.",
        "clinical_correlation": "Patients with PCA infarctions commonly present with visual field deficits, such as contralateral homonymous hemianopia. The presence of macular sparing is a key clinical indicator that helps differentiate PCA strokes from lesions in the visual pathways elsewhere.",
        "diagnostic_approach": "The differential diagnosis includes lesions in the optic radiation (which may produce similar deficits but typically lack macular sparing), retinal pathologies involving the ophthalmic artery, and infarcts of the anterior or posterior choroidal arteries. Neuroimaging with MRI, especially diffusion-weighted imaging, can confirm the diagnosis and the specific vascular territory involved.",
        "classification_and_neurology": "Anterior choroidal artery infarcts are classified under ischemic strokes of the territory of the internal carotid artery branches. According to the TOAST classification, these infarcts fall under large-artery atherosclerosis or cardioembolism depending on etiology. The AChA syndrome is a distinct clinical entity within cerebrovascular disease, characterized by involvement of deep perforating arteries supplying subcortical structures. The classification of stroke syndromes has evolved to emphasize vascular territory and clinical presentation correlations. While the PCA territory infarcts are considered posterior circulation strokes, AChA infarcts are part of the anterior circulation stroke spectrum. Understanding these classifications aids in diagnostic precision and management decisions. Some controversy exists regarding the variability of AChA territory and collateral supply, which can influence clinical presentation and complicate strict classification.",
        "classification_and_nosology": "PCA strokes are classified as ischemic strokes within the posterior circulation. They are a distinct subgroup of cerebral infarctions with well-recognized clinical and radiographic features.",
        "management_principles": "Management follows the acute ischemic stroke protocols (e.g., IV thrombolysis if within the therapeutic window, antiplatelet therapy, and supportive measures). For pregnant or lactating patients, careful imaging choices (MRI without gadolinium when possible) and adjusted therapeutic interventions are recommended according to current guidelines.",
        "option_analysis": "Option A (Anterior choroidal artery) mainly affects deep structures such as the internal capsule and thalamus; Option B (Posterior choroidal artery) is less commonly implicated in isolated visual field defects; Option C (Ophthalmic artery) involves the retina and would produce different visual findings. Option D (Posterior cerebral artery) is the only artery whose occlusion classically results in the described occipital lobe infarct and corresponding visual field defect, making it the correct answer.",
        "clinical_pearls": "1) Macular sparing is a key sign pointing to PCA involvement. 2) Visual field deficits in stroke are typically due to occipital lobe involvement. 3) A careful history and imaging correlation are essential in differentiating between retinal and cerebral causes of visual loss.",
        "current_evidence": "Current stroke guidelines emphasize rapid neuroimaging for suspected PCA infarcts. Research into advanced neuroimaging techniques has further refined our ability to localize ischemia within the posterior circulation and guide prompt therapeutic intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "https://drive.google.com/file/d/18rBzE-r1x4I_HPYSxtbxYOm2xoSRKMi7/preview"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992995",
    "fields": {
      "question_number": "237",
      "question_text": "Same image, and the question what to do next to confirm the diagnosis?",
      "options": {
        "A": "Brain CT Angio"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "After identification of a visual field defect suggestive of a PCA stroke, the next step is to confirm the vascular occlusion using imaging that can visualize the cerebral arteries. This confirmation is crucial for guiding acute stroke management.",
        "pathophysiology": "An occlusion of the PCA leads to ischemia in the occipital lobe responsible for processing visual information. Confirming the occlusion helps in establishing the diagnosis and in planning appropriate acute management, including thrombolysis or endovascular interventions if within the appropriate time window.",
        "clinical_correlation": "The patient\u2019s visual field deficit, in this context, directs the clinician to suspect a PCA infarct. Confirmatory vascular imaging not only reinforces the diagnosis but also helps exclude other potential causes of visual loss such as retinal artery occlusion or other intracranial vascular pathologies.",
        "diagnostic_approach": "The main differentials in this setting include other causes of visual deficits such as optic neuritis, retinal artery occlusion, or lesions in the optic radiation. Brain CT angiography (CTA) offers a rapid method to visualize arterial occlusion and is widely available in most emergency departments, making it the preferred next step in the acute setting.",
        "classification_and_neurology": "Cerebrovascular diseases are classified broadly into ischemic and hemorrhagic strokes. Ischemic strokes are further subclassified based on etiology, such as large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar stroke), stroke of other determined etiology, and stroke of undetermined etiology, per the TOAST classification system. Imaging findings help distinguish these subtypes by revealing vessel pathology. Vascular imaging with CTA fits within the diagnostic workup recommended for ischemic stroke classification. This classification has evolved with advances in imaging allowing more precise etiological diagnosis, which informs prognosis and management. Controversies remain regarding the optimal imaging modality in certain clinical contexts, but CTA is widely accepted for rapid vascular assessment.",
        "classification_and_nosology": "This scenario falls under posterior circulation ischemic stroke. Vascular imaging is used to classify the stroke subtype (infarction due to large vessel occlusion versus small vessel disease) which then guides further treatment.",
        "management_principles": "First-line management includes rapid imaging confirmation (via CT angiography) to assess the occlusion. Subsequent management follows acute ischemic stroke protocols including IV thrombolysis if indicated and endovascular therapy if within the appropriate time window. In pregnant or lactating women, minimizing radiation is critical. When using CTA, protective measures should be taken, or if available, an MRI/MRA without gadolinium can be considered as an alternative.",
        "option_analysis": "Option A (Brain CT Angio) is the recommended and most practical imaging technique to confirm a suspected PCA occlusion. The marked answer Option B is not defined with any content, making it an unsuitable choice. Options C and D are not provided, but among the available options, CTA is the gold standard in the emergency setting.",
        "clinical_pearls": "1) In suspected PCA infarcts, vascular imaging with CT angiography is essential for confirmation. 2) Rapid confirmation of the occlusion can help determine eligibility for thrombolytic or endovascular therapy. 3) In pregnant and lactating patients, imaging choices should balance diagnostic yield with safety considerations.",
        "current_evidence": "Recent stroke guidelines and research emphasize the role of CT angiography in the rapid evaluation of acute ischemic stroke in posterior circulation. Studies have shown that timely CTA significantly improves outcomes by allowing prompt therapeutic decisions, and emerging protocols continue to optimize imaging strategies in vulnerable populations, including pregnant and breastfeeding women."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99992996",
    "fields": {
      "question_number": "238",
      "question_text": "Patient presented with chronic headache, no other neurological symptoms, found to have 3 mm unruptured aneurysm, what to do?",
      "options": {
        "A": "Observe and follow in 6 months"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Unruptured intracranial aneurysms are often detected incidentally when patients are investigated for unrelated complaints (such as chronic headache). The management strategy is based on aneurysm size, location, morphology, and patient risk factors. Small aneurysms, especially those around 3 mm in diameter, have a very low risk of rupture and are usually managed conservatively.",
        "pathophysiology": "Aneurysms develop due to weakening of the arterial wall from factors like hemodynamic stress and degenerative changes. Rupture risk correlates with the size of the aneurysm and its location. A 3 mm aneurysm, commonly found in the anterior circulation, possesses a minimal rupture risk. Studies indicate that the natural history of such small aneurysms is generally benign when other high\u2010risk features are absent.",
        "clinical_correlation": "In a patient with a chronic headache, finding a small (3 mm) aneurysm without any focal neurological deficits or signs of subarachnoid hemorrhage suggests an incidental lesion. The patient\u2019s clinical stability supports a non-interventional approach with periodic imaging follow-up rather than immediate invasive treatment.",
        "diagnostic_approach": "The initial diagnosis is made with noninvasive imaging such as CT angiography (CTA) or MR angiography (MRA). For small aneurysms, serial imaging (typically 6\u201312 months intervals) is recommended to monitor for any changes in size or morphology. Differential diagnoses include other vascular malformations, but the clear identification of an aneurysmal outpouching confines the diagnosis.",
        "classification_and_neurology": "Cerebral aneurysms are classified primarily by morphology and location. Saccular (berry) aneurysms are the most common type, characterized by a neck and dome, typically at arterial bifurcations. Fusiform and dissecting aneurysms are less common and involve circumferential vessel dilation or intramural hematoma, respectively. The International Study of Unruptured Intracranial Aneurysms (ISUIA) classification stratifies rupture risk based on aneurysm size and location. This system guides management decisions. The nosology also distinguishes between ruptured and unruptured aneurysms, with the latter further subclassified by size (<7 mm considered low risk). Evolution of classification systems has integrated clinical factors such as patient age, comorbidities, and aneurysm morphology to refine risk stratification. Current consensus favors individualized risk assessment rather than a one-size-fits-all approach.",
        "classification_and_nosology": "Intracranial aneurysms are classified by size (small, medium, large, giant), shape (saccular, fusiform), and location (anterior vs. posterior circulation). A 3 mm aneurysm falls under the \u2018small\u2019 category, which is associated with low rupture rates compared to larger aneurysms.",
        "management_principles": "The first-line management for an asymptomatic, small unruptured aneurysm is conservative observation. This includes periodic imaging follow\u2013up (often at around 6 months) and risk factor modification (control of hypertension, smoking cessation). In patients who are pregnant or lactating, non-ionizing imaging modalities like MRA (avoiding gadolinium if possible) are preferred, and invasive procedures are generally deferred unless absolutely indicated.",
        "option_analysis": "Option A: 'Observe and follow in 6 months' is appropriate and aligns with current guidelines for a small (3 mm) unruptured aneurysm. Other options involving intervention (endovascular coiling or surgical clipping) would be considered overtreatment given the very low rupture risk.",
        "clinical_pearls": "1. Aneurysm rupture risk is strongly size-dependent\u2014aneurysms <5 mm in the anterior circulation are generally observed. 2. Serial imaging is the key to safely monitoring these lesions. 3. Risk factor management (e.g., hypertension control, smoking cessation) is critical in all patients.",
        "current_evidence": "Recent guidelines from the American Heart Association and neurosurgical societies endorse a conservative approach for small, asymptomatic aneurysms, emphasizing observation with serial imaging. Emerging evidence continues to support that invasive intervention is reserved for larger or high-risk aneurysms."
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
