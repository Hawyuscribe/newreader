from mcq.models import MCQCaseConversionSession
# Get latest session
s = MCQCaseConversionSession.objects.first()
if s:
    print("Session ID:", s.id)
    print("MCQ ID:", s.mcq.id)
    print("Status:", s.status)
    if s.case_data:
        print("Case keys:", list(s.case_data.keys()))
        cp = s.case_data.get('clinical_presentation', 'None')
        print("Clinical presentation:", cp[:200] if cp else 'None')
else:
    print("No sessions found")