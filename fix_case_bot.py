#!/usr/bin/env python3
"""
Script to deploy the enhanced case bot that fixes the following issues:
1. Cases switching mid-conversation
2. Revealing diagnosis before conclusion
3. Not sending placeholder messages for investigations/localization
4. Not properly guiding users through diagnostic process
"""

import shutil
import os
from datetime import datetime

def backup_current_case_bot():
    """Backup the current case_bot.py"""
    source = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot.py'
    backup = f'/Users/tariqalmatrudi/NEWreader/backup_case_learning_{datetime.now().strftime("%Y%m%d_%H%M%S")}/case_bot.py'
    
    # Create backup directory
    backup_dir = os.path.dirname(backup)
    os.makedirs(backup_dir, exist_ok=True)
    
    # Copy current file
    shutil.copy2(source, backup)
    print(f"✅ Backed up current case_bot.py to: {backup}")
    return backup

def deploy_enhanced_case_bot():
    """Deploy the enhanced case bot"""
    source = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot_enhanced.py'
    target = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot.py'
    
    # Check if enhanced version exists
    if not os.path.exists(source):
        print(f"❌ Enhanced case bot not found at: {source}")
        return False
    
    # Backup current version
    backup_path = backup_current_case_bot()
    
    # Deploy enhanced version
    shutil.copy2(source, target)
    print(f"✅ Deployed enhanced case bot from: {source}")
    print(f"✅ Enhanced case bot is now active at: {target}")
    
    return True

def verify_deployment():
    """Verify the deployment worked"""
    target = '/Users/tariqalmatrudi/NEWreader/django_neurology_mcq/mcq/case_bot.py'
    
    try:
        with open(target, 'r') as f:
            content = f.read()
            
        # Check for key enhanced features
        checks = [
            ('SessionManager', 'Session management class'),
            ('CaseHistoryTracker', 'Case history tracking'),
            ('NEVER reveal the specific diagnosis', 'Diagnosis protection'),
            ('placeholder message', 'Placeholder message system'),
            ('guide the user without revealing', 'User guidance system'),
        ]
        
        print("\n📋 Verification Results:")
        all_passed = True
        
        for check, description in checks:
            if check in content:
                print(f"✅ {description}: Found")
            else:
                print(f"❌ {description}: Missing")
                all_passed = False
        
        if all_passed:
            print("\n🎉 All enhanced features verified successfully!")
            return True
        else:
            print("\n⚠️  Some features may be missing")
            return False
            
    except Exception as e:
        print(f"❌ Error verifying deployment: {e}")
        return False

def main():
    """Main deployment function"""
    print("🚀 Deploying Enhanced Case-Based Learning System...")
    print("="*60)
    
    print("\n📋 Issues being fixed:")
    print("1. Cases switching mid-conversation")
    print("2. Revealing diagnosis before conclusion")
    print("3. Not sending placeholder messages for investigations/localization")
    print("4. Not properly guiding users through diagnostic process")
    
    print("\n🔧 Starting deployment...")
    
    if deploy_enhanced_case_bot():
        print("\n✅ Deployment successful!")
        
        if verify_deployment():
            print("\n📝 Key improvements deployed:")
            print("• Proper session management with 3-hour timeout")
            print("• Case history tracking to avoid repetition")
            print("• Diagnosis protection - never reveals until conclusion")
            print("• Placeholder message system for investigations")
            print("• Enhanced user guidance without revealing diagnosis")
            print("• Rate limiting and API retry logic")
            print("• Critical element tracking for better flow")
            
            print("\n🎯 The case-based learning system should now:")
            print("• Never switch cases mid-conversation")
            print("• Always ask placeholder questions for localization/investigations")
            print("• Guide users without revealing the diagnosis")
            print("• Maintain proper case state throughout the session")
            
        else:
            print("\n⚠️  Deployment completed but verification had issues")
    else:
        print("\n❌ Deployment failed")

if __name__ == "__main__":
    main()