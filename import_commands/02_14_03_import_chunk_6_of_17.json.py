
# Import batch 3 of 3 from chunk_6_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993173",
    "fields": {
      "question_number": "162",
      "question_text": "Typical case scenario of lateral medullary syndrome, with decreased right side hearing. Symptoms started acutely. Diagnosis?",
      "options": {
        "A": "PICA",
        "B": "AICA",
        "C": "SCA",
        "D": "Middle cerebral artery"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Watershed strokes occur in border-zone regions between two major arterial territories (e.g., between the ACA and MCA or MCA and PCA territories) where blood supply is most vulnerable to drops in perfusion. In patients with vascular risk factors such as diabetes, hypertension, and dyslipidemia, atherosclerotic narrowing and episodes of hypotension can lead to these characteristic infarcts.",
        "pathophysiology": "Due to advanced atherosclerotic changes, the distal branches of major cerebral arteries receive marginal blood flow. During periods of systemic hypotension or when there is significant carotid stenosis, these border zones are most at risk for ischemia. Recent evidence emphasizes that hemodynamic compromise rather than embolic occlusion leads to the wedge\u2010shaped infarctions seen in watershed regions.",
        "clinical_correlation": "This patient\u2019s left-sided weakness accompanied by DWI abnormalities on MRI that show a rostro\u2010caudal or wedge\u2010shaped pattern in a border zone region fits a watershed infarct. The risk factor profile further supports a mechanism based on compromised perfusion to distal vascular territories.",
        "diagnostic_approach": "Neuroimaging with MRI (especially DWI) is essential to identify the infarct pattern. Vascular imaging (carotid Doppler, CT angiography) is used to assess for carotid stenosis. Differential diagnoses include cardioembolic stroke (which generally presents with multiple cortical infarcts) and lacunar infarcts (from small vessel occlusion). The infarct distribution distinguishes watershed from these other etiologies.",
        "classification_and_neurology": "Brainstem strokes are classified based on vascular territories: - **PICA syndrome (Lateral medullary syndrome):** infarction of lateral medulla, supplied by PICA - **AICA syndrome (Lateral pontine syndrome):** infarction of lateral pons and cerebellar structures supplied by AICA - **SCA syndrome:** infarction in superior cerebellar artery territory, affecting superior cerebellum and midbrain structures - **MCA syndrome:** infarcts in middle cerebral artery territory, affecting lateral cerebral cortex, not brainstem  This classification is grounded in vascular neuroanatomy and clinical localization. The distinction between PICA and AICA syndromes is critical because they affect different brainstem levels and produce distinct clinical pictures. Contemporary stroke classification systems like the TOAST criteria classify strokes by etiology but rely on vascular territory to guide clinical localization and management. There is consensus that hearing loss implicates AICA territory due to cochlear nucleus involvement.",
        "classification_and_nosology": "Watershed strokes are classified as ischemic strokes occurring in border zones, separate from embolic strokes and small vessel (lacunar) infarcts. They represent a distinct entity related predominantly to hemodynamic failure.",
        "management_principles": "Acute management involves standard stroke protocols including antiplatelet therapy (e.g., aspirin \u00b1 clopidogrel in the acute phase), blood pressure stabilization, and aggressive risk factor modification. In patients with significant carotid stenosis, revascularization may be considered. For pregnant or lactating patients, low-dose aspirin is generally safe and blood pressure agents (like labetalol) can be used with fetal safety in mind.",
        "option_analysis": "\u2022 A: Vasculitis is less likely in an older patient with consistent atherosclerotic risk factors.  \u2022 B: Cardioembolic strokes typically result in cortical infarcts and are often associated with arrhythmias such as atrial fibrillation.  \u2022 C: Watershed is correct given the context of hemodynamic compromise in border zones.  \u2022 D: A hypercoagulable state is also less likely given the patient\u2019s age and risk profile.",
        "clinical_pearls": "\u2022 Watershed infarcts are located at the junctions of major arterial territories. \u2022 They are typically due to hemodynamic compromise rather than embolic phenomena. \u2022 MRI with DWI is the gold standard to identify the specific infarct pattern.",
        "current_evidence": "Recent guidelines stress the importance of advanced neuroimaging to differentiate stroke subtypes. There is also evolving evidence on the benefits of dual antiplatelet therapy in high-risk TIA and stroke prevention in patients with significant carotid stenosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993174",
    "fields": {
      "question_number": "163",
      "question_text": "59 years old male, DM, HTN, DLP, presented with sudden dysarthria and right arm numbness, lasted for 10 minutes. Currently he is asymptomatic, NIHSS zero. Brain CT reported normal as well as normal basic labs. What is the best next step?",
      "options": {
        "A": "Reassurance",
        "B": "Neck CTA",
        "C": "ECHO",
        "D": "Toxic screen"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "A transient ischemic attack (TIA) is defined as a brief episode of neurological dysfunction resulting from temporary cerebral ischemia with no evidence of acute infarction on imaging. In patients with significant vascular risk factors such as diabetes mellitus, hypertension, and dyslipidemia, it is essential to search for an underlying vascular etiology that could predict an impending stroke.",
        "pathophysiology": "TIA is most commonly due to embolic phenomena or a transient thrombosis in an atherosclerotic vessel. In patients with risk factors, atherosclerotic plaques can develop in the carotid arteries, leading to narrowing and potential plaque rupture, which may cause transient episodes of ischemia.",
        "clinical_correlation": "This 59\u2010year\u2010old male presented with sudden dysarthria and right arm numbness that resolved within 10 minutes. His transient symptoms, absence of residual deficits (NIHSS 0), and a normal CT scan are typical for a TIA. However, his vascular risk factors increase the risk of significant carotid disease or other vascular causes.",
        "diagnostic_approach": "The workup of TIA involves excluding other causes of transient neurological deficits (such as migraine, seizure, or hypoglycemia) and then identifying the source of ischemia. Key diagnostic studies include brain imaging (CT/MRI) and vascular imaging. A Neck CTA is recommended to assess for carotid stenosis, which, if significant, could necessitate urgent intervention. Cardiac sources are also considered, but in this patient, the likelihood points more toward extracranial atherosclerosis given his risk profile.",
        "classification_and_neurology": "TIA falls within the cerebrovascular disease spectrum as defined by the World Health Organization and American Heart Association/American Stroke Association (AHA/ASA). Historically, TIA was defined by symptom duration <24 hours; however, modern imaging-based definitions classify TIA as transient neurological symptoms without infarction on diffusion-weighted MRI, distinguishing it from minor stroke. Etiologically, TIAs are classified using the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. This patient\u2019s profile and presentation most likely correspond to large artery atherosclerosis due to vascular risk factors. Understanding this classification guides targeted investigations and therapy. Controversies remain regarding the optimal imaging and timing of evaluation, but consensus emphasizes urgent assessment due to stroke risk.",
        "classification_and_nosology": "TIA is classified under cerebrovascular diseases and is differentiated from stroke by its transient nature (symptoms lasting less than 24 hours without persistent infarction on imaging). The identification of TIA is clinically significant because it is a warning syndrome for future ischemic strokes.",
        "management_principles": "According to current guidelines, patients with suspected TIA should undergo prompt vascular imaging. A Neck CTA is indicated to evaluate the carotid arteries for significant stenosis, which can be managed either medically or, if severe (\u226570%), may require interventions such as carotid endarterectomy. In patients who are pregnant or lactating, while CTA does involve radiation exposure, carotid Doppler ultrasound can be utilized as an alternative imaging modality to avoid ionizing radiation.",
        "option_analysis": "Option A (Reassurance) is not acceptable because even though the symptoms have resolved, TIA is a critical warning sign of future stroke and requires further evaluation. Option B (Neck CTA) is correct because it effectively assesses the carotid arteries for atherosclerotic disease, which is highly relevant given the patient's risk profile. Option C (ECHO) may be useful to rule out a cardiac source, but it is less immediately prioritized in a scenario strongly suggesting extracranial carotid disease. Option D (Toxic screen) is not supported by the clinical scenario as there is no evidence or suspicion of a toxic/metabolic cause.",
        "clinical_pearls": "Always treat a TIA as a warning sign and thoroughly investigate its etiology. In a patient with multiple vascular risk factors, extracranial carotid disease is a common culprit, and vascular imaging (via Neck CTA or Doppler ultrasound) should be performed without delay.",
        "current_evidence": "Recent studies and guidelines from stroke associations underscore the importance of rapid vascular imaging in TIA patients to identify high-risk carotid stenosis. This approach is based on evidence that early identification can reduce the risk of subsequent ischemic strokes through timely medical or surgical intervention."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_1.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993175",
    "fields": {
      "question_number": "164",
      "question_text": "45 years old lady, has sudden severe headache following neck manipulation, predominantly on the right side. She has no other symptoms and no vascular factors. Attached image of her exam findings - which artery is likely dissected?",
      "options": {
        "A": "ICA dissection",
        "B": "MCA dissection",
        "C": "Ophthalmic artery",
        "D": "Vertebral dissection"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Arterial dissections occur when a tear in the arterial wall allows blood to enter between its layers, creating a false lumen. In the cervical region, both internal carotid and vertebral artery dissections are recognized, but an ICA dissection is classically associated with a painful, unilateral headache often accompanied by signs of sympathetic disruption (a partial Horner syndrome). Patients are frequently middle\u2010aged women, and the event can be triggered by minor trauma such as neck manipulation.",
        "pathophysiology": "In an ICA dissection, a tear in the intima allows blood to accumulate within the vessel wall, forming an intramural hematoma. This may narrow the true lumen or lead to thrombus formation. Disruption of the adjacent sympathetic plexus results in features such as ipsilateral ptosis and miosis (Horner syndrome).",
        "clinical_correlation": "A 45\u2010year\u2010old woman with a sudden severe headache following neck manipulation fits the profile for a traumatic dissection. The exam image (though not available here) likely shows subtle findings (e.g., a partial Horner syndrome on the right side) that support the diagnosis of a right ICA dissection. The absence of posterior circulation or cerebellar/brainstem signs makes vertebral dissection less likely in this case.",
        "diagnostic_approach": "The evaluation of suspected arterial dissection involves vascular imaging such as CT angiography or MRI/MRA, which can delineate the arterial wall and reveal a dissection with a false lumen or intramural hematoma. Differential diagnoses include vertebral artery dissection (typically with posterior circulation signs), migraine, and even subarachnoid hemorrhage, but the localized exam finding (eg, Horner syndrome) helps focus the diagnosis on the ICA.",
        "classification_and_neurology": "Arterial dissections are classified based on the affected vessel and the clinical syndrome. Cervical artery dissections include both ICA and vertebral artery dissections. The **TOAST classification** for ischemic stroke includes arterial dissection as a subtype of large artery atherosclerosis or other determined etiology. Dissections belong to the broader category of vascular disorders causing ischemic stroke. They can be further subclassified into spontaneous versus traumatic dissections. The current consensus, as per the American Heart Association/American Stroke Association (AHA/ASA) guidelines, recognizes cervical artery dissection as a distinct cause of stroke, particularly in younger patients. There is ongoing debate regarding the best classification of dissections, especially with advances in imaging revealing asymptomatic or subclinical dissections. The nosology also includes differentiation between intracranial and extracranial dissections, with extracranial ICA dissections being more common and clinically significant.",
        "classification_and_nosology": "Internal carotid artery dissection is classified as a non-atherosclerotic, often traumatic, vasculopathy. It is subcategorized under cervical artery dissections, and depending on the cause, it may be termed spontaneous or traumatic (here linked to neck manipulation).",
        "management_principles": "Management of ICA dissection generally involves antithrombotic therapy (either antiplatelet agents or anticoagulation) to reduce the risk of thromboembolic stroke. Current guidelines suggest that both approaches are valid, with treatment tailored to individual patient risk factors. In pregnant and lactating women, low molecular weight heparin is the preferred agent because of its safety profile during pregnancy and lactation. Close follow-up with repeat imaging is usually warranted to assess healing.",
        "option_analysis": "Option A (ICA dissection) is the most consistent with the clinical picture provided: a unilateral headache following neck manipulation and exam findings suggestive of sympathetic involvement (eg, Horner syndrome). Options B (MCA dissection) and C (Ophthalmic artery) are far less common and do not fit the clinical scenario. Option D (Vertebral dissection) is frequently cited in association with neck manipulation; however, vertebral dissection usually presents with posterior headache and additional brainstem or cerebellar neurologic deficits, which this patient does not exhibit.",
        "clinical_pearls": "\u2022 Neck manipulation can precipitate arterial dissections in susceptible individuals.  \u2022 A unilateral headache with signs of sympathetic dysfunction (Horner syndrome) should raise suspicion for ICA dissection.  \u2022 Although vertebral artery dissection is commonly associated with chiropractic manipulation, its presentation typically includes posterior circulation signs.",
        "current_evidence": "Recent clinical studies and guidelines underscore the importance of early and accurate imaging (using CT angiography/MRA) in suspected carotid dissections. Furthermore, meta-analyses suggest that antiplatelet and anticoagulant therapies provide comparable outcomes in preventing stroke from these dissections, with particular considerations for pregnancy and lactation favoring agents like low molecular weight heparin due to their safety profiles."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993176",
    "fields": {
      "question_number": "165",
      "question_text": "61 years old female presented with sudden severe headache, worst in her life, with double vision. Her headache was more on the right side, not responding to simple analgesia. Examination shows 6 mm right pupil not reactive to light, with no other neurological deficits. Which artery affected?",
      "options": {
        "A": "PCom artery aneurysm",
        "B": "AICA",
        "C": "SCA",
        "D": "ICA dissection"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In this case the patient\u2019s sudden, severe headache \u2013 often described as the worst headache of one\u2019s life \u2013 associated with diplopia and a fixed dilated pupil is classic for an aneurysmal subarachnoid hemorrhage from a posterior communicating (PCom) artery aneurysm compressing the oculomotor nerve.",
        "pathophysiology": "A posterior communicating artery aneurysm can enlarge or rupture leading to bleeding in the subarachnoid space. Because the oculomotor nerve courses adjacent to the PCom artery, the aneurysm can compress its peripheral parasympathetic fibers, resulting in pupillary dilation and impaired light reaction. This mechanism is well documented and underlies the classic presentation.",
        "clinical_correlation": "The patient\u2019s unilateral headache, oculomotor nerve deficit (6 mm pupil that is non-reactive), and double vision all point to a compressive lesion from an aneurysm. The lack of other neurological deficits is typical in a localized compressive process before more diffuse bleeding or secondary complications occur.",
        "diagnostic_approach": "Initial evaluation includes a non-contrast head CT to detect subarachnoid hemorrhage. If the CT is negative and suspicion remains high, a lumbar puncture is indicated. CT angiography or digital subtraction angiography is used to confirm the presence and location of an aneurysm. Differential diagnoses include migraine with aura (which would not cause fixed pupil dilation), cluster headache, and other intracranial hemorrhages.",
        "classification_and_neurology": "Intracranial aneurysms are classified based on morphology (saccular, fusiform), location (anterior vs posterior circulation), and etiology (congenital, acquired). The PCom artery aneurysm is a type of saccular (berry) aneurysm located in the anterior circulation of the circle of Willis.   Cranial nerve III palsies are classified by etiology into compressive (aneurysm, tumor), ischemic (diabetes, hypertension), inflammatory, traumatic, or infectious causes. This case fits into the compressive category due to aneurysm.  The nosology of subarachnoid hemorrhage includes traumatic and non-traumatic causes, with aneurysmal rupture being the most common non-traumatic cause. The Hunt and Hess grading system and the Fisher scale are used to classify SAH severity and predict prognosis. Understanding these classifications helps guide diagnosis, prognosis, and management.",
        "classification_and_nosology": "Intracranial aneurysms are classified by their location and morphology. A saccular (berry) aneurysm in the region of the PCom artery is the most common type associated with third nerve palsy and subarachnoid hemorrhage.",
        "management_principles": "Acute management involves stabilization and blood pressure control. Definitive treatment aims to secure the aneurysm via neurosurgical clipping or endovascular coiling \u2013 with current guidelines favoring endovascular therapy in many cases. In pregnant or lactating patients, careful multidisciplinary planning is required, balancing maternal-fetal risks; imaging and intervention are performed with modified protocols (e.g., minimizing radiation exposure).",
        "option_analysis": "Option A (PCom artery aneurysm) is correct due to its classic presentation causing compressive oculomotor nerve palsy. Option B (AICA) and Option C (SCA) are related to cerebellar or brainstem structures and do not classically produce isolated third nerve palsy with subarachnoid hemorrhage. Option D (ICA dissection) usually produces pain with possible Horner syndrome rather than an isolated fixed, dilated pupil.",
        "clinical_pearls": "1. A 'thunderclap' headache with a fixed, dilated pupil should immediately raise suspicion for a PCom aneurysm causing third nerve palsy. 2. The parasympathetic fibers lie peripherally in the oculomotor nerve, making them more vulnerable to compression.",
        "current_evidence": "Recent guidelines by the American Heart Association emphasize rapid imaging and intervention in suspected aneurysmal subarachnoid hemorrhage. Endovascular coiling has become increasingly preferred, depending on aneurysm morphology and patient factors."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993177",
    "fields": {
      "question_number": "166",
      "question_text": "Scenario of 65 years old male with multiple cardiovascular risk factors and afib, with 1 day history of right sided dense plegia and aphasia. His brain CT attached. His clinical status doesn't change. What is the best next treatment option to consider? NB: patient was clinically stable with no clinical features of TICP.",
      "options": {
        "A": "Anticoagulation",
        "B": "Osmotic therapy",
        "C": "Craniotomy/decompression",
        "D": "Aspirin"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This patient presents with an acute ischemic stroke in the setting of atrial fibrillation and vascular risk factors. Cardioembolic strokes from AF tend to be large and can lead to significant deficits. In the acute management phase, treatment decisions are tailored to minimize hemorrhagic risk.",
        "pathophysiology": "Atrial fibrillation can lead to the formation of thrombi in the left atrium, which may embolize to cerebral vessels causing ischemic stroke. The dense plegia and aphasia indicate a large infarct in the left hemisphere. The early initiation of anticoagulation in large infarcts is associated with an increased risk of hemorrhagic transformation.",
        "clinical_correlation": "Dense right-sided weakness and aphasia suggest a left hemisphere stroke likely due to a cardioembolic event. The fact that the patient\u2019s clinical status is stable and there are no signs of increased intracranial pressure or hemorrhage (as seen on CT) guides the immediate management strategy.",
        "diagnostic_approach": "After the non-contrast CT confirms an ischemic stroke (and rules out hemorrhage), additional work up includes ECG and cardiac monitoring for AF, echocardiography, and vascular imaging. Differential diagnoses include thrombotic stroke from large artery atherosclerosis or small-vessel lacunar infarctions, but the presence of AF points to a cardioembolic source.",
        "classification_and_neurology": "Ischemic stroke is classified etiologically using systems such as the TOAST criteria, which divides ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This patient fits the cardioembolic stroke category due to AF. The classification guides treatment and prognosis. Stroke can also be classified temporally (acute, subacute, chronic) and by severity (using NIHSS scores). The management guidelines for acute ischemic stroke have evolved, emphasizing early reperfusion therapy and careful secondary prevention tailored to stroke subtype. Controversies remain regarding optimal timing of anticoagulation after cardioembolic stroke, especially in large infarcts, due to hemorrhagic transformation risk. Current consensus favors initial antiplatelet therapy followed by delayed anticoagulation in stable patients.",
        "classification_and_nosology": "This is a case of acute ischemic stroke, specifically a cardioembolic stroke, which is categorized under embolic strokes of undetermined source when accompanied by atrial fibrillation.",
        "management_principles": "The standard of care is to start antiplatelet therapy (aspirin) in the acute setting to reduce the risk of early recurrence while deferring full anticoagulation to avoid hemorrhagic transformation. Current guidelines recommend delaying initiation of oral anticoagulation for about 4-14 days in patients with large infarcts. In patients who are pregnant or lactating, aspirin (at appropriate low doses) remains an acceptable choice for short-term management, with bridging to appropriate anticoagulation once it is safe.",
        "option_analysis": "Option A (Anticoagulation) is generally avoided in the first days after a large ischemic stroke due to the elevated risk of hemorrhagic conversion; Option B (Osmotic therapy) is reserved for managing raised intracranial pressure, which is not evident here; Option C (Craniotomy/decompression) is indicated for malignant cerebral edema with signs of TICP. Option D (Aspirin) is the correct immediate management choice.",
        "clinical_pearls": "1. In cardioembolic strokes, the timing of initiating anticoagulation is critical: too early increases hemorrhagic risk, especially in large infarcts. 2. Aspirin is the mainstay of immediate secondary prevention in patients not eligible for early full anticoagulation.",
        "current_evidence": "Recent studies and AHA/ASA guidelines advocate for a cautious delay in initiating anticoagulation in large cardioembolic strokes, with aspirin being used acutely to balance the risks of recurrent stroke versus hemorrhagic transformation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_3.png"
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
