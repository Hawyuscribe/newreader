
# Import batch 1 of 3 from chunk_8_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993203",
    "fields": {
      "question_number": "286",
      "question_text": "82 female with stroke NIHSS 20, BP 180/100, 3 hrs from symptoms onset, brain CT pic look okay no clear hypodensity but showed subtle early ischemic changes in BG, insular ribbon what to do next",
      "options": {
        "A": "(Labetalol) is incorrect because the patient\u2019s blood pressure is already below the threshold that would mandate reduction prior to thrombolysis. Option b (Thrombolysis) is correct because the patient is within the therapeutic window and meets criteria for acute reperfusion therapy. Option c (Thrombectomy) is not the immediate next step without vascular imaging confirmation of a large vessel occlusion and is typically adjunctive to tPA rather than a substitute in this scenario."
      },
      "correct_answer": "b",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case involves an elderly patient with a significant acute ischemic stroke (NIHSS 20) who is still within the 4.5-hour window for reperfusion therapy. The priority is to restore cerebral blood flow quickly, provided that contraindications, such as uncontrolled high blood pressure, are not present.",
        "pathophysiology": "Acute ischemic stroke results from a sudden reduction in blood flow, leading to infarction. Intravenous thrombolysis with tissue plasminogen activator (tPA) acts by cleaving plasminogen into plasmin, which dissolves the thrombus. Despite subtle early CT changes (e.g., insular ribbon, basal ganglia hypodensity), these findings do not preclude tPA use if they do not involve a large area of established infarction.",
        "clinical_correlation": "The patient\u2019s high NIHSS score indicates a severe stroke, and the presentation is consistent with a large vessel occlusion or a severe cortical/subcortical infarct. Although the blood pressure is 180/100 mmHg, it is below the threshold of >185/110 mmHg that typically necessitates aggressive antihypertensive management before thrombolysis.",
        "diagnostic_approach": "A noncontrast CT scan is used primarily to exclude hemorrhage and to identify early signs of ischemia. The decision for reperfusion therapy is based on clinical assessment, timing, and imaging. Differential diagnoses include stroke mimics such as seizure postictal states, hypoglycemia, or intracranial hemorrhage, but these are ruled out by the scan and clinical context.",
        "classification_and_neurology": "Acute ischemic stroke is classified etiologically using systems such as the TOAST classification, which categorizes stroke into large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and cryptogenic. This patient's presentation and imaging suggest a large vessel territory infarct, likely MCA distribution. Stroke severity is classified by NIHSS score, with 20 indicating severe stroke. The management of acute ischemic stroke falls under cerebrovascular disease classification within neurology. The therapeutic approach aligns with guidelines from the American Heart Association/American Stroke Association (AHA/ASA) for acute ischemic stroke. There is ongoing debate about extending thrombolysis windows and the role of advanced imaging to guide therapy, but current consensus supports intravenous thrombolysis within 4.5 hours of onset in eligible patients.",
        "classification_and_nosology": "This stroke falls under the category of acute ischemic stroke. Strokes are classified based on etiology (e.g., large artery atherosclerosis, cardioembolism, small vessel occlusion) and severity (using scales such as NIHSS).",
        "management_principles": "For patients within the 4.5-hour window, IV thrombolysis with tPA is the first-line therapy. Blood pressure management is essential only if values exceed 185/110 mmHg. Since this patient\u2019s BP is 180/100 mmHg, there is no need for pre-thrombolytic antihypertensive therapy. Mechanical thrombectomy may be considered subsequently if large vessel occlusion is confirmed, but the immediate priority is IV tPA. In pregnant or lactating patients, the use of tPA is a challenging decision; although not an absolute contraindication, careful assessment by a multidisciplinary team is essential to balance maternal benefits versus risks to the fetus.",
        "option_analysis": "Option a (Labetalol) is incorrect because the patient\u2019s blood pressure is already below the threshold that would mandate reduction prior to thrombolysis. Option b (Thrombolysis) is correct because the patient is within the therapeutic window and meets criteria for acute reperfusion therapy. Option c (Thrombectomy) is not the immediate next step without vascular imaging confirmation of a large vessel occlusion and is typically adjunctive to tPA rather than a substitute in this scenario.",
        "clinical_pearls": "1. For tPA eligibility, the blood pressure must be <185/110 mmHg; values slightly below this threshold do not require pre-treatment antihypertensives. 2. Early ischemic changes on CT do not automatically exclude patients from thrombolysis. 3. In high NIHSS strokes, prompt reperfusion therapy is crucial to salvage penumbral tissue.",
        "current_evidence": "Contemporary guidelines from AHA/ASA continue to support IV thrombolysis with tPA within 4.5 hours of symptom onset in eligible patients. Recent studies emphasize that strict blood pressure management prior to tPA is warranted only when levels exceed the set threshold, reinforcing that timely reperfusion is the critical factor in improving outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_23.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993204",
    "fields": {
      "question_number": "287",
      "question_text": "Acute stroke treated with tPA pic showing tongue angio edema, patient stable but severely dysarthric, what to do",
      "options": {
        "A": "(Intubation) is inappropriate because the patient is currently stable without airway compromise\u2014intubation is indicated only when there is imminent respiratory failure or severe obstruction. Option B (Steroid with antihistamine) directly addresses the inflammatory and mediator",
        "C": "(ACE inhibitor with diuretics) is contraindicated because ACE inhibitors can exacerbate angioedema by further increasing bradykinin levels, and diuretics do not address the underlying issue and may worsen hemodynamics."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "tPA-induced angioedema is a recognized complication of thrombolytic therapy. It is thought to be mediated by an increase in bradykinin levels that causes vasodilation and increased vascular permeability, resulting in localized swelling\u2014often seen in the tongue or facial area.",
        "pathophysiology": "tPA catalyzes the conversion of plasminogen to plasmin, which not only dissolves clots but can also lead to increased bradykinin production. Elevated bradykinin levels cause vascular leakage leading to angioedema. Patients with a history of ACE inhibitor use are at an increased risk, though it can occur independently. The underlying mechanism involves an atypical inflammatory response that is not IgE-mediated.",
        "clinical_correlation": "In this patient, although there is severe dysarthria (likely from tongue swelling affecting articulation), the airway remains uncompromised. Recognizing that the patient is stable without respiratory distress guides management away from invasive airway protection unless further compromise occurs.",
        "diagnostic_approach": "The diagnosis is primarily clinical with a correlation between recent tPA administration and the onset of localized swelling. Differential diagnoses include allergic reactions, anaphylaxis, or other causes of upper airway edema. However, the timing post-tPA and the focal nature (tongue angioedema) supports the diagnosis of tPA-induced angioedema.",
        "classification_and_neurology": "tPA-induced angioedema is classified as a drug-induced, bradykinin-mediated angioedema distinct from histamine-mediated allergic angioedema. Within the broader category of angioedema, etiologies include hereditary (C1 esterase inhibitor deficiency), acquired, allergic (IgE-mediated), and drug-induced forms. The nosology recognizes tPA-induced angioedema as a unique iatrogenic complication related to fibrinolytic therapy, often overlapping with ACEi-associated angioedema due to shared bradykinin pathways. Stroke management guidelines categorize this complication under adverse drug reactions requiring emergent intervention. Understanding this classification aids in targeted management, differentiating it from anaphylaxis or other causes of airway swelling.",
        "classification_and_nosology": "This condition is classified as an iatrogenic adverse drug reaction. It is specifically categorized under drug-induced angioedema, distinct from IgE-mediated allergic reactions.",
        "management_principles": "First-line treatment in tPA-induced angioedema is medical management using steroids (e.g., methylprednisolone) and antihistamines (e.g., diphenhydramine) to reduce inflammation and counter any histamine-mediated effects. Airway management (e.g., intubation) is reserved for cases with evidence of respiratory compromise or rapidly progressing edema. In pregnant or lactating patients, steroids and antihistamines are used when benefits outweigh risks; close monitoring of both mother and fetus is essential, and consultation with maternal\u2013fetal medicine is advised in severe cases.",
        "option_analysis": "Option A (Intubation) is inappropriate because the patient is currently stable without airway compromise\u2014intubation is indicated only when there is imminent respiratory failure or severe obstruction. Option B (Steroid with antihistamine) directly addresses the inflammatory and mediator-driven process, making it the correct initial management. Option C (ACE inhibitor with diuretics) is contraindicated because ACE inhibitors can exacerbate angioedema by further increasing bradykinin levels, and diuretics do not address the underlying issue and may worsen hemodynamics.",
        "clinical_pearls": "1. Always assess for airway compromise in patients with angioedema\u2014if the airway is stable, medical management is preferred. 2. tPA-induced angioedema is bradykinin-mediated, so typical anaphylaxis protocols (epinephrine) may not be effective. 3. History of concomitant ACE inhibitor use can increase the risk of this complication.",
        "current_evidence": "Recent stroke management guidelines acknowledge tPA-induced angioedema as a rare complication and recommend early medical management with steroids and antihistamines. Studies emphasize that prompt recognition and treatment can prevent progression to airway obstruction, reducing the overall morbidity associated with thrombolytic therapy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993205",
    "fields": {
      "question_number": "288",
      "question_text": "TIA found to have atrial flutter echo normal",
      "options": {
        "A": "(Factor Xa inhibitor) is correct as these agents have been shown to reduce the risk of cardioembolic stroke effectively. The marked answer was B, which is incorrect. Other potential options might include antiplatelet therapy or solely using rate"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Transient Ischemic Attacks (TIAs) associated with atrial flutter are typically the result of cardioembolic events. In nonvalvular atrial flutter, thrombus formation within the atria can lead to embolization and subsequent neurological deficits.",
        "pathophysiology": "Atrial flutter results in rapid, regular atrial contractions that foster blood stasis, particularly in the atrial appendage, thereby increasing the risk of thrombus formation. These emboli may dislodge and travel to cerebral vasculature causing TIAs or strokes. Although the echocardiogram is normal (suggesting no structural heart disease), the arrhythmia itself remains the source of embolism.",
        "clinical_correlation": "A patient with atrial flutter and TIA is at significant risk for future strokes of embolic origin. Recognizing the cardioembolic mechanism is essential for instituting appropriate long\u2010term anticoagulation to prevent recurrence.",
        "diagnostic_approach": "Diagnosis is confirmed through ECG demonstrating atrial flutter. Echocardiography is used to rule out structural abnormalities but does not exclude the risk posed by the arrhythmia. Differential diagnoses include TIAs from large artery atherosclerosis or small vessel disease, which typically have different risk profiles and management strategies.",
        "classification_and_neurology": "TIA is classified under cerebrovascular diseases, specifically ischemic cerebrovascular events. According to the American Heart Association/American Stroke Association (AHA/ASA) guidelines, TIA is defined clinically by transient neurological symptoms without infarction on imaging. Atrial flutter is classified as a supraventricular tachyarrhythmia within cardiac arrhythmias. In the context of stroke classification, the TOAST (Trial of Org 10172 in Acute Stroke Treatment) criteria categorize strokes and TIAs by etiology; atrial flutter-associated TIA falls under cardioembolic stroke/TIA subtype. This classification guides management decisions, particularly anticoagulation. The nosology has evolved with improved imaging and understanding of arrhythmia-related embolism, emphasizing the need for rhythm monitoring and anticoagulation in non-valvular atrial arrhythmias. Controversies exist regarding the relative embolic risk of atrial flutter versus atrial fibrillation, but current consensus treats them similarly for stroke prevention.",
        "classification_and_nosology": "This falls under the category of cardioembolic stroke/TIA. It is part of the broader group of ischemic strokes where the heart is the source of an embolism.",
        "management_principles": "The latest guidelines recommend the use of direct oral anticoagulants (DOACs), particularly Factor Xa inhibitors (e.g., apixaban, rivaroxaban), as first-line therapy for stroke prevention in patients with nonvalvular atrial flutter and atrial fibrillation. In the acute setting following a TIA, early initiation of appropriate anticoagulation is indicated. For pregnant patients, however, DOACs are contraindicated due to teratogenicity and limited safety data; low molecular weight heparin (LMWH) is preferred in such cases. Similar caution applies during lactation, with LMWH being considered safer.",
        "option_analysis": "Option A (Factor Xa inhibitor) is correct as these agents have been shown to reduce the risk of cardioembolic stroke effectively. The marked answer was B, which is incorrect. Other potential options might include antiplatelet therapy or solely using rate-control medications, but these do not address the embolic risk adequately.",
        "clinical_pearls": "1. Atrial flutter and fibrillation both confer a high risk for cardioembolic events, necessitating prompt anticoagulation. 2. Echocardiography may be normal in these patients despite significant embolic risk. 3. Factor Xa inhibitors are favored in the nonpregnant population for their ease of use and favorable risk\u2013benefit profile.",
        "current_evidence": "Recent trials and updates in cardiology guidelines support DOACs\u2014including Factor Xa inhibitors\u2014as first-line agents for stroke prevention in nonvalvular atrial arrhythmias. Ongoing research continues to compare outcomes between DOACs and warfarin, firmly establishing the DOAC class as a mainstay in this field."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993206",
    "fields": {
      "question_number": "289",
      "question_text": "Case of malignant MCA with mass effect and decreased level of consciousness found unresponsive, what will change outcomes",
      "options": {
        "A": "(Decompressive hemicraniectomy) directly addresses the life\u2010threatening cerebral edema and mass effect, thereby altering the natural history and improving survival and functional outcome. Option B (Stroke admission) is an important supportive measure but does not counteract the mass effect. Option C (Hyperventilation) may transiently reduce ICP via cerebral vasoconstriction but is not a definitive treatment, and its effects are short"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Malignant middle cerebral artery (MCA) infarction is a severe form of ischemic stroke characterized by extensive cerebral edema and mass effect, often leading to rapid neurological deterioration and death if left untreated.",
        "pathophysiology": "A large MCA infarct results in cytotoxic and vasogenic edema that significantly increases intracranial pressure (ICP). This swelling can lead to herniation syndromes, which are life-threatening. Decompressive hemicraniectomy is performed to alleviate the pressure, thereby reducing the risk of secondary brain injury.",
        "clinical_correlation": "Patients typically present with decreased level of consciousness, hemiparesis, and signs of raised ICP. The rapid deterioration seen in malignant MCA infarcts correlates with the underlying pathophysiology of uncontrollable edema and midline shift.",
        "diagnostic_approach": "Diagnosis is confirmed via neuroimaging such as CT or MRI, which shows a large infarct territory, midline shift, and signs of herniation. Differential diagnoses include intracerebral hemorrhage and cerebral venous thrombosis; however, the imaging characteristics and clinical setting help distinguish malignant MCA infarction.",
        "classification_and_neurology": "Malignant MCA infarction is classified as a subtype of large vessel ischemic stroke within the cerebrovascular disease spectrum. According to the TOAST classification, it falls under cardioembolic or large artery atherosclerosis strokes depending on etiology but is defined clinically and radiographically by its large infarct volume and malignant course. It is often differentiated from smaller MCA strokes by its rapid progression and life-threatening mass effect. The term \u201cmalignant\u201d reflects the high mortality and morbidity associated with the edema and herniation. Classification schemes have evolved to incorporate imaging criteria (e.g., infarct size >145 cm\u00b3 on diffusion-weighted MRI) that predict malignant edema. Current consensus guidelines recognize malignant MCA infarction as an indication for decompressive hemicraniectomy. Controversies in classification relate to timing and criteria for surgical intervention and the role of advanced imaging biomarkers. Overall, malignant MCA infarction is a severe clinical phenotype within the ischemic stroke family with distinct management implications.",
        "classification_and_nosology": "Malignant MCA syndrome is a subtype of large ischemic strokes associated with malignant edema and high mortality. It is categorized separately from other ischemic strokes owing to its rapid progression and poor natural history if untreated.",
        "management_principles": "The first-line treatment to change outcomes in malignant MCA infarction is decompressive hemicraniectomy, ideally performed within 24\u201348 hours of symptom onset, as multiple randomized controlled trials have demonstrated improved survival and functional outcomes. Supportive care in a specialized stroke unit is essential but not sufficient as a standalone intervention. In pregnant patients, decompressive surgery may still be indicated when maternal life is at risk; multidisciplinary management involving neurosurgery, obstetrics, and neonatology is critical. In lactating mothers, the surgical decision-making remains similar with additional supportive measures.",
        "option_analysis": "Option A (Decompressive hemicraniectomy) directly addresses the life\u2010threatening cerebral edema and mass effect, thereby altering the natural history and improving survival and functional outcome. Option B (Stroke admission) is an important supportive measure but does not counteract the mass effect. Option C (Hyperventilation) may transiently reduce ICP via cerebral vasoconstriction but is not a definitive treatment, and its effects are short-lived. The marked answer was D, which does not correspond to any effective intervention for altering outcomes in malignant MCA infarction.",
        "clinical_pearls": "1. Timely decompressive hemicraniectomy can significantly reduce mortality in malignant MCA infarction. 2. Recognize that supportive care alone (stroke unit admission) is not sufficient in the face of malignant edema. 3. Temporary measures like hyperventilation are only bridges to definitive therapy.",
        "current_evidence": "Landmark studies such as DESTINY, DECIMAL, and HAMLET have confirmed the benefit of early decompressive hemicraniectomy in selected patients with malignant MCA infarction. These studies have influenced current guidelines, emphasizing surgery within 48 hours as a key determinant of improved outcome."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993207",
    "fields": {
      "question_number": "290",
      "question_text": "SCA came with ??",
      "options": {},
      "correct_answer": "1",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Stroke involving the territory of the Superior Cerebellar Artery (SCA) can affect lateral midbrain and cerebellar structures. The involvement of descending sympathetic fibers leads to the development of ipsilateral Horner's syndrome, manifesting as ptosis, miosis, and anhidrosis.",
        "pathophysiology": "The SCA supplies parts of the lateral midbrain and upper cerebellum. Ischemia in this region may disrupt sympathetic pathways that run adjacent to these structures, thereby causing ipsilateral Horner's syndrome. The disruption is due to infarction of small fibers that regulate sympathetic outflow.",
        "clinical_correlation": "Patients with SCA stroke may present with cerebellar signs such as ataxia along with additional features like ipsilateral Horner's syndrome. Recognition of these signs assists in localizing the lesion to the lateral midbrain and SCA territory.",
        "diagnostic_approach": "Neuroimaging including MRI and CT angiography are used to delineate the affected vascular territory. The differential diagnosis includes lateral medullary (Wallenberg) syndrome, midbrain infarcts from other arterial distributions, and other brainstem pathologies. Isolated 4th nerve palsies usually point to lesions in the dorsal midbrain, which are less typical in SCA infarcts.",
        "classification_and_neurology": "SCA stroke is classified under ischemic strokes of the posterior circulation according to the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system. It falls within the category of large artery atherosclerosis or cardioembolism depending on etiology. The posterior circulation strokes encompass infarctions in territories supplied by the vertebral, basilar, posterior cerebral, and cerebellar arteries (including SCA, anterior inferior cerebellar artery, and posterior inferior cerebellar artery). The classification has evolved to emphasize vascular territory localization, facilitating tailored diagnostic and therapeutic approaches. While some frameworks separate brainstem and cerebellar strokes, the SCA stroke straddles both, highlighting the importance of integrated neurovascular understanding. There is consensus that clinical syndromes correspond closely to vascular territories, but overlap and variability exist.",
        "classification_and_nosology": "SCA infarcts are classified under brainstem and cerebellar strokes. They are considered part of the posterior circulation strokes, distinguished by their specific vascular territory and associated clinical syndromes.",
        "management_principles": "Management of SCA infarcts is largely supportive and similar to other ischemic strokes with antithrombotic therapy initiation, risk factor modification, and rehabilitation. In the acute setting, if the patient is within the thrombolytic window and meets criteria, IV thrombolysis may be considered. In pregnant or lactating patients, the risk\u2013benefit analysis of thrombolytic therapy is performed on a case-by-case basis, with current guidelines advising cautious use when indicated.",
        "option_analysis": "Option 1 (Ipsilateral Horner's syndrome) is correct because it is a classic clinical finding that results from involvement of sympathetic fibers in the lateral midbrain adjacent to the SCA territory. Option 2 (4th cranial nerve palsy) is incorrect, as isolated trochlear nerve involvement is uncommon in SCA infarcts and usually suggests a different midbrain lesion location.",
        "clinical_pearls": "1. Ipsilateral Horner's syndrome is a key lateralizing sign in strokes involving the lateral midbrain or upper brainstem. 2. Recognize that posterior circulation strokes have unique clinical syndromes compared to anterior circulation strokes. 3. Detailed neuro-ophthalmologic examination can significantly aid in lesion localization.",
        "current_evidence": "Recent reviews of posterior circulation stroke syndromes consolidate the finding that sympathetic pathway involvement, leading to ipsilateral Horner's syndrome, is a reliable clinical sign in SCA territory infarcts. Advanced imaging techniques continue to refine our understanding of the vascular territories involved in brainstem strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993208",
    "fields": {
      "question_number": "291",
      "question_text": "What to expect from O.A. infarction",
      "options": {
        "A": "Ipsilateral Horner",
        "B": "Ipsilateral hearing loss"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Ophthalmic artery (OA) infarction is an ocular ischemic event resulting from an abrupt interruption of blood flow to the retina. This condition is most commonly associated with embolic or thrombotic occlusion of the ophthalmic artery, a branch of the internal carotid artery.",
        "pathophysiology": "When the ophthalmic artery is occluded, the retina suffers an abrupt ischemic insult because it has minimal collateral supply. The resulting retinal ischemia quickly leads to cell death and irreversible vision loss unless very prompt interventions are instituted. The embolus may originate from atherosclerotic plaques or cardioembolic sources.",
        "clinical_correlation": "Clinically, OA infarction presents as sudden, usually painless, monocular visual loss. Patients may also exhibit a relative afferent pupillary defect on examination with fundoscopic findings such as a pale retina with a cherry-red spot at the fovea. In contrast, signs such as ipsilateral Horner syndrome or hearing loss are more typical with other vascular territories (e.g., carotid dissection or labyrinthine infarction).",
        "diagnostic_approach": "Diagnosis is made with an urgent ophthalmologic evaluation including fundoscopic exam and ancillary tests such as fluorescein angiography. Vascular imaging (e.g., carotid Doppler ultrasound or CTA) should be pursued to identify embolic sources. Differential diagnoses include central retinal artery occlusion (CRAO) from other causes, giant cell arteritis (in older individuals), and acute optic neuritis.",
        "classification_and_neurology": "Ophthalmic artery infarction is classified under ischemic cerebrovascular diseases, specifically as part of anterior circulation strokes involving the internal carotid artery and its branches. It falls within the broader category of ocular ischemic syndromes and retinal artery occlusions. The American Heart Association/American Stroke Association (AHA/ASA) stroke classification systems categorize this as a large artery atherosclerosis or embolic stroke depending on etiology. The condition is distinct from posterior circulation strokes, which affect the brainstem and cerebellum, and from other ocular pathologies such as optic neuritis or glaucoma. Contemporary nosology emphasizes vascular territory-based classification to guide diagnosis and management. There is consensus on the importance of differentiating ophthalmic artery infarction from other causes of monocular vision loss due to its vascular implications and stroke risk.",
        "classification_and_nosology": "Ophthalmic artery infarction falls under ocular ischemic syndromes and is classified as a type of retinal circulatory disorder. It is distinct from other causes of acute vision loss such as optic neuritis or retinal detachment.",
        "management_principles": "Management is considered emergent. Options include measures aimed at dislodging the embolus (e.g., ocular massage, intraocular pressure reduction with medications) and systemic management (antiplatelet agents, risk factor optimization). There is limited evidence for thrombolytic or surgical interventions in this setting. In pregnant or lactating patients, any systemic medications must be carefully chosen to balance maternal benefit with fetal/neonatal safety; procedural interventions, when deemed life- or sight\u2010saving, are generally pursued with appropriate shielding and precautions.",
        "option_analysis": "\u2022 Option A (Ipsilateral Horner): This finding is more characteristic of carotid dissection rather than an OA infarction. \n\u2022 Option B (Ipsilateral Hearing Loss): Sudden hearing loss is more typically seen with infarction of the labyrinthine artery (usually a branch of the anterior inferior cerebellar artery) rather than the ophthalmic artery. \n\u2022 Option C: Although the text is missing here, it is presumed that Option C was intended to describe the hallmark presentation of OA infarction (i.e., acute, painless monocular vision loss with retinal findings). \n\u2022 Option D: Not provided.",
        "clinical_pearls": "1. The retina is exquisitely sensitive to ischemia, and irreversible damage may occur within a short time window. \n2. Sudden monocular vision loss should prompt immediate evaluation for vascular occlusive disease. \n3. Always consider systemic vascular risk factors and embolic sources in patients with ocular ischemia.",
        "current_evidence": "Recent studies and reviews have emphasized that early recognition and treatment of retinal arterial occlusions are crucial; however, no treatment modality (including thrombolysis) has consistently proven effective. Current guidelines remain focused on rapid risk factor assessment and secondary prevention rather than a standardized acute intervention, and research into hyperacute reperfusion strategies is ongoing."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993209",
    "fields": {
      "question_number": "292",
      "question_text": "45 YO female came with SAH and found to have P-chom aneurysm what's next",
      "options": {
        "A": "Endovascular coiling",
        "B": "Surgical clipping",
        "C": "Observation"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Aneurysmal subarachnoid hemorrhage (SAH) with a posterior communicating (P-com or P-chom) artery aneurysm is a neurosurgical emergency. The primary goal is to prevent rebleeding by securing the aneurysm.",
        "pathophysiology": "Rupture of a P-com aneurysm leads to bleeding into the subarachnoid space, causing a sudden rise in intracranial pressure, meningeal irritation, and potential for vasospasm. The P-com aneurysm is one of the common sites for aneurysms and is intimate with the oculomotor nerve, which can lead to nerve palsies.",
        "clinical_correlation": "Patients typically present with a sudden, severe (\u2018thunderclap\u2019) headache, often accompanied by neck stiffness, nausea/vomiting, and in some cases, focal neurological deficits such as third nerve palsy. Rapid identification and treatment are essential to reduce mortality and complications from rebleeding or vasospasm.",
        "diagnostic_approach": "Initial evaluation includes a non\u2010contrast CT scan to detect SAH, followed by vascular imaging such as CT angiography (CTA) or digital subtraction angiography (DSA) to diagnose and precisely localize the aneurysm. Differential diagnoses include other causes of SAH such as perimesencephalic hemorrhage and arteriovenous malformations.",
        "classification_and_neurology": "Ruptured intracranial aneurysms causing SAH fall under the broader category of cerebrovascular disorders and neurovascular emergencies. They are classified by location (anterior vs posterior circulation), morphology (saccular, fusiform), and rupture status (ruptured vs unruptured). The International Subarachnoid Aneurysm Trial (ISAT) and other consensus guidelines have helped refine classification and management approaches. The World Federation of Neurosurgical Societies (WFNS) grading system and Hunt and Hess scale classify SAH severity based on clinical presentation. This nosology aids in prognostication and treatment planning. Controversies remain regarding the best approach for certain aneurysm types and patient subgroups, but consensus favors early aneurysm securing in ruptured cases.",
        "classification_and_nosology": "Aneurysmal SAH falls within cerebrovascular accidents resulting from aneurysm rupture. Aneurysms are classified by their location (e.g., anterior communicating, posterior communicating, middle cerebral) and morphology (saccular, fusiform, etc.).",
        "management_principles": "The definitive management is to secure the aneurysm. Endovascular coiling is generally considered the first-line intervention when the aneurysm anatomy is favorable, particularly following large randomized trials (such as the ISAT) which demonstrated improved outcomes with coiling in appropriate cases. Surgical clipping remains an alternative when coiling is not feasible. In pregnant or lactating patients, the decision must balance maternal risk and fetal exposure to radiation and contrast agents; shielding and careful procedural planning can mitigate risks.",
        "option_analysis": "\u2022 Option A (Endovascular coiling): Correct \u2013 It is considered first-line therapy for many ruptured aneurysms, including P-com aneurysms, when anatomy permits. \n\u2022 Option B (Surgical clipping): While a valid alternative, it is typically reserved for aneurysms not amenable to endovascular treatment. \n\u2022 Option C (Observation): Inappropriate in the context of a ruptured aneurysm due to the imminent risk of rebleeding.",
        "clinical_pearls": "1. In aneurysmal SAH, securing the aneurysm as early as possible greatly reduces the risk of rebleeding. \n2. P-com aneurysms can produce an acute third nerve palsy. \n3. The ISAT trial has significantly influenced the preference for endovascular management in suitable aneurysms.",
        "current_evidence": "Current guidelines and recent evidence support endovascular coiling as a first\u2010line therapy for ruptured cerebral aneurysms when indicated by their size and shape. Ongoing research continues to refine criteria for selecting between clipping and coiling, with an emphasis on reducing complications and improving long-term outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993210",
    "fields": {
      "question_number": "293",
      "question_text": "Clear scenario of anterior choroidal artery infarction, they brought VF suggestive of it",
      "options": {
        "A": "anterior choroidal artery infarction"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Anterior choroidal artery infarction is a distinct type of ischemic stroke affecting the small branch of the internal carotid system. It has a characteristic clinical presentation that helps localize the lesion.",
        "pathophysiology": "Occlusion of the anterior choroidal artery results in ischemia of structures such as the posterior limb of the internal capsule, parts of the optic radiation, and the medial temporal lobe. The resulting infarct produces a combination of motor, sensory, and visual deficits.",
        "clinical_correlation": "Patients with anterior choroidal artery infarction may show contralateral hemiparesis, hemisensory loss, and specific visual field deficits (typically a homonymous hemianopia). The presence of a visual field defect that corresponds with the infarct territory supports the diagnosis.",
        "diagnostic_approach": "Diagnosis is made via neuroimaging studies \u2013 diffusion-weighted MRI is highly sensitive in the hyperacute setting, while CT scans can help in the early phase and rule out hemorrhage. Differential diagnoses include lacunar strokes from other small vessel occlusions and infarctions in the posterior cerebral artery territory.",
        "classification_and_neurology": "Anterior choroidal artery infarction is classified under ischemic strokes within the cerebrovascular disease taxonomy. According to the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification, it is categorized as a large artery atherosclerosis or cardioembolism subtype depending on etiology. The AChA infarction is a subtype of lacunar or subcortical infarcts but differs from classic small vessel lacunes due to its vascular territory and clinical presentation. The classification of stroke by vascular territory is essential for clinical localization and management. Over time, neuroimaging advances have refined the understanding of AChA infarction as a distinct clinical and radiological entity. There is some debate about the overlap between AChA and MCA or PCA infarcts, but consensus supports recognizing AChA territory infarcts based on clinical and imaging criteria. This classification aids in prognosis and therapeutic decision-making.",
        "classification_and_nosology": "This condition is classified as a type of ischemic stroke, often due to small vessel disease or embolism affecting the branch vessels of the internal carotid artery.",
        "management_principles": "Management of an anterior choroidal artery infarct follows standard acute ischemic stroke protocols. If the patient presents within the thrombolytic window, IV thrombolysis may be indicated. Secondary prevention with antiplatelet agents, control of risk factors (hypertension, diabetes, hyperlipidemia), and rehabilitation are essential. In pregnant or lactating patients, thrombolytic use is carefully considered based on risk-benefit analysis, and antiplatelet therapy selection is guided by safety data in these populations.",
        "option_analysis": "\u2022 Option A (Anterior choroidal artery infarction): Correct \u2013 the clinical vignette clearly supports this diagnosis. \n\u2022 Other options: Not provided, making Option A the only and thus the correct answer in context.",
        "clinical_pearls": "1. The classic triad of anterior choroidal artery infarction is contralateral hemiparesis, hemisensory loss, and homonymous hemianopia. \n2. Diffusion-weighted MRI is the gold standard for early detection of small vessel strokes. \n3. Prompt recognition allows for timely intervention and secondary prevention.",
        "current_evidence": "Recent studies reiterate the importance of early imaging and intervention in ischemic stroke. Guidelines continue to support thrombolysis for eligible patients with small vessel infarcts, and ongoing research focuses on neuroprotective strategies and long-term rehabilitation outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993211",
    "fields": {
      "question_number": "294",
      "question_text": "Stroke all stroke workups mentioned except CTA asked what to do next",
      "options": {
        "A": "(CTA): Correct"
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Acute stroke workup aims not only to rule out hemorrhage but also to evaluate the cerebral vasculature for occlusions or stenoses that may guide reperfusion strategies like thrombectomy. CTA (computed tomography angiography) is critical for visualizing the intracranial vessels.",
        "pathophysiology": "In the setting of an ischemic stroke, rapid imaging beyond a non-contrast CT is essential to assess vessel patency. CTA provides detailed images of both extracranial and intracranial arteries, identifying occlusions or significant stenoses that could be amenable to endovascular intervention.",
        "clinical_correlation": "After initial stroke imaging (typically non-contrast CT to exclude hemorrhage), if the clinical picture supports an ischemic stroke and intervention is under consideration, CTA is the next step. It is especially indicated in patients who may benefit from mechanical thrombectomy and helps in differentiating large vessel occlusion strokes from smaller infarcts.",
        "diagnostic_approach": "The standard acute stroke imaging protocol begins with a non-contrast head CT followed by CTA to assess the cerebral vasculature. Differential imaging modalities such as MRA or carotid Doppler have more limited roles in the hyperacute phase. Carotid Doppler, for instance, evaluates mainly extracranial vessels, while MRI/MRA may not be rapidly available.",
        "classification_and_neurology": "Stroke classification systems, such as the TOAST criteria, categorize ischemic strokes based on etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. Vascular imaging including CTA is instrumental in classifying strokes as large artery atherosclerosis or dissection by revealing arterial pathology. The American Heart Association/American Stroke Association (AHA/ASA) guidelines emphasize vascular imaging as part of the comprehensive stroke evaluation. The classification informs secondary prevention strategies and prognosis. Over time, stroke classification has evolved to integrate advanced imaging findings, recognizing the heterogeneity of stroke mechanisms and facilitating personalized management.",
        "classification_and_nosology": "Acute stroke evaluation is broadly divided into imaging protocols focused on hemorrhagic versus ischemic stroke, with CTA playing a central role in identifying large vessel occlusions (LVOs) in ischemic strokes.",
        "management_principles": "Once CTA confirms large vessel occlusion or other vascular abnormalities, the treatment plan may include intravenous thrombolysis (if within the time window) followed by mechanical thrombectomy. In pregnancy or lactating patients, careful shielding is employed to reduce fetal radiation exposure; decisions are based on a risk-benefit assessment given the emergent nature of stroke.",
        "option_analysis": "\u2022 Option A (CTA): Correct \u2013 It is the next appropriate step as it provides essential vascular information that complements non-contrast CT findings. \n\u2022 Other options (Non-contrast CT alone, carotid Doppler, MRI/MRA, cardiac evaluation): These are either limited in vascular evaluation or not immediately practical in the emergent setting and therefore do not replace CTA in acute stroke protocols.",
        "clinical_pearls": "1. CTA is indispensable in the acute stroke setting for identifying large vessel occlusions that might benefit from thrombectomy. \n2. Time is brain: rapid and accurate imaging directly influences acute management and outcomes. \n3. Integration of CTA findings with clinical assessment optimizes patient selection for reperfusion therapies.",
        "current_evidence": "Recent guidelines from the American Heart Association/American Stroke Association (AHA/ASA) underscore the importance of CTA in acute stroke protocols. Research continues to refine imaging selection criteria to identify patients most likely to benefit from advanced endovascular therapies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993212",
    "fields": {
      "question_number": "295",
      "question_text": "Scenario patient feeling unwell, then start seeing animals after which he had decreased LOC intubated, decerebrate posturing CT brain attached showed hyperdense basilar sign otherwise no clear ischemic changes what to do next",
      "options": {
        "A": "(CTA) is correct because after seeing the hyperdense basilar sign, CTA is the appropriate next diagnostic step to determine the exact location and extent of the occlusion. Option B (EEG) is incorrect because EEG evaluates electrical brain activity and is not useful in diagnosing vascular occlusions."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "The hyperdense basilar artery sign is a classic radiologic clue for basilar artery occlusion. In a patient with altered mental status and brainstem signs (e.g., decerebrate posturing), identifying a vascular occlusion is critical. CTA is recognized as the primary non\u2010invasive vascular imaging modality to evaluate suspected occlusions.",
        "pathophysiology": "Basilar artery occlusion is generally the result of thromboembolic disease. The hyperdense sign on noncontrast CT represents a clot within the artery, which leads to reduced or absent blood flow to brainstem structures. This occlusion results in ischemia of critical structures, leading to rapid neurologic deterioration, as evidenced by decreased level of consciousness and posturing abnormalities.",
        "clinical_correlation": "Clinically, patients with basilar artery occlusion may present with symptoms ranging from visual disturbances and vertigo to coma and decerebrate posturing because of brainstem involvement. The acute neurologic deterioration observed in this case fits the profile of a posterior circulation stroke.",
        "diagnostic_approach": "After identifying the hyperdense sign on CT, the next step is to perform computed tomography angiography (CTA) to confirm the diagnosis. Differential diagnoses may include other causes of coma or brainstem dysfunction such as hemorrhage, encephalitis, or metabolic derangements; however, the imaging clue of a hyperdense artery specifically points to vascular occlusion.",
        "classification_and_neurology": "Basilar artery occlusion is classified under **ischemic strokes**, specifically within the **posterior circulation stroke** subgroup. According to the TOAST classification, it falls under **large artery atherosclerosis** or **cardioembolism** depending on etiology. Posterior circulation strokes encompass infarctions in territories supplied by the vertebral, basilar, and posterior cerebral arteries. The classification of stroke types has evolved to emphasize vascular territory and mechanism, aiding targeted management. BAO represents a severe subset of large vessel occlusions with high morbidity and mortality. Contemporary stroke classifications incorporate imaging findings such as vessel occlusion on CTA/MRA to refine diagnosis and guide reperfusion strategies. There is consensus that BAO requires urgent recognition distinct from anterior circulation strokes due to its unique clinical and prognostic implications.",
        "classification_and_nosology": "Basilar artery occlusion falls under the category of acute ischemic strokes affecting the posterior circulation. It is classified as a large vessel occlusion (LVO), which often requires emergent reperfusion therapy.",
        "management_principles": "Once a basilar artery occlusion is confirmed on CTA, management may include intravenous thrombolysis if within the time window and mechanical thrombectomy. Early recanalization is critical for reducing morbidity and mortality. In pregnant or lactating patients, the use of CTA is generally considered safe with appropriate shielding, and treatment decisions (such as IV thrombolysis) require a careful risk-benefit analysis balancing maternal and fetal risks.",
        "option_analysis": "Option A (CTA) is correct because after seeing the hyperdense basilar sign, CTA is the appropriate next diagnostic step to determine the exact location and extent of the occlusion. Option B (EEG) is incorrect because EEG evaluates electrical brain activity and is not useful in diagnosing vascular occlusions.",
        "clinical_pearls": "1. The hyperdense basilar artery sign on noncontrast CT is an important early indicator of basilar occlusion. 2. CTA is the gold standard noninvasive imaging modality for confirming vascular occlusions in acute stroke settings.",
        "current_evidence": "Recent stroke management guidelines emphasize the importance of rapid vascular imaging in suspected posterior circulation strokes. Studies have confirmed that early CTA allows for prompt decision-making regarding reperfusion therapies, which is critical in basilar occlusion cases."
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
