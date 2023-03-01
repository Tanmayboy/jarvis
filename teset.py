from jarvis import jarvis
jarvis = Jarvis(
    model_name="jarvis",
    beam_width=2,
    max_length=30,
    min_length=10,
    do_sample=True,
    temperature=0.7,
)

input_text = "What is the meaning of life?"
generated_text = jarvis.generate_text(input_text)
print(generated_text)
