from enum import Enum
from typing import Any, Protocol, TypedDict, TypeGuard

import numpy as np
import numpy.typing as npt
from pydantic import BaseModel


class StrEnum(str, Enum):
    value: str

    def __str__(self) -> str:
        return self.value


class TextResponse(BaseModel):
    __root__: str


class MessageResponse(BaseModel):
    message: str


class BoundingBox(TypedDict):
    x1: int
    y1: int
    x2: int
    y2: int


class ModelType(StrEnum):
    CLIP = "clip"
    FACIAL_RECOGNITION = "facial-recognition"
    WEAPONS_DETECTION = "weapons-detection"


class ModelRuntime(StrEnum):
    ONNX = "onnx"
    ARMNN = "armnn"


class HasProfiling(Protocol):
    profiling: dict[str, float]


class Face(TypedDict):
    boundingBox: BoundingBox
    embedding: npt.NDArray[np.float32]
    imageWidth: int
    imageHeight: int
    score: float

# class DetectedWeapons(TypedDict):
#     image: str
#     score: float

class DetectedWeapons(TypedDict):
    filePath: str

def has_profiling(obj: Any) -> TypeGuard[HasProfiling]:
    return hasattr(obj, "profiling") and isinstance(obj.profiling, dict)


def is_ndarray(obj: Any, dtype: "type[np._DTypeScalar_co]") -> "TypeGuard[npt.NDArray[np._DTypeScalar_co]]":
    return isinstance(obj, np.ndarray) and obj.dtype == dtype
