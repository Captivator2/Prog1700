## 🟢 **1. Terminator (Start/End)**
- **Symbol**: Oval  
- **Purpose**: Marks the beginning or end of a flowchart.
- **Pseudocode**:
  ```plaintext
  START
  ...
  END
  ```
- **Example**:
  ```plaintext
  START
  INPUT number
  OUTPUT number * 2
  END
  ```

---

## 🟦 **2. Process**
- **Symbol**: Rectangle  
- **Purpose**: Represents a calculation or action.
- **Pseudocode**:
  ```plaintext
  SET total TO 0
  total ← total + value
  ```
- **Example**:
  ```plaintext
  SET radius TO 5
  SET area TO 3.14 * radius * radius
  ```

---

## 🟨 **3. Input/Output**
- **Symbol**: Parallelogram  
- **Purpose**: Represents data input or output.
- **Pseudocode**:
  ```plaintext
  INPUT name
  OUTPUT "Hello, " + name
  ```
- **Example**:
  ```plaintext
  INPUT temperature
  OUTPUT "The temperature is " + temperature + "°C"
  ```

---

## 🔷 **4. Decision**
- **Symbol**: Diamond  
- **Purpose**: Represents a decision point (yes/no, true/false).
- **Pseudocode**:
  ```plaintext
  IF age >= 18 THEN
      OUTPUT "Adult"
  ELSE
      OUTPUT "Minor"
  ENDIF
  ```
- **Example**:
  ```plaintext
  IF score >= 50 THEN
      OUTPUT "Pass"
  ELSE
      OUTPUT "Fail"
  ENDIF
  ```

---

## ⚪ **5. Connector**
- **Symbol**: Circle  
- **Purpose**: Connects different parts of a flowchart, especially across pages.
- **Pseudocode**:
  ```plaintext
  // CONTINUE TO Step 2
  ```
- **Example**:
  ```plaintext
  // Jump to LOOP section
  ```

---

## 🔁 **6. Looping (Iteration)**
- **Symbol**: Often a decision symbol with arrows looping back  
- **Purpose**: Repeats a set of actions.
- **Pseudocode**:
  - **WHILE Loop**:
    ```plaintext
    WHILE count < 5 DO
        OUTPUT count
        count ← count + 1
    ENDWHILE
    ```
  - **FOR Loop**:
    ```plaintext
    FOR i FROM 1 TO 3 DO
        OUTPUT "Iteration " + i
    ENDFOR
    ```

---

## 🧩 **7. Function/Procedure Call**
- **Symbol**: Rectangle with double vertical edges (or standard process box)  
- **Purpose**: Calls a reusable block of code.
- **Pseudocode**:
  ```plaintext
  CALL CalculateArea(5)
  ```
- **Example**:
  ```plaintext
  FUNCTION CalculateArea(radius)
      RETURN 3.14 * radius * radius
  ENDFUNCTION

  CALL CalculateArea(7)
  ```

---

## ➕ **8. Assignment**
- **Symbol**: Process box  
- **Purpose**: Assigns a value to a variable.
- **Pseudocode**:
  ```plaintext
  SET x TO 10
  x ← x + 5
  ```
- **Example**:
  ```plaintext
  SET score TO 75
  SET grade TO "B"
  ```

