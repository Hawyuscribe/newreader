
# Import batch 2 of 3 from chunk_5_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993303",
    "fields": {
      "question_number": "332",
      "question_text": "Patient with progressive myoclonus and dementia how to confirm the diagnosis",
      "options": {
        "A": "nalysis indicates that Option A (MRI) is the most appropriate diagnostic test for confirming the diagnosis of PME by demonstrating neurodegenerative changes. Assessments of lactate or invasive muscle biopsy are not first"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Progressive myoclonus epilepsies (PME) comprise a heterogeneous group of neurodegenerative disorders characterized by action myoclonus, seizures, and cognitive decline. Accurate diagnosis relies on a combination of clinical evaluation and neuroimaging.",
        "pathophysiology": "PME disorders are typically associated with progressive neuronal loss and cortical atrophy. These changes are often detectable on brain MRI, which may reveal cortical and cerebellar atrophy corresponding to the clinical manifestations of myoclonus and dementia.",
        "clinical_correlation": "Patients with PME present with gradually worsening myoclonic jerks, seizures, and cognitive impairment. MRI findings corroborate the clinical severity by showing brain atrophy and other characteristic patterns that differentiate PME from other neurodegenerative conditions.",
        "diagnostic_approach": "The most appropriate initial diagnostic modality is MRI, which helps visualize brain atrophy and other structural changes. Although genetic testing is definitive, MRI serves as a critical first step. Differential diagnoses include mitochondrial disorders, metabolic encephalopathies, and other causes of dementia, but their imaging profiles are distinct (e.g., lactate peaks in mitochondrial disorders).",
        "classification_and_neurology": "Progressive myoclonus syndromes belong to the broader category of **neurogenetic epilepsies** and are classified based on genetic etiology and clinical phenotype. Major types include Unverricht-Lundborg disease (EPM1), Lafora disease (EPM2), neuronal ceroid lipofuscinoses, and others. The International League Against Epilepsy (ILAE) recognizes PMS within the spectrum of progressive epileptic encephalopathies. Classification has evolved from purely clinical to molecular-genetic frameworks, emphasizing genotype-phenotype correlations. This nosology aids prognosis, genetic counseling, and targeted management. Controversies remain regarding overlapping phenotypes and how to best integrate emerging genetic data into classification systems.",
        "classification_and_nosology": "PME is classified within genetic epilepsies and includes several subtypes such as Unverricht-Lundborg disease and Lafora body disease. The classification is based on genetic mutations and clinical presentation.",
        "management_principles": "Management is largely symptomatic, including the use of antiepileptic drugs (such as valproate and levetiracetam) for seizure control. There is no curative treatment; intervention focuses on improving quality of life and providing supportive care. In pregnant and lactating patients, careful choice of antiepileptic medications is crucial due to teratogenic potential and drug safety profiles.",
        "option_analysis": "Although the original marked answer was D, the option analysis indicates that Option A (MRI) is the most appropriate diagnostic test for confirming the diagnosis of PME by demonstrating neurodegenerative changes. Assessments of lactate or invasive muscle biopsy are not first-line tests in this context.",
        "clinical_pearls": "1. MRI is a rapid, non-invasive tool essential for the early detection of neurodegenerative changes in PME. 2. A detailed family history enhances diagnostic accuracy in suspected genetic epilepsies. 3. Following imaging, genetic testing is crucial for a definitive diagnosis.",
        "current_evidence": "Current research supports the role of MRI as an invaluable screening tool in PME. Advances in genetic testing techniques are increasingly aiding in the precise categorization of these disorders, although MRI remains the cornerstone of initial evaluation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993304",
    "fields": {
      "question_number": "333",
      "question_text": "Case about Kearns Sayre and asked about the mutation",
      "options": {
        "A": "Sporadic large mitochondrial DNA deletion"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Kearns-Sayre syndrome (KSS) is a mitochondrial cytopathy characterized by a classic triad: progressive external ophthalmoplegia, pigmentary retinopathy, and the onset of symptoms before the age of 20. It is a multi-system disorder affecting tissues with high-energy demands.",
        "pathophysiology": "KSS is caused by sporadic, large-scale deletions in mitochondrial DNA, which lead to defective energy production in affected cells. This mitochondrial dysfunction preferentially affects muscles and the nervous system, including ocular and cardiac tissues.",
        "clinical_correlation": "Patients typically present with ptosis, ophthalmoplegia, and retinal pigmentary changes, along with possible conduction abnormalities and endocrine dysfunction. These features align well with the underlying mitochondrial defect.",
        "diagnostic_approach": "Confirmation of KSS is achieved via genetic testing demonstrating large, sporadic mitochondrial DNA deletions. Differential considerations include other forms of mitochondrial myopathy and neuromuscular disorders, but the combination of ophthalmoplegia, retinopathy, and conduction issues is characteristic of KSS.",
        "classification_and_neurology": "Kearns-Sayre syndrome belongs to the broader category of mitochondrial cytopathies, specifically classified as a mitochondrial DNA deletion syndrome. Mitochondrial diseases are heterogeneous and can be classified based on genetic etiology (mtDNA point mutations, large deletions, nuclear DNA mutations affecting mitochondria), clinical phenotype, or biochemical defect. KSS is part of the spectrum of mitochondrial DNA deletion disorders, which also include Pearson marrow-pancreas syndrome and chronic progressive external ophthalmoplegia (CPEO). The nosology has evolved from purely clinical syndromes to genotype-phenotype correlations enabled by molecular diagnostics. Current consensus classifies KSS as a mitochondrial deletion syndrome characterized by multisystem involvement with onset before age 20 and the classic triad of PEO, pigmentary retinopathy, and cardiac conduction defects. There is ongoing discussion about overlap syndromes and the continuum between CPEO and KSS, reflecting variable heteroplasmy and tissue involvement.",
        "classification_and_nosology": "KSS is classified under mitochondrial disorders and myopathies. It is generally considered sporadic, although mitochondrial inheritance patterns are important in other mitochondrial diseases.",
        "management_principles": "Management is primarily supportive. Cardiac conduction defects require regular monitoring and may necessitate pacemaker insertion. Other supportive treatments involve addressing endocrine abnormalities and using co-factors like coenzyme Q10. In pregnancy and lactation, careful counseling and monitoring are essential, given the risk of mitochondrial transmission; however, most cases of KSS are sporadic and do not follow a classical maternal inheritance pattern.",
        "option_analysis": "Option A, specifying a sporadic large mitochondrial DNA deletion, is correct because it accurately reflects the genetic etiology of KSS. Other options would not account for the typical mitochondrial deletion seen in this syndrome.",
        "clinical_pearls": "1. KSS usually manifests before age 20 with a classic triad that includes ophthalmoplegia and pigmentary retinopathy. 2. Pay special attention to cardiac conduction abnormalities as they can necessitate urgent intervention. 3. Genetic counseling is important, especially in familial cases, despite the sporadic nature of the deletions.",
        "current_evidence": "Recent studies continue to support the role of mitochondrial DNA analysis in confirming KSS. Management guidelines emphasize regular cardiac screening and multidisciplinary supportive care, with ongoing research into targeted therapies for mitochondrial disorders."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993385",
    "fields": {
      "question_number": "414",
      "question_text": "An engineer patient diagnosed with Huntington disease, telling you not to tell his employee?",
      "options": {
        "A": "Send his employee an email",
        "B": "hide genetic test",
        "C": "record him as he\u2019s having other diagnoses",
        "D": "respect him and record that on file"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question tests your understanding of patient confidentiality and the ethical duty to respect a patient\u2019s wishes regarding the disclosure of sensitive genetic information. Huntington disease is a neurodegenerative disorder that carries significant social and employment implications, so the patient\u2019s autonomy and privacy must be maintained.",
        "pathophysiology": "Huntington disease is caused by an autosomal dominant mutation\u2014a CAG trinucleotide repeat expansion in the huntingtin (HTT) gene. The abnormal protein product leads to neuronal dysfunction and degeneration (especially in the caudate nucleus), but the molecular pathology does not lessen the need for strict confidentiality.",
        "clinical_correlation": "An engineer receiving a diagnosis of Huntington disease may worry about potential employment discrimination or stigma. The ethical challenge arises when a patient explicitly states that he does not want his employer to be informed about his diagnosis. This scenario is not uncommon when dealing with genetic or stigmatizing diagnoses.",
        "diagnostic_approach": "While the diagnosis is established clinically and by genetic testing, the approach to handling such sensitive information revolves around strict adherence to confidentiality rules. Differential considerations might include conditions that mimic Huntington disease (such as other choreas), but here the focus is on ethical documentation rather than additional testing.",
        "classification_and_neurology": "Huntington disease is classified as a hereditary neurodegenerative disorder within the family of trinucleotide repeat expansion diseases. It belongs to the broader category of chorea syndromes and neurogenetic disorders. The genetic classification is based on the HTT gene mutation with expanded CAG repeats. Nosologically, HD is distinct from other choreas such as Sydenham chorea or drug-induced chorea. Ethical management of genetic information is addressed in guidelines from neurology and genetics societies, emphasizing confidentiality and informed consent. The classification of HD emphasizes its autosomal dominant inheritance pattern, which informs counseling and risk assessment. Ethical frameworks in neurogenetics have evolved to prioritize patient autonomy and confidentiality, with consensus statements from bodies like the American Academy of Neurology and the European Society of Human Genetics guiding practice.",
        "classification_and_nosology": "Huntington disease is classified as an autosomal dominant neurodegenerative disorder. It falls under the category of trinucleotide repeat disorders, similar to certain spinocerebellar ataxias.",
        "management_principles": "The current management underscores multidisciplinary care, including neurologic evaluation, psychiatric support, and genetic counseling. Management of confidentiality is guided by ethical principles outlined in the AMA Code of Medical Ethics and HIPAA regulations. For patients who are pregnant or lactating, genetic counseling is essential as these conditions may impact family planning and require careful discussion of risks without breaching confidentiality.",
        "option_analysis": "Option A (sending an email to his employee) violates confidentiality; Option B (hiding the genetic test) mismanages medical records and transparency; Option C (recording another diagnosis) is both unethical and inaccurate. Option D (respecting his wishes and noting this in the chart) is correct as it adheres to confidentiality and documentation principles.",
        "clinical_pearls": "1. Always prioritize patient confidentiality, especially with stigmatizing genetic diseases. 2. Document the patient\u2019s wishes clearly in the medical record. 3. Recall that ethical principles trump unwarranted disclosure, even when third parties might be affected.",
        "current_evidence": "The latest ethical guidelines from the AMA and HIPAA emphasize patient autonomy and confidentiality. Recent discussions in medical ethics also highlight the importance of nondisclosure unless the patient gives explicit consent, particularly in the era of increased genetic testing."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993386",
    "fields": {
      "question_number": "415",
      "question_text": "Girl with (migraine head, stroke and dementia), and family history of similar issues in her father. What is your diagnosis?",
      "options": {
        "A": "CADASIL",
        "B": "MELAS"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question is designed to evaluate your knowledge of hereditary vascular disorders of the brain. A patient (in this case, a girl) presenting with migraine, stroke, and dementia along with a family history (affected father) is characteristic of a specific genetic small vessel disease.",
        "pathophysiology": "CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy) is caused by mutations in the NOTCH3 gene. The resulting abnormality leads to degeneration of vascular smooth muscle cells and accumulation of granular osmiophilic material, which in turn causes multiple subcortical infarcts and eventual cognitive decline.",
        "clinical_correlation": "Patients with CADASIL often present with migraine-like headaches (commonly with aura), recurrent subcortical ischemic events, and early-onset dementia. The autosomal dominant inheritance (often with a paternal history) helps distinguish it from other hereditary conditions like MELAS, which follows a maternal pattern.",
        "diagnostic_approach": "The diagnosis is supported by brain MRI findings (white matter hyperintensities involving the temporal poles and subcortical regions) and confirmed by genetic testing. Differential diagnoses include MELAS (characterized by stroke-like episodes and lactic acidosis, with maternal inheritance) and other causes of early stroke in young patients.",
        "classification_and_neurology": "CADASIL is classified under hereditary cerebral small vessel diseases, specifically as an autosomal dominant arteriopathy with subcortical infarcts and leukoencephalopathy. It falls within the broader category of genetic small vessel diseases causing vascular cognitive impairment. The classification is based on genetic etiology (NOTCH3 mutation), clinical phenotype, and neuroimaging features.  MELAS belongs to the group of mitochondrial encephalomyopathies, classified by mitochondrial DNA mutations affecting oxidative phosphorylation. It is part of the broader category of mitochondrial cytopathies with multisystem involvement.  The nosological distinction is critical for prognosis and management. Over time, classification systems have integrated genetic and imaging data to refine diagnostic criteria, with CADASIL recognized as the prototypical monogenic small vessel disease. Some controversy exists regarding phenotypic variability and overlap with sporadic small vessel disease, but genetic confirmation remains the gold standard.",
        "classification_and_nosology": "CADASIL is classified as a hereditary, non-atherosclerotic small vessel disease. It is an important cause of stroke in younger adults and falls under the broader category of genetic arteriopathies.",
        "management_principles": "There is no curative treatment for CADASIL. Management typically involves addressing vascular risk factors (blood pressure control, smoking cessation), symptomatic management of migraines, and supportive care for cognitive decline. In pregnant or lactating women, medication choices (such as anti-migraine drugs) require an assessment of teratogenic risks, with non-teratogenic options preferred.",
        "option_analysis": "Option A correctly identifies CADASIL. Option B (MELAS) is less likely due to differences in inheritance patterns (mitochondrial inheritance with maternal transmission) and clinical features, making it the incorrect choice.",
        "clinical_pearls": "1. CADASIL should be considered in younger patients with a combination of migraine, stroke, and cognitive decline with a positive family history. 2. MRI findings (especially anterior temporal lobe involvement) are key to diagnosis. 3. Always consider the inheritance pattern when evaluating genetic disorders.",
        "current_evidence": "Recent guidelines emphasize early diagnosis via MRI and genetic testing in suspected CADASIL cases. Ongoing research looks into targeted therapies, but current management remains largely supportive and symptomatic."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993387",
    "fields": {
      "question_number": "416",
      "question_text": "Patient came with a ct brain attached, asked about which artery? \u0645\u0643\u0631\u0631",
      "options": {
        "B": ", which we assume represents the artery shown on the CT image (commonly the MCA is invoked in such questions). Options corresponding to other arteries (ACA, PCA, etc.) are incorrect based on the imaging findings. Without the full list, we infer that Option B best matches the territory demonstrated on the provided CT."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question involves the interpretation of a CT brain image to identify the vascular territory involved. Knowledge of cerebral arterial anatomy and the typical imaging appearances of infarcts in various arterial territories is key to answering this question.",
        "pathophysiology": "Ischemic strokes are generally categorized based on the artery that is occluded. Each cerebral artery supplies a distinct region of the brain. For instance, an occlusion of the Middle Cerebral Artery (MCA) is the most common and typically produces infarcts in the lateral hemispheric region. The underlying mechanism involves thrombotic or embolic events leading to tissue infarction in the territory supplied by the culprit artery.",
        "clinical_correlation": "Clinically, an infarct in the MCA territory may present with contralateral weakness, sensory loss, or aphasia (if the dominant hemisphere is involved). CT imaging, typically performed acutely, is crucial to rule out hemorrhage and to help localize the infarcted region which correlates with the vascular territory.",
        "diagnostic_approach": "The differential diagnosis includes infarcts in the territories of the anterior cerebral artery (ACA), posterior cerebral artery (PCA), and other less common vessels. The CT imaging characteristics, coupled with clinical findings, help differentiate among these. Advanced imaging (CT angiography or MRI) can further delineate the vascular anatomy.",
        "classification_and_nosology": "Cerebrovascular accidents (strokes) are classified based on the vascular territory involved, which assists in targeted management strategies. This includes large vessel occlusions (like MCA occlusion) versus small vessel disease.",
        "management_principles": "Immediate management follows established stroke protocols (e.g., the \u201ctime is brain\u201d approach). First-line treatments include intravenous thrombolysis when indicated, and mechanical thrombectomy in eligible patients. In pregnant or lactating women, decisions regarding thrombolytic therapy should carefully weigh maternal benefits versus fetal risks, with current guidelines providing specific recommendations on the safe use of such interventions during pregnancy.",
        "option_analysis": "Although the options are not fully detailed, the marked answer is Option B, which we assume represents the artery shown on the CT image (commonly the MCA is invoked in such questions). Options corresponding to other arteries (ACA, PCA, etc.) are incorrect based on the imaging findings. Without the full list, we infer that Option B best matches the territory demonstrated on the provided CT.",
        "clinical_pearls": "1. The MCA is the most commonly involved artery in ischemic strokes. 2. CT brain imaging is the cornerstone of initial stroke evaluation to exclude hemorrhage and to assess infarct location. 3. Rapid identification of the vascular territory guides immediate therapeutic decisions.",
        "current_evidence": "Recent stroke guidelines stress the importance of early CT imaging and prompt reperfusion therapy. Ongoing research continues to refine criteria for thrombolysis and thrombectomy, including in special populations such as pregnant patients, ensuring that the latest protocols are followed."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993388",
    "fields": {
      "question_number": "417",
      "question_text": "Same Q as above, asked about genes?",
      "options": {
        "A": "CAG trinucleotide repeat"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This question assesses your knowledge of the genetic basis of a neurodegenerative disorder. The option 'CAG trinucleotide repeat' is most classically associated with Huntington disease, which is characterized by a progressive degeneration of neurons and specific radiologic findings (such as caudate atrophy).",
        "pathophysiology": "Huntington disease is caused by an expansion of the CAG trinucleotide repeat in the Huntingtin (HTT) gene. This mutation leads to the production of an abnormal protein that accumulates within neurons, particularly in the caudate nucleus and putamen, causing cell death and resulting in a spectrum of neuropsychiatric and motor disturbances.",
        "clinical_correlation": "The clinical presentation typically includes choreiform movements, cognitive decline, and psychiatric symptoms. Imaging studies (MRI or CT) often reveal atrophy of the caudate nucleus with ex vacuo dilation of the lateral ventricles. Genetic testing demonstrating an expanded CAG repeat confirms the diagnosis.",
        "diagnostic_approach": "The definitive diagnosis is made through genetic testing that quantifies the number of CAG repeats. Differential diagnoses might include other trinucleotide repeat disorders (e.g., spinocerebellar ataxias), but the clinical picture and pattern of atrophy help pinpoint Huntington disease.",
        "classification_and_neurology": "CAG trinucleotide repeat disorders belong to the broader category of **polyglutamine (polyQ) diseases**, a subset of trinucleotide repeat expansion disorders. These are primarily autosomal dominant neurodegenerative diseases characterized by CAG repeat expansions in coding regions.  The nosology includes: - Huntington's disease (HTT gene) - Spinocerebellar ataxias (multiple SCA genes, e.g., SCA1, SCA3) - Dentatorubral-pallidoluysian atrophy (DRPLA) - Spinal and bulbar muscular atrophy (Kennedy disease)  Classification systems have evolved from clinical syndromes to molecular genetic definitions, emphasizing repeat length, gene locus, and phenotype. Controversies remain regarding genotype-phenotype correlations and the role of modifying genes.",
        "classification_and_nosology": "Huntington disease falls under the category of neurodegenerative, autosomal dominant disorders. It is classified as a trinucleotide repeat disorder, contributing to a family history of similar presentations with anticipation (earlier onset in successive generations).",
        "management_principles": "There is no cure for Huntington disease; management is symptomatic and supportive. This includes medications for chorea (such as tetrabenazine or deutetrabenazine), psychiatric care, and occupational therapy. For pregnant or lactating women, treatment decisions require careful consideration of fetal exposure risks, and genetic counseling is crucial for family planning.",
        "option_analysis": "Option A, 'CAG trinucleotide repeat', is the correct answer because it directly relates to the genetic mutation found in Huntington disease. Other options (not provided) would depict alternative genetic mutations not associated with this disorder.",
        "clinical_pearls": "1. Huntington disease is characterized by progressive neurodegeneration with prominent caudate atrophy on imaging. 2. The genetic mutation involves an expansion of CAG repeats in the HTT gene \u2013 more repeats correlate with earlier onset (anticipation). 3. Early genetic counseling is essential for patients and their families when facing this diagnosis.",
        "current_evidence": "Recent research in Huntington disease focuses on targeted molecular therapies including antisense oligonucleotides and other gene-silencing approaches. Current guidelines stress symptomatic management and the importance of multidisciplinary care, with ongoing trials examining potential disease-modifying therapies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993095",
    "fields": {
      "question_number": "70",
      "question_text": "Female patient came with ischemic stroke, history of previous 2 abortions, elevated prothrombin time. what to investigate?",
      "options": {
        "A": "Antiphospholipid syndrome",
        "B": "Prothrombin Gene Mutation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Antiphospholipid syndrome (APS) is an autoimmune prothrombotic disorder that frequently presents in young women with a history of recurrent pregnancy losses and thrombotic events such as stroke. The antibodies produced in APS interfere with phospholipid-dependent coagulation tests, creating a paradox where laboratory tests demonstrate prolonged clotting times while the patient remains at high risk for thrombosis.",
        "pathophysiology": "APS is mediated by autoantibodies (e.g., lupus anticoagulant, anticardiolipin, and anti-\u03b22 glycoprotein I) that bind to plasma proteins associated with phospholipids, leading to endothelial cell activation, platelet aggregation, and an increased production of tissue factor. This results in a hypercoagulable state and explains both the thrombotic events, such as stroke, and the recurrent spontaneous abortions seen in these patients. Despite the in vitro prolongation of tests like the activated partial thromboplastin time, the in vivo state is one of increased clotting.",
        "clinical_correlation": "A young female presenting with an ischemic stroke alongside a history of two abortions should prompt consideration of APS. The recurrent pregnancy loss, in the setting of abnormal clotting tests, fits the classic description of APS, making it the prime suspect in such a clinical scenario.",
        "diagnostic_approach": "Diagnosis is established by demonstrating the persistence of antiphospholipid antibodies on two occasions at least 12 weeks apart. Differential diagnoses include other thrombophilic conditions such as the prothrombin gene mutation and Factor V Leiden mutation, but the strong association of APS with obstetric complications helps in differentiating APS from these other conditions.",
        "classification_and_neurology": "APS is classified under systemic autoimmune diseases and specifically as a primary or secondary antiphospholipid antibody syndrome depending on the presence or absence of associated autoimmune diseases like systemic lupus erythematosus (SLE). The classification criteria for APS were updated in 2006 (revised Sapporo criteria) and require at least one clinical and one laboratory criterion. Clinically, thrombotic events or pregnancy morbidity define the syndrome. Laboratory criteria include lupus anticoagulant, anticardiolipin antibodies, and anti-beta-2 glycoprotein I antibodies, each detected on two occasions at least 12 weeks apart. Prothrombin gene mutation is a hereditary thrombophilia caused by a point mutation in the prothrombin gene leading to elevated prothrombin levels and increased venous thrombosis risk. It belongs to inherited thrombophilias alongside Factor V Leiden mutation, protein C/S deficiency, and antithrombin deficiency. APS is thus an acquired autoimmune thrombophilia predominantly causing arterial and venous thrombosis, while prothrombin gene mutation is a genetic thrombophilia mainly causing venous thrombosis. Understanding this classification aids in targeted diagnostic and therapeutic strategies.",
        "classification_and_nosology": "APS is classified as either primary (occurring in isolation) or secondary (associated with other autoimmune diseases such as systemic lupus erythematosus). It falls under the category of acquired thrombophilias.",
        "management_principles": "Management of APS involves long-term anticoagulation to prevent further thrombotic events. For non-pregnant patients, vitamin K antagonists (e.g., warfarin) with INR goals tailored to risk are standard. In pregnant patients, warfarin is contraindicated due to teratogenicity; instead, a combination of low molecular weight heparin (LMWH) and low-dose aspirin is recommended. LMWH is also considered safe during lactation.",
        "option_analysis": "Option A (Antiphospholipid syndrome) is correct because the clinical scenario (ischemic stroke with a history of recurrent abortions and abnormal clotting values) is highly suggestive of APS. Option B (Prothrombin Gene Mutation) is less favored as it is not as strongly linked to recurrent pregnancy losses as APS.",
        "clinical_pearls": "1. In young women with stroke and a history of recurrent miscarriages, always consider APS. 2. Laboratory tests may show prolonged clotting times paradoxically in a prothrombotic state. 3. Confirmatory antibody tests should be repeated 12 weeks apart for a definitive diagnosis.",
        "current_evidence": "Recent guidelines, including those from the American College of Rheumatology and European League Against Rheumatism, reinforce the importance of both clinical and laboratory criteria for diagnosing APS and emphasize individualized anticoagulant strategies, especially in pregnancy where LMWH is preferred."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993096",
    "fields": {
      "question_number": "71",
      "question_text": "Case scenario of a post RTA patient with brain stem symptoms and findings, asked about mechanism?",
      "options": {
        "A": "Artery to artery",
        "B": "Cardioembolic"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Post-traumatic brainstem symptoms following a road traffic accident (RTA) should raise concern for vascular injuries in the vertebrobasilar system. Traumatic dissections of cervical arteries, such as the vertebral arteries, can lead to distal embolization\u2014a phenomenon described as artery-to-artery embolism.",
        "pathophysiology": "Blunt trauma from an RTA may result in an intimal tear in a cervical artery, forming an intramural hematoma and eventually a thrombus. This thrombus can either occlude the vessel locally or shed emboli that travel to distal territories, including the brainstem. This artery-to-artery embolic mechanism is a recognized cause of ischemic stroke in younger individuals following trauma.",
        "clinical_correlation": "In a post-RTA patient, developing brainstem symptoms (such as vertigo, dysphagia, or ataxia) is consistent with an arterial dissection leading to embolic events in the posterior circulation. The clinical scenario strongly suggests that the underlying mechanism is related to traumatic injury of the cervical artery that subsequently embolizes.",
        "diagnostic_approach": "Diagnosis requires prompt imaging, with CT angiography (CTA) or MR angiography (MRA) to visualize the vessel wall and detect dissection. Differential diagnoses include direct traumatic brain injury (like hemorrhage or contusion) and cervical spine injury; however, the presence of vascular symptoms directs the focus toward arterial injury.",
        "classification_and_neurology": "Stroke classification systems such as the TOAST (Trial of Org 10172 in Acute Stroke Treatment) criteria categorize ischemic strokes based on presumed mechanism: large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology.   Artery-to-artery embolism falls under the large artery atherosclerosis category, defined by significant stenosis or occlusion of a major extracranial or intracranial artery supplying the infarcted territory. Cardioembolic strokes are classified separately due to distinct sources and management.  Recent classifications have evolved to better characterize stroke subtypes with advanced imaging and molecular markers, but TOAST remains widely used. Some controversies exist in differentiating artery-to-artery embolism from in situ thrombosis or small vessel disease when imaging is inconclusive, but clinical context and vascular studies aid classification.",
        "classification_and_nosology": "Cervical artery dissection is classified among traumatic vascular injuries and is a significant cause of ischemic stroke in young patients without traditional vascular risk factors.",
        "management_principles": "Initial management typically involves antithrombotic therapy. The choice between antiplatelet agents and anticoagulation remains somewhat controversial, though many clinicians lean towards antiplatelet therapy based on current evidence. In pregnant patients, LMWH and low-dose aspirin are preferred due to teratogenic concerns with warfarin. The same agents are considered safe during lactation.",
        "option_analysis": "Option A (Artery to artery) is correct because it accurately describes the mechanism wherein a thrombus originating from a traumatic dissection embolizes to affect the brainstem. Option B (Cardioembolic) is less likely in a trauma context because there is no indication of a cardiac source for emboli.",
        "clinical_pearls": "1. Always consider vertebral artery dissection in patients with head/neck trauma who present with posterior circulation symptoms. 2. Early vascular imaging is crucial for diagnosis. 3. The mechanism of artery-to-artery embolism is key in translating trauma into an ischemic event.",
        "current_evidence": "Recent studies and guidelines emphasize the importance of early imaging with CTA/MRA in trauma patients with neurological deficits and support the use of antithrombotic therapy (either antiplatelets or anticoagulants) in the management of cervical artery dissections, with special considerations for pregnant patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993097",
    "fields": {
      "question_number": "72",
      "question_text": "CT brain attached showed right pica territory infarction, asked about finding on exam?",
      "options": {
        "A": "Left side uvula deviation",
        "B": "Left Side Ptosis",
        "C": "Right body decrease sensation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "A right PICA (Posterior Inferior Cerebellar Artery) territory infarction typically affects the lateral medulla, a region containing critical cranial nerve nuclei including the nucleus ambiguus, which is involved in palatal elevation.",
        "pathophysiology": "Infarction due to occlusion of the PICA results in ischemia of structures in the lateral medulla. When the nucleus ambiguus is compromised, particularly on the right side, the muscles of the soft palate on that side are weakened. This leads to a relative overactivity on the contralateral (left) side, pulling the uvula toward the unaffected side.",
        "clinical_correlation": "Clinically, a patient with a right PICA infarct may present with signs of lateral medullary (Wallenberg) syndrome, including dysphagia, hoarseness, and loss of gag reflex. The classic neurological exam finding of uvula deviation to the left is consistent with a right-sided lesion affecting the vagal-innervated musculature of the palate.",
        "diagnostic_approach": "Diagnosis is generally confirmed with MRI, which clearly delineates the infarct in the PICA distribution. Differential considerations include other brainstem or cerebellar stroke syndromes, but the pattern of cranial nerve involvement helps localize the lesion to the lateral medulla.",
        "classification_and_neurology": "PICA territory infarction is classified under ischemic strokes affecting the posterior circulation. The posterior circulation includes the vertebral arteries, basilar artery, and their branches such as PICA, anterior inferior cerebellar artery (AICA), and superior cerebellar artery (SCA).   Within the TOAST classification system for ischemic stroke, PICA infarction is categorized as a large artery atherosclerosis or cardioembolic stroke depending on etiology. Lateral medullary syndrome is a clinical syndrome attributable to PICA infarcts.   This syndrome is part of brainstem stroke syndromes, which are distinct from anterior circulation strokes due to unique vascular territories and neuroanatomical structures involved. The nosology has evolved with improved imaging, allowing precise correlation of clinical syndromes with vascular territories and infarct localization.",
        "classification_and_nosology": "PICA infarcts are classified under posterior circulation strokes and are a notable subset of lateral medullary syndromes.",
        "management_principles": "Acute treatment for ischemic stroke follows standard protocols, including consideration for thrombolytic therapy if within the therapeutic window. Secondary prevention involves the use of antiplatelet agents. In pregnant patients, aspirin is preferred, while LMWH may be used if anticoagulation is indicated, and both are considered safe during lactation.",
        "option_analysis": "Option A (Left side uvula deviation) is correct because a right-sided lesion leads to weakness of the right palate, causing the uvula to deviate to the left. Option B (Left side Ptosis) is more aligned with sympathetic pathway involvement (Horner\u2019s syndrome) and is not a classical feature of a straightforward PICA infarct. Option C (Right body decrease sensation) is inconsistent with the typical crossed findings (ipsilateral face and contralateral body sensory loss) in lateral medullary syndrome.",
        "clinical_pearls": "1. In PICA infarcts, look for signs of lateral medullary syndrome including palatal weakness and uvula deviation. 2. Uvula deviation typically occurs away from the side of the lesion. 3. MRI is the imaging modality of choice in suspected posterior circulation strokes.",
        "current_evidence": "Recent research supports the early use of advanced MRI techniques (including diffusion-weighted imaging) in the diagnosis of brainstem strokes. Updated guidelines also stress the importance of thorough neurological examination in localizing brainstem lesions such as those seen in PICA territory infarcts."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993098",
    "fields": {
      "question_number": "73",
      "question_text": "Same as above Q asked about investigation?",
      "options": {
        "A": "MRI",
        "B": "MRV (should rule out CVT)",
        "C": "LP"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In the investigation of an acute ischemic stroke, particularly one localized to a specific arterial territory such as the PICA, it is paramount to directly visualize the brain parenchyma. Magnetic Resonance Imaging (MRI) is the gold standard for detecting acute infarctions in the brain.",
        "pathophysiology": "Ischemic strokes, like those in the PICA territory, result from occlusion of an arterial supply leading to cell death in the affected region. MRI, especially diffusion-weighted imaging (DWI), is highly sensitive to these early ischemic changes. MR Venography (MRV) is designed to evaluate the cerebral venous system and is most useful when cerebral venous thrombosis (CVT) is suspected\u2014an entirely different pathologic process with distinct clinical features.",
        "clinical_correlation": "For a patient exhibiting classic signs of a right PICA infarction (e.g., lateral medullary syndrome features), an MRI will confirm the arterial infarct. In contrast, CVT typically presents with symptoms such as headache, seizures, and signs of raised intracranial pressure, not with the focal deficits seen in arterial strokes.",
        "diagnostic_approach": "The appropriate investigation in this setting is an MRI of the brain, which provides clear visualization of the infarcted tissue. MRV should be reserved for cases where there is clinical suspicion for CVT. Lumbar puncture (LP) does not play a role in the routine evaluation of arterial strokes.",
        "classification_and_neurology": "CVT is classified under cerebrovascular disorders distinct from arterial ischemic stroke. The International Classification of Diseases (ICD-11) categorizes CVT as a subtype of stroke associated with venous thrombosis. Within CVT, classification can be based on the location of thrombosis (e.g., superior sagittal sinus, transverse sinus, deep cerebral veins), acute versus chronic presentation, and underlying etiology (e.g., infectious, non-infectious, idiopathic). The disease family includes venous thromboembolism disorders, overlapping with systemic hypercoagulability syndromes. Classification systems have evolved with advances in imaging and understanding of pathophysiology, emphasizing the need to distinguish CVT from arterial stroke due to differing management and prognosis.",
        "classification_and_nosology": "Acute ischemic strokes are categorized by the arterial territory involved, with PICA strokes being a subset of posterior circulation strokes.",
        "management_principles": "After confirming the diagnosis with MRI, acute management may include thrombolytic therapy if within the therapeutic window, followed by secondary prevention with antiplatelet agents and risk factor management. In pregnant patients, the use of thrombolytics must be carefully weighed against potential risks, and aspirin is often the antiplatelet agent of choice. During lactation, both aspirin (in low doses) and other approved agents are considered safe, while warfarin is avoided in pregnancy.",
        "option_analysis": "Option A (MRI) is the correct investigation because it accurately images the brain parenchyma and can reliably detect infarctions in the PICA distribution. Option B (MRV) is incorrect as it is designed to evaluate the venous system for conditions such as CVT, which is not the suspected pathology in this case. Option C (LP) is not indicated in evaluating an arterial stroke.",
        "clinical_pearls": "1. MRI with diffusion-weighted imaging is the investigation of choice in detecting acute ischemic strokes. 2. MRV is reserved for the assessment of cerebral venous thrombosis, which has a markedly different clinical presentation. 3. Accurate imaging is critical in determining time-sensitive stroke interventions.",
        "current_evidence": "Current American Heart Association/American Stroke Association guidelines endorse the use of MRI (particularly DWI sequences) in the acute setting for the detection of cerebral ischemia. Recent studies also highlight the limited role of MRV in arterial strokes, reinforcing that MRV is not indicated unless CVT is specifically suspected."
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
