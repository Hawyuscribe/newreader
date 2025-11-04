
# Import batch 2 of 3 from chunk_12_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993132",
    "fields": {
      "question_number": "60",
      "question_text": "73 years old female patient presented with decrease LOC showing hemorrhage with fluid level:",
      "options": {
        "A": "Amyloid",
        "B": "CVT",
        "C": "Anticoagulation use"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This case describes an elderly patient (73 years old) with decreased level of consciousness and imaging showing a hemorrhage with a fluid level. A fluid\u2013fluid level within a hemorrhage is a radiologic sign often associated with coagulopathy or the effects of anticoagulation, where the blood fails to clot uniformly, leading to layering of blood components. Although lobar hemorrhages in the elderly can also be due to cerebral amyloid angiopathy, the presence of a fluid level is more characteristic of bleeding in the setting of anticoagulant use.",
        "pathophysiology": "In patients on anticoagulant therapy (e.g., warfarin or direct oral anticoagulants), the normal clotting cascade is impaired. This leads to less effective clot formation and allows blood to remain in a liquid state for longer periods. Consequently, red blood cells may settle out, creating a visible fluid\u2013fluid level on imaging studies. This phenomenon is less typical in conditions like cerebral amyloid angiopathy or hemorrhagic venous infarctions seen in CVT.",
        "clinical_correlation": "Elderly patients are often on anticoagulant therapy for conditions such as atrial fibrillation, mechanical heart valves, or a history of thromboembolism. In such patients, even minor head trauma or spontaneous bleeding can lead to significant intracranial hemorrhage. Decreased level of consciousness is a common manifestation, and the imaging finding of a fluid level within the hemorrhage further supports a coagulopathy-related bleed.",
        "diagnostic_approach": "When evaluating an intracranial hemorrhage in an elderly patient, it is essential to review the medication history (especially anticoagulant use), blood coagulation profiles, and correlate clinical symptoms with imaging findings. Differential diagnoses include: 1) Cerebral amyloid angiopathy, which typically causes lobar hemorrhages but without a distinct fluid level; 2) Cerebral venous thrombosis (CVT), which may lead to hemorrhagic infarcts but is less likely in this age group and with this imaging characteristic; 3) Anticoagulation-induced hemorrhage, which is strongly suggested by the presence of a fluid level.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on etiology, location, and imaging characteristics. The major etiological categories include hypertensive hemorrhages (deep basal ganglia, thalamus), cerebral amyloid angiopathy (lobar), anticoagulant-related hemorrhages, vascular malformations, and hemorrhagic transformation of ischemic strokes. Fluid levels within hematomas are a radiological sign rather than a separate classification but are strongly associated with coagulopathy-induced hemorrhages. The International Classification of Diseases (ICD) classifies hemorrhagic strokes under cerebrovascular diseases, with subcodes for hemorrhage type and cause. Contemporary nosology emphasizes the importance of identifying underlying causes such as anticoagulation to guide management.",
        "classification_and_nosology": "Intracerebral hemorrhages are classified according to their location (lobar, deep, cerebellar, brainstem) and underlying etiology. Anticoagulation-induced hemorrhages fall under the category of secondary hemorrhages due to medication-induced coagulopathy. While cerebral amyloid angiopathy is also a cause of lobar hemorrhages in the elderly, its imaging characteristics differ, and the fluid\u2013fluid level is not typical of this condition.",
        "management_principles": "Management of anticoagulation-induced intracranial hemorrhage involves immediate stabilization of the patient, blood pressure control, and reversal of the anticoagulation. This might include the administration of vitamin K and prothrombin complex concentrate for warfarin-related bleed or specific reversal agents (e.g., idarucizumab for dabigatran, andexanet alfa for factor Xa inhibitors) when indicated. In pregnant or lactating patients (though not applicable in this 73-year-old case), management decisions would consider the safety of reversal agents; current guidelines recommend using agents with established safety profiles in pregnancy when reversal of anticoagulation is needed, with multidisciplinary consultation involving neurology, obstetrics, and hematology.",
        "option_analysis": "Option A (Amyloid) is less likely because while cerebral amyloid angiopathy causes lobar hemorrhage, it does not typically produce a fluid\u2013fluid level. Option B (CVT) can lead to hemorrhagic infarcts but is not commonly associated with a fluid level and is more frequent in younger individuals. Option D is absent. Therefore, option C (Anticoagulation use) is the most consistent with the clinical and radiologic findings described.",
        "clinical_pearls": "\u2022 A fluid\u2013fluid level in an intracranial hemorrhage should prompt evaluation for coagulopathy or anticoagulation use. \u2022 A thorough medication history is critical in elderly patients presenting with hemorrhage. \u2022 Reversal of anticoagulation is a key step in management to prevent hemorrhage expansion.",
        "current_evidence": "Recent guidelines emphasize the importance of early recognition and reversal of anticoagulation in the setting of intracranial hemorrhage to reduce morbidity and mortality. Studies support the use of rapid reversal agents and multidisciplinary approaches for optimal outcomes. Although cerebral amyloid angiopathy is a common cause of lobar hemorrhages in the elderly, the imaging finding of a fluid level is most consistent with anticoagulant-associated bleeding, which is supported by current clinical and radiographic evidence."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993459",
    "fields": {
      "question_number": "1",
      "question_text": "What is the artey?",
      "options": {
        "A": "mca",
        "B": "pca",
        "C": "ant choroidal artery"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question appears to assess knowledge of cerebral vascular anatomy. The options reference major cerebral arteries: the middle cerebral artery (MCA), posterior cerebral artery (PCA), and the anterior choroidal artery. The anterior choroidal artery is a smaller, but clinically important vessel that typically arises from the internal carotid artery. It supplies critical regions such as portions of the internal capsule, optic tract, and parts of the choroid plexus of the lateral ventricle.",
        "pathophysiology": "Occlusion or infarction in the territory of the anterior choroidal artery can produce the classic anterior choroidal syndrome, which may result in contralateral hemiparesis, hemisensory deficits, and homonymous hemianopia. Its small size and the fact that it supplies deep brain structures underscore the clinical relevance when vascular compromise occurs.",
        "clinical_correlation": "Clinically, patients with an infarct in the anterior choroidal artery territory may present with a combination of motor, sensory, and visual deficits. Recognizing the distribution of neurological deficits can help distinguish strokes in this territory from those involving the MCA (which usually involves lateral cortical areas) or PCA (which often present with primary visual field deficits without the same degree of motor involvement).",
        "diagnostic_approach": "In practice, neuroimaging such as CT angiography or MR angiography is used to delineate the vascular territories and identify the culprit vessel. The differential diagnosis involves distinguishing between larger vessel strokes (MCA or PCA territory) and smaller deep infarcts. In a stroke setting, clinical findings supported by imaging can lead to targeted management.",
        "classification_and_neurology": "The **anterior choroidal artery syndrome** is classified among lacunar or small vessel infarcts due to the artery\u2019s small caliber and deep perforating branches. However, it can also result from large artery atherosclerosis or embolism involving the internal carotid artery.  In the TOAST classification of ischemic stroke etiology, AChA strokes may fall into the categories of large artery atherosclerosis or cardioembolism depending on the underlying cause.  From a vascular anatomy standpoint, the AChA is considered a branch of the internal carotid artery, distinct from the MCA and PCA, which arise from the internal carotid and basilar arteries respectively. This anatomical classification is critical for understanding stroke syndromes and potential collateral pathways.  Controversies exist regarding the variability of the AChA territory and its collateral supply, which may influence clinical presentations.",
        "classification_and_nosology": "Anterior choroidal artery syndrome is classified under ischemic strokes. Its clinical profile is distinct from other stroke syndromes (e.g., MCA syndrome characterized by broader cortical deficits or PCA syndrome predominantly affecting vision) despite some overlapping features. Thus, the nosological framework combines both anatomical and clinical considerations.",
        "management_principles": "Management of an infarct in the anterior choroidal artery territory follows general ischemic stroke guidelines, including rapid revascularization therapy (e.g., IV thrombolysis if within therapeutic window) and secondary prevention (antiplatelet therapy, blood pressure control, and management of risk factors). In pregnancy, thrombolytic therapy (such as IV alteplase) can be considered after a careful risk-benefit analysis, and imaging modalities are selected to minimize fetal exposure. For lactating patients, standard stroke treatments are generally continued with counseling regarding medication safety during lactation.",
        "option_analysis": "Option A (MCA) and Option B (PCA) both represent major cerebral arteries with distinct territorial supplies. The middle cerebral artery supplies large portions of the lateral cerebral cortex, whereas the posterior cerebral artery primarily supplies the occipital lobes. The anterior choroidal artery, Option C, is a small but critical branch commonly arising from the internal carotid artery, and it has a well-defined territory that, when infarcted, produces a distinct clinical picture. The marked answer, Option C, is the appropriate and most specific answer given the likely intent of the question.",
        "clinical_pearls": "\u2022 The anterior choroidal artery supplies key deep brain structures including portions of the internal capsule and the optic tract.  \u2022 Infarcts in its territory may cause a combination of motor, sensory, and visual deficits (anterior choroidal artery syndrome).  \u2022 Timely identification of the involved artery via imaging is critical for rapid intervention.  \u2022 In pregnant or lactating patients, modifications in imaging technique and therapy (e.g., thrombolytics) need to be considered according to current guidelines.",
        "current_evidence": "Recent stroke management guidelines emphasize rapid identification of the vascular occlusion and tailored reperfusion strategies. Advances in imaging have allowed more precise localization of infarcts even in small arterial territories such as the anterior choroidal artery. Moreover, evidence supports that standard stroke treatments can be safely and effectively modified for use in pregnant and lactating patients, with careful monitoring and risk assessment."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993420",
    "fields": {
      "question_number": "1",
      "question_text": "What yoi will do?",
      "options": {
        "A": "Shunt",
        "B": "anticoagulant",
        "C": "give",
        "D": "give LMWH"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In neurology and neurosurgery, a shunt procedure is employed to divert cerebrospinal fluid (CSF) and thereby relieve the signs and symptoms of hydrocephalus. Hydrocephalus may be obstructive (non-communicating) or communicating, and when medical management fails or is not indicated, surgical CSF diversion via shunting (typically a ventriculoperitoneal shunt) is the definitive treatment.",
        "pathophysiology": "Hydrocephalus results from an imbalance between CSF production and absorption or from an obstruction of CSF flow. This leads to an accumulation of CSF within the ventricular system, causing increased intracranial pressure. Over time, this pressure can compress brain tissue and lead to neurological deficits. The shunt bypasses the obstructed flow, allowing CSF to be diverted from the ventricles to another body cavity (usually the peritoneal cavity) where it can be absorbed.",
        "clinical_correlation": "Patients with hydrocephalus may present with symptoms such as headache, nausea, vomiting, altered mental status, gait disturbances, and in some cases cognitive impairment. In conditions like normal pressure hydrocephalus (NPH), the classic clinical triad includes gait apraxia, dementia, and urinary incontinence. The decision to place a shunt is based on clinical findings as well as radiologic evidence of ventriculomegaly.",
        "diagnostic_approach": "Diagnosis requires neuroimaging, usually with CT or MRI. These studies help to confirm ventriculomegaly and to differentiate between communicating and non\u2010communicating causes of hydrocephalus. A lumbar puncture (after imaging rules out mass lesions) may also be used diagnostically especially in NPH where a large volume tap test can predict shunting success.",
        "classification_and_neurology": "Cerebrovascular diseases are classified broadly into ischemic strokes, hemorrhagic strokes, and venous strokes (CVT). The International Classification of Diseases (ICD-11) and the TOAST criteria focus on arterial ischemic stroke subtypes. CVT is classified under venous strokes, a distinct nosological entity due to its unique pathophysiology and treatment. This classification influences management algorithms. Over time, recognition of CVT as a separate category has improved diagnosis and targeted therapy. Controversies exist regarding anticoagulation in hemorrhagic CVT, but consensus supports its use. The differentiation between arterial and venous strokes is critical for appropriate therapy.",
        "classification_and_nosology": "Hydrocephalus is classified into communicating (non-obstructive) and non-communicating (obstructive) types. The underlying etiologies include congenital defects, hemorrhage, infection, tumors, and normal pressure hydrocephalus. Surgical shunting is typically considered when there is evidence of increased intracranial pressure or progressive neurologic deterioration.",
        "management_principles": "The standard management of symptomatic hydrocephalus is CSF diversion by shunt placement. Current guidelines suggest that shunting is indicated in patients with confirmed hydrocephalus who have corresponding clinical symptoms. In pregnant patients, the decision to intervene surgically is based on symptom severity and risks. While the procedure itself carries risks inherent to surgery and anesthesia, multidisciplinary planning can minimize fetal risk. For lactating patients, shunt surgery is also considered safe, although supportive care and coordination with obstetrics is advisable.",
        "option_analysis": "Option A (Shunt) is the only answer that corresponds to a definitive treatment in a scenario that implies a CSF diversion need. Options B (anticoagulant) and D (give LMWH) are relevant for conditions like cerebral venous sinus thrombosis and are not indicated in hydrocephalus unless there is an overlapping thromboembolic event. Option C ('give') is incomplete and non-specific. Given the context and the management strategy for hydrocephalus, the shunt option is the most appropriate.",
        "clinical_pearls": "\u2022 Always correlate clinical symptoms with imaging findings to confirm the diagnosis of hydrocephalus before proceeding with shunt placement. \u2022 In cases of ambiguous neurological presentations, distinguishing between vascular (e.g., CVT requiring anticoagulation) and CSF flow disorders (requiring shunting) is key. \u2022 In special populations like pregnant or lactating women, multidisciplinary care ensures that both maternal and fetal/neonatal risks are minimized.",
        "current_evidence": "Recent guidelines and studies continue to endorse CSF shunting (particularly ventriculoperitoneal shunting) as the gold standard for managing symptomatic hydrocephalus. Surgical techniques and postoperative care protocols have improved, reducing complications. In clinical practice, careful selection and preoperative testing (sometimes including a lumbar drain trial) help improve outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993403",
    "fields": {
      "question_number": "1",
      "question_text": "What is the mechanism?",
      "options": {},
      "correct_answer": "T",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question is centered on identifying the underlying mechanism responsible for a hemorrhagic event. It requires distinguishing between structural causes (such as hypertension-induced vessel changes or aneurysmal rupture) and systemic causes (like coagulopathy) that affect the clotting cascade. In this scenario, the key is recognizing that an impaired coagulation mechanism directly predisposes to bleeding.",
        "pathophysiology": "Coagulopathies impair the normal clotting cascade\u2014whether due to anticoagulant medication, liver dysfunction, or congenital disorders\u2014resulting in an inability to form stable fibrin clots. Unlike hemorrhages secondary to chronic hypertension (which result from long-term vascular remodeling and are typically seen in deep brain structures) or aneurysms (which usually cause sudden subarachnoid bleeding), coagulopathy-associated hemorrhages stem from a systemic deficiency in clot formation leading to spontaneous bleeding even without pre-existing vascular lesions.",
        "clinical_correlation": "Patients with coagulopathy\u2010induced hemorrhages may present with intracerebral bleeding that appears in atypical locations compared to the classic deep brain regions seen in hypertensive hemorrhage. Laboratory tests (such as PT, INR, and PTT) help confirm the diagnosis. Clinically, the lack of a history of severe hypertension or aneurysmal symptoms combined with abnormal coagulation profiles should guide clinicians toward this diagnosis.",
        "diagnostic_approach": "The diagnostic workup includes neuroimaging (CT/MRI) to determine the location and pattern of hemorrhage, along with coagulation studies to assess clotting function. Differential diagnoses include: 1) Hypertensive hemorrhage (typically in the basal ganglia, thalamus, or cerebellum) characterized by a history of chronic hypertension; 2) Aneurysmal rupture, which classically causes subarachnoid hemorrhage; and 3) Other vascular malformations that usually have distinct imaging patterns.",
        "classification_and_neurology": "Cerebrovascular diseases are classified by the **American Heart Association/American Stroke Association (AHA/ASA)** into ischemic and hemorrhagic stroke subtypes. Hemorrhagic strokes are further divided into intracerebral hemorrhage (ICH) and subarachnoid hemorrhage (SAH). Etiologically, hemorrhagic strokes can be due to hypertension, vascular malformations, aneurysms, or coagulopathies. The presence of coagulopathy places the hemorrhage in a distinct subclass characterized by bleeding tendency rather than vessel wall pathology. This classification aids in prognostication and management. The **Trial of Org 10172 in Acute Stroke Treatment (TOAST)** classification is primarily for ischemic strokes but highlights the importance of mechanistic categorization for guiding therapy. Current consensus emphasizes integrating clinical, radiological, and laboratory data to subtype cerebrovascular events accurately.",
        "classification_and_nosology": "Intracerebral hemorrhages are classified based on their etiology (e.g., hypertensive, amyloid angiopathy, coagulopathy-related, aneurysmal). Hemorrhages driven by coagulopathy are grouped under secondary hemorrhages resulting from systemic or iatrogenic causes.",
        "management_principles": "Management focuses on rapid stabilization and reversal of the coagulopathic state. First-line interventions include administration of vitamin K, fresh frozen plasma, or prothrombin complex concentrates based on the underlying cause. In cases where anticoagulant medications are involved, specific reversal agents (for example, idarucizumab for dabigatran) may be required. In pregnant or lactating patients, the decision to reverse a coagulopathy must balance maternal risks with fetal considerations; many reversal agents have been studied in these populations, and a multidisciplinary approach (involving obstetrics and hematology) is advised.",
        "option_analysis": "\u2022 Option 1 (Hypertension): Incorrect because while chronic HTN can cause hemorrhage, it typically does so through long-term vascular changes rather than through an acute impairment of coagulation. \u2022 Option 2 (Coagulopathy): Correct since a systemic clotting defect disrupts normal hemostasis and predisposes to bleeding. \u2022 Option 3 (Aneurysm): Incorrect as aneurysms lead to hemorrhage via focal arterial dilation and rupture, usually resulting in subarachnoid hemorrhage.",
        "clinical_pearls": "1. In the absence of typical risk factors like chronic hypertension, always consider a coagulopathy when evaluating spontaneous intracranial hemorrhage. 2. Rapid identification and reversal of a coagulation defect can prevent further bleeding and improve outcomes.",
        "current_evidence": "Recent literature emphasizes the importance of differentiating hemorrhage etiologies because treatment differs markedly. Advances in specific reversal agents have improved outcomes in coagulopathy\u2010induced hemorrhages. Current guidelines stress the prompt correction of coagulation abnormalities, particularly in patients receiving anticoagulants."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993417",
    "fields": {
      "question_number": "1",
      "question_text": "82 years old male pt came within 3 hrs and have no contraindication for tpa and ct attached with early signe of stroke but infarction not established what you will give",
      "options": {
        "A": "aspirin",
        "B": "plavix",
        "C": "tpa"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question tests the acute management of ischemic stroke within the therapeutic time window. The central concept is that timely administration of a thrombolytic agent, such as tissue plasminogen activator (tPA), significantly improves neurological outcomes by dissolving the clot obstructing cerebral blood flow.",
        "pathophysiology": "Acute ischemic stroke is caused by an arterial occlusion that leads to cerebral ischemia. tPA acts by converting plasminogen to plasmin, which then degrades fibrin, effectively lysing the clot and restoring blood flow to the affected brain region. This reperfusion of the penumbra limits infarct size.",
        "clinical_correlation": "In the clinical scenario described, the 82-year-old male presents within a crucial 3-hour window, where early CT imaging reveals subtle signs of ischemia without established infarction, making him an ideal candidate for tPA. Despite advanced age, the eligibility criteria for tPA are met, reflecting current practices where age alone is not a contraindication.",
        "diagnostic_approach": "Diagnosis is confirmed with a non-contrast CT scan to rule out hemorrhage and ascertain the absence of significant infarction. Differential considerations include transient ischemic attack (TIA) and hemorrhagic stroke, but rapid imaging and clinical examination help exclude these possibilities.",
        "classification_and_neurology": "Acute ischemic stroke is classified under cerebrovascular diseases within the International Classification of Diseases (ICD-10: I63). It is further categorized by etiology using the TOAST classification:  - Large artery atherosclerosis - Cardioembolism - Small vessel occlusion (lacunar) - Stroke of other determined etiology - Stroke of undetermined etiology  This classification aids in understanding stroke mechanisms and tailoring secondary prevention. The management of acute ischemic stroke falls under emergency neurology and stroke medicine, with treatment protocols standardized by guidelines such as those from the American Heart Association/American Stroke Association (AHA/ASA). The evolution of classification systems has improved diagnostic precision and therapeutic strategies.",
        "classification_and_nosology": "Acute ischemic strokes are classified by etiology (e.g., cardioembolic, large-artery atherosclerotic, small vessel disease) and location. The management decision for tPA is based on time from symptom onset and radiographic findings rather than stroke subtype.",
        "management_principles": "First-line treatment for eligible patients with acute ischemic stroke is IV tPA administered within 3 to 4.5 hours of symptom onset. If patients present outside this window or have contraindications, alternative interventions such as mechanical thrombectomy may be considered. For pregnant patients facing stroke, tPA can be administered after careful risk-benefit analysis and consultation with obstetric specialists, as improved maternal outcomes often translate into better fetal outcomes. In lactating women, tPA administration is generally considered safe, but appropriate counseling is recommended.",
        "option_analysis": "\u2022 Option A (Aspirin) and Option B (Plavix): These antiplatelet agents are used for long-term secondary prevention, not for acute thrombolysis. \u2022 Option C (tPA): Correct, as it addresses the need for prompt thrombolysis in acute ischemic stroke. \u2022 Option D: Not provided and unnecessary in this context.",
        "clinical_pearls": "1. The mantra 'time is brain' underlines the importance of rapid thrombolytic therapy in acute stroke management. 2. Advanced age should not preclude the use of tPA if other eligibility criteria are satisfied.",
        "current_evidence": "Recent studies and stroke guidelines (e.g., those from the American Heart Association) reinforce the use of IV tPA in eligible patients within the tight treatment window. Continuous updates in stroke care protocols stress rapid imaging and swift decision-making, and recent research supports the safety and effectiveness of tPA even in older populations."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993567",
    "fields": {
      "question_number": "15",
      "question_text": "Rt small thalamic hemorrhage since one day, BP normal, pic attached no hydro or ventricular extension what to do next",
      "options": {
        "A": "(Prophylaxis LMWH): Correct because it reduces the risk of thromboembolic complications in a patient with a stable hemorrhage. \u2022 Option B (EVD): Incorrect, as external ventricular drainage is indicated in cases with hydrocephalus or significant intraventricular bleeding, which is not present in this patient."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question focuses on the management of a patient with a small intracerebral hemorrhage, specifically addressing the prevention of secondary thromboembolic complications. Once a hemorrhage is stable, prophylactic measures to minimize venous thromboembolism become paramount.",
        "pathophysiology": "A small thalamic hemorrhage, when stable and not complicated by hydrocephalus or ventricular extension, still puts the patient at risk for venous thromboembolism due to prolonged immobilization. Low Molecular Weight Heparin (LMWH) acts by inhibiting factor Xa (and to a lesser extent, thrombin), thereby reducing the risk of clot formation without significantly increasing the chance of rebleeding when administered at the correct time.",
        "clinical_correlation": "In this case, the patient\u2019s blood pressure is normal and imaging confirms that the hemorrhage is confined to the thalamus with no evidence of mass effect or hydrocephalus. This scenario supports the initiation of prophylactic anticoagulation to prevent deep venous thrombosis (DVT) as part of secondary prevention.",
        "diagnostic_approach": "Neuroimaging helps assess the size and nature of the hemorrhage. Differential diagnoses might include hemorrhagic transformation of an ischemic stroke or a ruptured aneurysm; however, these alternatives are less likely given the imaging findings and absence of hydrocephalus.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on location (lobar, deep, brainstem, cerebellar), etiology (hypertensive, amyloid angiopathy, vascular malformations, coagulopathy), and clinical severity. The deep hemorrhages include thalamic and basal ganglia hemorrhages and are commonly associated with hypertensive small vessel disease. The American Heart Association/American Stroke Association (AHA/ASA) stroke guidelines categorize ICH management based on hemorrhage size, location, presence of intraventricular hemorrhage, and clinical status. This classification guides prognosis and treatment. The nosology also differentiates primary ICH from secondary causes such as trauma or tumor. The current consensus emphasizes individualized management plans based on hemorrhage characteristics and patient comorbidities.",
        "classification_and_nosology": "Intracerebral hemorrhages are stratified by location (lobar, deep, thalamic, cerebellar) and the underlying cause. The management approach in a stable, small hemorrhage differs from that required for larger or more complicated hemorrhages.",
        "management_principles": "The first step involves ensuring hemodynamic stability and controlling blood pressure. If the hemorrhage is confirmed to be stable (typically after the first 24 hours), prophylactic LMWH is recommended to lower the risk of DVT. In special populations such as pregnant women, LMWH is generally considered safe (category B) with minimal placental transfer, and in lactating mothers, LMWH remains the preferred anticoagulant given its low risk of transmission through breast milk.",
        "option_analysis": "\u2022 Option A (Prophylaxis LMWH): Correct because it reduces the risk of thromboembolic complications in a patient with a stable hemorrhage. \u2022 Option B (EVD): Incorrect, as external ventricular drainage is indicated in cases with hydrocephalus or significant intraventricular bleeding, which is not present in this patient.",
        "clinical_pearls": "1. In patients with intracerebral hemorrhage, the initiation of VTE prophylaxis should be timed appropriately (after 24 hours) to avoid rebleeding. 2. A stable, small hemorrhage without ventricular involvement allows for safe prophylactic anticoagulation.",
        "current_evidence": "Latest guidelines from stroke and neurosurgical societies support early prophylactic anticoagulation in patients with stable intracerebral hemorrhage to prevent DVT. Recent studies continue to refine optimal timing and dosing strategies to maximize safety and efficacy while minimizing the risk of hematoma expansion."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993589",
    "fields": {
      "question_number": "156",
      "question_text": "Male with progressive myelopathy attached image clearly showing slow void, and long cord signal changes, dx",
      "options": {
        "A": "(DAVF): Correct, as the combination of progressive myelopathy and MRI findings with slow flow voids and elongated cord signal anomalies is classic for this diagnosis. Alternative options such as multiple sclerosis, transverse myelitis, or spinal tumors do not typically show the vascular flow voids on imaging."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This question examines the identification of a spinal vascular malformation as the cause of progressive myelopathy. The key concept is understanding that chronic venous congestion due to abnormal arteriovenous shunting can lead to spinal cord dysfunction over time.",
        "pathophysiology": "Spinal dural arteriovenous fistula (DAVF) is characterized by an abnormal connection between a radiculomeningeal artery and a medullary vein. This shunt elevates venous pressure, leading to cord congestion and ischemia. The chronic venous hypertension results in progressive myelopathy due to a combination of cord edema and insufficient perfusion.",
        "clinical_correlation": "Patients with DAVF typically present with slowly progressive symptoms such as lower extremity weakness, sensory changes, and sphincter dysfunction. The MRI findings of long-segment T2 hyperintensity with serpiginous flow voids strongly suggest the presence of dilated, abnormal vessels consistent with DAVF, correlating directly with the progressive clinical picture.",
        "diagnostic_approach": "The diagnostic strategy includes MRI which reveals both the cord signal changes and the characteristic flow voids of dilated vessels. Differential diagnoses include multiple sclerosis (often multifocal and ovoid lesions without abnormal flow voids), transverse myelitis (acute inflammatory process without dilated vessels), and spinal neoplasms (typically focal with mass effect rather than diffuse vascular changes).",
        "classification_and_neurology": "Spinal dural arteriovenous fistulas belong to the broader category of spinal vascular malformations. The most widely accepted classification system is the **Moldenhauer classification**, which divides spinal AVMs into four types:  - **Type I:** Spinal dural arteriovenous fistulas (DAVFs) \u2013 low-flow fistulas between dural arteries and radicular veins. - **Type II:** Intramedullary glomus AVMs \u2013 compact nidus within the spinal cord. - **Type III:** Juvenile or extensive AVMs \u2013 diffuse intramedullary and extramedullary involvement. - **Type IV:** Perimedullary AVFs \u2013 direct fistulas on the pial surface without nidus.  DAVFs (Type I) are the most common and typically present with progressive myelopathy due to venous hypertension. This classification helps guide diagnosis and management strategies. Over time, imaging advances have refined this system, but Moldenhauer's remains a clinical standard. Some controversies exist regarding the overlap between perimedullary AVFs and DAVFs, but the key distinction lies in the fistula location and flow dynamics.",
        "classification_and_nosology": "Spinal vascular malformations are categorized into several types, with spinal DAVF being the most common acquired type. It is classified separately from other vascular pathologies such as intradural arteriovenous malformations or pial fistulas.",
        "management_principles": "The first-line treatment for spinal DAVF is endovascular embolization, aiming to interrupt the abnormal shunt. When embolization is not feasible or is incomplete, surgical disconnection of the fistula is considered. In pregnant patients, management requires a multidisciplinary approach given the risks associated with radiation exposure and anesthesia; tailored intervention with minimized fluoroscopy time is advised. For lactating patients, similar considerations apply with close monitoring and counseling regarding procedural risks.",
        "option_analysis": "\u2022 Option A (DAVF): Correct, as the combination of progressive myelopathy and MRI findings with slow flow voids and elongated cord signal anomalies is classic for this diagnosis. Alternative options such as multiple sclerosis, transverse myelitis, or spinal tumors do not typically show the vascular flow voids on imaging.",
        "clinical_pearls": "1. When evaluating progressive myelopathy, always inspect MRI images for abnormal flow voids which may indicate a DAVF. 2. Early recognition of spinal DAVF is critical to prevent irreversible spinal cord damage.",
        "current_evidence": "Recent research and clinical guidelines emphasize the importance of prompt diagnosis and intervention in spinal DAVF. Newer endovascular techniques and surgical approaches have demonstrated improved outcomes, and current studies focus on optimizing the timing and method of intervention to maximize neurological recovery."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993635",
    "fields": {
      "question_number": "167",
      "question_text": "Male with renal impairment, stroke, angiokeratoma pic asking about enzyme supp",
      "options": {
        "A": "(alpha"
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Fabry disease is an X\u2010linked lysosomal storage disorder caused by a deficiency in the enzyme alpha-galactosidase A. This deficiency leads to the accumulation of glycosphingolipids, particularly globotriaosylceramide (Gb3), in various cell types and tissues, including vascular endothelial cells, kidney, heart, and skin.",
        "pathophysiology": "The lack of functional alpha-galactosidase A results in progressive storage of Gb3 within lysosomes. This accumulation induces cellular damage, microvascular dysfunction, and inflammatory changes that contribute to end-organ damage such as renal impairment, cerebrovascular ischemia (stroke), and characteristic skin findings (angiokeratomas). In men especially, the classic phenotype can be severe, with early manifestations affecting multiple systems.",
        "clinical_correlation": "Patients often present with a combination of symptoms including neuropathic pain, angiokeratomas (small, reddish-purple skin lesions), renal impairment, and an increased risk for cerebrovascular events. The concurrence of renal dysfunction, stroke, and skin lesions in a male patient is highly suggestive of Fabry disease.",
        "diagnostic_approach": "Diagnosis is confirmed by measuring alpha-galactosidase A activity in plasma or leukocytes and can be supported by genetic testing for mutations in the GLA gene. Differential diagnoses include other lysosomal storage disorders such as Gaucher disease (beta\u2010glucocerebrosidase deficiency) and Pompe disease (alpha\u2010glucosidase deficiency), which have distinct clinical and enzymatic profiles.",
        "classification_and_neurology": "Fabry disease is classified within the broader group of lysosomal storage disorders (LSDs), specifically under glycosphingolipidoses. It is an X-linked inherited metabolic disorder caused by mutations in the GLA gene encoding alpha-galactosidase A. The disease exhibits classic and late-onset (or variant) phenotypes, with the classic form presenting in childhood or adolescence with multisystem involvement, while late-onset variants may present predominantly with cardiac or renal manifestations in adulthood. The nosology distinguishes Fabry disease from other LSDs such as Gaucher disease (glucocerebrosidase deficiency) and Pompe disease (acid alpha-glucosidase deficiency). The current consensus emphasizes the importance of early diagnosis and enzyme replacement therapy (ERT) as disease-modifying treatment. There is ongoing debate about screening strategies and management of heterozygous females due to variable expression.",
        "classification_and_nosology": "Fabry disease is classified as a lysosomal storage disorder and is inherited in an X-linked recessive manner. It is subdivided into classic and later-onset (atypical) types, with the classic type generally presenting in childhood or adolescence and the atypical type often manifesting later.",
        "management_principles": "The first-line treatment is enzyme replacement therapy (ERT) with recombinant alpha-galactosidase A, which helps reduce substrate accumulation and slow disease progression. Adjunctive management includes supportive interventions for renal, cardiac, and cerebrovascular complications. In pregnancy and lactation, treatment decisions must carefully balance maternal benefits against potential fetal risks, and multidisciplinary consultation is advised as current data on ERT during pregnancy remain limited.",
        "option_analysis": "Option A (alpha-galactosidase, here noted as 'Galtcosidase') is correct since it directly addresses the enzyme deficiency in Fabry disease. Other enzymes listed, such as beta-glucocerebrosidase (associated with Gaucher disease), alpha-glucosidase (associated with Pompe disease), or galactocerebrosidase (associated with Krabbe disease), are unrelated to the pathogenesis of Fabry disease.",
        "clinical_pearls": "1. The triad of renal impairment, stroke, and angiokeratomas in a male patient should prompt consideration of Fabry disease. 2. Early initiation of ERT may attenuate long-term organ damage. 3. Enzyme activity assays coupled with genetic testing are crucial for a definitive diagnosis.",
        "current_evidence": "Recent clinical studies underscore the benefits of early intervention with ERT in Fabry disease to delay progression of organ dysfunction. Current guidelines advocate for a multidisciplinary approach, with close attention to cardiac and renal monitoring, and emerging research continues to refine optimal dosing and treatment initiation timings."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993564",
    "fields": {
      "question_number": "17",
      "question_text": "Scenario patient feeling unwell, then start seeing animals after which he had decreased LOC intubated, decerebrate posturing CT brain attached showed hyperdense basilar sign otherwise no clear ischemic changes what to do next",
      "options": {
        "A": "(CTA) is correct because CTA provides non",
        "B": "(EEG) is incorrect as it evaluates brain electrical activity and is not useful in diagnosing vascular occlusions."
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Basilar artery occlusion is a serious form of ischemic stroke affecting the posterior circulation. The hyperdense basilar artery sign on non-contrast CT is a key radiological finding that raises suspicion for this condition.",
        "pathophysiology": "An occlusive thrombus or embolus within the basilar artery can lead to reduced blood flow to critical brainstem regions. The hyperdense appearance on CT reflects the clot\u2019s density relative to normal blood, while the resultant ischemia causes brainstem dysfunction, which may manifest as altered consciousness or abnormal posturing.",
        "clinical_correlation": "In the described scenario, the patient\u2019s initial nonspecific symptoms rapidly progress to severe neurological compromise (decreased level of consciousness, decerebrate posturing) indicating brainstem involvement. The hyperdense basilar sign on CT strongly suggests a vascular occlusion requiring urgent further imaging and intervention.",
        "diagnostic_approach": "Following a non-contrast CT that reveals a hyperdense basilar artery, the next step is to perform CT angiography (CTA) to confirm the location and extent of the occlusion, assess collateral circulation, and guide reperfusion strategies. The differential includes non-ischemic causes of brainstem dysfunction (e.g., encephalopathy, metabolic disturbances) but these do not explain the hyperdense vascular sign.",
        "classification_and_neurology": "Basilar artery occlusion is classified under **ischemic strokes**, specifically within the **posterior circulation stroke** subgroup. According to the TOAST classification, it falls under **large artery atherosclerosis** or **cardioembolism** depending on etiology. Posterior circulation strokes encompass infarctions in territories supplied by the vertebral, basilar, and posterior cerebral arteries. The classification of stroke types has evolved to emphasize vascular territory and mechanism, aiding targeted management. BAO represents a severe subset of large vessel occlusions with high morbidity and mortality. Contemporary stroke classifications incorporate imaging findings such as vessel occlusion on CTA/MRA to refine diagnosis and guide reperfusion strategies. There is consensus that BAO requires urgent recognition distinct from anterior circulation strokes due to its unique clinical and prognostic implications.",
        "classification_and_nosology": "Basilar artery occlusion is classified as a posterior circulation stroke, which is a subtype of ischemic stroke. It is typically caused by thromboembolic events and, if untreated, is associated with high morbidity and mortality.",
        "management_principles": "Management involves rapid reperfusion, which may include intravenous thrombolysis (if within the therapeutic window, usually 4.5 hours) and endovascular thrombectomy. Intensive care monitoring and supportive measures are essential. In pregnant patients, risk-benefit analysis regarding thrombolysis or endovascular interventions should be performed in conjunction with obstetrical consultation, as the safety profiles of these treatments during pregnancy require careful consideration.",
        "option_analysis": "Option A (CTA) is correct because CTA provides non-invasive, rapid confirmation of vascular occlusion by visualizing the basilar artery. Option B (EEG) is incorrect as it evaluates brain electrical activity and is not useful in diagnosing vascular occlusions.",
        "clinical_pearls": "1. A hyperdense basilar artery sign on CT should prompt immediate vascular imaging with CTA. 2. Time is brain: rapid identification and treatment of basilar artery occlusion are crucial to prevent devastating brainstem infarction. 3. Endovascular therapy has become a key component in the management of large vessel occlusions.",
        "current_evidence": "Recent guidelines and studies have reinforced the role of CTA in the acute stroke workup, with growing evidence supporting endovascular thrombectomy even in extended time windows for select patients. Current protocols emphasize rapid diagnosis and the integration of advanced neuroimaging to optimize outcomes."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993461",
    "fields": {
      "question_number": "2",
      "question_text": "What is the mechanism?",
      "options": {
        "A": "tramatic haemorrage",
        "B": "ICh",
        "C": "lobar haemorrage"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "Intracerebral hemorrhage (ICH) refers to bleeding within the brain tissue and is most commonly a spontaneous event due to hypertension, although other causes exist. Differentiating among traumatic hemorrhage, deep (hypertensive) ICH, and lobar hemorrhages is key in understanding the underlying pathology.",
        "pathophysiology": "Hypertensive ICH typically results from chronic hypertension causing degeneration of the small penetrating arteries (with Charcot-Bouchard microaneurysm formation), leading to rupture and bleeding into the brain parenchyma. In contrast, lobar hemorrhages often occur in the cerebral lobes and may be associated with cerebral amyloid angiopathy, particularly in the elderly, while traumatic hemorrhages result from injury.",
        "clinical_correlation": "Clinical presentations of ICH vary but generally include a sudden onset of neurological deficits, headache, and altered consciousness. The location of the hemorrhage (deep versus lobar) can provide clues about the underlying etiology: deep ICH is commonly linked to hypertension, whereas lobar hemorrhages suggest alternative causes.",
        "diagnostic_approach": "Non-contrast CT is the first-line diagnostic tool to identify the location and extent of bleeding. History (including the presence or absence of trauma) and risk factors such as long-standing hypertension or amyloid angiopathy help differentiate the type of hemorrhage. Magnetic resonance imaging (MRI) may further characterize the hemorrhage and identify underlying lesions.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified primarily by location and etiology. The major categories include: 1) Hypertensive deep hemorrhages affecting basal ganglia, thalamus, pons, and cerebellum; 2) Lobar hemorrhages, often related to cerebral amyloid angiopathy; 3) Traumatic hemorrhages, including contusions and diffuse axonal injury; and 4) Secondary hemorrhages due to vascular malformations, tumors, or coagulopathy. The classification is reflected in systems such as the SMASH-U classification (Structural lesion, Medication, Amyloid angiopathy, Systemic/Hypertensive, Hypertensive, Undetermined) which aids in etiologic diagnosis. This nosology has evolved to emphasize etiology for guiding management and prognosis. There is consensus that distinguishing spontaneous ICH (e.g., hypertensive, amyloid) from traumatic hemorrhage is critical, as mechanisms and treatments differ substantially.",
        "classification_and_nosology": "ICH is a type of hemorrhagic stroke and is classified based on location (e.g., deep, lobar, brainstem, cerebellar) as well as underlying cause (e.g., hypertensive, amyloid-related). This classification has implications for prognosis and management.",
        "management_principles": "Management of ICH includes aggressive blood pressure control, reversal of any coagulopathy, and supportive care in an intensive care setting. In cases of large hematomas or significant mass effect, surgical intervention may be considered. For pregnant or lactating patients, blood pressure targets remain similar; however, interventions must carefully weigh maternal neurological status against fetal risks, often necessitating multidisciplinary management.",
        "option_analysis": "Option A (traumatic hemorrhage) is incorrect in a scenario without evidence of trauma. Option B (ICH) is correct because it aligns with the pathophysiology of spontaneous intracerebral hemorrhage typically seen in hypertensive patients. Option C (lobar hemorrhage) refers to a subtype generally associated with cerebral amyloid angiopathy and does not represent the general mechanism established for hypertensive ICH.",
        "clinical_pearls": "1. Hypertensive ICH most often involves deep brain structures such as the basal ganglia and thalamus. 2. Distinguishing between spontaneous and traumatic hemorrhage is critical and relies heavily on patient history and imaging findings. 3. Rapid blood pressure management is a cornerstone of ICH treatment to prevent hematoma expansion.",
        "current_evidence": "Recent clinical trials have supported intensive blood pressure control as a means to limit hematoma growth and improve outcomes in ICH. Research continues into minimally invasive surgical approaches, and updated guidelines emphasize individualized care that considers both the size and location of the hemorrhage."
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
