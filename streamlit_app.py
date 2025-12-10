import streamlit as st

st.set_page_config(page_title="RAG Doc Assistant", layout="wide")
st.title("📄 RAG Doc Assistant (Local Llama 3)")

# --- DEBUG: check imports and show errors on page ---
try:
    from app.services.rag import answer_question
except Exception as e:
    st.error("❌ Error importing `answer_question` from app.services.RAG")
    st.write("Make sure you run this from the project ROOT folder (where main.py lives).")
    st.write("And check that `app/__init__.py` exists.")
    st.exception(e)
    st.stop()

st.success("✅ Successfully imported RAG pipeline.")

st.write("Ask questions about the PDFs you ingested into `data/raw/`.")

# Init chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "sources" in msg:
            with st.expander("📚 Sources"):
                for i, s in enumerate(msg["sources"]):
                    st.markdown(f"**Source {i}**: `{s['metadata'].get('source', 'unknown')}`")
                    st.write(s["text"])

# Input
if prompt := st.chat_input("Ask something about your documents..."):
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Run RAG
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = answer_question(prompt)
            answer = result["answer"]
            context = result["context"]

        st.markdown(answer)

        sources = [
            {"text": d, "metadata": m}
            for (d, m) in context
        ]

        if sources:
            with st.expander("📚 Sources"):
                for i, s in enumerate(sources):
                    st.markdown(f"**Source {i}**: `{s['metadata'].get('source', 'unknown')}`")
                    st.write(s["text"])

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )
