
# Import batch 1 of 3 from chunk_5_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993086",
    "fields": {
      "question_number": "312",
      "question_text": "Patient with tongue deviation to the left side and ptosis in his left upper eyelid, what is the artery involved?",
      "options": {
        "A": "ICA"
      },
      "correct_answer": "D",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question tests knowledge of brainstem vascular territories. A patient presenting with ipsilateral tongue deviation implies a lesion of the hypoglossal nerve (CN XII) or its nucleus in the medulla, and ipsilateral ptosis suggests disruption of sympathetic fibers, often seen in Horner syndrome. These findings together point toward a combined medullary involvement that is typically seen with a vertebral artery insult.",
        "pathophysiology": "The vertebral artery and its branches supply both the medial and lateral parts of the medulla. Infarction in this region can affect the hypoglossal nucleus (resulting in tongue deviation toward the lesion) and the adjacent descending sympathetic fibers (leading to ptosis as part of Horner syndrome). This pattern may result from vertebral artery dissection or thrombosis compromising both the paramedian branches (feeding the medial medulla) and the branches (such as PICA, which supplies the lateral medulla) when the occlusion is proximal enough to affect both territories.",
        "clinical_correlation": "Clinically, patients may present with tongue deviation toward the side of the lesion due to ipsilateral hypoglossal nerve involvement, while ptosis is a hallmark of associated Horner syndrome. This constellation of signs should prompt imaging workup for medullary infarction, with attention to the vertebral artery.",
        "diagnostic_approach": "Initial evaluation involves non-contrast CT to rule out hemorrhage, followed by MRI with diffusion\u2010weighted imaging and vascular imaging (MRA, CTA, or DSA) to confirm an infarct and assess the integrity of the vertebral artery. Differential diagnoses include isolated medial medullary syndrome (usually from anterior spinal artery occlusion) and lateral medullary (Wallenberg) syndrome, but the combined features point toward vertebral artery pathology.",
        "classification_and_neurology": "The condition falls within the **ischemic stroke syndromes** classified by vascular territory involvement. The internal carotid artery stroke is categorized under large vessel occlusion strokes in the TOAST classification system, which stratifies ischemic strokes by etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology.   This patient\u2019s presentation aligns with a large artery atherosclerosis affecting the ICA and its branches. The classification helps guide diagnosis and management.   Controversies exist regarding the precise boundaries of vascular territories and overlap syndromes, but consensus supports the ICA as the primary artery involved in such combined cranial nerve deficits.",
        "classification_and_nosology": "This presentation falls under the category of posterior circulation stroke. It may be classified as a brainstem stroke with overlapping features of medial medullary syndrome (tongue deviation from CN XII involvement) and lateral medullary syndrome (ptosis from disrupted sympathetic fibers).",
        "management_principles": "Acute management follows standard ischemic stroke protocols: rapid neuroimaging, consideration of thrombolysis or endovascular intervention (if within the therapeutic window), and aggressive management of vascular risk factors. In cases of vertebral artery dissection, antithrombotic therapy (anticoagulants or antiplatelets) is indicated. In pregnant or lactating women, treatment decisions are made cautiously; intravenous thrombolysis may be considered if the benefits outweigh risks, and antithrombotic agents with established safety profiles in pregnancy (e.g., low-dose aspirin) might be used.",
        "option_analysis": "Option A (ICA) is incorrect as the internal carotid artery supplies the anterior circulation and does not primarily supply the medulla. The marked answer D implies the vertebral artery, which is the correct vessel implicated as it supplies the medullary regions containing both the hypoglossal nucleus and the descending sympathetic fibers.",
        "clinical_pearls": "1. Ipsilateral tongue deviation indicates a lesion of the hypoglossal nucleus or nerve; 2. Ptosis in the setting of brainstem stroke should prompt consideration of an associated Horner syndrome from lateral medullary involvement; 3. Combined medial and lateral medullary signs are highly suggestive of vertebral artery pathology.",
        "current_evidence": "Recent studies underscore the importance of early vascular imaging in brainstem strokes. Advances in endovascular treatments and refined criteria for thrombolysis are improving outcomes in vertebral artery-related strokes. Current stroke guidelines emphasize detailed evaluation of the posterior circulation, especially in cases demonstrating mixed medullary findings."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993087",
    "fields": {
      "question_number": "313",
      "question_text": "Brain CT showing right SCA territory infarction (level of midbrain) and asked about the artery",
      "options": {
        "A": "SCA"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question focuses on the identification of the vascular territory involved in a midbrain infarction seen on CT. The Superior Cerebellar Artery (SCA) supplies not only portions of the cerebellum but also parts of the midbrain, making it the target vessel in SCA territory infarctions.",
        "pathophysiology": "Occlusion of the SCA, which originates from the basilar artery near the rostral pons, can lead to infarction of the superior aspect of the cerebellum and nearby midbrain structures. This disruption of blood flow results in localized ischemia and consequent neurological deficits.",
        "clinical_correlation": "Patients with SCA territory infarction may present with ataxia, dysmetria, and sometimes ocular motor disturbances if adjacent midbrain structures are compromised. The CT finding localizes the infarct to the SCA territory at the level of the midbrain, correlating with these clinical findings.",
        "diagnostic_approach": "After an initial non-contrast CT to exclude hemorrhage, MRI with diffusion-weighted imaging provides better detail of the infarction. Vascular imaging such as MRA or CTA is used to confirm occlusion of the SCA. Differential diagnoses include infarctions in adjacent territories such as the posterior cerebral artery (PCA) territory, but the CT localization helps narrow the diagnosis.",
        "classification_and_neurology": "SCA infarctions are classified under **posterior circulation strokes**, which include infarcts in territories supplied by the vertebral, basilar, posterior cerebral, and cerebellar arteries (including SCA, anterior inferior cerebellar artery [AICA], and posterior inferior cerebellar artery [PICA]).  The TOAST classification system categorizes ischemic strokes based on etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined cause, and undetermined cause), which applies to SCA strokes as well. The SCA infarct falls under large artery or cardioembolic strokes depending on the mechanism.   Historically, cerebellar strokes were less well understood but are now recognized as distinct entities with specific clinical and radiologic features. The current consensus emphasizes detailed vascular territory localization to guide management.",
        "classification_and_nosology": "This infarct is categorized as a posterior circulation stroke. Strokes involving the SCA are less common than other posterior circulation events but have a distinct vascular supply and clinical presentation.",
        "management_principles": "Management of SCA infarcts follows standard ischemic stroke guidelines: prompt reperfusion therapy (if within the window), supportive care, and secondary prevention with antithrombotic therapy and risk factor modification. In pregnant or lactating patients, thrombolytics may be used with careful consideration of maternal and fetal risks, and antiplatelet agents with safety data in pregnancy are preferred.",
        "option_analysis": "Option A, which identifies the Superior Cerebellar Artery as the vessel involved, is correct. Other potential options (not provided) would involve vessels not supplying this region (e.g., posterior cerebral or anterior inferior cerebellar arteries), making Option A the best choice in this scenario.",
        "clinical_pearls": "1. The SCA supplies the rostral cerebellum and parts of the midbrain; 2. Infarction in this territory can lead to cerebellar ataxia and coordination deficits; 3. Accurate vascular localization on imaging is key to guiding appropriate management.",
        "current_evidence": "Current stroke guidelines recommend detailed imaging of the posterior circulation in suspected SCA infarcts. Emerging endovascular techniques and improved MRI protocols are enhancing early diagnosis and management of these less common strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_6.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993088",
    "fields": {
      "question_number": "314",
      "question_text": "74-year-old male with CT brain image showing large hemorrhage in the cortex what to do next",
      "options": {
        "A": "(MRI): Though MRI (especially with SWI) is sensitive for detecting microbleeds and cavernous malformations, it is not the first",
        "B": "(CTA): CTA is a rapid, non",
        "C": "(Conventional angiography"
      },
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question addresses the appropriate next step in the evaluation of a large cortical hemorrhage in a 74-year-old male, with suspicion for an underlying vascular malformation (e.g., cerebral angiodysplasia). The stepwise diagnostic process is critical for planning further therapeutic interventions.",
        "pathophysiology": "A large cortical hemorrhage in an elderly patient may be due to rupture of abnormal vascular structures such as arteriovenous malformations (AVMs) or cavernous malformations. The vulnerability of these malformed vessels to bleeding necessitates detailed vascular imaging to delineate the lesion\u2019s architecture and hemodynamics.",
        "clinical_correlation": "Clinically, patients with cortical hemorrhages may present acutely with focal neurological deficits, headache, or seizures. When imaging reveals a cortical bleed, it is important to consider vascular malformations as a cause, especially in the absence of other risk factors such as severe hypertension.",
        "diagnostic_approach": "Initial evaluation begins with a non-contrast CT to identify hemorrhage. While MRI (with specialized sequences like SWI) and CTA can provide additional information, conventional digital subtraction angiography (DSA) remains the gold standard for detailed visualization of cerebral vasculature, particularly in the assessment of complex vascular malformations. Differential diagnoses include hypertensive hemorrhage, amyloid angiopathy, or hemorrhagic transformation of an ischemic stroke, but the cortical location raises suspicion for an underlying malformation.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on location, etiology, and underlying pathology. The primary classification separates hemorrhages into lobar (cortical), deep (basal ganglia, thalamus), brainstem, and cerebellar. Etiologically, ICH is divided into hypertensive, amyloid angiopathy-related, vascular malformations (AVMs, cavernous malformations, dural arteriovenous fistulas), neoplastic, coagulopathic, and traumatic. The diagnosis of vascular malformations falls under the cerebrovascular disease category in the WHO classification of neurological disorders. Over time, advanced imaging modalities have refined classification by allowing identification of specific vascular lesions. Controversies remain regarding the classification of certain small vascular lesions and their hemorrhagic risk, but consensus supports angiographic evaluation to guide management.",
        "classification_and_nosology": "Intracerebral hemorrhages are classified based on location (lobar vs. deep) and etiology (hypertensive, amyloid, vascular malformation). A large cortical hemorrhage in an elderly patient with suspected vascular malformation is best evaluated further by categorizing the lesion based on DSA findings.",
        "management_principles": "Once a vascular malformation is identified, management may include endovascular embolization, surgical resection, or radiosurgery, guided by the lesion\u2019s size, location, and vascular supply. In the acute setting, managing intracranial pressure and stabilizing the patient are priorities. For pregnant or lactating patients, imaging modalities that minimize radiation exposure are preferred; however, if DSA is indicated, appropriate shielding and risk\u2013benefit analysis must be performed, as maternal neurological stability is paramount.",
        "option_analysis": "\u2022 Option a (MRI): Though MRI (especially with SWI) is sensitive for detecting microbleeds and cavernous malformations, it is not the first-line test in the emergent evaluation of a large cortical hemorrhage due to limited availability and potential to miss high-flow abnormalities. \n\u2022 Option b (CTA): CTA is a rapid, non-invasive method but may not detect all subtleties of small or complex vascular malformations. \n\u2022 Option c (Conventional angiography - DSA): This option is correct because DSA is the gold standard, providing high-resolution and dynamic imaging necessary for detailed assessment of the lesion and for planning therapeutic interventions.",
        "clinical_pearls": "1. In cortical hemorrhages, always consider an underlying vascular malformation; 2. DSA remains the definitive imaging technique for complex cerebrovascular evaluations; 3. Quick and accurate vascular assessment guides appropriate management and improves outcomes.",
        "current_evidence": "Recent guidelines and studies have reinforced the use of DSA in cases of lobar hemorrhage with suspicion for vascular malformations. Emerging techniques in interventional neuroradiology continue to improve the safety and efficacy of endovascular treatments following DSA-based diagnosis."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_27.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993089",
    "fields": {
      "question_number": "315",
      "question_text": "Patient post MVA came with symptoms of lateral medullar, mechanism of stroke?",
      "options": {
        "A": ", which posits a mechanism involving vertebral artery injury leading to artery"
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "This question evaluates understanding of the mechanism of stroke following trauma, specifically in the context of lateral medullary syndrome. The lateral medulla is most commonly affected by occlusion of the Posterior Inferior Cerebellar Artery (PICA), which itself is often compromised secondary to vertebral artery injury.",
        "pathophysiology": "In patients following a motor vehicle accident (MVA), trauma can lead to injury of the vertebral artery. Such injury can result in dissection or intimal damage that promotes thrombus formation. The resulting artery-to-artery embolism can lodge in the branches of the vertebral artery (notably PICA) and cause ischemia in the lateral medulla, producing the classic symptoms of lateral medullary (Wallenberg) syndrome.",
        "clinical_correlation": "Patients with lateral medullary syndrome typically present with a constellation of symptoms such as dysphagia, hoarseness, vertigo, ataxia, and loss of pain and temperature sensation on the ipsilateral face with contralateral body involvement. In the context of trauma, the mechanism of vertebral artery injury is highly relevant in explaining these clinical manifestations.",
        "diagnostic_approach": "Diagnosis involves neuroimaging. CT and MRI help localize the infarct, while vascular imaging (CTA, MRA, or DSA) is essential to demonstrate vertebral artery injury and possible dissection. Differential diagnoses include cardioembolism, small vessel disease (typically causing lacunar infarcts), and venous thrombosis, but in trauma, vertebral artery dissection is most consistent with the presentation.",
        "classification_and_neurology": "Lateral medullary syndrome is classified under ischemic strokes affecting the posterior circulation territory, specifically brainstem strokes. According to the TOAST classification, it falls under large artery atherosclerosis or artery-to-artery embolism if caused by vertebral artery dissection or thrombus. It is part of the broader category of brainstem infarcts, which are further subdivided by vascular territory (e.g., medial medullary, lateral medullary, pontine, midbrain strokes). The syndrome is named after Wallenberg, who first described the clinical features associated with lateral medullary infarction. The nosology has evolved with advances in neuroimaging, allowing more precise localization and identification of vascular lesions. While traditionally attributed to atherosclerosis, the recognition of traumatic vertebral artery dissection and artery-to-artery thromboembolism has refined the classification and understanding of its etiology. There remains some debate about subclassification based on etiology (dissection vs. atherosclerosis) but consensus supports artery-to-artery thrombus as a primary mechanism in trauma-related cases.",
        "classification_and_nosology": "Lateral medullary syndrome is categorized as a posterior circulation stroke. When trauma is involved, the underlying etiology is typically arterial dissection with secondary thromboembolism.",
        "management_principles": "Management includes stabilizing the patient, antithrombotic therapy (anticoagulation or antiplatelet therapy) to prevent further embolism, and close monitoring of neurological status. In cases of vertebral artery dissection, conservative management is often preferred. For pregnant and lactating patients, therapeutic choices should consider both maternal and fetal safety; for instance, low molecular weight heparin is often used due to its safety profile in pregnancy.",
        "option_analysis": "Option a, which posits a mechanism involving vertebral artery injury leading to artery-to-artery thrombus formation, is correct. Other mechanisms such as cardioembolism, small vessel disease, or venous thrombosis are less consistent with the trauma-induced scenario and the specific vascular distribution of the lateral medulla.",
        "clinical_pearls": "1. Lateral medullary syndrome (Wallenberg syndrome) is classically due to occlusion of PICA; in trauma, this is most often secondary to vertebral artery dissection. 2. Early vascular imaging is key in trauma patients to identify vertebral artery injury. 3. Management with antithrombotic therapy can prevent further embolic events in cases of arterial dissection.",
        "current_evidence": "Recent literature emphasizes the importance of early recognition and treatment of vertebral artery dissection in the setting of trauma. Updated guidelines support the use of antithrombotic therapy and detailed vascular imaging (preferably DSA in complex cases) to guide management and improve outcomes in patients with lateral medullary syndrome."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993090",
    "fields": {
      "question_number": "316",
      "question_text": "Acute stroke With CT image with no established stroke ASPECT 8? Was treated with tPA CTA done and prepared for thrombectomy then he vomited (increase ICP \u2192 (ICH)?) and become lethargic bp 180/110",
      "options": {},
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "When managing an acute stroke patient who has received tPA, any sudden neurological deterioration must be evaluated immediately with imaging to determine complications, especially hemorrhagic transformation. The core concept is to use imaging as a decision-making tool before altering therapeutic measures.",
        "pathophysiology": "Thrombolytic therapy can predispose patients to hemorrhagic transformation due to reperfusion injury. Vomiting and lethargy may indicate raised intracranial pressure secondary to bleeding. Additionally, high blood pressure can exacerbate hemorrhage by increasing the transmural capillary pressure, further compromising the blood-brain barrier.",
        "clinical_correlation": "In the described case, the patient\u2019s sudden deterioration (vomiting and lethargy) following tPA is highly concerning for hemorrhage. The clinical scenario necessitates a rapid, non\u2010contrast CT scan to distinguish between hemorrhagic transformation, malignant edema, or other complications.",
        "diagnostic_approach": "The immediate diagnostic step is to obtain a non-contrast head CT to confirm or exclude intracranial hemorrhage. Differential diagnoses include hemorrhagic transformation (the most likely in this context), malignant cerebral edema post-stroke, or other intracranial events. Prompt imaging is vital to guide further interventions such as ceasing tPA or implementing controlled blood pressure reduction.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases in the ICD-11 and the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification system, which categorizes ischemic stroke by etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined cause, and undetermined cause). Hemorrhagic transformation is a secondary complication classified by radiological criteria (e.g., hemorrhagic infarction vs. parenchymal hematoma) and clinical severity. The management of acute ischemic stroke with reperfusion therapies is guided by clinical and imaging criteria, including ASPECTS for early ischemic changes and vessel imaging for thrombectomy candidacy. This case exemplifies the dynamic interplay between ischemic stroke classification and hemorrhagic complications.",
        "classification_and_nosology": "This scenario falls under iatrogenic complications of thrombolytic therapy in acute ischemic stroke. It is classified as a potential hemorrhagic complication secondary to reperfusion injury, a recognized adverse event following tPA administration.",
        "management_principles": "Based on the latest guidelines, after tPA administration, any clinical worsening should prompt an urgent CT scan. Once hemorrhage is confirmed, tPA must be stopped, and blood pressure should be managed carefully. Subsequent treatment may include reversal agents if available, neurosurgical consultation, and strict blood pressure control. In pregnant or lactating women, the benefits of rapid imaging and intervention outweigh potential risks; however, radiation exposure should be minimized with appropriate shielding if possible.",
        "option_analysis": "Option (c) advocating for an immediate CT scan is the correct initial action. Option (b) (stopping tPA) and option (a) (decreasing blood pressure) are both important but should only be executed after imaging confirmation to avoid inappropriate management that might worsen ischemic injury. The marked answer (D) is therefore incorrect as it does not address the immediate diagnostic need.",
        "clinical_pearls": "1. Neurological deterioration post-tPA mandates immediate non-contrast CT imaging to rule out hemorrhagic transformation. 2. Blood pressure and tPA management adjustments should be guided by imaging findings. 3. Timely diagnosis is crucial to modify therapy and prevent further complications.",
        "current_evidence": "Recent studies and updated guidelines from the AHA/ASA emphasize the importance of prompt imaging to guide management in post-thrombolysis patients. Emerging evidence supports that immediate CT scanning improves outcomes by confirming the diagnosis of hemorrhage and ensuring targeted subsequent interventions."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993091",
    "fields": {
      "question_number": "317",
      "question_text": "Patient with small left internal capsule infarction and right-sided weakness (not minor stroke) for 2 days found to have PFO (not mentioned if there was a specific feature of it) HTN with uncontrolled BP. What is the treatment?",
      "options": {},
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Aspirin is a well-established first-line antiplatelet agent for secondary prevention in ischemic stroke, particularly in strokes resulting from small vessel disease (lacunar strokes).",
        "pathophysiology": "Aspirin works by irreversibly inhibiting cyclooxygenase-1 (COX-1), leading to a reduction in thromboxane A2 synthesis, thereby preventing platelet aggregation that can cause further ischemic events.",
        "clinical_correlation": "In this patient, the small left internal capsule infarct with right-sided weakness is consistent with a lacunar stroke, typically attributable to small vessel disease exacerbated by uncontrolled hypertension. Aspirin reduces the risk of subsequent strokes by minimizing platelet aggregation.",
        "diagnostic_approach": "Differential diagnoses include cardioembolic stroke, large artery atherosclerosis, and small vessel (lacunar) infarcts. Clinical assessment and imaging help differentiate these entities; for example, cardioembolic strokes may require echocardiography while lacunar strokes correlate with risk factors like hypertension.",
        "classification_and_neurology": "Ischemic strokes are classified by the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. This patient's stroke fits the small vessel occlusion (lacunar) subtype given the small internal capsule infarct and risk factors. PFO-related strokes fall under 'stroke of undetermined etiology' or 'cryptogenic stroke' if no other cause is found, especially if paradoxical embolism is suspected. The presence of hypertension supports small vessel disease classification. The classification guides secondary prevention: antiplatelet therapy for small vessel and large artery strokes, anticoagulation for cardioembolic strokes. PFO closure is considered in select patients with cryptogenic stroke and high-risk PFO features. Nosology continues to evolve with better imaging and cardiac evaluation, but current consensus supports individualized treatment based on stroke subtype and risk factors.",
        "classification_and_nosology": "Lacunar strokes are classified under small vessel disease, a subtype of ischemic stroke. This classification guides the choice of antiplatelet therapy over anticoagulation.",
        "management_principles": "Guidelines for secondary prevention in lacunar stroke recommend starting with aspirin as a single antiplatelet agent along with aggressive risk factor control (hypertension, diabetes, hyperlipidemia). For patients who are pregnant or lactating, low-dose aspirin is generally considered safe after a risk\u2013benefit evaluation.",
        "option_analysis": "Option (a) Aspirin is correct as it is first-line for lacunar strokes. Option (b) Warfarin is not indicated since there is no evidence of cardioembolism. Option (c) PFO closure is reserved for cryptogenic strokes with high-risk PFO features absent in this case. Option (d) Dual antiplatelet therapy is typically used short-term in minor stroke or TIA scenarios, not for a non-minor lacunar stroke.",
        "clinical_pearls": "1. Lacunar strokes, typically related to small vessel disease, are best managed with single antiplatelet therapy. 2. Effective blood pressure control is critical in secondary prevention. 3. Aspirin\u2019s anti-thrombotic properties are key to reducing the recurrence of ischemic events.",
        "current_evidence": "Recent guidelines from AHA/ASA reinforce single antiplatelet therapy (aspirin) for secondary stroke prevention in small vessel disease. Studies continue to demonstrate that the benefits of aspirin outweigh the risks in lacunar strokes, with dual antiplatelet therapy reserved for specific short-term indications."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993092",
    "fields": {
      "question_number": "318",
      "question_text": "Case of stroke with intracranial stenosis what to do?",
      "options": {
        "A": "DAPT"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In cases of stroke associated with intracranial stenosis, dual antiplatelet therapy (DAPT) is a cornerstone strategy to prevent recurrent embolic events by targeting multiple platelet activation pathways.",
        "pathophysiology": "Intracranial atherosclerotic disease leads to stenosis, increasing the risk of cerebral ischemia due to reduced blood flow and embolic phenomena. DAPT (typically aspirin plus clopidogrel) reduces platelet aggregation and subsequent thrombus formation, lowering the risk of recurrent stroke.",
        "clinical_correlation": "Patients with intracranial stenosis have a high risk for recurrent ischemic events. Initiating DAPT in the immediate post-stroke period has been shown to reduce the incidence of further strokes, especially in the critical early phase.",
        "diagnostic_approach": "Intracranial stenosis is diagnosed with vascular imaging modalities such as CT angiography, MR angiography, or digital subtraction angiography. Differential diagnoses include extracranial carotid stenosis and cardioembolic sources, which are differentiated through comprehensive clinical and imaging evaluations.",
        "classification_and_neurology": "Intracranial arterial stenosis is classified based on the affected vessel and severity of luminal narrowing. The Warfarin-Aspirin Symptomatic Intracranial Disease (WASID) trial defined significant stenosis as \u226550% narrowing. It falls under the category of large-artery atherosclerosis in the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification of ischemic stroke etiologies. This classification aids in tailoring management and prognostication. Over time, classification systems have evolved to incorporate imaging modalities and stenosis quantification. Controversies remain regarding the best definitions for symptomatic versus asymptomatic stenosis and the optimal thresholds for intervention.",
        "classification_and_nosology": "Intracranial atherosclerotic disease is under the umbrella of large-artery cerebrovascular disease. It is often categorized based on the degree of stenosis (mild, moderate, severe), with management strategies tailored accordingly.",
        "management_principles": "Current guidelines recommend starting DAPT (aspirin and clopidogrel) for patients with symptomatic intracranial stenosis for about 90 days, in conjunction with aggressive risk factor management including statins and blood pressure control. For pregnant or lactating patients, low-dose aspirin is often considered acceptable; however, clopidogrel must be used with caution and only if clearly indicated.",
        "option_analysis": "Option (A) DAPT is correct as it aligns with current best practices for reducing recurrent stroke risk in patients with intracranial stenosis. Other options, not provided here, might include single antiplatelet therapy or anticoagulation, which are less effective in this context.",
        "clinical_pearls": "1. DAPT is most beneficial in the first 90 days following a stroke attributed to intracranial stenosis. 2. Aggressive risk factor modification is essential for long-term stroke prevention. 3. Imaging confirmation of stenosis is crucial for guiding therapy.",
        "current_evidence": "Recent trials such as SAMMPRIS have supported the use of DAPT in patients with symptomatic intracranial stenosis. Updated guidelines continue to emphasize a combination of dual antiplatelet therapy and intensive medical management to decrease the risk of recurrent events."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993093",
    "fields": {
      "question_number": "319",
      "question_text": "Patient has stroke with slurred speech you referred him to speech therapist and rehab service, this is considered as:",
      "options": {},
      "correct_answer": "c",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Prevention strategies in stroke are classified into three categories: primary (preventing the first event), secondary (preventing recurrence), and tertiary (minimizing disability and enhancing recovery post-event). Referral to rehabilitation services falls under tertiary prevention.",
        "pathophysiology": "Tertiary prevention focuses on improving functional outcomes and reducing long-term disability through rehabilitative measures. Neuroplasticity plays a key role as targeted therapies help the brain reorganize in response to injury.",
        "clinical_correlation": "For a patient with slurred speech post-stroke, referral to a speech therapist and rehabilitation services is aimed at reducing impairments and improving quality of life. This intervention targets restoration of lost function and compensation strategies.",
        "diagnostic_approach": "The clinical scenario clearly differentiates from primary and secondary prevention. Primary prevention involves measures before any stroke occurs, and secondary prevention focuses on preventing additional strokes. In contrast, tertiary prevention addresses the consequences of a stroke.",
        "classification_and_neurology": "Stroke prevention is classified within the broader framework of preventive medicine and cerebrovascular disease management. The three-tier classification\u2014primary, secondary, and tertiary prevention\u2014is universally accepted and endorsed by organizations such as the American Heart Association (AHA) and World Health Organization (WHO). Primary prevention involves risk factor modification in asymptomatic individuals; secondary prevention targets patients with established cerebrovascular disease to prevent recurrence; tertiary prevention encompasses rehabilitation and disability limitation post-stroke. This classification aids in structuring clinical pathways and research. While some literature discusses quaternary prevention (avoiding overmedicalization), the three-level model remains the standard in stroke care.",
        "classification_and_nosology": "Tertiary prevention includes all rehabilitative strategies aimed at reducing disability after a disease event. Post-stroke rehabilitation, including speech therapy, is a central part of tertiary preventive measures.",
        "management_principles": "Current guidelines support early and comprehensive rehabilitation for stroke survivors. A multi-disciplinary approach including physical, occupational, and speech therapy is recommended. For pregnant or lactating patients, rehabilitative programs should be adapted to ensure maternal and fetal safety while maximizing recovery.",
        "option_analysis": "Option (a) Primary prevention is incorrect as it applies to preventing the first stroke. Option (b) Secondary prevention targets preventing recurrence rather than rehabilitating deficits. Option (c) Tertiary prevention is correct because it involves addressing the impairments after the stroke. Option (d) is not applicable.",
        "clinical_pearls": "1. Early rehabilitation is essential in improving post-stroke outcomes. 2. Tertiary prevention minimizes long\u2010term disability and enhances functional recovery. 3. Multi-disciplinary care is key in comprehensive stroke recovery.",
        "current_evidence": "Recent research highlights the effectiveness of early, intensive rehabilitation in promoting neuroplasticity and improving functional outcomes. Updated guidelines continue to recommend structured rehabilitation programs as an integral part of post-stroke care."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993094",
    "fields": {
      "question_number": "320",
      "question_text": "Case of press female with high BP 180/?? Presented with seizure and confusion with MRI showing bilateral occipital cortical hyperintensity dx",
      "options": {
        "A": "(PRES) is correct because the clinical presentation of severe hypertension, seizures, confusion, and the MRI findings of bilateral occipital hyperintensities are classic for PRES. Other options like ischemic stroke, infectious encephalitis, or demyelinating disease would not typically present with these bilateral, symmetrical imaging features combined with the acute hypertensive setting."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Posterior reversible encephalopathy syndrome (PRES) is an acute neurological disorder characterized by vasogenic edema predominantly affecting the posterior cerebral regions. It typically occurs in the setting of abrupt blood pressure elevations, eclampsia, or exposure to certain immunosuppressive drugs.",
        "pathophysiology": "PRES results from a breakdown of cerebral autoregulation. The sudden rise in blood pressure overwhelms the vessels' ability to constrict, leading to hyperperfusion and extravasation of fluid into the interstitial space, primarily in the parieto-occipital regions. This manifests on MRI as symmetric hyperintensities on T2/FLAIR sequences. In cases of pregnancy such as pre-eclampsia/eclampsia, similar mechanisms apply, further emphasizing the syndrome\u2019s ties to hypertensive emergencies.",
        "clinical_correlation": "Clinically, patients present with headache, seizures, visual disturbances, confusion, and sometimes focal neurological deficits. The classic neuroimaging finding is bilateral, predominantly occipital cortical hyperintensities corresponding to vasogenic edema. These features help distinguish PRES from conditions like ischemic stroke or encephalitis.",
        "diagnostic_approach": "The diagnosis is primarily based on clinical history (e.g., severe hypertension, exposure to causative agents) combined with MRI findings. Differential diagnoses include ischemic stroke (typically focal and with diffusion restriction), infectious encephalitis (often accompanied by fever and CSF abnormalities), and demyelinating disorders (which have a subacute course with different lesion patterns).",
        "classification_and_neurology": "PRES is classified as a reversible encephalopathy syndrome within the broader category of cerebrovascular and neurovascular disorders. It is not a distinct disease entity but rather a syndrome resulting from various etiologies that cause cerebral autoregulatory failure and endothelial dysfunction. Classification systems categorize PRES based on clinical context (e.g., hypertensive crisis, eclampsia, immunosuppressive therapy), radiological patterns (typical posterior predominant vs. atypical involving frontal lobes, basal ganglia, brainstem), and severity. The syndrome overlaps with hypertensive encephalopathy but is distinguished by imaging features and reversibility. Nosologically, PRES is considered part of the spectrum of reversible cerebral edema syndromes. Recent consensus emphasizes the importance of recognizing PRES as a clinico-radiological syndrome rather than a diagnosis of exclusion. Controversies remain regarding the exact pathophysiological mechanisms and the relationship between PRES and related conditions such as reversible cerebral vasoconstriction syndrome (RCVS).",
        "classification_and_nosology": "PRES is classified as an acute neurotoxic syndrome that can be secondary to hypertensive crises, eclampsia, renal failure, or immunosuppressive treatment. It is sometimes referred to as reversible posterior leukoencephalopathy syndrome.",
        "management_principles": "First-line management centers on prompt blood pressure lowering with agents sensitive to patient context. In pregnant or lactating women, antihypertensives like labetalol, hydralazine, and nifedipine are preferred due to their safety profiles. Seizure management with antiepileptics (e.g., levetiracetam) may be necessary. Secondary management includes treatment of the precipitating cause (e.g., eclampsia or renal dysfunction).",
        "option_analysis": "Option A (PRES) is correct because the clinical presentation of severe hypertension, seizures, confusion, and the MRI findings of bilateral occipital hyperintensities are classic for PRES. Other options like ischemic stroke, infectious encephalitis, or demyelinating disease would not typically present with these bilateral, symmetrical imaging features combined with the acute hypertensive setting.",
        "clinical_pearls": "1. PRES is often reversible if blood pressure is promptly controlled. 2. Visual disturbances are common due to the posterior cerebral involvement. 3. Always consider PRES in hypertensive emergencies, especially in obstetric patients.",
        "current_evidence": "Recent studies and guidelines continue to emphasize early diagnosis with MRI and rapid blood pressure management to prevent permanent deficits. Ongoing research into the pathophysiology of blood-brain barrier disruption in PRES is enhancing therapeutic strategies."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993302",
    "fields": {
      "question_number": "331",
      "question_text": "Picture of skin rash (Angiokeratomas) with history of father death due to a stroke and asked about the gene",
      "options": {
        "A": "Alpha-galactosidase A"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X-linked lysosomal storage disorder caused by a deficiency of the enzyme alpha-galactosidase A. This enzymatic defect leads to the accumulation of glycosphingolipids, particularly globotriaosylceramide (Gb3), in various tissues.",
        "pathophysiology": "The deficiency in alpha-galactosidase A results in progressive accumulation of Gb3 in the vascular endothelium, kidneys, heart, and skin. The deposition in dermal capillaries causes the formation of angiokeratomas, while accumulation in cerebral vasculature increases the risk of early stroke.",
        "clinical_correlation": "Skin findings such as angiokeratomas\u2014small, dark red to black papules\u2014are hallmarks of Fabry disease. Additionally, patients can present with acroparesthesias, hypohidrosis, corneal verticillata, and an increased risk of cardiovascular and cerebrovascular events. A family history of early stroke further supports the diagnosis.",
        "diagnostic_approach": "The diagnosis is confirmed by measuring alpha-galactosidase A enzyme activity and genetic testing for mutations in the GLA gene. Differential diagnoses might include other metabolic or vascular skin disorders, but the systemic involvement and enzyme assay help direct the diagnosis.",
        "classification_and_neurology": "Fabry disease belongs to the group of lysosomal storage disorders (LSDs), specifically classified under sphingolipidoses due to defective glycosphingolipid metabolism. It is an X-linked inherited metabolic disorder caused by mutations in the GLA gene. The disease is part of the broader category of inherited metabolic and neurogenetic disorders that cause systemic and neurological symptoms. Historically, LSDs were classified based on the accumulated substrate and enzyme deficiency; modern classifications incorporate molecular genetics. Fabry disease is distinguished from other LSDs by its unique enzyme deficiency and clinical spectrum. There is consensus on its classification, but phenotypic variability, especially in heterozygous females, poses diagnostic challenges. It is also grouped under inherited causes of stroke and small vessel disease in neurology.",
        "classification_and_nosology": "Fabry disease is classified as a lysosomal storage disorder. It follows an X-linked inheritance pattern, which explains the variable penetrance and presentation in female carriers compared to affected males.",
        "management_principles": "First-line treatment involves enzyme replacement therapy (ERT) to reduce Gb3 accumulation. Adjunctive therapies include pain management and interventions for renal or cardiac complications. In pregnancy and lactation, while data are limited, ERT has been used with caution under close specialist supervision, ensuring minimal risk to both mother and fetus.",
        "option_analysis": "Option A (Alpha-galactosidase A) is correct as it is the gene responsible for the production of the enzyme deficient in Fabry disease. Other options would not correlate with the genetic defect seen in this condition.",
        "clinical_pearls": "1. Angiokeratomas are an early and key diagnostic clue in Fabry disease. 2. Even heterozygous females can exhibit symptoms due to X-linked inheritance variability. 3. Early initiation of ERT can slow the progression of organ damage.",
        "current_evidence": "Recent guidelines advocate for early diagnosis with enzyme assays and genetic testing. Advances in treatment, including pharmacological chaperones and gene therapy, are under investigation, promising improved outcomes in the future."
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
