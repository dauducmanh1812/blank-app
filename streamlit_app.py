import streamlit as st

# Set Streamlit page configuration for a wider layout and custom title
st.set_page_config(
    layout="centered",
    page_title="Will You Marry Me, Từ Thanh Hằng?",
    initial_sidebar_state="collapsed" # Hide sidebar for a cleaner look
)

# Custom CSS for styling the entire app, including Streamlit's internal elements
# This ensures the background, centering, and custom fonts are applied correctly.
st.markdown("""
    <style>
        /* Import Google Fonts for 'Inter' and 'Dancing Script' */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Dancing+Script:wght@700&display=swap');

        /* Ensure html and body take full viewport height and width, hide overflow */
        html, body {
            margin: 0;
            padding: 0;
            height: 100vh;
            width: 100vw;
            overflow: hidden; /* Hide overflow for heart animations */
        }

        /* Hide Streamlit's default header and toolbar for a cleaner look */
        [data-testid="stHeader"] {
            display: none !important;
        }
        [data-testid="stToolbar"] {
            display: none !important;
        }
        [data-testid="stDecoration"] { /* This often refers to the top bar/decoration */
            display: none !important;
        }
        [data-testid="stSidebar"] { /* In case it's not fully collapsed */
            display: none !important;
        }

        /* Target Streamlit's main app container to apply background and centering */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #fce4ec 0%, #ffebee 100%); /* Soft pink gradient */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            width: 100vw;
            overflow: hidden; /* Important for heart animations */
            padding: 0 !important; /* Remove default padding */
        }

        /* Target Streamlit's main vertical block container to center content */
        [data-testid="stVerticalBlock"] {
            display: flex;
            flex-direction: column; /* Ensure content stacks vertically */
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
        }

        /* Target Streamlit's element container within the vertical block for centering */
        /* This ensures the actual content within the block is centered */
        [data-testid="stVerticalBlock"] > div:first-child {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            padding: 1rem; /* Add some padding to prevent content from touching edges */
            box-sizing: border-box; /* Include padding in width/height */
        }

        /* Styling for the main proposal card container */
        .proposal-container {
            background-color: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px); /* Frosted glass effect */
            border-radius: 2rem; /* More rounded corners */
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15); /* Softer shadow */
            padding: 2.5rem; /* Increased padding for better spacing */
            text-align: center;
            max-width: 90%;
            width: 500px; /* Fixed width for larger screens */
            position: relative;
            z-index: 10; /* Ensure it's above the heart animations */
            animation: fadeInScale 1s ease-out forwards; /* Fade-in animation */
            margin: auto; /* Center the container itself */
        }

        /* Media query for smaller screens to adjust max-width and padding */
        @media (max-width: 600px) {
            .proposal-container {
                padding: 1.5rem; /* Smaller padding on mobile */
                width: 95%; /* Take more width on small screens */
            }
            .proposal-title {
                font-size: 2.5rem; /* Smaller title on mobile */
            }
            .proposal-message p {
                font-size: 1rem; /* Smaller text on mobile */
            }
            .proposal-message .text-2xl {
                font-size: 1.5rem; /* Adjust specific text size */
            }
            .proposal-message .text-3xl {
                font-size: 2rem; /* Adjust specific text size */
            }
            div.stButton > button {
                padding: 0.8rem 2rem; /* Smaller button padding */
                font-size: 1rem; /* Smaller button font */
            }
        }


        /* Keyframe animation for the proposal container fade-in */
        @keyframes fadeInScale {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        /* Styling for the main title "My Dearest Từ Thanh Hằng," */
        .proposal-title {
            font-family: 'Dancing Script', cursive; /* Elegant script font */
            color: #d81b60; /* Deep rose color */
            font-size: 3.5rem; /* Larger font size */
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1); /* Subtle text shadow */
        }

        /* Styling for the hidden proposal message */
        .proposal-message {
            color: #4a4a4a;
            font-size: 1.3rem;
            line-height: 1.6;
            margin-bottom: 2rem;
            opacity: 0; /* Hidden by default */
            transform: translateY(20px); /* Starts slightly below */
            transition: opacity 0.8s ease-out, transform 0.8s ease-out; /* Smooth transition */
        }

        /* Class to show the proposal message */
        .proposal-message.show {
            opacity: 1;
            transform: translateY(0);
        }

        /* Styling for the Streamlit button to match the original design */
        div.stButton > button {
            background: linear-gradient(45deg, #ff4081, #e91e63); /* Vibrant pink gradient */
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 9999px; /* Pill shape */
            font-size: 1.2rem;
            font-weight: bold;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease; /* Smooth transitions for hover/active */
            box-shadow: 0 8px 15px rgba(233, 30, 99, 0.4); /* Soft shadow */
            width: fit-content; /* Adjust width to content */
            margin: 0 auto; /* Center the button */
            display: block; /* Make it a block element to apply margin auto */
        }

        /* Hover effect for the button */
        div.stButton > button:hover {
            transform: translateY(-3px); /* Lift effect */
            box-shadow: 0 12px 20px rgba(233, 30, 99, 0.6); /* Enhanced shadow */
        }

        /* Active (click) effect for the button */
        div.stButton > button:active {
            transform: translateY(0); /* Return to original position */
            box-shadow: 0 5px 10px rgba(233, 30, 99, 0.3); /* Reduced shadow */
        }

        /* Container for the floating heart animations */
        .heart-animation-container {
            position: fixed; /* Fixed position to cover the whole viewport */
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none; /* Allows clicks to pass through */
            overflow: hidden;
            z-index: 1; /* Below the proposal container */
        }

        /* Styling for individual heart elements */
        .heart {
            position: absolute;
            background-color: #ff79b0; /* Lighter pink heart color */
            transform: rotate(-45deg); /* Rotate to form a heart shape */
            animation: floatUp 5s infinite ease-in-out; /* Floating animation */
            opacity: 0; /* Hidden initially */
            border-radius: 50% 50% 0 0; /* Creates the top rounded parts of the heart */
        }

        /* Pseudo-elements to complete the heart shape */
        .heart::before,
        .heart::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: inherit; /* Inherit background color */
            border-radius: 50%; /* Creates the side rounded parts */
        }

        .heart::before {
            left: -50%; /* Position to the left */
        }

        .heart::after {
            top: -50%; /* Position to the top */
        }

        /* Keyframe animation for hearts floating up */
        @keyframes floatUp {
            0% {
                transform: translateY(100vh) rotate(-45deg) scale(0); /* Starts from bottom, small */
                opacity: 0;
            }
            20% {
                opacity: 0.8; /* Fades in */
                transform: translateY(80vh) rotate(-45deg) scale(0.5);
            }
            100% {
                transform: translateY(-20vh) rotate(-45deg) scale(1.2); /* Floats up and out, larger */
                opacity: 0; /* Fades out */
            }
        }
    </style>
""", unsafe_allow_html=True) # unsafe_allow_html is necessary to inject custom HTML/CSS/JS

# Use Streamlit's session state to manage the visibility of the proposal message.
# This ensures the state persists across reruns caused by button clicks.
if 'revealed' not in st.session_state:
    st.session_state.revealed = False

# Heart animation container injected as raw HTML.
# JavaScript will dynamically add heart elements to this container.
st.markdown('<div class="heart-animation-container" id="heart-container"></div>', unsafe_allow_html=True)

# The main proposal content is wrapped in a div with the 'proposal-container' class.
# Using st.markdown to create this div allows for custom styling.
st.markdown('<div class="proposal-container">', unsafe_allow_html=True)

# Display the initial title using st.markdown with the custom class
st.markdown('<h1 class="proposal-title">My Dearest Từ Thanh Hằng,</h1>', unsafe_allow_html=True)

# Display the introductory message
st.markdown("""
    <p class="text-gray-600 text-lg mb-4">
        There are moments in life when words feel too small to express the depth of one's feelings.
        But I hope these words, from the bottom of my heart, convey everything.
    </p>
""", unsafe_allow_html=True)

# Conditionally display the "Reveal" button or the proposal message
if not st.session_state.revealed:
    # If the message hasn't been revealed, show the button.
    # When the button is clicked, it sets 'revealed' to True and reruns the app.
    if st.button("Click to Reveal My Heart"):
        st.session_state.revealed = True
        st.rerun() # Rerun the app to show the proposal message and trigger heart animation JS
else:
    # If the message has been revealed, display the proposal text.
    st.markdown("""
        <div id="proposalMessage" class="proposal-message show mt-8">
            <p class="text-xl font-semibold mb-4 text-pink-700">
                Every day with you is a blessing, a joy, and an adventure I cherish.
                You fill my life with laughter, warmth, and a love I never knew was possible.
            </p>
            
            <p class="text-3xl font-extrabold mt-6 text-pink-800">
                Anh yêu em, Từ Thanh Hằng!
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Inject JavaScript for the heart animation.
    # This script will only run when the 'revealed' state is True.
    # It checks if the interval is already set to prevent multiple animations.
    st.markdown(f"""
        <script>
            function createHeart() {{
                const heartContainer = document.getElementById('heart-container');
                if (!heartContainer) return; // Ensure the container exists

                const heart = document.createElement('div');
                heart.classList.add('heart');
                const size = Math.random() * 20 + 10; // Random size for hearts
                heart.style.width = size + 'px';
                heart.style.height = size + 'px';
                heart.style.left = (Math.random() * 100) + 'vw'; // Random horizontal starting position
                heart.style.animationDuration = (Math.random() * 3 + 4) + 's'; // Random animation duration
                heart.style.animationDelay = (Math.random() * 2) + 's'; // Random delay before animation starts
                heartContainer.appendChild(heart);

                // Remove heart element after its animation completes to prevent DOM clutter
                heart.addEventListener('animationend', () => {{
                    heart.remove();
                }});
            }}

            // Start the heart animation interval only if it's not already running.
            // This prevents multiple intervals from being created on Streamlit reruns.
            if (typeof window.heartInterval === 'undefined' || window.heartInterval === null) {{
                window.heartInterval = setInterval(createHeart, 300); // Create a new heart every 300 milliseconds
            }}
        </script>
    """, unsafe_allow_html=True)

# Close the proposal container div
st.markdown('</div>', unsafe_allow_html=True)
