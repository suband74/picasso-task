logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
   
    'formatters': {
        'main_format': {
            'format': '{asctime} - {levelname} - {filename} - {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'main_format',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'main_format',
            'filename': 'information.log'
        },
        },
    'loggers': {
        'main': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}