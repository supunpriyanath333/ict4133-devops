# Break and Fix CI Demo - Instructional Script

## Overview
This demo demonstrates the **"Safety Net"** concept of Continuous Integration using GitHub Actions. Students will see how automated testing catches bugs before they reach production.

---

## 📋 Step 1: The Push (Demonstrating Automation)

### What to Say:
> "I've just written a simple calculator function and some tests. Let me push this code to GitHub and show you what happens automatically."

### Actions:
```bash
git add calculator.py test_calculator.py .github/workflows/ci-pipeline.yml
git commit -m "Add calculator with tests and CI pipeline"
git push origin main
```

### What to Show:
1. Navigate to your GitHub repository in the browser
2. Click on the **"Actions"** tab
3. Point out that a workflow run has **automatically started**

### Key Teaching Points:
- ✅ **Automation**: "Notice I didn't manually trigger anything. The moment I pushed, GitHub Actions started running."
- ✅ **Trigger Event**: "Our workflow is configured to run on every `push` event."
- ✅ **No Human Intervention**: "This is CI in action - automatic verification of every code change."

---

## 🔴 Step 2: The Failure (Explaining the Red X and Logs)

### What to Say:
> "Uh oh, look at that red X. Our CI pipeline caught something. Let's investigate what went wrong."

### Actions:
1. Click on the **failed workflow run** (red X icon)
2. Click on the **"Run Unit Tests"** job
3. Expand the **"Run Tests"** step
4. Show the error output in the logs

### What to Show in the Logs:
```
AssertionError: Expected 4, but got 0
```

### Key Teaching Points:
- ❌ **Safety Net in Action**: "The CI pipeline prevented broken code from being considered 'good'."
- ❌ **Fast Feedback**: "I found out within seconds that something is wrong."
- ❌ **Clear Error Messages**: "The logs tell me exactly what failed - the test expected 4 but got 0."
- ❌ **Root Cause**: "Let's look at the code... Ah! The `add()` function is subtracting instead of adding!"

### Code Review (Show on Screen):
```python
def add(a, b):
    return a - b  # BUG: Should be a + b
```

---

## ✅ Step 3: The Fix (Showing the Green Checkmark)

### What to Say:
> "Now let me fix the bug and push again. Watch what happens."

### Actions:
1. Open `calculator.py`
2. Fix the bug:
```python
def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b  # FIXED: Now correctly adds
```

3. Commit and push:
```bash
git add calculator.py
git commit -m "Fix: Correct addition function to add instead of subtract"
git push origin main
```

### What to Show:
1. Return to the **Actions** tab
2. Wait for the workflow to complete
3. Point out the **green checkmark** ✅
4. Click into the successful run and show the passing tests

### What to Show in the Logs:
```
✓ Test passed: 2 + 2 = 4
✓ Test passed: -1 + 1 = 0
✓ Test passed: 5 + 0 = 5

✅ All tests passed!
```

### Key Teaching Points:
- ✅ **Confidence**: "Now I have confidence that my code works correctly."
- ✅ **Continuous Verification**: "Every change is automatically verified."
- ✅ **Team Protection**: "In a team, this prevents anyone from accidentally breaking the codebase."
- ✅ **Quality Gate**: "The green checkmark is our quality gate - only passing code is considered acceptable."

---

## 🎯 Summary for Students

### The CI Safety Net Concept:
1. **Write Code** → Developer creates features and tests
2. **Push Code** → Triggers automated CI pipeline
3. **Run Tests** → Pipeline executes all tests automatically
4. **Get Feedback** → Immediate pass/fail status
5. **Fix Issues** → Developer corrects problems before merge
6. **Repeat** → Continuous cycle of improvement

### Why This Matters:
- 🚀 **Catch bugs early** (before production)
- ⚡ **Fast feedback loop** (seconds, not days)
- 🛡️ **Protect the team** (prevent breaking changes)
- 📊 **Maintain quality** (automated enforcement)
- 💰 **Save money** (bugs are cheaper to fix early)

---

## 📝 Optional Extensions

### For Advanced Students:
1. **Add more test cases** to increase coverage
2. **Add a badge** to README.md showing build status
3. **Configure branch protection** to require passing tests before merge
4. **Add code coverage reporting** with pytest-cov
5. **Set up notifications** for failed builds

### Discussion Questions:
- What happens if someone tries to merge code with failing tests?
- How does this scale to larger teams?
- What other types of checks could we automate? (linting, security scans, etc.)
