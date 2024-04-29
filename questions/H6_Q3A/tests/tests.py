import cgrader

class TestGrader(cgrader.CGrader):
    def tests(self):
        self.test_compile_file("student.c", "student", add_c_file=[
            "/grade/tests/main.c",
            "/grade/tests/globals.c",
            "/grade/tests/util.c"
        ], name="Compiling implementation")

        self.test_run("./student", self.data['params']['masks'], exp_output="SUCCESS!\n", name="Testing code")

g = TestGrader()
g.start()
