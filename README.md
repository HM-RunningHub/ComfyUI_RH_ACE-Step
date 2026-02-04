# ComfyUI_RH_ACE-Step

![License](https://img.shields.io/badge/License-Apache%202.0-green)

ComfyUI custom nodes for [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5) - the most powerful open-source music generation model. Generate AI music directly in ComfyUI with commercial-grade quality.

## ✨ Features

- **ACE-Step Model Loader** - Load ACE-Step DiT and LLM models
- **Generation Parameters** - Configure music generation settings (BPM, duration, key, time signature)
- **Music Creator** - Generate music from text descriptions and lyrics
- **Artist Node** - AI-powered lyrics and music composition assistant with 50+ language support

## 🛠️ Installation

1. Clone this repository into your ComfyUI custom_nodes folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/HM-RunningHub/ComfyUI_RH_ACE-Step.git
```

2. Restart ComfyUI

## 📦 Model Download & Installation

### Model Directory Structure

All models must be placed in `ComfyUI/models/ACE-Step/` with the following structure:

```
ComfyUI/
└── models/
    └── ACE-Step/
        ├── vae/                          # VAE model (required)
        ├── Qwen3-Embedding-0.6B/         # Text embedding model (required)
        ├── acestep-v15-turbo/            # DiT model (required)
        └── acestep-5Hz-lm-1.7B/          # LLM model (choose one)
        └── acestep-5Hz-lm-4B/            # LLM model (optional, better quality)
```

### Download Methods

#### Method 1: Download from HuggingFace (Recommended)

```bash
# Download main model package (includes all required models)
huggingface-cli download ACE-Step/Ace-Step1.5 --local-dir ComfyUI/models/ACE-Step

# Optional: Download 4B LLM model for better quality
huggingface-cli download ACE-Step/acestep-5Hz-lm-4B --local-dir ComfyUI/models/ACE-Step/acestep-5Hz-lm-4B
```

#### Method 2: Download from ModelScope (For China users)

```bash
# Install modelscope CLI
pip install modelscope

# Download main model
modelscope download --model ACE-Step/Ace-Step1.5 --local_dir ComfyUI/models/ACE-Step
```

#### Method 3: Manual Download

| Model | HuggingFace | Description |
|-------|-------------|-------------|
| **Main Package** | [ACE-Step/Ace-Step1.5](https://huggingface.co/ACE-Step/Ace-Step1.5) | Contains: vae, Qwen3-Embedding-0.6B, acestep-v15-turbo, acestep-5Hz-lm-1.7B |
| acestep-5Hz-lm-4B | [ACE-Step/acestep-5Hz-lm-4B](https://huggingface.co/ACE-Step/acestep-5Hz-lm-4B) | Large LLM model (4B params, best quality) |
| acestep-5Hz-lm-0.6B | [ACE-Step/acestep-5Hz-lm-0.6B](https://huggingface.co/ACE-Step/acestep-5Hz-lm-0.6B) | Lightweight LLM model (0.6B params, for low VRAM) |

### LLM Model Selection Guide

| Your GPU VRAM | Recommended LLM Model | Notes |
|---------------|----------------------|-------|
| **≤6GB** | None (DiT only) | LLM disabled to save memory |
| **6-12GB** | acestep-5Hz-lm-0.6B | Lightweight, good balance |
| **12-16GB** | acestep-5Hz-lm-1.7B | Better quality (default) |
| **≥16GB** | acestep-5Hz-lm-4B | Best quality |

## 🚀 Usage

### Example Workflow

Download the example workflow from [`workflows/example_workflow.json`](workflows/example_workflow.json) and import it into ComfyUI.

The example demonstrates two generation modes:

1. **Artist Mode** - Simple prompt: "一首中国风伤感恋爱歌曲" (A Chinese-style sad love song)
2. **Manual Mode** - Full control with custom caption, lyrics, BPM, duration, key, and time signature

### Basic Workflow

1. **Loader Node** - Load ACE-Step models (DiT + LLM)
   - Select LLM type: `acestep-5Hz-lm-1.7B` or `acestep-5Hz-lm-4B`
2. **GenerationParams Node** - Set music parameters:
   - Caption: Music style description
   - Lyrics: Song lyrics (with structure tags like `[Verse]`, `[Chorus]`)
   - BPM: Beats per minute (30-300)
   - Duration: Length in seconds (10-600)
   - Key Scale: Musical key (e.g., "B minor")
   - Time Signature: Beats per measure (e.g., "4")
3. **Creator Node** - Generate the music
4. **SaveAudio Node** - Save the generated audio

### Artist Mode

Use the **Artist Node** for AI-assisted composition:
- Input a simple prompt describing the song you want
- LLM automatically generates caption, lyrics, and music parameters
- Supports 50+ languages for vocals
- Optional instrumental mode (no vocals)

## 📝 Node Reference

| Node | Description |
|------|-------------|
| `RunningHub ACE-Step Loader` | Load DiT and LLM models |
| `RunningHub ACE-Step GenerationParams` | Manual parameter configuration |
| `RunningHub ACE-Step Creator` | Generate music from parameters |
| `RunningHub ACE-Step Artist` | AI-assisted music composition |

## 🌐 Supported Languages

Auto Detect, Arabic, Azerbaijani, Bengali, Bulgarian, Catalan, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian, Vietnamese, Cantonese, and more (50+ languages).

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [ACE-Step 1.5 Official](https://github.com/ace-step/ACE-Step-1.5) - Original ACE-Step project
- [HuggingFace Models](https://huggingface.co/ACE-Step) - Model downloads
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [RunningHub](https://runninghub.cn)

## 🙏 Acknowledgements

This project is based on [ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5), co-led by ACE Studio and StepFun.
