import streamlit as st
import time

# ----------------------------
# Gallery Data
# ----------------------------
gallery_items = [
    {"type": "image", "title": "Beautiful Mountain", "path": "assets/img.png"},
    {"type": "video", "title": "AI Robot Cooking", "path": "assets/Angry_Robot_Chef_Cooking_Entertainment_video_of_ai_robot.mp4"},
    {"type": "image", "title": "Sunset Beach", "path": "assets/img.png"},
    {"type": "video", "title": "Smart Kitchen Automation", "path": "assets/Angry_Robot_Chef_Cooking_Entertainment_video_of_ai_robot.mp4"},
    {"type": "image", "title": "City Lights", "path": "assets/img.png"},
]


# ----------------------------
# Config
# ----------------------------
st.set_page_config(page_title="Gallery", layout="wide")
st.title("📸 Gallery")


num_cols = 3  # Grid columns
fixed_width = 250
fixed_height = 250

# ----------------------------
# Shimmer Effect Function
# ----------------------------
def shimmer_placeholder():
    """Simulates shimmer loading placeholder"""
    placeholder = st.empty()
    with placeholder.container():
        for _ in range(2):  # 2 shimmer rows
            cols = st.columns(num_cols)
            for col in cols:
                with col:
                    st.markdown(
                        f"""
                        <div style="width:{fixed_width}px; height:{fixed_height}px; background: linear-gradient(
                            to right,
                            #e0e0e0 8%,
                            #f8f8f8 18%,
                            #e0e0e0 33%
                        );
                        background-size: 800px {fixed_height}px;
                        animation: shimmer 1.5s infinite linear;
                        border-radius: 10px;
                        margin-bottom: 8px;">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        "<div style='width:70%; height:15px; background:#e0e0e0; border-radius:5px;'></div>",
                        unsafe_allow_html=True,
                    )

                    # CSS for shimmer animation
                    st.markdown(
                        """
                        <style>
                        @keyframes shimmer {
                            0% { background-position: -800px 0; }
                            100% { background-position: 800px 0; }
                        }
                        </style>
                        """,
                        unsafe_allow_html=True,
                    )
    return placeholder

# ----------------------------
# Show Shimmer First
# ----------------------------
placeholder = shimmer_placeholder()

# Simulate loading time
time.sleep(2)

# ----------------------------
# Show Actual Gallery
# ----------------------------
placeholder.empty()  # Clear shimmer

for i in range(0, len(gallery_items), num_cols):
    cols = st.columns(num_cols)
    for col, item in zip(cols, gallery_items[i:i + num_cols]):
        with col:
            st.markdown(
                f"""
                <div style="width:{fixed_width}px; height:{fixed_height}px; overflow:hidden; border-radius:10px; border:1px solid #ddd; display:flex; align-items:center; justify-content:center;">
                """,
                unsafe_allow_html=True,
            )

            if item["type"] == "image":
                st.image(item["path"], width=fixed_width, use_container_width=False)
            elif item["type"] == "video":
                # Open video as binary to avoid path errors
                with open(item["path"], "rb") as video_file:
                    video_bytes = video_file.read()
                    st.video(video_bytes)

            st.markdown("</div>", unsafe_allow_html=True)
            st.caption(item["title"])