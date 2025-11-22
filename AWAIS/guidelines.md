- Dont use endl, its slow, use \n

> 🚫 Before You Start

- **DO NOT** open the problem booklet until explicitly instructed
- Read all instructions carefully before beginning
- Use DOMJudge for any clarification requests during the contest

> 💻 Technical Requirements
> Code Execution

- Your code must be executable via command line:

  - **Java**: Must compile with `javac` and run without package statements
  - **C++**: Must compile with `g++` and run without system pauses
  - **Python**: Must run with Python 3 interpreter

- **Remove these before submission:**
  ❌ `package` statements (Java)
  ❌ `getch()` / `system("pause")` (C++)
  ❌ Any file operations for input/output

> File Submission

- Submit ONLY source code files:
  ✅ `.java` files for Java
  ✅ `.cpp` files for C++
  ✅ `.py` files for Python

- **DO NOT submit:**
  ❌ Input files
  ❌ Output files
  ❌ Any other file types

- **File Naming:**
  - No whitespace in filenames
  - No special characters in filenames
  - Java: filename must match main class name

> I/O

- **ALWAYS** read from Standard Input:

  - C: `stdin`
  - C++: `cin`
  - Java: `System.in`
  - Python: `stdin` or `input()`

- **NEVER** create/open files for input
- **ALWAYS** write to Standard Output:

  - C: `stdout`
  - C++: `cout`
  - Java: `System.out`
  - Python: `stdout` or `print()`

- **NEVER** create/open files for output

⚠️ Critical Output Format Rules
Auto-Judging System

- Your output is compared **BYTE-BY-BYTE** with judge's output
- **ZERO TOLERANCE** for differences - even a single byte mismatch fails
- Must match **EXACTLY** including:

Pay Special Attention To:
🔍 **Spaces**: Extra or missing spaces will fail
🔍 **Commas/Dots**: Punctuation must be exact
🔍 **Newlines**: Line endings must match precisely
🔍 **Decimal Places**: Floating point precision must match
🔍 **Case Sensitivity**: Upper/lower case must be identical
🔍 **Whitespace**: Trailing/leading spaces matter

⏱️ Performance Constraints

- **Time Limit**: 5 seconds for all problems (unless specified otherwise)
- Ensure your solution is optimized within this constraint
- Test with worst-case inputs locally if possible

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Your solution here
    // Read from cin, write to cout

    return 0;
}
```

```py
import sys

def main():
    # Your solution here
    # Read from sys.stdin, write to sys.stdout

if __name__ == "__main__":
    main()
```

> Before Submission Checklist

- [ ] Removed all file I/O operations
- [ ] Removed package statements (Java)
- [ ] Removed system pauses (C++)
- [ ] Verified output format exactly matches problem statement
- [ ] Tested with sample inputs
- [ ] File name follows naming rules
- [ ] Code compiles and runs successfully

> Output Format Verification

- [ ] Spaces are exactly as specified
- [ ] Newlines are in correct positions
- [ ] Decimal precision matches requirements
- [ ] Case matches exactly
- [ ] No extra trailing spaces
- [ ] No missing separators

🆘 During Contest

> Clarification Requests

- Use DOMJudge system for any questions
- Judges will respond through the system
- Check clarifications regularly for updates
