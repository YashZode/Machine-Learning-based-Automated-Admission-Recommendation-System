
# src/run_prediction_test.py

from predict_admission import predict_admission_chance


# Sample user input (you can change these values)
input_data = {
    "gre_score": 320,
    "toefl_score": 110,
    "university_rating": 4,
    "sop_score": 4.0,
    "lor_score": 4.5,
    "cgpa": 9.1,
    "research": 1
}

# Make prediction
result = predict_admission_chance(**input_data)

# Display output
print("\n🎓 Admission Prediction Result")
print(f"Chance of Admit: {result['admit_chance']}%")
print(f"Candidate Classification: {result['classification']}")
