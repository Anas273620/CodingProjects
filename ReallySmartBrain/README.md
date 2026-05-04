# ReallySmartBrain

Image classification demo using ImageAI with a MobileNetV2 model.

## Features

- Loads pretrained MobileNetV2 weights
- Classifies a local image
- Prints predictions with confidence scores

## Files

- `brain.py` — main inference script
- `mobilenet_v2-b0353104.pth` — model weights
- Sample images: `godzilla.jpg`, `house.jpg`, `giraffe.jpg`

## Run

```bash
cd ReallySmartBrain
python brain.py
```

## Notes

- Update `brain.py` to switch input image or result count.
