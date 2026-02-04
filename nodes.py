import uuid
import folder_paths
from .acestep.handler import AceStepHandler
from .acestep.llm_inference import LLMHandler
from .acestep.inference import GenerationParams, GenerationConfig, generate_music, create_sample
import torchaudio
import os

class RunningHub_ACEStep_Loader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "llm type": (["acestep-5Hz-lm-1.7B", "acestep-5Hz-lm-4B"], {'default': "acestep-5Hz-lm-4B"}),
            }
        }

    RETURN_TYPES = ('ACEStepDit', 'ACEStepLLM', )
    RETURN_NAMES = ('ACE-Step Dit', 'ACE-Step LLM', )
    FUNCTION = "load"
    CATEGORY = "RunningHub/ACE-Step"

    def load(self, **kwargs):
        dit_handler = AceStepHandler()
        llm_handler = LLMHandler()
        llm_type = kwargs.get('llm type', "acestep-5Hz-lm-4B")
        print(llm_type)

        # 初始化服务
        dit_handler.initialize_service(
            project_root="/workspace/ComfyUI/models/ACE-Step",
            config_path="acestep-v15-turbo",
            device="cuda"
        )

        llm_handler.initialize(
            checkpoint_dir="/workspace/ComfyUI/models/ACE-Step",
            lm_model_path=llm_type,
            backend="vllm",
            device="cuda"
        )
        # component = {'dit_handler': dit_handler, 'llm_handler': llm_handler}
        return (dit_handler, llm_handler, )

class RunningHub_ACEStep_GenerationParams:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                'caption': ('STRING', {'default': "", 'multiline': True}),
                'lyrics': ('STRING', {'default': "", 'multiline': True}),
                'bpm': ('INT', {'default': 100, 'min': 30, 'max': 300}),
                'duration': ('FLOAT', {'default': 160, 'min': 10, 'max': 600}),
                'keyscale': ('STRING', {'default': "B minor", }),
                'timesignature': ('STRING', {'default': "4", }),
            }
        }
    
    RETURN_TYPES = ('ACEStepGenerationParams', )
    RETURN_NAMES = ('generation params', )
    FUNCTION = "generate"
    CATEGORY = "RunningHub/ACE-Step"

    def generate(self, **kwargs):
        caption = kwargs.get('caption', None)
        lyrics = kwargs.get('lyrics', None)
        bpm = kwargs.get('bpm', None)
        duration = kwargs.get('duration', None)
        keyscale = kwargs.get('keyscale', None)
        timesignature = kwargs.get('timesignature', None)
        params = GenerationParams(
            caption=caption,
            lyrics=lyrics,
            bpm=bpm,
            duration=duration,
            keyscale=keyscale,
            timesignature=timesignature,
        )
        return (params, )

class RunningHub_ACEStep_Creator:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # 'components': ('ACEStepComponent', ),
                'dit_handler': ('ACEStepDit', ),
                'llm_handler': ('ACEStepLLM', ),
                'params': ('ACEStepGenerationParams', ),
                'seed': ('INT', {'default': 42, 'min': 0, 'max': 4294967295}),
            }
        }

    RETURN_TYPES = ('AUDIO', )
    RETURN_NAMES = ('music', )
    FUNCTION = "generate"
    CATEGORY = "RunningHub/ACE-Step"

    def __init__(self):
        self.config = GenerationConfig(
            batch_size=1,
            audio_format="flac",
        )

    def generate(self, **kwargs):
        # components = kwargs.get('components', None)
        dit_handler = kwargs.get('dit_handler', None)
        llm_handler = kwargs.get('llm_handler', None)
        params = kwargs.get('params', None)
        seed = kwargs.get('seed', 42) ^ (2 ** 32)
        # dit_handler = components.get('dit_handler', None)
        # llm_handler = components.get('llm_handler', None)
        self.config.seeds = seed

        result = generate_music(dit_handler, llm_handler, params, self.config, save_dir=folder_paths.get_temp_directory())

        if result.success:
            for audio in result.audios:
                print(f"已生成：{audio['path']}")
                print(f"Key：{audio['key']}")
                print(f"Seed：{audio['params']['seed']}")
        else:
            raise RuntimeError(result.error)
        path = result.audios[0]['path']
        waveform, sample_rate = torchaudio.load(path)
        audio = {"waveform": waveform.unsqueeze(0), "sample_rate": sample_rate}

        return (audio, )

class RunningHub_ACEStep_Artist:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                'llm_handler': ('ACEStepLLM', ),
                'prompt': ('STRING', {'default': "", 'multiline': True}),
                'seed': ('INT', {'default': 42, 'min': 0, 'max': 4294967295}),
            }
        }

    RETURN_TYPES = ('ACEStepGenerationParams', )
    RETURN_NAMES = ('generation params', )
    FUNCTION = "generate"
    CATEGORY = "RunningHub/ACE-Step"

    def generate(self, **kwargs):
        llm_handler = kwargs.get('llm_handler', None)
        prompt = kwargs.get('prompt', None)
        result = create_sample(llm_handler, prompt)
        if result.success:
            caption = result.caption
            lyrics = result.lyrics
            bpm = result.bpm
            duration = result.duration
            keyscale = result.keyscale
            timesignature = result.timesignature
            params = GenerationParams(
                caption=caption,
                lyrics=lyrics,
                bpm=bpm,
                duration=duration,
                keyscale=keyscale,
                timesignature=timesignature,
            )
            return (params, )
        else:
            raise RuntimeError(result.error)

# class RunningHub_ACEStep_Coverist:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 # 'components': ('ACEStepComponent', ),
#                 'dit_handler': ('ACEStepDit', ),
#                 'llm_handler': ('ACEStepLLM', ),
#                 'caption': ('STRING', {'default': "", 'multiline': True}),
#                 'src_audio': ('AUDIO', ),
#                 'audio_cover_strength': ('FLOAT', {'default': 0.8, 'min': 0.0, 'max': 1.0}),
#                 'seed': ('INT', {'default': 42, 'min': 0, 'max': 4294967295}),
#             }
#         }
    
#     RETURN_TYPES = ('AUDIO', )
#     RETURN_NAMES = ('music', )
#     FUNCTION = "generate"
#     CATEGORY = "RunningHub/ACE-Step"
    
#     def __init__(self):
#         self.config = GenerationConfig(
#             batch_size=1,
#             audio_format="flac",
#         )

#     def generate(self, **kwargs):
#         dit_handler = kwargs.get('dit_handler', None)
#         llm_handler = kwargs.get('llm_handler', None)
#         caption = kwargs.get('caption', None)
#         src_audio = kwargs.get('src_audio', None)
#         tmp_audio_file = os.path.join(folder_paths.get_temp_directory(), f'{uuid.uuid4()}.flac')
#         torchaudio.save(tmp_audio_file, src_audio['waveform'].squeeze(0), src_audio['sample_rate'])
#         audio_cover_strength = kwargs.get('audio_cover_strength', 0.8)
#         params = GenerationParams(
#             task_type="cover",
#             src_audio=tmp_audio_file,
#             caption=caption,
#             audio_cover_strength=audio_cover_strength,
#         )
#         result = generate_music(dit_handler, llm_handler, params, self.config, save_dir=folder_paths.get_temp_directory())
#         if result.success:
#             for audio in result.audios:
#                 print(f"已生成：{audio['path']}")
#                 print(f"Key：{audio['key']}")
#                 print(f"Seed：{audio['params']['seed']}")
#         else:
#             raise RuntimeError(result.error)
#         return (result, )


NODE_CLASS_MAPPINGS = {
    "RunningHub ACE-Step Loader": RunningHub_ACEStep_Loader,
    "RunningHub ACE-Step GenerationParams": RunningHub_ACEStep_GenerationParams,
    "RunningHub ACE-Step Creator": RunningHub_ACEStep_Creator,
    "RunningHub ACE-Step Artist": RunningHub_ACEStep_Artist,
    # "RunningHub ACE-Step Coverist": RunningHub_ACEStep_Coverist,
}