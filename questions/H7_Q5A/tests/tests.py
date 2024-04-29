import cgrader

class TestGrader(cgrader.CGrader):
    def tests(self):
        self.test_compile_file("student_uart.c", "student_uart", add_c_file=[
            "/grade/tests/main.c",
            "/grade/tests/globals.c",
            "/grade/tests/uart.c"
        ], name="Compiling implementation")

        self.test_run("./student_uart", exp_output="SUCCESS!\n", name="Testing code")

g = TestGrader()
g.start()
