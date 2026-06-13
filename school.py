import streamlit as st

with st.sidebar:
    st.title("DASHBOARD")
    page = st.selectbox(
        "Choose Section",
        ["Home", "About", "Subjects", "Facilities", "Contact"]
    )

if page=="Home":
    st.title("GODSWAY ACCADEMY")
    st.header("**WELCOME TO GODSWAY ACCADEMY'S WEBPAGE**")
    st.image("godsway_badge.png")
    st.header("*Cultural Day At GODSWAY ACCADEMY*")
    st.image("cultural_day.png")
    st.header("*Career Day At GODSWAY ACCADEMY*")
    st.image("career_day.png")
    st.image("godsway1.png")
    st.image("godsway2.png")
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right,#ffffff, #0000ff);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


if page=="About":
    st.image("godsway_badge.png")
    st.subheader("**AbOUT GODSWAY ACCADEMY**")
    st.write("Godsway Academy is a leading educational institution dedicated to providing quality education in a safe, nurturing, and inspiring environment. Our mission is to develop students academically, morally, spiritually, and socially, preparing them to become responsible leaders and productive members of society.")
    st.write("At Godsway Academy, we  Our curriculum combines academic excellence with strong moral values, critical thinking, creativity, and practical skills. We encourage students to develop confidence, discipline, integrity, and a lifelong love for learning.and student-centered teaching methods, we strive to help every learner reach their full potential.")
    st.write(" Our curriculum combines academic excellence with strong moral values, critical thinking, creativity, and practical skills. We encourage students to develop confidence, discipline, integrity, and a lifelong love for learning.")
    st.write(" With well-equipped classrooms, science and computer laboratories, a library, sports facilities, and a supportive learning community, Godsway Academy provides an environment where students can grow, succeed, and thrive.")
    st.write(" **Our Motto:** *Building Minds. Shaping Futures. Honoring God.*")
    st.write(" **Our Core Values:**")
    st.write("*🚀Excellence*")
    st.write("*🚀Integrity*")
    st.write("*🚀Faith*")
    st.write("*🚀Discipline*")
    st.write("*🚀Leadership*")
    st.write("*🚀Service*")
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right,#964b00);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    


elif page=="Subjects":
    st.image("godsway_badge.png")
    st.header("Subjects Offered")
    st.subheader("At Godsway Academy, we provide a well-rounded curriculum designed to equip students with the knowledge and skills needed for academic success and personal development.")
    st.header("Core Subjects")
    st.write("✅ English Language")
    st.write("✅ Mathmatics")
    st.write("✅ Integrated Science")
    st.write("✅ Social Studies")
    st.write("✅ Information and Communication Technology (ICT)")

    st.header("Languages")
    st.write("✅ French")
    st.write("✅ Spanish")
    st.write("✅ Italian")
    st.write("✅ Latin")
    st.write("✅ Arabic")
    
    st.header("Creative & Practical Subjects")
    st.write("✅ Creative Arts")
    st.write("✅ Home Economics")
    st.write("✅ Design & Technology")
    st.write("✅ Career Technology")

    st.header("Sports & Physical Development")
    st.write("✅ Physical Education")
    st.write("✅ Health Education")
    st.write("✅ Athletics and Sports Activities")

    st.header("Co-Curricular Activities")
    st.write("✅ Debate Club")
    st.write("✅ Science Club")
    st.write("✅ Coding & Robotics Club")
    st.write("✅ Music and Drama")
    st.write("✅ Leadership Development")
    st.write("✅ Community Service Programs")
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #0000ff);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    
    
elif page=="Facilities":
    st.image("godsway_badge.png")
    st.header("**Our Infrastructure**")
    st.write("Godsway Academy provides a modern and conducive learning environment designed to support academic excellence, creativity, and personal development.")
    
    st.subheader("🏫 Main School Building")
    st.image("mainschool.png")
    st.write("✅Modern and spacious classrooms")
    st.write("✅Administrative offices")
    st.write("✅Reception area")
    st.write("✅Staff common room")
    st.write("✅Student-friendly environment")
    
    st.subheader("🪑 Modern Classrooms")
    st.image("classroom.png")
    st.write("✅Comfortable seating arrangements")
    st.write("✅Interactive learning environment")
    st.write("✅Audio-visual teaching aids")
    st.write("✅Proper lighting and ventilation")
    
    st.subheader("📚 School Library")
    st.image("library.png")
    st.write("✅Well-stocked with educational books")
    st.write("✅Quiet reading environment")
    st.write("✅Research and study resources")
    st.write("✅Digital learning materials")
    
    st.subheader("🔬 Science Laboratory")
    st.write("✅Equipped for practical science lessons")
    st.write("✅Physics, Chemistry, and Biology experiments")
    st.write("✅Safe learning environment")
    st.write("✅Hands-on scientific exploration")
    
    st.subheader("⚽ Sports Complex & Playground")
    st.image("sports_complex.png")
    st.write("✅Football field")
    st.write("✅Basketball and volleyball courts")
    st.write("✅Athletics activities")
    st.write("✅Physical fitness programs")
    
    st.subheader("🚌 School Transportation ")
    st.image("school_bus.png")
    st.write("✅Safe and reliable school bus service")
    st.write("✅Comfortable transportation for students")
    st.write("✅Professional drivers")
    st.write("✅Timely pick-up and drop-off")
    
    st.subheader("🎓 Graduation & Event Hall")
    st.image("graduation_hall.png")
    st.write("✅School ceremonies and events")
    st.write("✅Awards and graduation programs")
    st.write("✅Parent-teacher meetings")
    st.write("✅Cultural celebrations")
    
    st.subheader("🙏 School Assembly Grounds")
    st.image("assembly.png")
    st.write("✅Morning assemblies")
    st.write("✅School announcements")
    st.write("✅Special programs and celebrations")
    st.write("✅Character and leelopment activities")
    
    st.subheader("🌳 Beautiful School Environment")
    st.image("environment.png")
    st.write("✅Clean and secure campus")
    st.write("✅Landscaped gardens")
    st.write("✅Safe learning atmosphere")
    st.write("✅Comfortable outdoor spaces")
    
    st.subheader("✅ playground")
    st.image("playground.png")
    st.write("✅Clean playground")
    st.write("✅Lots of things for your kids to play with")
    st.write("✅Secured")
    st.write("✅We have medics availabel")
    
    st.subheader("✅ computer lab")
    st.image("computerlab1.png")
    st.write("✅Lots of computers")
    st.write("✅More praticals than theory")
    st.write("✅Safe with no faults")
    st.write("✅The teachers are experts")
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right,#040720);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


elif page=="Contact":
    st.image("godsway_badge.png")
    st.header("YOU CAN CONTACT US ON THIS LINES FOR MORE DETAILS")
    if st.button("*WHATSAPP US ON*"):
        st.session_state['0592882841'] = ("http://whatsapp.com/0592882841")
    if '0592882841' in st.session_state:
        st.write(st.session_state['0592882841'])
    st.subheader("📞 **Phone:** +233592882841")
    st.subheader("📧 **Email:** christianbonzoh@gmail.com")
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right,#964b00);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)






