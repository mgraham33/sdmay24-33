from enum import Enum
import random, json


"""
Enum for existing rules files. Makes it easier to load rules without remembering filenames
"""
class RuleSets(Enum):
    ADC = "rules_adc.json"
    UART = "rules_uart.json"


"""
Stores register configuration information
"""
class RegisterConfiguration:
    """
    Constructor

    :param rules: List of rules from the json file for this register
    :type rules: List of dictionaries (json)
    :param options: List of configured options for each rule
    :type options: List of integers
    :param mask: Optional mask to hold data for which bits of the configuration matter for grading
    :type mask: Integer
    """
    def __init__(self, rules:list, options:list, mask:int=-1):
        if not len(rules) == len(options):
            raise ValueError("Options don't fit the rules")
        self._size = len(rules)
        self.rules = rules
        self.options = options
        self.register_value = self.build_register()
        if mask == -1:
            self.mask = 0
            # for each rule, create a mask for the width of the rule and shift it to the proper spot
            for i in range(self._size):
                self.mask |= (2**rules[i]['width'] - 1) << rules[i]['bit']
        else:
            self.mask = mask

    """
    Updates the options list to match the current register_value.
    Effectively the inverse of build_register()
    """
    def update_options(self):
        # for each rule
        for i in range(self._size):
            rule = self.rules[i]
            bit = rule['bit']
            # mask the register accordingly
            mask = (2**rule['width'] - 1) << bit
            # and shift it to the lsb
            masked_register = (self.register_value & mask) >> bit
            # and update the options list
            self.options[i] = masked_register

    """
    Builds a register value given the configuration's register rules list and options.

    :returns: Unsigned 32-bit number to fill a register with to configure it with the rules and options given.
    """
    def build_register(self):
        register = 0
        # for each rule
        for i in range(self._size):
            rule = self.rules[i]
            option = self.options[i]
            # shift the option for that rule to its correct place and or it with the accumulator
            register |= option << rule['bit']
        return register

    """
    Gets a list of the selected options for this register and options.

    :returns: List of strings. The strings are the text contained in each rule's 'options' object based on the selected option.
    """
    def get_readable_options(self):
        # only display the text if there are actual options in the rule (i.e. fields for data won't have explicit options)
        return [
            self.rules[i]['options'][self.options[i]] if
            'options' in self.rules[i] else
            f"{self.rules[i]['name']} = {self.options[i]}" 
            for i in range(self._size)
        ]


"""
Class to make loading and handling register configuration data easier.
"""
class RegisterRuleSet:
    """
    Constructor
    Loads the given rule set as json data for the rules

    :param ruleset: Rule set to load the json of.
    :type ruleset: RuleSets enum item
    """
    def __init__(self, ruleset:RuleSets):
        with open("../../registerConfig/json/" + ruleset.value, "r") as file:
            self._json = json.load(file)

    """
    Gets the rules of the specified register

    :param register_name: Name of the register to retrieve rules for
    :type register_name: Enum instance with the register name as the value
    :returns: List of the rules for the given register
    """
    def get_rules(self, register_name:Enum):
        return self._json[register_name.value]
    
    """
    Generates a randomly instantiated register based on the register name.

    :param register_name: Name of the register to generate randomly
    :type register_name: Enum instance with the register name as the value
    :param mask: Optional mask to tell grader which bits matter
    :type mask: Integer
    :returns: RegisterConfiguration object containing the rules, options, and built register
    """
    def generate(self, register_name:Enum, mask:int=-1):
        # get the rules for the given register name
        rules = self._json[register_name.value]
        # generate a random option for each rule with bounds being the number of possible options for the rule
        options = [
            random.randint(0, len(rules[i]['options'])-1) if 
            'options' in rules[i] else 
            random.randint(rules[i]['min'], rules[i]['max']) 
            for i in range(len(rules))
        ]
        return RegisterConfiguration(rules, options, mask)
