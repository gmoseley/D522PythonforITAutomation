# D522 — Python for IT Automation

WGU course D522 challenge work. I'm working through Python fundamentals with a focus on IT automation topics (networking, log parsing, config management, file I/O).

## How this works

Claude AI generates challenges based on the WGU D522 course content and pretest data — framed around real IT scenarios like parsing log lines, managing hostnames, and reading config files.

I solve the challenges myself using Google, W3Schools, and local testing in VS Code. No AI assistance on the solutions.

Claude AI then grades each solution against a rubric (A+ → F) and leaves feedback inline in the file.

## Repository layout

```
completed/      ← my solutions with grades
  ch04_strings/
  ch05_operators/
  ch06_tuples_sets/
  ch10_loops/
  ch11_error_handling/
  ch12_file_management/
  ch13_modules/

blank/          ← clean challenge files — try them yourself
  ch04_strings/
  ch05_operators/
  ...

initialTraining/  ← early exercises (variables, loops, functions, etc.)
capstone/         ← multi-file capstone projects
```

## Want to try the challenges?

Grab any file from `blank/` and work through it. Each challenge has:
- A one-line task description
- Starter variables (IT-relevant context)
- A `print('Challenge X answer:')` label marking where your answer goes
- The last 3 challenges in each file are WGU exam-style function stubs

No peeking at `completed/` until you've given it a shot.

## Grading rubric

| Grade | Meaning |
|-------|---------|
| A+    | Correct, idiomatic Python |
| A     | Correct output, minor style issue |
| B     | Works but fragile, wrong method, or partially correct |
| B-    | Partially correct with a notable bug |
| C/F   | Wrong output or fundamentally broken |
