---
title: "Generating code coverage report with gcc, gcov, and lcov"
timestamp: 2019-01-02T07:30:01
tags:
  - CodeMaven
published: false
author: szabgab
archive: true
---


[Generating Code Coverage Report Using GNU Gcov and Lcov](https://medium.com/@naveen.maltesh/generating-code-coverage-report-using-gnu-gcov-lcov-ee54a4de3f11)



```
cmake -DCOVERAGE=1 .
make -j8
app/tests/runTests
lcov -c --directory . --rc lcov_branch_coverage=1 --output-file all.info
lcov --remove all.info '/usr/*' '3rdparty/*' 'app/tests/*' --rc lcov_branch_coverage=1 --output-file selected.info
genhtml selected.info --rc lcov_branch_coverage=1 --output-directory out
```

