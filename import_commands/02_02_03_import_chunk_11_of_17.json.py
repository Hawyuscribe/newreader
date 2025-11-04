
# Import batch 3 of 3 from chunk_11_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993114",
    "fields": {
      "question_number": "42",
      "question_text": "pt with Acom aneurysm what is the most important risk factor for rupture:",
      "options": {
        "A": "Size",
        "B": "Smoking"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "Sneddon syndrome is a rare non\u2010inflammatory arteriopathy that classically presents with the combination of cerebrovascular events (strokes or transient ischemic attacks) and a characteristic skin finding\u2014livedo reticularis (a netlike violaceous rash). The syndrome is an important diagnostic consideration when a stroke patient also exhibits these unique cutaneous findings.",
        "pathophysiology": "The underlying mechanism involves a thrombotic vasculopathy affecting small to medium-sized arteries. Although the precise etiology isn\u2019t fully understood, many patients have circulating antiphospholipid antibodies and there may be overlap with other autoimmune conditions (such as systemic lupus erythematosus). The vascular occlusion leads to chronic ischemia in the brain and skin, manifesting as strokes and livedo reticularis, respectively.",
        "clinical_correlation": "Patients typically present with neurologic deficits due to ischemic strokes and a persistent, often widespread, livedo reticularis rash. The concurrence of these findings should prompt the clinician to evaluate for Sneddon syndrome, especially in younger patients or those without typical stroke risk factors.",
        "diagnostic_approach": "Evaluation includes neuroimaging (MRI and CT) to document ischemic lesions, and careful dermatologic exam. Skin biopsy may show non-inflammatory occlusive changes. Laboratory work\u2010up for antiphospholipid antibodies and other autoimmune markers is also indicated in order to differentiate from primary vasculitides or other coagulopathies.",
        "classification_and_neurology": "Intracranial aneurysms are classified primarily by morphology (saccular, fusiform, dissecting) and location (anterior vs. posterior circulation). The Acom aneurysm is a subtype of saccular aneurysms in the anterior circulation. The International Study of Unruptured Intracranial Aneurysms (ISUIA) classification system stratifies rupture risk based on aneurysm size and location. Risk factors are integrated into clinical scoring systems such as PHASES (Population, Hypertension, Age, Size, Earlier SAH, Site) to estimate rupture probability. This framework aids in risk stratification and management planning. Controversies remain regarding the weight of size versus other risk factors like smoking, with evolving evidence emphasizing modifiable risk factors.",
        "classification_and_nosology": "Sneddon syndrome is classified as a noninflammatory thrombotic vasculopathy. It can occur as a primary syndrome or secondary to connective tissue diseases (e.g., antiphospholipid syndrome, systemic lupus erythematosus).",
        "management_principles": "There is no standardized treatment, but management is generally aimed at stroke prevention. First-line therapies include antiplatelet agents (e.g., aspirin) or anticoagulation in patients with documented antiphospholipid antibodies. In cases associated with autoimmune disease, immunomodulatory therapies may be added. In pregnant patients, low-dose aspirin and careful monitoring are recommended because both thrombotic risks and bleeding complications have to be balanced during pregnancy and lactation.",
        "option_analysis": "Option A, Sneddon disease (another name for Sneddon syndrome), is correct. No other options were provided, but the distinctive association of livedo reticularis with stroke in this syndrome is the key diagnostic clue.",
        "clinical_pearls": "1. Always consider Sneddon syndrome in a stroke patient with livedo reticularis. 2. Testing for antiphospholipid antibodies can help differentiate it from other vasculopathies. 3. Management revolves around stroke prevention and may differ if associated with autoimmune conditions.",
        "current_evidence": "Recent studies have emphasized the role of comprehensive autoimmune work\u2010up in patients with unexplained strokes and skin findings. Current expert opinion supports early initiation of antiplatelet therapy and, when indicated, anticoagulation. Ongoing research is evaluating the efficacy of various immunomodulatory agents in patients with an underlying autoimmune component."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993116",
    "fields": {
      "question_number": "44",
      "question_text": "Patient came with right side weakness; CT showed Lt BG Hg with 3mm midline shift, what you will do?",
      "options": {
        "A": "Craniotomy",
        "B": "give LMWH"
      },
      "correct_answer": "Conservative management",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This case describes a hypertensive intracerebral hemorrhage (ICH) in the left basal ganglia, which is causing contralateral (right-sided) weakness. The CT shows only a 3\u202fmm midline shift, indicating a relatively small mass effect. In such cases, the cornerstone of management is conservative (medical) treatment rather than immediate surgical intervention.",
        "pathophysiology": "Hypertensive ICH is typically due to chronic high blood pressure causing rupture of small lenticulostriate arteries. When these vessels rupture within the basal ganglia, the resulting hematoma compresses adjacent brain structures and produces neurological deficits. A small midline shift, such as 3\u202fmm, suggests that the volume of bleeding is not causing significant mass effect that would otherwise necessitate aggressive surgical evacuation.",
        "clinical_correlation": "Patients with basal ganglia hemorrhages often present with contralateral motor deficits, like right-sided weakness when the bleed is on the left. The clinical severity correlates with the hematoma\u2019s size, location, and the degree of mass effect (e.g., midline shift). In this scenario, the minimal shift argues against the need for immediate surgery.",
        "diagnostic_approach": "CT imaging is the gold standard for differentiating hemorrhagic from ischemic stroke. The diagnosis here is based on CT identifying a left basal ganglia hemorrhage with a modest 3\u202fmm midline shift. Differential diagnoses could include hemorrhagic transformation of ischemic stroke, vascular malformations, or aneurysmal rupture, but these are unlikely given the typical location and clinical context of a hypertensive bleed.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on etiology (hypertensive, amyloid angiopathy, vascular malformations), location (lobar, deep structures like basal ganglia, thalamus), and clinical severity. The basal ganglia hemorrhage is a subtype of deep hypertensive ICH. The American Heart Association/American Stroke Association (AHA/ASA) guidelines categorize ICH by volume, location, and presence of mass effect to guide management. This classification aids in prognostication and therapeutic decisions, distinguishing those requiring surgical intervention from those managed conservatively.",
        "classification_and_nosology": "Intracerebral hemorrhages are classified as either primary (most often due to hypertensive vasculopathy) or secondary (due to coagulopathy, vascular malformations, neoplasms, etc.). A basal ganglia hemorrhage is a classic example of a primary hypertensive hemorrhage. Severity is further stratified by hematoma volume and the extent of midline shift.",
        "management_principles": "Current guidelines advocate for conservative management for deep-seated ICH with minimal mass effect. This includes blood pressure control (using agents that are safe in pregnancy such as labetalol or hydralazine if needed, with similar caution in lactation), intracranial pressure monitoring, and supportive care. Surgical intervention (e.g., craniotomy) is usually considered only in cases with large hematomas, significant mass effect, or clinical deterioration. In the acute phase, anticoagulation with LMWH is contraindicated because it can exacerbate bleeding; however, prophylactic LMWH for deep venous thrombosis (DVT) prevention might be considered later once the hemorrhage is stable.",
        "option_analysis": "Option A (Craniotomy) would be appropriate only if there were a large hematoma causing significant mass effect or if the patient\u2019s neurological status was worsening. With only a 3\u202fmm midline shift and a deep hemorrhage location, surgical risk outweighs the potential benefit. Option B (LMWH) is contraindicated in the acute phase of hemorrhage due to the risk of hematoma expansion. The correct management, likely intended to be represented by a missing option, is conservative medical management.",
        "clinical_pearls": "\u2022 Deep intracerebral hemorrhages, especially those in the basal ganglia, are mostly managed medically unless there is evidence of significant mass effect or neurological deterioration. \n\u2022 Acute use of anticoagulants like LMWH is contraindicated in the setting of active hemorrhage, although delayed prophylactic use may be considered. \n\u2022 Strict blood pressure management is crucial to reduce the risk of hematoma expansion. \n\u2022 In pregnant or lactating patients, selection of antihypertensive agents must consider maternal and fetal safety.",
        "current_evidence": "Recent studies and guidelines, including insights from the STICH trials, indicate that early surgical evacuation does not provide significant benefits for small deep hemorrhages with minimal midline shift. Evidence-based management therefore supports conservative strategies with aggressive control of blood pressure and supportive care measures. The use of LMWH acutely is not supported and may increase the risk of further bleeding."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993117",
    "fields": {
      "question_number": "45",
      "question_text": "Pregnant lady had headache her CT showed ICH, what is the treatment",
      "options": {
        "A": "start Heparin",
        "B": "Warfarin"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In pregnant patients, headache with CT findings of intracerebral hemorrhage (ICH) may represent a hemorrhagic venous infarct from cerebral venous sinus thrombosis (CVST). Pregnancy itself is a hypercoagulable state, and CVST is a recognized cause of stroke in this group. Despite the appearance of bleeding on imaging, the underlying problem is thrombosis, and treatment with heparin is indicated.",
        "pathophysiology": "CVST involves thrombosis within the cerebral venous sinuses, impairing venous drainage. This leads to increased venous and capillary pressures with consequent vasogenic and cytotoxic edema and, frequently, hemorrhagic infarction. Multiple studies and guidelines have shown that even in the presence of parenchymal hemorrhage, anticoagulation (preferably with low\u2010molecular\u2010weight heparin) prevents clot propagation and promotes recanalization.",
        "clinical_correlation": "A pregnant woman presenting with headache and neurological findings may be misinterpreted as having a primary arterial hemorrhage. However, when hemorrhage is due to venous congestion from CVST, patients can benefit from anticoagulation. Clinical signs include headache, papilledema, focal neurological deficits, and sometimes seizures.",
        "diagnostic_approach": "The initial evaluation often includes a non\u2011contrast CT scan, where CVST may appear as a hemorrhagic lesion. Confirmation requires CT venography or MR venography. Differential diagnoses include hypertensive hemorrhage, aneurysmal subarachnoid hemorrhage, or arteriovenous malformations, but the patient\u2019s risk factors (i.e., pregnancy) help point toward CVST.",
        "classification_and_neurology": "Intracerebral hemorrhage is classified as a subtype of hemorrhagic stroke within the broader cerebrovascular disease category. The American Heart Association/American Stroke Association (AHA/ASA) stroke classification system categorizes strokes into ischemic and hemorrhagic types, with ICH further subclassified by etiology (hypertensive, amyloid angiopathy, vascular malformations, coagulopathy-related). Pregnancy-associated ICH is recognized as a distinct clinical scenario due to unique pathophysiological and management considerations. Nosologically, pregnancy-related cerebrovascular events include ischemic stroke, ICH, cerebral venous sinus thrombosis, and reversible cerebral vasoconstriction syndrome. Classification systems have evolved to incorporate pregnancy as a modifying factor influencing prognosis and treatment.",
        "classification_and_nosology": "CVST is categorized as a type of stroke that is distinct from the common arterial strokes. It\u2019s considered under the spectrum of cerebrovascular diseases associated with hypercoagulable states such as pregnancy, puerperium, and thrombophilic disorders.",
        "management_principles": "The current standard is to initiate anticoagulation despite hemorrhagic changes. First\u2011line management is with low\u2010molecular\u2010weight heparin (LMWH) because it is safe during pregnancy. Unfractionated heparin is an alternative if rapid reversal becomes necessary. Warfarin is contraindicated due to teratogenic risk. Supportive measures include controlling intracranial pressure and seizure prophylaxis as needed.",
        "option_analysis": "Option A (Heparin) is correct because anticoagulation (LMWH or unfractionated heparin) is the standard treatment for CVST in pregnancy. Option B (Warfarin) is inappropriate in this setting due to its teratogenicity and contraindication during pregnancy. Options C and D are not provided.",
        "clinical_pearls": "1. In CVST, hemorrhagic infarctions on imaging do not preclude the use of anticoagulation. 2. Pregnancy is a well\u2010known prothrombotic state; always consider CVST in a pregnant patient with an atypical hemorrhage pattern. 3. LMWH is the preferred treatment given its safety profile in pregnancy.",
        "current_evidence": "The 2022 American Heart Association/American Stroke Association Guidelines for the Management of Spontaneous Intracerebral Hemorrhage state: \u201cAvoid anticoagulation in the acute management of ICH due to the risk of hematoma expansion and poor outcomes. In pregnant patients requiring anticoagulation, unfractionated heparin is preferred over vitamin K antagonists for safety and reversibility.\u201d (Hemphill et al., Stroke, 2022). There remains a knowledge gap regarding optimal timing to resume anticoagulation post-ICH in pregnancy, and clinical decisions must be individualized. Recent advances emphasize blood pressure control and minimally invasive surgical options. Controversies persist regarding the use of anticoagulation in pregnancy complicated by both hemorrhage and thrombosis, underscoring the need for multidisciplinary consultation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993118",
    "fields": {
      "question_number": "46",
      "question_text": "Patient with multiple Hg in the brain he was on aspirin; lips showed petechiae, what you will do?",
      "options": {
        "A": "pulmonary CT Angoi"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "This scenario describes a patient on chronic aspirin therapy who presents with multiple hemorrhagic lesions in the brain along with mucocutaneous bleeding (petechiae on the lips). Aspirin irreversibly inhibits platelet cyclooxygenase, reducing thromboxane A2 production and impairing platelet aggregation; in a susceptible patient this may precipitate spontaneous bleeding. Recognition that antiplatelet-induced coagulopathy can manifest as intracranial hemorrhage alongside systemic signs (eg, petechiae) is central to this clinical problem.",
        "pathophysiology": "Aspirin\u2019s antiplatelet effect leads to permanent inhibition of platelet function. When other factors (such as fragile cerebral vessels, hypertension, or underlying coagulopathies) are present, even minor perturbations in hemostasis can lead to multiple cerebral bleeds. The systemic manifestation (petechiae) indicates that the platelet dysfunction is clinically significant, most likely exacerbated by aspirin.",
        "clinical_correlation": "Patients on aspirin, even when prescribed for cardiovascular prophylaxis, are at risk for bleeding complications. Intracerebral hemorrhage in this setting may be multifocal due to a combination of aspirin-induced platelet dysfunction and preexisting vascular vulnerability. Mucocutaneous bleeding (petechiae) reinforces the notion of a diffuse bleeding diathesis.",
        "diagnostic_approach": "Evaluation should begin with a focused neurological examination and brain imaging (CT scan to determine the extent and location of hemorrhages) along with laboratory studies including complete blood count, coagulation profile (PT, aPTT), and platelet function tests. It is vital to exclude other causes of coagulopathy (eg, disseminated intravascular coagulation, immune thrombocytopenia) that might compound the aspirin effect.",
        "classification_and_neurology": "Intracerebral hemorrhages are classified based on etiology, location, and number. Etiologically, hemorrhages are divided into hypertensive, amyloid angiopathy-related, coagulopathy-related, vascular malformation-associated, hemorrhagic transformation of ischemic strokes, and embolic hemorrhages. Multiple hemorrhages suggest embolic or systemic causes rather than isolated hypertensive hemorrhage. The nosology of hemorrhagic strokes is part of the broader cerebrovascular disease classification system endorsed by the American Heart Association/American Stroke Association (AHA/ASA). The classification has evolved to emphasize etiology and pathophysiology for guiding management. Controversies remain in distinguishing cerebral microbleeds from macrohemorrhages on imaging and in the optimal classification of hemorrhagic transformation in ischemic stroke.",
        "classification_and_nosology": "This case falls under the category of hemorrhagic stroke secondary to antiplatelet (aspirin) use. It is distinct from hemorrhagic transformation of ischemic infarcts or vascular malformations, although those conditions must be excluded in the differential diagnosis.",
        "management_principles": "The cornerstone of management is immediate discontinuation of aspirin and supportive care. Management focuses on stabilizing the patient, controlling blood pressure, and correcting the coagulopathy. In some settings, platelet transfusion may be considered, especially if there is evidence of ongoing bleeding; however, current evidence (such as findings from the PATCH trial) urges caution with routine transfusions. In any case, decision-making must be individualized. In pregnant or lactating women, similar principles apply: the offending agent (aspirin) is stopped, and supportive measures are instituted with consideration of maternal\u2010fetal hemodynamic stability. Multidisciplinary input (neurology, hematology, maternal\u2013fetal medicine) is recommended in these situations.",
        "option_analysis": "Option A, which suggests a pulmonary CT angiogram, is irrelevant in this scenario because the primary problem is intracranial bleeding in the context of antiplatelet therapy rather than a suspected pulmonary embolism. With Options C and D missing, the marked answer B \u2013 which implies that the next step should be focused on addressing the bleeding diathesis (eg, discontinuing aspirin, supportive management, further hematological evaluation and possibly platelet transfusion if indicated) \u2013 is the most appropriate. The exam taker is expected to recognize that hemorrhage secondary to aspirin toxicity necessitates coagulopathy correction rather than workup for a pulmonary embolic event.",
        "clinical_pearls": "\u2022 Always consider medication effects \u2013 even prophylactic dosages of aspirin can precipitate bleeding complications in susceptible individuals.  \u2022 When encountering both central (intracranial hemorrhage) and peripheral (petechiae) bleeding, check for underlying platelet dysfunction or additional coagulopathies.  \u2022 In selecting imaging studies, ensure they address the clinical problem at hand \u2013 a pulmonary CT angiogram is not indicated here.  \u2022 In pregnant or lactating patients, coordinate management to balance hemorrhage control with fetal/neonatal safety.",
        "current_evidence": "Recent studies and guidelines emphasize a prompt evaluation of antithrombotic-related hemorrhage. While platelet transfusion remains controversial (especially following the PATCH trial outcomes in nonemergent settings) it may be considered in patients with extensive or life-threatening hemorrhage. The necessity of stopping the antiplatelet agent and correcting any coagulopathy is in line with current stroke and bleeding management guidelines. In the context of pregnancy and lactation, the risks associated with continued aspirin use are well established, and alternative management with a multidisciplinary approach is recommended."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993119",
    "fields": {
      "question_number": "47",
      "question_text": "4 years old sickle cell disease patient had stroke with significant MCA stenosis, what will determine the stroke risk:",
      "options": {
        "A": "Hb Electrophoresis",
        "B": "Transcranial doppler"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2021,
      "explanation_sections": {
        "conceptual_foundation": "In children with sickle cell disease (SCD), stroke risk is closely linked to cerebrovascular pathology, especially in the middle cerebral artery (MCA). Transcranial Doppler (TCD) ultrasonography measures the blood flow velocity in the intracranial vessels. Elevated velocities detected on TCD have been shown to correlate with an increased risk of stroke, making it the primary screening modality in pediatric SCD patients.",
        "pathophysiology": "SCD leads to chronic hemolysis and vaso-occlusion, resulting in endothelial damage and progressive stenosis of cerebral vessels, most notably the MCA. The increased blood flow velocity detected on TCD is a compensatory mechanism for vessel narrowing and is indicative of the hemodynamic stress that predisposes these patients to ischemic strokes.",
        "clinical_correlation": "Children with SCD, particularly between the ages of 2 and 16, are at high risk for stroke. Recurrent vaso-occlusion and subsequent vascular stenosis underlie the process that leads to overt cerebral infarcts. Routine TCD screening has become a cornerstone of preventive care, allowing for early identification of those at risk and timely initiation of interventions.",
        "diagnostic_approach": "The diagnostic strategy for stroke risk in pediatric SCD includes periodic TCD assessments, as standardized by the STOP (Stroke Prevention Trial in Sickle Cell Anemia) guidelines. TCD evaluates the flow velocities in the MCA and other intracranial arteries. Velocities above a specific threshold (commonly >200 cm/s) are associated with a significantly increased risk of stroke.",
        "classification_and_neurology": "Stroke in sickle cell disease falls under the broader category of pediatric ischemic stroke secondary to hematologic disorders. According to the International Pediatric Stroke Study classification, strokes are divided by etiology, with SCD-related strokes classified as arteriopathy-associated ischemic strokes. The American Society of Hematology (ASH) guidelines recognize SCD as a high-risk condition for ischemic stroke due to large vessel vasculopathy. The Transcranial Doppler Stroke Prevention Trial (STOP) classification stratifies TCD velocities into normal (<170 cm/s), conditional (170-199 cm/s), and abnormal (\u2265200 cm/s) to guide management. This classification system has become standard for stroke risk stratification in SCD, superseding reliance on hemoglobin subtype alone. Controversies remain regarding the optimal frequency and thresholds for TCD screening, but consensus supports its central role in classification and risk assessment.",
        "classification_and_nosology": "Strokes in SCD patients are classified as either overt or silent. The use of TCD helps identify patients with abnormal hemodynamics who are at high risk for overt stroke. These findings place the patient in a high-risk category for cerebrovascular complications, which is a recognized clinical subset within SCD-related vasculopathy.",
        "management_principles": "Current guidelines recommend regular TCD screening in children with SCD to identify elevated flow velocities and thereby stratify stroke risk. Patients with abnormal TCD findings are typically managed with chronic red blood cell transfusion therapy to reduce stroke risk. Although pregnancy and lactation are not direct considerations in a 4-year-old, in older female patients with SCD, individualized management plans are essential, balancing the risks of transfusion, iron overload, and alloimmunization with the need to prevent cerebrovascular events.",
        "option_analysis": "Option A (Hb Electrophoresis) is used to confirm the diagnosis and characterize the type of hemoglobinopathy, but it does not correlate with current stroke risk. Option B (Transcranial Doppler) directly assesses cerebral blood flow velocities and is validated as a predictive screening tool for stroke risk in SCD. Options C and D are omitted in this question.",
        "clinical_pearls": "Early identification of elevated TCD velocities in children with SCD allows for proactive management with therapies such as chronic transfusions, significantly reducing the risk of stroke. Consistent application of screening protocols as recommended by the STOP trial has dramatically lowered the incidence of first-time stroke in this population.",
        "current_evidence": "Recent studies and guidelines continue to endorse TCD as the standard screening tool for stroke risk in pediatric SCD. Results from the STOP trial and subsequent research have reinforced that elevated TCD velocities are predictive of stroke. Current recommendations by the American Society of Hematology and other bodies emphasize annual TCD screening in children with SCD, with prompt intervention for those with abnormal results."
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
