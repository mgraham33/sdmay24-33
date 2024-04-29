import cgrader
import random

class TestGrader(cgrader.CGrader):
    def tests(self):
        self.compile_file("student.c", "main", add_c_file=[
            "/grade/tests/main.c",
            "/grade/tests/globals.c",
            "/grade/tests/answer.c",
            "/grade/tests/util.c"
        ])
        period = self.data['params']['period']
        duty = self.data['params']['duty']
        self.test_run("./main", input=f"{period}\n{duty}\n", exp_output="Success!\n")
    
g = TestGrader()
g.start()
