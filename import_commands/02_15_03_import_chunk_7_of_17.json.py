
# Import batch 3 of 3 from chunk_7_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993200",
    "fields": {
      "question_number": "283",
      "question_text": "Intracranial MCA severe stenosis what next",
      "options": {
        "A": "(DAPT) is correct because the SAMMPRIS trial demonstrated that using both aspirin and clopidogrel reduces recurrent stroke risk in severe intracranial stenosis. Other alternatives like single antiplatelet therapy, anticoagulation, or immediate endovascular procedures have either not shown superior benefits or carry higher procedural risks."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "This case involves a patient with severe intracranial stenosis of the MCA, a high\u2010risk condition for recurrent ischemic events. The aim is to stabilize the atherosclerotic plaque and prevent embolization, making antiplatelet therapy the mainstay of management.",
        "pathophysiology": "Severe intracranial stenosis is most commonly due to atherosclerotic disease. The culprit lesion leads to endothelial injury and turbulent blood flow, promoting platelet activation and microembolization. Dual antiplatelet therapy (DAPT)\u2014combining aspirin\u2019s irreversible COX inhibition with clopidogrel\u2019s blockade of the ADP receptor\u2014addresses two different pathways in platelet aggregation, as demonstrated in the SAMMPRIS trial.",
        "clinical_correlation": "Clinically, patients might present with transient ischemic attacks or strokes confined to the vascular territory supplied by the affected MCA. The risk of subsequent stroke is high if the stenosis remains untreated, which makes early aggressive management essential.",
        "diagnostic_approach": "Imaging modalities like CTA, MRA, or digital subtraction angiography (DSA) are used to confirm the degree of stenosis. Differential diagnoses include extracranial carotid stenosis, vasculitis, or other intracranial arteriopathies. Noninvasive vascular imaging usually helps differentiate these conditions.",
        "classification_and_neurology": "Intracranial arterial stenosis is classified within the broader category of large artery atherosclerotic cerebrovascular disease, as per the TOAST (Trial of ORG 10172 in Acute Stroke Treatment) classification system. This system categorizes ischemic strokes based on etiology: large artery atherosclerosis, cardioembolism, small vessel occlusion, other determined etiology, and undetermined etiology. Intracranial MCA stenosis falls under large artery atherosclerosis. Further subclassification can be based on the degree of stenosis (mild <50%, moderate 50-69%, severe \u226570%), and the presence of symptoms (symptomatic vs. asymptomatic). The WASID (Warfarin-Aspirin Symptomatic Intracranial Disease) trial criteria are often used to define severity. There has been debate regarding optimal classification, but consensus supports using vascular imaging and clinical correlation to guide management. Understanding this nosology aids in prognosis and therapeutic decision-making.",
        "classification_and_nosology": "This condition falls under intracranial atherosclerotic disease, a subset of ischemic stroke etiologies categorized under large artery atherosclerosis. Severity is typically quantified by the percentage of luminal narrowing (often >70% being high risk).",
        "management_principles": "According to current guidelines and the SAMMPRIS trial, the first-line management for symptomatic severe intracranial stenosis is aggressive medical therapy. DAPT (aspirin plus clopidogrel) should be initiated\u2014commonly for 90 days\u2014along with risk factor modification (blood pressure, lipids, glycemic control). Endovascular options (such as stenting) are reserved for cases refractory to medical management. In pregnancy or lactation, low-dose aspirin may be used safely; however, clopidogrel\u2019s safety profile is not as well established. In such scenarios, the risks and benefits should be weighed carefully, often involving a multidisciplinary discussion.",
        "option_analysis": "Option a (DAPT) is correct because the SAMMPRIS trial demonstrated that using both aspirin and clopidogrel reduces recurrent stroke risk in severe intracranial stenosis. Other alternatives like single antiplatelet therapy, anticoagulation, or immediate endovascular procedures have either not shown superior benefits or carry higher procedural risks.",
        "clinical_pearls": "1. The SAMMPRIS trial firmly supports DAPT in the acute management of symptomatic high-grade intracranial stenosis. 2. Aggressive medical management and risk factor modification remain the cornerstone of therapy. 3. Noninvasive imaging is key to an accurate diagnosis and subsequent management planning.",
        "current_evidence": "Recent guidelines continue to reinforce that for symptomatic intracranial atherosclerotic disease, DAPT for a period (commonly 90 days) along with intensive risk factor management is the optimal first-line approach. Endovascular intervention is reserved for selected cases when medical management fails."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993201",
    "fields": {
      "question_number": "284",
      "question_text": "Patient with ESRD Scenario with pic showing rt superficial borderzone infarction at MCA/ACA territory asking about next investigation",
      "options": {
        "A": "(Brain CTA) is acceptable as the next investigation if it includes imaging of the neck vessels. It is noninvasive and provides reliable information about both intracranial and extracranial vessels. Option b (Conventional angiography) is more invasive and carries a higher risk of complications including stroke, arterial injury, and contrast nephropathy, particularly in ESRD; hence, it is reserved for cases where noninvasive tests are inconclusive or for planning interventional procedures."
      },
      "correct_answer": "a",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "In patients with watershed (borderzone) infarcts, it is important to evaluate the entire cerebrovascular axis as these infarcts can be related to either hemodynamic compromise or proximal large vessel disease. Noninvasive vascular imaging is pivotal in clarifying the cause.",
        "pathophysiology": "Borderzone or watershed infarcts occur at the junctions between vascular territories, often due to hypoperfusion or embolic events affecting both intracranial and extracranial vessels. In patients with ESRD, who may have vascular calcifications and concomitant atherosclerosis, assessing both extra- and intracranial vasculature is crucial.",
        "clinical_correlation": "In the setting of ESRD and borderzone infarcts, the patient may have subtle neurological deficits. Given the association with renal disease, there is often extensive vascular disease, making comprehensive vascular imaging essential for further management.",
        "diagnostic_approach": "A CT angiography (CTA) that ideally includes both the intracranial and neck vessels is preferred. Although the option provided mentions brain CTA (which might imply that neck vessels are included as per standard protocol), it is critical to assess for extracranial carotid stenosis as well. Differential diagnoses include embolic stroke from a cardiac source, vasculitis, or internal carotid occlusion.",
        "classification_and_neurology": "Borderzone infarctions are classified under ischemic stroke subtypes in the TOAST (Trial of Org 10172 in Acute Stroke Treatment) classification as 'large artery atherosclerosis' or 'hemodynamic stroke' depending on the etiology. Watershed infarcts can be cortical (between MCA and ACA or MCA and PCA territories) or internal (between deep and superficial MCA territories). This classification system emphasizes the importance of vascular imaging and clinical context to differentiate stroke mechanisms. Alternative classification systems like CCS (Causative Classification of Stroke System) also incorporate imaging and clinical features. Understanding these classifications helps tailor investigations and treatment strategies. The consensus is that borderzone infarcts often indicate hemodynamic compromise, necessitating vascular imaging focused on extracranial and intracranial arteries.",
        "classification_and_nosology": "Stroke subtypes based on vascular territory include watershed infarcts, which fall under the classification of ischemic strokes resulting from either systemic hypoperfusion or localized large vessel disease.",
        "management_principles": "Once vascular imaging is performed, management involves addressing underlying etiologies. First-line investigations include noninvasive CTA (with both brain and neck imaging) due to its rapidity and lower risk. In patients with ESRD, contrast administration must be judicious; however, in those on dialysis the risk of further renal injury is less of a concern. In scenarios involving pregnancy, alternative imaging modalities or minimized contrast protocols should be considered to reduce fetal exposure.",
        "option_analysis": "Option a (Brain CTA) is acceptable as the next investigation if it includes imaging of the neck vessels. It is noninvasive and provides reliable information about both intracranial and extracranial vessels. Option b (Conventional angiography) is more invasive and carries a higher risk of complications including stroke, arterial injury, and contrast nephropathy, particularly in ESRD; hence, it is reserved for cases where noninvasive tests are inconclusive or for planning interventional procedures.",
        "clinical_pearls": "1. Watershed infarcts should prompt a full evaluation of both intra- and extracranial vasculature. 2. In ESRD patients, the use of CTA remains acceptable due to the limited concern over contrast-induced nephropathy in end-stage disease. 3. Noninvasive imaging is the preferred first step in vascular evaluation.",
        "current_evidence": "Recent studies endorse the use of comprehensive CTA as an effective, rapid, and safe tool for evaluating patients with suspected cerebrovascular disease. In patients with ESRD, modifications in contrast use are considered, but the overall imaging strategy remains the same."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993202",
    "fields": {
      "question_number": "285",
      "question_text": "Minor stroke NIHSS 3 (left side decrease sensation, mild facial weakness) within the window what\u2019s next",
      "options": {
        "A": "(DAPT) is incorrect as sole acute treatment because while it reduces recurrent events, it does not actively lyse the clot. Option b (tPA) is correct because clot dissolution is essential for reperfusion in the hyperacute phase of ischemic stroke. Option c (Aspirin alone) is insufficient for acute reperfusion therapy; it is used more for secondary prevention post"
      },
      "correct_answer": "b",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part I",
      "exam_year": 2022,
      "explanation_sections": {
        "conceptual_foundation": "For patients presenting with a minor stroke (NIHSS 3) within the treatment window, the crucial decision is whether to use IV thrombolysis to restore perfusion. Even minor deficits can be disabling, and timely reperfusion is key.",
        "pathophysiology": "Ischemic stroke results from occlusion of cerebral arteries, leading to infarction of brain tissue downstream. Thrombolytic therapy with tPA initiates enzymatic fibrinolysis of the clot, thereby restoring blood flow and potentially minimizing infarct size if administered early in the time window.",
        "clinical_correlation": "Patients with minor stroke symptoms, like decreased sensation and mild facial weakness, may still experience significant disability. Early intervention with IV tPA can improve outcomes by re-establishing perfusion before irreversible damage ensues.",
        "diagnostic_approach": "The diagnosis of an ischemic stroke is primarily based on clinical assessment and neuroimaging (typically noncontrast CT) to rule out hemorrhage. Differential diagnoses include transient ischemic attack (TIA), migraine with aura, or seizure-related deficits, but imaging along with clinical findings usually clarifies the diagnosis.",
        "classification_and_neurology": "Ischemic stroke is classified etiologically by systems such as the TOAST criteria into large artery atherosclerosis, cardioembolism, small vessel occlusion (lacunar), other determined, and undetermined causes. Minor stroke is a clinical severity classification rather than a distinct subtype. The NIHSS provides a standardized measure of severity, guiding therapeutic decisions. Acute ischemic stroke management protocols stratify patients based on time from onset and stroke severity. The classification of stroke severity (minor, moderate, severe) influences eligibility for reperfusion therapies. Current consensus supports thrombolysis for eligible patients regardless of minor deficits, given evidence of benefit. Controversies exist about treating very mild or rapidly improving symptoms, but guidelines emphasize individualized assessment.",
        "classification_and_nosology": "Minor strokes, defined by low NIHSS scores, are categorized under ischemic strokes. Despite a seemingly low score, the deficits can be clinically disabling, making timely reperfusion therapy vital.",
        "management_principles": "For eligible patients presenting within 4.5 hours from symptom onset, IV thrombolysis with tPA is considered first-line therapy. Although DAPT (aspirin plus clopidogrel) has proven benefits in secondary prevention (as per the CHANCE and POINT trials), it does not have the reperfusion action required in the hyperacute phase. In the context of pregnancy or lactation, the use of tPA demands a rigorous risk-benefit assessment. Although tPA is not an absolute contraindication during pregnancy, caution is advised due to the potential risk of maternal and fetal hemorrhage; multidisciplinary consultation is recommended.",
        "option_analysis": "Option a (DAPT) is incorrect as sole acute treatment because while it reduces recurrent events, it does not actively lyse the clot. Option b (tPA) is correct because clot dissolution is essential for reperfusion in the hyperacute phase of ischemic stroke. Option c (Aspirin alone) is insufficient for acute reperfusion therapy; it is used more for secondary prevention post-thrombolysis or when tPA is contraindicated.",
        "clinical_pearls": "1. Even minor strokes with low NIHSS scores can be disabling; timely tPA administration is crucial. 2. The therapeutic time window for tPA is 4.5 hours from symptom onset. 3. DAPT is useful for secondary prevention, not as a replacement for acute thrombolytic therapy.",
        "current_evidence": "Recent guidelines from the American Heart Association/American Stroke Association continue to recommend IV tPA within the 4.5-hour window for eligible patients, even for minor strokes if deficits are considered disabling. Multiple trials have consolidated the role of thrombolysis in acute management over antiplatelet-only strategies."
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
