import streamlit as st
from PIL import Image

def highlight_codons(sequence, positions):
    # Ensure the sequence length is divisible by 3
    if len(sequence) % 3 != 0:
        return "Error: Sequence length is not a multiple of 3."

    # Initialize the highlighted sequence
    highlighted_sequence = sequence

    # Highlight codons at specified positions
    for position in positions:
        # Find the codon at the specified position
        start_index_codon = (position - 1) * 3
        end_index_codon = start_index_codon + 3
        codon = sequence[start_index_codon:end_index_codon]

        # Highlight the codon in the sequence
        highlighted_sequence = (
            highlighted_sequence[:start_index_codon] +
            f'<span style="background-color: yellow; font-weight: bold;">{codon}</span>' +
            highlighted_sequence[end_index_codon:]
        )

    return highlighted_sequence

# Streamlit app
image = Image.open('dna_logo.jpg')

st.image(image, use_column_width=True)

# To remove footer and menu
st.beta_set_page_config(page_title='Nuclotide Codon Position Finder', layout='wide', initial_sidebar_state='expanded', menu=None, footer=None)

# Nuclotide codon position finder
st.write("""
# Nuclotide Codon Position Finder

This app finds the position of codons and highlights that position.
""")

# User input for nucleotide sequence
sequence_input = st.text_input("Enter Nucleotide Sequence:")

# User input for positions to highlight (comma-separated)
positions_input = st.text_input("Enter Positions to Highlight (comma-separated):")

# Convert positions input to a list of integers
highlight_positions = [int(pos.strip()) for pos in positions_input.split(',') if pos.strip()]

# Highlight codons and display the result
if sequence_input and highlight_positions:
    highlighted_result = highlight_codons(sequence_input, highlight_positions)
    st.markdown(f"The highlighted sequence: {highlighted_result}", unsafe_allow_html=True)
else:
    st.warning("Please enter a nucleotide sequence and at least one position to highlight.")
