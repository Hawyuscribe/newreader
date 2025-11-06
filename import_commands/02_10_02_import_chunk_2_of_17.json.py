
# Import batch 2 of 3 from chunk_2_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993007",
    "fields": {
      "question_number": "249",
      "question_text": "Sickle cell disease patient developed ischemic stroke, what to do as secondary prevention?",
      "options": {
        "A": "Chronic blood transfusion (from AHA/ASA 2021 guidelines for secondary prevention of stroke)"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "In patients with sickle cell disease (SCD), the risk of ischemic stroke is significantly elevated due to abnormal red blood cell morphology causing vaso-occlusion and endothelial damage. Secondary prevention strategies focus on reducing the proportion of sickled cells to prevent further vascular occlusion.",
        "pathophysiology": "Sickle cells have altered rheological properties and can occlude small cerebral vessels. Chronic transfusion therapy dilutes the concentration of hemoglobin S (HbS) in the circulation, thereby decreasing the likelihood of sickling and subsequent vaso-occlusion. This reduction in HbS minimizes endothelial injury and reduces the risk of recurrent stroke.",
        "clinical_correlation": "Patients with SCD who have already suffered an ischemic stroke are at high risk for recurrence. Clinical management involves aggressive intervention to lower HbS levels. Chronic blood transfusions have been shown to reduce this risk effectively.",
        "diagnostic_approach": "Workup includes brain imaging to confirm ischemia along with laboratory evaluation of hemoglobin electrophoresis. Transcranial Doppler ultrasound may also be used for screening in children with SCD to assess stroke risk.",
        "classification_and_neurology": "Ischemic stroke in sickle cell disease falls under the category of stroke due to hematologic disorders within the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system. It is classified as a stroke of 'other determined etiology' related to sickle cell vasculopathy. The stroke subtype is primarily large artery atherosclerosis-like vasculopathy, but with a unique pathogenesis due to sickling-induced endothelial injury. This classification helps differentiate it from cardioembolic or small vessel lacunar strokes, which have different management. The nosology has evolved to recognize the distinct mechanisms in SCD-related stroke, emphasizing the role of chronic hemolysis and vascular pathology unique to this population.",
        "classification_and_nosology": "Stroke in SCD is a recognized complication within the spectrum of sickle cell vasculopathy. It is classified as an ischemic stroke secondary to hematologic abnormalities.",
        "management_principles": "For secondary stroke prevention in SCD, chronic red blood cell transfusion is considered the first-line therapy (as recommended by the AHA/ASA 2021 guidelines). The goal is to maintain HbS levels below 30% to minimize the risk of further vaso-occlusive events. Hydroxyurea is another therapy that can reduce sickling and is often used in conjunction with supportive measures. In pregnant or lactating patients with SCD, transfusion protocols require careful coordination to avoid alloimmunization and iron overload, and multidisciplinary care is essential.",
        "option_analysis": "\u2022 Option A (Chronic blood transfusion) is the recommended strategy for secondary stroke prevention in patients with SCD. \u2022 Other options (though not detailed here) such as antiplatelet agents are less effective in modifying the underlying sickling process.",
        "clinical_pearls": "\u2022 In SCD, prevention of stroke centers on reducing the hemoglobin S percentage \u2013 keeping it below 30% is crucial. \u2022 Regular transfusions, while effective, necessitate monitoring for iron overload and may require chelation therapy. \u2022 Multidisciplinary management is key, especially in patients who are pregnant or lactating.",
        "current_evidence": "The latest AHA/ASA guidelines (2021) strongly advocate for chronic transfusion therapy for secondary stroke prevention in SCD patients. Emerging research is also evaluating the role of gene therapy and other novel agents, but transfusion remains the standard of care at present."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993008",
    "fields": {
      "question_number": "250",
      "question_text": "Scenario with picture of AVM, which of the following is a risk factor for bleeding?",
      "options": {
        "A": "Previous history of bleeding",
        "B": "Deep AVM",
        "C": "Deep venous drain",
        "D": "Presence of aneurysm",
        "E": "Highest grade with size"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Arteriovenous malformations (AVMs) are congenital vascular anomalies composed of a tangle of abnormal vessels with direct arteriovenous shunting. One of the key clinical concerns in AVMs is the risk of hemorrhage. A previous history of bleeding is recognized as an important predictor for future hemorrhagic events because it suggests vessel wall instability.",
        "pathophysiology": "AVMs have an abnormal architecture lacking the normal capillary bed, leading to high-flow, high-pressure shunts. A prior hemorrhage indicates that the fragile, dysplastic vessels have already ruptured once, thereby increasing the likelihood of rebleeding. The hemodynamic stress and turbulent flow further predispose to weakening and rupture of adjacent vessel segments. This concept is supported by studies showing that prior hemorrhage is the strongest predictor for subsequent bleeding.",
        "clinical_correlation": "Clinically, patients with a history of AVM-related hemorrhage are at heightened risk for rebleeding, which may result in sudden neurological deterioration, headache, or focal deficits. Recognition of this risk emphasizes the need for close monitoring and often an aggressive therapeutic approach.",
        "diagnostic_approach": "The diagnosis and risk stratification of AVMs involve neuroimaging. Digital subtraction angiography (DSA) remains the gold standard, though CT/MR angiography can provide valuable information regarding the nidus, venous drainage, and any associated aneurysms. Differential diagnoses include cavernous malformations (which typically present with smaller, \u2018popcorn-like\u2019 lesions and less aggressive hemorrhagic risk) and capillary telangiectasias.",
        "classification_and_neurology": "AVMs are classified based on angiographic features, nidus size, location, and venous drainage patterns. The Spetzler-Martin grading system is widely used to estimate surgical risk and includes size (small <3 cm, medium 3-6 cm, large >6 cm), eloquence of adjacent brain, and venous drainage (superficial or deep). Deep AVMs and those with deep venous drainage receive higher grades, indicating increased complexity and bleeding risk. Additionally, the presence of associated aneurysms is considered in risk stratification but is not part of the Spetzler-Martin grade. Alternative classification systems, such as the Lawton-Young supplementary grading scale, incorporate patient age and hemorrhagic presentation. The consensus recognizes that higher grade AVMs are more challenging to treat but do not necessarily correlate directly with bleeding risk; rather, specific features like deep location, deep venous drainage, prior hemorrhage, and aneurysms are more predictive of hemorrhage.",
        "classification_and_nosology": "AVMs are often classified using the Spetzler-Martin grading system, which considers factors such as size, location (eloquent vs. non-eloquent brain areas), and venous drainage patterns. Although the grading system is used primarily for surgical risk assessment, factors like previous hemorrhage are considered in overall prognostication and management planning.",
        "management_principles": "The management of AVMs with a history of hemorrhage is challenging. First-line options include microsurgical resection, endovascular embolization, and stereotactic radiosurgery, often used in combination. Decision making is based on AVM location, size, venous drainage, and patient-specific factors. In pregnancy or lactation, noninvasive modalities and careful consideration of radiation exposure are paramount, with embolization using newer materials sometimes preferred if intervention is urgent. Multidisciplinary discussion is essential in these scenarios.",
        "option_analysis": "Option A (Previous history of bleeding) is correct because a prior hemorrhage is the most consistent predictor for subsequent AVM rupture. Option B (Deep AVM) and Option C (Deep venous drainage) are also associated with higher hemorrhagic risk but are not as strongly predictive as a history of bleeding. Option D (Presence of aneurysm) is a recognized risk factor, particularly with intranidal aneurysms, and Option E (Highest grade with size) can be associated with increased risk, but the literature most strongly supports previous hemorrhage as the most significant risk factor.",
        "clinical_pearls": "\u2022 A prior hemorrhagic event in AVM patients greatly increases the risk of rebleeding. \u2022 Deep location and deep venous drainage also elevate hemorrhage risk. \u2022 Multimodality imaging is crucial for risk stratification and management planning.",
        "current_evidence": "Recent studies and guideline updates continue to support previous hemorrhage as a key risk factor for AVM bleeding. Research is ongoing into the molecular and hemodynamic factors that predispose certain AVMs to rebleed, and treatment algorithms are increasingly tailored to individual hemorrhagic risk profiles, especially when managing high-risk lesions in special populations such as pregnant or lactating patients."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_6.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993292",
    "fields": {
      "question_number": "321",
      "question_text": "Pt with muscle weakness, optic atrophy, hearing loss, family history of similar condition:",
      "options": {
        "A": "SCA 7",
        "B": "SCA 6",
        "C": "Friedrich ataxia"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Spinocerebellar ataxia type 7 (SCA7) is one of several autosomal dominant cerebellar ataxias characterized by progressive neurodegeneration. Unlike many other SCAs, SCA7 uniquely presents with visual impairment due to retinal degeneration, often accompanied by optic atrophy and sometimes hearing loss, which is a result of widespread neurodegeneration.",
        "pathophysiology": "SCA7 is caused by a CAG trinucleotide repeat expansion in the ATXN7 gene leading to an abnormally long polyglutamine tract within the ataxin-7 protein. This abnormal protein misfolds and aggregates, causing neuronal dysfunction and cell death particularly in the cerebellum, brainstem, and retina. The degeneration of retinal photoreceptors leads to pigmentary retinopathy and subsequent optic nerve atrophy.",
        "clinical_correlation": "Patients with SCA7 typically present with progressive cerebellar ataxia along with visual impairment, which may initially manifest as blurry vision or difficulty with central vision, eventually leading to optic atrophy. Hearing loss can also occur as a less common but noted feature. A positive family history supports the diagnosis of an autosomal dominant disorder.",
        "diagnostic_approach": "The diagnosis is established by clinical examination, family history, and confirmation via genetic testing for the ATXN7 gene repeat expansion. Differential diagnoses include SCA6, which generally presents with a more pure cerebellar ataxia without significant retinal involvement, and Friedreich ataxia (which is autosomal recessive and more commonly features cardiomyopathy and peripheral neuropathy rather than optic atrophy).",
        "classification_and_neurology": "The spinocerebellar ataxias are classified within the broader category of autosomal dominant cerebellar ataxias (ADCA). SCA7 belongs to the polyglutamine (polyQ) expansion diseases, a subgroup characterized by CAG repeat expansions encoding elongated polyglutamine tracts in specific proteins, leading to toxic gain of function. This group includes SCA1, SCA2, SCA3, SCA6, SCA7, and others. SCA6 is also a polyQ disorder but differs clinically and genetically from SCA7. Friedrich ataxia, in contrast, is an autosomal recessive ataxia caused by a GAA repeat expansion in the FXN gene, leading to frataxin deficiency and mitochondrial dysfunction. The nosology of SCAs has evolved from clinical phenotyping to molecular genetic classification, improving diagnostic accuracy and understanding of pathogenesis. Current consensus relies heavily on genetic testing to confirm subtype, given overlapping clinical features among SCAs.",
        "classification_and_nosology": "SCA7 falls under the group of polyglutamine disorders, a subset of spinocerebellar ataxias. It is categorized based on its genetic profile and distinct clinical manifestations, particularly the combination of cerebellar dysfunction and progressive visual loss.",
        "management_principles": "There is currently no cure for SCA7; management is supportive and focuses on symptom relief and rehabilitation. Physical therapy, occupational therapy, and speech therapy are key components of care. Genetic counseling is essential for affected families. In pregnant or lactating patients, special care should be taken regarding medications that may exacerbate neurological symptoms, and genetic counseling is crucial in family planning.",
        "option_analysis": "Option A (SCA 7) is correct as it best fits the clinical picture of progressive ataxia combined with optic atrophy and hearing loss. Option B (SCA 6) is primarily associated with cerebellar ataxia without significant retinal or optic pathway involvement. Option C (Friedreich ataxia) typically presents earlier in life with ataxia, cardiomyopathy, and diabetes, and follows an autosomal recessive inheritance pattern. The blank Option D provides no diagnostic value.",
        "clinical_pearls": "\u2022 Visual impairment (often from retinal degeneration) is a hallmark of SCA7. \u2022 A positive family history with autosomal dominant inheritance should prompt consideration of SCA7. \u2022 Genetic testing is definitive in distinguishing between different SCAs.",
        "current_evidence": "Recent advances in molecular genetics have improved early diagnosis of SCA7. Although no disease-modifying therapies currently exist, ongoing research into polyglutamine disorders holds promise for targeted therapies. Updated guidelines stress the importance of multidisciplinary management and genetic counseling, particularly for women in their childbearing years."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993293",
    "fields": {
      "question_number": "322",
      "question_text": "Young male coming with early dementia and bilateral LL weakness, has brothers who are similarly affected, MRI showed diffuse white matter lesions what is the diagnosis:",
      "options": {
        "A": "Adrenoleukodystrophy.",
        "B": "Hereditary spastic paraplegia.",
        "C": "Krabbe disease",
        "D": "Tangier disease"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Adrenoleukodystrophy (ALD) is a peroxisomal disorder characterized by the accumulation of very long chain fatty acids (VLCFAs), leading to progressive demyelination of the white matter and adrenal insufficiency. It is typically inherited in an X-linked manner, which explains its prevalence in young males and its occurrence among affected brothers.",
        "pathophysiology": "The defect in ALD lies in the ABCD1 gene, which impairs the transport of VLCFAs into peroxisomes for beta-oxidation. The resultant accumulation of these fatty acids disrupts membrane integrity and causes inflammatory demyelination in the central nervous system. The adrenal cortex is similarly affected, leading to adrenal insufficiency in many patients.",
        "clinical_correlation": "Young males with ALD often present with behavioral changes, cognitive decline (early dementia), and motor dysfunction such as spastic paraparesis (which may manifest as bilateral lower limb weakness). MRI typically reveals diffuse, often parieto-occipital, white matter lesions. A family history positive for similar neurological impairment heightens the suspicion of ALD.",
        "diagnostic_approach": "Diagnosis is based on clinical presentation, neuroimaging (with MRI showing symmetric white matter changes), and biochemical assays showing elevated VLCFA levels, followed by genetic testing for confirmation. Differential diagnoses include hereditary spastic paraplegia (which typically lacks significant white matter changes and cognitive decline), Krabbe disease (which presents in infancy), and Tangier disease (which has distinct lipid abnormalities and lacks the neurological pattern seen in ALD).",
        "classification_and_neurology": "Adrenoleukodystrophy belongs to the broader family of leukodystrophies\u2014genetically determined disorders characterized by abnormal development or destruction of CNS white matter. It is classified as a peroxisomal disorder due to its pathogenesis involving peroxisomal metabolic dysfunction. The nosology includes:  - X-linked ALD (most common form) - Childhood cerebral ALD - Adult cerebral ALD - Adrenomyeloneuropathy (AMN)  This classification reflects clinical phenotypes linked to the same genetic defect. Leukodystrophies are further divided by underlying biochemical defects (e.g., lysosomal, peroxisomal, mitochondrial). Other leukodystrophies include Krabbe disease (lysosomal), metachromatic leukodystrophy, and Alexander disease. Hereditary spastic paraplegia (HSP) is a separate group of inherited motor neuron diseases primarily affecting corticospinal tracts without diffuse white matter involvement. Tangier disease is a rare lipid metabolism disorder characterized by low HDL cholesterol without CNS demyelination. The current consensus uses genetic, biochemical, and clinical features to classify these disorders, though overlapping phenotypes sometimes complicate diagnosis.",
        "classification_and_nosology": "ALD is classified as a leukodystrophy and is grouped with peroxisomal disorders. Its X-linked inheritance pattern predominantly affects males, with heterozygous females typically having milder or later-onset symptoms.",
        "management_principles": "The management of ALD includes hormone replacement for adrenal insufficiency and consideration of hematopoietic stem cell transplantation (HSCT) in early cerebral disease to slow progression of demyelination. Emerging gene therapies are under investigation. In pregnant patients, counseling and careful endocrine management are critical, while lactation requires attention to the safety of any medications used (for instance, continuing hydrocortisone replacement as indicated).",
        "option_analysis": "Option A (Adrenoleukodystrophy) is correct because the clinical picture of early dementia, bilateral lower limb weakness, diffuse white matter lesions on MRI, and a positive family history in a young male strongly fits ALD. Option B (Hereditary spastic paraplegia) usually lacks the white matter changes and cognitive decline. Option C (Krabbe disease) typically presents in infancy with rapid neurodegeneration, and Option D (Tangier disease) is primarily a lipid metabolism disorder without the described neuroimaging findings.",
        "clinical_pearls": "\u2022 ALD is an X-linked peroxisomal disorder that primarily affects young males. \u2022 Elevated VLCFA levels are key to the diagnosis. \u2022 Early intervention with HSCT may slow cerebral progression if undertaken before significant neurological decline.",
        "current_evidence": "Recent studies emphasize the importance of early detection via newborn screening programs and the potential role of emerging gene therapies and HSCT. Current guidelines outline a multidisciplinary approach for managing neurologic and endocrine aspects of ALD, with special considerations for counseling women at risk during pregnancy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993294",
    "fields": {
      "question_number": "323",
      "question_text": "What is the mechanism of stroke in dissection?",
      "options": {
        "B": ") is assumed to represent the mechanism of stroke via thrombus formation and subsequent embolization from the dissection site. This is the accepted pathophysiological mechanism in most cases of cervical artery dissection. Other potential answers may have described hemodynamic compromise or direct occlusion, but evidence favors an embolic mechanism as the predominant cause of ischemic stroke in dissection."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Arterial dissection involves a tear in the intimal layer of the vessel wall. This creates a false lumen where blood can accumulate, leading to an intramural hematoma. The process can result in luminal narrowing and the formation of thrombi, which may subsequently embolize.",
        "pathophysiology": "In dissection, an intimal tear allows blood to enter the arterial wall, dissecting between layers. This results in an intramural hematoma that can compress the true lumen and cause cerebral ischemia either via hemodynamic insufficiency or, more commonly, through thrombus formation at the site of the tear. Pieces of the thrombus can break off and embolize distally, causing an ischemic stroke.",
        "clinical_correlation": "Patients with arterial dissection often present with acute pain (such as neck or head pain) followed by focal neurological deficits due to cerebral ischemia. The embolic mechanism explains the frequently observed multifocal ischemic lesions on imaging. Recognizing the mechanism helps tailor management toward preventing further embolic events.",
        "diagnostic_approach": "Noninvasive imaging, including CT angiography and MR angiography, is key in diagnosing arterial dissection by visualizing the double lumen or an intramural hematoma. Differential diagnoses include atherosclerotic stroke, vasculitis, and cardioembolic stroke. Distinguishing features on imaging, such as the elongated dissection flap or tapered occlusion, aid in differentiation.",
        "classification_and_nosology": "Arterial dissections can be classified based on location (e.g., cervical carotid or vertebral dissection) and etiology (spontaneous versus traumatic). They represent an important cause of stroke in younger patients without significant atherosclerotic risk factors.",
        "management_principles": "Initial management of arterial dissection is medical, focusing on antithrombotic therapy to prevent thromboembolism. Current guidelines suggest using either antiplatelet or anticoagulant agents with no clear superiority of one over the other in many cases. Endovascular intervention may be considered in patients with persistent symptoms or worsening dissection. In pregnant patients, low-molecular-weight heparin is often preferred over vitamin K antagonists due to safety profiles, and therapy should be closely coordinated with obstetric care. Lactating mothers can typically use antiplatelet agents safely, but the choice of medication should be individualized.",
        "option_analysis": "Although the specific options are not provided, the marked answer (Option B) is assumed to represent the mechanism of stroke via thrombus formation and subsequent embolization from the dissection site. This is the accepted pathophysiological mechanism in most cases of cervical artery dissection. Other potential answers may have described hemodynamic compromise or direct occlusion, but evidence favors an embolic mechanism as the predominant cause of ischemic stroke in dissection.",
        "clinical_pearls": "\u2022 Arterial dissection is a common cause of stroke in young patients and often presents with pain followed by neurological deficits. \u2022 The primary mechanism involves thrombus formation in a false lumen with subsequent embolization. \u2022 Early diagnosis with vascular imaging is crucial in guiding appropriate antithrombotic therapy.",
        "current_evidence": "Recent randomized studies have shown similar outcomes between antiplatelet and anticoagulant strategies for cervical artery dissections. Current guidelines emphasize individualized therapy and highlight safety considerations for special populations such as pregnant and lactating women, recommending agents with favorable risk profiles and minimal fetal/neonatal exposure."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993295",
    "fields": {
      "question_number": "324",
      "question_text": "Scenario for patient developed embolic stroke, his routine work up unremarkable, what to do next?",
      "options": {
        "B": "is assumed to represent the choice of extended cardiac monitoring. This is the correct next step after a negative initial evaluation in a patient with an embolic stroke pattern."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Embolic strokes occur when a clot formed elsewhere, most commonly in the heart, dislodges and travels to the cerebral circulation. When routine etiological work\u2010up (e.g., basic transthoracic echocardiography, carotid ultrasound) is unremarkable, the stroke remains cryptogenic or classified as an Embolic Stroke of Undetermined Source (ESUS).",
        "pathophysiology": "In many cryptogenic strokes, paroxysmal atrial fibrillation is suspected even though it can be missed on a standard workup. Clots form in the left atrium or appendage due to stasis, and intermittent arrhythmia leads to embolization. Up\u2010to\u2010date evidence, including studies such as the CRYSTAL\u2010AF trial, supports that prolonged cardiac monitoring increases detection of intermittent arrhythmias as the inciting cause.",
        "clinical_correlation": "Patients with embolic strokes typically present with sudden focal neurological deficits. In cases where the conventional workup proves negative, the clinical suspicion for paroxysmal atrial fibrillation remains high, and this may be the hidden source of embolism.",
        "diagnostic_approach": "After initial neuroimaging (CT/MRI) and cardiac evaluation with TTE/TEE have ruled out obvious sources, the next diagnostic step is long-term cardiac monitoring. Differential diagnoses include other embolic sources (e.g., aortic arch atheroma), small vessel lacunar strokes, or non-embolic etiologies; however, the multifocal embolic pattern generally steers workup toward paroxysmal arrhythmias.",
        "classification_and_nosology": "This scenario generally falls under the umbrella of cryptogenic stroke or ESUS (Embolic Stroke of Undetermined Source) \u2014 a subtype of ischemic stroke where no clear cause is found after standard evaluation.",
        "management_principles": "First-line management after a negative routine workup is to utilize prolonged cardiac rhythm monitoring (e.g., a 30-day event monitor or even an implantable loop recorder if indicated) to detect paroxysmal atrial fibrillation. If AF is detected, long-term anticoagulation is recommended. In pregnant or lactating patients, if anticoagulation becomes necessary, unfractionated heparin or low molecular weight heparin (LMWH) is preferred due to their safety profiles during pregnancy and lactation.",
        "option_analysis": "Although the specific answer choices aren\u2019t provided, answer option B is assumed to represent the choice of extended cardiac monitoring. This is the correct next step after a negative initial evaluation in a patient with an embolic stroke pattern.",
        "clinical_pearls": "1. Cryptogenic strokes account for a significant proportion of embolic strokes where routine testing is negative. 2. Prolonged cardiac monitoring increases the diagnostic yield for detecting paroxysmal atrial fibrillation. 3. Once AF is documented, the management pivots to anticoagulation rather than antiplatelet therapy.",
        "current_evidence": "Recent trials like CRYSTAL\u2010AF and EMBRACE have solidified the role of prolonged cardiac monitoring in detecting paroxysmal atrial fibrillation in patients with cryptogenic stroke, influencing recent guideline recommendations from the American Stroke Association."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993296",
    "fields": {
      "question_number": "325",
      "question_text": "Scenario for ischemic stroke, imaging showed bilateral anterior and posterior circulation strokes, what is the best step for management of this patient if TTE and TEE were negative?",
      "options": {
        "B": ", which is presumed to represent the strategy of prolonged or extended cardiac monitoring, is correct. It targets the possibility of intermittent atrial fibrillation that may have been missed on initial examinations."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "When imaging demonstrates strokes in both the anterior and posterior circulation bilaterally, a cardioembolic source is highly suspected. Even if initial cardiac studies (TTE and TEE) are negative, intermittent or paroxysmal atrial fibrillation may still be the underlying cause.",
        "pathophysiology": "The mechanism behind such multi-territorial strokes is most often embolic in nature. Paroxysmal atrial fibrillation can be elusive because its episodes may be transient. Negative echocardiographic studies do not rule out arrhythmogenic causes, hence the importance of prolonged rhythm monitoring.",
        "clinical_correlation": "Patients with multi-territorial infarctions can present with a combination of neurological deficits affecting different regions. The finding of strokes in multiple vascular territories strongly suggests an embolic source even in the absence of structural abnormalities on TTE/TEE.",
        "diagnostic_approach": "After ruling out major cardiac sources with TTE and TEE, it is important to pursue extended monitoring, such as with Holter monitors or implantable loop recorders, to detect intermittent arrhythmias like atrial fibrillation. Differential considerations include aortic arch atheroma, hypercoagulable states, or less common embolic sources, but the clinical pattern directs the workup toward paroxysmal AF.",
        "classification_and_nosology": "This condition is classified under ischemic stroke due to embolism, and in the absence of detected arrhythmias on initial workup, it falls under the category of embolic stroke of undetermined source (ESUS).",
        "management_principles": "In light of a negative TTE/TEE and a high clinical suspicion for paroxysmal atrial fibrillation, the first-line management is prolonged cardiac rhythm monitoring. If atrial fibrillation is subsequently detected, then the patient should be managed with anticoagulation rather than antiplatelet therapy. In pregnant or lactating patients, LMWH is currently preferred for anticoagulation due to its safety profile.",
        "option_analysis": "Option B, which is presumed to represent the strategy of prolonged or extended cardiac monitoring, is correct. It targets the possibility of intermittent atrial fibrillation that may have been missed on initial examinations.",
        "clinical_pearls": "1. Bilateral and multi-territorial strokes strongly raise the suspicion of a cardioembolic source. 2. Negative initial echocardiograms do not exclude paroxysmal atrial fibrillation. 3. Prolonged cardiac monitoring can reveal intermittent arrhythmias that guide appropriate anticoagulation therapy.",
        "current_evidence": "Recent studies and guideline updates emphasize the diagnostic utility of prolonged cardiac monitoring (e.g., via the EMBRACE or CRYSTAL-AF trials) in evaluating patients with ESUS, reinforcing this strategy in clinical practice."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993297",
    "fields": {
      "question_number": "326",
      "question_text": "Picture of spine MRI for patient has progressive myelopathy, ask about the diagnosis",
      "options": {
        "B": "corresponds to 'cervical spondylotic myelopathy', this is the correct choice based on the clinical picture and typical MRI findings associated with the condition."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2018,
      "explanation_sections": {
        "conceptual_foundation": "Progressive myelopathy refers to a slowly worsening dysfunction of the spinal cord. In older adults, one of the most common causes is degenerative changes in the cervical spine, commonly known as cervical spondylotic myelopathy.",
        "pathophysiology": "Cervical spondylotic myelopathy is caused by chronic degenerative changes such as disc herniation, osteophyte formation, ligamentum flavum hypertrophy, and sometimes ossification of the posterior longitudinal ligament. These changes lead to narrowing of the spinal canal (stenosis) and subsequent compression of the spinal cord.",
        "clinical_correlation": "Patients typically present with gradual onset of motor weakness, gait instability, sensory disturbances, and in some cases, hyperreflexia. The progression is usually insidious, reflecting the slow nature of degenerative changes in the cervical spine.",
        "diagnostic_approach": "Diagnosis is established with magnetic resonance imaging (MRI) of the spine, which reveals features such as spinal canal narrowing and intramedullary hyperintensities indicative of cord compression. Differential diagnoses include demyelinating diseases (e.g., multiple sclerosis), intramedullary tumors, infectious processes (e.g., spinal epidural abscess), and inflammatory conditions. Correlation with clinical findings is essential.",
        "classification_and_nosology": "Cervical spondylotic myelopathy is categorized under degenerative spinal disorders and is the most common cause of spinal cord dysfunction in older populations.",
        "management_principles": "The first-line management often involves conservative treatment (physical therapy, pain management, and careful monitoring) in mild cases. However, in individuals with progressive neurological deficits, surgical decompression (e.g., anterior cervical discectomy and fusion or laminectomy) is recommended. For pregnant or lactating patients, the treatment approach must carefully weigh the risks and benefits; conservative management is preferred if the deficits are not severe, but if surgery is necessary, timing and anesthetic considerations become critical.",
        "option_analysis": "Assuming option B corresponds to 'cervical spondylotic myelopathy', this is the correct choice based on the clinical picture and typical MRI findings associated with the condition.",
        "clinical_pearls": "1. Cervical spondylotic myelopathy is a common cause of progressive spinal cord compression in elderly patients. 2. MRI is the diagnostic modality of choice to evaluate for cord compression. 3. Early surgical intervention in progressive cases can improve neurological outcomes.",
        "current_evidence": "Recent guidelines suggest that early surgical decompression in patients with moderate to severe deficits can lead to improved long-term outcomes. Ongoing research continues to refine the indications and timing for surgery based on imaging and clinical severity."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993020",
    "fields": {
      "question_number": "113",
      "question_text": "Acute stroke With CT image with no established stroke ASPECT 8? Was treated with tPA CTA done and prepared for thrombectomy then he vomited and become lethargic bp 180/110",
      "options": {
        "A": "decrease bp",
        "B": "Stop tPA",
        "C": "Send him to CT"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "Acute ischemic stroke treatment often includes intravenous thrombolysis (tPA) and, when indicated, endovascular thrombectomy. However, post-treatment complications must be vigilantly monitored.",
        "pathophysiology": "tPA increases the risk of hemorrhagic transformation, especially in the setting of large infarct volumes or uncontrolled hypertension. A sudden deterioration, such as vomiting and lethargy, may signal an intracranial hemorrhage or increased intracranial pressure secondary to bleeding, particularly if blood pressure rises to levels like 180/110 mm Hg.",
        "clinical_correlation": "In this scenario, the patient initially had a favorable CT (ASPECTS 8) and was being managed with tPA while being evaluated for thrombectomy. The subsequent acute neurological deterioration (vomiting, lethargy) in the context of elevated blood pressure is highly concerning for a hemorrhagic complication or neurologic worsening, warranting immediate re-evaluation.",
        "diagnostic_approach": "The first step in managing sudden neurological decline after thrombolysis is to rapidly re-image the brain using non-contrast CT to assess for hemorrhagic transformation. Differential diagnoses include hemorrhagic transformation of the infarct, malignant cerebral edema, or even an unrelated complication. Immediate imaging helps differentiate these conditions.",
        "classification_and_neurology": "Acute ischemic stroke is classified etiologically based on the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion, stroke of other determined etiology, and stroke of undetermined etiology. The ASPECTS system classifies early ischemic changes on CT to stratify patients for reperfusion therapy. Post-thrombolysis complications include hemorrhagic transformation (classified radiologically as hemorrhagic infarction or parenchymal hematoma) and cerebral edema. Stroke severity is often graded using the NIH Stroke Scale (NIHSS). These classification systems aid in prognosis, therapeutic decisions, and research standardization. Current consensus emphasizes integrating clinical, imaging, and etiological classifications to tailor individualized management.",
        "classification_and_nosology": "This situation represents a complication of acute stroke management\u2014specifically, a potential hemorrhagic transformation following thrombolytic therapy.",
        "management_principles": "According to current stroke guidelines, the initial management for any suspected hemorrhagic complication post tPA is to obtain emergent neuroimaging to confirm the diagnosis. Blood pressure management is also critical; while strict BP control (generally <185/110 mm Hg pre-tPA) is maintained during and after thrombolysis, any new neurological changes necessitate re-imaging before further interventions. In pregnant or lactating patients, imaging protocols remain the same, and care should be taken in selecting antihypertensive agents that are safe in these populations (e.g., labetalol or hydralazine).",
        "option_analysis": "Option C, which directs the clinician to send the patient for an immediate CT scan, is the appropriate response. Options such as just decreasing blood pressure or stopping tPA are premature without confirming hemorrhage via re-imaging. The CT scan is needed to determine the correct next steps.",
        "clinical_pearls": "1. Any sudden neurological change during or after thrombolytic therapy should prompt immediate re-imaging. 2. Elevated blood pressure post-tPA, especially in the setting of neurological deterioration, raises concern for hemorrhage. 3. Adhering to BP thresholds during thrombolytic therapy is crucial to minimize hemorrhagic risk.",
        "current_evidence": "Current guidelines from the American Heart Association/American Stroke Association continue to stress the importance of urgent non-contrast head CT in the assessment of suspected hemorrhagic complications after tPA administration. Recent studies emphasize the predictive value of re-imaging when patients show clinical deterioration."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993021",
    "fields": {
      "question_number": "114",
      "question_text": "Case of press female with high BP 180/?? Presented with seizure and confusion with MRI showing bilateral occipital cortical hyperintensity dx",
      "options": {
        "A": "PRESS"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2019,
      "explanation_sections": {
        "conceptual_foundation": "This case describes a hypertensive female presenting with seizures and confusion, with MRI findings of bilateral occipital cortical hyperintensities. The clinical picture is characteristic of Posterior Reversible Encephalopathy Syndrome (PRES), a clinical\u2013radiological entity often seen in the setting of severe hypertension (and other triggers such as eclampsia, renal failure, or immunosuppressive therapy).",
        "pathophysiology": "PRES is believed to result from a failure of autoregulation in the cerebral vasculature caused primarily by sudden severe hypertension. This leads to endothelial dysfunction and subsequent vasogenic edema (predominantly in the posterior circulation\u2014in the parieto\u2010occipital regions). Recent research supports the idea that cerebral hyperperfusion and disruption of the blood\u2013brain barrier are key mechanisms in its development.",
        "clinical_correlation": "Patients with PRES present with headache, nausea, altered consciousness, visual disturbances, and seizures. The MRI typically shows symmetrical hyperintense lesions on T2/FLAIR sequences in the parieto-occipital lobes. The condition is reversible if promptly recognized and managed by controlling blood pressure and addressing the underlying cause.",
        "diagnostic_approach": "Diagnosis of PRES is primarily clinical and radiologic. Differential diagnoses include acute ischemic stroke (which usually demonstrates diffusion restriction on MRI), encephalitis, and reversible cerebral vasoconstriction syndrome (RCVS). The bilateral and posterior distribution on MRI helps to distinguish PRES from other entities.",
        "classification_and_neurology": "PRES is classified as a reversible encephalopathy syndrome within the spectrum of cerebrovascular and neurotoxic conditions. It is not a single disease but a syndrome with heterogeneous etiologies including hypertensive encephalopathy, eclampsia, cytotoxic drug exposure, autoimmune diseases, and renal failure. Nosologically, it falls under acute hypertensive and metabolic encephalopathies in cerebrovascular classification systems. The term 'PRES' was first coined in 1996, and since then, the classification has evolved to recognize its diverse causes and variable imaging patterns. Contemporary consensus views PRES as a clinico-radiological syndrome characterized by reversible vasogenic edema predominantly in posterior brain regions, but atypical variants involving other brain areas are increasingly recognized. There remains debate about the relative contributions of vasogenic edema versus cytotoxic injury and the exact pathophysiological mechanisms, reflecting ongoing research.",
        "classification_and_nosology": "PRES falls under the category of reversible encephalopathy syndromes. Although termed 'posterior', the syndrome may involve other regions, but predominantly the parieto-occipital areas are affected.",
        "management_principles": "Management focuses on rapid control of blood pressure using IV antihypertensive agents (e.g., nicardipine or labetalol) in a controlled fashion \u2013 typically targeting a 25% reduction in mean arterial pressure over the first few hours. Seizure control with anticonvulsants may be required. In pregnant patients (e.g., eclampsia), intravenous magnesium sulfate is indicated and BP management should be tailored to maternal and fetal risks; lactating mothers should be managed similarly with appropriate follow\u2010up.",
        "option_analysis": "Option A (PRES) is correct. Although the option is noted as 'PRESS', it is understood to be a reference to Posterior Reversible Encephalopathy Syndrome. No other options were given, and the presentation aligns perfectly with this diagnosis.",
        "clinical_pearls": "1. PRES is reversible with prompt management. 2. The typical MRI pattern is bilateral parieto-occipital vasogenic edema. 3. Severe hypertension is a key trigger.",
        "current_evidence": "Recent guidelines emphasize careful blood pressure management and rapid identification of PRES. Neuroimaging (MRI) remains the cornerstone of diagnosis, and emerging literature continues to explore the various precipitating factors beyond hypertension, including drug toxicity and systemic inflammatory states."
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
