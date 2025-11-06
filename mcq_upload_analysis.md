# MCQ Upload Methods to Heroku

## Current Situation Analysis

### JSON Structure
- Files contain MCQs with `question_number` that can repeat within same file
- Each MCQ has extensive explanation_sections with multiple subsections
- Files include metadata like exam_type and year at both file and MCQ level
- Field mapping discrepancies (JSON uses `options` as list of objects, DB expects JSONField dict)

### Database Schema
- `question_number` is CharField, NOT unique (allows duplicates)
- `options` field expects dictionary format
- `explanation_sections` is JSONField
- `exam_year` is IntegerField (JSON has `year` string)
- Primary key is auto-incrementing integer ID

## All Possible Upload Methods

### 1. Django Fixtures via loaddata
**How it works:**
- Convert JSON to Django fixture format
- Use `heroku run python manage.py loaddata`
- Django handles database operations

**Pros:**
- Built-in Django command
- Handles relationships properly
- Atomic transactions
- Clear error messages

**Cons:**
- Requires exact field matching
- Need unique PKs across all fixtures
- Can fail on first error in batch

### 2. Custom Management Command
**How it works:**
- Create custom Django command
- Deploy to Heroku
- Run via `heroku run python manage.py import_mcqs`

**Pros:**
- Full control over import logic
- Can handle complex transformations
- Better error handling
- Progress tracking

**Cons:**
- Requires code deployment
- Must maintain custom code

### 3. Direct Database Connection
**How it works:**
- Connect to Heroku PostgreSQL directly
- Use psycopg2 or similar to insert records

**Pros:**
- Fast bulk operations
- Bypasses Django ORM overhead
- Direct SQL control

**Cons:**
- Security risks
- Bypasses Django validations
- Harder to maintain

### 4. REST API Endpoint
**How it works:**
- Create API endpoint on Django
- POST MCQs via HTTP requests

**Pros:**
- Reusable for future imports
- Can be secured with authentication
- Allows remote uploads

**Cons:**
- Requires API development
- Slower for bulk operations
- Additional error handling needed

### 5. Admin Interface Upload
**How it works:**
- Add bulk upload to Django admin
- Upload CSV/JSON through web interface

**Pros:**
- User-friendly
- No command line needed
- Visual feedback

**Cons:**
- Limited by web timeout
- File size restrictions
- Requires admin access

### 6. S3 + Background Job
**How it works:**
- Upload files to S3
- Trigger background job to process

**Pros:**
- Handles large files
- Asynchronous processing
- Scalable

**Cons:**
- Complex setup
- Requires additional services
- Delay in processing

### 7. Shell Script with Chunks
**How it works:**
- Split JSON into chunks
- Upload chunks sequentially via shell

**Pros:**
- Simple to implement
- Can resume on failure
- Memory efficient

**Cons:**
- Multiple network calls
- Slower than bulk operations
- Need to manage state

### 8. Database Dump/Restore
**How it works:**
- Create PostgreSQL dump locally
- Restore to Heroku database

**Pros:**
- Fast for large datasets
- Preserves all data types
- Single operation

**Cons:**
- Overwrites existing data
- Requires database access
- All-or-nothing approach

### 9. CSV Import via pgcopy
**How it works:**
- Convert JSON to CSV
- Use PostgreSQL COPY command

**Pros:**
- Very fast
- Efficient for large datasets
- Native PostgreSQL feature

**Cons:**
- Limited data type support
- No validation
- Requires CSV conversion

### 10. Streaming Upload
**How it works:**
- Stream JSON data to Heroku
- Process line by line

**Pros:**
- Memory efficient
- Real-time processing
- Good for large files

**Cons:**
- Complex implementation
- Network dependency
- Error recovery challenges

## Recommended Approach Based on Your JSON Structure

Given your specific requirements:
- JSON files with duplicate question numbers (valid distinct questions)
- Complex nested explanation_sections
- Need to preserve all data including subsections
- Files already in JSON format

**Best Method: Enhanced Django Fixtures with Smart PK Management**

### Implementation Strategy:

1. **Pre-process JSON files to handle:**
   - Convert `options` from list to dictionary format
   - Map `year` to `exam_year`
   - Ensure all explanation_sections have required keys
   - Generate unique PKs starting from high number (e.g., 500000)

2. **Create fixtures with:**
   - Preserved original question_numbers
   - All explanation subsections intact
   - Proper field mapping
   - Unique PKs to avoid conflicts

3. **Upload using:**
   - Chunked fixtures (50-100 MCQs per chunk)
   - Sequential uploads with verification
   - Error recovery between chunks

4. **Verification after each chunk:**
   - Check count increase
   - Verify last uploaded MCQ
   - Log any failures for retry

This approach balances reliability, simplicity, and your specific data structure requirements.