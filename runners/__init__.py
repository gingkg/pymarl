from .parallel_runner import ParallelRunner
from .episode_runner import EpisodeRunner


REGISTRY = dict()
REGISTRY["episode"] = EpisodeRunner
REGISTRY["parallel"] = ParallelRunner
