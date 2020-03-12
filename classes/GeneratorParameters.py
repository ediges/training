class GeneratorParameters:
    def __init__(self, generatorParameterId, name, label, type, required, validator, massage, value):
        self.value = value
        self.massage = massage
        self.validator = validator
        self.required = required
        self.type = type
        self.label = label
        self.name = name
        self.generatorParameterId = generatorParameterId



