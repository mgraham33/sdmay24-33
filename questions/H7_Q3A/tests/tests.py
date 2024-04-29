import cgrader
import random

class TestGrader(cgrader.CGrader):
    def tests(self):
        self.pin = self.data['params']['pin']

        self.change_mode("/grade/tests/send_outputs.txt", "777")
        self.run_command("touch send_answers.txt", sandboxed=False)
        self.change_mode("send_answers.txt", "777")

        self.test_compile_file("student_software.c", "student_software", add_c_file=[
            "/grade/tests/answer_software_send.c",
            "/grade/tests/test_software.c",
            "/grade/tests/globals.c",
            "/grade/tests/uart.c"
        ], name="Compiling software implementation")

        self.test_run("./student_software", f"1\n{self.pin}\n", exp_output="INIT SUCCESS!\n", name="Testing 'init_portB()' in software")
        self.test_run("./student_software", f"2\n{self.pin}\n", exp_output="SEND SUCCESS!\n", name="Testing 'serial_send()' in software")


g = TestGrader()
g.start()
