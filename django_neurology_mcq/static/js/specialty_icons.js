/**
 * Neurology Subspecialty Icons
 * This file contains the icon definitions and helper functions for displaying
 * specialty-specific icons throughout the application.
 */

// Map of subspecialty names to their detailed information
const NEUROLOGY_SPECIALTIES = {
  "Critical Care Neurology": {
    icon: "brain-circuit-icu",
    color: "#e53e3e",
    description: "Focuses on life-threatening neurological conditions requiring intensive care",
    className: "specialty-critical"
  },
  "Dementia": {
    icon: "brain-fragments",
    color: "#718096",
    description: "Specializes in cognitive disorders and memory impairment in adults",
    className: "specialty-dementia"
  },
  "Epilepsy": {
    icon: "brain-waves",
    color: "#805ad5",
    description: "Focuses on seizure disorders and their treatment",
    className: "specialty-epilepsy"
  },
  "Headache": {
    icon: "head-pulse",
    color: "#d69e2e",
    description: "Specializes in various types of headaches and treatment strategies",
    className: "specialty-headache"
  },
  "Movement Disorders": {
    icon: "brain-tremor",
    color: "#38a169",
    description: "Concentrates on conditions affecting movement control like Parkinson's disease",
    className: "specialty-movement"
  },
  "Neuroanatomy": {
    icon: "brain-structure",
    color: "#d53f8c",
    description: "Study of the anatomy and organization of the nervous system",
    className: "specialty-neuroanatomy"
  },
  "Neurogenetics": {
    icon: "dna-neuron",
    color: "#319795",
    description: "Studies genetic influences on neurological development and disease",
    className: "specialty-neurogenetics"
  },
  "Neuroimmunology": {
    icon: "brain-shield",
    color: "#3182ce",
    description: "Focuses on immune system interactions with the nervous system",
    className: "specialty-neuroimmune"
  },
  "Neuro-infectious": {
    icon: "brain-virus",
    color: "#dd6b20",
    description: "Specializes in infections affecting the nervous system",
    className: "specialty-neuroinfectious"
  },
  "Neuro-oncology": {
    icon: "brain-tumor",
    color: "#d53f8c",
    description: "Focuses on tumors of the brain and nervous system",
    className: "specialty-neurooncology"
  },
  "Neuro-otology": {
    icon: "ear-brain",
    color: "#4299e1",
    description: "Specializes in neurological disorders affecting hearing and balance",
    className: "specialty-neurootology"
  },
  "Neuroophthalmology": {
    icon: "eye-brain",
    color: "#6b46c1",
    description: "Focuses on visual problems related to the nervous system",
    className: "specialty-neuroophthalmology"
  },
  "Neuropsychiatry": {
    icon: "brain-mind",
    color: "#667eea",
    description: "Bridges neurology and psychiatry to treat mental disorders with neurological bases",
    className: "specialty-neuropsychiatry"
  },
  "Neurotoxicology": {
    icon: "brain-toxin",
    color: "#718096",
    description: "Studies effects of toxins on the nervous system",
    className: "specialty-neurotoxicology"
  },
  "Neuromuscular": {
    icon: "nerve-muscle",
    color: "#dd6b20",
    description: "Focuses on disorders affecting nerves controlling muscles",
    className: "specialty-neuromuscular"
  },
  "Pediatric Neurology": {
    icon: "child-brain",
    color: "#3182ce",
    description: "Specializes in neurological disorders in children",
    className: "specialty-pediatric"
  },
  "Sleep Neurology": {
    icon: "brain-wave-sleep",
    color: "#5a67d8",
    description: "Focuses on neurological aspects of sleep disorders",
    className: "specialty-sleep"
  },
  "Vascular Neurology/Stroke": {
    icon: "brain-vessel",
    color: "#e53e3e",
    description: "Specializes in stroke and other cerebrovascular diseases",
    className: "specialty-vascular"
  },
  "Other/Unclassified": {
    icon: "brain-misc",
    color: "#6b46c1",
    description: "Other neurological specialties and interdisciplinary areas",
    className: "specialty-other"
  }
};

// SVG icon definitions - using custom paths to create unique neurological icons
const SPECIALTY_ICONS = {
  // Critical Care Neurology - Brain with monitoring lines/ICU elements
  "brain-circuit-icu": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M3 18v1h18v-1" class="monitor-path"/>
      <path d="M4 22h16" class="monitor-path"/>
      <path d="M7 18v4" class="monitor-path"/>
      <path d="M17 18v4" class="monitor-path"/>
      <path d="M8 14l2-2 2 2 2-2 2 2" class="ekg-path"/>
    </svg>
  `,
  
  // Dementia - Brain with fragmented/disconnected sections
  "brain-fragments": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M8 6c0-1.1.9-2 2-2s2 .9 2 2" class="brain-path"/>
      <path d="M12 4c1.1 0 2 .9 2 2s-.9 2-2 2" class="brain-path"/>
      <path d="M16 6c0-1.1-.9-2-2-2" class="brain-path"/>
      <path d="M12 8c-1.1 0-2-.9-2-2" class="brain-path"/>
      <path d="M8 10c0-1.1.9-2 2-2s2 .9 2 2" class="brain-path"/>
      <path d="M12 8c1.1 0 2 .9 2 2s-.9 2-2 2" class="brain-path"/>
      <path d="M16 10c0-1.1-.9-2-2-2" class="brain-path"/>
      <path d="M12 12c-1.1 0-2-.9-2-2" class="brain-path"/>
      <path d="M8 14c0-1.1.9-2 2-2s2 .9 2 2" class="brain-path"/>
      <path d="M12 12c1.1 0 2 .9 2 2s-.9 2-2 2" class="brain-path"/>
      <path d="M16 14c0-1.1-.9-2-2-2" class="brain-path"/>
      <path d="M12 16c-1.1 0-2-.9-2-2" class="brain-path"/>
    </svg>
  `,
  
  // Epilepsy - Brain with wave/seizure activity
  "brain-waves": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M7 10l2-2 2 2 2-2 4 4" class="eeg-path"/>
      <path d="M7 14l2-4 2 4 2-4 4 4" class="eeg-path"/>
    </svg>
  `,
  
  // Headache - Head profile with pain indicators
  "head-pulse": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M16 8c0-3.87-3.13-7-7-7-3.87 0-7 3.13-7 7 0 2.38 1.19 4.47 3 5.74V16c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74z" class="head-path"/>
      <path d="M10 8l4 4" class="pulse-path"/>
      <path d="M14 8l-4 4" class="pulse-path"/>
      <path d="M6 6l2 2" class="pulse-path"/>
      <path d="M8 6l-2 2" class="pulse-path"/>
    </svg>
  `,
  
  // Movement Disorders - Brain with tremor lines
  "brain-tremor": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M9 18v3" class="tremor-path"/>
      <path d="M9 19.5H7" class="tremor-path"/>
      <path d="M9 21H7" class="tremor-path"/>
      <path d="M9 18H7" class="tremor-path"/>
      <path d="M15 18v3" class="tremor-path"/>
      <path d="M15 19.5h2" class="tremor-path"/>
      <path d="M15 21h2" class="tremor-path"/>
      <path d="M15 18h2" class="tremor-path"/>
    </svg>
  `,
  
  // Neuroanatomy - Detailed brain structure
  "brain-structure": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M8 12c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z" class="structure-path"/>
      <path d="M16 12c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z" class="structure-path"/>
      <path d="M12 7c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1z" class="structure-path"/>
      <path d="M12 16c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1z" class="structure-path"/>
    </svg>
  `,
  
  // Neurogenetics - DNA helix with neuron
  "dna-neuron": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M5 4l14 0" class="dna-path"/>
      <path d="M5 8l14 0" class="dna-path"/>
      <path d="M5 12l14 0" class="dna-path"/>
      <path d="M5 16l14 0" class="dna-path"/>
      <path d="M5 20l14 0" class="dna-path"/>
      <path d="M7 4l0 16" class="dna-path"/>
      <path d="M17 4l0 16" class="dna-path"/>
      <path d="M12 2v3c0 1.1-.9 2-2 2H7" class="neuron-path"/>
      <path d="M12 22v-3c0-1.1-.9-2-2-2H7" class="neuron-path"/>
      <path d="M12 2v3c0 1.1.9 2 2 2h3" class="neuron-path"/>
      <path d="M12 22v-3c0-1.1.9-2 2-2h3" class="neuron-path"/>
    </svg>
  `,
  
  // Neuroimmunology - Brain with shield/immune system
  "brain-shield": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M12 2l-7 3v5c0 4.4 2.9 8.4 7 9.8 4.1-1.4 7-5.4 7-9.8V5l-7-3z" class="shield-path" style="opacity: 0.3;"/>
      <path d="M12 5v9l5-5" class="checkmark-path"/>
    </svg>
  `,
  
  // Neuro-infectious - Brain with virus particles
  "brain-virus": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <circle cx="8" cy="8" r="1" class="virus-path"/>
      <circle cx="14" cy="6" r="1" class="virus-path"/>
      <circle cx="16" cy="11" r="1" class="virus-path"/>
      <circle cx="10" cy="12" r="1" class="virus-path"/>
      <path d="M8 8l-1-1M8 8l1-1M8 8l-1 1M8 8l1 1" class="virus-spike-path"/>
      <path d="M14 6l-1-1M14 6l1-1M14 6l-1 1M14 6l1 1" class="virus-spike-path"/>
      <path d="M16 11l-1-1M16 11l1-1M16 11l-1 1M16 11l1 1" class="virus-spike-path"/>
      <path d="M10 12l-1-1M10 12l1-1M10 12l-1 1M10 12l1 1" class="virus-spike-path"/>
    </svg>
  `,
  
  // Neuro-oncology - Brain with tumor representation
  "brain-tumor": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <circle cx="14" cy="10" r="3" class="tumor-path"/>
      <path d="M13 7l2 2M12 8l3 3M11 9l3 3M12 10l2 2" class="tumor-detail-path"/>
    </svg>
  `,
  
  // Neuro-otology - Ear connected to brain representation
  "ear-brain": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M16 10c0-3.87-3.13-7-7-7-3.87 0-7 3.13-7 7 0 2.38 1.19 4.47 3 5.74V18c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74z" class="brain-path"/>
      <path d="M17 8c1.7 0 3-1.3 3-3s-1.3-3-3-3-3 1.3-3 3c0 1.7 1.3 3 3 3z" class="ear-path"/>
      <path d="M14 7l2-2" class="connection-path"/>
      <path d="M17 8l0 3" class="ear-canal-path"/>
      <circle cx="17" cy="13" r="1" class="eardrum-path"/>
    </svg>
  `,
  
  // Neuroophthalmology - Eye connected to brain
  "eye-brain": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M16 10c0-3.87-3.13-7-7-7-3.87 0-7 3.13-7 7 0 2.38 1.19 4.47 3 5.74V18c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74z" class="brain-path"/>
      <path d="M14 7l2-2" class="connection-path"/>
      <path d="M19 8c-2.8 0-5 2.2-5 5s2.2 5 5 5 5-2.2 5-5-2.2-5-5-5z" class="eye-path"/>
      <circle cx="19" cy="13" r="2" class="pupil-path"/>
    </svg>
  `,
  
  // Neuropsychiatry - Brain with emotional/mental representation
  "brain-mind": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M9 8c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1z" class="emotion-path"/>
      <path d="M15 8c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1z" class="emotion-path"/>
      <path d="M9 12c1.3 0 2.5.4 3 1 .5-.6 1.7-1 3-1" class="emotion-path"/>
    </svg>
  `,
  
  // Neurotoxicology - Brain with toxin symbol
  "brain-toxin": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M10 20h4l1 2H9z" class="hazard-path"/>
      <path d="M9 18h6l1 2H8z" class="hazard-path"/>
      <path d="M12 6l2 3.5-2 3.5-2-3.5z" class="toxin-path"/>
    </svg>
  `,
  
  // Neuromuscular - Nerve connected to muscle
  "nerve-muscle": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M12 18v2" class="nerve-path"/>
      <path d="M10 20h4" class="nerve-path"/>
      <path d="M9 20c-1.1 0-2 .9-2 2h10c0-1.1-.9-2-2-2z" class="muscle-path"/>
      <path d="M7 22h10" class="muscle-path"/>
    </svg>
  `,
  
  // Pediatric Neurology - Child silhouette with brain
  "child-brain": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <circle cx="12" cy="5" r="3" class="head-path"/>
      <path d="M12 8v4" class="body-path"/>
      <path d="M10 10l2 2l2-2" class="body-path"/>
      <path d="M12 12l-1 4" class="body-path"/>
      <path d="M12 12l1 4" class="body-path"/>
      <path d="M10 6c.83-.84 2.17-.84 3 0" class="brain-path"/>
      <path d="M10 5h3" class="brain-path"/>
      <path d="M10 4c.83.84 2.17.84 3 0" class="brain-path"/>
    </svg>
  `,
  
  // Sleep Neurology - Brain with sleep waves
  "brain-wave-sleep": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M4 18c1.3-1 3.5-1 5 0 1.5-1 3.7-1 5 0" class="sleep-wave-path"/>
      <path d="M4 21c1.3-1 3.5-1 5 0 1.5-1 3.7-1 5 0" class="sleep-wave-path"/>
    </svg>
  `,
  
  // Vascular Neurology/Stroke - Brain with blood vessels
  "brain-vessel": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M8 7c.5-.5 1-1 2-1s2 .5 2.5 1 1 1 2 1 1.5-.5 2-1" class="vessel-path"/>
      <path d="M8 10c.5-.5 1-1 2-1s2 .5 2.5 1 1 1 2 1 1.5-.5 2-1" class="vessel-path"/>
      <path d="M8 13c.5-.5 1-1 2-1s2 .5 2.5 1 1 1 2 1 1.5-.5 2-1" class="vessel-path"/>
      <circle cx="14" cy="8" r="1" class="occlusion-path"/>
    </svg>
  `,
  
  // Other/Unclassified - Generic brain with question mark
  "brain-misc": `
    <svg viewBox="0 0 24 24" class="specialty-svg">
      <path d="M12 2C8.13 2 5 5.13 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.87-3.13-7-7-7z" class="brain-path"/>
      <path d="M12 12v1" class="question-path"/>
      <path d="M12 8v1" class="question-path"/>
      <path d="M10 6h4" class="question-path"/>
      <path d="M14 6v2c0 1.1-.9 2-2 2" class="question-path"/>
    </svg>
  `
};

/**
 * Returns SVG icon HTML for a given subspecialty
 * 
 * @param {string} subspecialtyName - The name of the subspecialty
 * @param {object} options - Options for rendering
 * @param {string} options.size - Size of the icon (sm, md, lg) - default: md
 * @param {boolean} options.colored - Whether to use the specialty color - default: true
 * @param {boolean} options.withText - Whether to include the subspecialty name - default: false
 * @param {string} options.customClass - Additional CSS classes to add
 * @returns {string} HTML for the subspecialty icon
 */
function getSpecialtyIcon(subspecialtyName, options = {}) {
  const defaults = {
    size: 'md',
    colored: true,
    withText: false,
    customClass: ''
  };
  
  const settings = { ...defaults, ...options };
  const specialty = NEUROLOGY_SPECIALTIES[subspecialtyName] || NEUROLOGY_SPECIALTIES["Other/Unclassified"];
  const iconSvg = SPECIALTY_ICONS[specialty.icon] || SPECIALTY_ICONS["brain-misc"];
  
  // Size classes
  const sizeClass = {
    'sm': 'icon-sm',
    'md': 'icon-md',
    'lg': 'icon-lg'
  }[settings.size] || 'icon-md';
  
  // Build the HTML
  const colorStyles = settings.colored ? `style="--icon-color: ${specialty.color};"` : '';
  const iconWrapper = `<div class="specialty-icon ${specialty.className} ${sizeClass} ${settings.customClass}" ${colorStyles}>${iconSvg}</div>`;
  
  if (settings.withText) {
    return `
      <div class="specialty-item">
        ${iconWrapper}
        <span class="specialty-name">${subspecialtyName}</span>
      </div>
    `;
  }
  
  return iconWrapper;
}

/**
 * Creates a specialty card with icon, name, description and optional stats
 * 
 * @param {string} subspecialtyName - The name of the subspecialty
 * @param {object} options - Options for the card
 * @param {number} options.count - Count of MCQs in this specialty (optional)
 * @param {number} options.completed - Count of completed MCQs (optional)
 * @param {string} options.customClass - Additional CSS classes to add
 * @returns {string} HTML for the specialty card
 */
function createSpecialtyCard(subspecialtyName, options = {}) {
  const defaults = {
    count: null,
    completed: null,
    customClass: ''
  };
  
  const settings = { ...defaults, ...options };
  const specialty = NEUROLOGY_SPECIALTIES[subspecialtyName] || NEUROLOGY_SPECIALTIES["Other/Unclassified"];
  
  // Calculate percentage if we have both count and completed
  let percentageHtml = '';
  if (settings.count !== null && settings.completed !== null && settings.count > 0) {
    const percentage = Math.round((settings.completed / settings.count) * 100);
    percentageHtml = `
      <div class="specialty-stats">
        <div class="d-flex justify-content-between align-items-center">
          <small class="text-muted">${settings.completed}/${settings.count} completed</small>
          <small class="text-muted">${percentage}%</small>
        </div>
        <div class="specialty-progress">
          <div class="progress-bar" role="progressbar" style="width: ${percentage}%"></div>
        </div>
      </div>
    `;
  }
  
  // Build the card HTML
  return `
    <div class="specialty-card ${specialty.className} ${settings.customClass}">
      <div class="card-body text-center">
        ${getSpecialtyIcon(subspecialtyName, { size: 'lg', colored: true })}
        <h3 class="specialty-title">${subspecialtyName}</h3>
        <p class="specialty-description">${specialty.description}</p>
        ${percentageHtml}
      </div>
    </div>
  `;
}

// Add CSS to the document
function initializeSpecialtyIcons() {
  // Add CSS styles for the icons if not already present
  if (!document.getElementById('specialty-icons-css')) {
    const iconStyles = document.createElement('style');
    iconStyles.id = 'specialty-icons-css';
    iconStyles.textContent = `
      .specialty-svg {
        width: 100%;
        height: 100%;
        stroke-width: 2;
        stroke-linecap: round;
        stroke-linejoin: round;
        fill: none;
      }
      
      .brain-path, .head-path {
        stroke: var(--icon-color, var(--neuro-primary));
        fill: rgba(var(--icon-color, var(--neuro-primary)), 0.1);
      }
      
      .monitor-path, .vessel-path, .nerve-path, .dna-path, .structure-path,
      .eeg-path, .ekg-path, .tremor-path, .connection-path, .synapse-path,
      .ear-path, .ear-canal-path, .eye-path, .question-path, .neuron-path,
      .shield-path, .emotion-path, .body-path, .checkmark-path, .sleep-wave-path {
        stroke: var(--icon-color, var(--neuro-primary));
      }
      
      .pupil-path, .eardrum-path, .tumor-path, .virus-path, .toxin-path, 
      .muscle-path, .hazard-path, .occlusion-path {
        stroke: var(--icon-color, var(--neuro-primary));
        fill: rgba(var(--icon-color, var(--neuro-primary)), 0.2);
      }
      
      .virus-spike-path {
        stroke: var(--icon-color, var(--neuro-primary));
        stroke-width: 1;
      }
      
      .specialty-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
      }
      
      .specialty-name {
        margin-top: 0.5rem;
        font-weight: 500;
      }
      
      .icon-sm {
        width: 24px;
        height: 24px;
      }
      
      .icon-md {
        width: 48px;
        height: 48px;
      }
      
      .icon-lg {
        width: 80px;
        height: 80px;
      }
      
      .specialty-description {
        font-size: 0.9rem;
        color: var(--neuro-grey-matter);
      }
    `;
    document.head.appendChild(iconStyles);
  }
  
  // Replace placeholder icons with SVG icons (skip case-based learning page)
  if (!document.querySelector('.specialty-card[data-case-specialty]')) {
    document.querySelectorAll('[data-specialty]').forEach(element => {
      // Skip elements that render their own specialty visuals (e.g., enhanced case-based learning)
      if (element.dataset.skipSpecialtyIcon === 'true') {
        return;
      }
      if (element.classList && element.classList.contains('cbl-card')) {
        return;
      }
      if (element.closest('[data-disable-specialty-icons]')) {
        return;
      }
      const hasExistingContent =
        element.childElementCount > 0 ||
        (element.textContent && element.textContent.trim().length > 0);
      if (hasExistingContent && element.dataset.forceSpecialtyIcon !== 'true') {
        return;
      }
      const subspecialty = element.dataset.specialty;
      const options = {
        size: element.dataset.size || 'md',
        colored: element.dataset.colored !== 'false',
        withText: element.dataset.withText === 'true',
        customClass: element.dataset.class || ''
      };
      
      element.innerHTML = getSpecialtyIcon(subspecialty, options);
    });
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeSpecialtyIcons);

// Export functions for use in other scripts
window.neurologyIcons = {
  getSpecialtyIcon,
  createSpecialtyCard,
  NEUROLOGY_SPECIALTIES
};
