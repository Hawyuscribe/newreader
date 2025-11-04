
# Import batch 3 of 3 from chunk_10_of_17.json
from django.db import transaction
from mcq.models import MCQ

# MCQ data for this batch
fixture_data = [
  {
    "model": "mcq.mcq",
    "pk": "99993330",
    "fields": {
      "question_number": "359",
      "question_text": "a woman who was being investigated for stroke, was found to have high titer of anti-beta II glycoprotein AB, and anticardiolipin AB. She was diagnosed with antiphospholipid syndrome. she has a history of a prior LL DVT, a small PFO was also found. what is the appropriate management?",
      "options": {
        "A": "DAPT",
        "B": "warfarin",
        "C": "closure of PFO",
        "D": "ASA"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Antiphospholipid syndrome (APS) is an autoimmune disorder characterized by the formation of antibodies against phospholipid-binding proteins (notably anticardiolipin and anti-beta2 glycoprotein I). These antibodies predispose patients to both arterial and venous thrombotic events. In this case, the patient\u2019s history, including a prior lower limb DVT and a stroke, is consistent with thrombotic manifestations of APS.",
        "pathophysiology": "In APS, the autoantibodies induce a hypercoagulable state by activating endothelial cells, platelets, and complement pathways, while interfering with the natural anticoagulant mechanisms. This results in an increased risk for clot formation in both the arterial and venous systems. The presence of high titers of anticardiolipin and anti-beta2 glycoprotein I antibodies confirms the autoimmune-mediated coagulation dysregulation.",
        "clinical_correlation": "Patients with APS frequently present with recurrent thrombotic events such as DVTs and cerebrovascular accidents (strokes), as seen in this patient. Although a small patent foramen ovale (PFO) was incidentally detected, the hypercoagulable state from APS is the primary concern, and the PFO does not change the management approach in this context.",
        "diagnostic_approach": "The diagnosis of APS is based on the revised Sapporo criteria (or Sydney criteria), which require: 1) a clinical history of vascular thrombosis and/or pregnancy morbidity, and 2) laboratory confirmation of antiphospholipid antibodies (anticardiolipin, anti-beta2 glycoprotein I, or lupus anticoagulant) on two or more occasions at least 12 weeks apart. Differential diagnoses include other hypercoagulable disorders such as inherited thrombophilias, malignancy-related thrombosis, and other autoimmune disorders like systemic lupus erythematosus.",
        "classification_and_nosology": "APS is classified into primary APS (occurring in isolation) and secondary APS (associated with other autoimmune conditions, typically SLE). In this case, with no other reported autoimmune symptoms, the patient likely has primary APS.",
        "management_principles": "Long-term anticoagulation is the cornerstone of management in APS patients with prior thrombotic events. Warfarin is the anticoagulant of choice in nonpregnant patients, with a target INR of 2-3 under standard circumstances. For women who are pregnant or lactating, warfarin is contraindicated due to its teratogenicity, and the recommended management is with low molecular weight heparin (LMWH) combined with low-dose aspirin.",
        "option_analysis": "Option A (DAPT) and Option D (ASA) do not provide sufficient anticoagulation in APS. Option C (closure of PFO) is not the primary treatment for preventing thromboembolic events in APS, since the hypercoagulability is the primary driver of thrombotic events rather than embolism through a PFO alone. Therefore, Option B (warfarin) is the best management choice for this patient.",
        "clinical_pearls": "1. In APS, always consider long-term anticoagulation as the patient is at high risk for recurrent thrombotic events. 2. Warfarin is the preferred treatment for nonpregnant patients; however, in pregnancy, LMWH with low-dose aspirin is advised. 3. Incidentally found PFOs in the setting of APS do not warrant closure unless they are clearly contributing to embolic events in the absence of a hypercoagulable state.",
        "current_evidence": "Recent guidelines and clinical evidence continue to advocate for the use of warfarin in patients with APS and documented thrombotic events to reduce the risk of recurrence. Studies have confirmed that maintaining an INR in the target range (typically 2-3) significantly lowers the risk of further thrombosis. In the event of pregnancy, current recommendations favor LMWH over warfarin due to the known teratogenic effects of the latter."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993331",
    "fields": {
      "question_number": "360",
      "question_text": "Scenario about dermatomyositis (they mentioned pt. With weakness and typical skin lesion, and cough) ??? (Not sure about details and choices) Which antibody:",
      "options": {
        "A": "Anti synthetase",
        "B": "Anti mda5",
        "C": "Anti SRP",
        "D": "ANTI TIF"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Dermatomyositis is an idiopathic inflammatory myopathy characterized by proximal muscle weakness and distinctive cutaneous findings such as heliotrope rash and Gottron papules. Its subtypes are partly defined by myositis\u2010specific antibodies, each correlating with different clinical patterns and systemic involvements.",
        "pathophysiology": "An autoimmune process leads to muscle fiber injury and a complement-mediated microangiopathy in the skin. Among the antibodies, the anti-synthetase group (most notably anti-Jo1) targets aminoacyl-tRNA synthetases, fostering an inflammatory cascade that can also involve the lungs and result in interstitial lung disease (ILD).",
        "clinical_correlation": "In this scenario, the patient presents with muscle weakness, a classic dermatomyositis skin eruption, and a cough. The presence of cough raises the suspicion for ILD, a well-described feature in patients with anti-synthetase syndrome.",
        "diagnostic_approach": "Evaluation involves a combination of clinical examination, serum creatine kinase levels, autoantibody panels (examining myositis-specific antibodies including anti-synthetase), electromyography, and often muscle biopsy. In patients with respiratory symptoms, chest imaging (e.g., high-resolution CT scan) is essential to screen for ILD.",
        "classification_and_nosology": "Dermatomyositis, one of the idiopathic inflammatory myopathies, is subclassified based on the associated autoantibodies. These include anti-synthetase antibodies (defining the anti-synthetase syndrome with ILD, arthritis, and mechanic\u2019s hands), anti-MDA5 (often linked with rapidly progressive ILD in clinically amyopathic DM), anti-SRP (associated with necrotizing myopathy), and anti-TIF1 (which carries a malignancy risk).",
        "management_principles": "The mainstay of management is high-dose corticosteroids along with additional immunosuppressive agents (such as methotrexate, azathioprine, or mycophenolate mofetil) to control muscle and lung inflammation. In cases with significant ILD, more aggressive immunomodulatory therapy may be warranted. For pregnant and lactating patients, corticosteroids remain the first-line treatment; however, agents such as methotrexate are contraindicated, so alternative therapies with better safety profiles in pregnancy must be chosen.",
        "option_analysis": "Option A (Anti-synthetase antibodies) is the best answer in this scenario. Although anti-MDA5 is also associated with ILD, it is more typically seen in clinically amyopathic dermatomyositis with minimal muscle weakness. Anti-SRP is characteristically linked to severe necrotizing myopathy without significant skin manifestations, and anti-TIF1 is more commonly associated with malignancy-related dermatomyositis rather than ILD. The combination of weakness, classic DM rash, and a cough (suggesting ILD) aligns best with an anti-synthetase antibody profile.",
        "clinical_pearls": "A cough in a patient with dermatomyositis mandates a thorough evaluation for interstitial lung disease. Identifying the specific autoantibody profile is crucial, as it influences both prognostication and selection of immunosuppressive therapy. Anti-synthetase syndrome, signified by the presence of antibodies such as anti-Jo1, often includes extramuscular manifestations like ILD, arthritis, and mechanic\u2019s hands.",
        "current_evidence": "Recent research and guidelines emphasize the importance of myositis-specific antibody testing to tailor immunosuppressive therapy. Early detection and management of ILD significantly improve outcomes, and treatment decisions should carefully incorporate patient factors, including pregnancy and lactation, to ensure safety and efficacy."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993332",
    "fields": {
      "question_number": "361",
      "question_text": "Stab wound with ulnar neuropathy what you will find in NCS after 5 days:",
      "options": {
        "A": "Decrease recruitment",
        "B": "Fibrillations",
        "C": "Insertional activity",
        "D": "Complex repetitive discharges"
      },
      "correct_answer": "C",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "After an acute nerve injury such as a stab wound to the ulnar nerve, the muscle fibers begin to show signs of denervation. However, the classical fibrillation potentials that are emblematic of denervation do not typically appear until 10\u201314 days post-injury. Instead, one of the earliest detectable abnormalities on needle electromyography (EMG) is increased insertional activity, which reflects the instability of the muscle membrane when denervated.",
        "pathophysiology": "Following a nerve injury, Wallerian degeneration ensues distal to the lesion. This process leads to impaired neuromuscular transmission and muscle membrane instability. The increased irritability of these denervated fibers results in abnormal electrical discharges upon insertion of the EMG needle. Fibrillation potentials and positive sharp waves, more specific markers of denervation, take time (typically 10\u201314 days) to develop as the full extent of axonal degeneration becomes evident.",
        "clinical_correlation": "In the setting of a ulnar nerve injury from a stab wound, patients can present with motor deficits (e.g., weakness in ulnar-innervated hand muscles) and sensory disturbances in the ulnar distribution. Early electrodiagnostic studies (around 5 days post-injury) help localize the lesion and estimate the timing of the nerve injury. The presence of increased insertional activity correlates with acute muscle fiber membrane instability secondary to denervation.",
        "diagnostic_approach": "The diagnostic evaluation of acute nerve injuries involves both nerve conduction studies (NCS) and needle EMG. While NCS can demonstrate features such as conduction block and reduced compound muscle action potentials, needle EMG is particularly useful in detecting early spontaneous activity. At 5 days post-injury, the key abnormality is increased insertional activity; fibrillation potentials typically emerge after 7\u201314 days. The differential includes distinguishing between neurapraxia (conduction block without axonal loss) and more severe axonotmesis or neurotmesis.",
        "classification_and_nosology": "Ulnar neuropathy is classified by the severity and type of nerve injury: neurapraxia (a transient conduction block with no axonal damage), axonotmesis (axonal damage with preservation of the connective tissue framework), or neurotmesis (complete disruption of the nerve). The electrodiagnostic findings combined with the clinical history and examination help classify the injury, which is important for prognosis and management.",
        "management_principles": "Management of acute ulnar neuropathy depends on the severity of the injury. Conservative management, including observation and physical therapy, may be appropriate for neurapraxia, while surgical intervention is considered in cases of axonotmesis or neurotmesis. Pregnancy and lactation considerations are critical; when surgical intervention is necessary, one should use anesthetic and surgical medications that are safe in pregnancy and lactation. In addition, non-teratogenic agents should be chosen and multidisciplinary consultation may be warranted to balance maternal and fetal risks.",
        "option_analysis": "Option A (Decrease in recruitment) refers to a reduction of motor unit activation on voluntary effort and is less sensitive in the early phase of denervation. Option B (Fibrillations) indeed represents classic signs of denervation but generally are not seen until around 10\u201314 days after the injury, making them less likely at 5 days. Option D (Complex repetitive discharges) are typically associated with chronic changes or reinnervation phenomena. Option C (Insertional activity) is the early abnormal finding on needle EMG attributable to increased muscle fiber irritability shortly after denervation, making it the correct answer.",
        "clinical_pearls": "Timing is crucial when interpreting electrodiagnostic studies in nerve injuries. Fibrillation potentials are a late sign (typically emerging after 1\u20132 weeks), whereas increased insertional activity is one of the earliest indicators of denervation. Recognizing the timeline of these findings is essential for accurate diagnosis.",
        "current_evidence": "Recent neuromuscular and electrodiagnostic literature confirms that the earliest EMG abnormality in acute nerve injury, such as an ulnar neuropathy secondary to a stab wound, is increased insertional activity. This evidence underscores the importance of performing serial studies if initial exams are inconclusive, particularly in the context of early post-trauma evaluation."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993333",
    "fields": {
      "question_number": "362",
      "question_text": "Scenario about essential myoclonus relieved by alcohol asking about dx.",
      "options": {
        "A": "Cortical myoclonus",
        "B": "Essential myoclonus",
        "C": "Physiological myoclonus",
        "D": "Epileptic myoclonus"
      },
      "correct_answer": "B",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "Essential myoclonus is an idiopathic movement disorder in which the patient exhibits involuntary, brief, shock\u2010like muscle contractions (myoclonic jerks) in the absence of other neurological abnormalities. Although the term \u2018essential tremor\u2019 is more widely recognized, there is a subset of patients who experience predominantly myoclonic jerks that can be termed as 'essential' if no secondary cause is identified.",
        "pathophysiology": "The underlying mechanism is thought to involve abnormal hyperexcitability in the relevant motor circuits\u2014often at the level of the sensorimotor cortex or subcortical structures\u2014with a disturbance in inhibitory neurotransmission. Unlike epileptic or cortical myoclonus (where discrete electrophysiologic abnormalities and often EEG correlates are noted), essential myoclonus lacks any structural lesion and is presumed to be due to a dysfunction in motor regulation. Although not as well characterized as essential tremor, some patients report improvement with alcohol, which is believed to temporarily modulate GABA\u2010ergic tone.",
        "clinical_correlation": "Patients typically present with isolated myoclonic jerks that may be action-induced or present at rest. A notable clinical feature is the improvement of symptoms with the intake of alcohol, which also serves as a supportive clue in the diagnosis. Importantly, these patients do not exhibit other neurological deficits, and their workup (including imaging and routine EEG) is usually unremarkable.",
        "diagnostic_approach": "Workup generally includes a thorough clinical examination, neurophysiological studies such as EMG (which can help differentiate among different types of myoclonus), and sometimes EEG for ruling out epileptic phenomena. Differential diagnoses include cortical or epileptic myoclonus (which are associated with abnormal EEG changes), physiological myoclonus (a normal variant seen in sleep or benign fasciculations), and secondary causes of myoclonus (such as metabolic or toxic states).",
        "classification_and_nosology": "Myoclonus can be classified by its clinical presentation (focal, multifocal, or generalized) and by its anatomical origin (cortical, subcortical/brainstem, spinal, or peripheral). The label 'essential' is used for idiopathic cases in which no other neurological signs or structural abnormalities can be identified.",
        "management_principles": "Management is largely symptomatic. First-line treatment options include medications such as clonazepam, valproate, or levetiracetam. Since alcohol may transiently improve symptoms, its effect supports the diagnosis but alcohol is not recommended as a treatment strategy. In women who are pregnant or lactating, benzodiazepines and levetiracetam may be used with caution after weighing the risks and benefits, whereas valproate is generally contraindicated due to its teratogenicity.",
        "option_analysis": "Option A (Cortical myoclonus) typically implies an epileptic or neurodegenerative process with characteristic EEG findings, which is not the case here. Option C (Physiological myoclonus) represents normal, benign phenomena (e.g., sleep or hiccups) that are transient and do not present as a persistent syndrome. Option D (Epileptic myoclonus) would be accompanied by other seizure-related phenomena and abnormal EEG discharges. Thus, Option B (Essential myoclonus) fits best given the isolated, alcohol-responsive nature of the myoclonic jerks.",
        "clinical_pearls": "1. Alcohol responsiveness is a key supportive feature in disorders falling under the 'essential' category (as seen in essential tremor and, less commonly, essential myoclonus). 2. Differentiating between cortical/epileptic myoclonus and essential myoclonus is crucial; the absence of EEG abnormalities and other neurological signs points toward an essential, idiopathic process.",
        "current_evidence": "Recent research emphasizes the role of dysfunctional inhibitory neurotransmission in idiopathic movement disorders. While essential tremor is much better characterized in clinical studies, evolving neurophysiological techniques continue to refine our understanding of less common presentations such as essential myoclonus. Guidelines still recommend symptomatic therapy with agents that enhance GABAergic transmission with special consideration for women of childbearing potential."
      },
      "source_file": "vascular_mcqs_20250519_071211_processed_20250519_225344_processed_20250520_014212.json"
    }
  },
  {
    "model": "mcq.mcq",
    "pk": "99993334",
    "fields": {
      "question_number": "363",
      "question_text": "IV drug user came with acute stroke in 2 hours, CT image attached (good aspect) Was febrile and had a pan systolic murmur. What is the treatment?",
      "options": {
        "A": "antibiotics",
        "B": "thrombolysis",
        "C": "thrombectomy"
      },
      "correct_answer": "A",
      "subspecialty": "Vascular Neurology/Stroke",
      "exam_type": "Part II",
      "exam_year": 2020,
      "explanation_sections": {
        "conceptual_foundation": "In patients with acute ischemic stroke, treatment is usually time sensitive. However, in the context of infective endocarditis, which is a well-known source of septic emboli, the management approach differs considerably compared to atherosclerotic strokes.",
        "pathophysiology": "Infective endocarditis, particularly in IV drug users, predisposes to the formation of infected vegetations on heart valves. Embolization of these vegetations can lead to ischemic strokes. Unlike typical thromboembolic strokes from atherosclerosis or cardiac mural thrombi, septic emboli carry a risk of causing hemorrhagic conversion and mycotic aneurysms.",
        "clinical_correlation": "The patient\u2019s history of intravenous drug use, the presence of fever, and a pan\u2010systolic murmur strongly point towards infective endocarditis as the underlying etiology of the stroke. In such cases, rapid identification and treatment of the infection are paramount to prevent further embolic events and complications.",
        "diagnostic_approach": "The diagnostic workup in such cases includes blood cultures, echocardiography (transthoracic and/or transesophageal) to identify vegetations on the valves, as well as neuroimaging (CT or MRI) to assess the nature of the stroke. Differential diagnoses include atherosclerotic stroke, cardioembolic stroke from atrial fibrillation, or hemorrhagic stroke. The clinical context and imaging help distinguish septic embolism secondary to endocarditis from these other types.",
        "classification_and_nosology": "Stroke secondary to infective endocarditis is classified as an embolic stroke. It falls into the category of cardioembolic strokes but is unique due to its septic source, which contributes additional risks like hemorrhage.",
        "management_principles": "The primary treatment is the initiation of appropriate intravenous antibiotics tailored to the suspected or identified organism (often covering Staphylococcus aureus in IV drug users). Thrombolysis is contraindicated in infective endocarditis due to the high risk of intracranial hemorrhage and potential worsening of the septic embolic phenomenon. In cases of large vessel occlusion where mechanical thrombectomy is considered, careful evaluation is needed and generally, thrombectomy is not the first-line treatment if an infection is present. In pregnant or lactating patients, antibiotic selection should consider fetal safety, with agents such as penicillins or cephalosporins often preferred.",
        "option_analysis": "Option A (antibiotics) is the appropriate treatment given the clinical scenario of presumed infective endocarditis causing septic emboli. Option B (thrombolysis) is contraindicated in the setting of infective endocarditis. Option C (thrombectomy) is not routinely indicated in septic embolic strokes because of the risk of infecting the cerebral vasculature and provoking hemorrhage. Option D is missing and thus not applicable.",
        "clinical_pearls": "1. In a febrile patient with IV drug use and a new murmur, always suspect infective endocarditis as a source of embolic stroke. 2. Thrombolysis is contraindicated in infective endocarditis because of the increased risk of hemorrhagic conversion.",
        "current_evidence": "Recent guidelines emphasize the need for rapid antibiotic administration in infective endocarditis and caution against the use of thrombolytic therapy in septic embolic strokes due to bleeding risks. Research continues to refine the management strategies in these complex patients, particularly regarding the timing of surgical interventions if indicated."
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
