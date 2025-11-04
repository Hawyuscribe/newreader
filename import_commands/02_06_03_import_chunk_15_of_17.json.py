
# Import batch 3 of 3 from chunk_15_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993389",
    "fields": {
      "question_number": "418",
      "question_text": "Male patient present with lacinating pain last for seconds and MRI done showed SCA compress over trigeminal nerve RX?:",
      "options": {
        "A": "Decompressive surgery",
        "B": "carbamazepine"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Trigeminal neuralgia is a chronic pain condition characterized by sudden, brief, and lancinating facial pain in the distribution of the trigeminal nerve. It is often triggered by minimal stimulation such as light touch, speaking, or chewing.",
        "pathophysiology": "The classic form of trigeminal neuralgia is usually caused by a neurovascular conflict, where an artery (commonly the superior cerebellar artery) compresses the trigeminal nerve root, leading to demyelination. This demyelination results in ectopic nerve firing and paroxysmal pain.",
        "clinical_correlation": "Patients typically report episodes of severe, sharp, electric shock-like pain that lasts for seconds. These episodes can be triggered by everyday activities and severely impact quality of life.",
        "diagnostic_approach": "While the diagnosis is primarily clinical, high-resolution MRI can be used to confirm the presence of a vascular loop compressing the nerve. Differential diagnoses include postherpetic neuralgia, dental causes of facial pain, and atypical facial pain syndromes.",
        "classification_and_neurology": "Trigeminal neuralgia is classified under neuropathic facial pain disorders. The International Headache Society (IHS) classifies TN as 'Classical TN' when caused by neurovascular compression without other pathology, 'Secondary TN' when due to an identifiable neurological disease (e.g., multiple sclerosis, tumor), and 'Idiopathic TN' when no cause is identified. This classification helps differentiate treatment approaches and prognosis. Classical TN belongs to the family of cranial neuralgias characterized by paroxysmal neuropathic pain. The nosology has evolved with advances in imaging that allow identification of neurovascular compression, refining the classical versus secondary distinction. Controversies remain regarding the significance of vascular contact without symptoms and the role of central mechanisms in TN pain generation.",
        "classification_and_nosology": "Trigeminal neuralgia is classified as classical (or type I) when pain is paroxysmal and sporadic, and atypical (or type II) when there is a constant dull background pain accompanying the paroxysmal episodes.",
        "management_principles": "First-line treatment is with anticonvulsant medications, with carbamazepine being the drug of choice due to its efficacy in reducing neural hyperexcitability. If patients do not respond or experience intolerable side effects, second-line options include oxcarbazepine, gabapentin, or surgical treatments (such as microvascular decompression) in refractory cases. In pregnant patients, carbamazepine is associated with teratogenicity (FDA Category D) and must be used with caution\u2014alternative agents or careful risk-benefit analysis is advised. For lactating mothers, the use of carbamazepine requires monitoring of the infant due to possible drug exposure via breast milk.",
        "option_analysis": "Option B (carbamazepine) is correct as it is the first-line medical treatment for trigeminal neuralgia. Option A (decompressive surgery) is typically reserved for patients who are refractory to medical management.",
        "clinical_pearls": "1. Trigeminal neuralgia is often described as electric shock-like facial pain triggered by everyday activities. 2. Carbamazepine is the first-line therapy, but surgical options exist for refractory cases.",
        "current_evidence": "Recent studies continue to support carbamazepine as the first-line medication for trigeminal neuralgia, with ongoing research into optimizing dosing strategies and exploring surgical interventions for patients who do not respond adequately to medical therapy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993390",
    "fields": {
      "question_number": "419",
      "question_text": "scenario about child have ?ADHD and (cafe au late ash laf flickers\u2026.) dx?",
      "options": {},
      "correct_answer": "1",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Neurofibromatosis type 1 (NF1) is a genetic neurocutaneous disorder characterized by distinctive skin findings such as caf\u00e9-au-lait macules, neurofibromas, and sometimes associated neurobehavioral issues like ADHD. It is one of the most common genetically inherited disorders affecting the skin and nervous system.",
        "pathophysiology": "NF1 is caused by mutations in the NF1 gene, which codes for neurofibromin\u2014a tumor suppressor protein involved in the regulation of cell growth. Loss of neurofibromin function leads to abnormal cell proliferation and the development of neurofibromas, along with pigmentary skin changes. Additionally, neurodevelopmental issues such as attention deficit hyperactivity disorder (ADHD) are frequently observed.",
        "clinical_correlation": "In pediatric patients presenting with caf\u00e9-au-lait spots and behavioral symptoms such as ADHD, NF1 should be strongly considered. The presence of multiple caf\u00e9-au-lait macules is a hallmark feature of NF1, differentiating it from NF2, which more commonly presents with bilateral vestibular schwannomas and lacks the pigmentary abnormalities.",
        "diagnostic_approach": "Diagnosis of NF1 is primarily clinical, based on NIH diagnostic criteria which include: six or more caf\u00e9-au-lait macules (of a specified size), neurofibromas or a family history, freckling in the axillary/inguinal regions, Lisch nodules, and bony dysplasia. Differential diagnoses include other neurocutaneous syndromes such as NF2 and Legius syndrome, with distinctive features differentiating them.",
        "classification_and_neurology": "Neurofibromatoses are classified as autosomal dominant neurocutaneous syndromes within the broader category of phakomatoses. NF1 (von Recklinghausen disease) and NF2 are distinct entities based on genetic etiology and clinical phenotype. The NIH Consensus Development Conference established diagnostic criteria for NF1 in 1987, which remain the cornerstone for clinical diagnosis. NF2 diagnostic criteria focus on bilateral vestibular schwannomas or family history plus related tumors. While both belong to the neurofibromatosis family, NF1 is more common (~1 in 3000) and NF2 rarer (~1 in 25,000). Recent nosological updates emphasize molecular confirmation and recognize mosaic forms. Controversies exist regarding overlapping features and the spectrum of schwannomatosis, a third related disorder.",
        "classification_and_nosology": "NF1 is classified as a neurocutaneous syndrome or phakomatosis and follows an autosomal dominant pattern with variable expressivity. NF2 is a separate condition characterized by bilateral vestibular schwannomas and lacks key features like caf\u00e9-au-lait spots.",
        "management_principles": "Management of NF1 is multidisciplinary and focuses on monitoring for complications such as optic pathway gliomas, skeletal abnormalities, and learning disabilities including ADHD. Behavioral issues are managed using standard ADHD therapies with consideration of age and individual tolerability; however, potential side effects of medications (e.g., stimulant-associated appetite suppression or sleep disturbances) should be monitored. In pregnant patients with NF1, there is an increased risk of complications such as hypertension and tumor growth, necessitating close surveillance. There are no specific contraindications during lactation, though management should be individualized.",
        "option_analysis": "Option 1 (NF1) is correct because the combination of caf\u00e9-au-lait spots and ADHD is classic for Neurofibromatosis type 1. Option 2 (NF2) is incorrect as it primarily manifests with bilateral vestibular schwannomas and does not typically include the pigmentary or neurobehavioral features seen in NF1.",
        "clinical_pearls": "1. Caf\u00e9-au-lait macules are a key dermatologic clue to NF1 in children. 2. NF1 is frequently associated with neurodevelopmental issues such as ADHD, necessitating early behavioral evaluation and intervention.",
        "current_evidence": "Recent research has focused on genotype-phenotype correlations in NF1 and early intervention strategies for neurodevelopmental disorders. Updated consensus guidelines emphasize regular multidisciplinary screening for complications, including routine ophthalmologic and neurological evaluations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993152",
    "fields": {
      "question_number": "89",
      "question_text": "Case scenario of a patient who came with left PICA? territory infarction (attached CT brain) asked about what\u2019s next?",
      "options": {
        "A": "Neurosurgery consultation",
        "B": "Dual anti-platelet"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "A posterior inferior cerebellar artery (PICA) territory infarction is a type of ischemic stroke affecting the posterior circulation. The mainstay of management for most ischemic strokes, when thrombolysis is not pursued or is contraindicated, is antithrombotic therapy, with current guidelines supporting dual antiplatelet therapy (DAPT) in selected cases (e.g., minor stroke) to reduce early recurrence.",
        "pathophysiology": "Occlusion of the PICA leads to ischemia in the portions of the cerebellum (and possibly lateral medulla) it supplies. The resulting infarction may cause local tissue damage with risk for edema and, in some cases, mass effect. In many cases without large swelling or compressive effects, the infarction is managed medically.",
        "clinical_correlation": "Patients with PICA infarctions can present with symptoms such as vertigo, ataxia, nausea, vomiting, and sometimes features of lateral medullary (Wallenberg) syndrome if the medulla is involved. The clinical picture, along with CT (or MRI) imaging, guides management decisions.",
        "diagnostic_approach": "Initial imaging with non-contrast CT is used to rule out hemorrhage and identify infarction. Differential diagnoses include cerebellar hemorrhage, brainstem lesions, and posterior fossa neoplasms. MRI imaging may provide additional detail if needed. The clinical context (size of infarct, presence of edema) guides whether neurosurgical consultation is later required if there is a risk of brainstem compression.",
        "classification_and_neurology": "Ischemic strokes are classified by vascular territory and etiology. PICA infarcts belong to the category of posterior circulation strokes involving vertebrobasilar arterial territories. Etiologically, strokes are categorized by TOAST classification into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. PICA infarcts often arise from large artery atherosclerosis or arterial dissection. This classification guides management and prognosis. Recent consensus emphasizes the importance of vascular imaging to identify occlusion site and stroke mechanism. The nosology of posterior circulation strokes is evolving with advanced imaging and molecular diagnostics, improving etiologic precision and therapeutic targeting.",
        "classification_and_nosology": "This infarct is classified as an ischemic stroke in the posterior circulation. Depending on detection and severity, strokes can be further categorized into minor versus major strokes, with specific management protocols for each based on evidence\u2010based trials.",
        "management_principles": "For an acute ischemic stroke in a non\u2010thrombolysis candidate or after thrombolysis, current guidelines recommend antiplatelet therapy. In patients with minor stroke (often defined with low NIHSS scores) dual antiplatelet therapy \u2013 typically aspirin plus clopidogrel \u2013 is recommended for a short duration (commonly 21 to 90 days) to reduce early recurrent stroke risk. In patients who are pregnant or lactating, low-dose aspirin is generally considered acceptable when needed; clopidogrel may be used with caution, although risks and benefits should be carefully weighed with specialist consultation.",
        "option_analysis": "Option A (Neurosurgery consultation) is generally reserved for patients with significant cerebellar edema or mass effect leading to neurological deterioration, which is not indicated by the scenario provided. Option B (Dual antiplatelet therapy) is appropriate in the acute ischemic stroke setting for secondary prevention in a minor stroke, making it the correct choice. Options C and D are not provided or not indicated.",
        "clinical_pearls": "\u2022 Dual antiplatelet therapy should be considered in minor ischemic strokes to prevent early recurrence. \u2022 Always assess for signs of cerebellar edema in posterior circulation strokes, which may require urgent neurosurgical intervention. \u2022 Early CT imaging helps differentiate infarction from hemorrhage, guiding management decisions.",
        "current_evidence": "Recent studies, including the CHANCE and POINT trials, have demonstrated that short-term dual antiplatelet therapy can reduce recurrent stroke risk in patients with minor ischemic stroke. Guidelines continue to support this approach while underscoring the need for individualized care based on infarct size and associated complications."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993153",
    "fields": {
      "question_number": "90",
      "question_text": "Cadasil scenario of pt tried stroke dementia migraine asked about how to dx??",
      "options": {
        "A": "(assuming it represents this combined approach) is thus correct. Other options, such as CT brain, skin biopsy alone, CSF analysis, or angiography, are either less sensitive or nonspecific and therefore incorrect."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy) is a hereditary small vessel disease that typically presents with migraine with aura, recurrent strokes, and cognitive decline. The diagnosis relies on recognizing a combination of clinical features, characteristic MRI findings, and confirmatory genetic testing.",
        "pathophysiology": "CADASIL results from a mutation in the NOTCH3 gene, which leads to abnormal accumulation of granular osmiophilic material in the vascular smooth muscle cells and subsequent degeneration. This process causes progressive white matter changes and subcortical infarcts over time.",
        "clinical_correlation": "Patients often present with a triad of migraine (often with aura), recurrent ischemic strokes, and cognitive impairment progressing to dementia. Neuroimaging (MRI) typically shows confluent white matter hyperintensities, particularly in the anterior temporal lobes and external capsules, which is highly suggestive of CADASIL.",
        "diagnostic_approach": "The diagnostic workup for suspected CADASIL begins with MRI of the brain to look for characteristic white matter changes. Differential diagnoses include sporadic small vessel ischemic disease, multiple sclerosis, and other leukoencephalopathies, but the distinct anterior temporal and external capsule involvement helps differentiate CADASIL. Definitive diagnosis is made by genetic testing for mutations in the NOTCH3 gene. Historically, skin biopsy to detect granular osmiophilic material was used but has been largely supplanted by molecular diagnostics.",
        "classification_and_neurology": "CADASIL is classified as a hereditary cerebral small vessel disease (SVD), specifically an autosomal dominant arteriopathy. It belongs to the broader family of genetic small vessel diseases that cause ischemic and hemorrhagic strokes, including CARASIL (recessive), COL4A1-related angiopathies, and Fabry disease. The classification of cerebral small vessel diseases includes:  - **Sporadic small vessel disease:** age-related, hypertensive arteriopathy - **Hereditary small vessel diseases:** CADASIL (NOTCH3 mutations), CARASIL (HTRA1 mutations), etc.  The recognition of CADASIL as a distinct nosological entity is based on genetic, clinical, and radiological criteria. Over time, classification systems have evolved from purely clinical to incorporate molecular genetics, improving diagnostic accuracy. Some controversy exists regarding phenotypic variability and overlap with sporadic SVD, but genetic testing has clarified diagnostic boundaries. Current consensus supports CADASIL as the prototype of hereditary SVD caused by NOTCH3 mutations.",
        "classification_and_nosology": "CADASIL is classified as a hereditary small vessel arteriopathy. It falls under the umbrella of cerebral small vessel diseases (SVD) and is inherited in an autosomal dominant pattern.",
        "management_principles": "There is currently no cure for CADASIL; management is largely supportive and focuses on controlling vascular risk factors. Antiplatelet agents (typically low-dose aspirin) may be prescribed for secondary stroke prevention, and migraine management is symptomatic. In pregnancy, risk factor management should be balanced carefully as some medications may not be safe; low-dose aspirin may be continued if indicated. Lactating mothers should be managed similarly with close consultation from specialists, as most treatments are based on symptomatic control and prevention.",
        "option_analysis": "The correct diagnostic pathway is to perform an MRI brain, which shows characteristic white matter lesions (especially in the anterior temporal lobe and external capsule), followed by genetic testing for NOTCH3 mutations to confirm the diagnosis. Option A (assuming it represents this combined approach) is thus correct. Other options, such as CT brain, skin biopsy alone, CSF analysis, or angiography, are either less sensitive or nonspecific and therefore incorrect.",
        "clinical_pearls": "\u2022 The combination of migraine with aura, recurrent strokes, and cognitive decline in a patient with a family history should prompt consideration of CADASIL. \u2022 MRI findings of anterior temporal lobe and external capsule involvement are highly specific for CADASIL. \u2022 Genetic testing for NOTCH3 mutations remains the gold standard for confirmation.",
        "current_evidence": "Recent research emphasizes the sensitivity of MRI in identifying CADASIL and supports the use of NOTCH3 genetic testing as definitive. Continued studies are aimed at better understanding the natural history and potential therapeutic targets for this progressive disease."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993154",
    "fields": {
      "question_number": "91",
      "question_text": "Picture of MRA Time of float (floating thrombus) and asking what you want to do next ..?? STENOSIS (\u0627\u0644\u0635\u0648\u0631\u0629 \u0627\u0644\u0645\u0648\u062c\u0648\u062f\u0629 \u0641\u064a \u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631 \u0645\u0643\u0627\u0646 \u0641\u064a\u0647\u0627 \u0648\u0645\u0643\u0627\u0646\u0627\u062a \u0648\u0627\u0636\u062d\u0647 \u0628\u0633 \u0647\u0630\u064a \u0627\u0644\u0635\u0648\u0631\u0629 \u0644\u0644\u062a\u0642\u0631\u064a\u0628)",
      "options": {
        "A": "heparin infusion",
        "B": "start hydrocortisone",
        "C": "?surgery",
        "D": "dual or single anti platet"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Promotion",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "A floating thrombus, as seen on an MRA (magnetic resonance angiography), is a thrombotic lesion that is not fully adherent to the vessel wall and carries a high risk of embolization. It is typically associated with significant arterial stenosis.",
        "pathophysiology": "High-grade stenosis can lead to turbulent blood flow, which predisposes the formation of thrombus. A free-floating thrombus is dangerous because parts of it can dislodge and embolize to distal vascular territories, potentially causing transient ischemic attacks or stroke.",
        "clinical_correlation": "Patients may exhibit transient neurological deficits or signs of an acute ischemic event depending on where embolization occurs. The imaging finding of a floating thrombus is considered an emergency due to the risk of stroke from embolic occlusion of distal vessels.",
        "diagnostic_approach": "Non-invasive imaging such as MRA is often used for vascular evaluation. Differential diagnoses include stable atherosclerotic plaque without thrombus, arterial dissection, or vasculitis. The presence of a mobile component (floating thrombus) differentiates it from a fixed plaque, signaling higher embolic risk.",
        "classification_and_neurology": "Floating thrombus in the context of arterial stenosis falls under the broader classification of ischemic stroke etiologies, specifically within the category of large artery atherosclerosis as per the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system. It is considered a high-risk embolic source. This condition is distinct from cardioembolic strokes or small vessel lacunar strokes. The classification emphasizes the source of embolism and vascular pathology. Over time, classification systems have evolved to incorporate imaging findings such as intraluminal thrombus and plaque morphology, refining risk stratification and management. There is consensus that floating thrombi represent an unstable lesion requiring urgent intervention, though debate exists regarding optimal treatment modalities.",
        "classification_and_nosology": "A floating thrombus is classified under acute thrombotic events associated with atherosclerotic stenosis. It represents a dynamic process in the spectrum of cerebrovascular thromboembolic disease.",
        "management_principles": "Immediate anticoagulation with a heparin infusion is the usual first-line treatment to prevent further embolization and allow stabilization of the thrombus. This is typically followed by further imaging and consideration for definitive procedures (such as carotid endarterectomy or stenting) once the acute phase is managed. In pregnant patients, unfractionated heparin or low molecular weight heparin is preferred because they do not cross the placenta; similar principles apply while lactating, as these agents are safe.",
        "option_analysis": "Option A (heparin infusion) is correct because it provides immediate anticoagulation, reducing the risk of thrombus propagation and embolization. Option B (hydrocortisone) is irrelevant for thrombus management. Option C (surgical intervention) may be considered in selected cases and at a later stage once the thrombus is stabilized, and option D (dual or single antiplatelet) does not provide the rapid anticoagulant effect needed in this emergent scenario.",
        "clinical_pearls": "\u2022 A free-floating thrombus is an emergent finding that requires prompt anticoagulation to mitigate the risk of distal embolization. \u2022 Heparin infusion is the first-line management in such cases before contemplating surgical or endovascular interventions. \u2022 Always assess for contraindications to anticoagulation in the acute phase.",
        "current_evidence": "Current literature and guidelines support the initiation of anticoagulation, particularly heparin infusion, as the best initial management for a free-floating carotid thrombus. Ongoing research continues to refine the timing and integration of surgical interventions in the management algorithm."
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
