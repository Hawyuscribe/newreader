
# Import batch 3 of 3 from chunk_4_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993081",
    "fields": {
      "question_number": "307",
      "question_text": "Case scenario about acute ischemic stroke happened in the morning and her presented in the evening with high BP of 190/90 and asked what to do in regards to his blood pressure",
      "options": {
        "A": "No management",
        "B": "oral amlodipine",
        "C": "IV labetalol",
        "D": "IV nicardipine"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In acute ischemic stroke, blood pressure is often elevated as part of the body\u2019s response to maintain cerebral perfusion in the ischemic penumbra. Unless blood pressure exceeds a critical threshold, aggressive lowering may be harmful.",
        "pathophysiology": "Cerebral autoregulation in the setting of an ischemic stroke often shifts, causing the brain to be dependent on higher blood pressure to perfuse the penumbral regions. Lowering the blood pressure too aggressively can worsen ischemia in these vulnerable areas.",
        "clinical_correlation": "A patient who presents later in the day after an acute ischemic stroke with a blood pressure of 190/90 mmHg falls below the thresholds typically necessitating urgent blood pressure lowering (usually >220/120 mmHg in those not receiving thrombolytic therapy).",
        "diagnostic_approach": "This management decision is based on serial blood pressure measurements, clinical assessment, and imaging confirming ischemic stroke without hemorrhagic transformation. Differential diagnoses include hypertensive emergency unrelated to stroke, but here the elevated BP is likely a physiological response.",
        "classification_and_neurology": "Acute ischemic stroke is classified within the cerebrovascular disease spectrum, according to systems such as the TOAST classification, which categorizes ischemic strokes based on etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.). Blood pressure management is a key component of acute stroke care protocols but does not change the ischemic stroke subtype classification. Management guidelines are informed by evidence-based consensus from organizations like the American Heart Association/American Stroke Association (AHA/ASA), which provide specific blood pressure thresholds and recommendations for treatment during the hyperacute and acute phases of ischemic stroke. These guidelines have evolved over time as evidence has clarified the risks and benefits of BP control in this setting.",
        "classification_and_nosology": "Ischemic stroke is one of the two major categories of stroke (ischemic vs. hemorrhagic), with ischemic strokes further subclassified based on etiology (thrombotic, embolic, lacunar).",
        "management_principles": "For ischemic stroke not treated with thrombolysis, current guidelines recommend permissive hypertension (up to 220/120 mmHg) to maintain perfusion to the ischemic penumbra. Therefore, no acute blood pressure management is indicated unless levels exceed these limits. In patients who are pregnant or lactating, similar principles apply; blood pressure management is generally deferred unless severely elevated, with close monitoring to avoid compromising cerebral blood flow.",
        "option_analysis": "Option A (No management) is correct because the patient\u2019s blood pressure of 190/90 mmHg is below the threshold that would require acute intervention in an ischemic stroke patient outside the thrombolytic window. Options B, C, and D involve pharmacologic lowering, which could potentially reduce cerebral perfusion in the affected area and worsen neurological outcomes.",
        "clinical_pearls": "\u2022 Permissive hypertension is typical in acute ischemic stroke management to optimize cerebral perfusion. \u2022 Blood pressure should only be lowered if it exceeds 220/120 mmHg in patients not receiving thrombolytic therapy. \u2022 Overzealous BP reduction can expand the ischemic core.",
        "current_evidence": "Recent guidelines from the AHA/ASA continue to support a conservative approach to blood pressure management in acute ischemic stroke, emphasizing maintaining cerebral perfusion. Emerging research continues to explore the optimal thresholds and timing for antihypertensive therapy in various stroke subgroups."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993082",
    "fields": {
      "question_number": "308",
      "question_text": "Intracranial bleed and asked about the blood pressure management",
      "options": {
        "A": "140/90",
        "B": "160/90"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In intracerebral hemorrhage (ICH), blood pressure management is critical because elevated blood pressure is associated with hematoma expansion and worsened outcomes. The goal is to reduce secondary brain injury by stabilizing the patient\u2019s blood pressure.",
        "pathophysiology": "Elevated blood pressure in the setting of an intracranial bleed can increase the hydrostatic pressure across the ruptured vessel wall, leading to hematoma enlargement. This expansion increases intracranial pressure (ICP) and may cause further brain tissue damage. Key trials such as INTERACT2 have demonstrated that careful blood pressure reduction can mitigate these effects.",
        "clinical_correlation": "Patients with ICH typically present with sudden neurological deficits, headache, nausea, and altered consciousness. The hypertensive state may exacerbate the mass effect from the hemorrhage, leading to additional neurological deterioration as seen with signs of raised ICP.",
        "diagnostic_approach": "Diagnosis is primarily made through non-contrast CT scanning, which distinguishes hemorrhagic stroke from ischemic stroke. Differential diagnoses include ischemic stroke, hypertensive encephalopathy, and other causes of acute neurological decline. Blood pressure monitoring is integrated into the management plan once ICH is identified.",
        "classification_and_neurology": "Intracerebral hemorrhage is classified under hemorrhagic stroke within the cerebrovascular disease spectrum. It differs from ischemic stroke by its pathophysiology, clinical presentation, and management. ICH can be further subclassified by etiology (hypertensive, amyloid angiopathy, anticoagulation-related, vascular malformations). The current classification systems, such as the WHO stroke classification and the American Heart Association/American Stroke Association (AHA/ASA) stroke guidelines, incorporate ICH as a distinct entity requiring specific therapeutic approaches. Recent consensus emphasizes the importance of early BP management as a modifiable risk factor influencing outcomes. Controversies remain regarding the optimal BP target, but evolving evidence supports intensive BP lowering within safe limits.",
        "classification_and_nosology": "Intracerebral hemorrhage is classified under hemorrhagic strokes. It is typically separated from subarachnoid hemorrhage (which involves bleeding into the subarachnoid space) and further stratified by underlying cause (hypertensive, amyloid angiopathy, etc.).",
        "management_principles": "First-line management involves stabilization with supportive care and rapid blood pressure control. Current AHA/ASA guidelines recommend that for patients presenting with ICH and systolic blood pressure between 150-220 mm Hg, lowering the systolic blood pressure to around 140 mm Hg is reasonable. IV antihypertensives (such as nicardipine or labetalol) are commonly used. In pregnancy, antihypertensive options like labetalol or hydralazine are preferred given their safety profiles, while in lactation, similar agents with minimal secretion into breast milk are chosen.",
        "option_analysis": "Option A (140/90) is consistent with guideline recommendations targeting a systolic blood pressure of approximately 140 mm Hg to attenuate further bleeding. Option B (160/90) is less optimal because maintaining a higher blood pressure could risk further hemorrhage expansion.",
        "clinical_pearls": "1. Rapid blood pressure control in ICH can limit hematoma expansion and improve outcomes. 2. CT imaging is the cornerstone of diagnosis in differentiating ICH from other stroke types.",
        "current_evidence": "Recent studies including the INTERACT2 trial have reinforced the safety and potential benefit of aggressive blood pressure lowering to a target of 140 mm Hg systolic in patients with ICH. Current guidelines reflect these findings, emphasizing individualized care while balancing the risk of cerebral hypoperfusion."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993083",
    "fields": {
      "question_number": "309",
      "question_text": "Lady with two days history of malignant left MCA and midline shift (CT was attached) transferred from another hospital what will you do for her",
      "options": {
        "A": "Craniectomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Malignant middle cerebral artery (MCA) infarction refers to a large, space\u2010occupying ischemic stroke resulting in extensive cerebral edema, increased intracranial pressure (ICP), and potential herniation. Decompressive craniectomy is a surgical intervention used to relieve this pressure.",
        "pathophysiology": "In malignant MCA infarction, the abrupt loss of blood flow leads to neuronal death and cytotoxic edema. The ensuing swelling increases ICP and can result in midline shift, compressing vital brainstem structures. Surgical decompression helps prevent or reduce secondary injury from the mass effect.",
        "clinical_correlation": "Patients typically present with rapid neurological deterioration including decreased consciousness, hemiparesis, and signs of raised ICP. CT imaging revealing significant edema and midline shift confirms the severity of the infarction.",
        "diagnostic_approach": "Diagnosis is based on clinical examination supported by CT or MRI. Differential diagnoses include hemorrhagic transformation of an infarct or large territorial infarcts from other cerebrovascular territories. The presence of significant midline shift is a key indicator for surgical decompression.",
        "classification_and_neurology": "Malignant MCA infarction is classified within the spectrum of ischemic stroke subtypes, specifically as a large vessel occlusion stroke involving the MCA territory. Stroke classification systems such as the TOAST criteria categorize strokes by etiology (large artery atherosclerosis, cardioembolism, small vessel disease, etc.), while the OCSP (Oxfordshire Community Stroke Project) classification describes strokes by clinical syndromes, with malignant MCA infarction corresponding to total anterior circulation infarcts (TACI). The designation 'malignant' refers to the clinical and radiological severity rather than etiology, emphasizing the high risk of fatal cerebral edema. This classification aids in prognostication and management decisions. The concept of malignant MCA infarction has evolved with the recognition that early decompressive surgery can alter the natural history, shifting it from a uniformly fatal condition to one with potential for survival and recovery.",
        "classification_and_nosology": "Malignant MCA syndrome is a severe subtype of ischemic stroke, categorized by large infarcts in the MCA territory with a high risk of cerebral edema and herniation.",
        "management_principles": "Early decompressive craniectomy (within 48 hours of symptom onset) has been shown to improve survival and functional outcomes. First-line management in malignant MCA infarction is surgical decompression combined with optimal medical management, including ICP control. For pregnant patients, careful coordination with obstetric teams is necessary; while decompressive craniectomy is generally safe, anesthetic and surgical planning must take fetal safety into account. In lactation, standard surgical management applies with supportive measures for the mother.",
        "option_analysis": "Option A (Craniectomy) is correct because decompressive craniectomy is the recommended intervention for malignant MCA infarction with midline shift. Other medical management options alone (such as osmotherapy) are often insufficient in the context of malignant edema.",
        "clinical_pearls": "1. Time is brain\u2014early decompressive surgery can significantly reduce mortality in malignant MCA syndrome. 2. CT evidence of midline shift is a critical sign indicating the need for surgical intervention.",
        "current_evidence": "Landmark trials such as DECIMAL, DESTINY, and HAMLET have provided strong evidence that early decompressive hemicraniectomy in malignant MCA strokes leads to improved outcomes, despite the risk of survival with significant disability. Current guidelines support its use in appropriately selected patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993084",
    "fields": {
      "question_number": "310",
      "question_text": "Case of lateral pontine syndrome (hint was hearing loss)",
      "options": {
        "A": "AICA",
        "B": "PICA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Lateral pontine syndrome is a brainstem stroke syndrome that results from infarction in the territory of the anterior inferior cerebellar artery (AICA). The involvement of the cochlear nuclei is a key feature that distinguishes this syndrome.",
        "pathophysiology": "Occlusion of the AICA leads to ischemia in the lateral aspect of the pons, affecting cranial nerve nuclei (such as the facial nerve) and the cochlear nuclei. This results in deficits including hearing loss, facial paralysis, and sometimes loss of balance due to vestibular involvement.",
        "clinical_correlation": "Patients with lateral pontine syndrome typically present with ipsilateral facial weakness, loss of facial sensation, and hearing loss, along with vestibulocochlear disturbances like vertigo. In contrast, lateral medullary (Wallenberg) syndrome, usually from PICA occlusion, does not typically feature hearing loss.",
        "diagnostic_approach": "Diagnosis is made based on clinical findings corroborated by imaging studies such as MRI, which can delineate the infarcted territory. Differential diagnoses include lateral medullary syndrome and other brainstem pathologies; the presence of auditory symptoms favors an AICA infarct.",
        "classification_and_neurology": "Lateral pontine syndrome falls under the broader category of brainstem ischemic stroke syndromes within cerebrovascular diseases. According to the TOAST classification, it is classified as a large artery atherosclerosis or cardioembolic stroke subtype affecting the vertebrobasilar circulation. The syndrome is a subtype of lateral brainstem syndromes, specifically localized to the pons. In the vascular territory classification, it corresponds to infarction in the AICA distribution. This contrasts with lateral medullary (Wallenberg) syndrome, which involves the PICA territory. Over time, stroke classification systems have evolved from purely clinical syndromes to incorporate imaging and etiological data, improving diagnostic accuracy. Some controversy remains about the overlap of clinical features between AICA and PICA strokes, but the presence of hearing loss is a key discriminant favoring AICA involvement.",
        "classification_and_nosology": "This syndrome is classified under brainstem strokes. Lateral pontine syndrome specifically refers to lesions within the AICA distribution.",
        "management_principles": "Management is primarily supportive and includes antiplatelet therapy, risk factor modification, and rehabilitation. There is no specific surgical intervention; however, acute stroke protocols (including thrombolysis if within the time window) may be applicable. In pregnancy and lactation, management is conservative with safe antiplatelet regimens and careful monitoring of blood pressure and other risk factors.",
        "option_analysis": "Option A (AICA) is correct because the clinical presentation\u2014particularly hearing loss\u2014is characteristic of an AICA infarct. Option B (PICA) is more commonly associated with lateral medullary syndrome, which does not typically present with hearing deficits.",
        "clinical_pearls": "1. Hearing loss is a crucial distinguishing feature of lateral pontine syndrome due to AICA involvement. 2. Detailed neurological examination and imaging are essential in differentiating brainstem stroke syndromes.",
        "current_evidence": "Recent advances in MRI and MR angiography have improved the accurate localization of brainstem infarcts. Current stroke management guidelines emphasize early diagnosis and supportive care to optimize neurological recovery."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993085",
    "fields": {
      "question_number": "311",
      "question_text": "Case scenario of alexia without agraphia, what artery is involved?",
      "options": {
        "A": "PCA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Alexia without agraphia (pure alexia) is a disconnection syndrome where a patient loses the ability to read while retaining the ability to write. This occurs due to lesions in the dominant (usually left) occipital lobe and involvement of the splenium of the corpus callosum, which disconnects visual input from language processing areas.",
        "pathophysiology": "The left posterior cerebral artery (PCA) supplies the occipital lobe, including the visual cortex. Infarction in this territory, particularly when it involves the splenium, interrupts the transfer of visual information to the angular gyrus, leading to alexia without agraphia. The neural pathways involved in writing remain intact, preserving the patient\u2019s ability to produce written language.",
        "clinical_correlation": "Patients present with the inability to read printed words (alexia), yet they can write normally (without agraphia). This clinical dissociation is a hallmark diagnostic clue for a left PCA stroke affecting the visual cortex and splenium.",
        "diagnostic_approach": "Diagnosis is made with neuroimaging, typically MRI with diffusion-weighted imaging, which reveals infarction in the left occipital region and possibly the splenium. Differential diagnoses include other causes of acquired reading disorders, but the combination with a vascular distribution strongly implicates PCA involvement.",
        "classification_and_neurology": "Alexia without agraphia falls under the category of **language disorders (aphasias)**, specifically a **disconnection syndrome**. It is classified as a type of **alexia**, which is a subset of acquired reading disorders.  - **Alexia with agraphia:** lesion involves dominant angular gyrus. - **Alexia without agraphia:** lesion involves left occipital cortex and splenium (PCA territory).  The classification aligns with vascular syndromes defined by arterial territories. The PCA territory infarcts cause this syndrome, differentiating it from middle cerebral artery (MCA) infarcts which more commonly cause aphasia or agraphia.",
        "classification_and_nosology": "Alexia without agraphia is classified as a disconnection syndrome and is most often associated with infarction due to occlusion of the posterior cerebral artery in the dominant hemisphere.",
        "management_principles": "Management of PCA strokes includes acute stroke interventions such as IV thrombolysis or mechanical thrombectomy if within the appropriate time window, in addition to secondary prevention measures using antiplatelet agents and risk factor optimization. For pregnant or lactating patients, treatment is adjusted to ensure fetal or neonatal safety, with careful selection of thrombolytic and antiplatelet therapies following current obstetric guidelines.",
        "option_analysis": "Option A (PCA) is correct, as the vascular territory of the PCA supplies the areas responsible for visual processing and reading. Lesions in other vascular territories would not produce the specific syndrome of alexia without agraphia.",
        "clinical_pearls": "1. The dissociation between preserved writing and impaired reading (alexia without agraphia) is a classic sign of left occipital lobe and splenium involvement. 2. Prompt neuroimaging is critical to identify the infarct and guide appropriate therapeutic interventions.",
        "current_evidence": "Contemporary stroke management protocols emphasize rapid diagnosis and treatment. Advances in neuroimaging have improved the localization of infarcts, and guidelines continue to support aggressive management of PCA strokes within the thrombolysis and thrombectomy time windows, with adaptations in pregnancy and lactation as needed."
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
