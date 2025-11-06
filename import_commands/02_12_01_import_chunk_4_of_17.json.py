
# Import batch 1 of 3 from chunk_4_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993052",
    "fields": {
      "question_number": "224",
      "question_text": "Maxillary, nasal lesion with proptosis, causes of CVT:",
      "options": {
        "A": "(Direct invasion): Correct",
        "B": "(Veins): Incorrect",
        "D": "oes not explain the mechanism. Option c (LN [Lymph nodes]): Incorrect"
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This question examines the mechanism by which maxillary or nasal lesions that produce proptosis can lead to cerebral venous thrombosis (CVT). The central concept is the potential for direct extension of infection or malignancy from adjacent extracranial structures to intracranial venous sinuses.",
        "pathophysiology": "Maxillary or nasal lesions, particularly those with an invasive component, may extend directly into the cerebral venous system. The valveless venous networks interconnect the extracranial and intracranial compartments, allowing pathogens or tumor cells to directly invade the dural sinuses, causing endothelial injury and subsequent thrombosis.",
        "clinical_correlation": "Patients with such lesions typically present with signs of orbital involvement like proptosis, headache, and sometimes visual disturbances. CVT may present with additional symptoms including seizures and altered mental status. Recognizing direct invasive spread is crucial for early diagnosis and management.",
        "diagnostic_approach": "Diagnostic imaging plays a vital role. Magnetic resonance venography (MRV) or CT venography (CTV) can delineate the presence of thrombosis. Differentiation from other causes of proptosis (e.g., orbital cellulitis, cavernous sinus thrombosis from other etiologies) is achieved by correlating clinical history with imaging findings.",
        "classification_and_neurology": "CVT is classified under cerebrovascular disorders and specifically within venous and sinus thrombosis categories in the International Classification of Diseases (ICD) and stroke classification systems. Etiologically, CVT is divided into **septic** and **aseptic** types. Septic CVT arises from infections such as sinusitis, otitis, or facial infections, whereas aseptic CVT is associated with prothrombotic states, malignancy, or systemic diseases. The case of maxillary/nasal lesions with proptosis aligns with septic CVT due to direct contiguous spread. Historically, classification has evolved from purely anatomical to include etiological and pathophysiological frameworks, recognizing the importance of infectious sources and systemic risk factors. Current consensus emphasizes identifying underlying causes to guide management. The nosology reflects the disease\u2019s heterogeneity, incorporating clinical, radiological, and etiological dimensions.",
        "classification_and_nosology": "CVT is classified as a type of stroke due to venous occlusion. It can be septic (associated with infection) or aseptic. In this context, it results from direct invasion by adjacent pathology from the maxillofacial region.",
        "management_principles": "The primary treatment is anticoagulation to prevent thrombus propagation, even in the context of hemorrhagic transformation, along with addressing the underlying lesion (via antibiotics, surgery, or oncological management). In the setting of pregnancy and lactation, low molecular weight heparin is commonly used for CVT due to its safety profile compared to unfractionated heparin or warfarin.",
        "option_analysis": "Option a (Direct invasion): Correct \u2013 It accurately describes the mechanism by which a maxillary, nasal lesion with proptosis causes CVT via anatomical venous connections. Option b (Veins): Incorrect \u2013 Too vague; while veins are the site of thrombosis, this option does not explain the mechanism. Option c (LN [Lymph nodes]): Incorrect \u2013 Lymphatic structures do not directly communicate with the intracranial venous system and are not involved in the pathogenesis of CVT in this scenario.",
        "clinical_pearls": "1. Direct extension of infection or malignancy through valveless venous channels is a well-known cause of CVT. 2. Proptosis in the setting of nasal or maxillary lesions should prompt evaluation for intracranial complications. 3. Early imaging with MRV or CTV is critical in making the diagnosis.",
        "current_evidence": "Recent clinical literature emphasizes the importance of recognizing the anatomical pathways for infection spread in the head and neck region. Updated guidelines support early anticoagulation and management of the primary lesion to improve outcomes in CVT."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993053",
    "fields": {
      "question_number": "225",
      "question_text": "The management of a patient who developed angioedema after starting tPA:",
      "options": {
        "A": "Reassurance",
        "B": "intubate",
        "C": "anti-histamine & steroids",
        "D": "is not provided."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Angioedema is a localized, self\u2010limited edema of the deep dermis and subcutaneous tissues. When it occurs in the context of tPA administration (often in patients with underlying ACE\u2010inhibitor use), it is thought to be secondary to an abnormal release of vasoactive mediators. The clinical scenario requires rapid recognition because swelling of the tongue, lips, or oropharynx can progress to airway compromise.",
        "pathophysiology": "tPA not only lyses fibrin clots but also activates plasmin which can trigger the release of bradykinin. Increased bradykinin levels lead to vasodilation and increased vascular permeability. Although the process is bradykinin\u2010mediated (instead of the classic histaminergic allergic reaction), many of the treatments overlap. In some cases, the reaction may be severe enough to require aggressive airway management.",
        "clinical_correlation": "Patients receiving tPA for ischemic stroke may develop angioedema within the infusion period. Clinically, swelling typically involves the tongue, lips, and sometimes the floor of the mouth. Although it may start as a localized process, rapid progression can lead to difficulty breathing and potential airway loss, especially in patients with predisposing factors such as concurrent ACE inhibitor use.",
        "diagnostic_approach": "This diagnosis is based on clinical observation. The differential includes allergic reaction/anaphylaxis from other agents, or soft tissue infections. In the setting of recent tPA administration and a typical distribution (orolingual), tPA-induced angioedema is the most likely diagnosis. Monitoring for airway patency and assessing progression is critical.",
        "classification_and_neurology": "Angioedema is classified based on etiology into allergic (IgE-mediated), non-allergic (bradykinin-mediated), hereditary, and drug-induced types. tPA-induced angioedema falls under the category of drug-induced, bradykinin-mediated angioedema. The nosological framework recognizes this as a subtype distinct from histamine-mediated allergic angioedema, which has different therapeutic implications. Within cerebrovascular complications, this entity is a recognized adverse effect of thrombolytic therapy. The classification systems for angioedema have evolved to emphasize underlying pathophysiology rather than just clinical presentation, guiding targeted treatment strategies. Controversies remain regarding the precise role of histamine versus bradykinin in tPA-induced cases, influencing management approaches.",
        "classification_and_nosology": "tPA-induced angioedema is classified as a drug-induced adverse reaction with features overlapping with bradykinin-mediated angioedema. It is considered a rare but serious complication of thrombolytic therapy.",
        "management_principles": "The first step in management is to immediately stop the tPA infusion. In mild cases where airway compromise is not imminent, treatment with anti-histamines (H1 blockers) and corticosteroids is recommended to reduce inflammation. Epinephrine may be considered if there are signs of a more typical anaphylactic reaction. However, if there is any concern for airway compromise, securing the airway (with intubation) is imperative. In pregnant or lactating patients, these medications are used with caution but are acceptable when maternal airway protection is needed. Consultation with anesthesia and otolaryngology may be warranted for airway management.",
        "option_analysis": "Option A (Reassurance) is insufficient as the risk of airway compromise requires active intervention. Option B (Intubate) is reserved for cases with significant airway compromise and is not the first-line approach in the absence of severe symptoms. Option C (anti-histamine & steroids) is the appropriate first-line management for mild to moderate angioedema post-tPA, making it the correct answer. Option D is not provided.",
        "clinical_pearls": "\u2022 tPA-induced angioedema is most commonly seen in patients on ACE inhibitors. \u2022 Always monitor for airway compromise and be ready to secure the airway. \u2022 Early cessation of tPA infusion is critical in the management of this complication.",
        "current_evidence": "Recent studies and guidelines emphasize that while the angioedema associated with tPA is bradykinin-mediated, initial management with anti-histamines and steroids remains standard practice, along with vigilant airway monitoring. There is emerging interest in specific bradykinin inhibitors (like icatibant), but these are not yet standard."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993054",
    "fields": {
      "question_number": "226",
      "question_text": "83-Year-old man, presented with 3 hr Hx of stroke, CT brain done What to do next \u0646\u0633\u064a\u062a \u062a\u0641\u0627\u0635\u064a\u0644 \u0627\u0644\u062d\u0627\u0644\u0629",
      "options": {
        "A": "(Reassurance) is insufficient as the risk of airway compromise requires active intervention. Option B (Intubate) is reserved for cases with significant airway compromise and is not the first",
        "C": "(anti",
        "D": "is not provided."
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Angioedema is a localized, self\u2010limited edema of the deep dermis and subcutaneous tissues. When it occurs in the context of tPA administration (often in patients with underlying ACE\u2010inhibitor use), it is thought to be secondary to an abnormal release of vasoactive mediators. The clinical scenario requires rapid recognition because swelling of the tongue, lips, or oropharynx can progress to airway compromise.",
        "pathophysiology": "tPA not only lyses fibrin clots but also activates plasmin which can trigger the release of bradykinin. Increased bradykinin levels lead to vasodilation and increased vascular permeability. Although the process is bradykinin\u2010mediated (instead of the classic histaminergic allergic reaction), many of the treatments overlap. In some cases, the reaction may be severe enough to require aggressive airway management.",
        "clinical_correlation": "Patients receiving tPA for ischemic stroke may develop angioedema within the infusion period. Clinically, swelling typically involves the tongue, lips, and sometimes the floor of the mouth. Although it may start as a localized process, rapid progression can lead to difficulty breathing and potential airway loss, especially in patients with predisposing factors such as concurrent ACE inhibitor use.",
        "diagnostic_approach": "This diagnosis is based on clinical observation. The differential includes allergic reaction/anaphylaxis from other agents, or soft tissue infections. In the setting of recent tPA administration and a typical distribution (orolingual), tPA-induced angioedema is the most likely diagnosis. Monitoring for airway patency and assessing progression is critical.",
        "classification_and_neurology": "Ischemic stroke is classified etiologically by systems such as the TOAST classification, which categorizes strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. The current question pertains to acute management of ischemic stroke, which falls under cerebrovascular diseases in the ICD-10 (I63). The classification guides both prognosis and secondary prevention strategies. Acute ischemic stroke management is distinct from hemorrhagic stroke and transient ischemic attack (TIA), each with different therapeutic approaches. The evolution of classification systems has incorporated imaging and pathophysiology to better tailor treatments.",
        "classification_and_nosology": "tPA-induced angioedema is classified as a drug-induced adverse reaction with features overlapping with bradykinin-mediated angioedema. It is considered a rare but serious complication of thrombolytic therapy.",
        "management_principles": "The first step in management is to immediately stop the tPA infusion. In mild cases where airway compromise is not imminent, treatment with anti-histamines (H1 blockers) and corticosteroids is recommended to reduce inflammation. Epinephrine may be considered if there are signs of a more typical anaphylactic reaction. However, if there is any concern for airway compromise, securing the airway (with intubation) is imperative. In pregnant or lactating patients, these medications are used with caution but are acceptable when maternal airway protection is needed. Consultation with anesthesia and otolaryngology may be warranted for airway management.",
        "option_analysis": "Option A (Reassurance) is insufficient as the risk of airway compromise requires active intervention. Option B (Intubate) is reserved for cases with significant airway compromise and is not the first-line approach in the absence of severe symptoms. Option C (anti-histamine & steroids) is the appropriate first-line management for mild to moderate angioedema post-tPA, making it the correct answer. Option D is not provided.",
        "clinical_pearls": "\u2022 tPA-induced angioedema is most commonly seen in patients on ACE inhibitors. \u2022 Always monitor for airway compromise and be ready to secure the airway. \u2022 Early cessation of tPA infusion is critical in the management of this complication.",
        "current_evidence": "Recent studies and guidelines emphasize that while the angioedema associated with tPA is bradykinin-mediated, initial management with anti-histamines and steroids remains standard practice, along with vigilant airway monitoring. There is emerging interest in specific bradykinin inhibitors (like icatibant), but these are not yet standard."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993055",
    "fields": {
      "question_number": "227",
      "question_text": "Tongue deviation to the Lt",
      "options": {
        "A": "(Reassurance) is insufficient as the risk of airway compromise requires active intervention. Option B (Intubate) is reserved for cases with significant airway compromise and is not the first",
        "C": "(anti",
        "D": "is not provided."
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Angioedema is a localized, self\u2010limited edema of the deep dermis and subcutaneous tissues. When it occurs in the context of tPA administration (often in patients with underlying ACE\u2010inhibitor use), it is thought to be secondary to an abnormal release of vasoactive mediators. The clinical scenario requires rapid recognition because swelling of the tongue, lips, or oropharynx can progress to airway compromise.",
        "pathophysiology": "tPA not only lyses fibrin clots but also activates plasmin which can trigger the release of bradykinin. Increased bradykinin levels lead to vasodilation and increased vascular permeability. Although the process is bradykinin\u2010mediated (instead of the classic histaminergic allergic reaction), many of the treatments overlap. In some cases, the reaction may be severe enough to require aggressive airway management.",
        "clinical_correlation": "Patients receiving tPA for ischemic stroke may develop angioedema within the infusion period. Clinically, swelling typically involves the tongue, lips, and sometimes the floor of the mouth. Although it may start as a localized process, rapid progression can lead to difficulty breathing and potential airway loss, especially in patients with predisposing factors such as concurrent ACE inhibitor use.",
        "diagnostic_approach": "This diagnosis is based on clinical observation. The differential includes allergic reaction/anaphylaxis from other agents, or soft tissue infections. In the setting of recent tPA administration and a typical distribution (orolingual), tPA-induced angioedema is the most likely diagnosis. Monitoring for airway patency and assessing progression is critical.",
        "classification_and_neurology": "Hypoglossal nerve dysfunction is classified under lower motor neuron cranial neuropathies within the spectrum of brainstem syndromes. Brainstem strokes are categorized by vascular territories: medial medullary syndrome (anterior spinal artery), lateral medullary syndrome (posterior inferior cerebellar artery), etc.   The lesion affecting the hypoglossal nerve in the medulla is part of medial medullary syndrome, characterized by: - Ipsilateral hypoglossal nerve palsy - Contralateral hemiparesis - Contralateral proprioceptive loss  Classification of brainstem strokes follows vascular and anatomical localization. Current consensus emphasizes clinical-radiological correlation for precise nosology. Controversies exist in differentiating overlapping syndromes or lesions with atypical presentations, but hypoglossal nerve signs remain a key localizing feature.",
        "classification_and_nosology": "tPA-induced angioedema is classified as a drug-induced adverse reaction with features overlapping with bradykinin-mediated angioedema. It is considered a rare but serious complication of thrombolytic therapy.",
        "management_principles": "The first step in management is to immediately stop the tPA infusion. In mild cases where airway compromise is not imminent, treatment with anti-histamines (H1 blockers) and corticosteroids is recommended to reduce inflammation. Epinephrine may be considered if there are signs of a more typical anaphylactic reaction. However, if there is any concern for airway compromise, securing the airway (with intubation) is imperative. In pregnant or lactating patients, these medications are used with caution but are acceptable when maternal airway protection is needed. Consultation with anesthesia and otolaryngology may be warranted for airway management.",
        "option_analysis": "Option A (Reassurance) is insufficient as the risk of airway compromise requires active intervention. Option B (Intubate) is reserved for cases with significant airway compromise and is not the first-line approach in the absence of severe symptoms. Option C (anti-histamine & steroids) is the appropriate first-line management for mild to moderate angioedema post-tPA, making it the correct answer. Option D is not provided.",
        "clinical_pearls": "\u2022 tPA-induced angioedema is most commonly seen in patients on ACE inhibitors. \u2022 Always monitor for airway compromise and be ready to secure the airway. \u2022 Early cessation of tPA infusion is critical in the management of this complication.",
        "current_evidence": "Recent studies and guidelines emphasize that while the angioedema associated with tPA is bradykinin-mediated, initial management with anti-histamines and steroids remains standard practice, along with vigilant airway monitoring. There is emerging interest in specific bradykinin inhibitors (like icatibant), but these are not yet standard."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993056",
    "fields": {
      "question_number": "228",
      "question_text": "Case of chronic fluctuating paraparesis\nimage attached",
      "options": {
        "A": "(Reassurance) is insufficient as the risk of airway compromise requires active intervention. Option B (Intubate) is reserved for cases with significant airway compromise and is not the first",
        "C": "(anti",
        "D": "is not provided."
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Angioedema is a localized, self\u2010limited edema of the deep dermis and subcutaneous tissues. When it occurs in the context of tPA administration (often in patients with underlying ACE\u2010inhibitor use), it is thought to be secondary to an abnormal release of vasoactive mediators. The clinical scenario requires rapid recognition because swelling of the tongue, lips, or oropharynx can progress to airway compromise.",
        "pathophysiology": "tPA not only lyses fibrin clots but also activates plasmin which can trigger the release of bradykinin. Increased bradykinin levels lead to vasodilation and increased vascular permeability. Although the process is bradykinin\u2010mediated (instead of the classic histaminergic allergic reaction), many of the treatments overlap. In some cases, the reaction may be severe enough to require aggressive airway management.",
        "clinical_correlation": "Patients receiving tPA for ischemic stroke may develop angioedema within the infusion period. Clinically, swelling typically involves the tongue, lips, and sometimes the floor of the mouth. Although it may start as a localized process, rapid progression can lead to difficulty breathing and potential airway loss, especially in patients with predisposing factors such as concurrent ACE inhibitor use.",
        "diagnostic_approach": "This diagnosis is based on clinical observation. The differential includes allergic reaction/anaphylaxis from other agents, or soft tissue infections. In the setting of recent tPA administration and a typical distribution (orolingual), tPA-induced angioedema is the most likely diagnosis. Monitoring for airway patency and assessing progression is critical.",
        "classification_and_neurology": "Spinal vascular malformations are classified broadly into: - Spinal dural arteriovenous fistulas (DAVFs): acquired fistulous connections between dural arteries and medullary veins. - Spinal arteriovenous malformations (AVMs): congenital high-flow intramedullary or perimedullary malformations. - Cavernous malformations (cavernomas): low-flow clusters of dilated capillaries. - Venous malformations and other rare entities.  Fibrocartilaginous embolism is not a vascular malformation but a vascular ischemic event caused by embolism.  The Spetzler classification system and other angiographic schemes help differentiate these lesions based on angioarchitecture and flow dynamics. Recent consensus emphasizes the importance of differentiating DAVFs due to their unique pathophysiology and treatment implications. Controversies remain regarding the nomenclature and optimal subclassification, but the clinical utility of distinguishing DAVFs from AVMs and cavernomas is well accepted.",
        "classification_and_nosology": "tPA-induced angioedema is classified as a drug-induced adverse reaction with features overlapping with bradykinin-mediated angioedema. It is considered a rare but serious complication of thrombolytic therapy.",
        "management_principles": "The first step in management is to immediately stop the tPA infusion. In mild cases where airway compromise is not imminent, treatment with anti-histamines (H1 blockers) and corticosteroids is recommended to reduce inflammation. Epinephrine may be considered if there are signs of a more typical anaphylactic reaction. However, if there is any concern for airway compromise, securing the airway (with intubation) is imperative. In pregnant or lactating patients, these medications are used with caution but are acceptable when maternal airway protection is needed. Consultation with anesthesia and otolaryngology may be warranted for airway management.",
        "option_analysis": "Option A (Reassurance) is insufficient as the risk of airway compromise requires active intervention. Option B (Intubate) is reserved for cases with significant airway compromise and is not the first-line approach in the absence of severe symptoms. Option C (anti-histamine & steroids) is the appropriate first-line management for mild to moderate angioedema post-tPA, making it the correct answer. Option D is not provided.",
        "clinical_pearls": "\u2022 tPA-induced angioedema is most commonly seen in patients on ACE inhibitors. \u2022 Always monitor for airway compromise and be ready to secure the airway. \u2022 Early cessation of tPA infusion is critical in the management of this complication.",
        "current_evidence": "Recent studies and guidelines emphasize that while the angioedema associated with tPA is bradykinin-mediated, initial management with anti-histamines and steroids remains standard practice, along with vigilant airway monitoring. There is emerging interest in specific bradykinin inhibitors (like icatibant), but these are not yet standard."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_18.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993057",
    "fields": {
      "question_number": "229",
      "question_text": "Homonymous hemianopia:",
      "options": {
        "A": "(ACA) is incorrect because the anterior cerebral artery supplies medial frontal and parietal lobes and is not involved in the primary visual pathway. Option b (MCA) is also incorrect because, although the MCA supplies lateral cortex including sensorimotor areas, it generally spares the deep visual pathway structures. Option c (Anterior choroidal artery) is correct as it directly supplies the optic tract and lateral geniculate nucleus, causing homonymous hemianopia when infarcted."
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Homonymous hemianopia is a visual field defect defined by the loss of the same half of the visual field in both eyes. It arises from lesions in the retrochiasmal visual pathways (post-optic chiasm), where the processing of visual information is segregated by visual field.",
        "pathophysiology": "The anterior choroidal artery supplies critical components of the visual pathway including the optic tract, lateral geniculate nucleus, and portions of the internal capsule. An infarction in the territory of the anterior choroidal artery can damage these structures, leading directly to a contralateral homonymous hemianopia. Recent imaging studies and vascular research have confirmed the relevance of this arterial territory in producing isolated or predominantly visual deficits.",
        "clinical_correlation": "Patients with infarcts in the anterior choroidal territory may present with a sudden visual field loss (contralateral homonymous hemianopia) accompanied sometimes by subtle motor or sensory deficits from internal capsule involvement. Recognizing the pattern of visual field loss helps in localizing the lesion to the post-chiasmal visual pathways.",
        "diagnostic_approach": "The evaluation includes formal visual field testing, neuroimaging such as a CT scan or MRI to assess for infarction, and vascular imaging (CTA or MRA) to evaluate the patency of the anterior choroidal artery. Differential diagnoses include occipital lobe infarcts (posterior cerebral artery territory) and lesions affecting the optic radiations.",
        "classification_and_neurology": "Homonymous hemianopia is classified as a type of visual field defect resulting from lesions posterior to the optic chiasm. From a cerebrovascular perspective, strokes are classified by the arterial territory involved: anterior cerebral artery (ACA), middle cerebral artery (MCA), posterior cerebral artery (PCA), and anterior choroidal artery (AChA). The AChA territory is considered a distinct vascular territory due to its unique supply to deep brain structures including parts of the visual pathway. This classification aids in diagnostic localization and management. While the PCA territory is classically associated with occipital lobe infarcts causing homonymous hemianopia, AChA infarcts can produce similar visual deficits due to involvement of the optic tract or LGN. Nosologically, homonymous hemianopia is a syndrome rather than a disease, arising from various etiologies including vascular, neoplastic, or demyelinating lesions affecting the retrochiasmal visual pathway.",
        "classification_and_nosology": "This condition falls under cerebrovascular accidents (ischemic strokes) affecting the small penetrating arteries. It is distinct from strokes of larger vessels (MCA, ACA, PCA) and is classified as a lacunar infarct if limited to deep structures.",
        "management_principles": "Management involves acute stroke protocols including rapid imaging, possible IV thrombolytic therapy if within the therapeutic window, and secondary prevention measures (antiplatelet therapy, blood pressure management, etc.). Pregnancy and lactation require careful consideration of imaging modalities (preferring noncontrast CT in emergencies) and medication safety profiles when selecting antithrombotic therapy.",
        "option_analysis": "Option a (ACA) is incorrect because the anterior cerebral artery supplies medial frontal and parietal lobes and is not involved in the primary visual pathway. Option b (MCA) is also incorrect because, although the MCA supplies lateral cortex including sensorimotor areas, it generally spares the deep visual pathway structures. Option c (Anterior choroidal artery) is correct as it directly supplies the optic tract and lateral geniculate nucleus, causing homonymous hemianopia when infarcted.",
        "clinical_pearls": "\u2022 Homonymous hemianopia localizes the lesion to the post-chiasmal visual pathways. \u2022 Anterior choroidal artery infarcts can also cause subtle motor deficits due to internal capsule involvement. \u2022 Rapid neuroimaging is key in acute visual deficits to distinguish stroke from other causes.",
        "current_evidence": "Current stroke guidelines emphasize early identification and management of small vessel strokes. Recent studies have reinforced the importance of correlating specific visual deficits with vascular territories to guide acute management and appropriate secondary prevention strategies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993058",
    "fields": {
      "question_number": "230",
      "question_text": "56-year-old male with Hx of memory loss for 24 hours & asking the same question repeatedly, investigation",
      "options": {
        "A": "(CT & CTA) is correct because it meets the urgency of diagnosing acute cerebrovascular events and provides both hemorrhage exclusion and vascular assessment. Option b (MRI) while sensitive for ischemia, is less appropriate in the emergency setting due to longer scan times and possible contraindications. The marked answer (B) is therefore incorrect."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "In the setting of an acute neurological deficit (such as memory loss and repetitive questioning) suspected to be due to a cerebrovascular event, rapid imaging is critical for timely diagnosis and management.",
        "pathophysiology": "Acute memory loss in a 56-year-old male raises concern for ischemic events or transient ischemic attacks. The pathophysiological process involves an interruption of blood flow causing neuronal dysfunction. Early identification of hemorrhage versus ischemia is essential, as management diverges drastically between these conditions.",
        "clinical_correlation": "Patients presenting with acute memory loss and repetitive questioning may be experiencing deficits related to ischemia in brain regions responsible for memory (e.g., hippocampal areas or other related structures). The clinical urgency is to rule out hemorrhage and to identify any vascular occlusion that might be amenable to thrombolysis or endovascular intervention.",
        "diagnostic_approach": "The initial imaging study should be a noncontrast CT scan to rapidly exclude hemorrhage, paired with CT angiography (CTA) to evaluate for luminal stenosis or occlusion in the cerebral or cervical arteries. Although MRI, particularly diffusion-weighted imaging, is more sensitive for early ischemic changes, it is less practical in the initial emergency setting because of its longer acquisition time and limited availability.",
        "classification_and_neurology": "This presentation falls under the classification of transient ischemic attack (TIA) or minor ischemic stroke within cerebrovascular disease taxonomy. According to the American Heart Association/American Stroke Association (AHA/ASA), TIAs are defined as transient neurological deficits lasting less than 24 hours without evidence of infarction on imaging. Minor strokes have similar symptoms but with imaging evidence of infarction. The classification system differentiates ischemic cerebrovascular events by duration, imaging findings, and clinical severity. Transient global amnesia is a separate clinical syndrome but can overlap symptomatically. Over time, classification has evolved from purely time-based definitions to tissue-based definitions emphasizing imaging findings. Current consensus favors MRI diffusion-weighted imaging (DWI) to differentiate TIA from minor stroke. This case highlights the importance of early vascular imaging within this nosological framework to guide management.",
        "classification_and_nosology": "This scenario falls under the umbrella of acute stroke evaluation. The algorithm for stroke diagnosis typically prioritizes noncontrast CT followed by CTA in emergency protocols.",
        "management_principles": "According to current stroke guidelines, the initial management of suspected stroke entails rapid noncontrast CT to exclude hemorrhage, followed by CTA to assess for treatable vascular occlusions. These tests determine eligibility for interventions like IV thrombolysis or mechanical thrombectomy. In scenarios involving pregnancy or lactation, imaging protocols may be adjusted to minimize radiation exposure while still providing rapid diagnostic information; noncontrast CT remains acceptable if benefit outweighs risks, and shielding methods can be used.",
        "option_analysis": "Option a (CT & CTA) is correct because it meets the urgency of diagnosing acute cerebrovascular events and provides both hemorrhage exclusion and vascular assessment. Option b (MRI) while sensitive for ischemia, is less appropriate in the emergency setting due to longer scan times and possible contraindications. The marked answer (B) is therefore incorrect.",
        "clinical_pearls": "\u2022 In acute stroke workup, a noncontrast CT scan is the first-line investigation to rapidly rule out hemorrhage. \u2022 CT angiography adds key vascular information that guides interventional decisions. \u2022 Time is brain: rapid imaging is crucial to preserving neurological function.",
        "current_evidence": "Recent guidelines from the American Heart Association/American Stroke Association continue to advocate for CT/CTA as the standard first-line imaging for suspected acute stroke due to its speed, accessibility, and effectiveness in guiding emergency treatment decisions. Research consistently shows that delays in imaging can worsen outcomes in stroke management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993059",
    "fields": {
      "question_number": "231",
      "question_text": "Case about patient with recurrent epistaxis & Telangiectasia over- skin. - mucous membranes - retina & GIT. What to do next:",
      "options": {
        "A": "(Annual MRI brain) is not routinely indicated unless neurological symptoms develop. Option b (Regular BP check",
        "C": "(ECHO) may help screen for pulmonary arteriovenous malformations but does not tackle the GI bleeding risk. Option d (Endoscopy) is the correct next step as it directly evaluates and may treat gastrointestinal telangiectasias responsible for chronic bleeding."
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Hereditary hemorrhagic telangiectasia (HHT) is a genetic disorder that leads to abnormal blood vessel formation. It commonly presents with telangiectasias on the skin, mucous membranes, retina, and gastrointestinal (GI) tract, as well as recurrent bleeding episodes (epistaxis).",
        "pathophysiology": "HHT is caused by mutations (such as in ENG or ACVRL1 genes) that affect angiogenesis, leading to fragile and abnormally dilated vessels (telangiectasias and arteriovenous malformations). These vascular malformations are prone to bleeding, particularly in mucosal and gastrointestinal sites, resulting in chronic blood loss and potential anemia.",
        "clinical_correlation": "Patients with HHT often experience recurrent spontaneous nosebleeds, and the presence of telangiectasias on the skin, retina, and especially in the GI tract points to potential sources of occult bleeding leading to iron deficiency anemia. Identifying GI lesions is crucial for targeted management.",
        "diagnostic_approach": "Diagnostic work-up involves a combination of physical examination, family history, and endoscopic evaluation (such as an upper and lower GI endoscopy) to identify sources of GI bleeding. Differential diagnoses include other causes of GI bleeding (peptic ulcer disease, angiodysplasia, and inflammatory bowel diseases), but the presence of mucocutaneous telangiectasia strongly supports HHT.",
        "classification_and_neurology": "HHT is classified as a rare autosomal dominant vascular disorder within the broader category of hereditary vascular malformation syndromes. The Cura\u00e7ao criteria provide a clinical classification framework: definite HHT (\u22653 criteria), possible (2 criteria), or unlikely (<2 criteria). The nosology places HHT in the family of vascular dysplasia syndromes characterized by AVMs and telangiectasias. Genetic subtypes include HHT1 (ENG mutation) and HHT2 (ACVRL1 mutation), with phenotypic differences such as a higher prevalence of pulmonary and cerebral AVMs in HHT1. This classification aids in prognostication and screening strategies. Competing classifications focus on molecular genetic testing versus clinical criteria, but consensus favors a combined approach. Understanding HHT\u2019s place among neurovascular disorders highlights its relevance to stroke neurology due to AVM-related hemorrhages.",
        "classification_and_nosology": "HHT is classified as a vascular dysplasia and is inherited in an autosomal dominant pattern. It is diagnosed based on clinical criteria (the Cura\u00e7ao criteria) that include epistaxis, telangiectasias, visceral lesions, and family history.",
        "management_principles": "Management of HHT focuses on controlling bleeding and screening for organ involvement. For GI bleeding, endoscopy (option d) is the cornerstone of diagnosis and potential therapeutic intervention (e.g., laser coagulation). Additional management includes iron supplementation, blood transfusions for severe anemia, and sometimes systemic therapies. In pregnancy and lactation, careful management is essential to balance maternal bleeding risks with fetal safety, and endoscopic procedures are performed with appropriate sedation and monitoring.",
        "option_analysis": "Option a (Annual MRI brain) is not routinely indicated unless neurological symptoms develop. Option b (Regular BP check-up) does not specifically address the bleeding risk or source in HHT. Option c (ECHO) may help screen for pulmonary arteriovenous malformations but does not tackle the GI bleeding risk. Option d (Endoscopy) is the correct next step as it directly evaluates and may treat gastrointestinal telangiectasias responsible for chronic bleeding.",
        "clinical_pearls": "\u2022 HHT is strongly suggested by recurrent epistaxis combined with telangiectasias on the skin, mucous membranes, and GI tract. \u2022 Endoscopic evaluation is essential in patients with HHT who have signs of GI bleeding. \u2022 Maintaining a high index of suspicion for AVMs in multiple organ systems is crucial in HHT.",
        "current_evidence": "Recent consensus statements and guidelines for HHT management recommend targeted screening\u2014including endoscopy\u2014for patients with symptoms suggestive of GI involvement, rather than routine annual neuroimaging or cardiac studies in asymptomatic individuals. Current research is also exploring the role of antiangiogenic therapies in reducing bleeding episodes in HHT."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993298",
    "fields": {
      "question_number": "327",
      "question_text": "Patient with radial fracture one month ago came complaining of pain and erythema, the exam was difficult because of pain what is the dx:",
      "options": {
        "A": "Complex regional pain syndrome",
        "B": "Arterial insufficiency",
        "C": "Dejerine Roussy syndrome"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Complex Regional Pain Syndrome (CRPS) is a chronic pain condition that commonly arises after a traumatic event, such as a fracture. It is characterized by persistent pain that is disproportionate to the initial injury, along with sensory, vasomotor, and motor disturbances.",
        "pathophysiology": "The underlying mechanism of CRPS involves a combination of peripheral sensitization, central nervous system changes, neurogenic inflammation, and autonomic dysregulation. Following trauma, an abnormal inflammatory response and maladaptive neuroplastic changes lead to persistent pain, swelling, and skin changes such as erythema.",
        "clinical_correlation": "In patients with a history of a radial fracture who later complains of severe, persistent pain, erythema, and difficulty with examination due to tenderness, CRPS is a leading diagnostic consideration. These symptoms correlate with the typical features of CRPS, such as allodynia, hyperalgesia, and trophic skin changes.",
        "diagnostic_approach": "Diagnosis of CRPS is clinical and based on the widely accepted Budapest Criteria, which include sensory, vasomotor, sudomotor/edema, and motor/trophic findings. Differential diagnoses include arterial insufficiency (which would show diminished pulses and pallor) and post-stroke pain syndrome (Dejerine Roussy syndrome), which is associated with central nervous system lesions rather than post-traumatic changes.",
        "classification_and_neurology": "CRPS is classified within the International Association for the Study of Pain (IASP) taxonomy as a neuropathic pain syndrome with distinct subtypes: Type I (formerly Reflex Sympathetic Dystrophy) without confirmed nerve injury, and Type II (causalgia) with identifiable nerve injury. This classification emphasizes the presence or absence of nerve damage but recognizes overlapping clinical features. The Budapest criteria (developed in 2003 and refined subsequently) are the current gold standard for diagnosis and classification, requiring specific clinical signs and symptoms across sensory, vasomotor, sudomotor/edema, and motor/trophic domains. CRPS falls under the broader category of chronic pain syndromes and autonomic nervous system disorders. Nosologically, it is distinct from neuropathic pain due to nerve injury (e.g., Dejerine-Roussy syndrome) and vascular disorders such as arterial insufficiency, although clinical overlap can occur. The classification system has evolved from purely sympathetic-focused models to a more integrated neuroinflammatory and neuroplasticity framework, reflecting advances in understanding.",
        "classification_and_nosology": "CRPS is classified into two types: Type I (without a confirmed nerve injury) and Type II (with nerve injury). In this case, following a fracture with no specific nerve injury reported, the presentation is consistent with CRPS Type I.",
        "management_principles": "Management of CRPS is multimodal. First-line treatments include physical and occupational therapy to improve function and desensitize the affected limb, along with analgesics such as non-steroidal anti-inflammatory drugs (NSAIDs) and neuropathic agents (e.g., gabapentin). Second-line options include corticosteroids and nerve blocks. In refractory cases, more advanced modalities like spinal cord stimulation may be considered. In pregnancy and lactation, therapeutic decisions require careful evaluation of drug safety profiles, often favoring non-pharmacological interventions and using medications with established safety records.",
        "option_analysis": "Option a (Complex Regional Pain Syndrome) is correct because the symptomatology\u2014persistent pain, erythema, and tactile hypersensitivity following a fracture\u2014fits with a CRPS diagnosis. Option b (Arterial insufficiency) is less likely since it typically presents with diminished pulses and pallor rather than the observed erythema and disproportionate pain. Option c (Dejerine Roussy syndrome) pertains to thalamic pain following stroke, which is unrelated to a recent fracture.",
        "clinical_pearls": "\u2022 CRPS often develops after trauma and is marked by pain that is out of proportion to the injury. \u2022 Early mobilization and multidisciplinary management are key to improving outcomes in CRPS. \u2022 Diagnosis is clinical, using criteria such as the Budapest Criteria to guide evaluation.",
        "current_evidence": "Recent literature emphasizes early intervention in CRPS, with a trend towards integrative pain management strategies including physical therapy, psychological support, and careful pharmacologic management. Updated guidelines strongly advocate for individualized, multimodal treatment plans to reduce chronic pain and functional impairment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993299",
    "fields": {
      "question_number": "328",
      "question_text": "Case of Wilson disease and features of KF ring (greenish and greyish discoloration) the most common feature:",
      "options": {
        "A": "Mania",
        "B": "Psychosis",
        "C": "Depression"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Wilson disease is an autosomal recessive disorder caused by mutations in the ATP7B gene, which leads to defective copper metabolism and toxic copper accumulation in organs such as the liver, brain, and eyes. The detection of Kayser-Fleischer (KF) rings \u2013 copper deposition in the Descemet membrane of the cornea \u2013 is a key clinical clue in patients with neurologic involvement.",
        "pathophysiology": "Due to the ATP7B mutation, copper is not adequately excreted into bile, leading to its accumulation in various tissues. Copper deposition in the basal ganglia and frontal lobes contributes to the neuropsychiatric manifestations, while deposition in the cornea manifests as KF rings. The toxic effects of copper on neuronal metabolism and neurotransmitter pathways are thought to contribute to mood disturbances, including depression.",
        "clinical_correlation": "Patients with Wilson disease may present with hepatic dysfunction, movement disorders, and neuropsychiatric symptoms. Among the psychiatric manifestations, depression is one of the most common, often predating overt neurological deficits. Awareness of these signs is critical for early diagnosis and treatment.",
        "diagnostic_approach": "Diagnosis is based on a combination of findings: a low serum ceruloplasmin level, increased urinary copper excretion, evidence of copper accumulation on liver biopsy, and the presence of KF rings detected with slit-lamp examination. Differential diagnoses include other causes of psychiatric illness or movement disorders; however, the combination with hepatic dysfunction and KF ring findings is highly suggestive of Wilson disease.",
        "classification_and_neurology": "Wilson disease is classified as a hereditary disorder of copper metabolism within the broader category of inborn errors of metabolism and neurogenetic disorders. It falls under the group of metal storage diseases alongside disorders like hemochromatosis and aceruloplasminemia. Nosologically, WD is categorized as an autosomal recessive metabolic encephalopathy with hepatic and neuropsychiatric manifestations.  The Leipzig criteria incorporate clinical, biochemical, and genetic data for diagnosis, emphasizing KF ring presence, low ceruloplasmin, elevated urinary copper, and ATP7B mutations. This classification system reflects an evolution from purely clinical diagnosis to integrated molecular and biochemical criteria. Debates continue regarding screening asymptomatic relatives and the role of genetic testing in diagnosis, but consensus guidelines (e.g., EASL, AASLD) support a structured diagnostic approach combining clinical and laboratory findings.",
        "classification_and_nosology": "Wilson disease falls under the category of metabolic and neurodegenerative disorders. It is classified by its inheritance pattern and its multi-systemic involvement, particularly affecting the liver and brain.",
        "management_principles": "Treatment involves copper chelation with agents such as penicillamine or trientine, zinc supplementation to block copper absorption, and sometimes dietary copper restriction. In patients presenting with neuropsychiatric symptoms, collaborative care including psychiatric management is essential. For pregnancy and lactation, penicillamine and trientine are used cautiously with dosage adjustments and close monitoring; zinc is also considered a safe option during these periods.",
        "option_analysis": "Option A (Mania) and Option B (Psychosis) are recognized neuropsychiatric manifestations in Wilson disease but are less common than mood disturbances. Option C (Depression), which is marked, represents the most frequent psychiatric presentation, making it the correct answer.",
        "clinical_pearls": "1. Kayser-Fleischer rings are nearly pathognomonic for Wilson disease in the presence of neurologic symptoms. 2. Depression is the most common and often early psychiatric manifestation, warranting careful evaluation in young patients with mood disturbances. 3. Early diagnosis and treatment with copper chelation can significantly improve outcomes.",
        "current_evidence": "Recent guidelines emphasize interdisciplinary management including hepatology, neurology, and psychiatry. Advances in imaging and genetic testing have improved early detection, and current research continues to explore optimal dosing regimens for chelation therapy and alternative treatments that minimize adverse effects, especially in women of childbearing potential."
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
