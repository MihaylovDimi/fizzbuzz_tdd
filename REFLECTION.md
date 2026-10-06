# Reflection: TDD and the Agile Manifesto (FizzBuzz)

## 1. How did writing the test first influence the design of the function's input and output?

Writing the first test helped me decide what the function should look like before I wrote any code. The test `assert fizzbuzz(1) == "1"` made it clear that the function should be called `fizzbuzz`, take a number as input and return text as output. This turned out to matter later, because for numbers that are not multiples of 3 or 5 I had to use `str(n)` to return the number as text. In this way, the test defined the function's interface first, and the code was then written to match it.

## 2. In what ways did the unit tests act as executable documentation?

Test names such as `test_returns_fizz_for_3` and `test_returns_buzz_for_5` show directly what the function is supposed to do. Even without reading the production code, I can understand the main FizzBuzz rules just by looking at the tests. The difference from an ordinary written document is that the tests actually run and check whether the described behaviour is still true. This means that if the code changes and breaks a rule, a test shows the problem immediately, instead of the documentation simply going out of date.

## 3. Did you feel the confidence to refactor once you had passing tests? How does this support "Responding to change over following a plan"?

Yes. The passing tests gave me confidence to refactor, because after each change I could immediately check that the function still behaved the same way. In Phase 4d I rewrote the whole function, and afterwards all five tests still passed. Without the tests, it would have been much harder to know whether I had broken one of the earlier rules. The case of 15 also showed this clearly, because the test immediately revealed the problem with the order of the checks and let me fix it.

This supports the Agile value of "Responding to change over following a plan", because I can change the code more easily when requirements change, without worrying that I will break functionality that already works. For example, if the customer asked for numbers divisible by 7 to return "Bang", I would first write a failing test for 7, then change the function and use the full test suite to check that the change has not broken the existing behaviour.