# <p align="center">Simple Prompt Generator</p>
### <p align="center">A user-friendly tool for generating high-quality text prompts for AI image generation models like Midjourney, DALL-E, Stable Diffusion, and more. Our Hugging Face demo attracts over 2,500 users monthly!</p><br>

<div align="center">
    <img src='https://visitor-badge.laobi.icu/badge?page_id=WiNE-iNEFF.Simple_Prompt_Generator&left_color=red&right_color=green&left_text=Visitors' alt='visitor badge'>
    <img src="https://img.shields.io/github/downloads/WiNE-iNEFF/Simple_Prompt_Generator/total">
</div>

## Table of Contents
- [Quick Start](#quick-start)
- [Features](#features)
- [Examples](#examples)
- [Updates](#updates)
- [Support and Participation](#support-and-participation)
- [License](#license)

## Quick Start
To use the script from the command line, run:
```bash
python main.py -p "pr1.txt" -n 5 -a 2
```

### Parameters:
- `-p` or `--prompts`: Selects the prompt file. Choose between 'pr1.txt' (Prompt Generator v0.1 for better quality) or 'pr2.txt' (Prompt Generator v0.2 for more tags).
- `-n` or `--num`: Number of words in the prompt (default: 10, maximum: 20).
- `-a` or `--artists`: Number of artists to include in the prompt (default: 2).

Alternatively, try the generator through:
- [Website](https://wine-ineff.github.io/Simple_Prompt_Generator/): A web interface for easy prompt generation.
- [App](https://github.com/WiNE-iNEFF/Simple_Prompt_Generator/releases): Downloadable application for offline use.
- [Gradio Demo](https://huggingface.co/spaces/WiNE-iNEFF/HF_Simple_Prompt_Generator): Interactive demo on Hugging Face.
- [Colab Notebook](https://github.com/WiNE-iNEFF/Stable_Diffusion_colab): Run the generator in Google Colab.

## Features
- Easy-to-use interface for generating prompts.
- Supports multiple AI models like Midjourney, DALL-E, Stable Diffusion, Disco Diffusion, Flux, and more.
- Customizable prompt length and artist inclusion.
- Available as a web app, desktop app, Gradio demo, and Colab notebook.

## Examples
##### Version 0.1:
**Prompt**: `galaxy, art by ismail inceoglu, render, detailed, photorealistic, photorealistic dramatic anime boy, trending on pixiv, full hd, magic circle, landscape, photorealistic, sunsets, flowers, global illumination, block cities, digital painting, mirrors`

| Model                | Result             |
| -------------------- | ------------------ |
| Flux                 | ![](img/flux3.png) |
| Stable Diffusion 3.5 | ![](img/sd3.png)   |

**Prompt**: `by peter mohrbacher,  hdr, Sunsets, artstation, 4k 3d, by wayne barlowe,  rossdraws global illumination, terragen, hyper detailed, Animal T-Shirt Design, art by atey ghailan, battle field, epic, art by craig mullins, full hd, by craig mullins, Anime / Manga`

| Model | Result             |
| ----- | ------------------ |
| Flux  | ![](img/flux5.png) |

##### Version 0.2:
**Prompt**: `light painting, art by john kenn mortense, baroque, art nouveau, space, neon, telephoto, cyclic, art by lemma guya, radiant light, light nover, vray render, unreal engine, tornadic`

| Model                | Result             |
| -------------------- | ------------------ |
| Flux                 | ![](img/flux1.png) |
| Stable Diffusion 3.5 | ![](img/sd1.png)   |

**Prompt**: `by atey ghailan, cinematic, radiant light, rose, scrapbooking, by peter mohrbacher,  12-bit, flowers, postage stamp, post-apocalypse, character design, art by john Constable, fanbox`

| Model                | Result             |
| -------------------- | ------------------ |
| Flux                 | ![](img/flux2.png) |
| Stable Diffusion 3.5 | ![](img/sd2.png)   |

**Prompt**: `fanbox, drawing, 4-bit, wet paint, weta FX, by wlop, art by Ko Young Hoon, art by craig mullins, beautiful lighting, by hajime sorayama,  Octal, puffy paint, volumetric lighting, art by atey ghailan, tones of black, by Ralph Steadman, logo`

| Model                | Result             |
| -------------------- | ------------------ |
| Flux                 | ![](img/flux4.png) |
| Stable Diffusion 3.4 | ![](img/sd4.png)   |

For more examples, follow us on:
- [Instagram](https://www.instagram.com/wine_ineff)

## Updates
###### 08.02.25:
- New web application design for a better user experience.
###### 22.12.24:
- Updated "*README.md*".
- Added new examples for **Stable Diffusion 3.5** and **Flux.1**.
###### 01.04.23:
- Improved code and fixed bugs from the last update.
###### 19.02.23:
- Updated code and text prompts for better experiments.
- Added the ability to specify the number of artists in the prompt.
- Updated the website.
###### 12.02.23:
- Changed the website code for better usability on both PC and mobile devices.
- Removed some poor prompts in Prompt Generator v0.1.
- Added [Gradio page](https://huggingface.co/spaces/WiNE-iNEFF/HF_Simple_Prompt_Generator).

## Support and Participation
If you find this project helpful, please consider starring the repository or sharing it with others!

You can also support the development financially:

| Wallet       | Adress                                           |
| ------------ | ------------------------------------------------ |
| TON          | UQDXHLtVLfeMsUjk_XtvgEC6CYxo63ZkLOrrFlaAe2cGn3-Z |
| BTC          | 3KhWEKA2LpGeesshPCfgRRLsZuBHFtCnfU               |
| USDT (TRC20) | TGfzwpq2FhQbWisZMWyY98h2KgqV2JVjFH               |

## License
<p align="center">Licensed under MIT | Copyright Ⓒ 2022 Artsem Holub</p>


