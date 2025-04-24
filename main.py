import streamlit as st
st.set_page_config(
    page_title="My Friends Circle",
    page_icon="👫",
    layout="centered"
)

# Add custom styling that works in both light and dark mode
st.markdown("""
<style>
    .friend-card {
        background-color: rgba(70, 70, 70, 0.2);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(250, 250, 250, 0.2);
        margin-bottom: 20px;
    }
    .friend-description {
        color: inherit !important;
        font-size: 1.1rem;
    }
    .st-emotion-cache-10trblm {
        color: #ff9d00;
    }
    .st-emotion-cache-1gulkj5 {
        color: #29b5e8;
    }
</style>
""", unsafe_allow_html=True)

t = st.title("Hello Everyone! This is Ritam")
sh = st.subheader("Welcome to my friends description app")

name  = st.text_input("Enter your name: ")

friends_info = {
    "Urismita": "Urismita is my college mate, she is always my favorite person from the beginning of my college and will stay forever in my heart.",
    
    "Yashraj": "Yashraj is my friend from my childhood and he is still my friend. His mother always tells him to go with Brahmin Girls otherwise their family will be punished. His girlfriend's name is Anamica who stays in Dum Dum.",
    
    "Mahakash": "Mahakash is a guy who is crazy in his mind. He is in a relationship with his noni from 2022.",
    
    "Sayandeep": "Sayandeep is a person who always loves a girl named Udita but he can't speak with that girl.",
    
    "Shahensha": "Shahensha is my friend whom we always harass and he is crazy about girls.",
    
    "Arunava": "Arunava is a person who is the lover of Rittika and his previous girlfriend was Ditipriya who loves Yashraj.",
    
    "Rajibul": "Rajibul is a person who is now crazy to get a beautiful girl and he is a tea lover.",
    
    "Subhajit": "Subhajit is a man who loves the princess of Paschim Bhanganmari and he always plays games.",
    
    "Chandrima": "Chandrima is a shy girl whom Sandip likes but nobody can tell.",
    
    "Antara": "Antara is a topper who is excellent in every field from study to dance and writing.",
    
    "Kaushiki": "Kaushiki is a simple girl who is a girlfriend of Priam, the pagla man.",
    
    "Itisha": "Itisha is a friend who is always helpful to others and crazy about the girls.",
    
    "Tamasa": "Tamasa is a friend who is the queen of Go Down and crazy about web series.",
    
    "Koyel": "Koyel is a friend and the queen of Boga and is crazy about lust.",
    
    "Mampi": "Mampi is a girl who is always lunatic and crazy about Koreans.",
    
    
}

selected_friend = st.selectbox(
    "Select a friend to see their story:",
    list(friends_info.keys())
)

if selected_friend:
    st.markdown(f"## About {selected_friend}")

    st.markdown(f"""
    <div class="friend-card">
        <p>{friends_info[selected_friend]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(f"Show frienship for {selected_friend}"):
            st.balloons()
            st.success(f"You've shown your appreciation for {selected_friend}!")
    
    with col2:
        if st.button(f"Inside joke with {selected_friend}"):
            st.snow()
            st.info(f"You and {selected_friend} share so many funny memories!")

st.markdown("### Share a memory with this friend")
memory = st.text_area("Write a favorite memory or message:")
if st.button("Save Memory") and memory:
    st.success(f"Your memory with {selected_friend} has been saved! (Note: This is a demo feature)")

st.markdown("---")
st.markdown("### Friends are the family we choose for ourselves and I am also a family member like a elder brother")
st.markdown("Created for my amazing friend circle")