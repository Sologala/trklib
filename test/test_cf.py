from matplotlib.font_manager import is_opentype_cff_font
import pyCFTrackers.cftracker.tracker_factory as tracker_factory
import argparse
import cv2
from tqdm import tqdm
selected_trackers = ["KCF_HOG", "STAPLE-CA"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("video", help="input video")
    parser.add_argument("--vis", help="show visualization", default=True)
    parser.add_argument("--start", help="start frame index ", default=0)
    parser.add_argument("--box", help="init box x,y,w,h", default="")
    args = parser.parse_args()

    trackers = [tracker_factory.PyTracker(
        trk_name) for trk_name in selected_trackers]

    init_box = args.box

    cap = cv2.VideoCapture()
    cap.open(args.video)
    if not cap.isOpened():
        print(f"open video {args.video} faild")
        exit(-1)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    h, w = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(
        cv2.CAP_PROP_FRAME_WIDTH))
    nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.set(cv2.CAP_PROP_POS_FRAMES, min(nframes, int(args.start)))
    _, img = cap.read()

    if init_box == "":
        init_box = cv2.selectROI("roi-seletect", img)
    else:
        init_box = [int(w) for w in init_box.split(',')]

    for trk in trackers:
        trk.init(img, init_box)

    for i in tqdm(range(1, nframes)):
        _, imgf = cap.read()
        for trk in trackers:
            img = imgf.copy()
            box = trk.track(img)
            imgshow = trk.drawVerbose(img, box)
            imgshow = cv2.resize(imgshow, None, fx=0.3, fy=0.3)
            cv2.imshow(f"{trk.tracker_type}", imgshow)
        cv2.waitKey(10)


if __name__ == "__main__":
    main()
