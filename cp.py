# get file as first argument
# copy file to directory

# num=11

for num in range(1, 16):

    paragraphs = f"""

    <br><br><br>
    <section>

        <div class="container">
        <div class="columns is-centered has-text-centered"> 
        <h4 class="title is-4 mb-4">{num}번. 아래 영상들을 보고 가장 좋은 오디오를 골라주세요.</h4>
        </div>
        <div id="wrapper" style="display: flex; justify-content: space-around; align-items: flex-start; flex-wrap: wrap; text-align: center; gap: 20px; width: 60%; margin: auto;"> 
            <figure style="flex-basis: calc(30%); max-width: calc(30%);">
                it is finding your own voice where your own voice sits naturally and stably and healthily
            </figure>
            <figure style="flex-basis: calc(30%); max-width: calc(30%);">
                <video controls playsinline style="width: 100%; height: auto; object-fit: contain;"> 
                    <source type="video/mp4" src="video/automated_dub/row{num}/1_gt.mp4" /> 
                </video>
                <figcaption>input GT 영상</figcaption>
            </figure>
            <figure style="flex-basis: calc(30%); max-width: calc(30%);">
                <video controls playsinline style="width: 100%; height: auto; object-fit: contain;"> 
                    <source type="video/mp4" src="video/automated_dub/row{num}/3_hpm.mp4" /> 
                </video>
                <figcaption>1번 영상</figcaption>
            </figure>
            <figure style="flex-basis: calc(30%); max-width: calc(30%);">
                <video controls playsinline style="width: 100%; height: auto; object-fit: contain;"> 
                    <source type="video/mp4" src="video/automated_dub/row{num}/4_style.mp4" /> 
                </video>
                <figcaption>2번 영상</figcaption>
            </figure>
            <figure style="flex-basis: calc(30%); max-width: calc(30%);">
                <video controls playsinline style="width: 100%; height: auto; object-fit: contain;"> 
                    <source type="video/mp4" src="video/automated_dub/row{num}/ours_.mp4" /> 
                </video>
                <figcaption>3번 영상</figcaption>
            </figure>
            <figure style="flex-basis: calc(30%); max-width: calc(30%);">
                <video controls playsinline style="width: 100%; height: auto; object-fit: contain;"> 
                    <source type="video/mp4" src="video/automated_dub/row{num}/2_ours.mp4" /> 
                </video>
                <figcaption>4번 영상</figcaption>
            </figure>
        </div>
        <div class="box" style="padding: 1rem 1.25rem;">
            <p><b>가장 좋은 오디오를 가진 </b>영상을 하나 골라주세요.</p>
        <div class="question" style="padding: 0.3em 1.25rem; margin: 0;">
            <input type="radio" id="motion1_rank1" name="motion_rank1" value="1">
            <label for="motion1">1번 영상</label>
            <input type="radio" id="motion2_rank1" name="motion_rank1" value="2">
            <label for="motion2">2번 영상</label>
            <input type="radio" id="motion3_rank1" name="motion_rank1" value="3">
            <label for="motion3">3번 영상</label>
            <input type="radio" id="motion4_rank1" name="motion_rank1" value="4">
            <label for="motion4">4번 영상</label>
        </div>
        </section>

    """

    print(paragraphs)
