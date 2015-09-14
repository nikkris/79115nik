Paper review 1:

Combining search-based and constraint-based testing

[i] Reference:
Jan Malburg and Gordon Fraser. 2011. Combining search-based and constraint-based testing. In Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering (ASE '11). IEEE Computer Society, Washington, DC, USA, 436-439. DOI=10.1109/ASE.2011.6100092 http://dx.doi.org/10.1109/ASE.2011.6100092

http://dl.acm.org/citation.cfm?id=2190094

[ii] Important keywords:

[ii1] White box testing: Task of generating suitable inputs for programs using the program’s source code. This testing make use of internal structure of an application in addition to functionality.
[ii2]  Meta-heuristic search: One method to automatically generate test data to achieve high coverage. These methods use some form of stochastic optimization such as a genetic algorithm to generate data and guide the search process.  

[ii3] Constraint based testing: Another method to automatically generate test data to achieve high coverage by solving constraints produced by symbolic execution. Constraint based testing assumes knowledge about the source code or internal details to generate test cases.

[ii4]: Dynamic symbolic execution (DSE): In DSE, exploration is started with a random value for which the program is executed. Exploration continues in this path with state updation as and when a branch is executed.

[iii] Brief notes:

[iii1] Motivation: Meta-heuristic search and constraint-based techniques have emerged as two successful approaches to automatically generate test data that achieve high coverage. There is a growing awareness that these are not competing techniques but offer great potential for combination. Previous work in this area uses search-based techniques for particular cases where constraint solvers are not good [2], or hooks together search-based tools for method sequence generation with dynamic symbolic execution tools [3].

[iii2] Hypothesis: The authors propose a technique that intrinsically combines search-based testing with constraint-based testing. The combination achieves higher coverage than pure search requiring less iterations, and also same or higher coverage than DSE. GA-DSE achieves significantly higher branch coverage than random search, a GA, or DSE.

Agenetic algorithm (GA) evolves a population of candidate solutions, and a fitness function guides this search towards achieving a given coverage criterion. However, to avoid that the search gets stuck and to increase the speed with which the state space is explored, the authors added a special mutation operator: Rather than just flipping bits or blindly manipulating an input value, this new operator considers the path conditions that represent the execution path of a candidate solution, and negates one of these path conditions, just like dynamic symbolic execution does. A constraint solver then produces the new, mutated input, and this new input is guaranteed to take a different execution path, boosting the exploration aspect of the search.

[iii3] Baseline results: The baseline results are summarized in the following table.
![Result] (https://raw.githubusercontent.com/nikkris/79115nik/master/paper/1/Result.png)
 
[iii4] New results: To overcome the issue of finding whether search based or constraint based method works for general test cases, the authors present a novel combination of evolutionary search and dynamic symbolic execution. If one of the underlying techniques performs particularly bad, then this can be easily compensated given enough iterations. The use of search based method allows us to easily change the search objective to generate test cases not for branch coverage but for other coverage criteria or any other objective. It is also easy to integrate secondary objectives such as the test suite size.

[iv] Improvements

[iv1] The authors have not made clear the significance of choosing Java PathFinder to test their new algorithm. Explaining the significance of this test data set will help new readers appreciate the kind of problems tackled by this algorithm, and will help new researchers make a decision if they want to test their algorithm using this data set.

[iv2] It is immediately not clear whether the limitations on scalability and handling nonlinear or floating point arithmetic mentioned about constraint solvers in Section II-A is due to the limitation of the class of constraint solvers or due to limitation of softwares such as DART and PEX mentioned in the paper. A clarification in this front will be appreciated.

[iv3] I understand that even though mutation operator will try to optimize the values to reach a target branch, it is not guaranteed. This is evident from their earlier statement in Section I:  “However, to avoid that the search gets stuck and to increase the speed with which the state space is explored, the authors added a special mutation operator.” Hence the authors should have rephrased their last statement in Section III as “On the third branch condition, this DSE based mutation operator would fail just like DSE because of the limitations of constraint solvers, but the normal mutation operators would still optimize the value of z towards satisfying the condition, increasing the chance for reaching the target branch.”



