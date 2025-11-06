
from mcq.models import MCQ, Bookmark, Flashcard, Note, ReasoningSession

# Delete related models first
bookmark_count = Bookmark.objects.count()
print(f"Deleting {bookmark_count} bookmarks...")
Bookmark.objects.all().delete()

flashcard_count = Flashcard.objects.count()
print(f"Deleting {flashcard_count} flashcards...")
Flashcard.objects.all().delete()

note_count = Note.objects.count()
print(f"Deleting {note_count} notes...")
Note.objects.all().delete()

reasoning_count = ReasoningSession.objects.count()
print(f"Deleting {reasoning_count} reasoning sessions...")
ReasoningSession.objects.all().delete()

# Finally delete MCQs
count = MCQ.objects.count()
print(f"Deleting {count} MCQs...")
MCQ.objects.all().delete()
print("Done clearing all MCQs")
