## ![alt text](image.png)

---

## 1) Assignment Details

* **Course:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Title:** Alarm Deactivation — Code from Flowchart
* **Type:** **In-class programming exam** (individual)
* **Timebox:** See Brightspace / invigilator instructions
* **Weight:** See course evaluation table
* **Submission Filename (exact):** `w#-alarm-deactivation-final.py`

  * *Example:* `W01234567-alarm-deactivation-final.py`
* **Files Provided in Exam Folder:**

  * `flowchart.pdf` *(read carefully; code must follow it)*
  * `passwords.txt` *(five valid 5-digit passcodes; one line each)*

> **Important:** The **flowchart governs the required logic**. Your code will be evaluated primarily on fidelity to that flow. Do **not** include code from outside sources.

---

## 2) Overview / Purpose / Objectives

You will translate a given **flowchart of an alarm deactivation process** into a working Python program. The exercise assesses your ability to:

* Implement control flow and validation from a specification (flowchart),
* Use **loops**, **conditionals**, and **file I/O** correctly,
* Manage **program state** (activated/deactivated/alarm tripped),
* Demonstrate **debugging discipline** during an invigilated exam.

---

## 3) Learning Outcomes Addressed (PROG1700)

* **O1** Translate logic principles into programming code to solve problems.
* **O2** Perform input/output operations (read `passwords.txt`, display/log prompts).
* **O3** Store data inside data structures (read file lines to a suitable structure).
* **O4** Implement conditional logic to control program behaviour.
* **O5** Implement functions/procedures to create maintainable/readable code.
* **O6** Design and implement loops for repetitive tasks (attempt counter).
* **O7** Implement debugging techniques using an IDE.

---

## 6) Deliverables

* **One Python file:** `w#-alarm-deactivation-final.py`
* (No additional documents required.) Your program must run in the exam folder alongside `passwords.txt`.

---

## 7) Demonstration (invigilated)

Be prepared to quickly show:

1. A failed sequence that **triggers** the alarm (e.g., invalid length / bad codes to exhaust attempts).
2. A successful entry of a **correct 5-digit code** that **deactivates** the system.
3. Where you read the file and how you validated input length/characters.
4. Briefly point out where your code follows the flowchart’s decisions/loops.

---

## 8) Rubric (100 points)

| **Criteria**                               | **Exemplary (A)**                                                                                                                  | **Proficient (B)**                                                          | **Developing (C)**                                                        | **Insufficient (D/F)**                                          | **Pts** |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------- | ------: |
| **Flowchart Fidelity**                     | Program **precisely** matches all decision points, loops, and states from the flowchart; messages & transitions are unambiguous.   | Minor deviations that do **not** change behaviour; overall flow intact.     | Noticeable divergences; some branches or states are unclear or missing.   | Ignores flowchart; behaviour does not reflect required process. |  **20** |
| **Attempt Control (3 tries)**              | Exact **3-attempt** logic; counter decrements on any non-5-digit or wrong code; resets/ends exactly as per chart.                  | Minor off-by-one or messaging issues; logic correct.                        | Attempt tracking inconsistent or partially enforced.                      | Attempt control missing or incorrect.                           |  **15** |
| **5-Digit Validation**                     | Strictly enforces **length=5** and **all digits** before file check; invalid input still **consumes an attempt**.                  | Enforces length & digits with small edge-case gaps; still consumes attempt. | Only partial checks (length or digits); inconsistent attempt consumption. | Minimal validation or accepts non-conforming input.             |  **10** |
| **File I/O (`passwords.txt`)**             | Safely reads file; trims lines; stores passcodes in a suitable structure; handles missing/empty lines gracefully.                  | Reads and checks correctly; minor robustness gaps.                          | Reads but with fragile parsing or assumptions.                            | Fails to read/parse file correctly.                             |  **10** |
| **State Management**                       | Clear states: **activated → deactivated** or **activated → alarm**; no illegal transitions; user feedback is clear.                | States correct with minor UX/print issues.                                  | State changes occur but are confusing or poorly signposted.               | States incorrect or missing.                                    |  **10** |
| **Conditionals & Logic (O4)**              | Clean, readable branching; conditions directly reflect chart; no dead code.                                                        | Mostly clean; a few redundant checks.                                       | Tangled branching; logic hard to follow.                                  | Illogical or non-functional branching.                          |  **10** |
| **Loops (O6)**                             | Loop structure directly implements attempt policy; terminates exactly when required.                                               | Loop works; minor termination quirks.                                       | Loop mis-orders checks or leaves edge cases.                              | Loop absent/malfunctioning.                                     |  **10** |
| **Functions / Structure (O5)**             | Core logic factored into small, named functions (e.g., read_passcodes, is_valid_input, check_code, run_controller); main is clear. | Some functions used; moderate cohesion.                                     | Largely monolithic; limited modularity.                                   | No meaningful structure; all in global flow.                    |   **5** |
| **User Feedback / UX**                     | Prompts and outputs make attempt count, state, and results obvious to the examiner.                                                | Mostly clear feedback.                                                      | Feedback sometimes unclear.                                               | Feedback missing/ambiguous.                                     |   **5** |
| **Robustness & Basic Error Handling (O7)** | Handles trivial read errors (message + exit), strips whitespace, tolerates empty lines; no crashes on normal misuse.               | Minor rough edges; still stable.                                            | Fragile in common cases; occasional crashes.                              | Crashes or hangs easily.                                        |   **5** |
| **Total**                                  |                                                                                                                                    |                                                                             |                                                                           |                                                                 | **100** |

---

## 9) Submission Guidelines

* Submit your **single** Python file named exactly `w#-alarm-deactivation-final.py` to the Brightspace exam dropbox **before time expires**.
* Ensure your script **runs in the exam folder** containing `passwords.txt`.
* No extra libraries; **standard Python only**.
* Late submissions follow exam policy.

---

## 10) Exam Conditions / Academic Integrity

* **Individual** work. No collaboration.
* **No internet, no AI tools, no external code** (beyond Python standard library).
* You may consult the provided **flowchart** and your local IDE help.
* **Oral validation** may be used: you may be asked to explain how your code implements specific branches/loops from the flowchart.

> **Mismatch between flowchart logic and code** will be penalized even if the program “seems to work,” to ensure outcomes O1/O4/O6 are met.

---

## 11) Resources / Equipment

* Python 3.x, VS Code (Python extension), local file access
* `flowchart.pdf` (provided), `passwords.txt` (provided)

---

## 12) Copyright

© 2025, Davis Boudreau — For use in PROG1700 at NSCC.

