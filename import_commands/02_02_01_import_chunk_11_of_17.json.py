
# Import batch 1 of 3 from chunk_11_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993335",
    "fields": {
      "question_number": "364",
      "question_text": "Stroke and diagnosed with acute ischemic stroke, patient undergone work up and her vessels imaging showed atherosclerotic disease however no critical stenosis, ECHO is normal except for an EF of 55%, 8-hour Holter did not show any arrhythmia, HBA1C and lipid profile was accepted. What is the most likely mechanism of her stroke?",
      "options": {
        "A": "embolism (most likely it wasn\u2019t clear)",
        "B": "hypoperfusion",
        "C": "vessel stenosis",
        "D": "thrombosis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke has several potential mechanisms, including embolic, thrombotic (in situ), hypoperfusion, or due to severe vessel stenosis. When routine investigations fail to reveal a high-grade source, the etiology may be classified as embolic or cryptogenic.",
        "pathophysiology": "Embolic strokes occur when an embolus, originating from the heart or another source, occludes a cerebral artery. In some patients, particularly those who lack identifiable causes like atrial fibrillation, high-grade arterial stenosis, or cardiac thrombi, the stroke is considered embolic in nature\u2014often termed an embolic stroke of undetermined source (ESUS).",
        "clinical_correlation": "The described patient has evidence of atherosclerotic disease but no critical stenosis, a normal echocardiogram with preserved ejection fraction, and no arrhythmias on prolonged monitoring. These findings support the likelihood of an embolic event where the source remains unclear, fitting the profile of a cryptogenic embolism.",
        "diagnostic_approach": "A comprehensive evaluation includes vascular imaging (Doppler ultrasound, CT/MR angiography) to look for significant stenoses, cardiac investigations (echocardiography, Holter monitoring) to search for embolic sources, and laboratory assessments for thrombophilia. Differential diagnoses include hypoperfusion-related strokes (which typically occur in watershed zones) and in situ thrombosis over a ruptured plaque, but the workup in this case points away from these causes.",
        "classification_and_nosology": "This type of stroke falls under the umbrella of embolic strokes, and if no definite source is identified, it is classified as an embolic stroke of undetermined source (ESUS). ESUS represents a subset of cryptogenic strokes that are presumed embolic based on imaging and clinical features.",
        "management_principles": "Current guidelines recommend antiplatelet therapy (e.g., aspirin) as the mainstay for secondary prevention in ESUS, along with aggressive management of vascular risk factors. Although clinical trials have investigated the role of direct oral anticoagulants for ESUS, antiplatelet therapy remains standard unless a clear embolic source is subsequently identified. In pregnant or lactating patients, low-dose aspirin is generally considered safe for stroke prevention.",
        "option_analysis": "Option A (embolic mechanism) is most consistent with the workup findings and the clinical scenario (i.e., an embolic stroke of undetermined source). Option B (hypoperfusion) usually produces watershed infarcts and is associated with systemic hypotension. Option C (vessel stenosis) is less likely given the imaging did not reveal critical stenosis, and Option D (thrombosis from a local clot) is less favored when embolic sources are more likely even if occult.",
        "clinical_pearls": "1. ESUS should be considered when a stroke appears embolic but no high\u2010grade stenosis or cardiac source is identified after a comprehensive evaluation. 2. Management of ESUS focuses on secondary prevention with antiplatelet therapy and risk factor modification.",
        "current_evidence": "Recent clinical trials have explored the role of anticoagulants in ESUS, but current guidelines continue to recommend antiplatelet agents as first-line therapy. Ongoing research may eventually refine the approach, especially in patients with subtle prothrombotic tendencies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993336",
    "fields": {
      "question_number": "365",
      "question_text": "short scenario with attached image of NCS showing drop of amplitude:",
      "options": {
        "A": "Conduction block",
        "B": "Temporal dispersion"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Nerve conduction studies (NCS) evaluate the integrity of peripheral nerves. A key parameter is the amplitude of the compound muscle action potential (CMAP). A significant drop in amplitude across a segment of the nerve suggests that many axons are not contributing normally, often because of a conduction block.",
        "pathophysiology": "Conduction block occurs when demyelination or other pathologic processes prevent the consistent propagation of the nerve impulse across a segment of a nerve. This results in a reduction of the recorded CMAP amplitude distal to the lesion. Temporal dispersion, on the other hand, is characterized by prolonged duration of the CMAP due to variable slowing among individual nerve fibers, which tends to smear out the waveform rather than simply reduce its amplitude.",
        "clinical_correlation": "In conditions such as multifocal motor neuropathy or in some forms of demyelinating neuropathies, conduction block is a key electrophysiological finding that correlates with segmental demyelination. The patient\u2019s nerve conduction study demonstrating a drop in amplitude is highly suggestive of a conduction block.",
        "diagnostic_approach": "Interpretation of NCS involves comparing amplitude, conduction velocity, and waveform morphology. Differential considerations include temporal dispersion (which shows waveform broadening rather than isolated amplitude reduction) and axonal loss (which may also reduce amplitude but tends to affect the entire nerve rather than in a focal block).",
        "classification_and_nosology": "Conduction abnormalities in peripheral neuropathies are generally categorized as demyelinating (where conduction block and temporal dispersion are key findings) versus axonal (characterized by reduced amplitude across the board without significant slowing or dispersion).",
        "management_principles": "Management of conditions showing conduction block depends on the underlying cause. In multifocal motor neuropathy, for example, treatment with intravenous immunoglobulin (IVIg) is first-line. Corticosteroids are typically ineffective or may worsen the condition. In pregnancy or lactation, IVIg is generally considered safe and is often used as a treatment modality for immune-mediated neuropathies.",
        "option_analysis": "Option A (Conduction block) is correct since the drop in amplitude on NCS is most indicative of this phenomenon. Option B (Temporal dispersion) would be characterized by a waveform with increased duration and not solely a drop in amplitude. Options C and D are not provided, making them non-applicable.",
        "clinical_pearls": "1. A focal drop in CMAP amplitude with preserved conduction velocity across other segments is highly suggestive of a conduction block. 2. Differentiating conduction block from temporal dispersion is essential as the management and prognosis of demyelinating versus axonal neuropathies differ.",
        "current_evidence": "Recent electrophysiological studies and guidelines continue to stress the importance of distinguishing conduction block from other NCS abnormalities. In immune-mediated neuropathies, early identification of conduction block facilitates timely treatment, with IVIg being supported by robust evidence and considered safe even during pregnancy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993337",
    "fields": {
      "question_number": "366",
      "question_text": "36-year-old patient who present with memory complaint and visual-spatial defect what is the responsible gene (Alzheimer scenario):",
      "options": {
        "A": "TREM",
        "B": "ubiquitin",
        "C": "EPO4",
        "D": "APP"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Alzheimer\u2019s disease (AD) is a neurodegenerative disorder characterized by progressive memory loss, changes in language and visuospatial function, and other cognitive deficits. In familial (early\u2010onset) AD, specific gene mutations such as those in the amyloid precursor protein (APP) gene drive the pathology. This question, describing a 36\u2010year\u2010old with memory and visuospatial complaints, points toward an early-onset Alzheimer\u2019s picture where mutations in the APP gene are implicated.",
        "pathophysiology": "Mutations in the APP gene result in abnormal processing of the amyloid precursor protein, leading to an overproduction or improper formation of beta-amyloid peptides. These peptides aggregate extracellularly into plaques which, along with neurofibrillary tangles composed of hyperphosphorylated tau protein, contribute to neurodegeneration. Current evidence supports that this cascade of events triggers synaptic dysfunction, oxidative stress, and neuronal death.",
        "clinical_correlation": "Patients with early-onset AD typically present with cognitive deficits including memory impairment and difficulty with visuospatial tasks (which may manifest as problems with navigation or recognizing objects/people). Familial AD that involves APP mutations may present earlier than typical sporadic cases and follow an autosomal dominant inheritance pattern.",
        "diagnostic_approach": "The diagnosis is based on clinical evaluation, cognitive testing, and neuroimaging. Differential diagnoses include frontotemporal dementia, vascular dementia, and other neurodegenerative disorders. In familial cases, genetic testing for APP mutations (as well as presenilin 1 and 2 mutations) can support the diagnosis.",
        "classification_and_nosology": "Alzheimer\u2019s disease is classified as a neurodegenerative disorder and dementia. Early-onset familial AD is a distinct subtype and is often associated with genetic mutations such as APP, PSEN1, and PSEN2, setting it apart from the more common late-onset sporadic form.",
        "management_principles": "Management is primarily symptomatic with cholinesterase inhibitors (e.g., donepezil, rivastigmine) and NMDA receptor antagonists (e.g., memantine). While there is no cure, supportive care and cognitive therapy are added. In the context of pregnancy and lactation, these medications are used with caution. Genetic counseling is recommended for familial cases. Ongoing research into beta-amyloid-targeting immunotherapies is being pursued, although these are not yet standard care.",
        "option_analysis": "Option A (TREM) refers to genes like TREM2, which while associated with an increased risk of AD, are not typically the causative mutation in early-onset familial Alzheimer\u2019s. Option B (ubiquitin) and C (EPO4) are not implicated as causal mutations in AD. Option D (APP) is the gene directly responsible when mutated in early-onset familial Alzheimer\u2019s, making it the correct answer.",
        "clinical_pearls": "1. Early-onset familial Alzheimer\u2019s disease often involves mutations in APP, PSEN1, or PSEN2 and presents at a much younger age than sporadic AD. 2. Visuospatial deficits can be an early sign in certain variants of AD (eg, posterior cortical atrophy).",
        "current_evidence": "Recent studies continue to elucidate the role of APP processing in AD pathogenesis, and emerging immunotherapies targeting beta-amyloid are under investigation. Genetic testing remains an important tool in diagnosing familial cases, with updated guidelines recommending counseling for affected families."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993338",
    "fields": {
      "question_number": "367",
      "question_text": "Essential tremor scenario with asthma rx;",
      "options": {
        "A": "Primidone"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Essential tremor (ET) is one of the most common movement disorders, clinically manifesting as a postural or action tremor affecting the hands and sometimes the head. First-line treatment options typically include non-selective beta-blockers (eg, propranolol) and primidone (a barbiturate).",
        "pathophysiology": "The underlying mechanism of essential tremor is not fully understood, but it is thought to involve abnormal oscillatory activity in the cerebellothalamocortical circuit. This leads to involuntary rhythmic contractions of muscles during voluntary movement or when maintaining a posture.",
        "clinical_correlation": "ET typically presents with bilateral action tremor that worsens with intentional movement. When a patient also has a comorbidity such as asthma, the use of non-selective beta-blockers may exacerbate bronchospasm, thereby making primidone the preferred treatment.",
        "diagnostic_approach": "Diagnosis is clinical, based on history and physical examination. Differential diagnoses include Parkinson\u2019s disease (characterized by rest tremor), dystonic tremor, and tremor from hyperthyroidism. A detailed history can help distinguish ET from these conditions.",
        "classification_and_nosology": "Essential tremor is classified as a neurological movement disorder and is considered an isolated tremor syndrome. It can be familial and has a variable response to medical therapy.",
        "management_principles": "For essential tremor, first-line therapy is often propranolol; however, in patients with contraindications such as asthma, primidone becomes the treatment of choice. Second-line treatments include topiramate and gabapentin. In pregnancy and lactation, primidone must be used with caution due to potential teratogenic effects; however, if needed, it may be used with careful risk-benefit analysis and under close monitoring.",
        "option_analysis": "Option A (Primidone) is correct because it avoids the bronchoconstrictive effects seen with beta-blockers in patients with asthma. The absence of other options reinforces that primidone is the best choice for ET in the setting of asthma.",
        "clinical_pearls": "1. Essential tremor is typically an action or postural tremor and is often familial. 2. Beta-blockers are contraindicated in patients with reactive airway disease such as asthma.",
        "current_evidence": "Recent guidelines continue to support primidone as an effective treatment for essential tremor, particularly in patients who cannot tolerate beta-blockers. Ongoing research into the cerebellothalamocortical circuits may further clarify the pathophysiological basis of ET and lead to novel therapeutic targets."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993339",
    "fields": {
      "question_number": "368",
      "question_text": "Scenario of old pt. Had stroke and became hyperactive, flight of ideas and pressured speech (mania) where will expect the lesion:",
      "options": {
        "A": "Caudate",
        "B": "Thalamus"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Secondary mania following a cerebrovascular accident is a recognized clinical phenomenon. It can occur when a stroke affects brain regions involved in mood regulation. This case describes an elderly patient who developed hyperactivity, flight of ideas, and pressured speech (core features of mania) after a stroke.",
        "pathophysiology": "Disruption of neural circuits, particularly within the frontal\u2013subcortical pathways, can lead to disinhibition and mood dysregulation. Lesions in the basal ganglia, especially the caudate nucleus, have been implicated in secondary mania due to their role in modulating emotional processing and executive function.",
        "clinical_correlation": "Post-stroke mania is uncommon but has been associated with lesions in right hemispheric structures. The caudate nucleus plays a key role in behavioral modulation, and its injury can result in symptoms resembling a manic episode, as seen in the case.",
        "diagnostic_approach": "Evaluation includes a detailed neuropsychiatric assessment in the context of recent stroke. Differential diagnoses include primary bipolar disorder, medication-induced mood changes, and other post-stroke mood disorders. Neuroimaging (CT/MRI) aids in localizing the lesion and correlating it with clinical findings.",
        "classification_and_nosology": "This condition is classified as vascular or secondary mania, which is distinct from primary bipolar disorder due to its clear association with brain lesions following vascular events.",
        "management_principles": "Management of post-stroke mania involves stabilization using mood stabilizers (eg, lithium or valproic acid) and atypical antipsychotics. Tailoring treatment in the elderly is crucial, given the increased risk of adverse effects. In pregnancy or lactation, mood stabilizer choice requires careful risk assessment: for example, lithium may be considered with appropriate monitoring while valproate is generally avoided due to teratogenicity.",
        "option_analysis": "Option A (Caudate) is correct because lesions in the caudate nucleus, particularly in the right hemisphere, have been linked to secondary mania after stroke. Option B (Thalamus) is also in the region of interest but is less commonly cited as the primary site responsible for manic symptoms in post-stroke presentations, making the caudate the better answer here. Missing options (C and D) do not affect the correctness of the selection.",
        "clinical_pearls": "1. Post-stroke mania is a rare but recognized syndrome associated with lesions in the frontal\u2013subcortical circuits, particularly the caudate. 2. Always consider a vascular etiology when new-onset mood changes occur in the elderly following a stroke.",
        "current_evidence": "Recent reviews and case series have reinforced the link between right caudate lesions and the development of mania post-stroke. Neuroimaging studies continue to clarify the involvement of basal ganglia circuits in mood regulation, aiding both diagnosis and management."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993340",
    "fields": {
      "question_number": "369",
      "question_text": "Scenario for GCA what is the most likely mechanism (or artery):",
      "options": {
        "A": "Posterior ciliary artery",
        "B": "RCAO"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Giant Cell Arteritis (GCA) is a systemic vasculitis affecting large and medium-sized arteries, notably those branching from the carotid artery. A critical complication of GCA is vision loss resulting from ischemia of the optic nerve.",
        "pathophysiology": "In GCA, inflammatory infiltration of the arterial wall leads to intimal thickening and luminal narrowing. When this process affects the posterior ciliary arteries, which supply the optic nerve head, it can lead to anterior ischemic optic neuropathy and subsequent visual impairment. This mechanism is central to the pathogenesis of vision loss in GCA.",
        "clinical_correlation": "Patients with GCA often present with new-onset headache, jaw claudication, visual disturbances, and systemic symptoms such as fever and weight loss. The involvement of the posterior ciliary arteries is what typically results in the sight-threatening complications seen in GCA.",
        "diagnostic_approach": "The diagnosis is based on a combination of clinical features, elevated inflammatory markers (ESR and CRP), and confirmatory temporal artery biopsy. Differential diagnoses include other vasculitides, non-arteritic anterior ischemic optic neuropathy, and other causes of sudden vision loss. Prompt recognition is essential given the risk of irreversible blindness.",
        "classification_and_nosology": "GCA is classified as a large-vessel vasculitis. It is grouped with other vasculitides in classifications by the American College of Rheumatology. Most frequently, it affects individuals over 50 years of age and is considered a medical emergency when visual symptoms are present.",
        "management_principles": "First-line treatment for GCA is high-dose corticosteroids, initiated immediately upon suspicion to mitigate the risk of blindness. The use of adjunctive therapies such as low-dose aspirin is common. Newer agents like tocilizumab (an IL-6 receptor inhibitor) have shown promise in recent trials. In pregnant patients, corticosteroids are used when clearly indicated, balancing the maternal benefits against fetal risks, and during lactation, the risk is minimized with careful monitoring.",
        "option_analysis": "Option A (Posterior ciliary artery) is correct because occlusion or inflammation of these arteries is the primary mechanism leading to visual loss in GCA. Option B (RCAO, likely referring to a central retinal artery occlusion variant) is not the typical mechanism in GCA; the pathology primarily involves the posterior ciliary circulation. Options C and D are not provided, making Option A the best choice.",
        "clinical_pearls": "1. Immediate high-dose corticosteroids are crucial in GCA to prevent permanent vision loss. 2. The posterior ciliary arteries are the key vascular structures whose compromise leads to anterior ischemic optic neuropathy in GCA.",
        "current_evidence": "Recent guidelines and large trials, including the GiACTA trial, have supported the use of tocilizumab as an effective adjunctive treatment to steroids in GCA. Emphasis remains on early identification and treatment to prevent complications such as blindness, and ongoing research continues to refine optimal management strategies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993341",
    "fields": {
      "question_number": "370",
      "question_text": "Giant cell arteritis what is next:",
      "options": {
        "A": "Steroid",
        "B": "biopsy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Giant cell arteritis (GCA) is a systemic large\u2010vessel vasculitis primarily affecting the temporal arteries in older adults. It is characterized by headache, jaw claudication, scalp tenderness, and a high risk of vision loss due to ischemic complications.",
        "pathophysiology": "GCA involves granulomatous inflammation with the presence of giant cells in the arterial wall. This leads to luminal narrowing, impaired blood flow, and subsequent ischemia of tissues supplied by affected vessels (notably the optic nerve, which can lead to permanent vision loss).",
        "clinical_correlation": "Patients typically present with new-onset headache, jaw claudication, visual disturbances, and sometimes systemic symptoms such as fever and weight loss. Elevated inflammatory markers (ESR, CRP) further support the clinical suspicion. Delay in treatment can result in irreversible complications such as blindness.",
        "diagnostic_approach": "The diagnosis is supported by clinical findings and laboratory tests. While a temporal artery biopsy is the gold standard for confirmation, it should be performed after initiating treatment because delaying steroids can lead to permanent damage. Key differentials include polymyalgia rheumatica and other vasculitides.",
        "classification_and_nosology": "GCA is categorized under the large vessel vasculitides. It frequently overlaps with polymyalgia rheumatica and is primarily seen in patients over the age of 50.",
        "management_principles": "First-line management for suspected GCA is immediate initiation of high-dose corticosteroids (e.g., prednisone 40-60 mg daily, or IV steroids if there is imminent vision threat). Temporal artery biopsy should be arranged within 1-2 weeks of starting therapy. In select cases, steroid\u2010sparing agents like Tocilizumab are used. Although rare in pregnancy, if encountered, the benefits of steroid use must be weighed against potential risks to the fetus.",
        "option_analysis": "Option A (Steroid) is correct because immediate steroid administration is essential to prevent irreversible complications such as vision loss. Option B (Biopsy), although important for definitive diagnosis, should not delay the initiation of steroids.",
        "clinical_pearls": "1. In suspected GCA, never delay high-dose steroids, as time is vision. 2. Temporal artery biopsy confirms the diagnosis but can be performed after starting steroids. 3. Always check inflammatory markers (ESR/CRP) to support the clinical picture.",
        "current_evidence": "Recent guidelines emphasize urgent treatment with high-dose steroids in suspected GCA to mitigate the risk of blindness. Additionally, newer studies support the adjunctive use of biologics like Tocilizumab, particularly in steroid-dependent cases."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993342",
    "fields": {
      "question_number": "371",
      "question_text": "Scenario of young female with picture of 2 attacks and 2 objective findings came with new relapse of sudden left-sided weakness for 5 days after hx of exhaustion what to do: (or scenario of clinical isolated syndrome not sure)",
      "options": {
        "A": "Start fingolimod",
        "B": "Start interferon",
        "C": "Emergent pulse steroid",
        "D": "MRI brain",
        "E": "MRI?"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Multiple sclerosis (MS) is a chronic autoimmune demyelinating disorder that typically affects young adults, especially females. The condition is marked by episodes of neurological dysfunction (relapses) interspersed with periods of recovery (remission).",
        "pathophysiology": "MS pathogenesis involves T-cell mediated immune responses that target the myelin sheath of central nervous system neurons, resulting in discrete areas of demyelination (plaques). Relapses may be triggered by fatigue, stress, or infections, leading to new inflammatory lesions.",
        "clinical_correlation": "The patient\u2019s history of multiple attacks with objective findings fulfills the criteria for dissemination in time and space. The new onset of sudden left-sided weakness after an exhausting episode suggests an acute relapse, for which prompt therapy is essential to curb inflammatory demyelination and expedite recovery.",
        "diagnostic_approach": "Magnetic resonance imaging (MRI) of the brain and spinal cord with gadolinium is the gold standard for detecting new or active lesions in MS. Although imaging is important for disease monitoring, clinical management of an acute relapse should not be delayed pending MRI findings.",
        "classification_and_nosology": "MS is classified as an inflammatory demyelinating disease with several clinical subtypes, including relapsing-remitting, primary progressive, and secondary progressive. The relapsing-remitting form is most common, particularly in young women.",
        "management_principles": "For acute relapses, the first-line therapy is high-dose intravenous methylprednisolone (typically 1 gram daily for 3-5 days). Disease-modifying therapies (e.g., interferon beta, fingolimod) are used for long-term management, not for immediate relapse treatment. In pregnancy, pulse steroids may be used after a careful risk-benefit analysis, and many long-term disease-modifying drugs are contraindicated.",
        "option_analysis": "Option C (Emergent pulse steroid) is correct as immediate treatment with high-dose corticosteroids is the standard of care for acute MS relapses. Options A and B (starting fingolimod or interferon) are intended for long-term disease modification rather than acute management, and options D/E (MRI) are important diagnostically but do not address the need for prompt relapse treatment.",
        "clinical_pearls": "1. In MS, always use high-dose IV steroids to manage acute relapses. 2. MRI is crucial for diagnosis and monitoring but should not delay urgent treatment. 3. Long-term disease-modifying therapies are separate from acute relapse management.",
        "current_evidence": "Recent studies and guidelines continue to support the use of high-dose IV corticosteroids for acute relapses, emphasizing rapid intervention to minimize irreversible neurological damage. There is ongoing research into refining dosing regimens and exploring the safe use of steroids during pregnancy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993343",
    "fields": {
      "question_number": "372",
      "question_text": "A pediatric patient who presented with expansile spinal cord signal changes with partial enhancement:",
      "options": {
        "A": "Astrocytoma",
        "B": "Ependymoma",
        "C": "Hemangioma"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In pediatric patients, intramedullary spinal tumors are relatively uncommon, with astrocytomas being the most frequently encountered type. These tumors tend to present with cord expansion and mixed signal characteristics on MRI.",
        "pathophysiology": "Spinal astrocytomas originate from glial cells and are often infiltrative in nature. Their growth leads to expansion of the spinal cord with patchy or partial contrast enhancement, reflecting their heterogeneous cellular makeup.",
        "clinical_correlation": "Pediatric patients with spinal astrocytomas may present with progressive neurological deficits such as motor weakness or sensory changes. The MRI finding of an expansile lesion with partial enhancement is a typical radiologic appearance for this type of tumor, as opposed to more well-circumscribed lesions seen with ependymomas.",
        "diagnostic_approach": "MRI is the imaging modality of choice to evaluate intramedullary lesions in the spinal cord. Differentials include ependymoma (often more common in adults and showing homogeneous enhancement) and, less commonly, hemangioma. Clinical context (age, presentation) is crucial in differentiating these conditions.",
        "classification_and_nosology": "Spinal cord astrocytomas are classified under glial tumors and graded via the WHO system. In children, these tumors are most commonly low-grade (WHO grade I or II), although high-grade variants can occur.",
        "management_principles": "The mainstay of treatment is surgical resection with the goal of maximal safe removal while preserving neurological function. Adjuvant radiation or chemotherapy may be considered in cases where the tumor is incompletely resectable or high grade. For patients who are pregnant, management requires multidisciplinary discussion to balance maternal and fetal risks, with non-emergent surgeries potentially delayed or modified.",
        "option_analysis": "Option A (Astrocytoma) is correct because it represents the most common type of intramedullary spinal tumor in children with the described imaging characteristics. Option B (Ependymoma) is more typical in adults, and Option C (Hemangioma) is relatively uncommon in this clinical context.",
        "clinical_pearls": "1. Pediatric intramedullary spinal tumors are most often astrocytomas. 2. Expansile lesions with partial enhancement on MRI are characteristic of astrocytomas in children. 3. Early diagnosis with MRI is vital for planning appropriate surgical management.",
        "current_evidence": "Recent advances focus on improved surgical techniques and targeted therapies for pediatric spinal astrocytomas, with studies evaluating the role of molecular markers in guiding prognosis and treatment strategies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993344",
    "fields": {
      "question_number": "373",
      "question_text": "Vague scenario of pt. With no hx available because no family around brought to ER with decrease level of consciousness and fever (not mentioned rigidity) ct brain and csf normal what to do:",
      "options": {
        "A": "Dantrolene",
        "B": "Acyclovir",
        "C": "Antibiotics",
        "D": "Toxicity screening"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This scenario describes a patient with decreased level of consciousness and fever. Even with normal CT imaging and CSF studies initially, there must be a high index of suspicion for central nervous system infections such as herpes simplex encephalitis (HSE).",
        "pathophysiology": "HSV encephalitis typically involves the temporal lobes and leads to inflammation, edema, and potential necrosis of brain tissue. Early in the course, diagnostic studies including CT and CSF analysis can be deceptively normal, yet the viral replication and immune response are actively causing neuronal injury.",
        "clinical_correlation": "The patient\u2019s presentation with fever and altered mental status, even in the absence of meningeal signs (such as rigidity), raises concern for HSE. Early diagnosis is crucial since delays significantly worsen outcomes.",
        "diagnostic_approach": "The diagnostic workup for suspected HSE includes lumbar puncture with PCR for HSV, electroencephalography (EEG), and potentially repeat imaging. Differential diagnoses include bacterial meningitis (usually with marked CSF abnormalities), toxic/metabolic encephalopathies, and other viral encephalitides.",
        "classification_and_nosology": "HSV encephalitis falls under the broader category of viral encephalitis and is considered a neurologic emergency due to its rapid progression and high mortality if untreated.",
        "management_principles": "The mainstay of management is the immediate initiation of intravenous acyclovir. Guidelines recommend starting acyclovir empirically in any suspected case of HSE, regardless of initial imaging or CSF findings, due to the high risk of morbidity and mortality. In pregnant or lactating women, acyclovir is generally considered safe when used after evaluating the risks and benefits. Empiric antibiotic coverage may also be instituted if bacterial causes are considered, but acyclovir remains critical.",
        "option_analysis": "Option B (Acyclovir) is correct because it targets HSV promptly, which is crucial even when early diagnostic tests are normal. Option A (Dantrolene) is used for conditions like neuroleptic malignant syndrome, Option C (Antibiotics) is more applicable to bacterial infections (which typically would alter CSF findings), and Option D (Toxicity screening) does not address a treatable infectious process.",
        "clinical_pearls": "1. Always initiate acyclovir in cases of suspected HSV encephalitis without waiting for confirmatory tests. 2. Early treatment is associated with better neurological outcomes. 3. Normal early CT and CSF results do not exclude the diagnosis of HSE.",
        "current_evidence": "Current guidelines stress that the decision to begin acyclovir should be made on clinical suspicion alone, as studies have shown that delays in treatment are associated with worse outcomes. Recent research also explores adjunctive therapies and improved diagnostic algorithms to identify early cases of HSE more effectively."
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
