# GPT-5-nano Optimization Configuration

# Model-specific settings
GPT5_NANO_SETTINGS = {
    "temperature": 0.4,      # Lower for more consistent output
    "top_p": 0.85,          # More focused than default 0.9
    "max_tokens": 500,      # Reduced from 600 for faster response
    "timeout": 20,          # Shorter timeout for nano model
    "retry_attempts": 2,    # Fewer retries for faster failing
}

# Prompt optimization settings
PROMPT_OPTIMIZATION = {
    "max_question_length": 200,     # Truncate long questions
    "max_instruction_length": 100,  # Limit custom instructions
    "use_concise_system_prompt": True,
    "skip_explanation_context": False,  # Keep for accuracy
}

# Cache settings (for future implementation)
CACHE_SETTINGS = {
    "enable_caching": True,
    "cache_ttl": 3600,  # 1 hour
    "cache_key_prefix": "gpt5_nano_options",
}

# Medical enhancement settings
MEDICAL_ENHANCEMENT = {
    "min_option_length": 20,     # Minimum characters for an option
    "target_option_length": 80,  # Target length for enhanced options
    "add_clinical_features": True,
    "add_diagnostic_details": True,
    "preserve_correct_answer": True,
}

# Error handling
ERROR_HANDLING = {
    "fallback_to_local_enhancement": True,
    "log_api_errors": True,
    "retry_on_empty_response": True,
    "max_retries": 2,
}

# Performance monitoring
MONITORING = {
    "track_processing_time": True,
    "log_improvement_ratio": True,
    "alert_on_slow_response": 10,  # seconds
    "track_model_usage": True,
}
