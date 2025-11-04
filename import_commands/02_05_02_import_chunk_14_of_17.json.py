
# Import batch 2 of 3 from chunk_14_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993291",
    "fields": {
      "question_number": "130",
      "question_text": "Case of malignant MCA and presented after 24 hours with midline shift what is the most important thing to do?",
      "options": {
        "A": "decompressive cranectomy",
        "B": "admission to stroke unit"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Malignant middle cerebral artery (MCA) infarction is characterized by a large territory stroke that leads to significant cerebral edema, increased intracranial pressure, and often, midline brain shift. Timely surgical intervention can be life-saving in these cases.",
        "pathophysiology": "Massive infarction in the MCA territory leads to cytotoxic and vasogenic edema. As the swelling increases, intracranial pressure rises, potentially resulting in brain herniation. Decompressive hemicraniectomy (or craniectomy) is performed to physically allow the swollen brain tissue to expand, thereby reducing intracranial pressure and preventing fatal herniation.",
        "clinical_correlation": "Patients with malignant MCA infarction typically have rapidly deteriorating neurological function, and imaging may reveal a large infarct with significant edema and midline shift. If not promptly managed, these patients are at high risk for herniation and death.",
        "diagnostic_approach": "Diagnosis is based on clinical presentation and neuroimaging (CT/MRI) showing extensive infarction involving the MCA territory, significant cerebral edema, and midline shift. Differential diagnoses include large hemorrhagic strokes and other causes of cerebral edema, but the context of infarction guides the diagnosis.",
        "classification_and_neurology": "Malignant MCA infarction is classified as a subtype of ischemic stroke under the cerebrovascular disease taxonomy. It falls within the large vessel occlusion strokes affecting the anterior circulation. According to TOAST classification, it is an atherothrombotic or cardioembolic stroke depending on etiology. The term 'malignant' refers to the clinical syndrome of massive infarction with life-threatening cerebral edema rather than a distinct pathological entity. Stroke classifications have evolved to emphasize vessel involvement, infarct size, and clinical severity, with malignant MCA infarction representing the most severe clinical phenotype of MCA territory strokes. This classification informs prognosis and management strategies, differentiating it from smaller, non-malignant MCA infarcts.",
        "classification_and_nosology": "Malignant MCA infarction is classified as a severe form of ischemic stroke, distinguished by the extent of the infarct and the rapid progression to life-threatening cerebral edema. It is generally considered part of the spectrum of large territory strokes.",
        "management_principles": "The mainstay of treatment is decompressive hemicraniectomy. First-line management involves early surgical intervention, ideally within 48 hours of stroke onset, as studies have demonstrated improved survival and functional outcomes. Supportive care in a stroke unit is also essential, but in the presence of significant midline shift and malignant edema, prompt decompressive surgery takes precedence. In pregnancy and lactation, decompressive craniectomy is similarly indicated when life-threatening cerebral edema is present; however, multidisciplinary collaboration including obstetrics is needed to balance maternal and fetal risks.",
        "option_analysis": "Option A (Decompressive craniectomy) is the correct and most urgent intervention in malignant MCA syndrome with midline shift. Option B (Admission to stroke unit) is important for supportive care, but it does not address the life-threatening increase in intracranial pressure. In this emergency setting, surgical decompression is critical.",
        "clinical_pearls": "1) Decompressive surgery should be performed within 48 hours of stroke onset for optimal outcomes in malignant MCA infarction. 2) Rapid identification of cerebral edema and midline shift on imaging is crucial. 3) Multidisciplinary care is essential, especially in special populations such as pregnant patients.",
        "current_evidence": "Recent randomized controlled trials and meta-analyses support early decompressive hemicraniectomy in reducing mortality and improving outcomes in malignant MCA infarction. Guidelines continue to endorse surgical decompression in patients with significant midline shift, even when presentation is beyond the very early hours, provided the window (usually up to 48 hours) is respected."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993400",
    "fields": {
      "question_number": "429",
      "question_text": "SCA causes?",
      "options": {
        "A": "Ipsilateral hornors/ptosis",
        "B": "Ipsilateral fourth nerve palsy"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "The Superior Cerebellar Artery (SCA) supplies portions of the superior cerebellum and parts of the rostral brainstem. Infarction or pathology in this vascular territory can affect both cerebellar structures and adjacent midbrain areas including cranial nerve nuclei or their fiber tracts.",
        "pathophysiology": "Ischemia in the SCA territory may extend to parts of the midbrain where the trochlear nerve (cranial nerve IV) courses near the dorsal aspect. Disruption of blood flow can lead to infarction of these areas and result in an ipsilateral fourth nerve palsy. In contrast, symptoms such as Horner\u2019s syndrome (ptosis with miosis) are more characteristic of lesions affecting the lateral medulla (PICA territory) or sympathetic pathways.",
        "clinical_correlation": "Patients with SCA involvement typically present with cerebellar signs like ataxia and dysmetria. When the infarct affects adjacent midbrain regions, additional findings like an ipsilateral fourth nerve palsy (leading to vertical diplopia or difficulty with downward gaze) can occur.",
        "diagnostic_approach": "Diagnosis is established with neuroimaging such as MRI with diffusion-weighted imaging and MR angiography to delineate the vascular territory. Differential diagnoses include lateral medullary syndrome (which may present with ipsilateral Horner\u2019s syndrome), and other brainstem or cerebellar strokes. Careful evaluation of clinical signs coupled with imaging findings helps differentiate these entities.",
        "classification_and_neurology": "SCAs belong to the broader category of inherited ataxias, classified based on genetic mutations and clinical features. The most widely accepted classification is by genetic subtype (e.g., SCA1, SCA2, SCA3, etc.), each caused by different gene mutations, mostly trinucleotide repeat expansions. This genetic classification correlates variably with clinical phenotypes and neuropathological findings. SCAs are part of the spinocerebellar degenerations family, which also includes autosomal recessive ataxias and other inherited cerebellar disorders. Recent consensus emphasizes genotype-driven classification due to advances in molecular diagnostics. Controversies remain regarding phenotype overlap and variable expressivity among subtypes, complicating clinical diagnosis without genetic confirmation.",
        "classification_and_nosology": "SCA involvement is usually categorized under posterior circulation strokes. It is part of the broader group of cerebellar and brainstem infarctions, distinct from anterior circulation strokes.",
        "management_principles": "Acute management follows ischemic stroke guidelines including rapid neuroimaging, possible thrombolysis if within the therapeutic window, and secondary prevention measures (antiplatelet agents, control of risk factors). If there is extension into brainstem regions, supportive care and monitoring in a stroke unit are essential. In pregnant and lactating patients, decisions regarding thrombolysis require balancing maternal and fetal risks, but protocols exist to guide safe management.",
        "option_analysis": "Option A (Ipsilateral Horner\u2019s syndrome/ptosis) is more typical of lateral medullary (PICA) infarcts affecting sympathetic fibers. Option B (Ipsilateral fourth nerve palsy) reflects involvement of midbrain areas near the SCA territory, making it the more appropriate answer in this context.",
        "clinical_pearls": "1. SCA infarcts classically present with cerebellar ataxia and may include ocular motor deficits when adjacent midbrain structures are involved. 2. Horner\u2019s syndrome is usually seen with lesions in the posterior inferior cerebellar artery (PICA) distribution. 3. Detailed neuroimaging is essential to appropriately localize posterior circulation strokes.",
        "current_evidence": "Recent literature emphasizes the importance of early multimodal imaging in posterior circulation strokes to direct acute management. Guidelines continue to support thrombolytic therapy following strict criteria, and emerging evidence highlights the role of endovascular techniques in select cases."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993279",
    "fields": {
      "question_number": "61",
      "question_text": "Scenario about patient with my Moyamoya syndrome and history of ischemic stroke, what is the best treatment to prevent future stroke?",
      "options": {
        "A": "Chronic transfusion",
        "B": "Aspirin and clopidogrel",
        "C": "?",
        "D": "?"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Moyamoya syndrome is characterized by progressive stenosis or occlusion of the terminal portions of the internal carotid arteries, with the formation of a network of fragile collateral vessels. This chronic process predisposes patients to ischemic strokes and, less commonly, hemorrhagic events.",
        "pathophysiology": "The progressive narrowing of major intracranial arteries leads to reduced cerebral perfusion. The compensatory development of collateral vessels (which appear as a \u201cpuff of smoke\u201d on angiography) is often insufficient to meet metabolic demands. This mismatch predisposes patients to recurrent ischemic events. The definitive treatment addresses the hemodynamic compromise by surgically improving cerebral blood flow through revascularization.",
        "clinical_correlation": "Patients with Moyamoya syndrome often present with transient ischemic attacks or strokes, and may have a history of prior ischemic events. Ischemic symptoms, such as weakness or speech difficulties, are common. The risk of future stroke remains high without definitive intervention.",
        "diagnostic_approach": "Diagnosis is confirmed with imaging such as MRI/MRA or conventional angiography, which reveals the characteristic vasculature. Differential diagnoses include other causes of intracranial arterial stenosis (e.g., atherosclerosis, vasculitis) and genetic conditions that predispose to stroke. Characteristic findings on angiography help differentiate Moyamoya from these other conditions.",
        "classification_and_neurology": "Moyamoya syndrome is classified within the broader category of cerebrovascular occlusive diseases. It is distinguished from Moyamoya disease, which is idiopathic, by the presence of associated conditions (e.g., sickle cell disease, neurofibromatosis). The classification follows the guidelines from the Research Committee on Moyamoya Disease (Japan) and international consensus, which separate idiopathic from secondary Moyamoya. The disease is also categorized by angiographic staging (Suzuki stages I-VI) reflecting progressive arterial occlusion and collateral development. This nosological framework aids in prognostication and treatment planning. Moyamoya syndrome is part of the ischemic stroke etiologies under large-vessel occlusive diseases with unique collateral pathophysiology. Controversies remain regarding the classification of atypical presentations and the overlap with other vasculopathies.",
        "classification_and_nosology": "Moyamoya disease is idiopathic, while Moyamoya syndrome refers to similar vascular changes associated with other diseases (e.g., neurofibromatosis, Down syndrome, or post-radiation vasculopathy). Both are classified as forms of chronic cerebrovascular occlusive disease affecting the anterior circulation.",
        "management_principles": "The primary treatment to prevent future stroke in Moyamoya is surgical revascularization. First-line surgical options include direct bypass (e.g., superficial temporal artery to middle cerebral artery [STA-MCA] bypass) or indirect revascularization procedures (e.g., encephaloduroarteriosynangiosis [EDAS]). Medical management with antiplatelets may be used as an adjunct or bridge while awaiting surgery, but is not sufficient on its own. In patients with sickle cell disease\u2013associated Moyamoya, chronic transfusion therapy may be considered, but this is not typical for non\u2013sickle cell Moyamoya. In pregnancy and lactation, surgical procedures are approached with caution; if indicated, a multidisciplinary team should evaluate the timing and risk, with medical therapy (including low-dose aspirin) possibly used during gestation under close monitoring.",
        "option_analysis": "Option A (Chronic transfusion) is primarily used in sickle cell disease\u2013associated stroke prevention, not in primary Moyamoya syndrome. Option B (Aspirin and clopidogrel) suggests dual antiplatelet therapy, which is not the standard definitive treatment for Moyamoya. Option C, presumed to stand for surgical revascularization, is the best treatment to prevent future strokes in this context.",
        "clinical_pearls": "1. Surgical revascularization is the treatment of choice for prevention of recurrent stroke in Moyamoya syndrome. 2. Moyamoya should be suspected in patients (especially in children and young adults) with recurrent ischemic events and characteristic angiographic findings. 3. Comprehensive management may require coordination across neurology, neurosurgery, and, when relevant, hematology (in sickle cell disease).",
        "current_evidence": "Recent guidelines and studies from stroke and neurosurgical societies continue to support early revascularization in symptomatic Moyamoya to improve long\u2010term outcomes. Advances in surgical techniques and perioperative care have further optimized outcomes in both pediatric and adult populations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993280",
    "fields": {
      "question_number": "62",
      "question_text": "Patient on Warfarin developed weakness, CT brain attached showed intracranial bleeding with fluid level feature, what is the cause?",
      "options": {
        "A": "Coagulopathy",
        "B": "?",
        "C": "?",
        "D": "?"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "Patients on warfarin are at risk for hemorrhagic complications due to its anticoagulant effect. Warfarin interferes with the synthesis of vitamin K dependent clotting factors, predisposing patients to bleeding.",
        "pathophysiology": "Warfarin-induced coagulopathy leads to impaired clot formation. In the event of intracranial bleeding, the lack of effective coagulation can result in blood layering, creating a fluid\u2013fluid level on CT imaging. The fluid level signifies that the blood components have separated due to inadequate clot stabilization.",
        "clinical_correlation": "A patient on warfarin who develops sudden weakness and is found to have intracranial bleeding on CT should raise suspicion for a coagulopathy-induced hemorrhage. The presence of a fluid level on imaging supports the diagnosis of a bleeding diathesis rather than a typical hemorrhagic stroke resulting solely from hypertension.",
        "diagnostic_approach": "CT imaging is the first modality to assess intracranial hemorrhage. Laboratory tests including PT/INR are critical to evaluate the degree of anticoagulation. Differential diagnoses include hypertensive hemorrhage and hemorrhagic conversion of an ischemic stroke; however, the fluid level is particularly suggestive of a coagulopathic bleed as seen with warfarin over-anticoagulation.",
        "classification_and_neurology": "Intracranial hemorrhages are classified based on anatomical location: intracerebral (parenchymal), subarachnoid, subdural, and epidural hemorrhages. Warfarin-associated hemorrhages fall under secondary intracerebral hemorrhages due to coagulopathy. According to the American Heart Association/American Stroke Association (AHA/ASA) guidelines, anticoagulant-related ICH is a distinct subtype with unique management considerations. The classification also considers etiology: hypertensive, amyloid angiopathy, vascular malformations, trauma, and coagulopathy-induced. This nosological framework aids in diagnosis and treatment planning. Over time, classification systems have evolved to emphasize etiology and risk factors, reflecting advances in imaging and molecular understanding. Currently, anticoagulant-associated ICH is recognized as a high-risk hemorrhage subtype requiring tailored reversal strategies.",
        "classification_and_nosology": "Intracranial hemorrhage secondary to warfarin use falls under medication-induced coagulopathy. It is managed separately from spontaneous hypertensive hemorrhages or hemorrhagic strokes of other etiologies.",
        "management_principles": "Management involves rapid reversal of warfarin\u2019s effects using vitamin K and prothrombin complex concentrates (or fresh frozen plasma, if PCC is unavailable). Blood pressure control and supportive care are also essential. In pregnancy and lactation, reversal agents must be used cautiously; for example, vitamin K is generally safe, but FFP and PCC should be administered with considerations for both maternal and fetal health. Monitoring of coagulation parameters following reversal is critical.",
        "option_analysis": "Option A (Coagulopathy) is correct because warfarin causes a bleeding diathesis leading to intracranial hemorrhage with characteristic imaging findings. The other options (B, C, D) are either not provided or are less likely to explain the CT fluid level seen in this scenario.",
        "clinical_pearls": "1. Warfarin\u2019s anticoagulant effect increases the risk of intracranial hemorrhage, often with a characteristic fluid\u2013fluid level on CT due to poor clot formation. 2. Always verify coagulation parameters (INR/PT) in patients on warfarin presenting with new neurological symptoms. 3. Rapid reversal of anticoagulation is crucial to minimize further bleeding complications.",
        "current_evidence": "Recent evidence emphasizes the use of PCC for rapid warfarin reversal, with updated guidelines advocating for tailored reversal strategies based on the severity of bleeding and INR levels. Studies continue to refine the risk/benefit profiles of various reversal agents, especially in patients with concurrent comorbidities."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993281",
    "fields": {
      "question_number": "63",
      "question_text": "Patient presented with right face, arm and leg weakness with mild articulation difficulties, where is the localization of his lesion?",
      "options": {
        "A": "Internal capsule",
        "B": "Midbrain"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "The internal capsule, particularly its posterior limb, is a compact area where corticospinal and corticobulbar fibers converge. A lesion here can produce a contralateral, often complete, motor deficit affecting the face, arm, and leg.",
        "pathophysiology": "A lacunar infarct or other small vessel occlusion in the internal capsule damages the densely packed motor fibers, leading to pure motor hemiparesis. The involvement of corticobulbar fibers can also result in mild dysarthria (articulation difficulties).",
        "clinical_correlation": "Patients presenting with weakness affecting the contralateral face, arm, and leg, along with slight speech articulation problems, are classic for an internal capsule lesion. There is typically no significant sensory deficit, which helps differentiate it from strokes involving other areas.",
        "diagnostic_approach": "Magnetic resonance imaging (MRI) and CT scans are used to localize the infarct. Differential diagnoses include middle cerebral artery (MCA) strokes, which often produce additional cortical signs, and brainstem strokes, which can also produce lower cranial nerve involvement. The pure motor pattern favors a lacunar infarct in the internal capsule.",
        "classification_and_neurology": "This clinical syndrome falls under the classification of **lacunar strokes**, a subtype of ischemic stroke affecting small penetrating arteries supplying deep brain structures like the internal capsule. According to the TOAST classification system (Trial of Org 10172 in Acute Stroke Treatment), lacunar strokes are categorized as small vessel occlusion strokes.   The internal capsule lesion is a classic example of a lacunar infarct causing a pure motor stroke. The midbrain lesion would be classified under large vessel or brainstem strokes depending on etiology.   Over time, stroke classification has evolved from purely clinical syndromes to incorporate imaging and etiological criteria, improving diagnostic accuracy and management. The current consensus emphasizes integrating clinical, radiological, and vascular studies for precise nosology.",
        "classification_and_nosology": "This type of stroke is classified under lacunar syndromes, a subgroup of small vessel disease strokes. It is often associated with chronic hypertension and diabetes.",
        "management_principles": "Acute management involves standard ischemic stroke protocols, including consideration of thrombolytic therapy if within the window period and secondary prevention with antiplatelet agents and risk factor modification. In pregnant or lactating patients, management of stroke follows established protocols with particular attention to medication safety (e.g., aspirin is generally considered safe in low doses; thrombolysis can be considered if benefits outweigh risks). Long-term management focuses on controlling vascular risk factors to prevent recurrence.",
        "option_analysis": "Option A (Internal capsule) is correct because it best accounts for the presentation of pure motor deficits involving the face, arm, and leg with mild dysarthria. Option B (Midbrain) is less likely because midbrain lesions often involve additional cranial nerve deficits or altered consciousness, which are not described here.",
        "clinical_pearls": "1. The classic \u201cpure motor stroke\u201d syndrome is most commonly due to a lacunar infarct in the posterior limb of the internal capsule. 2. Small, deep infarcts often occur in patients with chronic vascular risk factors like hypertension and diabetes. 3. Rapid imaging and risk factor control are key to optimizing outcomes in lacunar strokes.",
        "current_evidence": "Current stroke guidelines emphasize early identification and management of lacunar strokes, with studies supporting intensive risk factor modification to reduce the risk of recurrent events. Research into advanced imaging techniques continues to improve our ability to localize small deep infarcts."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993282",
    "fields": {
      "question_number": "64",
      "question_text": "Patient presented with weakness, MRI brain showed ischemic infarction in superior cerebellar artery, what would be expected to be seen?",
      "options": {
        "A": "Ipsilateral Horner/ ptosis",
        "B": "Ipsilateral fourth nerve palsy",
        "C": "?",
        "D": "?"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "The superior cerebellar artery (SCA) supplies the superior aspect of the cerebellum, which is central to coordination, balance, and fine motor control. Infarction in this vascular territory typically produces cerebellar signs, such as ipsilateral limb ataxia, dysmetria, and dysdiadochokinesia. The core concept is localizing neurological deficits based on vascular territories within the posterior fossa.",
        "pathophysiology": "An ischemic stroke in the SCA territory leads to infarction of cerebellar tissue. This results in edema and loss of function in the regions controlling coordination. Although the SCA may supply parts of the cerebellar peduncles and, in some cases, adjacent regions of the midbrain, isolated involvement of cranial nerve IV (which governs the superior oblique muscle and mediates downward gaze) is much less typical. Rather, the damage mainly disrupts cerebellar circuits.",
        "clinical_correlation": "Patients with SCA infarcts commonly present with ipsilateral cerebellar signs including limb ataxia and dysmetria. They may have disturbances in balance and coordination, which can manifest as a wide-based gait, tremor, or difficulty with rapid alternating movements. A fourth nerve palsy, which would produce vertical diplopia and difficulty with downward gaze, is more characteristic of a specific midbrain lesion rather than a pure cerebellar (SCA) stroke.",
        "diagnostic_approach": "When evaluating a patient with suspected posterior circulation stroke, the differential diagnoses include infarcts in the PICA territory (lateral medullary syndrome with features such as ipsilateral Horner syndrome and loss of pain and temperature on the face), AICA infarcts (which can involve facial nerve deficits and hearing loss), and midbrain strokes. Neuroimaging (MRI) is key to localizing the vascular territory and differentiating between these entities.",
        "classification_and_neurology": "SCA infarction is classified under ischemic strokes within the posterior circulation stroke category. The TOAST classification system categorizes strokes based on etiology (large artery atherosclerosis, cardioembolism, small vessel occlusion, etc.), with SCA strokes often related to large artery atherosclerosis or embolism. Anatomically, it belongs to the vertebrobasilar stroke subgroup, distinct from anterior circulation strokes. The classification emphasizes vascular territory localization to guide diagnosis and management. Over time, neuroimaging and clinical criteria have refined stroke classification, integrating vascular territory, etiology, and clinical syndrome. Some controversies exist regarding overlap syndromes and the precise clinical-anatomical correlations, but consensus supports vascular territory-based classification for guiding therapy.",
        "classification_and_nosology": "This scenario falls under ischemic cerebrovascular disease, specifically a cerebellar infarction in the SCA territory. Cerebellar strokes are categorized within the spectrum of posterior circulation strokes.",
        "management_principles": "Standard management of ischemic stroke includes prompt evaluation for thrombolytic eligibility and secondary prevention measures (antiplatelet therapy, risk factor management, and rehabilitation). In cerebellar strokes, supportive care is crucial due to the risk of edema and compression of adjacent structures. Although decompressive strategies may be needed in large infarcts, in SCA strokes the focus is usually on symptomatic and rehabilitative management. In pregnant or lactating patients, thrombolytic and antithrombotic therapies are administered following established guidelines (with careful risk\u2010benefit analysis) and imaging is used to confirm infarct location.",
        "option_analysis": "Option A (Ipsilateral Horner/ptosis) is more indicative of a lateral medullary (PICA) infarct, involving disruption of the descending sympathetic fibers. Option B (Ipsilateral fourth nerve palsy) points toward a midbrain lesion affecting the trochlear nerve. Neither of these options captures the classic presentation of an SCA infarct. The expected clinical finding would be cerebellar dysfunction, such as ipsilateral limb ataxia or other markers of cerebellar involvement, which we assume corresponds to option C (though not explicitly listed).",
        "clinical_pearls": "1. SCA strokes typically produce ipsilateral cerebellar signs like ataxia and dysmetria. 2. Isolated cranial nerve deficits (such as a fourth nerve palsy) are usually linked to midbrain or other brainstem lesions rather than pure cerebellar infarcts.",
        "current_evidence": "Recent stroke management guidelines emphasize early recognition and localization of posterior circulation strokes using MRI. Studies consistently show that cerebellar infarcts in the SCA territory manifest with coordination deficits rather than isolated ocular motor nerve palsies. There remains active research in optimizing early rehabilitative interventions for cerebellar strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993283",
    "fields": {
      "question_number": "65",
      "question_text": "Elderly patient brought to emergency by his family who saw him unresponsive in bed, last time seen well was 1 day ago, CT brain attached showing large infarction area (Right MCA) with midline shift, what is the most important thing to do?",
      "options": {
        "A": "decompressive craniectomy",
        "B": "admission to stroke unit",
        "C": "?",
        "D": "?"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "The superior cerebellar artery (SCA) supplies the superior aspect of the cerebellum, which is central to coordination, balance, and fine motor control. Infarction in this vascular territory typically produces cerebellar signs, such as ipsilateral limb ataxia, dysmetria, and dysdiadochokinesia. The core concept is localizing neurological deficits based on vascular territories within the posterior fossa.",
        "pathophysiology": "An ischemic stroke in the SCA territory leads to infarction of cerebellar tissue. This results in edema and loss of function in the regions controlling coordination. Although the SCA may supply parts of the cerebellar peduncles and, in some cases, adjacent regions of the midbrain, isolated involvement of cranial nerve IV (which governs the superior oblique muscle and mediates downward gaze) is much less typical. Rather, the damage mainly disrupts cerebellar circuits.",
        "clinical_correlation": "Patients with SCA infarcts commonly present with ipsilateral cerebellar signs including limb ataxia and dysmetria. They may have disturbances in balance and coordination, which can manifest as a wide-based gait, tremor, or difficulty with rapid alternating movements. A fourth nerve palsy, which would produce vertical diplopia and difficulty with downward gaze, is more characteristic of a specific midbrain lesion rather than a pure cerebellar (SCA) stroke.",
        "diagnostic_approach": "When evaluating a patient with suspected posterior circulation stroke, the differential diagnoses include infarcts in the PICA territory (lateral medullary syndrome with features such as ipsilateral Horner syndrome and loss of pain and temperature on the face), AICA infarcts (which can involve facial nerve deficits and hearing loss), and midbrain strokes. Neuroimaging (MRI) is key to localizing the vascular territory and differentiating between these entities.",
        "classification_and_neurology": "Large MCA infarctions fall under the classification of ischemic strokes in the cerebrovascular disease taxonomy. According to the TOAST classification, these are usually due to large artery atherosclerosis or cardioembolism. The concept of 'malignant MCA infarction' describes large territory infarcts with significant edema causing mass effect.  This subtype is recognized as a distinct clinical entity due to its high morbidity and mortality. The classification emphasizes the importance of infarct size and secondary complications such as edema. Over time, the recognition of malignant MCA infarction has led to specific therapeutic approaches including decompressive surgery.",
        "classification_and_nosology": "This scenario falls under ischemic cerebrovascular disease, specifically a cerebellar infarction in the SCA territory. Cerebellar strokes are categorized within the spectrum of posterior circulation strokes.",
        "management_principles": "Standard management of ischemic stroke includes prompt evaluation for thrombolytic eligibility and secondary prevention measures (antiplatelet therapy, risk factor management, and rehabilitation). In cerebellar strokes, supportive care is crucial due to the risk of edema and compression of adjacent structures. Although decompressive strategies may be needed in large infarcts, in SCA strokes the focus is usually on symptomatic and rehabilitative management. In pregnant or lactating patients, thrombolytic and antithrombotic therapies are administered following established guidelines (with careful risk\u2010benefit analysis) and imaging is used to confirm infarct location.",
        "option_analysis": "Option A (Ipsilateral Horner/ptosis) is more indicative of a lateral medullary (PICA) infarct, involving disruption of the descending sympathetic fibers. Option B (Ipsilateral fourth nerve palsy) points toward a midbrain lesion affecting the trochlear nerve. Neither of these options captures the classic presentation of an SCA infarct. The expected clinical finding would be cerebellar dysfunction, such as ipsilateral limb ataxia or other markers of cerebellar involvement, which we assume corresponds to option C (though not explicitly listed).",
        "clinical_pearls": "1. SCA strokes typically produce ipsilateral cerebellar signs like ataxia and dysmetria. 2. Isolated cranial nerve deficits (such as a fourth nerve palsy) are usually linked to midbrain or other brainstem lesions rather than pure cerebellar infarcts.",
        "current_evidence": "Recent stroke management guidelines emphasize early recognition and localization of posterior circulation strokes using MRI. Studies consistently show that cerebellar infarcts in the SCA territory manifest with coordination deficits rather than isolated ocular motor nerve palsies. There remains active research in optimizing early rehabilitative interventions for cerebellar strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993284",
    "fields": {
      "question_number": "66",
      "question_text": "A 45-year-old man suffers bilateral vertebral artery dissections and multiple brain stem and cerebellar infarctions causing right hemiplegia, dysarthria, and dysphagia. Two years later he returns, complaining of oscillopsia at rest. (Not mentioned: Examination of his eyes reveals a 1-Hz pendular oscillation comprising conjugate vertical and torsional components; the right eye intorts as",
      "options": {
        "A": "(Ipsilateral Horner/ptosis) is more indicative of a lateral medullary (PICA) infarct, involving disruption of the descending sympathetic fibers. Option B (Ipsilateral fourth nerve palsy) points toward a midbrain lesion affecting the trochlear nerve. Neither of these options captures the classic presentation of an SCA infarct. The expected clinical finding would be cerebellar dysfunction, such as ipsilateral limb ataxia or other markers of cerebellar involvement, which we assume corresponds to option C (though not explicitly listed)."
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "The superior cerebellar artery (SCA) supplies the superior aspect of the cerebellum, which is central to coordination, balance, and fine motor control. Infarction in this vascular territory typically produces cerebellar signs, such as ipsilateral limb ataxia, dysmetria, and dysdiadochokinesia. The core concept is localizing neurological deficits based on vascular territories within the posterior fossa.",
        "pathophysiology": "An ischemic stroke in the SCA territory leads to infarction of cerebellar tissue. This results in edema and loss of function in the regions controlling coordination. Although the SCA may supply parts of the cerebellar peduncles and, in some cases, adjacent regions of the midbrain, isolated involvement of cranial nerve IV (which governs the superior oblique muscle and mediates downward gaze) is much less typical. Rather, the damage mainly disrupts cerebellar circuits.",
        "clinical_correlation": "Patients with SCA infarcts commonly present with ipsilateral cerebellar signs including limb ataxia and dysmetria. They may have disturbances in balance and coordination, which can manifest as a wide-based gait, tremor, or difficulty with rapid alternating movements. A fourth nerve palsy, which would produce vertical diplopia and difficulty with downward gaze, is more characteristic of a specific midbrain lesion rather than a pure cerebellar (SCA) stroke.",
        "diagnostic_approach": "When evaluating a patient with suspected posterior circulation stroke, the differential diagnoses include infarcts in the PICA territory (lateral medullary syndrome with features such as ipsilateral Horner syndrome and loss of pain and temperature on the face), AICA infarcts (which can involve facial nerve deficits and hearing loss), and midbrain strokes. Neuroimaging (MRI) is key to localizing the vascular territory and differentiating between these entities.",
        "classification_and_neurology": "Pendular nystagmus is classified under central nystagmus types, distinct from peripheral vestibular nystagmus. It differs from jerk nystagmus by having smooth, sinusoidal oscillations rather than fast and slow phases. Central nystagmus can be further categorized based on etiology: demyelinating (e.g., multiple sclerosis), ischemic (brainstem/cerebellar infarcts), congenital, or paraneoplastic.  This patient's condition falls under ischemic central ocular motor disorders secondary to posterior circulation stroke. The broader disease family includes cerebrovascular diseases affecting the brainstem and cerebellum, with resultant neuro-ophthalmological syndromes.   Classification systems for nystagmus have evolved from purely phenomenological to incorporating etiology and pathophysiology, as reflected in consensus statements from neuro-ophthalmology societies. Current frameworks emphasize the importance of waveform characteristics, direction, and associated neurological signs to guide diagnosis and management.",
        "classification_and_nosology": "This scenario falls under ischemic cerebrovascular disease, specifically a cerebellar infarction in the SCA territory. Cerebellar strokes are categorized within the spectrum of posterior circulation strokes.",
        "management_principles": "Standard management of ischemic stroke includes prompt evaluation for thrombolytic eligibility and secondary prevention measures (antiplatelet therapy, risk factor management, and rehabilitation). In cerebellar strokes, supportive care is crucial due to the risk of edema and compression of adjacent structures. Although decompressive strategies may be needed in large infarcts, in SCA strokes the focus is usually on symptomatic and rehabilitative management. In pregnant or lactating patients, thrombolytic and antithrombotic therapies are administered following established guidelines (with careful risk\u2010benefit analysis) and imaging is used to confirm infarct location.",
        "option_analysis": "Option A (Ipsilateral Horner/ptosis) is more indicative of a lateral medullary (PICA) infarct, involving disruption of the descending sympathetic fibers. Option B (Ipsilateral fourth nerve palsy) points toward a midbrain lesion affecting the trochlear nerve. Neither of these options captures the classic presentation of an SCA infarct. The expected clinical finding would be cerebellar dysfunction, such as ipsilateral limb ataxia or other markers of cerebellar involvement, which we assume corresponds to option C (though not explicitly listed).",
        "clinical_pearls": "1. SCA strokes typically produce ipsilateral cerebellar signs like ataxia and dysmetria. 2. Isolated cranial nerve deficits (such as a fourth nerve palsy) are usually linked to midbrain or other brainstem lesions rather than pure cerebellar infarcts.",
        "current_evidence": "Recent stroke management guidelines emphasize early recognition and localization of posterior circulation strokes using MRI. Studies consistently show that cerebellar infarcts in the SCA territory manifest with coordination deficits rather than isolated ocular motor nerve palsies. There remains active research in optimizing early rehabilitative interventions for cerebellar strokes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993285",
    "fields": {
      "question_number": "67",
      "question_text": "Elderly patient presented with swallowing difficulty, examination found deviation of uvula to left side, Brain MRI reported brainstem infarction, what would be an expected symptom?",
      "options": {
        "A": "Right Horner (or Ptosis)",
        "B": "Left horror",
        "C": "Left hand ataxia",
        "D": "Right LL sensory loss"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "The patient\u2019s presentation with dysphagia and uvula deviation indicates involvement of the vagus nerve (CN X) motor fibers, particularly those from the nucleus ambiguus. In brainstem infarctions (especially lateral medullary or Wallenberg syndrome), a lesion on one side leads to weakness of the affected palatal muscles, causing the uvula to deviate toward the intact side. In this case, a uvula deviating to the left implies a right-sided lesion. One of the expected associated findings in a right lateral medullary infarction is an ipsilateral (right) Horner syndrome due to disruption of the descending sympathetic fibers.",
        "pathophysiology": "In lateral medullary (Wallenberg) syndrome, occlusion of the posterior inferior cerebellar artery (PICA) leads to infarction of the lateral aspect of the medulla. This region contains the nucleus ambiguus (affecting CN X and IX, leading to dysphagia and palatal weakness), the spinal trigeminal nucleus (affecting facial pain and temperature sensation), descending sympathetic fibers (leading to ipsilateral Horner syndrome), and portions of the spinothalamic tract (producing contralateral pain and temperature loss).",
        "clinical_correlation": "Elderly patients are predisposed to vascular events due to underlying atherosclerotic disease. When presenting with acute dysphagia and palatal abnormalities (such as uvula deviation), brainstem infarction should be considered. The lateral medullary syndrome is classically associated with these cranial nerve deficits, and the presence of an ipsilateral Horner syndrome (right side in this scenario) supports the diagnosis.",
        "diagnostic_approach": "Diagnosis is supported by neuroimaging (MRI) confirming a brainstem infarction. A thorough neurological examination helps localize the lesion: uvula deviation indicates a CN X palsy, while additional findings such as ipsilateral Horner syndrome, contralateral loss of pain and temperature sensation in the body, and possible cerebellar signs further refine the diagnosis. Differential diagnoses include other brainstem stroke syndromes such as lateral pontine syndrome, but the combination of dysphagia, uvula deviation, and sympathetic disruption is most in keeping with a lateral medullary (Wallenberg) syndrome.",
        "classification_and_neurology": "Brainstem strokes are classified anatomically: midbrain, pontine, and medullary infarcts, each with characteristic syndromes. Lateral medullary infarction (Wallenberg syndrome) is a subtype of posterior circulation stroke involving the vertebral or PICA territory. The TOAST classification categorizes strokes by etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined, or undetermined causes. Brainstem strokes fall under posterior circulation strokes, often due to large artery atherosclerosis or artery-to-artery embolism. The classification of brainstem syndromes is based on lesion location and clinical features, which guide diagnosis and prognosis. While classical syndromes are well described, overlap and variant presentations exist due to anatomical variability and lesion size.",
        "classification_and_nosology": "This condition is classified under posterior circulation strokes, specifically lateral medullary syndrome (Wallenberg syndrome). It is a well\u2010defined clinical syndrome resulting from infarction in the lateral portion of the medulla, typically due to occlusion of the PICA.",
        "management_principles": "Management of brainstem infarction follows standard acute ischemic stroke protocols, including evaluation for thrombolytic therapy (if within the window period) and supportive care (managing dysphagia, preventing aspiration, blood pressure control, and early rehabilitation). Special considerations in pregnancy involve a careful risk-benefit analysis for thrombolysis and imaging (non-contrast MRI is preferred), while in lactating patients, most acute stroke therapies (e.g., aspirin, heparin) are considered compatible with breastfeeding. Multidisciplinary management is crucial.",
        "option_analysis": "Option A (Right Horner syndrome) is the most consistent with a right-sided lateral medullary infarct. Option B (Left Horner syndrome) would be inconsistent with the lateralization indicated by the uvula deviation. Option C (Left hand ataxia) does not fit the typical distribution of deficits seen in this syndrome, and Option D (Right lower limb sensory loss) misrepresents the expected pattern, as contralateral pain/temperature loss would more likely be diffusely distributed rather than isolated to the lower limb.",
        "clinical_pearls": "\u2022 Uvula deviation away from the lesion side is a key sign of CN X dysfunction; it helps localize the lesion in brainstem infarcts.  \u2022 In lateral medullary syndrome, look for ipsilateral Horner syndrome, dysphagia, and contralateral loss of pain and temperature sensation.  \u2022 A detailed neurological exam can provide significant localization clues even before imaging is obtained.",
        "current_evidence": "Contemporary guidelines emphasize rapid recognition and treatment of acute stroke syndromes. Thrombolytic therapy within the approved time window, rigorous secondary stroke prevention, and multidisciplinary rehabilitation remain the cornerstones of modern management. In specialized populations such as pregnant or lactating patients, customization of treatment modalities to minimize risk while ensuring efficacy is guided by current consensus statements and research."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_4.png"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993286",
    "fields": {
      "question_number": "68",
      "question_text": "Elderly presented with 6 hours right sided weakness including arm, leg and face with mild dysarthria. Brain CT attached showing acute left internal capsule infarction. What is the earlier finding of brain cell ischemia?",
      "options": {
        "A": "Astrocyte fragmentations",
        "B": "Cells or neuronal swelling",
        "C": "Microglial proliferation",
        "D": "?"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2024,
      "explanation_sections": {
        "conceptual_foundation": "In the setting of acute ischemia, the earliest microscopic finding is cytotoxic edema, which is manifested as cellular (neuronal) swelling. This reflects the failure of the cell\u2019s energy-dependent ionic pumps due to ischemia.",
        "pathophysiology": "When blood flow is interrupted, ATP production drops. Consequently, the Na+/K+ ATPase fails, causing an influx of sodium and water into the cell. Neuronal swelling (cytotoxic edema) ensues within minutes, making it one of the first indicators of cellular injury. Later changes such as astrocytic fragmentation and microglial proliferation occur as the ischemic cascade progresses.",
        "clinical_correlation": "Clinically, early ischemic changes can be subtle and may not be immediately visible on imaging. However, the underlying process of cell swelling correlates with the clinical manifestations of stroke (e.g., contralateral weakness, dysarthria) and the evolution of tissue damage seen in later imaging.",
        "diagnostic_approach": "Diagnosis is based on clinical presentation and imaging. Differential diagnoses include hemorrhagic stroke (ruled out by CT), hypoglycemia-related deficits, and transient ischemic attacks. Early CT changes are subtle; advanced imaging like MRI diffusion-weighted imaging can help detect early ischemia.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases in the ICD-11 and the TOAST classification system. TOAST classifies ischemic strokes into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), stroke of other determined etiology, and stroke of undetermined etiology. Internal capsule infarcts are frequently lacunar strokes due to small vessel disease. Histopathologically, ischemic stroke evolution follows stages: hyperacute (minutes to hours, neuronal swelling), acute (hours to days, astrocyte and microglial changes), subacute (days to weeks, macrophage infiltration), and chronic (weeks to months, gliosis and cavitation). This temporal classification aids in correlating clinical presentation with imaging and histology.",
        "classification_and_nosology": "Ischemic stroke is classified according to the Oxfordshire Community Stroke Project into subtypes (e.g., lacunar infarcts, partial anterior circulation infarcts, etc.) based on clinical and imaging findings. Cytotoxic edema is a hallmark of acute ischemic injury.",
        "management_principles": "Management of acute ischemic stroke focuses on timely reperfusion if within the therapeutic window, supportive care, and secondary prevention. There is no intervention to reverse cellular swelling immediately, but rapid reperfusion (via IV tPA or endovascular intervention if indicated) is vital. For patients who are pregnant or lactating, the benefits of reperfusion therapy must be balanced against potential risks, though tPA is generally considered if indicated.",
        "option_analysis": "Option A (Astrocyte fragmentations) and Option C (Microglial proliferation) represent later histopathological events. Option B (Cells or neuronal swelling) correctly identifies the earliest change in ischemia.",
        "clinical_pearls": "1. Cytotoxic edema is the earliest marker of neuronal injury in stroke. 2. Early signs of ischemia may not be apparent on CT and might require advanced imaging. 3. Time is brain: early detection and management are crucial.",
        "current_evidence": "Recent literature stress the importance of early intervention in ischemic stroke and the role of advanced neuroimaging in detecting early cellular changes. New research continues to emphasize optimizing reperfusion strategies even when cellular injury is already underway."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json",
      "image_url": "page_2.png"
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
