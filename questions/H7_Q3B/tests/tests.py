import cgrader
import random

class TestGrader(cgrader.CGrader):
    def tests(self):
        lcrh = self.data['params']['uartlcrh']
        mask = self.data['params']['uartlcrh_mask']
        ibrd = self.data['params']['ibrd']
        fbrd = self.data['params']['fbrd']

        self.test_compile_file("student_hardware.c", "student_hardware", add_c_file=[
            "/grade/tests/test_hardware.c",
            "/grade/tests/globals.c",
            "/grade/tests/uart.c"
        ], name="Compiling hardware implementation")

        self.test_run("./student_hardware", f"{lcrh}\n{mask}\n{ibrd}\n{fbrd}\n", exp_output=["INIT SUCCESS!\n", "SEND SUCCESS!\n"], name="Testing code", must_match_all_outputs=True, highlight_matches=True)


g = TestGrader()
g.start()
