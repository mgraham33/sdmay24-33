import cgrader

class QuestionGrader(cgrader.CGrader):
    
    def tests (self):
        self.compile_file("studentCode.c", "studentCode", add_c_file="/grade/tests/main.c")
        self.test_run("./studentCode", exp_output=["TEST 1 PASSED", "TEST 2 PASSED", "TEST 3 PASSED"], must_match_all_outputs=True)

g = QuestionGrader()
g.start()
