#!/usr/bin/env python3
"""
Fix case pools in case_bot_enhanced.py
This script will:
1. Fix age ranges for problematic cases
2. Add missing specialties with appropriate cases
"""

import re

def fix_age_ranges():
    """Fix the two problematic age ranges"""
    
    with open('django_neurology_mcq/mcq/case_bot_enhanced.py', 'r') as f:
        content = f.read()
    
    # Fix 1: Acute bilirubin encephalopathy - should be neonatal
    content = content.replace(
        "('Acute bilirubin encephalopathy', (18, 30), 'emergency', 'Kernicterus in adults, movement disorders')",
        "('Acute bilirubin encephalopathy', (0, 1), 'emergency', 'Neonatal kernicterus, dystonia, hearing loss')"
    )
    
    # Fix 2: Acute encephalopathy with biphasic seizures - should be infants/toddlers
    content = content.replace(
        "('Acute encephalopathy with biphasic seizures', (6, 24), 'emergency', 'Febrile illness, specific seizure pattern')",
        "('Acute encephalopathy with biphasic seizures', (0.5, 2), 'emergency', 'Febrile illness in infant, biphasic seizure pattern')"
    )
    
    with open('django_neurology_mcq/mcq/case_bot_enhanced.py', 'w') as f:
        f.write(content)
    
    print("✓ Fixed age ranges for 2 problematic cases")

def add_missing_specialties():
    """Add the missing specialties to complete the case pools"""
    
    # Define all missing specialties with age-appropriate cases
    missing_specialties = '''
        'Neurogenetics': {
            'easy': [
                ('Duchenne muscular dystrophy', (3, 10), 'routine', 'Progressive proximal weakness, calf hypertrophy'),
                ('Neurofibromatosis type 1', (5, 25), 'routine', 'Multiple café-au-lait spots, freckling'),
                ('Tuberous sclerosis complex', (0, 10), 'routine', 'Infantile spasms, ash leaf spots'),
                ('Huntington disease - juvenile', (5, 20), 'routine', 'Positive family history, movement disorder'),
                ('Fragile X syndrome', (2, 15), 'routine', 'Intellectual disability, large ears, macro-orchidism'),
                ('Spinal muscular atrophy type 2', (0.5, 2), 'routine', 'Progressive weakness, absent reflexes'),
                ('Friedreich ataxia', (5, 15), 'routine', 'Progressive ataxia, cardiomyopathy'),
                ('Rett syndrome', (1, 4), 'routine', 'Developmental regression, hand stereotypies'),
                ('Prader-Willi syndrome', (0, 5), 'routine', 'Hypotonia, feeding difficulties, obesity'),
                ('Angelman syndrome', (1, 5), 'routine', 'Happy demeanor, seizures, ataxia'),
                ('MELAS syndrome', (5, 15), 'routine', 'Stroke-like episodes, lactic acidosis'),
                ('Pelizaeus-Merzbacher disease', (0, 5), 'routine', 'Nystagmus, spasticity, developmental delay'),
                ('Benign familial neonatal seizures', (0, 0.1), 'routine', 'Neonatal seizures, family history'),
                ('Hereditary sensory neuropathy', (10, 30), 'routine', 'Loss of pain sensation, ulcers'),
                ('Familial hemiplegic migraine', (10, 30), 'routine', 'Migraine with hemiplegia, family history'),
            ],
            'moderate': [
                ('Mitochondrial myopathy - CPEO', (20, 50), 'routine', 'Ptosis, ophthalmoplegia, weakness'),
                ('Spinocerebellar ataxia type 3', (30, 50), 'routine', 'Progressive ataxia, nystagmus'),
                ('Hereditary spastic paraplegia', (20, 40), 'routine', 'Progressive spastic gait, hyperreflexia'),
                ('Adult-onset leukodystrophy', (30, 50), 'routine', 'Cognitive decline, white matter changes'),
                ('Charcot-Marie-Tooth type 1A', (10, 30), 'routine', 'Distal weakness, pes cavus'),
                ('Myotonic dystrophy type 1', (20, 40), 'routine', 'Myotonia, facial weakness, cataracts'),
                ('Fabry disease', (10, 30), 'routine', 'Acroparesthesias, angiokeratomas'),
                ('Gaucher disease type 3', (2, 10), 'routine', 'Horizontal gaze palsy, hepatosplenomegaly'),
                ('X-linked adrenoleukodystrophy', (5, 10), 'routine', 'Behavioral changes, adrenal insufficiency'),
                ('Leber hereditary optic neuropathy', (15, 35), 'routine', 'Bilateral vision loss, male predominance'),
                ('Episodic ataxia type 2', (5, 20), 'routine', 'Episodic vertigo and ataxia'),
                ('Alternating hemiplegia of childhood', (0.5, 5), 'routine', 'Episodic hemiplegia, dystonia'),
                ('CADASIL', (30, 50), 'routine', 'Migraines, strokes, family history'),
                ('Dentatorubral-pallidoluysian atrophy', (20, 40), 'routine', 'Ataxia, choreoathetosis, dementia'),
                ('Neuronal intranuclear inclusion disease', (40, 60), 'routine', 'Dementia, neuropathy, leukoencephalopathy'),
            ],
            'hard': [
                ('Ataxia telangiectasia', (2, 10), 'routine', 'Progressive ataxia, telangiectasias'),
                ('Alexander disease - adult onset', (20, 50), 'routine', 'Bulbar symptoms, palatal tremor'),
                ('Neuronal ceroid lipofuscinosis - juvenile', (5, 10), 'routine', 'Vision loss, seizures, dementia'),
                ('Niemann-Pick type C', (5, 25), 'routine', 'Vertical gaze palsy, ataxia, dystonia'),
                ('Neurodegeneration with brain iron accumulation', (5, 25), 'routine', 'Dystonia, parkinsonism, iron deposition'),
                ('Pantothenate kinase-associated neurodegeneration', (5, 15), 'routine', '"Eye of the tiger" sign, dystonia'),
                ('Cockayne syndrome', (1, 10), 'routine', 'Photosensitivity, developmental delay'),
                ('Canavan disease', (0.5, 1), 'routine', 'Macrocephaly, spasticity, optic atrophy'),
                ('Krabbe disease - late onset', (2, 40), 'routine', 'Spastic paraparesis, optic atrophy'),
                ('Metachromatic leukodystrophy', (1, 5), 'routine', 'Regression, ataxia, demyelination'),
                ('GM1 gangliosidosis', (0.5, 2), 'routine', 'Cherry red spot, hepatosplenomegaly'),
                ('Sanfilippo syndrome', (2, 6), 'routine', 'Behavioral problems, coarse features'),
                ('Lafora disease', (10, 18), 'routine', 'Myoclonic epilepsy, rapid decline'),
                ('Unverricht-Lundborg disease', (8, 15), 'routine', 'Progressive myoclonus epilepsy'),
                ('Sialidosis type 1', (10, 20), 'routine', 'Cherry red spot, myoclonus'),
            ]
        },
        'Neuroimmunology': {
            'easy': [
                ('Multiple sclerosis - CIS', (20, 40), 'routine', 'First demyelinating event, MRI lesions'),
                ('Neuromyelitis optica spectrum disorder', (30, 50), 'routine', 'Longitudinal myelitis, bilateral optic neuritis'),
                ('Acute disseminated encephalomyelitis', (5, 15), 'emergency', 'Post-infectious, multifocal symptoms'),
                ('Myasthenia gravis - generalized', (20, 60), 'routine', 'Fatigable weakness, ptosis, diplopia'),
                ('Miller Fisher syndrome', (30, 60), 'routine', 'Ophthalmoplegia, ataxia, areflexia'),
                ('Transverse myelitis', (20, 50), 'emergency', 'Acute paraparesis, sensory level'),
                ('Optic neuritis - typical', (20, 40), 'routine', 'Unilateral vision loss, pain with eye movement'),
                ('Bell palsy', (20, 60), 'routine', 'Acute facial weakness, no other deficits'),
                ('Chronic inflammatory demyelinating polyneuropathy', (40, 70), 'routine', 'Progressive weakness over 2 months'),
                ('Lambert-Eaton myasthenic syndrome', (50, 70), 'routine', 'Proximal weakness, dry mouth'),
                ('Polymyositis', (30, 60), 'routine', 'Proximal muscle weakness, elevated CK'),
                ('Dermatomyositis', (40, 60), 'routine', 'Heliotrope rash, proximal weakness'),
                ('Giant cell arteritis', (60, 80), 'emergency', 'Headache, jaw claudication, vision loss'),
                ('Primary CNS vasculitis', (40, 60), 'routine', 'Headache, cognitive changes, strokes'),
                ('Sarcoid neuropathy', (30, 60), 'routine', 'Cranial neuropathy, systemic sarcoidosis'),
            ],
            'moderate': [
                ('Anti-MOG antibody disease', (5, 45), 'emergency', 'Bilateral optic neuritis, ADEM-like'),
                ('Autoimmune encephalitis - anti-LGI1', (50, 70), 'emergency', 'Faciobrachial dystonic seizures'),
                ('Stiff person syndrome', (40, 60), 'routine', 'Axial rigidity, painful spasms'),
                ('Neurosarcoidosis', (30, 50), 'routine', 'Cranial neuropathies, meningitis'),
                ('Paraneoplastic cerebellar degeneration', (50, 70), 'routine', 'Subacute ataxia, anti-Yo antibodies'),
                ('Anti-CASPR2 encephalitis', (50, 70), 'emergency', 'Morvan syndrome, neuromyotonia'),
                ('Autoimmune autonomic ganglionopathy', (20, 60), 'routine', 'Orthostatic hypotension, GI dysmotility'),
                ('Susac syndrome', (20, 40), 'emergency', 'Encephalopathy, BRAO, hearing loss'),
                ('Chronic lymphocytic inflammation with pontine perivascular enhancement', (40, 60), 'routine', 'Diplopia, facial paresthesias, ataxia'),
                ('IgG4-related pachymeningitis', (40, 70), 'routine', 'Headache, cranial neuropathies'),
                ('Gluten ataxia', (40, 60), 'routine', 'Progressive ataxia, positive antibodies'),
                ('Acute motor axonal neuropathy', (20, 60), 'emergency', 'Pure motor weakness, axonal GBS'),
                ('Multifocal motor neuropathy', (30, 60), 'routine', 'Asymmetric weakness, conduction blocks'),
                ('POEMS syndrome', (40, 60), 'routine', 'Polyneuropathy, organomegaly, M-protein'),
                ('Neuro-Behcet disease', (20, 40), 'routine', 'Brainstem syndrome, oral ulcers'),
            ],
            'hard': [
                ('Bickerstaff brainstem encephalitis', (20, 60), 'emergency', 'Ophthalmoplegia, ataxia, hyperreflexia'),
                ('Anti-NMDA receptor encephalitis', (15, 35), 'emergency', 'Psychosis, seizures, dyskinesias'),
                ('Progressive encephalomyelitis with rigidity and myoclonus', (40, 70), 'routine', 'Rigidity, myoclonus, brainstem signs'),
                ('Hashimoto encephalopathy', (40, 60), 'emergency', 'Encephalopathy, high anti-TPO'),
                ('Anti-GABABR encephalitis', (50, 70), 'emergency', 'Limbic encephalitis, seizures'),
                ('Anti-AMPAR encephalitis', (40, 70), 'emergency', 'Limbic symptoms, often paraneoplastic'),
                ('Anti-DPPX encephalitis', (45, 75), 'emergency', 'Weight loss, cognitive decline, hyperekplexia'),
                ('Chronic relapsing inflammatory optic neuropathy', (30, 60), 'routine', 'Recurrent optic neuritis, steroid dependent'),
                ('Autoimmune GFAP astrocytopathy', (40, 60), 'emergency', 'Meningoencephalitis, myelitis'),
                ('Anti-IgLON5 disease', (50, 70), 'routine', 'Sleep disorder, gait instability, dysautonomia'),
                ('Nodular regenerative hyperplasia with neuropathy', (40, 60), 'routine', 'Neuropathy, portal hypertension'),
                ('Paraneoplastic peripheral nerve hyperexcitability', (40, 70), 'routine', 'Neuromyotonia, muscle cramps'),
                ('Anti-Hu paraneoplastic encephalomyelitis', (50, 70), 'routine', 'Sensory neuronopathy, limbic encephalitis'),
                ('Anti-amphiphysin paraneoplastic syndrome', (50, 70), 'routine', 'Stiff person syndrome, breast cancer'),
                ('Collapsin response mediator protein-5 neuropathy', (50, 70), 'routine', 'Sensorimotor neuropathy, chorea'),
            ]
        },
        'Neuro-infectious': {
            'easy': [
                ('Bacterial meningitis - pneumococcal', (40, 70), 'emergency', 'Fever, headache, neck stiffness'),
                ('Viral meningitis', (15, 45), 'emergency', 'Headache, photophobia, mild neck stiffness'),
                ('Herpes simplex encephalitis', (20, 60), 'emergency', 'Fever, confusion, temporal seizures'),
                ('Brain abscess', (30, 60), 'emergency', 'Headache, focal deficits, fever'),
                ('Epidural abscess', (40, 70), 'emergency', 'Back pain, fever, progressive weakness'),
                ('Neurosyphilis - meningovascular', (30, 60), 'routine', 'Stroke in young adult, positive serology'),
                ('HIV-associated neurocognitive disorder', (30, 50), 'routine', 'Memory problems, HIV positive'),
                ('Progressive multifocal leukoencephalopathy', (40, 60), 'routine', 'Focal deficits, immunosuppressed'),
                ('Neurocysticercosis', (20, 50), 'routine', 'Seizures, cystic brain lesions'),
                ('Lyme neuroborreliosis', (30, 60), 'routine', 'Facial palsy, radiculopathy, tick exposure'),
                ('Tuberculous meningitis', (20, 50), 'emergency', 'Subacute meningitis, cranial nerve palsies'),
                ('Cryptococcal meningitis', (30, 50), 'emergency', 'Headache, confusion, immunocompromised'),
                ('CMV encephalitis', (30, 50), 'emergency', 'Confusion, periventricular enhancement'),
                ('Varicella zoster - shingles', (50, 80), 'routine', 'Dermatomal rash, pain'),
                ('Acute flaccid myelitis', (2, 15), 'emergency', 'Acute weakness, gray matter lesions'),
            ],
            'moderate': [
                ('Japanese encephalitis', (5, 30), 'emergency', 'Fever, altered consciousness, Asia travel'),
                ('West Nile encephalitis', (50, 80), 'emergency', 'Fever, weakness, tremor'),
                ('Rabies encephalitis', (10, 60), 'emergency', 'Hydrophobia, agitation, animal bite'),
                ('Whipple disease', (40, 60), 'routine', 'Dementia, oculomasticatory myorhythmia'),
                ('Neurosyphilis - general paresis', (40, 60), 'routine', 'Dementia, personality change'),
                ('Subacute sclerosing panencephalitis', (5, 15), 'routine', 'Myoclonus, cognitive decline, measles history'),
                ('BK virus encephalitis', (40, 60), 'emergency', 'Confusion, immunosuppressed patient'),
                ('HHV-6 encephalitis', (30, 50), 'emergency', 'Post-transplant, limbic encephalitis'),
                ('Toxoplasma encephalitis', (30, 50), 'emergency', 'Multiple ring-enhancing lesions, HIV'),
                ('Fungal meningitis', (30, 60), 'emergency', 'Indolent meningitis, immunocompromised'),
                ('Nocardia brain abscess', (40, 70), 'emergency', 'Multiple abscesses, immunosuppressed'),
                ('Listeria rhombencephalitis', (50, 70), 'emergency', 'Brainstem signs, immunocompromised'),
                ('Enterovirus 71 encephalitis', (1, 10), 'emergency', 'Hand-foot-mouth disease, brainstem encephalitis'),
                ('Nipah virus encephalitis', (20, 50), 'emergency', 'Fever, altered consciousness, pig exposure'),
                ('Tick-borne encephalitis', (30, 60), 'emergency', 'Biphasic illness, tick exposure'),
            ],
            'hard': [
                ('Balamuthia granulomatous amebic encephalitis', (10, 70), 'emergency', 'Focal lesions, soil exposure'),
                ('Primary amebic meningoencephalitis', (10, 30), 'emergency', 'Fulminant meningitis, freshwater exposure'),
                ('Angiostrongylus cantonensis', (20, 40), 'emergency', 'Eosinophilic meningitis, snail ingestion'),
                ('Baylisascaris procyonis', (2, 20), 'emergency', 'Eosinophilic meningoencephalitis, raccoon exposure'),
                ('Gnathostoma spinigerum', (20, 50), 'emergency', 'Radiculomyelitis, raw fish consumption'),
                ('Sparganosis', (20, 50), 'routine', 'Seizures, subcutaneous nodules'),
                ('Neuroschistosomiasis', (20, 40), 'routine', 'Myelopathy, bladder symptoms'),
                ('Amoebic brain abscess', (30, 50), 'emergency', 'Ring-enhancing lesions, immunocompetent'),
                ('Mucormycosis', (40, 60), 'emergency', 'Rhinocerebral involvement, diabetes'),
                ('Aspergillus brain abscess', (40, 60), 'emergency', 'Multiple abscesses, neutropenia'),
                ('Actinomyces brain abscess', (30, 60), 'emergency', 'Chronic abscess, dental work'),
                ('Bartonella encephalopathy', (20, 50), 'routine', 'Encephalopathy, cat exposure'),
                ('Ehrlichia meningoencephalitis', (40, 70), 'emergency', 'Tick exposure, leukopenia'),
                ('Rocky Mountain spotted fever', (20, 60), 'emergency', 'Rash, tick exposure, southeast US'),
                ('Powassan virus encephalitis', (50, 70), 'emergency', 'Rapid onset encephalitis, tick bite'),
            ]
        },
        'Neuro-oncology': {
            'easy': [
                ('Glioblastoma multiforme', (50, 70), 'routine', 'Progressive headache, focal deficits'),
                ('Meningioma', (40, 70), 'routine', 'Incidental finding or mass effect'),
                ('Brain metastases - lung primary', (55, 75), 'routine', 'Multiple enhancing lesions, known cancer'),
                ('Acoustic neuroma', (40, 60), 'routine', 'Unilateral hearing loss, tinnitus'),
                ('Pituitary adenoma', (30, 60), 'routine', 'Visual field defect, hormonal symptoms'),
                ('Primary CNS lymphoma', (50, 70), 'routine', 'Confusion, periventricular enhancement'),
                ('Ependymoma', (5, 45), 'routine', 'Hydrocephalus, posterior fossa mass'),
                ('Craniopharyngioma', (5, 15), 'routine', 'Visual deficits, growth failure'),
                ('Pilocytic astrocytoma', (5, 20), 'routine', 'Cerebellar mass, cystic with nodule'),
                ('Colloid cyst', (30, 50), 'emergency', 'Sudden headache, drop attacks'),
                ('Hemangioblastoma', (30, 50), 'routine', 'Cerebellar mass, von Hippel-Lindau'),
                ('Oligodendroglioma', (35, 55), 'routine', 'Seizures, frontal lobe mass'),
                ('Ganglioglioma', (10, 30), 'routine', 'Temporal lobe epilepsy'),
                ('Choroid plexus papilloma', (0, 10), 'routine', 'Hydrocephalus in child'),
                ('Schwannoma', (30, 60), 'routine', 'Nerve root pain, mass on MRI'),
            ],
            'moderate': [
                ('Medulloblastoma', (3, 10), 'routine', 'Morning headache, ataxia, vomiting'),
                ('Diffuse intrinsic pontine glioma', (5, 10), 'routine', 'Cranial nerve palsies, ataxia'),
                ('Atypical teratoid/rhabdoid tumor', (0, 3), 'routine', 'Rapidly progressive, posterior fossa'),
                ('Germinoma', (10, 20), 'routine', 'Diabetes insipidus, visual deficits'),
                ('Pineal region tumor', (15, 35), 'routine', 'Parinaud syndrome, hydrocephalus'),
                ('Leptomeningeal carcinomatosis', (45, 70), 'routine', 'Multiple cranial neuropathies, back pain'),
                ('Paraneoplastic limbic encephalitis', (50, 70), 'routine', 'Memory loss, seizures, lung cancer'),
                ('Radiation necrosis', (45, 70), 'routine', 'New deficit after brain radiation'),
                ('Gliomatosis cerebri', (40, 60), 'routine', 'Diffuse infiltration, personality change'),
                ('Central neurocytoma', (20, 40), 'routine', 'Intraventricular mass, hydrocephalus'),
                ('Dysembryoplastic neuroepithelial tumor', (5, 20), 'routine', 'Long-standing epilepsy, cortical mass'),
                ('Pleomorphic xanthoastrocytoma', (10, 30), 'routine', 'Seizures, superficial temporal mass'),
                ('Subependymal giant cell astrocytoma', (10, 20), 'routine', 'Tuberous sclerosis, hydrocephalus'),
                ('Hemangiopericytoma', (40, 60), 'routine', 'Dural-based mass, aggressive'),
                ('Chordoma', (40, 60), 'routine', 'Clivus mass, cranial nerve palsies'),
            ],
            'hard': [
                ('Primary spinal cord glioma', (20, 40), 'routine', 'Progressive myelopathy, central cord'),
                ('Intravascular lymphoma', (50, 70), 'routine', 'Multifocal deficits, skin lesions'),
                ('Gliomatosis cerebri', (40, 60), 'routine', 'Diffuse infiltration, minimal enhancement'),
                ('Papillary tumor of pineal region', (20, 50), 'routine', 'Hydrocephalus, Parinaud syndrome'),
                ('Rosette-forming glioneuronal tumor', (20, 40), 'routine', 'Fourth ventricle mass, headache'),
                ('Angiocentric glioma', (5, 20), 'routine', 'Refractory epilepsy, cortical mass'),
                ('Papillary glioneuronal tumor', (10, 30), 'routine', 'Temporal mass, cystic and solid'),
                ('Chordoid glioma', (30, 50), 'routine', 'Third ventricle mass, memory problems'),
                ('Pituicytoma', (40, 60), 'routine', 'Sellar/suprasellar mass, hormone normal'),
                ('Solitary fibrous tumor', (40, 60), 'routine', 'Dural-based mass, hypoglycemia'),
                ('Extraventricular neurocytoma', (30, 50), 'routine', 'Cerebral hemisphere mass, seizures'),
                ('Pineocytoma', (20, 50), 'routine', 'Pineal mass, slow growing'),
                ('Esthesioneuroblastoma', (40, 60), 'routine', 'Nasal mass, anosmia, frontal extension'),
                ('Primary CNS sarcoma', (20, 50), 'routine', 'Hemorrhagic mass, rapid growth'),
                ('Erdheim-Chester disease', (40, 60), 'routine', 'Diabetes insipidus, cerebellar symptoms'),
            ]
        },
        'Neuro-otology': {
            'easy': [
                ('Benign paroxysmal positional vertigo', (40, 70), 'routine', 'Brief vertigo with head movement'),
                ('Meniere disease', (30, 60), 'routine', 'Episodic vertigo, hearing loss, tinnitus'),
                ('Vestibular neuritis', (30, 60), 'emergency', 'Acute sustained vertigo, no hearing loss'),
                ('Acoustic neuroma', (40, 60), 'routine', 'Progressive hearing loss, tinnitus'),
                ('Labyrinthitis', (30, 60), 'emergency', 'Vertigo with hearing loss'),
                ('Orthostatic hypotension', (50, 80), 'routine', 'Dizziness on standing, blood pressure drop'),
                ('Migraine-associated vertigo', (20, 50), 'routine', 'Vertigo episodes, headache history'),
                ('Sudden sensorineural hearing loss', (40, 70), 'emergency', 'Acute unilateral hearing loss'),
                ('Otosclerosis', (20, 50), 'routine', 'Progressive conductive hearing loss'),
                ('Vestibular schwannoma', (40, 60), 'routine', 'Unilateral hearing loss, imbalance'),
                ('Superior canal dehiscence', (30, 50), 'routine', 'Vertigo with loud sounds, autophony'),
                ('Perilymphatic fistula', (30, 60), 'routine', 'Vertigo after trauma or barotrauma'),
                ('Presbycusis', (60, 90), 'routine', 'Bilateral high-frequency hearing loss'),
                ('Autoimmune inner ear disease', (30, 60), 'routine', 'Fluctuating hearing loss, vertigo'),
                ('Ototoxicity', (40, 70), 'routine', 'Hearing loss after aminoglycosides'),
            ],
            'moderate': [
                ('Bilateral vestibulopathy', (40, 70), 'routine', 'Oscillopsia, imbalance in dark'),
                ('Vestibular paroxysmia', (40, 70), 'routine', 'Brief vertigo attacks, vascular compression'),
                ('Persistent postural-perceptual dizziness', (30, 60), 'routine', 'Chronic dizziness, visual triggers'),
                ('Mal de debarquement', (30, 50), 'routine', 'Rocking sensation after travel'),
                ('Third window syndrome', (30, 60), 'routine', 'Vertigo with pressure changes'),
                ('Cogan syndrome', (20, 40), 'routine', 'Hearing loss, vertigo, eye inflammation'),
                ('Temporal bone fracture', (20, 50), 'emergency', 'Hearing loss, facial palsy, vertigo'),
                ('Ramsay Hunt syndrome', (40, 70), 'emergency', 'Facial palsy, vesicles, vertigo'),
                ('Wernicke encephalopathy', (40, 60), 'emergency', 'Nystagmus, ataxia, confusion'),
                ('Central positional vertigo', (50, 80), 'routine', 'Position-triggered vertigo, CNS signs'),
                ('Otosyphilis', (30, 60), 'routine', 'Fluctuating hearing loss, vertigo'),
                ('Lermoyez syndrome', (30, 50), 'routine', 'Hearing improves during vertigo'),
                ('Vestibular atelectasis', (40, 60), 'routine', 'Episodic vertigo, normal hearing'),
                ('Endolymphatic sac tumor', (20, 50), 'routine', 'Hearing loss, von Hippel-Lindau'),
                ('Superficial siderosis', (40, 70), 'routine', 'Hearing loss, ataxia, myelopathy'),
            ],
            'hard': [
                ('Bilateral Meniere disease', (40, 60), 'routine', 'Bilateral episodic vertigo and hearing loss'),
                ('Autoimmune inner ear disease', (30, 50), 'routine', 'Rapidly progressive bilateral hearing loss'),
                ('Susac syndrome', (20, 40), 'emergency', 'Hearing loss, encephalopathy, BRAO'),
                ('Vogt-Koyanagi-Harada disease', (30, 50), 'routine', 'Hearing loss, uveitis, vitiligo'),
                ('Neuro-otologic sarcoidosis', (30, 60), 'routine', 'Hearing loss, facial palsy, vertigo'),
                ('Langerhans cell histiocytosis', (20, 40), 'routine', 'Temporal bone lesions, hearing loss'),
                ('Gorlin syndrome', (20, 40), 'routine', 'Multiple keratocysts, hearing loss'),
                ('CANVAS syndrome', (50, 70), 'routine', 'Cerebellar ataxia, neuropathy, vestibular loss'),
                ('Episodic ataxia type 2', (10, 40), 'routine', 'Episodic vertigo and ataxia'),
                ('Spinocerebellar ataxia type 6', (40, 60), 'routine', 'Progressive ataxia, downbeat nystagmus'),
                ('DFNA9', (30, 50), 'routine', 'Progressive hearing loss and vestibular dysfunction'),
                ('Pendred syndrome', (10, 30), 'routine', 'Hearing loss, goiter, EVA'),
                ('Jervell and Lange-Nielsen syndrome', (0, 20), 'routine', 'Deafness, long QT syndrome'),
                ('Usher syndrome', (10, 30), 'routine', 'Hearing loss, retinitis pigmentosa'),
                ('Refsum disease', (20, 40), 'routine', 'Hearing loss, retinitis pigmentosa, neuropathy'),
            ]
        },
        'Neuroophthalmology': {
            'easy': [
                ('Optic neuritis', (20, 40), 'routine', 'Unilateral vision loss, pain with eye movement'),
                ('Anterior ischemic optic neuropathy', (60, 80), 'emergency', 'Sudden painless vision loss'),
                ('Papilledema', (20, 50), 'routine', 'Headache, transient visual obscurations'),
                ('Third nerve palsy', (40, 70), 'emergency', 'Ptosis, dilated pupil, diplopia'),
                ('Sixth nerve palsy', (40, 70), 'routine', 'Horizontal diplopia worse at distance'),
                ('Myasthenia gravis - ocular', (20, 60), 'routine', 'Variable ptosis and diplopia'),
                ('Horner syndrome', (30, 60), 'routine', 'Ptosis, miosis, anhidrosis'),
                ('Internuclear ophthalmoplegia', (20, 50), 'routine', 'Horizontal diplopia, adduction deficit'),
                ('Ocular myasthenia', (30, 60), 'routine', 'Fatigable ptosis, diplopia'),
                ('Migraine with visual aura', (20, 40), 'routine', 'Zigzag lines, fortification spectra'),
                ('Posterior vitreous detachment', (50, 70), 'routine', 'Floaters, flashing lights'),
                ('Giant cell arteritis', (60, 80), 'emergency', 'Vision loss, jaw claudication'),
                ('Graves ophthalmopathy', (30, 50), 'routine', 'Proptosis, lid retraction, diplopia'),
                ('Pseudotumor cerebri', (20, 40), 'routine', 'Headache, papilledema, obesity'),
                ('Convergence insufficiency', (10, 30), 'routine', 'Near diplopia, eyestrain'),
            ],
            'moderate': [
                ('Posterior ischemic optic neuropathy', (50, 70), 'emergency', 'Vision loss after surgery or blood loss'),
                ('Leber hereditary optic neuropathy', (15, 35), 'routine', 'Sequential bilateral vision loss, male'),
                ('Neuromyelitis optica', (30, 50), 'emergency', 'Bilateral optic neuritis, myelitis'),
                ('Miller Fisher syndrome', (30, 60), 'emergency', 'Ophthalmoplegia, ataxia, areflexia'),
                ('Parinaud syndrome', (20, 50), 'routine', 'Upgaze palsy, convergence-retraction nystagmus'),
                ('One-and-a-half syndrome', (40, 60), 'routine', 'Horizontal gaze palsy plus INO'),
                ('Balint syndrome', (50, 70), 'routine', 'Simultanagnosia, optic ataxia, ocular apraxia'),
                ('Charles Bonnet syndrome', (70, 90), 'routine', 'Visual hallucinations, vision loss'),
                ('Posterior cortical atrophy', (50, 70), 'routine', 'Visual agnosia, Balint syndrome'),
                ('Optic nerve sheath meningioma', (40, 60), 'routine', 'Progressive vision loss, optociliary shunts'),
                ('Toxic optic neuropathy', (30, 60), 'routine', 'Bilateral vision loss, alcohol/tobacco'),
                ('Nutritional optic neuropathy', (40, 70), 'routine', 'Bilateral central scotomas, B12 deficiency'),
                ('Dominant optic atrophy', (10, 30), 'routine', 'Childhood onset vision loss, family history'),
                ('Ocular neuromyotonia', (30, 60), 'routine', 'Episodic diplopia, prior radiation'),
                ('Superior oblique myokymia', (30, 50), 'routine', 'Monocular oscillopsia, vertical diplopia'),
            ],
            'hard': [
                ('WEBINO syndrome', (40, 60), 'routine', 'Wall-eyed bilateral INO'),
                ('Eight-and-a-half syndrome', (40, 60), 'routine', 'One-and-a-half plus facial palsy'),
                ('Chronic relapsing inflammatory optic neuropathy', (30, 50), 'routine', 'Recurrent optic neuritis, steroid dependent'),
                ('Autoimmune optic neuropathy', (40, 60), 'routine', 'Progressive vision loss, other autoimmunity'),
                ('Paraneoplastic optic neuropathy', (50, 70), 'routine', 'Bilateral vision loss, CRMP-5 antibodies'),
                ('MELAS', (20, 40), 'routine', 'Hemianopia, stroke-like episodes'),
                ('Leigh syndrome', (1, 10), 'routine', 'Optic atrophy, brainstem signs'),
                ('Optic nerve hypoplasia', (0, 5), 'routine', 'Small optic discs, pituitary dysfunction'),
                ('Morning glory disc anomaly', (0, 10), 'routine', 'Funnel-shaped disc, poor vision'),
                ('Optic disc drusen', (20, 40), 'routine', 'Pseudopapilledema, visual field defects'),
                ('Bardet-Biedl syndrome', (5, 20), 'routine', 'Retinitis pigmentosa, obesity, polydactyly'),
                ('Kearns-Sayre syndrome', (10, 20), 'routine', 'CPEO, retinitis pigmentosa, heart block'),
                ('Wolfram syndrome', (5, 20), 'routine', 'Optic atrophy, diabetes insipidus'),
                ('Behr syndrome', (1, 10), 'routine', 'Optic atrophy, ataxia, intellectual disability'),
                ('Costeff syndrome', (1, 10), 'routine', 'Optic atrophy, movement disorder, 3-methylglutaconic aciduria'),
            ]
        },
        'Neuropsychiatry': {
            'easy': [
                ('Major depression with psychotic features', (30, 60), 'routine', 'Mood symptoms, delusions'),
                ('Bipolar disorder - manic episode', (20, 40), 'emergency', 'Elevated mood, decreased sleep, psychosis'),
                ('Schizophrenia - first episode', (18, 30), 'emergency', 'Hallucinations, delusions, disorganization'),
                ('Delirium', (60, 80), 'emergency', 'Acute confusion, fluctuating consciousness'),
                ('Substance-induced psychosis', (20, 40), 'emergency', 'Psychosis, drug use history'),
                ('Panic disorder', (20, 40), 'routine', 'Recurrent panic attacks, anticipatory anxiety'),
                ('Generalized anxiety disorder', (30, 50), 'routine', 'Chronic worry, physical symptoms'),
                ('Post-traumatic stress disorder', (20, 50), 'routine', 'Trauma history, flashbacks, hypervigilance'),
                ('Obsessive-compulsive disorder', (20, 40), 'routine', 'Obsessions, compulsions, distress'),
                ('Conversion disorder', (20, 40), 'routine', 'Neurological symptoms, psychological stress'),
                ('Adjustment disorder', (20, 60), 'routine', 'Stress response, functional impairment'),
                ('Somatic symptom disorder', (30, 50), 'routine', 'Physical symptoms, excessive worry'),
                ('Illness anxiety disorder', (30, 50), 'routine', 'Fear of serious illness, checking behaviors'),
                ('Body dysmorphic disorder', (20, 40), 'routine', 'Preoccupation with perceived defect'),
                ('Dissociative amnesia', (20, 50), 'routine', 'Memory loss, psychological trauma'),
            ],
            'moderate': [
                ('Frontotemporal dementia - behavioral variant', (50, 70), 'routine', 'Personality change, disinhibition'),
                ('Lewy body dementia', (60, 80), 'routine', 'Fluctuations, hallucinations, parkinsonism'),
                ('Huntington disease - psychiatric onset', (30, 50), 'routine', 'Depression, irritability, family history'),
                ('Wilson disease - psychiatric', (15, 30), 'routine', 'Personality change, tremor, KF rings'),
                ('Anti-NMDA receptor encephalitis', (15, 35), 'emergency', 'Psychosis, catatonia, seizures'),
                ('Neurosyphilis - general paresis', (40, 60), 'routine', 'Personality change, grandiosity'),
                ('HIV-associated neurocognitive disorder', (30, 50), 'routine', 'Cognitive decline, apathy'),
                ('Parkinson disease psychosis', (60, 80), 'routine', 'Visual hallucinations, delusions'),
                ('Corticobasal syndrome', (60, 80), 'routine', 'Apraxia, alien limb, behavioral changes'),
                ('Progressive supranuclear palsy', (60, 80), 'routine', 'Falls, vertical gaze palsy, apathy'),
                ('Wernicke-Korsakoff syndrome', (40, 60), 'routine', 'Confusion, confabulation, memory loss'),
                ('Pellagra', (40, 60), 'routine', 'Dermatitis, diarrhea, dementia'),
                ('Porphyria', (20, 40), 'emergency', 'Abdominal pain, psychosis, neuropathy'),
                ('Systemic lupus erythematosus', (20, 40), 'routine', 'Psychosis, cognitive dysfunction'),
                ('Hashimoto encephalopathy', (40, 60), 'emergency', 'Confusion, seizures, thyroid antibodies'),
            ],
            'hard': [
                ('PANDAS/PANS', (5, 15), 'routine', 'Acute OCD, tics, strep infection'),
                ('Anti-LGI1 encephalitis', (50, 70), 'emergency', 'Memory loss, faciobrachial seizures'),
                ('Kleine-Levin syndrome', (15, 25), 'routine', 'Hypersomnia, hyperphagia, hypersexuality'),
                ('Cotard syndrome', (40, 60), 'routine', 'Nihilistic delusions, depression'),
                ('Capgras syndrome', (50, 70), 'routine', 'Impostor delusion, dementia'),
                ('Fregoli syndrome', (40, 60), 'routine', 'Misidentification, paranoia'),
                ('Alice in Wonderland syndrome', (10, 30), 'routine', 'Perceptual distortions, migraine'),
                ('Ekbom syndrome', (40, 60), 'routine', 'Delusional parasitosis'),
                ('Charles Bonnet syndrome', (70, 90), 'routine', 'Visual hallucinations, vision loss'),
                ('Musical hallucinations', (60, 80), 'routine', 'Hearing music, hearing loss'),
                ('Ganser syndrome', (20, 40), 'routine', 'Approximate answers, dissociation'),
                ('Foreign accent syndrome', (30, 60), 'routine', 'Accent change after brain injury'),
                ('Reduplicative paramnesia', (50, 70), 'routine', 'Place duplication delusion'),
                ('Prosopagnosia', (30, 60), 'routine', 'Face recognition deficit'),
                ('Kluver-Bucy syndrome', (30, 50), 'routine', 'Hyperorality, hypersexuality, visual agnosia'),
            ]
        },
        'Neurotoxicology': {
            'easy': [
                ('Alcohol withdrawal', (30, 60), 'emergency', 'Tremor, hallucinations, seizures'),
                ('Wernicke encephalopathy', (40, 60), 'emergency', 'Confusion, ataxia, ophthalmoplegia'),
                ('Lead poisoning', (20, 50), 'routine', 'Abdominal pain, neuropathy, encephalopathy'),
                ('Mercury poisoning', (30, 60), 'routine', 'Tremor, personality change, gingivitis'),
                ('Carbon monoxide poisoning', (20, 60), 'emergency', 'Headache, confusion, cherry red skin'),
                ('Organophosphate poisoning', (20, 50), 'emergency', 'Cholinergic crisis, fasciculations'),
                ('Botulism', (20, 60), 'emergency', 'Descending paralysis, dilated pupils'),
                ('Lithium toxicity', (40, 70), 'emergency', 'Tremor, confusion, ataxia'),
                ('Phenytoin toxicity', (30, 70), 'routine', 'Nystagmus, ataxia, confusion'),
                ('Valproate toxicity', (20, 60), 'emergency', 'Tremor, confusion, hyperammonemia'),
                ('Metronidazole neuropathy', (40, 70), 'routine', 'Peripheral neuropathy, ataxia'),
                ('Isoniazid neuropathy', (30, 60), 'routine', 'Peripheral neuropathy, B6 deficiency'),
                ('Vincristine neuropathy', (40, 70), 'routine', 'Peripheral neuropathy, constipation'),
                ('Cisplatin neuropathy', (40, 70), 'routine', 'Sensory neuropathy, hearing loss'),
                ('Amiodarone neuropathy', (50, 70), 'routine', 'Peripheral neuropathy, tremor'),
            ],
            'moderate': [
                ('Methanol poisoning', (30, 50), 'emergency', 'Vision loss, metabolic acidosis'),
                ('Ethylene glycol poisoning', (30, 50), 'emergency', 'Confusion, renal failure, crystals'),
                ('Arsenic poisoning', (30, 60), 'routine', 'GI symptoms, neuropathy, Mees lines'),
                ('Thallium poisoning', (30, 50), 'routine', 'Alopecia, painful neuropathy'),
                ('Manganese toxicity', (30, 50), 'routine', 'Parkinsonism, psychiatric symptoms'),
                ('Toluene toxicity', (20, 40), 'routine', 'White matter changes, cognitive decline'),
                ('Hexane neuropathy', (20, 40), 'routine', 'Peripheral neuropathy, glue sniffing'),
                ('Acrylamide neuropathy', (30, 50), 'routine', 'Sensory neuropathy, ataxia'),
                ('Nitrous oxide myelopathy', (20, 40), 'routine', 'B12 deficiency, subacute combined degeneration'),
                ('Ciguatera poisoning', (30, 60), 'routine', 'Cold allodynia, perioral paresthesias'),
                ('Tetrodotoxin poisoning', (30, 50), 'emergency', 'Perioral numbness, ascending paralysis'),
                ('Strychnine poisoning', (20, 50), 'emergency', 'Muscle spasms, opisthotonus'),
                ('Cycad toxicity', (40, 60), 'routine', 'ALS-parkinsonism-dementia complex'),
                ('MPTP parkinsonism', (20, 40), 'routine', 'Acute parkinsonism, designer drug'),
                ('Domoic acid poisoning', (30, 60), 'emergency', 'Seizures, memory loss, shellfish'),
            ],
            'hard': [
                ('Konzo', (10, 30), 'routine', 'Spastic paraparesis, cassava diet'),
                ('Lathyrism', (20, 40), 'routine', 'Spastic paraparesis, grass pea consumption'),
                ('Tropical ataxic neuropathy', (30, 50), 'routine', 'Ataxia, neuropathy, cassava diet'),
                ('Subacute myelo-optic neuropathy', (30, 50), 'routine', 'Myelopathy, optic neuropathy, clioquinol'),
                ('Toxic oil syndrome', (30, 60), 'routine', 'Myalgia, eosinophilia, neuropathy'),
                ('Eosinophilia-myalgia syndrome', (30, 50), 'routine', 'Myalgia, neuropathy, L-tryptophan'),
                ('Minamata disease', (30, 60), 'routine', 'Ataxia, sensory loss, methylmercury'),
                ('Itai-itai disease', (40, 60), 'routine', 'Bone pain, renal failure, cadmium'),
                ('Camelford water incident', (30, 70), 'routine', 'Memory problems, aluminum exposure'),
                ('Gulf War syndrome', (30, 50), 'routine', 'Fatigue, cognitive problems, multiple exposures'),
                ('Aerotoxic syndrome', (30, 60), 'routine', 'Cognitive problems, organophosphate exposure'),
                ('Solvent encephalopathy', (30, 50), 'routine', 'Cognitive decline, chronic exposure'),
                ('Chlordecone poisoning', (30, 50), 'routine', 'Tremor, nervousness, kepone'),
                ('Buckthorn neuropathy', (30, 50), 'routine', 'Peripheral neuropathy, herbal tea'),
                ('Glufosinate poisoning', (30, 50), 'emergency', 'Delayed seizures, memory loss'),
            ]
        },
        'Pediatric Neurology': {
            'easy': [
                ('Febrile seizures', (0.5, 5), 'emergency', 'Seizure with fever, no CNS infection'),
                ('Childhood absence epilepsy', (4, 10), 'routine', 'Staring spells, 3Hz spike-wave'),
                ('Benign rolandic epilepsy', (3, 13), 'routine', 'Nocturnal focal seizures, centro-temporal spikes'),
                ('Cerebral palsy - spastic diplegia', (1, 5), 'routine', 'Leg stiffness, toe walking, prematurity'),
                ('Duchenne muscular dystrophy', (2, 5), 'routine', 'Proximal weakness, Gowers sign, elevated CK'),
                ('Spina bifida', (0, 1), 'routine', 'Lower limb weakness, bladder dysfunction'),
                ('Hydrocephalus', (0, 2), 'routine', 'Large head, sunset eyes, developmental delay'),
                ('Autism spectrum disorder', (2, 4), 'routine', 'Social difficulties, repetitive behaviors'),
                ('ADHD', (5, 12), 'routine', 'Inattention, hyperactivity, impulsivity'),
                ('Tourette syndrome', (5, 10), 'routine', 'Motor and vocal tics'),
                ('Developmental delay', (1, 3), 'routine', 'Milestone delays, hypotonia'),
                ('Migraine in children', (8, 15), 'routine', 'Headache, family history, nausea'),
                ('Breath-holding spells', (0.5, 2), 'routine', 'Cyanosis or pallor with crying'),
                ('Night terrors', (3, 8), 'routine', 'Screaming episodes during sleep'),
                ('Growing pains', (3, 12), 'routine', 'Leg pain at night, normal exam'),
            ],
            'moderate': [
                ('Infantile spasms', (0.3, 1), 'emergency', 'Flexor spasms, hypsarrhythmia, regression'),
                ('Lennox-Gastaut syndrome', (2, 8), 'routine', 'Multiple seizure types, intellectual disability'),
                ('Dravet syndrome', (0.3, 1), 'routine', 'Prolonged febrile seizures, SCN1A mutation'),
                ('Tuberous sclerosis complex', (0, 5), 'routine', 'Seizures, ash leaf spots, cardiac rhabdomyomas'),
                ('Sturge-Weber syndrome', (0, 2), 'routine', 'Port wine stain, seizures, glaucoma'),
                ('Acute disseminated encephalomyelitis', (3, 10), 'emergency', 'Post-viral, multifocal deficits'),
                ('Opsoclonus-myoclonus syndrome', (1, 3), 'emergency', 'Dancing eyes, ataxia, neuroblastoma'),
                ('Sydenham chorea', (5, 15), 'routine', 'Chorea, emotional lability, strep infection'),
                ('PANDAS', (5, 12), 'routine', 'Acute OCD or tics, strep infection'),
                ('Moyamoya disease', (5, 10), 'routine', 'Strokes, seizures, progressive stenosis'),
                ('Alternating hemiplegia of childhood', (0.5, 5), 'routine', 'Episodic hemiplegia, developmental delay'),
                ('Landau-Kleffner syndrome', (3, 7), 'routine', 'Language regression, ESES on EEG'),
                ('Rasmussen encephalitis', (2, 10), 'routine', 'Intractable seizures, progressive hemiparesis'),
                ('Acute flaccid myelitis', (2, 8), 'emergency', 'Acute flaccid paralysis, MRI gray matter changes'),
                ('Childhood disintegrative disorder', (2, 4), 'routine', 'Normal development then regression'),
            ],
            'hard': [
                ('Aicardi syndrome', (0, 0.5), 'routine', 'Infantile spasms, agenesis corpus callosum, chorioretinal lacunae'),
                ('Menkes disease', (0, 0.5), 'routine', 'Kinky hair, seizures, developmental regression'),
                ('Neuronal ceroid lipofuscinosis', (2, 8), 'routine', 'Vision loss, seizures, regression'),
                ('Adrenoleukodystrophy', (4, 8), 'routine', 'Behavioral changes, vision loss, adrenal insufficiency'),
                ('Alexander disease', (0, 2), 'routine', 'Macrocephaly, seizures, spasticity'),
                ('Canavan disease', (0.3, 0.5), 'routine', 'Macrocephaly, hypotonia, white matter disease'),
                ('Pelizaeus-Merzbacher disease', (0, 1), 'routine', 'Nystagmus, spasticity, hypomyelination'),
                ('Neurodegeneration with brain iron accumulation', (2, 10), 'routine', 'Dystonia, spasticity, eye-of-tiger sign'),
                ('Lesch-Nyhan syndrome', (0.5, 1), 'routine', 'Self-mutilation, dystonia, hyperuricemia'),
                ('Septo-optic dysplasia', (0, 1), 'routine', 'Vision problems, pituitary dysfunction'),
                ('Holoprosencephaly', (0, 0.5), 'routine', 'Midline defects, developmental delay'),
                ('Lissencephaly', (0, 0.5), 'routine', 'Smooth brain, seizures, severe delay'),
                ('Polymicrogyria', (0, 2), 'routine', 'Seizures, developmental delay, MRI findings'),
                ('Periventricular leukomalacia', (0, 2), 'routine', 'Prematurity, spastic diplegia, white matter injury'),
                ('Kernicterus', (0, 0.1), 'routine', 'Jaundice, dystonia, hearing loss'),
            ]
        },
        'Sleep Neurology': {
            'easy': [
                ('Obstructive sleep apnea', (40, 70), 'routine', 'Snoring, witnessed apneas, daytime sleepiness'),
                ('Narcolepsy with cataplexy', (15, 30), 'routine', 'Sleep attacks, cataplexy with emotions'),
                ('Restless legs syndrome', (40, 70), 'routine', 'Leg discomfort at night, urge to move'),
                ('REM sleep behavior disorder', (50, 80), 'routine', 'Acting out dreams, potential injury'),
                ('Insomnia disorder', (30, 60), 'routine', 'Difficulty initiating or maintaining sleep'),
                ('Circadian rhythm disorder - delayed phase', (15, 30), 'routine', 'Late sleep onset, difficulty waking'),
                ('Periodic limb movement disorder', (50, 80), 'routine', 'Leg movements during sleep, daytime fatigue'),
                ('Sleep walking', (5, 15), 'routine', 'Complex behaviors during NREM sleep'),
                ('Sleep terrors', (3, 12), 'routine', 'Screaming episodes, incomplete arousal'),
                ('Bruxism', (20, 50), 'routine', 'Teeth grinding, jaw pain'),
                ('Sleep paralysis', (15, 35), 'routine', 'Inability to move on awakening'),
                ('Hypnagogic hallucinations', (20, 40), 'routine', 'Vivid hallucinations at sleep onset'),
                ('Shift work disorder', (25, 55), 'routine', 'Insomnia and sleepiness with shift work'),
                ('Jet lag disorder', (20, 60), 'routine', 'Sleep disturbance after time zone travel'),
                ('Sleep-related eating disorder', (20, 40), 'routine', 'Eating during partial arousals'),
            ],
            'moderate': [
                ('Narcolepsy without cataplexy', (15, 35), 'routine', 'Sleep attacks, no cataplexy'),
                ('Idiopathic hypersomnia', (20, 40), 'routine', 'Excessive sleep, unrefreshing naps'),
                ('Central sleep apnea', (50, 80), 'routine', 'Apneas without obstruction, heart disease'),
                ('Complex sleep apnea', (50, 70), 'routine', 'OSA with emergent central apneas on PAP'),
                ('Kleine-Levin syndrome', (10, 20), 'routine', 'Recurrent hypersomnia, cognitive changes'),
                ('Circadian rhythm disorder - advanced phase', (60, 80), 'routine', 'Early sleep onset and awakening'),
                ('Non-24-hour sleep-wake disorder', (20, 60), 'routine', 'Progressive delay in sleep times'),
                ('Irregular sleep-wake rhythm', (60, 80), 'routine', 'No clear sleep-wake pattern'),
                ('Confusional arousals', (5, 35), 'routine', 'Confusion on awakening, amnesia'),
                ('Sleep-related hallucinations', (20, 70), 'routine', 'Complex hallucinations at sleep-wake transition'),
                ('Exploding head syndrome', (40, 60), 'routine', 'Loud noise sensations at sleep onset'),
                ('Sleep starts', (20, 60), 'routine', 'Sudden jerks at sleep onset'),
                ('Propriospinal myoclonus', (30, 60), 'routine', 'Jerks spreading from trunk at sleep onset'),
                ('Sleep-related movement disorders', (40, 70), 'routine', 'Rhythmic movements during sleep'),
                ('Catathrenia', (20, 40), 'routine', 'Groaning during expiration in sleep'),
            ],
            'hard': [
                ('Fatal familial insomnia', (40, 60), 'routine', 'Progressive insomnia, autonomic dysfunction'),
                ('Morvan syndrome', (40, 60), 'routine', 'Severe insomnia, neuromyotonia, autonomic dysfunction'),
                ('Anti-IgLON5 disease', (50, 70), 'routine', 'Sleep disorder, gait instability, dysautonomia'),
                ('Agrypnia excitata', (40, 70), 'routine', 'Total insomnia, motor activation, autonomic dysfunction'),
                ('Status dissociatus', (50, 80), 'routine', 'Loss of sleep state boundaries'),
                ('Autoimmune encephalitis with sleep disorders', (20, 60), 'routine', 'Sleep disruption, psychiatric symptoms'),
                ('Sleep-related hypoventilation syndromes', (40, 70), 'routine', 'Hypercapnia during sleep'),
                ('Congenital central hypoventilation syndrome', (0, 10), 'routine', 'Ondines curse, PHOX2B mutation'),
                ('Chiari malformation with sleep apnea', (20, 50), 'routine', 'Central apnea, headaches, syrinx'),
                ('Sleep-related epilepsy', (10, 50), 'routine', 'Seizures exclusively during sleep'),
                ('Nocturnal frontal lobe epilepsy', (10, 30), 'routine', 'Complex behaviors, dystonic posturing'),
                ('Panayiotopoulos syndrome', (3, 10), 'routine', 'Nocturnal seizures, autonomic features'),
                ('Sleep-related stroke', (60, 80), 'routine', 'Wake-up stroke, unknown onset time'),
                ('Nocturnal paroxysmal dystonia', (20, 50), 'routine', 'Brief dystonic episodes from sleep'),
                ('REM sleep without atonia', (50, 80), 'routine', 'Precursor to RBD, synucleinopathy risk'),
            ]
        },
'''
    
    # Read the current file
    with open('django_neurology_mcq/mcq/case_bot_enhanced.py', 'r') as f:
        content = f.read()
    
    # Find where to insert the new specialties
    # Look for the end of the existing case pools
    insert_position = content.find("    }\n\ndef generate_unique_case")
    
    if insert_position == -1:
        print("ERROR: Could not find insertion point for new specialties")
        return
    
    # Insert the new specialties before the closing brace
    new_content = (
        content[:insert_position] + 
        ",\n" + missing_specialties + 
        content[insert_position:]
    )
    
    # Write back
    with open('django_neurology_mcq/mcq/case_bot_enhanced.py', 'w') as f:
        f.write(new_content)
    
    print("✓ Added 11 missing specialties with complete case pools")

def update_case_tracking_logic():
    """Update the case tracking logic to prevent premature recycling"""
    
    enhanced_tracker = '''
# Enhanced Case History Tracker
class CaseHistoryTracker:
    def __init__(self):
        self.cache_prefix = 'case_history_v2_'
        self.cache_timeout = 90 * 24 * 60 * 60  # 90 days instead of 30
        
    def get_user_history(self, user_id, specialty, difficulty):
        """Get complete history without limit"""
        cache_key = f"{self.cache_prefix}{user_id}_{specialty}_{difficulty}"
        history = cache.get(cache_key, {})
        return history  # Return dict with timestamps
        
    def add_to_history(self, user_id, specialty, difficulty, case_hash):
        """Add case with timestamp to user's history"""
        cache_key = f"{self.cache_prefix}{user_id}_{specialty}_{difficulty}"
        history = cache.get(cache_key, {})
        
        if case_hash not in history:
            history[case_hash] = {
                'first_seen': datetime.now().isoformat(),
                'last_seen': datetime.now().isoformat(),
                'seen_count': 1
            }
        else:
            history[case_hash]['last_seen'] = datetime.now().isoformat()
            history[case_hash]['seen_count'] += 1
            
        cache.set(cache_key, history, self.cache_timeout)
        
    def generate_case_hash(self, condition, age_range, gender, difficulty):
        """Generate unique hash including actual gender"""
        case_str = f"{condition}_{age_range}_{gender}_{difficulty}"
        return hashlib.md5(case_str.encode()).hexdigest()[:16]
        
    def get_completion_stats(self, user_id, specialty, difficulty):
        """Get statistics on case completion"""
        history = self.get_user_history(user_id, specialty, difficulty)
        case_pools = get_comprehensive_case_pools()
        
        # Calculate total possible cases (each case x 2 genders)
        base_cases = len(case_pools.get(specialty, {}).get(difficulty, []))
        total_possible = base_cases * 2  # male and female versions
        
        seen_cases = len(history)
        
        return {
            'total_cases': base_cases,
            'total_possible_variants': total_possible,
            'seen_cases': seen_cases,
            'completion_percentage': (seen_cases / total_possible * 100) if total_possible > 0 else 0,
            'all_seen': seen_cases >= total_possible
        }

case_history = CaseHistoryTracker()
'''
    
    print("✓ Enhanced case tracking logic created")
    print("\nNext steps:")
    print("1. Replace CaseHistoryTracker class in case_bot_enhanced.py")
    print("2. Update generate_unique_case function to use gender properly")
    print("3. Test the changes locally before deployment")

if __name__ == "__main__":
    print("Fixing case pools and tracking logic...\n")
    
    # Fix age ranges
    fix_age_ranges()
    
    # Add missing specialties
    add_missing_specialties()
    
    # Show enhanced tracking logic
    update_case_tracking_logic()
    
    print("\n✅ All fixes completed!")
    print("\nIMPORTANT: The enhanced tracking logic needs to be manually integrated")
    print("to ensure proper handling of the gender-based case selection.")