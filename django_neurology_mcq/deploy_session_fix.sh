#!/bin/bash

echo "🚀 Deploying MCQ-Case Session Fix to Heroku"
echo "=========================================="

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Not in Django project root directory"
    exit 1
fi

# Add and commit changes if needed
echo "📦 Checking git status..."
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  Uncommitted changes detected. Please commit them first."
    exit 1
fi

# Push to Heroku
echo "🔄 Pushing to Heroku..."
git push heroku stable_version:main

# Run migrations if needed
echo "🗄️ Running migrations..."
heroku run python manage.py migrate

# Clear cache to ensure fresh conversions
echo "🧹 Clearing MCQ conversion cache..."
heroku run python manage.py shell << 'EOF'
from django.core.cache import cache
print("Clearing all MCQ conversion caches...")
keys = cache.keys("mcq_case_conversion_*")
if keys:
    cache.delete_many(keys)
    print(f"Cleared {len(keys)} cache entries")
else:
    print("No cache entries found")
EOF

echo "✅ Deployment complete!"
echo ""
echo "📋 Next steps to test on Heroku:"
echo "1. Open an MCQ that previously showed wrong case content"
echo "2. Click 'Turn into Case-Based Learning'"
echo "3. Verify the case content matches the MCQ topic"
echo ""
echo "🔍 To monitor logs: heroku logs --tail"