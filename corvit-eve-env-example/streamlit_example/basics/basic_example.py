import streamlit as st
#library for img
from PIL import Image
##title



## shimmer affact on video laoding
import time
import os

placeholder = st.empty()  # Create a placeholder for shimmer

# --- Shimmer CSS ---
shimmer_css = """
<style>
@keyframes shimmer {
  0% {
    background-position: -1000px 0;
  }
  100% {
    background-position: 1000px 0;
  }
}
.shimmer {
  width: 100%;
  height: 250px;
  border-radius: 12px;
  background: linear-gradient(
    to right,
    #eeeeee 8%,
    #dddddd 18%,
    #eeeeee 33%
  );
  background-size: 1000px 104px;
  animation: shimmer 2s infinite linear;
}
</style>
<div class="shimmer"></div>
"""

# Show shimmer first
placeholder.markdown(shimmer_css, unsafe_allow_html=True)

# Simulate video loading
time.sleep(3)  # Replace this with actual video loading process

# Clear shimmer and load video
video_path = os.path.join("assets", "Angry_Robot_Chef_Cooking_Entertainment_video_of_ai_robot.mp4")
with open(video_path, "rb") as video_file:
    placeholder.video(video_file,width=300)
st.title("Hello Fahad AI Engineer")

st.success('WelCome Dev!....')


#alret error
st.error("I think you missed the old code....")

#write
st.write("Please Enter")


#check box
st.header('Check box')

if st.checkbox('Show/Hide'):
    st.success('Subscribe')
else:
    st.warning('Not Subscribe yet')


# radio button
st.header('Radio button example')
course=st.radio('Select Course',('AI','Flutter'))

if course == 'AI':
    st.success("Welcome in AI ")
else:
    st.warning("Its not update")





# image
st.title('Asset Image')
img=Image.open('assets/img.png')
st.image(img)



# # Network image
st.header('Network Image')
st.image("https://i.pinimg.com/736x/70/7c/85/707c85fdd3cadf5a182ffda907c54576.jpg",  caption="Network Image",
         width=300
         # use_container_width=True
         )


#Video
st.video("assets/Angry_Robot_Chef_Cooking_Entertainment_video_of_ai_robot.mp4",width=250,)


##selected option
st.write()
