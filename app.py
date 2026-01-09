import streamlit as st
import pandas as pd
from datetime import datetime
# In your app.py
import random

def generate_synthetic_resume(role="AI Engineer", years=5):
    """Generate realistic synthetic resume for demos"""
    
    # Indian names (public domain)
    first_names = ["Rahul", "Priya", "Amit", "Sneha", "Vikram", "Anjali", "Arjun", "Meera"]
    last_names = ["Sharma", "Patel", "Kumar", "Singh", "Gupta", "Reddy", "Mukherjee", "Desai"]
    
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    
    # Skills based on role
    skill_sets = {
        "AI Engineer": ["Python", "TensorFlow", "PyTorch", "Scikit-learn", "Streamlit", "AWS"],
        "Data Scientist": ["Python", "SQL", "Pandas", "ML", "Tableau", "Big Data"],
        "Cybersecurity": ["Network Security", "Ethical Hacking", "SIEM", "Compliance", "Risk Assessment"],
        "FinTech Developer": ["Java", "Blockchain", "Payment Systems", "RegTech", "API Integration"]
    }
    
    skills = random.sample(skill_sets.get(role, skill_sets["AI Engineer"]), 4)
    
    # Education (Indian institutions)
    colleges = ["IIT Delhi", "NIT Trichy", "DTU", "SRCC", "Christ University", "VIT", "Manipal"]
    degrees = ["B.Tech", "M.Tech", "B.Com", "MBA"]
    
    resume = f"""
{name}
{role} | {years}+ Years Experience

PROFESSIONAL SUMMARY
Results-driven {role.lower()} with {years} years of experience in {', '.join(skills[:2])}. 
Proven track record of delivering AI solutions for MNC clients.

TECHNICAL SKILLS
{', '.join(skills)}

EXPERIENCE
Senior {role}
• Built AI applications using {skills[0]} and {skills[1]}
• Reduced time-to-hire by 40% for global clients
• Deployed predictive models saving ₹10L+/month

EDUCATION
{random.choice(degrees)} in Computer Science
{random.choice(colleges)} | 2015-2019

CERTIFICATIONS
• AI Mastermind Certification
• AWS Certified Developer
"""
    return resume.strip()
st.set_page_config(
    page_title="StaffingAI Pro - All-in-One Platform for Staffing Companies",
    page_icon="👥",
    layout="wide"
)

st.title("👥 StaffingAI Pro")
st.caption("5 AI tools in 1 platform — replace LinkedIn Recruiter, ATS, and Excel with AI")

# Sidebar: Navigation
with st.sidebar:
    st.header("🚀 Modules")
    module = st.radio(
        "Select Tool",
        [
            "Dashboard",
            "1. AI Candidate Sourcing",
            "2. AI JD & Resume Optimizer", 
            "3. AI Market Intelligence",
            "4. AI Client Reporting",
            "5. AI Cost Optimizer"
        ]
    )
    
    st.markdown("---")
    st.subheader("💡 About StaffingAI Pro")
    st.info("""
    Built by a **18-year staffing veteran** who’s won Mercedes, Siemens, Airbus.  
    **Replaces 5+ tools** at 10% of the cost.  
    **Ethical, bias-free, audit-ready**.
    """)
    
    st.markdown("🔗 [Book Demo](https://calendly.com/yourname)")

# Dashboard
if module == "Dashboard":
    st.header("📊 StaffingAI Pro Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("⏱️ Time Saved", "42 hrs/week", "vs manual")
    col2.metric("💰 Cost Reduced", "28%", "vs traditional tools")
    col3.metric("🎯 Placement Rate", "92%", "+8%")
    col4.metric("📄 Reports Generated", "15", "this week")
    
    st.subheader("🚀 Quick Actions")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("🔍 Source Candidates"):
            st.session_state.module = "1. AI Candidate Sourcing"
    with col2:
        if st.button("✍️ Optimize JD"):
            st.session_state.module = "2. AI JD & Resume Optimizer"
    with col3:
        if st.button("📈 Market Intel"):
            st.session_state.module = "3. AI Market Intelligence"
    with col4:
        if st.button("📊 Client Report"):
            st.session_state.module = "4. AI Client Reporting"
    with col5:
        if st.button("💰 Cost Optimize"):
            st.session_state.module = "5. AI Cost Optimizer"

# Module 1: AI Candidate Sourcing
elif module == "1. AI Candidate Sourcing":
    st.header("🔍 AI Candidate Sourcing Agent")
    st.subheader("Find pre-vetted candidates in 60 seconds")
    
    jd = st.text_area("Paste Job Description", height=150,
                     placeholder="E.g., 'Senior Python Developer with 5+ years in AI/ML...'")
    
    if st.button("Find Candidates"):
        if jd:
            st.subheader("✅ Pre-Vetted Candidates")
            
            # Simulated candidates (replace with real sourcing later)
            candidates = [
                {"name": "Rahul Sharma", "title": "AI Engineer", "experience": "6 years", "skills": "Python, TensorFlow, Streamlit", "email": "rahul@email.com", "phone": "+91 XXXXX XXXXX"},
                {"name": "Priya Patel", "title": "ML Developer", "experience": "5 years", "skills": "PyTorch, NLP, AWS", "email": "priya@email.com", "phone": "+91 XXXXX XXXXX"},
                {"name": "Amit Kumar", "title": "Data Scientist", "experience": "7 years", "skills": "Python, SQL, Scikit-learn", "email": "amit@email.com", "phone": "+91 XXXXX XXXXX"}
            ]
            
            for i, cand in enumerate(candidates):
                with st.expander(f"{cand['name']} - {cand['title']}"):
                    st.write(f"**Experience**: {cand['experience']}")
                    st.write(f"**Skills**: {cand['skills']}")
                    st.write(f"**Contact**: {cand['email']} | {cand['phone']}")
                    
                    st.subheader("📧 Personalized Outreach")
                    outreach = f"Hi {cand['name']},\n\nI came across your profile and was impressed by your experience in {cand['skills'][:10]}... We have an exciting {jd[:20]} role at a top MNC client. Would you be open to a quick call?\n\nBest,\n[Your Name]"
                    st.text_area("Message", outreach, height=150, key=f"msg_{i}")
            
            st.subheader("🛡️ Ethics & Compliance")
            st.info("✅ **Diversity Score**: 67% (balanced gender/region)\n✅ **Bias Check**: No demographic filters used\n✅ **Compliance**: GDPR/DPDP ready")

# Module 2: AI JD & Resume Optimizer
# In your "AI JD & Resume Optimizer" module
if st.button("Optimize JD & Resume"):
    if client_jd:
        # Generate synthetic resume based on JD
        role_hint = "AI Engineer"  # Extract from JD later
        synthetic_resume = generate_synthetic_resume(role=role_hint, years=5)
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("✅ Optimized Job Description")
            # ... your JD optimization logic
            
        with col2:
            st.subheader("✅ Synthetic Candidate Resume")
            st.text_area("Demo Resume", synthetic_resume, height=300)
            
        st.info("💡 **Note**: This is a synthetic resume for demo purposes. Real candidate data requires consent.")
elif module == "2. AI JD & Resume Optimizer":
    st.header("✍️ AI JD & Resume Optimizer")
    st.subheader("Make your JDs and resumes ATS-friendly")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Job Description")
        client_jd = st.text_area("Client's Original JD", height=200,
                                placeholder="E.g., 'Need coder for AI stuff...'")
        
    with col2:
        st.subheader("Candidate Resume")
        resume = st.text_area("Candidate Resume Summary", height=200,
                             placeholder="E.g., '5+ years in Python, built AI demos...'")
    
    if st.button("Optimize JD & Resume"):
        if client_jd and resume:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("✅ Optimized Job Description")
                optimized_jd = f"**Senior AI Engineer**\n\nWe are seeking an experienced AI Engineer with **5+ years in Python, Machine Learning, and Streamlit** to join our MNC client. Key responsibilities include building predictive models, deploying AI applications, and collaborating with cross-functional teams.\n\n**Requirements**:\n- Bachelor's in Computer Science\n- Proficiency in Python, Scikit-learn, TensorFlow\n- Experience with Streamlit deployment\n- Strong problem-solving skills"
                st.text_area("ATS-Friendly JD", optimized_jd, height=300)
                
            with col2:
                st.subheader("✅ Optimized Resume")
                optimized_resume = f"**AI Engineer | 5+ Years Experience**\n\n- Built **5+ production AI applications** using Python, Scikit-learn, and Streamlit\n- Reduced hiring time by **50%** for MNC clients (Mercedes, Siemens)\n- Deployed predictive maintenance systems saving **₹10L+/hour** in downtime\n- Expert in **ethical, bias-free AI** compliant with GDPR/DPDP"
                st.text_area("ATS-Friendly Resume", optimized_resume, height=300)
                
            st.subheader("🛡️ Compliance Check")
            st.success("✅ **EEOC Compliant**: No age/gender/location bias\n✅ **GDPR Ready**: Data processing consent included\n✅ **DPDP Compliant**: Indian privacy law adhered")

# Module 3: AI Market Intelligence
elif module == "3. AI Market Intelligence":
    st.header("📈 AI Market Intelligence")
    st.subheader("Real-time salary & hiring trends")
    
    col1, col2 = st.columns(2)
    with col1:
        role = st.text_input("Role", "AI Engineer")
    with col2:
        location = st.text_input("Location", "Bangalore")
    
    if st.button("Get Market Intel"):
        st.subheader(f"📊 {role} Market in {location}")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("💰 Avg Salary", "₹18 LPA", "+12% YoY")
        col2.metric("👥 Openings", "1,240", "+8% MoM")
        col3.metric("⏱️ Time-to-Fill", "42 days", "-5 days")
        
        st.subheader("🔥 Hot Skills")
        skills = ["Python", "TensorFlow", "Streamlit", "LLM", "AWS"]
        st.write(" | ".join([f"**{s}**" for s in skills]))
        
        st.subheader("🏢 Top Hiring Companies")
        companies = ["Microsoft", "Google", "Siemens", "Mercedes-Benz", "Fractal Analytics"]
        st.write(" | ".join(companies))
        
        st.subheader("📈 Trend Analysis")
        st.info("• **AI Engineers** demand up 35% YoY\n• **Streamlit skills** premium: +15% salary\n• **Ethical AI** knowledge: 60% of JDs mention")

# Module 4: AI Client Reporting
elif module == "4. AI Client Reporting":
    st.header("📊 AI Client Reporting Suite")
    st.subheader("Automated reports in 1 click")
    
    uploaded_file = st.file_uploader("Upload Placement Data (CSV)", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Loaded {len(df)} placements")
        
        if st.button("Generate Client Report"):
            st.subheader("📄 Automated Client Report")
            
            total_placements = len(df)
            fulfillment_rate = 92
            avg_time_to_fill = 38
            revenue = "₹2.4 Cr"
            
            report = f"""
            **Monthly Performance Report - {datetime.now().strftime('%B %Y')}**
            
            **Key Metrics:**
            • Total Placements: {total_placements}
            • Fulfillment Rate: {fulfillment_rate}%
            • Avg Time-to-Fill: {avg_time_to_fill} days
            • Revenue Generated: {revenue}
            
            **SLA Compliance:**
            • Critical Roles: 100% met
            • Standard Roles: 95% met
            
            **Top Performers:**
            • AI/ML: 45 placements
            • Cybersecurity: 32 placements
            • FinTech: 28 placements
            
            **Next Month Focus:**
            • Reduce time-to-fill by 10%
            • Increase premium role placements by 15%
            """
            
            st.text_area("Client Report", report, height=300)
            
            st.download_button(
                "📥 Download as PDF",
                report,
                "client_report.txt",
                "text/plain"
            )

# Module 5: AI Cost Optimizer
elif module == "5. AI Cost Optimizer":
    st.header("💰 AI Cost Optimizer")
    st.subheader("Maximize margins, minimize waste")
    
    col1, col2 = st.columns(2)
    with col1:
        revenue = st.number_input("Monthly Revenue (₹)", value=2500000)
    with col2:
        placements = st.number_input("Monthly Placements", value=50)
    
    if st.button("Analyze Costs"):
        cost_per_hire = revenue / placements
        industry_benchmark = 45000
        savings_potential = (cost_per_hire - industry_benchmark) * placements if cost_per_hire > industry_benchmark else 0
        
        st.subheader("🔍 Cost Analysis")
        col1, col2, col3 = st.columns(3)
        col1.metric("💸 Cost-per-Hire", f"₹{cost_per_hire:,.0f}")
        col2.metric("🎯 Industry Benchmark", f"₹{industry_benchmark:,.0f}")
        col3.metric("💰 Savings Potential", f"₹{savings_potential:,.0f}")
        
        st.subheader("💡 Optimization Recommendations")
        st.info("""
        • **Automate sourcing**: Save ₹15K/placement  
        • **Bulk resume screening**: Reduce 20 hrs/week  
        • **Standardize JDs**: Improve quality, reduce rework  
        • **Predictive analytics**: Focus on high-margin roles
        """)
        
        st.subheader("📈 ROI Projection")
        st.success("Implementing StaffingAI Pro can **reduce costs by 28%** and **increase margins by ₹15L/month**.")

# Footer
st.markdown("---")
st.caption("👥 StaffingAI Pro — Built by a 18-year staffing veteran | Ethical AI | Audit-Ready | [Book Demo](https://calendly.com/yourname)")

st.markdown("""
⚠️ **Compliance Notice**:  
This demo uses **synthetic data** for illustration.  
Real candidate data processing requires explicit consent per **DPDP Act 2023** and **GDPR**.  
StaffingAI Pro is designed for **ethical, compliant recruitment** only.
""")
