from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

# Initialize the engine:
engine = AnonymizerEngine()

# Invoke the anonymize function with the text, 
# analyzer results (potentially coming from presidio-analyzer) and
# Operators to get the anonymization output:
result = engine.anonymize(
    text="My name is cwainwr3-collab, cwainwr3-collab",
    analyzer_results=[],
    operators={"PERSON": {"type": "replace", "new_value": "BIP"}}
)

print(result)
