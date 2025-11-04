
# Import batch 2 of 3 from chunk_4_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993300",
    "fields": {
      "question_number": "329",
      "question_text": "Patient with progressive myoclonus and dementia how to confirm the diagnosis",
      "options": {
        "A": "MRI",
        "B": "Lactate",
        "C": "Muscle biopsy"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "The clinical scenario of progressive myoclonus and dementia is characteristic of a group of disorders known as progressive myoclonic epilepsies (PMEs), among which mitochondrial disorders such as Myoclonic Epilepsy with Ragged Red Fibers (MERRF) are well recognized.",
        "pathophysiology": "MERRF is caused by mutations in mitochondrial DNA that impair oxidative phosphorylation, leading to energy failure and the accumulation of abnormal mitochondria in skeletal muscle. This results in histopathological findings such as ragged red fibers on muscle biopsy. The energy deficiency particularly affects high-demand tissues, including the brain and muscles, contributing to myoclonic seizures, ataxia, and dementia.",
        "clinical_correlation": "Patients typically present with myoclonic jerks, seizures, ataxia, and varying degrees of cognitive impairment. The prominence of myoclonus together with progressive dementia guides clinicians to suspect a mitochondrial etiology.",
        "diagnostic_approach": "While neuroimaging such as MRI may demonstrate non-specific changes, and serum lactate levels may be elevated, the definitive diagnosis of mitochondrial disorders like MERRF is established through muscle biopsy, which reveals ragged red fibers on modified Gomori trichrome staining. Genetic testing can further support the diagnosis by identifying mitochondrial DNA mutations.",
        "classification_and_neurology": "Progressive myoclonus epilepsies (PMEs) represent a group of inherited neurodegenerative disorders characterized by myoclonus, seizures, and cognitive decline. They are classified based on genetic mutations and clinical features into types such as Unverricht-Lundborg disease, Lafora disease, and neuronal ceroid lipofuscinoses. The International League Against Epilepsy (ILAE) classifies PMEs under genetic generalized epilepsies with progressive neurological deterioration. This nosology has evolved with advances in molecular genetics, allowing genotype-phenotype correlations. Controversies exist regarding overlap with other neurodegenerative diseases and categorization based on clinical versus molecular criteria. However, current consensus emphasizes genetic diagnosis supported by clinical and imaging findings to guide precise classification.",
        "classification_and_nosology": "MERRF is classified as a mitochondrial encephalomyopathy. It falls within the broader category of mitochondrial disorders associated with defects in oxidative phosphorylation.",
        "management_principles": "Management is primarily supportive and symptomatic. Seizure control is often achieved with antiepileptic drugs (e.g., levetiracetam, clonazepam) while avoiding those that might worsen mitochondrial dysfunction. Coenzyme Q10 and other mitochondrial supplements may be considered; however, evidence is variable. In pregnancy and lactation, careful selection of antiepileptic drugs that have a better safety profile is essential, and genetic counseling is recommended due to the maternal inheritance of mitochondrial disorders.",
        "option_analysis": "Option A (MRI) is non-specific for diagnosing mitochondrial disorders because while it may show structural or signal abnormalities, it does not provide definitive diagnostic evidence. Option B (Lactate) can be supportive if elevated, but it is neither specific nor confirmatory. Option C (Muscle biopsy) is the gold standard for confirming the diagnosis of MERRF because it directly demonstrates the characteristic pathological findings (ragged red fibers). Therefore, Option C is the correct answer.",
        "clinical_pearls": "1. In suspected mitochondrial disorders with myoclonus and dementia, muscle biopsy remains the cornerstone of diagnosis. 2. Elevated lactate levels support the diagnosis but are not confirmatory. 3. MRI findings are typically non-specific in mitochondrial myopathies.",
        "current_evidence": "Recent studies continue to validate the role of muscle biopsy and genetic analysis in diagnosing mitochondrial diseases. Although biochemical markers such as lactate remain a useful adjunct, the combination of histological findings and mitochondrial DNA sequencing is recommended by current neuromuscular guidelines for a definitive diagnosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993301",
    "fields": {
      "question_number": "330",
      "question_text": "Patient with early-onset Alzheimer what is the gene (presenilin not in the choices):",
      "options": {
        "A": "APP",
        "B": "APOE"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Early-onset Alzheimer\u2019s disease (AD) is a hereditary form of dementia that typically presents before the age of 65. It is most commonly associated with mutations in genes involved in amyloid precursor protein (APP) processing, including APP itself as well as presenilin genes (PSEN1 and PSEN2).",
        "pathophysiology": "Mutations in the APP gene lead to abnormal processing of amyloid precursor protein, resulting in the formation of beta-amyloid plaques. These plaques disrupt neuronal function, trigger inflammatory responses, and contribute to neurodegeneration. When presenilin mutations are not available as an option, APP mutations are implicated as a critical pathogenic factor in early-onset AD.",
        "clinical_correlation": "Patients with early-onset AD present with memory loss, impaired judgment, and changes in behavior. The genetic underpinning in these cases often leads to more aggressive progression of the disease compared to sporadic, late-onset Alzheimer\u2019s.",
        "diagnostic_approach": "Diagnosis is primarily clinical, supported by neuroimaging (e.g., MRI, PET scans) and neuropsychological testing. Genetic testing for mutations in APP, PSEN1, and PSEN2 is used in familial cases. Differential diagnoses include frontotemporal dementia and other hereditary dementias, but the pattern of amyloid plaque deposition favors Alzheimer\u2019s.",
        "classification_and_neurology": "Alzheimer's disease is classified into early-onset (before 65 years) and late-onset forms. Early-onset AD is further divided into familial (genetically confirmed mutations) and sporadic cases. The familial early-onset AD falls within the category of autosomal dominant neurodegenerative disorders with known causative mutations in APP, PSEN1, and PSEN2 genes. Late-onset AD is multifactorial with complex genetic and environmental contributions, with APOE \u03b54 being the strongest genetic risk factor. The National Institute on Aging-Alzheimer's Association (NIA-AA) criteria incorporate clinical, biomarker, and genetic data to classify AD and its stages. This framework helps distinguish causative mutations from risk alleles and guides diagnostic and therapeutic strategies.",
        "classification_and_nosology": "Alzheimer\u2019s disease is classified as a neurodegenerative disorder involving amyloid and tau pathology. Early-onset Alzheimer\u2019s, although less common than the sporadic, late-onset form, has a clear genetic basis in many cases.",
        "management_principles": "Management includes the use of cholinesterase inhibitors and NMDA receptor antagonists (e.g., memantine) to slow the progression of cognitive decline. In early-onset cases, genetic counseling is vital. During pregnancy and lactation, careful evaluation of medication safety is necessary; some cognitive enhancers may require dose adjustments or close monitoring.",
        "option_analysis": "Option A (APP) is correct as mutations in the APP gene can cause early-onset Alzheimer\u2019s disease. Option B (APOE) is associated predominantly as a risk factor for the more common late-onset form rather than being a direct causative mutation in early-onset cases, making Option A the best choice given the exclusion of presenilin genes.",
        "clinical_pearls": "1. APP mutations are a recognized cause of familial early-onset Alzheimer\u2019s disease. 2. APOE is a risk factor for late-onset Alzheimer\u2019s, not a determinative gene in early-onset cases. 3. Early genetic diagnosis can be invaluable for family counseling and management planning.",
        "current_evidence": "Recent research supports the role of APP mutations in the pathogenesis of early-onset AD, and evolving therapies targeting amyloid-beta deposition are a focus of current clinical trials. Genetic testing has become more accessible, supporting its use in selected familial cases."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993073",
    "fields": {
      "question_number": "299",
      "question_text": "Brain MRI is showing unilateral watershed infarction what is the mechanism",
      "options": {
        "A": "ICA stenosis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Watershed infarcts occur in the areas of the brain that lie at the border zones between the major cerebral arterial territories. They are particularly vulnerable to reductions in perfusion, and unilateral involvement typically suggests a localized vascular abnormality.",
        "pathophysiology": "In cases of unilateral watershed infarction, the most common mechanism is severe stenosis of the internal carotid artery (ICA) on the affected side. The stenosis leads to reduced cerebral blood flow in the distal territories, especially under conditions of systemic hypotension or increased metabolic demand, causing ischemia in the border zone regions.",
        "clinical_correlation": "Patients with unilateral watershed infarcts may present with focal neurologic deficits that do not conform strictly to a single major arterial distribution. This pattern should prompt investigation into carotid artery disease as an underlying etiology.",
        "diagnostic_approach": "Evaluation typically includes neuroimaging with MRI to identify the pattern of infarction and vascular imaging (such as CT angiography, MR angiography, or carotid duplex ultrasound) to assess for ICA stenosis. Differential diagnoses include embolic infarcts and small vessel disease, but the watershed pattern is characteristic of hypoperfusion due to proximal stenosis.",
        "classification_and_neurology": "Watershed infarctions are classified within the broader category of ischemic strokes under the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system as large artery atherosclerosis or hemodynamic stroke subtype. They can be further subclassified into cortical (external) and internal watershed infarcts based on MRI findings and anatomical location. This nosological framework helps differentiate watershed infarcts from embolic strokes and small vessel lacunar infarcts. The classification has evolved with advances in neuroimaging, enabling more precise localization and etiological correlation. Some controversy exists regarding the relative contribution of embolism versus hemodynamic compromise in watershed infarctions, but current consensus emphasizes the role of large artery stenosis and hypoperfusion. Understanding these categories is essential for tailoring treatment strategies and prognostication.",
        "classification_and_nosology": "Watershed infarcts are categorized as border zone infarcts, which are distinguished from territorial infarcts caused by embolism or occlusion of a specific large vessel.",
        "management_principles": "First-line management involves optimizing cerebral perfusion and addressing the underlying vascular pathology. Antiplatelet therapy and risk factor modification (control of hypertension, hyperlipidemia, and diabetes) are recommended. In selected patients with significant symptomatic carotid stenosis, revascularization procedures (carotid endarterectomy or stenting) may be considered. In pregnancy and lactation, medical management is generally preferred with careful risk\u2013benefit analysis regarding any invasive intervention.",
        "option_analysis": "Option A (ICA stenosis) is correct as it directly relates to the hemodynamic compromise seen in unilateral watershed infarctions. The other options, though not listed, could include global hypotension which typically causes bilateral infarcts, or embolic phenomena which look different on imaging.",
        "clinical_pearls": "1. Unilateral watershed infarcts should raise suspicion for ipsilateral carotid artery disease. 2. Careful vascular imaging is essential to differentiate watershed infarcts from other types of stroke. 3. Medical management of ICA stenosis includes antiplatelet therapy and risk factor control, with revascularization reserved for selected cases.",
        "current_evidence": "Recent guideline updates emphasize the importance of early carotid imaging for patients with suspected watershed infarcts. Studies continue to refine criteria for carotid revascularization, and the use of less invasive imaging techniques has improved diagnosis and management. In pregnant patients, a conservative approach is typically favored unless the risk of stroke significantly outweighs procedural risks."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_24.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993074",
    "fields": {
      "question_number": "300",
      "question_text": "Patient underwent carotid endarterectomy due to severe symptomatic stenosis and the next day he deteriorated, brain CT is showing right frontal cortical SAH. What is the cause?",
      "options": {
        "A": "Hyperperfusion",
        "B": "Rupture of undiagnosed aneurysm"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Carotid endarterectomy is performed to eliminate high\u2010grade carotid stenosis and reduce stroke risk. However, rapid restoration of blood flow in chronically hypoperfused brain tissue can lead to a dysregulated vasodilatory response, resulting in cerebral hyperperfusion syndrome. This syndrome may manifest with headache, neurological deterioration, and imaging findings such as cortical subarachnoid hemorrhage (SAH).",
        "pathophysiology": "During chronic hypoperfusion, cerebral vessels undergo maximal vasodilation to maintain adequate blood flow. After revascularization, the sudden increase in perfusion pressure overwhelms the impaired autoregulation, leading to leakage of blood components and sometimes frank hemorrhage in the cortical regions. Recent studies emphasize that hyperperfusion can lead to blood\u2013brain barrier disruption and vasogenic edema, culminating in cortical SAH.",
        "clinical_correlation": "Patients usually present with acute neurological deterioration, headache, and sometimes seizures after carotid revascularization. In this case, the right frontal cortical SAH on CT scan corresponds with the territory affected by the altered hemodynamics.",
        "diagnostic_approach": "Primary imaging is non\u2010contrast CT to detect hemorrhagic changes. Differential diagnoses include rupture of a previously undiagnosed intracranial aneurysm or other procedural complications. However, the timing and pattern (cortical SAH in the revascularized territory) point toward hyperperfusion syndrome. Additional investigations may include MRI and angiography to further assess cerebral vasculature if needed.",
        "classification_and_neurology": "Post-CEA cerebral hyperperfusion syndrome is classified under cerebrovascular complications related to revascularization procedures. It is a subtype of reperfusion injury characterized by loss of cerebral autoregulation and resultant hyperemia. Within the broader nosology of stroke and cerebrovascular disorders, CHS is distinct from ischemic stroke, hemorrhagic stroke caused by hypertension or aneurysm rupture, and other causes of SAH. The classification has evolved to recognize CHS as a unique clinical syndrome with specific pathophysiology and management needs, separate from classic SAH etiologies. Contemporary stroke classification systems, such as the TOAST criteria, do not specifically categorize CHS but acknowledge it as a procedural complication. There is ongoing discussion regarding standardized diagnostic criteria for CHS to improve recognition and reporting consistency.",
        "classification_and_nosology": "Cerebral hyperperfusion syndrome is categorized as a reperfusion injury following surgical or endovascular revascularization, distinct from hemorrhagic transformation due to thrombolytic therapy.",
        "management_principles": "The cornerstone of management is strict blood pressure control using intravenous antihypertensives (e.g., labetalol, nicardipine) immediately after diagnosis. Supportive care in an intensive care setting is indicated. For pregnant or lactating patients, medications with established safety profiles (e.g., labetalol) should be preferred, and dosing should be carefully monitored due to altered hemodynamic status.",
        "option_analysis": "Option A (Hyperperfusion) correctly identifies the etiology as the rapid increase in cerebral blood flow overwhelming impaired autoregulation. Option B (Rupture of undiagnosed aneurysm) is less likely given the timing and CT pattern; aneurysmal SAH typically presents with diffuse cisternal blood rather than localized cortical hemorrhage.",
        "clinical_pearls": "1. Always consider hyperperfusion syndrome in patients who deteriorate shortly after carotid revascularization. 2. Early blood pressure management can significantly reduce morbidity. 3. Cortical SAH in the postoperative period is more suggestive of reperfusion injury than aneurysmal rupture.",
        "current_evidence": "Recent guidelines emphasize rigorous blood pressure control post-revascularization and advocate for standardized protocols in monitoring for hyperperfusion syndrome. Contemporary research continues to explore biomarkers that could predict which patients are at increased risk of this complication."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993075",
    "fields": {
      "question_number": "301",
      "question_text": "Locked in syndrome",
      "options": {
        "A": "Ventral pons"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Locked-in syndrome is a neurological disorder characterized by quadriplegia and anarthria with preserved consciousness, typically resulting from a lesion that disrupts motor pathways while sparing the reticular activating system.",
        "pathophysiology": "The ventral part of the pons houses the corticospinal and corticobulbar tracts. An infarct or hemorrhage in this region, commonly due to basilar artery occlusion, interrupts these tracts, rendering the patient 'locked-in.' Despite extensive paralysis, vertical eye movements and blinking are usually preserved because the midbrain structures controlling these functions remain intact.",
        "clinical_correlation": "Clinically, patients appear awake and alert but are unable to move or speak, communicating only through vertical eye movements. This is a direct consequence of damage to the ventral pons, where motor output is disrupted while sensory and consciousness pathways are spared.",
        "diagnostic_approach": "Diagnosis is based on clinical examination supported by neuroimaging (MRI is particularly sensitive). The differential includes coma or severe motor deficits from diffuse brain injury; however, preserved consciousness and specific eye movement patterns are key clues.",
        "classification_and_neurology": "Locked-in syndrome is classified as a brainstem stroke syndrome within the cerebrovascular disease taxonomy. It belongs to the family of motor pathway syndromes caused by focal ischemic lesions.   The classification can be further refined into: - **Classic LIS**: Complete paralysis except vertical eye movement and blinking. - **Incomplete LIS**: Some voluntary movement preserved. - **Total LIS**: Complete immobility including eye movements, often with impaired consciousness.  This nosology has been established through clinical-pathological correlation and imaging studies. LIS is distinct from disorders of consciousness (e.g., coma, vegetative state) and from other brainstem syndromes like Wallenberg syndrome, which affect different vascular territories and pathways.",
        "classification_and_nosology": "Locked-in syndrome is classified under brainstem syndromes and is typically secondary to ventral pontine lesions. It is not a disorder of consciousness but of motor output.",
        "management_principles": "Management is supportive and includes intensive care, prevention of complications (e.g., infections, thromboembolism), and rehabilitation. Early involvement of a multi-disciplinary team is essential. In pregnant or lactating patients, supportive care remains the mainstay with additional considerations for maternal and fetal monitoring if required.",
        "option_analysis": "Option A (Ventral pons) is correct because lesions in this area are classically responsible for locked-in syndrome. Other potential locations would not explain the classic preservation of consciousness with complete motor deficit.",
        "clinical_pearls": "1. Preserved vertical eye movements with complete paralysis strongly suggests locked-in syndrome. 2. Vascular lesions of the ventral pons, often due to basilar artery occlusion, are the most common cause. 3. Despite profound deficits, patients are fully conscious and should be treated with respect and efforts to communicate.",
        "current_evidence": "Current research focuses on innovative rehabilitation techniques and augmentative communication strategies for locked-in syndrome, as well as on developing neuroprotective strategies during the acute phase to minimize pontine damage."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993076",
    "fields": {
      "question_number": "302",
      "question_text": "Large acute MCA stroke and history of Afib what to give for acute management",
      "options": {
        "A": "Aspirin"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Acute management of ischemic stroke centers on rapid restoration of cerebral blood flow to save ischemic brain tissue. In patients with a large middle cerebral artery (MCA) stroke, timely administration of reperfusion therapies is essential, particularly if the etiology is cardioembolic, as in atrial fibrillation (Afib).",
        "pathophysiology": "In a cardioembolic stroke, a clot originating from the heart occludes a cerebral vessel. For large vessel occlusions, the resulting ischemia can progress rapidly to infarction. The most beneficial acute interventions aim to lyse or physically remove the clot to restore perfusion. The primary risk with delayed or inappropriate therapy (e.g., giving only antiplatelet agents) is continued infarction and a higher risk of hemorrhagic transformation.",
        "clinical_correlation": "Patients with large MCA strokes typically present with significant neurological deficits such as hemiplegia, aphasia (if the dominant hemisphere is affected), and visual field deficits. The presence of Afib strongly suggests a cardioembolic cause, which reinforces the need for rapid reperfusion therapy rather than solely antiplatelet therapy.",
        "diagnostic_approach": "Initial evaluation with non-contrast CT is performed to rule out hemorrhage, followed by CT angiography (CTA) to assess vessel occlusion. Differential diagnoses include lacunar infarcts or hemorrhagic stroke, but clinical context and imaging findings in large MCA territory point to a cardioembolic large vessel occlusion.",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology using systems such as the TOAST criteria:  - Large artery atherosclerosis - Cardioembolism (e.g., Afib) - Small vessel occlusion (lacunar) - Stroke of other determined etiology - Stroke of undetermined etiology  Cardioembolic strokes, including those caused by Afib, are characterized by sudden onset, often severe deficits, and a high risk of early recurrence. This classification guides management and prognosis. The current consensus emphasizes the importance of identifying cardioembolic sources to tailor secondary prevention, particularly anticoagulation therapy.",
        "classification_and_nosology": "Ischemic strokes are broadly classified as thrombotic, embolic (often cardioembolic), or lacunar. Cardioembolic strokes due to Afib are considered high-risk for recurrence and are managed differently from other types.",
        "management_principles": "For eligible patients within 4.5 hours of stroke onset, first-line management is intravenous thrombolysis with tissue plasminogen activator (tPA), provided there are no contraindications. For large vessel occlusions, mechanical thrombectomy is often the next step. Aspirin is typically used later for antiplatelet therapy once reperfusion strategies are complete and after a waiting period (usually 24 hours post-thrombolysis) to minimize hemorrhagic risk. In pregnant or lactating patients, thrombolytic therapy may be considered if the benefits outweigh the risks, with careful monitoring and consultation with maternal\u2010fetal medicine specialists.",
        "option_analysis": "Option A (Aspirin) is incorrect in the hyperacute management of a large MCA stroke, especially when the patient is within the window for reperfusion therapies. The correct acute intervention is intravenous thrombolysis (typically represented in alternative answer options as IV tPA), with thrombectomy considered if large vessel occlusion is confirmed. Since the marked answer was Aspirin, it does not align with the standard of care for eligible patients.",
        "clinical_pearls": "1. 'Time is brain'\u2014rapid administration of reperfusion therapy is critical in large vessel occlusions. 2. In cardioembolic strokes from Afib, reperfusion (via IV tPA and/or mechanical thrombectomy) is the priority over antiplatelet therapy in the acute phase. 3. Aspirin is generally deferred until at least 24 hours after thrombolytic therapy to reduce hemorrhagic risk.",
        "current_evidence": "Recent guidelines from the American Heart Association and European Stroke Organisation strongly support the use of IV thrombolysis within 4.5 hours of symptom onset and mechanical thrombectomy for eligible patients with large vessel occlusion. Emerging evidence also addresses careful patient selection to minimize hemorrhagic transformation, even in large infarcts."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993077",
    "fields": {
      "question_number": "303",
      "question_text": "Brain MRI is showing unilateral watershed infarction what to order?",
      "options": {
        "A": "CTA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Watershed infarctions occur in regions of the brain that lie at the junctions of major vascular territories. These infarcts are typically a result of hypoperfusion and can be indicative of significant carotid artery disease when they occur unilaterally.",
        "pathophysiology": "Watershed zones have a dual supply from adjacent arterial territories and are thus vulnerable to systemic hypotension or hemodynamic compromise. Unilateral watershed infarcts raise suspicion for ipsilateral carotid artery stenosis or occlusion, which diminishes perfusion pressure, especially during episodes of low systemic blood pressure.",
        "clinical_correlation": "The clinical presentation in patients with watershed infarcts often includes transient or fluctuating neurological deficits that may correspond to fluctuating cerebral perfusion. Unilateral findings particularly prompt evaluation of the carotid artery ipsilateral to the infarct.",
        "diagnostic_approach": "After initial MRI findings of a unilateral watershed infarct, vascular imaging is the next step to evaluate for carotid pathology. Options include CT angiography (CTA), MR angiography (MRA), or carotid duplex ultrasonography. The differentiation from embolic strokes lies in the distribution and border-zone pattern seen on imaging.",
        "classification_and_neurology": "Watershed infarctions are classified under ischemic strokes within the broader cerebrovascular disease taxonomy. According to the Trial of Org 10172 in Acute Stroke Treatment (TOAST) classification, watershed infarcts are often categorized as due to large-artery atherosclerosis or hemodynamic stroke subtype. The infarcts can be further subclassified based on location: cortical (external) watershed infarcts occurring at the junction of major cortical territories, and internal watershed infarcts located in the subcortical white matter between deep and superficial arterial systems. This classification aids in etiological diagnosis and management decisions. Over time, classifications have evolved to incorporate imaging patterns and hemodynamic assessments, recognizing that watershed infarcts represent a heterogeneous group with distinct pathophysiology. Current consensus emphasizes integrating clinical, imaging, and vascular studies to refine stroke subtype classification, which directly influences treatment strategy.",
        "classification_and_nosology": "Watershed infarctions are classified based on their location (cortical or internal) and are considered a manifestation of hemodynamic compromise rather than thromboembolic phenomena.",
        "management_principles": "The evaluation of a unilateral watershed infarction includes vascular imaging to assess for carotid stenosis. Management depends on the severity of carotid disease: medically managed with antiplatelet agents and statins for moderate stenosis, or consideration of revascularization procedures (endarterectomy or stenting) for high-grade stenosis. In pregnant or lactating patients, non-invasive imaging such as duplex ultrasound or MRI/MRA is preferred to avoid ionizing radiation, and if CTA is necessary, proper shielding and dose optimization are required.",
        "option_analysis": "Option A (CTA) is the correct next step because it provides detailed vascular imaging to evaluate carotid artery stenosis or occlusion. Alternative imaging modalities exist, but CTA is widely available and highly sensitive for detecting vascular pathology in the extracranial carotid circulation.",
        "clinical_pearls": "1. Unilateral watershed infarcts should trigger evaluation for ipsilateral carotid stenosis. 2. CTA is a rapid and effective tool for assessing carotid and intracranial arteries. 3. Hemodynamic compromise as a cause of stroke may necessitate different management strategies compared to embolic strokes.",
        "current_evidence": "Recent stroke guidelines endorse vascular imaging, such as CTA, as a critical component in the workup of watershed infarctions. Current research focuses on refining imaging protocols to better delineate the hemodynamic significance of carotid lesions and to guide revascularization decisions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_21.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993078",
    "fields": {
      "question_number": "304",
      "question_text": "Hemorrhagic stroke and INR of 3.1",
      "options": {
        "A": "PCC"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In patients with hemorrhagic stroke on warfarin, the elevated INR reflects anticoagulation that increases bleeding risk. Rapid reversal of coagulopathy is essential to limit hematoma expansion.",
        "pathophysiology": "Warfarin inhibits vitamin K\u2013dependent clotting factors (II, VII, IX, and X). In the setting of intracranial hemorrhage, an INR above the therapeutic range (here 3.1) can worsen bleeding. Prothrombin complex concentrate (PCC) contains these clotting factors, allowing rapid reversal of warfarin's effects.",
        "clinical_correlation": "Patients on warfarin who present with a hemorrhagic stroke have a higher risk of hematoma expansion. Reversal of anticoagulation is critical to minimize further bleeding and improve outcomes.",
        "diagnostic_approach": "Diagnosis is based on clinical presentation and neuroimaging (typically CT scan) showing hemorrhage. Laboratory tests (including INR) confirm the degree of anticoagulation. Differential diagnoses include other forms of intracerebral hemorrhage such as hypertensive bleeds, aneurysmal subarachnoid hemorrhage, or vascular malformations.",
        "classification_and_neurology": "Hemorrhagic stroke is classified under cerebrovascular diseases, specifically intracerebral hemorrhage (ICH), which is a subtype of hemorrhagic stroke distinct from subarachnoid hemorrhage (SAH). The World Health Organization and American Heart Association/American Stroke Association (AHA/ASA) classify stroke etiologies into ischemic and hemorrhagic, with further subclassifications based on etiology and location. Warfarin-associated hemorrhagic stroke falls under anticoagulant-related ICH, a recognized category due to its distinct management and prognosis. This classification aids in guiding treatment strategies, as anticoagulant-associated hemorrhages require rapid reversal of coagulopathy. Contemporary nosology emphasizes the importance of underlying risk factors such as hypertension, cerebral amyloid angiopathy, and anticoagulation status. There is consensus that anticoagulation-related ICH represents a high-risk subgroup requiring specialized management protocols, as outlined in recent stroke guidelines.",
        "classification_and_nosology": "Hemorrhagic stroke is categorized as intracerebral hemorrhage (nontraumatic) and may be further classified based on the underlying cause (e.g., anticoagulant-associated intracerebral hemorrhage).",
        "management_principles": "The first-line management includes rapid reversal of anticoagulation using PCC along with intravenous vitamin K administration. This is supported by guidelines like those from the American Heart Association/American Stroke Association. In pregnancy and lactation, reversal agents would be used similarly since the maternal benefit of stopping hemorrhage outweighs potential concerns; however, consultation with specialists is advised if anticoagulation has been used during pregnancy.",
        "option_analysis": "Option A (PCC) is correct because it provides the clotting factors necessary for rapid reversal. Other options (though not listed) such as fresh frozen plasma (FFP) are alternatives but are generally slower and carry volume overload risks.",
        "clinical_pearls": "\u2022 Rapid reversal of warfarin is critical in hemorrhagic strokes. \u2022 PCC achieves faster correction compared to FFP. \u2022 Always co-administer vitamin K to sustain factor synthesis.",
        "current_evidence": "Recent guidelines and studies favor the use of four-factor PCC over FFP due to its quicker effect and lower risk profile. Updated stroke management protocols emphasize rapid correction of anticoagulation in warfarin-associated hemorrhagic stroke."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993079",
    "fields": {
      "question_number": "305",
      "question_text": "Scenario of 82-year-old lady with ischemic stroke presented within 1 hour with no contraindications",
      "options": {
        "A": "Tpa"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke is caused by an occlusion of a cerebral artery leading to brain ischemia. Timely administration of thrombolytics, like tissue plasminogen activator (tPA), can dissolve the clot and restore perfusion if given within the therapeutic window.",
        "pathophysiology": "The infarction occurs when an embolus or thrombus occludes an artery. tPA acts by catalyzing the conversion of plasminogen to plasmin, which helps break down fibrin clots and restore blood flow.",
        "clinical_correlation": "In an 82-year-old woman presenting within 1 hour of symptom onset and with no contraindications, immediate treatment with tPA can salvage the penumbral tissue and improve functional outcomes. Although advanced age was once considered a relative contraindication, current evidence supports its use in selected elderly patients.",
        "diagnostic_approach": "Diagnosis is confirmed by the clinical presentation and brain imaging (noncontrast CT scan) which excludes hemorrhage. Differential diagnoses include stroke mimics (such as seizures, migraines, or hypoglycemia), but the classical rapid onset of focal deficits supports ischemic stroke.",
        "classification_and_neurology": "Ischemic strokes are classified based on etiology using systems such as the TOAST classification, which categorizes strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This classification informs secondary prevention strategies but is less critical in acute management decisions. Intravenous thrombolysis with tPA falls under the acute management of ischemic stroke within the cerebrovascular disease spectrum. The classification of stroke subtypes has evolved with advances in imaging and pathophysiological understanding, but the primary focus in the acute setting remains rapid diagnosis and reperfusion therapy eligibility.",
        "classification_and_nosology": "Ischemic stroke is classified under cerebrovascular accidents and can be further grouped by etiology (e.g., thrombotic, embolic, or lacunar infarcts).",
        "management_principles": "First-line management for acute ischemic stroke within the time window (typically up to 4.5 hours from onset) is IV tPA. Blood pressure management is conservative unless levels are exceedingly high. In the elderly and during pregnancy/lactation (if applicable), tPA remains the treatment of choice if no contraindications are present; careful risk\u2013benefit analysis is essential.",
        "option_analysis": "Option A (tPA) is correct. The absence of contraindications (e.g., recent surgery, hemorrhage) and the fact that the patient presents within the window support the use of thrombolytic therapy. Other options (not provided) would not be indicated in this early phase of ischemic stroke.",
        "clinical_pearls": "\u2022 Time is brain; early thrombolysis significantly improves outcomes. \u2022 Advanced age is not an absolute contraindication for tPA. \u2022 Always rule out hemorrhage before administering tPA.",
        "current_evidence": "Recent updates in stroke guidelines reaffirm the expanded window for tPA in select patients with confirmed ischemic stroke. Advanced imaging techniques help select candidates who can still benefit from thrombolysis despite older age."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993080",
    "fields": {
      "question_number": "306",
      "question_text": "Case scenario of a lady in postpartum period presented with headache and seizure, normal brian CT what to do next? (No Mg in the choices)",
      "options": {
        "A": "CTV"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In the postpartum period, headache and seizures raise concern for several etiologies including eclampsia and cerebral venous thrombosis (CVT). When a noncontrast CT brain is normal, further vascular imaging is indicated to evaluate conditions that may not be visible on standard CT.",
        "pathophysiology": "CVT occurs due to thrombosis of the cerebral venous sinuses, leading to impaired venous drainage, increased intracranial pressure, and potentially seizures and headache. Postpartum status is a prothrombotic state increasing the risk for CVT. In eclampsia, endothelial dysfunction and vasogenic edema (PRES) are common.",
        "clinical_correlation": "A postpartum woman with headache and seizure with a normal CT scan suggests that the pathology might be in the venous system (CVT) or related to subtle changes not visible on a standard CT (such as PRES). Although eclampsia is common, the absence of magnesium sulfate among options forces consideration of alternative diagnoses.",
        "diagnostic_approach": "After a normal CT, the next step is to use vascular imaging. MRI with MR venography is the gold standard for CVT, but if unavailable, CT venography (CTV) is an acceptable and rapid alternative. Differential diagnoses include eclamptic seizures, PRES, and other causes of postpartum seizures.",
        "classification_and_neurology": "Cerebral venous thrombosis is classified under the broader category of cerebrovascular diseases, specifically as a form of stroke due to venous etiology. According to the International Classification of Diseases (ICD-11) and the American Heart Association/American Stroke Association (AHA/ASA), CVT falls under 'Other cerebrovascular diseases' distinct from arterial ischemic strokes or hemorrhagic strokes. CVT can be further subclassified based on the location of thrombosis (e.g., superior sagittal sinus, transverse sinus, deep cerebral veins), etiology (idiopathic, pregnancy/postpartum, thrombophilia, infection), and clinical severity. Historically, classification systems have evolved from clinical-pathological to imaging-based frameworks, with current consensus emphasizing neuroimaging confirmation. There is some debate about optimal subclassification schemes, but consensus supports imaging-based diagnosis and classification to guide management.",
        "classification_and_nosology": "CVT is classified under cerebrovascular disorders and is recognized as a distinct entity within stroke syndromes. It is particularly notable in the peripartum and postpartum population due to hypercoagulability.",
        "management_principles": "The definitive management of CVT is anticoagulation (usually with low molecular weight heparin as first-line therapy), even in the presence of hemorrhage. In postpartum patients, treatment protocols remain similar; anticoagulation is considered safe in lactating women. For eclampsia (if suspected), magnesium sulfate is the treatment of choice, but since it is not an option here, the imaging workup to confirm an alternative diagnosis (i.e., CVT) is warranted.",
        "option_analysis": "Option A (CTV) is correct in this scenario because a normal CT does not exclude CVT. Vascular imaging, such as CT venography, is necessary to identify sinus thrombosis. Other options (though not provided) might have included magnesium sulfate for eclampsia, but the question specifies that magnesium is not among the choices, making CTV the next logical step.",
        "clinical_pearls": "\u2022 In the postpartum period, always consider CVT in women presenting with headache and seizures. \u2022 CT venography is a rapid, accessible alternative to MR venography in suspected CVT. \u2022 A normal CT does not rule out CVT or subtle changes seen in PRES.",
        "current_evidence": "Recent studies emphasize the importance of early detection of CVT using advanced imaging techniques. Updated guidelines suggest that in patients with high clinical suspicion and a normal noncontrast CT, vascular imaging should be pursued promptly to guide management."
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
