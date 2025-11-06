
# Import batch 2 of 3 from chunk_8_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993213",
    "fields": {
      "question_number": "296",
      "question_text": "Rt small thalamic hemorrhage since one day, BP normal, pic attached no hydro or ventricular extension what to do next",
      "options": {
        "A": "(Prophylactic LMWH) is correct and is supported by current guidelines for preventing thromboembolic complications in patients with stable intracerebral hemorrhage. Option B (EVD) is incorrect because external ventricular drainage is reserved for cases with significant hydrocephalus or intraventricular hemorrhage, which is not present in this case."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In patients with a small thalamic hemorrhage, after 24 hours if the hemorrhage remains stable and there is no evidence of hydrocephalus or intraventricular extension, the major concern becomes the prevention of venous thromboembolism (VTE). Prophylactic low molecular weight heparin (LMWH) is commonly used in this scenario.",
        "pathophysiology": "Small deep hemorrhages, such as those occurring in the thalamus, if not complicated by expansion or ventricular involvement, primarily pose a risk for secondary complications like deep vein thrombosis (DVT) due to immobility. The prophylactic use of LMWH helps mitigate this risk while the hemorrhage is stable.",
        "clinical_correlation": "The patient has a right thalamic hemorrhage that appears stable without hydrocephalus or ventricular extension on imaging. The stable nature of the hemorrhage makes it safe to initiate VTE prophylaxis, as the risk of bleeding expansion is minimized after the first 24 hours.",
        "diagnostic_approach": "Differential considerations include hemorrhagic transformation of an ischemic stroke, hypertensive hemorrhage, and vascular malformations. However, in the absence of hydrocephalus or ventricular extension, conservative management with VTE prophylaxis is most appropriate. Serial imaging may be done to monitor hematoma stability.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on location (lobar, deep, brainstem, cerebellar), etiology (hypertensive, amyloid angiopathy, vascular malformations, coagulopathy), and clinical severity. The deep hemorrhages include thalamic and basal ganglia hemorrhages and are commonly associated with hypertensive small vessel disease. The American Heart Association/American Stroke Association (AHA/ASA) stroke guidelines categorize ICH management based on hemorrhage size, location, presence of intraventricular hemorrhage, and clinical status. This classification guides prognosis and treatment. The nosology also differentiates primary ICH from secondary causes such as trauma or tumor. The current consensus emphasizes individualized management plans based on hemorrhage characteristics and patient comorbidities.",
        "classification_and_nosology": "Intracerebral hemorrhage (ICH) is classified based on location (lobar vs. deep, such as thalamic) and etiology. A small, deep thalamic hemorrhage in a normotensive or well-controlled blood pressure patient is managed conservatively.",
        "management_principles": "After 24 hours of hemorrhage stability, initiating prophylactic LMWH for DVT prevention is recommended in current stroke guidelines. Blood pressure management and neurological monitoring remain essential. In pregnant patients, LMWH is favored over unfractionated heparin for VTE prophylaxis due to its better safety profile, and it is generally considered safe in lactation.",
        "option_analysis": "Option A (Prophylactic LMWH) is correct and is supported by current guidelines for preventing thromboembolic complications in patients with stable intracerebral hemorrhage. Option B (EVD) is incorrect because external ventricular drainage is reserved for cases with significant hydrocephalus or intraventricular hemorrhage, which is not present in this case.",
        "clinical_pearls": "1. Prophylactic LMWH is indicated for DVT prevention in patients with stable small ICH after 24 hours. 2. EVD is not indicated unless there are signs of obstructive hydrocephalus or significant ventricular involvement.",
        "current_evidence": "Recent clinical trials and guidelines (such as those from the American Heart Association) support the early initiation of prophylactic anticoagulation with LMWH for patients with small, stable intracerebral hemorrhages, while carefully monitoring for any signs of hematoma expansion."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993214",
    "fields": {
      "question_number": "297",
      "question_text": "Male with progressive myelopathy attached image clearly showing slow void, and long cord signal changes, dx",
      "options": {
        "A": "(DAVF) is correct because the clinical presentation of a progressive myelopathy combined with the specific MRI findings (slow flow voids and long cord signal abnormalities) strongly supports a diagnosis of spinal dural arteriovenous fistula. Other options such as multiple sclerosis, transverse myelitis, or neoplasm lack the combination of flow voids and progressive cord changes seen in DAVF."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Spinal dural arteriovenous fistula (DAVF) is a vascular malformation where an abnormal connection exists between a dural artery and a draining vein. It typically presents with progressive myelopathy and distinct MRI findings, including long segment T2 hyperintensity within the cord and flow voids representing abnormal vessels.",
        "pathophysiology": "In DAVF, the arterial blood shunts directly into the venous system, leading to increased venous pressure and congestion. This venous hypertension results in chronic spinal cord ischemia and demyelination, manifesting as progressive neurological deficits over time.",
        "clinical_correlation": "Patients, often middle-aged males, present with progressive myelopathy characterized by symptoms such as gait disturbances and lower extremity weakness. The presence of flow voids (indicative of abnormal, dilated vessels) and longitudinal cord signal changes on MRI strongly point towards DAVF rather than inflammatory, demyelinating, or neoplastic processes.",
        "diagnostic_approach": "The differential diagnosis includes multiple sclerosis, transverse myelitis, spinal cord neoplasms, and infectious myelitis. Unlike these conditions, DAVF is suggested by the presence of flow voids on MRI and a gradual progression of myelopathy. Definitive diagnosis is usually confirmed with digital subtraction angiography (DSA), which maps the vascular anatomy in detail.",
        "classification_and_neurology": "Spinal dural arteriovenous fistulas belong to the broader category of spinal vascular malformations. The most widely accepted classification system is the **Moldenhauer classification**, which divides spinal AVMs into four types:  - **Type I:** Spinal dural arteriovenous fistulas (DAVFs) \u2013 low-flow fistulas between dural arteries and radicular veins. - **Type II:** Intramedullary glomus AVMs \u2013 compact nidus within the spinal cord. - **Type III:** Juvenile or extensive AVMs \u2013 diffuse intramedullary and extramedullary involvement. - **Type IV:** Perimedullary AVFs \u2013 direct fistulas on the pial surface without nidus.  DAVFs (Type I) are the most common and typically present with progressive myelopathy due to venous hypertension. This classification helps guide diagnosis and management strategies. Over time, imaging advances have refined this system, but Moldenhauer's remains a clinical standard. Some controversies exist regarding the overlap between perimedullary AVFs and DAVFs, but the key distinction lies in the fistula location and flow dynamics.",
        "classification_and_nosology": "Spinal DAVF is classified as a type of arteriovenous shunt affecting the dura of the spinal cord. It is distinct from intramedullary arteriovenous malformations and is an acquired, rather than congenital, vascular lesion in many cases.",
        "management_principles": "The first-line management for DAVF is endovascular embolization, which aims at occluding the fistula. Open surgical ligation is considered when embolization is not feasible or if the fistula recurs. In pregnant patients, the timing and modality of intervention require a careful multidisciplinary approach to balance maternal neurological recovery with fetal safety; similarly, lactating patients may need tailored anesthesia and procedural planning.",
        "option_analysis": "Option A (DAVF) is correct because the clinical presentation of a progressive myelopathy combined with the specific MRI findings (slow flow voids and long cord signal abnormalities) strongly supports a diagnosis of spinal dural arteriovenous fistula. Other options such as multiple sclerosis, transverse myelitis, or neoplasm lack the combination of flow voids and progressive cord changes seen in DAVF.",
        "clinical_pearls": "1. Flow voids on spinal MRI are a key indicator of abnormal vascular channels typical of DAVF. 2. Early diagnosis and treatment are essential to prevent permanent neurological deficits.",
        "current_evidence": "Current literature and updated neurovascular guidelines advocate for prompt diagnosis and early endovascular treatment of spinal DAVF to halt progression of myelopathy, with emerging evidence supporting the efficacy and safety of these interventions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993215",
    "fields": {
      "question_number": "298",
      "question_text": "Male with renal impairment, stroke, angiokeratoma pic asking about enzyme supp",
      "options": {
        "A": ", which corresponds to enzyme replacement with alpha"
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X-linked lysosomal storage disorder caused by a deficiency of the enzyme alpha-galactosidase A. This deficiency leads to systemic accumulation of glycosphingolipids, particularly globotriaosylceramide, affecting various organs including the kidneys, heart, nervous system, and skin.",
        "pathophysiology": "The lack of sufficient alpha-galactosidase A results in progressive deposition of glycosphingolipids within vascular endothelial cells and other tissues. The accumulation in blood vessels contributes to ischemic events such as stroke, while deposition in the skin leads to angiokeratoma formation. Renal impairment is also a common complication due to the buildup in the kidneys.",
        "clinical_correlation": "The classic clinical triad of Fabry disease includes stroke (especially in younger males), renal dysfunction, and characteristic angiokeratomas. The presence of angiokeratomas, along with a history of renal impairment and stroke, strongly points toward Fabry disease as the underlying diagnosis.",
        "diagnostic_approach": "Diagnosis is typically confirmed by measuring alpha-galactosidase A enzyme activity in plasma or leukocytes, along with genetic testing for mutations in the GLA gene. Differential diagnoses include other lysosomal storage disorders such as Gaucher, Pompe, and Krabbe diseases which have distinct enzyme deficiencies and clinical presentations.",
        "classification_and_neurology": "Fabry disease is classified within the broader group of lysosomal storage disorders (LSDs), specifically under glycosphingolipidoses. It is an X-linked inherited metabolic disorder caused by mutations in the GLA gene encoding alpha-galactosidase A. The disease exhibits classic and late-onset (or variant) phenotypes, with the classic form presenting in childhood or adolescence with multisystem involvement, while late-onset variants may present predominantly with cardiac or renal manifestations in adulthood. The nosology distinguishes Fabry disease from other LSDs such as Gaucher disease (glucocerebrosidase deficiency) and Pompe disease (acid alpha-glucosidase deficiency). The current consensus emphasizes the importance of early diagnosis and enzyme replacement therapy (ERT) as disease-modifying treatment. There is ongoing debate about screening strategies and management of heterozygous females due to variable expression.",
        "classification_and_nosology": "Fabry disease is categorized under X-linked lysosomal storage disorders. It is distinct from other storage diseases by its specific enzyme deficiency and pattern of organ involvement.",
        "management_principles": "The mainstay of Fabry disease treatment is enzyme replacement therapy (ERT) with recombinant alpha-galactosidase A. Early initiation of ERT can reduce glycosphingolipid deposition and ameliorate clinical symptoms. In pregnant women, the decision to initiate or continue ERT should involve a multidisciplinary team with careful risk-benefit analysis, as data are limited but suggest that treatment may be continued if clearly beneficial. Lactating patients should also receive tailored counseling regarding the safety profile of ERT during breastfeeding.",
        "option_analysis": "Option A, which corresponds to enzyme replacement with alpha-galactosidase A (often noted as 'Galtcosidase'), is correct because this directly addresses the underlying deficiency in Fabry disease. Other enzymes mentioned (e.g., beta-glucocerebrosidase, alpha-glucosidase, or galactocerebrosidase) are associated with different lysosomal storage disorders and are therefore incorrect in this context.",
        "clinical_pearls": "1. Always consider Fabry disease in younger patients presenting with stroke, renal impairment, and characteristic skin lesions (angiokeratomas). 2. Enzyme replacement therapy with recombinant alpha-galactosidase A is the current disease-specific treatment for Fabry disease.",
        "current_evidence": "Recent clinical studies and guideline updates continue to support the early use of ERT in Fabry disease to slow disease progression and improve outcomes. Ongoing research is looking into adjunctive therapies and optimal timing for initiating treatment, especially in special populations such as pregnant or lactating women."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993391",
    "fields": {
      "question_number": "420",
      "question_text": "14 years old boy with intense lancinating pain in feet. His 16 years old sister has same but milder symptoms. There is positive history of strokes in his maternal grandfather before age of 50. On examination; \u2193 pain sensation distally. His lower trunk evident for abnormal skin lesions as attached. What is the best test to reach diagnosis?",
      "options": {
        "A": "\u03b1-Galactosidase activity",
        "B": "Transferritine",
        "C": "VLCFA",
        "D": "PME22 gene"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X\u2010linked lysosomal storage disorder caused by deficient activity of the enzyme \u03b1\u2010galactosidase A. This enzyme deficiency leads to the accumulation of glycosphingolipids, particularly globotriaosylceramide, in various tissues including blood vessel walls, nerves, and skin.",
        "pathophysiology": "Due to a mutation in the GLA gene, the decreased activity of \u03b1\u2010galactosidase A results in the progressive deposition of globotriaosylceramide in endothelial cells, nerve cells, and other tissues. This accumulation causes vascular dysfunction, ischemia, and neuropathic pain. It also leads to characteristic skin lesions (angiokeratomas) and can predispose patients to early strokes.",
        "clinical_correlation": "The 14\u2010year\u2010old boy presenting with intense, lancinating pain in the feet and decreased pain sensation, alongside his sister\u2019s milder symptoms and a maternal grandfather with premature stroke, is highly suggestive of Fabry disease. The presence of skin lesions further strengthens the diagnosis since angiokeratomas are a hallmark of the condition.",
        "diagnostic_approach": "The diagnostic workup involves measuring \u03b1\u2010galactosidase A activity in plasma or leukocytes. Differential diagnoses to consider include other neuropathies such as diabetic neuropathy or hereditary sensory neuropathies; however, the combination of neuropathic pain, characteristic angiokeratomas, and a family history of early cerebrovascular events is specific for Fabry disease.",
        "classification_and_neurology": "Fabry disease is classified as a lysosomal storage disorder (LSD) within the broader family of inherited metabolic diseases. Specifically, it is an X-linked sphingolipidosis caused by \u03b1-Gal A deficiency.  - **Disease family:** Lysosomal storage disorders \u2192 Sphingolipidoses \u2192 Fabry disease. - **Inheritance:** X-linked recessive, with males typically more severely affected and females showing variable expression due to lyonization.  Classification systems have evolved from purely clinical to molecular and enzymatic definitions, with current consensus emphasizing genetic diagnosis alongside enzyme assays. Fabry disease is now recognized as a multisystem disorder with variable phenotypes, including classic and late-onset variants.  There is consensus to classify Fabry disease based on genotype-phenotype correlations and residual enzyme activity, guiding prognosis and therapy. Competing classifications focus on severity or organ involvement but molecular classification remains standard.",
        "classification_and_nosology": "Fabry disease is classified as a lysosomal storage disorder under the subgroup of glycosphingolipid storage diseases. It is inherited in an X\u2010linked manner, meaning hemizygous males are typically more severely affected, while heterozygous females may display variable phenotypes.",
        "management_principles": "Management initially involves enzyme replacement therapy (ERT) with agents such as agalsidase beta or agalsidase alfa to reduce substrate accumulation. For symptomatic relief, pain management strategies are employed. In addition, regular monitoring for renal, cardiac, and cerebrovascular complications is necessary. In pregnant or lactating women, the decision to initiate ERT must balance maternal benefits against potential risks, with recent guidelines generally supporting its use when indicated.",
        "option_analysis": "Option A (\u03b1\u2010Galactosidase activity) is the correct test for diagnosing Fabry disease. Option B (Transferritine) is related to iron metabolism and not relevant here. Option C (VLCFA) is used in the diagnostic workup of peroxisomal disorders like adrenoleukodystrophy. Option D (PME22 gene) pertains to certain hereditary neuropathies and is not applicable in this scenario.",
        "clinical_pearls": "1. Fabry disease should be considered in young patients with neuropathic pain and characteristic skin lesions. 2. An X\u2010linked inheritance pattern can lead to variable expression in females. 3. Early enzyme replacement can help mitigate long\u2010term complications such as renal and cerebrovascular disease.",
        "current_evidence": "Recent research supports the use of both enzyme replacement therapy and, in certain cases, chaperone therapy (e.g., migalastat) in patients with amenable mutations. Current guidelines stress early diagnosis and intervention to manage systemic complications efficiently."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993392",
    "fields": {
      "question_number": "421",
      "question_text": "Scenario typical for homocystinemia; thin tall patient with lens dislocation, slowly progressive cognitive delay. What is the best supplement to risk of further neurological symptoms and stroke?",
      "options": {
        "A": "Vitamin B6",
        "B": "Folate",
        "C": "Cobalamine",
        "D": "Something unrelated"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X\u2010linked lysosomal storage disorder caused by deficient activity of the enzyme \u03b1\u2010galactosidase A. This enzyme deficiency leads to the accumulation of glycosphingolipids, particularly globotriaosylceramide, in various tissues including blood vessel walls, nerves, and skin.",
        "pathophysiology": "Due to a mutation in the GLA gene, the decreased activity of \u03b1\u2010galactosidase A results in the progressive deposition of globotriaosylceramide in endothelial cells, nerve cells, and other tissues. This accumulation causes vascular dysfunction, ischemia, and neuropathic pain. It also leads to characteristic skin lesions (angiokeratomas) and can predispose patients to early strokes.",
        "clinical_correlation": "The 14\u2010year\u2010old boy presenting with intense, lancinating pain in the feet and decreased pain sensation, alongside his sister\u2019s milder symptoms and a maternal grandfather with premature stroke, is highly suggestive of Fabry disease. The presence of skin lesions further strengthens the diagnosis since angiokeratomas are a hallmark of the condition.",
        "diagnostic_approach": "The diagnostic workup involves measuring \u03b1\u2010galactosidase A activity in plasma or leukocytes. Differential diagnoses to consider include other neuropathies such as diabetic neuropathy or hereditary sensory neuropathies; however, the combination of neuropathic pain, characteristic angiokeratomas, and a family history of early cerebrovascular events is specific for Fabry disease.",
        "classification_and_neurology": "Homocystinuria due to CBS deficiency falls under the broader category of inherited disorders of amino acid metabolism, specifically under homocysteine metabolism disorders. It is classified as an autosomal recessive inborn error of metabolism. The nosology includes: - **Classical homocystinuria (CBS deficiency):** characterized by homocysteine accumulation and clinical features described above. - **Other homocysteinemias:** including remethylation defects (e.g., methylenetetrahydrofolate reductase deficiency, cobalamin metabolism defects) which have overlapping but distinct clinical and biochemical profiles. Classification has evolved with advances in molecular genetics, allowing differentiation between CBS deficiency and remethylation defects based on enzymatic and genetic studies. This distinction is crucial as treatment strategies differ. The disorder is part of the neurogenetics subspecialty and metabolic neurology, highlighting the importance of genetic and biochemical evaluation in neurological presentations.",
        "classification_and_nosology": "Fabry disease is classified as a lysosomal storage disorder under the subgroup of glycosphingolipid storage diseases. It is inherited in an X\u2010linked manner, meaning hemizygous males are typically more severely affected, while heterozygous females may display variable phenotypes.",
        "management_principles": "Management initially involves enzyme replacement therapy (ERT) with agents such as agalsidase beta or agalsidase alfa to reduce substrate accumulation. For symptomatic relief, pain management strategies are employed. In addition, regular monitoring for renal, cardiac, and cerebrovascular complications is necessary. In pregnant or lactating women, the decision to initiate ERT must balance maternal benefits against potential risks, with recent guidelines generally supporting its use when indicated.",
        "option_analysis": "Option A (\u03b1\u2010Galactosidase activity) is the correct test for diagnosing Fabry disease. Option B (Transferritine) is related to iron metabolism and not relevant here. Option C (VLCFA) is used in the diagnostic workup of peroxisomal disorders like adrenoleukodystrophy. Option D (PME22 gene) pertains to certain hereditary neuropathies and is not applicable in this scenario.",
        "clinical_pearls": "1. Fabry disease should be considered in young patients with neuropathic pain and characteristic skin lesions. 2. An X\u2010linked inheritance pattern can lead to variable expression in females. 3. Early enzyme replacement can help mitigate long\u2010term complications such as renal and cerebrovascular disease.",
        "current_evidence": "Recent research supports the use of both enzyme replacement therapy and, in certain cases, chaperone therapy (e.g., migalastat) in patients with amenable mutations. Current guidelines stress early diagnosis and intervention to manage systemic complications efficiently."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993393",
    "fields": {
      "question_number": "422",
      "question_text": "Long scenario deafness visual issues myoclonus, and also came with stroke MERF. WHAT you will do??",
      "options": {
        "A": "NOTCH 3",
        "B": "Measure pyruvate / lactate"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X\u2010linked lysosomal storage disorder caused by deficient activity of the enzyme \u03b1\u2010galactosidase A. This enzyme deficiency leads to the accumulation of glycosphingolipids, particularly globotriaosylceramide, in various tissues including blood vessel walls, nerves, and skin.",
        "pathophysiology": "Due to a mutation in the GLA gene, the decreased activity of \u03b1\u2010galactosidase A results in the progressive deposition of globotriaosylceramide in endothelial cells, nerve cells, and other tissues. This accumulation causes vascular dysfunction, ischemia, and neuropathic pain. It also leads to characteristic skin lesions (angiokeratomas) and can predispose patients to early strokes.",
        "clinical_correlation": "The 14\u2010year\u2010old boy presenting with intense, lancinating pain in the feet and decreased pain sensation, alongside his sister\u2019s milder symptoms and a maternal grandfather with premature stroke, is highly suggestive of Fabry disease. The presence of skin lesions further strengthens the diagnosis since angiokeratomas are a hallmark of the condition.",
        "diagnostic_approach": "The diagnostic workup involves measuring \u03b1\u2010galactosidase A activity in plasma or leukocytes. Differential diagnoses to consider include other neuropathies such as diabetic neuropathy or hereditary sensory neuropathies; however, the combination of neuropathic pain, characteristic angiokeratomas, and a family history of early cerebrovascular events is specific for Fabry disease.",
        "classification_and_neurology": "MELAS is classified under mitochondrial encephalomyopathies, a subgroup of mitochondrial diseases characterized by neurological and muscular involvement. It belongs to the broader category of primary mitochondrial disorders, which include syndromes such as MERRF (Myoclonic Epilepsy with Ragged Red Fibers), LHON (Leber Hereditary Optic Neuropathy), and others. The classification is based on clinical phenotype, genotype, and biochemical findings. Current consensus favors a phenotype-genotype correlation approach, recognizing overlapping features among mitochondrial syndromes. The nosology has evolved from purely clinical syndromes to integrated molecular diagnoses, emphasizing the importance of genetic and metabolic testing.",
        "classification_and_nosology": "Fabry disease is classified as a lysosomal storage disorder under the subgroup of glycosphingolipid storage diseases. It is inherited in an X\u2010linked manner, meaning hemizygous males are typically more severely affected, while heterozygous females may display variable phenotypes.",
        "management_principles": "Management initially involves enzyme replacement therapy (ERT) with agents such as agalsidase beta or agalsidase alfa to reduce substrate accumulation. For symptomatic relief, pain management strategies are employed. In addition, regular monitoring for renal, cardiac, and cerebrovascular complications is necessary. In pregnant or lactating women, the decision to initiate ERT must balance maternal benefits against potential risks, with recent guidelines generally supporting its use when indicated.",
        "option_analysis": "Option A (\u03b1\u2010Galactosidase activity) is the correct test for diagnosing Fabry disease. Option B (Transferritine) is related to iron metabolism and not relevant here. Option C (VLCFA) is used in the diagnostic workup of peroxisomal disorders like adrenoleukodystrophy. Option D (PME22 gene) pertains to certain hereditary neuropathies and is not applicable in this scenario.",
        "clinical_pearls": "1. Fabry disease should be considered in young patients with neuropathic pain and characteristic skin lesions. 2. An X\u2010linked inheritance pattern can lead to variable expression in females. 3. Early enzyme replacement can help mitigate long\u2010term complications such as renal and cerebrovascular disease.",
        "current_evidence": "Recent research supports the use of both enzyme replacement therapy and, in certain cases, chaperone therapy (e.g., migalastat) in patients with amenable mutations. Current guidelines stress early diagnosis and intervention to manage systemic complications efficiently."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993228",
    "fields": {
      "question_number": "1",
      "question_text": "A 66-year-old male patient presented with dysarthria and right sided weakness for 10 hours. CT brain done and showed acute ischemic change over the the left internal capsule (No attached image).\n\nWhich of the following is the next step in the management?",
      "options": {
        "A": "Aspirin",
        "B": "Dual antiplatelets",
        "C": "IV Labetalol",
        "D": "IV Nitroprusside"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X\u2010linked lysosomal storage disorder caused by deficient activity of the enzyme \u03b1\u2010galactosidase A. This enzyme deficiency leads to the accumulation of glycosphingolipids, particularly globotriaosylceramide, in various tissues including blood vessel walls, nerves, and skin.",
        "pathophysiology": "Due to a mutation in the GLA gene, the decreased activity of \u03b1\u2010galactosidase A results in the progressive deposition of globotriaosylceramide in endothelial cells, nerve cells, and other tissues. This accumulation causes vascular dysfunction, ischemia, and neuropathic pain. It also leads to characteristic skin lesions (angiokeratomas) and can predispose patients to early strokes.",
        "clinical_correlation": "The 14\u2010year\u2010old boy presenting with intense, lancinating pain in the feet and decreased pain sensation, alongside his sister\u2019s milder symptoms and a maternal grandfather with premature stroke, is highly suggestive of Fabry disease. The presence of skin lesions further strengthens the diagnosis since angiokeratomas are a hallmark of the condition.",
        "diagnostic_approach": "The diagnostic workup involves measuring \u03b1\u2010galactosidase A activity in plasma or leukocytes. Differential diagnoses to consider include other neuropathies such as diabetic neuropathy or hereditary sensory neuropathies; however, the combination of neuropathic pain, characteristic angiokeratomas, and a family history of early cerebrovascular events is specific for Fabry disease.",
        "classification_and_neurology": "Ischemic stroke is classified under cerebrovascular diseases and further categorized by etiology using systems like TOAST (Trial of ORG 10172 in Acute Stroke Treatment). TOAST classifies ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. The internal capsule infarct likely represents a lacunar stroke due to small vessel disease affecting penetrating arteries. This classification informs prognosis and secondary prevention strategies. Over time, stroke classification has evolved to incorporate imaging, clinical, and etiological data to tailor management. The current consensus emphasizes precise subtyping to optimize treatment and research comparability.",
        "classification_and_nosology": "Fabry disease is classified as a lysosomal storage disorder under the subgroup of glycosphingolipid storage diseases. It is inherited in an X\u2010linked manner, meaning hemizygous males are typically more severely affected, while heterozygous females may display variable phenotypes.",
        "management_principles": "Management initially involves enzyme replacement therapy (ERT) with agents such as agalsidase beta or agalsidase alfa to reduce substrate accumulation. For symptomatic relief, pain management strategies are employed. In addition, regular monitoring for renal, cardiac, and cerebrovascular complications is necessary. In pregnant or lactating women, the decision to initiate ERT must balance maternal benefits against potential risks, with recent guidelines generally supporting its use when indicated.",
        "option_analysis": "Option A (\u03b1\u2010Galactosidase activity) is the correct test for diagnosing Fabry disease. Option B (Transferritine) is related to iron metabolism and not relevant here. Option C (VLCFA) is used in the diagnostic workup of peroxisomal disorders like adrenoleukodystrophy. Option D (PME22 gene) pertains to certain hereditary neuropathies and is not applicable in this scenario.",
        "clinical_pearls": "1. Fabry disease should be considered in young patients with neuropathic pain and characteristic skin lesions. 2. An X\u2010linked inheritance pattern can lead to variable expression in females. 3. Early enzyme replacement can help mitigate long\u2010term complications such as renal and cerebrovascular disease.",
        "current_evidence": "Recent research supports the use of both enzyme replacement therapy and, in certain cases, chaperone therapy (e.g., migalastat) in patients with amenable mutations. Current guidelines stress early diagnosis and intervention to manage systemic complications efficiently."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993237",
    "fields": {
      "question_number": "10",
      "question_text": "A 60s-year-old male presented to the ER with 2 days history of unilateral weakness and dysarthria. On examination, BP 170/90, HR 80s. What is the next step in the management?",
      "options": {
        "A": "IV labetalol",
        "B": "IV nitroprusside",
        "C": "Observation",
        "D": "Resume home medications"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "This case involves an ischemic stroke patient presenting 2 days after symptom onset with moderately elevated blood pressure. In ischemic strokes, especially when the patient is outside the thrombolytic time window, permissive hypertension is generally allowed to ensure adequate cerebral perfusion to the affected areas.",
        "pathophysiology": "During an ischemic stroke, the brain\u2019s autoregulatory mechanisms may cause blood pressure to rise in an effort to maintain blood flow to the ischemic penumbra. Aggressive blood pressure reduction in this phase can decrease cerebral perfusion, risking expansion of the infarct. Thus, in patients who are not candidates for thrombolysis, blood pressure is often left untreated unless it is extremely high.",
        "clinical_correlation": "The patient presents with unilateral weakness and dysarthria, symptoms typical of a stroke, with blood pressure at 170/90 mmHg. Given that the stroke occurred 2 days ago and the blood pressure is not excessively high, the best approach is to continue supportive care with observation.",
        "diagnostic_approach": "While imaging (CT/MRI) is essential in stroke evaluation to differentiate between ischemic and hemorrhagic strokes, in this scenario the management focus is on blood pressure. Differential diagnoses include hemorrhagic stroke, stroke mimics, and lacunar infarcts; however, in the subacute phase of ischemia management, aggressive BP control is not indicated unless BP is >220/120 when not undergoing thrombolysis.",
        "classification_and_neurology": "AIS is classified under cerebrovascular diseases, specifically ischemic stroke subtypes (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.) according to TOAST criteria. Blood pressure management in AIS is part of acute stroke care protocols. The classification of hypertension in stroke is based on BP levels and timing relative to stroke onset. The American Heart Association/American Stroke Association (AHA/ASA) guidelines provide a framework for BP thresholds guiding treatment decisions. This approach has evolved from earlier more aggressive BP lowering to current permissive hypertension strategies, reflecting improved understanding of cerebral autoregulation in stroke.",
        "classification_and_nosology": "Ischemic strokes are categorized based on the underlying etiology (thrombotic, embolic, lacunar). This patient falls into the group of non-thrombolysis candidates where supportive care and observation are recommended.",
        "management_principles": "According to current AHA/ASA guidelines, in acute ischemic stroke patients not receiving thrombolysis, blood pressure should not be lowered aggressively unless it exceeds 220/120 mmHg. The tiered management involves supportive care, refraining from precipitous BP reduction, and monitoring. For women who are pregnant or lactating, similar principles apply with careful consideration of medication safety if any pharmacological intervention becomes necessary.",
        "option_analysis": "Option A (IV labetalol) and Option B (IV nitroprusside) suggest active blood pressure reduction which is not required at a BP of 170/90 mmHg in this clinical setting. Option D (Resume home medications) does not address the acute scenario adequately. Option C (Observation) is correct as it aligns with the principle of permissive hypertension in ischemic stroke beyond the thrombolysis window.",
        "clinical_pearls": "1. Permissive hypertension is a cornerstone of acute ischemic stroke management when patients are not eligible for thrombolysis. 2. The thrombolytic window (typically 4.5 hours) is critical; after that, supportive care is emphasized.",
        "current_evidence": "Recent guidelines continue to support a conservative approach to blood pressure management in non-thrombolysis ischemic stroke patients, emphasizing the risk of further ischemia with aggressive BP reductions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993238",
    "fields": {
      "question_number": "11",
      "question_text": "An elderly male presented to the ER with right sided weakness aphasia, Examination showed BP 220/120, HR 90s, patient was drowsy, aphasic, with right sided weakness NIHSS high (not sure about the number). What is the next step in management?",
      "options": {
        "A": "CT brain",
        "B": "Control Blood pressure",
        "C": "IV thrombolysis"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "In the acute management of stroke, neuroimaging is the cornerstone to differentiate between ischemic and hemorrhagic etiologies. A prompt CT scan is critical in establishing the diagnosis and guiding subsequent interventions.",
        "pathophysiology": "Markedly elevated blood pressure, as seen with 220/120 mmHg, increases the risk of hemorrhagic transformation and intracerebral bleeding. However, in the context of ischemic stroke, high blood pressure may be a compensatory mechanism to maintain perfusion to the penumbra. Knowing the stroke subtype through imaging is essential before any treatment decisions.",
        "clinical_correlation": "This elderly male exhibits classic stroke symptoms (right-sided weakness and aphasia) with a high NIHSS score and severely elevated BP. The clinical severity and high blood pressure necessitate immediate imaging to exclude hemorrhage.",
        "diagnostic_approach": "Differential diagnosis includes acute ischemic stroke, intracerebral hemorrhage, and stroke mimics. Computed tomography (CT) of the brain is the first-line diagnostic tool because it rapidly distinguishes hemorrhagic from ischemic stroke, which is critical for subsequent management decisions such as thrombolysis.",
        "classification_and_neurology": "Acute ischemic stroke is classified within cerebrovascular diseases, under the broader category of neurological emergencies. The TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system categorizes ischemic stroke etiologies into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. This classification informs secondary prevention strategies but is less critical in the hyperacute management phase. The American Heart Association/American Stroke Association (AHA/ASA) guidelines provide a framework for acute stroke management, emphasizing time-sensitive interventions. While hemorrhagic stroke is a differential diagnosis, the management pathways diverge significantly, underscoring the need for accurate classification via imaging prior to treatment.",
        "classification_and_nosology": "Acute stroke is broadly classified as ischemic or hemorrhagic. Once imaging differentiates these subtypes, management algorithms differ, particularly regarding eligibility for iv thrombolysis or endovascular therapy.",
        "management_principles": "Current guidelines recommend immediate CT imaging in suspected stroke cases. For patients with ischemic stroke and a history suggesting possible thrombolysis, blood pressure must be lowered to below 185/110 mmHg before IV thrombolysis can be initiated. However, the decision to control blood pressure comes after the imaging has confirmed the absence of hemorrhage.",
        "option_analysis": "Option A (CT brain) is correct because it confirms the diagnosis and rules out hemorrhage. Option B (Control Blood pressure) is an important step but should be undertaken after imaging confirms the type of stroke and when considering thrombolytic therapy. Option C (IV thrombolysis) cannot be administered without diagnostic imaging and addressing the blood pressure issue first.",
        "clinical_pearls": "1. 'Time is brain' \u2013 rapid imaging with CT is essential in suspected stroke cases. 2. Blood pressure management in stroke is nuanced; it is lowered only if thrombolysis is pursued after confirming ischemia.",
        "current_evidence": "Recent AHA/ASA updates reinforce the protocol of immediate CT imaging in acute stroke to guide timely treatment, especially in patients with elevated BP where the risk of hemorrhage is a concern."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993239",
    "fields": {
      "question_number": "12",
      "question_text": "Female patient with ESRD on regular hemodialysis complaining of recurrent TIAs last for less than 10 minutes inform of left sided weakness and dysarthria then resolved completely. These symptoms occur during the dialysis sessions. CT brain done and showed evidence of old ischemic stroke. Carotid US done and showed left ICA atherosclerotic changes with no visualized stenosis or occlusion.\nWhich of the following is important to order during evaluation of this patient?",
      "options": {
        "A": "CT angiography",
        "B": "MRI brain",
        "C": "CT Venogram"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2023,
      "explanation_sections": {
        "conceptual_foundation": "Transient ischemic attacks (TIAs) are brief episodes of neurological dysfunction resulting from transient cerebral ischemia. Recurrent TIAs warrant further vascular investigation to identify any clinically significant vessel disease.",
        "pathophysiology": "Patients with ESRD on hemodialysis are at higher risk for vascular calcification and atherosclerotic changes. Additionally, hemodynamic fluctuations during dialysis can precipitate transient episodes of cerebral hypoperfusion, leading to TIAs. Carotid ultrasound may not fully evaluate intracranial vessels, hence additional imaging is required.",
        "clinical_correlation": "This female patient experiences recurrent episodes of left-sided weakness and dysarthria during dialysis sessions. The presence of old ischemic changes on CT supports underlying cerebrovascular disease. While carotid ultrasound shows atherosclerotic changes without significant stenosis, the possibility of intracranial involvement or subtler vascular anomalies necessitates further evaluation.",
        "diagnostic_approach": "The differential diagnosis includes TIA due to embolic phenomena, hemodynamic instability causing global or watershed cerebral ischemia, and intracranial stenosis. CT angiography (CTA) is the non-invasive imaging modality of choice for evaluating both cervical and intracranial vasculature in this setting.",
        "classification_and_neurology": "TIAs and ischemic strokes are classified under cerebrovascular diseases per the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification, which categorizes ischemic strokes by etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This patient likely falls into large artery atherosclerosis with hemodynamic compromise or embolic phenomena. ESRD-related cerebrovascular disease is recognized as a high-risk condition with mixed pathophysiology involving both large and small vessels. The classification of TIAs has evolved with imaging advances; the tissue-based definition now requires absence of infarction on MRI to confirm TIA rather than stroke. This patient\u2019s old ischemic stroke on CT confirms prior infarction, emphasizing the continuum between TIA and stroke. Nosology helps guide diagnostic evaluation and management strategies.",
        "classification_and_nosology": "TIAs are classified by symptom duration (typically less than 24 hours) and are a clinical diagnosis that signals underlying cerebrovascular disease. They serve as a warning for potential future strokes and require a thorough vascular evaluation.",
        "management_principles": "For patients with TIA, the current guidelines recommend antiplatelet therapy, risk factor modification, and prompt vascular imaging (such as CTA) to evaluate for stenosis or other vascular abnormalities. In ESRD patients, contrast use requires careful consideration, and alternative imaging strategies may be considered if there are concerns regarding contrast-induced nephropathy, though in dialysis patients this is generally less concerning. For pregnant or lactating patients, the use of contrast is approached with caution and benefits weighed against potential risks.",
        "option_analysis": "Option A (CT angiography) is correct as it provides detailed visualization of the entire cerebrovascular tree, helping to identify lesions that may not be apparent on carotid ultrasound. Option B (MRI brain) is better for tissue characterization and detecting small infarcts but is less optimal for evaluating vascular anatomy in this context. Option C (CT Venogram) is not indicated as the clinical scenario does not suggest a venous pathology.",
        "clinical_pearls": "1. Recurrent TIAs are a red flag for impending stroke, necessitating comprehensive vascular evaluation. 2. In ESRD patients, hemodynamic shifts during dialysis can precipitate cerebral ischemia, making timely vascular imaging crucial.",
        "current_evidence": "Recent studies underscore the utility of CT angiography in TIA workups, as it can swiftly detect both extracranial and intracranial vascular pathologies that might be missed by ultrasound alone."
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
