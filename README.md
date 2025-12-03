# [PYTHON] ASCII generator

## [22/11/2024] A thank you to the Chinese community

Recently, this repository has been protected and supported by the Chinese community in relation to a copyright issue. A million thanks to Chinese netizens in particular, and the Chinese community in general

## Introduction

Here is my python source code for ASCII generator. With my code: 
* **Given input image, we could generate ASCII art stored under text format in different languages (.txt)**
* **Given input image, we could generate ASCII art stored under image formats in different languages (.png, .jpg, ...). In each format, there are 2 options: Black background and white characters, or vice versa**
* **Given input video, we could generate ASCII art stored under video formats in different languages (.avi, .mp4, ...)**
* **Video/image outputs could be in grayscale or color format. It is totally up to you**

## Multiple Language Conversion
We could generate ASCII art with different alphabets (english, german, french, korean, chinese, japanese, ...). Below are example output:
<p align="center">
  <img src="demo/english_output.jpg" width=800><br/>
  <i>English</i>
</p>

<p align="center">
  <img src="demo/japanese_output.jpg" width=800><br/>
  <i>Japanese (Dragon Ball)</i>
</p>

<p align="center">
  <img src="demo/german_output.jpg" width=800><br/>
  <i>German</i>
</p>

<p align="center">
  <img src="demo/korean_output.jpg" width=800><br/>
  <i>Korean (Dae Jang-geum)</i>
</p>

<p align="center">
  <img src="demo/french_output.jpg" width=800><br/>
  <i>French</i>
</p>

<p align="center">
  <img src="demo/chinese_output.jpg" width=800><br/>
  <i>Chinese (Actress)</i>
</p>

<p align="center">
  <img src="demo/spanish_output.jpg" width=800><br/>
  <i>Spanish</i>
</p>

<p align="center">
  <img src="demo/russian_output.jpg" width=800><br/>
  <i>Russian</i>
</p>

## Video to video
By running the sript **video2video_color.py** or **video2video.py** with different values for *background* and *mode*, we will have different outputs, for example:
<p align="center">
  <img src="demo/demo_complex_color_160.gif" width=800><br/>
  <i>Colored complex-character ASCII output</i>
</p>

<p align="center">
  <img src="demo/demo_simple_white_150.gif" width=800><br/>
  <i>White-background simple-character ASCII output</i>
</p>

## Image to text
By running the sript **img2txt.py** with different values for *mode*, we will have following outputs:
<p align="center">
  <img src="demo/input.jpg" width=800><br/>
  <i>Input image</i>
</p>

<p align="center">
  <img src="demo/demo_image_simple.png" width=800><br/>
  <i>Simple character ASCII output</i>
</p>

<p align="center">
  <img src="demo/demo_image_complex.png" width=800><br/>
  <i>Complex character ASCII output</i>
</p>

## Image to image
By running the sript **img2img_color.py** or **img2img.py** with different values for *background* and *mode*, we will have following outputs:
<p align="center">
  <img src="demo/input.jpg" width=800><br/>
  <i>Input image</i>
</p>

<p align="center">
  <img src="demo/output_complex_color_200.jpg" width=800><br/>
  <i>Colored complex-character ASCII output</i>
</p>

<p align="center">
  <img src="demo/output_simple_white_200.jpg" width=800><br/>
  <i>White-background simple-character ASCII output</i>
</p>

<p align="center">
  <img src="demo/output_simple_black_200.jpg" width=800><br/>
  <i>Black-background simple-character ASCII output</i>
</p>

<p align="center">
  <img src="demo/output_complex_white_200.jpg" width=800><br/>
  <i>White-background complex-character ASCII output</i>
</p>

<p align="center">
  <img src="demo/output_complex_black_200.jpg" width=800><br/>
  <i>Black-background complex-character ASCII output</i>
</p>

## Requirements

* **Python 3.6+**
* **opencv-python**
* **Pillow** 
* **numpy**

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/uvipen/ASCII-generator.git
cd ASCII-generator
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Image to Text (ASCII .txt output)
```bash
python img2txt.py --input data/input.jpg --output output/result.txt --mode complex --num_cols 150
```

**Arguments:**
| Argument | Default | Description |
|----------|---------|-------------|
| `--input` | `data/input.jpg` | Path to input image |
| `--output` | `data/output.txt` | Path to output text file |
| `--mode` | `complex` | `simple` (10 chars) or `complex` (70 chars) |
| `--num_cols` | `150` | Number of characters for output width |

---

### Image to Image (ASCII .jpg/.png output)

**Grayscale:**
```bash
python img2img.py --input data/input.jpg --output output/result.jpg --background black --num_cols 300
```

**Color:**
```bash
python img2img_color.py --input data/input.jpg --output output/result.jpg --background black --num_cols 300 --language english
```

**Arguments:**
| Argument | Default | Description |
|----------|---------|-------------|
| `--input` | `data/input.jpg` | Path to input image |
| `--output` | `data/output.jpg` | Path to output image |
| `--language` | `english` | Language alphabet (english, german, french, korean, chinese, japanese, russian, spanish, etc.) |
| `--mode` | `standard` | Character mode |
| `--background` | `black` | `black` or `white` background |
| `--num_cols` | `300` | Number of characters for output width |
| `--scale` | `2` | Upscale output (only in color version) |

---

### Video to Video (ASCII .mp4/.avi output)

**Grayscale:**
```bash
python video2video.py --input data/input.mp4 --output output/result.mp4 --mode simple --background white --num_cols 100
```

**Color:**
```bash
python video2video_color.py --input data/input.mp4 --output output/result.mp4 --mode complex --background black --num_cols 100
```

**Arguments:**
| Argument | Default | Description |
|----------|---------|-------------|
| `--input` | `data/input.mp4` | Path to input video |
| `--output` | `data/output.mp4` | Path to output video |
| `--mode` | `simple`/`complex` | `simple` (10 chars) or `complex` (70 chars) |
| `--background` | `white`/`black` | `black` or `white` background |
| `--num_cols` | `100` | Number of characters for output width |
| `--scale` | `1` | Upscale output |
| `--fps` | `0` | Frame rate (0 = use original) |
| `--overlay_ratio` | `0.2` | Size of original video overlay (0 to disable) |

## Examples

```bash
# Simple black & white ASCII from image
python img2img.py --input my_photo.jpg --output ascii_photo.png --background white --num_cols 200

# Colorful Japanese ASCII art
python img2img_color.py --input anime.jpg --output anime_ascii.jpg --language japanese --num_cols 400

# Convert a video with color ASCII
python video2video_color.py --input video.mp4 --output ascii_video.avi --num_cols 150 --overlay_ratio 0.15
```
