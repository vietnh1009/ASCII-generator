# [PYTHON] ASCII 生成器
语言：<a href="./README.md">English</a>｜中文

## [2024年11月22日] 对中国开发者社区的感谢

最近，这个Repo在版权问题上得到了中国开发者社区的保护和支持。特别感谢中国网民，以及整个中文社区。

## Introduction

这是我ASCII生成器的Python源代码，通过我的代码，你可以：
* **给定输入图像，我们可以生成以不同语言（.txt）存储在文本格式下的ASCII艺术**
* **给定输入图像，我们可以生成以不同语言（.png、.jpg...）存储在图像格式下的ASCII艺术。在每种格式中，我们有有2种选项：黑色背景和白色字符，反之亦然**
* **给定输入视频，我们可以生成以不同语言（.avi、.mp4...）存储在视频格式下的ASCII艺术**
* **视频/图像输出可以是灰度或彩色格式，由你随心而动**

## 多种语言转换
我们可以用不同语言的字符（英语、德语、法语、韩语、中文、日语等）生成ASCII艺术。以下是输出示例：
<p align="center">
  <img src="demo/english_output.jpg" width=800><br/>
  <i>英语</i>
</p>

<p align="center">
  <img src="demo/japanese_output.jpg" width=800><br/>
  <i>日语 (Dragon Ball)</i>
</p>

<p align="center">
  <img src="demo/german_output.jpg" width=800><br/>
  <i>德语</i>
</p>

<p align="center">
  <img src="demo/korean_output.jpg" width=800><br/>
  <i>韩语 (Dae Jang-geum)</i>
</p>

<p align="center">
  <img src="demo/french_output.jpg" width=800><br/>
  <i>法语</i>
</p>

<p align="center">
  <img src="demo/chinese_output.jpg" width=800><br/>
  <i>中文 (Actress)</i>
</p>

<p align="center">
  <img src="demo/spanish_output.jpg" width=800><br/>
  <i>西班牙语</i>
</p>

<p align="center">
  <img src="demo/russian_output.jpg" width=800><br/>
  <i>俄语</i>
</p>

## 视频到视频
通过以*背景*和*模式*的不同值运行脚本 **video2video_color.py**或**video2video.py**，我们将有以下不同的输出，例如：
<p align="center">
  <img src="demo/demo_complex_color_160.gif" width=800><br/>
  <i>着色复杂字符ASCII输出</i>
</p>

<p align="center">
  <img src="demo/demo_simple_white_150.gif" width=800><br/>
  <i>白色背景简单字符ASCII输出</i>
</p>

## 图像到文本
通过运行带有*模式*不同值的脚本 **img2txt.py**，我们将有以下不同的输出：
<p align="center">
  <img src="demo/input.jpg" width=800><br/>
  <i>输入图像</i>
</p>

<p align="center">
  <img src="demo/demo_image_simple.png" width=800><br/>
  <i>简单字符ASCII输出</i>
</p>

<p align="center">
  <img src="demo/demo_image_complex.png" width=800><br/>
  <i>复杂字符ASCII输出</i>
</p>

## 图像到图像
通过运行带有*背景*和*模式*不同值的脚本 **img2img_color.py**或**img2img.py**，我们将有以下不同的输出：
<p align="center">
  <img src="demo/input.jpg" width=800><br/>
  <i>输入图像</i>
</p>

<p align="center">
  <img src="demo/output_complex_color_200.jpg" width=800><br/>
  <i>着色复杂字符ASCII输出</i>
</p>

<p align="center">
  <img src="demo/output_simple_white_200.jpg" width=800><br/>
  <i>白色背景简单字符ASCII输出</i>
</p>

<p align="center">
  <img src="demo/output_simple_black_200.jpg" width=800><br/>
  <i>黑色背景简单字符ASCII输出</i>
</p>

<p align="center">
  <img src="demo/output_complex_white_200.jpg" width=800><br/>
  <i>白色背景复杂字符ASCII输出</i>
</p>

<p align="center">
  <img src="demo/output_complex_black_200.jpg" width=800><br/>
  <i>黑色背景复杂字符ASCII输出</i>
</p>

## 环境条件

* **python 3.6**
* **cv2**
* **PIL** 
* **numpy**
