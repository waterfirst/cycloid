import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time


def cycloid(t, r):
    return r * (t - np.sin(t)), r * (1 - np.cos(t))


def create_cycloid_frame(t, r, color):
    fig, ax = plt.subplots(figsize=(10, 6))

    x, y = cycloid(t, r)
    ax.plot(x, y, color=color, linewidth=2, label="Cycloid")

    circle_x = r * t[-1]
    circle_y = r
    theta = np.linspace(0, 2 * np.pi, 50)
    ax.plot(
        circle_x + r * np.cos(theta), circle_y + r * np.sin(theta), "r-", linewidth=2
    )

    ax.plot(x[-1], y[-1], "ro", markersize=10)
    ax.plot([0, circle_x], [r, r], "g--", linewidth=1)

    ax.set_xlim(0, 4 * np.pi * r)
    ax.set_ylim(0, 2.2 * r)
    ax.set_aspect("equal")
    ax.set_title("Cycloid Animation")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True)

    return fig


st.title("Interactive Cycloid Animation")

st.header("Physical Significance and Applications of Cycloids")

st.write(
    """
사이클로이드는 수학적 아름다움 뿐만 아니라 물리학과 공학에서도 중요한 의미를 갖습니다:

1. 등시곡선 (Tautochrone curve): 
   사이클로이드는 중력 하에서 물체가 어느 지점에서 출발하든 같은 시간에 도착하는 특성을 가집니다. 
   이는 17세기 크리스티안 하위헌스가 발견했으며, 정확한 시계 제작에 큰 영향을 미쳤습니다.

2. 최속강하선 (Brachistochrone curve): 
   두 점 사이를 중력만으로 이동할 때 가장 빠른 경로가 사이클로이드입니다. 
   이는 요한 베르누이가 제안한 문제로, 뉴턴, 라이프니츠 등 당대 최고의 수학자들이 해결에 참여했습니다.

3. 기계 공학 응용:
   - 기어 설계: 사이클로이드 곡선은 일정한 속도비를 유지하는 기어 톱니 형상에 사용됩니다.
   - 캠 메커니즘: 부드러운 운동을 만들어내는 캠 설계에 활용됩니다.

4. 건축 및 예술:
   사이클로이드의 아치 형태는 건축물의 구조적 안정성과 미적 요소로 사용됩니다.

5. 우주 공학:
   위성 궤도 설계와 우주선의 귀환 경로 계산에 사이클로이드의 원리가 적용됩니다.

6. 광학:
   반사경 설계에 사이클로이드 곡선이 사용되어 빛의 효율적인 집중과 분산을 가능케 합니다.

이러한 다양한 응용은 사이클로이드가 단순한 수학적 호기심을 넘어 실제 세계의 문제 해결에 
중요한 역할을 한다는 것을 보여줍니다.
"""
)

st.header("Cycloid Animation")

r = st.sidebar.slider("Radius of the circle", 0.1, 2.0, 1.0, 0.1)
color = st.sidebar.color_picker("Color of the cycloid", "#0000FF")
speed = st.sidebar.slider("Animation speed", 30, 100, 60)

num_frames = 100
t_values = np.linspace(0, 4 * np.pi, num_frames)

if "frame" not in st.session_state:
    st.session_state.frame = 0

if "playing" not in st.session_state:
    st.session_state.playing = False

# Play/Pause 버튼
if st.button("Play/Pause"):
    st.session_state.playing = not st.session_state.playing
    st.session_state.frame = 0  # 재생 시 항상 처음부터 시작

# 프레임 표시 영역
frame_text = st.empty()

# 그래프 표시 영역
plot_placeholder = st.empty()

# 애니메이션 실행
while st.session_state.playing and st.session_state.frame < num_frames:
    t = t_values[: st.session_state.frame + 1]
    fig = create_cycloid_frame(t, r, color)
    plot_placeholder.pyplot(fig)
    plt.close(fig)

    frame_text.text(f"Frame: {st.session_state.frame+1}/{num_frames}")

    st.session_state.frame += 1
    time.sleep(1 / speed)

# 애니메이션이 끝나면 재생 상태를 False로 설정
if st.session_state.frame >= num_frames:
    st.session_state.playing = False

# 마지막 프레임 유지
if not st.session_state.playing and st.session_state.frame > 0:
    t = t_values[: st.session_state.frame]
    fig = create_cycloid_frame(t, r, color)
    plot_placeholder.pyplot(fig)
    plt.close(fig)
