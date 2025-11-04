import logging
from mcq.models import MCQ

logger = logging.getLogger(__name__)

class TemporaryMCQCleanupMiddleware:
    """Middleware to ensure temporary MCQs are always cleaned up properly."""
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Clean up pending deletions from previous requests
        if 'mcq_pending_deletion' in request.session:
            try:
                mcq_id = request.session.pop('mcq_pending_deletion')
                deleted = MCQ.objects.filter(id=mcq_id).delete()
                if deleted[0] > 0:
                    logger.info(f"Cleaned up pending MCQ deletion: {mcq_id}")
            except Exception as e:
                logger.error(f"Error cleaning up pending MCQ: {str(e)}")
        
        # Process the request
        response = self.get_response(request)
        
        # Clean up when navigating away from test_weakness
        if request.path != '/test_weakness/' and 'temp_weakness_mcq_id' in request.session:
            try:
                mcq_id = request.session.pop('temp_weakness_mcq_id')
                deleted = MCQ.objects.filter(id=mcq_id).delete()
                if deleted[0] > 0:
                    logger.info(f"Cleaned up temporary weakness test MCQ: {mcq_id}")
            except Exception as e:
                logger.error(f"Error cleaning up temporary MCQ: {str(e)}")
        
        return response