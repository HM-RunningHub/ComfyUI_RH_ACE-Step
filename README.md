# ComfyUI_RH_ACE-Step

![License](https://img.shields.io/badge/License-Apache%202.0-green)

ComfyUI custom nodes for [ACE-Step](https://github.com/ace-step/ACE-Step) music generation model, enabling AI-powered music creation within ComfyUI.

## ✨ Features

- **ACE-Step Model Loader** - Load ACE-Step DiT and LLM models
- **Generation Parameters** - Configure music generation settings (BPM, duration, key, time signature)
- **Music Creator** - Generate music from text descriptions and lyrics
- **Artist Node** - AI-powered lyrics and music composition assistant with multi-language support

## 🛠️ Installation

1. Clone this repository into your ComfyUI custom_nodes folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/HM-RunningHub/ComfyUI_RH_ACE-Step.git
```

2. Restart ComfyUI

## 📦 Model Download

Download ACE-Step models and place them in `ComfyUI/models/ACE-Step/`:

- ACE-Step DiT model: `acestep-v15-turbo`
- ACE-Step LLM model: `acestep-5Hz-lm-1.7B` or `acestep-5Hz-lm-4B`

Model download link: [ACE-Step Official Repository](https://github.com/ace-step/ACE-Step)

## 🚀 Usage

### Basic Workflow

1. **Loader Node** - Load ACE-Step models (DiT + LLM)
2. **GenerationParams Node** - Set music parameters:
   - Caption: Music style description
   - Lyrics: Song lyrics
   - BPM: Beats per minute (30-300)
   - Duration: Length in seconds (10-600)
   - Key Scale: Musical key (e.g., "B minor")
   - Time Signature: Beats per measure (e.g., "4")
3. **Creator Node** - Generate the music

### Artist Mode

Use the **Artist Node** for AI-assisted composition:
- Input a simple prompt
- LLM generates caption, lyrics, and music parameters automatically
- Supports 50+ languages for vocals

## 📝 Node Reference

| Node | Description |
|------|-------------|
| `RunningHub ACE-Step Loader` | Load DiT and LLM models |
| `RunningHub ACE-Step GenerationParams` | Manual parameter configuration |
| `RunningHub ACE-Step Creator` | Generate music from parameters |
| `RunningHub ACE-Step Artist` | AI-assisted music composition |

## 🌐 Supported Languages

Auto Detect, Arabic, Azerbaijani, Bengali, Bulgarian, Catalan, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian, Vietnamese, and more.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [ACE-Step Official](https://github.com/ace-step/ACE-Step)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [RunningHub](https://runninghub.cn)
