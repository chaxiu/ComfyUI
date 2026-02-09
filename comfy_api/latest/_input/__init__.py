from .basic_types import ImageInput, AudioInput, MaskInput, LatentInput
import importlib.util

_VIDEO_AVAILABLE = importlib.util.find_spec("av") is not None
if _VIDEO_AVAILABLE:
    from .video_types import VideoInput

__all__ = [
    "ImageInput",
    "AudioInput",
    "MaskInput",
    "LatentInput",
]
if _VIDEO_AVAILABLE:
    __all__.append("VideoInput")
