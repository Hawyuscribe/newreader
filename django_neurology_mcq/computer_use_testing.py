#!/usr/bin/env python3
"""
Computer Use Integration for Clinical Reasoning Analysis Testing
This script provides automated testing capabilities that can be used with Anthropic's Computer Use
"""

import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional

class ComputerUseTestingInterface:
    """
    Interface for Computer Use to test the Clinical Reasoning Analysis system
    Provides structured feedback that can be consumed by Claude Code
    """
    
    def __init__(self, base_url: str = "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com"):
        self.base_url = base_url
        self.test_results = []
        self.current_test_session = {
            "session_id": f"test_{int(time.time())}",
            "timestamp": datetime.now().isoformat(),
            "tests": [],
            "issues_found": [],
            "performance_metrics": {}
        }
    
    def log_test_step(self, step_name: str, status: str, details: Dict[str, Any] = None):
        """Log a test step for Computer Use to call"""
        test_step = {
            "step": step_name,
            "status": status,  # "success", "failed", "warning"
            "timestamp": datetime.now().isoformat(),
            "details": details or {}
        }
        self.current_test_session["tests"].append(test_step)
        print(f"[TEST] {step_name}: {status.upper()}")
        if details:
            print(f"[DETAILS] {json.dumps(details, indent=2)}")
    
    def log_issue(self, issue_type: str, severity: str, description: str, location: str = None, screenshot: str = None):
        """Log an issue found during testing"""
        issue = {
            "type": issue_type,
            "severity": severity,  # "critical", "major", "minor", "cosmetic"
            "description": description,
            "location": location,
            "screenshot": screenshot,
            "timestamp": datetime.now().isoformat()
        }
        self.current_test_session["issues_found"].append(issue)
        print(f"[ISSUE] {severity.upper()}: {description}")
    
    def log_performance(self, metric_name: str, value: float, unit: str = "ms"):
        """Log performance metrics"""
        self.current_test_session["performance_metrics"][metric_name] = {
            "value": value,
            "unit": unit,
            "timestamp": datetime.now().isoformat()
        }
        print(f"[PERFORMANCE] {metric_name}: {value}{unit}")
    
    def generate_test_script_for_computer_use(self) -> str:
        """Generate instructions for Computer Use to follow"""
        return """
# Computer Use Testing Script for Clinical Reasoning Analysis

## Setup
1. Open a web browser
2. Navigate to the MCQ website
3. Log in as admin user
4. Look for the Admin Debug Console in top-right corner

## Test Sequence

### Test 1: Page Load and Console Check
1. Navigate to any MCQ page
2. Wait for page to fully load
3. Check if Admin Debug Console appears in top-right
4. Look for these console messages:
   - "MCQ Detail page loaded - JavaScript is working"
   - "🔧 openClinicalReasoningAnalysis function defined globally"
   - "✅ All systems ready - Clinical Reasoning Analysis should work!"
5. Call: computer_use_tester.log_test_step("page_load", "success" if all messages appear else "failed")

### Test 2: Answer Selection and Button Appearance
1. Select any answer option (A, B, C, or D)
2. Click "Check Answer" button
3. Wait for "Analyze My Clinical Reasoning" button to appear
4. Check console for: "Answer checked" message
5. Call: computer_use_tester.log_test_step("button_appearance", "success" if button appears else "failed")

### Test 3: Modal Opening
1. Click "Analyze My Clinical Reasoning" button
2. Check console for: "Opening Clinical Reasoning Analysis modal"
3. Verify professional modal opens with:
   - Header: "Clinical Reasoning Analysis"
   - Step indicator: "Step 1 of 3"
   - Clinical reasoning framework visualization
   - Text/Voice input toggle
4. Call: computer_use_tester.log_test_step("modal_opening", "success" if modal opens properly else "failed")

### Test 4: Text Input Testing
1. Click "Type" input method
2. Type at least 20 characters in the textarea
3. Check that character counter updates
4. Verify "Submit Analysis" button becomes enabled
5. Call: computer_use_tester.log_test_step("text_input", "success" if all works else "failed")

### Test 5: Voice Input Testing
1. Click "Voice" input method toggle
2. Click "Start Recording" button
3. Speak for 3-5 seconds
4. Click "Stop Recording"
5. Check console for transcription messages
6. Verify text appears in textarea
7. Call: computer_use_tester.log_test_step("voice_input", "success" if transcription works else "failed")

### Test 6: Analysis Submission
1. Ensure textarea has content (either typed or transcribed)
2. Click "Submit Analysis" button
3. Check for step 2 loading (Analysis in Progress)
4. Wait for step 3 (Results)
5. Verify professional results display appears
6. Call: computer_use_tester.log_test_step("analysis_submission", "success" if completes else "failed")

### Test 7: Error Handling
1. Try submitting with empty textarea
2. Verify validation error appears
3. Try voice recording without microphone permission
4. Verify graceful error handling
5. Call: computer_use_tester.log_test_step("error_handling", "success" if errors handled gracefully else "failed")

## Issue Reporting
For any issues found, call:
computer_use_tester.log_issue(
    issue_type="functional|ui|performance|accessibility",
    severity="critical|major|minor|cosmetic", 
    description="Detailed description of the issue",
    location="Specific UI element or step",
    screenshot="filename.png if screenshot taken"
)

## Performance Monitoring
Monitor and log these metrics:
- Page load time: computer_use_tester.log_performance("page_load_time", time_in_ms)
- Modal open time: computer_use_tester.log_performance("modal_open_time", time_in_ms)
- Voice transcription time: computer_use_tester.log_performance("transcription_time", time_in_ms)
- Analysis processing time: computer_use_tester.log_performance("analysis_time", time_in_ms)

## Final Report Generation
After completing all tests, call:
computer_use_tester.generate_final_report()
"""

    def generate_computer_use_commands(self) -> List[str]:
        """Generate specific commands for Computer Use to execute"""
        return [
            "# Initialize testing interface",
            "computer_use_tester = ComputerUseTestingInterface()",
            "",
            "# Navigate to website",
            "# [Computer Use: Open browser and navigate to MCQ site]",
            "",
            "# Test page load",
            "computer_use_tester.log_test_step('navigation', 'success', {'url': 'MCQ_page_URL'})",
            "",
            "# Check for debug console",
            "# [Computer Use: Look for debug console in top-right corner]",
            "computer_use_tester.log_test_step('debug_console_visible', 'success' if console_visible else 'failed')",
            "",
            "# Test answer selection",
            "# [Computer Use: Click answer option and check answer button]",
            "computer_use_tester.log_test_step('answer_selection', 'success')",
            "",
            "# Test modal opening",
            "# [Computer Use: Click 'Analyze My Clinical Reasoning' button]",
            "computer_use_tester.log_test_step('modal_open', 'success' if modal_opens else 'failed')",
            "",
            "# Test text input",
            "# [Computer Use: Type in textarea and verify button enables]",
            "computer_use_tester.log_test_step('text_input', 'success')",
            "",
            "# Test voice input", 
            "# [Computer Use: Try voice recording]",
            "computer_use_tester.log_test_step('voice_input', 'success' if transcription_works else 'failed')",
            "",
            "# Test analysis submission",
            "# [Computer Use: Submit analysis and wait for results]",
            "computer_use_tester.log_test_step('analysis_complete', 'success' if results_appear else 'failed')",
            "",
            "# Generate final report",
            "computer_use_tester.generate_final_report()"
        ]
    
    def generate_final_report(self) -> Dict[str, Any]:
        """Generate comprehensive test report for Claude Code"""
        total_tests = len(self.current_test_session["tests"])
        passed_tests = len([t for t in self.current_test_session["tests"] if t["status"] == "success"])
        critical_issues = len([i for i in self.current_test_session["issues_found"] if i["severity"] == "critical"])
        
        report = {
            "summary": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": total_tests - passed_tests,
                "pass_rate": (passed_tests / total_tests * 100) if total_tests > 0 else 0,
                "critical_issues": critical_issues,
                "total_issues": len(self.current_test_session["issues_found"])
            },
            "detailed_results": self.current_test_session,
            "recommendations": self.generate_recommendations(),
            "claude_code_actions": self.generate_claude_code_actions()
        }
        
        # Save report to file
        report_file = f"test_report_{self.current_test_session['session_id']}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n{'='*50}")
        print("FINAL TEST REPORT")
        print(f"{'='*50}")
        print(f"Tests Passed: {passed_tests}/{total_tests} ({report['summary']['pass_rate']:.1f}%)")
        print(f"Critical Issues: {critical_issues}")
        print(f"Total Issues: {report['summary']['total_issues']}")
        print(f"Report saved to: {report_file}")
        print(f"{'='*50}\n")
        
        return report
    
    def generate_recommendations(self) -> List[str]:
        """Generate recommendations based on test results"""
        recommendations = []
        
        # Check for common issues
        failed_tests = [t for t in self.current_test_session["tests"] if t["status"] == "failed"]
        critical_issues = [i for i in self.current_test_session["issues_found"] if i["severity"] == "critical"]
        
        if any("voice_input" in t["step"] for t in failed_tests):
            recommendations.append("Voice input functionality needs debugging - check microphone permissions and transcription API")
        
        if any("modal" in t["step"] for t in failed_tests):
            recommendations.append("Modal functionality issues detected - verify Bootstrap integration and event handlers")
        
        if critical_issues:
            recommendations.append("Critical issues found that prevent core functionality - immediate attention required")
        
        # Performance recommendations
        performance = self.current_test_session["performance_metrics"]
        if "page_load_time" in performance and performance["page_load_time"]["value"] > 3000:
            recommendations.append("Page load time is slow - consider optimizing JavaScript and CSS")
        
        if not recommendations:
            recommendations.append("All tests passed successfully - system is functioning well")
        
        return recommendations
    
    def generate_claude_code_actions(self) -> List[str]:
        """Generate specific actions for Claude Code to take"""
        actions = []
        failed_tests = [t for t in self.current_test_session["tests"] if t["status"] == "failed"]
        
        for test in failed_tests:
            if "voice_input" in test["step"]:
                actions.append("Fix voice recording functionality in ClinicalReasoningAnalyzer class")
            elif "modal" in test["step"]:
                actions.append("Debug modal opening and Bootstrap integration")
            elif "analysis" in test["step"]:
                actions.append("Fix analysis submission and results display")
            elif "text_input" in test["step"]:
                actions.append("Debug textarea validation and character counting")
        
        for issue in self.current_test_session["issues_found"]:
            if issue["severity"] == "critical":
                actions.append(f"URGENT: Fix critical issue - {issue['description']}")
        
        return actions

def main():
    """Main function for running tests manually or with Computer Use"""
    print("Computer Use Testing Interface for Clinical Reasoning Analysis")
    print("=" * 60)
    
    tester = ComputerUseTestingInterface()
    
    # Print instructions for Computer Use
    print("\n📋 INSTRUCTIONS FOR COMPUTER USE:")
    print(tester.generate_test_script_for_computer_use())
    
    # Print commands
    print("\n💻 COMPUTER USE COMMANDS:")
    for command in tester.generate_computer_use_commands():
        print(command)
    
    print("\n🔧 Integration complete! Computer Use can now test the Clinical Reasoning Analysis system.")
    print("Run this script in the Computer Use environment for automated testing.")

if __name__ == "__main__":
    main()