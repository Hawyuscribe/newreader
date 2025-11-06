"""
Tracking Report View for MCQ-to-Case Conversion Debugging
"""

from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .case_conversion_tracker import conversion_tracker

@staff_member_required
def get_tracking_report(request, tracking_id):
    """
    Get comprehensive tracking report for a specific conversion
    """
    try:
        report = conversion_tracker.get_tracking_report(tracking_id)
        
        if not report:
            return JsonResponse({
                'error': f'No tracking data found for tracking ID: {tracking_id}'
            }, status=404)
        
        if request.GET.get('format') == 'json':
            return JsonResponse(report)
        
        # Render HTML view for easy reading
        return render(request, 'admin/tracking_report.html', {
            'tracking_id': tracking_id,
            'report': report
        })
        
    except Exception as e:
        return JsonResponse({
            'error': f'Error retrieving tracking report: {str(e)}'
        }, status=500)


@staff_member_required 
def search_tracking_reports(request):
    """
    Search tracking reports by MCQ ID or user ID
    """
    mcq_id = request.GET.get('mcq_id')
    user_id = request.GET.get('user_id')
    
    # This would require implementing search functionality in the tracker
    # For now, return instructions
    return JsonResponse({
        'message': 'Tracking search not yet implemented',
        'instructions': {
            'get_report': f'/admin/debug/tracking-report/{{tracking_id}}/',
            'tracking_id_format': 'track_{mcq_id}_{user_id}_{timestamp}',
            'example': f'/admin/debug/tracking-report/track_123_1_1672531200/'
        }
    })